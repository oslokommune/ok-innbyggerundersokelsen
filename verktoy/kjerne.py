"""Innlesing og endringsdeteksjon for dokumentasjonen av innbyggerundersøkelsen.

Bærende prinsipp: endringer mellom utgaver UTLEDES her, de lagres aldri. Det som lagres, er
spørreskjemaet per utgave (data/skjema/) og den redaksjonelle dommen (data/vurderinger.yaml).
Da kan det ikke oppstå to sannheter som drifter fra hverandre.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

ROT = Path(__file__).resolve().parents[1]
DATA = ROT / "data"
SKJEMA = ROT / "skjema"
DOCS = ROT / "docs"

# Feltene i et spørsmål som beskriver hvordan det ble stilt. Endres ett av dem, skal det
# stå i endringsloggen for overgangen.
SKJEMAFELT = ("innledning", "instruksjon", "ledd_tekst", "svartype", "svaralternativer", "ikke_sikker_kode", "filter")

# Norske etiketter for DDI-kodene og de andre kodelistene i data/utgaver.yaml.
ETIKETTER = {
    "Probability.Stratified.Disproportional": "Sannsynlighetsutvalg: stratifisert, disproporsjonalt",
    "Probability.Stratified.Proportional": "Sannsynlighetsutvalg: stratifisert, proporsjonalt",
    "SelfAdministeredQuestionnaire.Paper": "papir",
    "SelfAdministeredQuestionnaire.CAWI": "nett",
    "Interview.Telephone.CATI": "telefon",
    "Interview.FaceToFace.CAPIorCAMI": "personlig intervju",
    "Individual": "Individ",
    "CrossSection": "Tverrsnitt",
    "Longitudinal.TrendRepeatedCrossSection": "Trend (gjentatt tverrsnitt)",
    "selvrapportert": "selvrapportert",
    "register": "register",
    "ikke_oppgitt": "ikke oppgitt",
    "ja": "Ja",
    "med_forbehold": "Med forbehold",
    "nei": "Nei",
}


def etikett(kode) -> str:
    return ETIKETTER.get(kode, str(kode))


def modusfordeling(utgave: dict) -> str:
    """«papir 52 %, nett 48 %»: andelen svar per modus, regnet av antallene i data."""
    per: dict[str, int] = {}
    for m in utgave["innsamling"]["modus"]:
        if m["antall"] is None:
            return ", ".join(sorted({etikett(x["kode"]) for x in utgave["innsamling"]["modus"]}))
        per[etikett(m["kode"])] = per.get(etikett(m["kode"]), 0) + m["antall"]
    total = sum(per.values())
    return ", ".join(f"{k} {round(100 * v / total)} %" for k, v in sorted(per.items(), key=lambda kv: -kv[1]))


# Metodefelt som sammenlignes mellom to utgaver: (navn, funksjon som henter verdien).
METODEFELT = (
    ("Målgruppe", lambda u: u["malgruppe"]["beskrivelse"]),
    ("Leverandør", lambda u: u["oppdrag"]["leverandor"]),
    ("Svar per innsamlingsmodus", modusfordeling),
    ("Årstid for feltarbeidet", lambda u: u["feltperiode"]["arstid"]),
    ("Vektet etter", lambda u: ", ".join(u["vekting"]["variabler"])),
    ("Kilde til landbakgrunn", lambda u: etikett(u["landbakgrunn"]["type"])),
)


class _Laster(yaml.SafeLoader):
    """SafeLoader som lar datoer være tekst («2026-09-23»), slik at data og generert
    dokumentasjon viser det samme som står i fila."""


_Laster.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def les_yaml(sti: Path) -> dict:
    with sti.open(encoding="utf-8") as f:
        return yaml.load(f, Loader=_Laster) or {}


def les_kilder() -> dict:
    return les_yaml(DATA / "kilder.yaml")


def kildeindeks() -> dict[str, dict]:
    return {k["id"]: k for k in les_kilder().get("kilder") or []}


def les_utgaver() -> dict:
    return les_yaml(DATA / "utgaver.yaml")


def utgaveliste() -> list[dict]:
    """Utgavene sortert kronologisk."""
    return sorted(les_utgaver().get("utgaver") or [], key=lambda u: u["aar"])


def les_konsepter() -> dict[str, dict]:
    return {k["id"]: k for k in les_yaml(DATA / "konsepter.yaml").get("konsepter") or []}


def skjemafiler() -> list[Path]:
    katalog = DATA / "skjema"
    return sorted(katalog.glob("*.yaml")) if katalog.is_dir() else []


def les_skjema() -> dict[str, dict]:
    """{utgave: innholdet i data/skjema/<utgave>.yaml}, kronologisk."""
    ut = {}
    for sti in skjemafiler():
        data = les_yaml(sti)
        ut[str(data.get("utgave") or sti.stem)] = data
    return dict(sorted(ut.items()))


def les_vurderinger() -> list[dict]:
    return les_yaml(DATA / "vurderinger.yaml").get("vurderinger") or []


def tekst(verdi) -> str | None:
    """Et tekstfelt kan være én streng eller en liste med linjer (underoverskrift og stamme)."""
    if verdi is None:
        return None
    if isinstance(verdi, list):
        return " / ".join(verdi)
    return verdi


def _sammenlign(verdi):
    """Sammenligningsform: bare mellomrom normaliseres. Tegnsetting og store/små bokstaver
    teller, fordi ordlyden skal være ordrett."""
    if isinstance(verdi, str):
        return re.sub(r"\s+", " ", verdi).strip()
    if isinstance(verdi, list):
        return [_sammenlign(v) for v in verdi]
    return verdi


def ikke_sikker_kode(post: dict) -> int | None:
    """Koden for «Ikke sikker» slik den står i skjemaet (None = ikke trykt/programmert)."""
    for alt in post.get("svaralternativer") or []:
        if (alt.get("tekst") or "").strip().lower() == "ikke sikker":
            return alt.get("kode")
    return None


def skjemaverdi(post: dict, felt: str):
    if felt == "ikke_sikker_kode":
        return ikke_sikker_kode(post)
    if felt in ("innledning", "instruksjon"):
        return _sammenlign(tekst(post.get(felt)))
    if felt == "svaralternativer":
        return [(a.get("kode"), _sammenlign(a.get("tekst"))) for a in post.get(felt) or []]
    return _sammenlign(post.get(felt))


def sporsmal_per_konsept(skjema: dict[str, dict] | None = None) -> dict[str, list[tuple[str, dict]]]:
    """{konsept: [(utgave, spørsmål), ...]} kronologisk."""
    skjema = les_skjema() if skjema is None else skjema
    ut: dict[str, list[tuple[str, dict]]] = {}
    for utgave, data in skjema.items():
        for post in data.get("sporsmal") or []:
            ut.setdefault(post["konsept"], []).append((utgave, post))
    return ut


@dataclass(frozen=True)
class Endring:
    konsept: str
    fra_utgave: str
    til_utgave: str
    felt: str
    fra_verdi: object
    til_verdi: object


def overganger(serie: list[tuple[str, dict]]) -> list[tuple[tuple[str, dict], tuple[str, dict]]]:
    return list(zip(serie, serie[1:]))


def finn_skjemaendringer(konsept: str, serie: list[tuple[str, dict]]) -> list[Endring]:
    endringer = []
    for (fra, a), (til, b) in overganger(serie):
        for felt in SKJEMAFELT:
            va, vb = skjemaverdi(a, felt), skjemaverdi(b, felt)
            if va != vb:
                endringer.append(Endring(konsept, fra, til, felt, va, vb))
    return endringer


def finn_metodeendringer(fra: dict, til: dict) -> list[tuple[str, str, str]]:
    ut = []
    for navn, hent in METODEFELT:
        va, vb = hent(fra), hent(til)
        if va != vb:
            ut.append((navn, va, vb))
    return ut


def vurderingsindeks(vurderinger: list[dict]) -> dict[tuple[str, str, str], dict]:
    return {(v["konsept"], str(v["fra_utgave"]), str(v["til_utgave"])): v for v in vurderinger}


def kilderefs(node, sti: str = ""):
    """Alle kildehenvisninger i en datastruktur: (sti, id). En henvisning er en mapping med
    `id` under en nøkkel som heter kilde, kilde_tillegg, sporreskjema eller i lista grunnlag."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("kilde", "kilde_tillegg", "sporreskjema") and isinstance(v, dict) and "id" in v:
                yield f"{sti}/{k}", v["id"]
            elif k == "grunnlag" and isinstance(v, list):
                for i, g in enumerate(v):
                    if isinstance(g, dict) and "id" in g:
                        yield f"{sti}/{k}/{i}", g["id"]
            else:
                yield from kilderefs(v, f"{sti}/{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from kilderefs(v, f"{sti}/{i}")
