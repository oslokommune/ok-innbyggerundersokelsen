"""Valider data/ mot skjema/ og mot seg selv.

Kjøres i CI og før commit. Exit 0 = alt i orden, exit 1 = feil.
Advarsler feiler ikke bygget, men vises. Med --streng blir advarsler til feil.

    python verktoy/validering.py [--streng]
"""

from __future__ import annotations

import datetime as dt
import json
import sys

import kjerne

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    Draft202012Validator = None


def _vis(sti) -> str:
    try:
        return sti.relative_to(kjerne.ROT).as_posix()
    except ValueError:
        return sti.name


def valider() -> tuple[list[str], list[str]]:
    feil: list[str] = []
    advarsler: list[str] = []

    # --- JSON Schema -------------------------------------------------------------------
    filer = [
        (kjerne.DATA / "kilder.yaml", "kilder.schema.json"),
        (kjerne.DATA / "utgaver.yaml", "utgaver.schema.json"),
        (kjerne.DATA / "konsepter.yaml", "konsepter.schema.json"),
        (kjerne.DATA / "vurderinger.yaml", "vurderinger.schema.json"),
    ] + [(sti, "sporreskjema.schema.json") for sti in kjerne.skjemafiler()]
    if Draft202012Validator is None:
        advarsler.append("jsonschema er ikke installert, så skjemavalideringen er hoppet over")
    else:
        for sti, skjemanavn in filer:
            skjema = json.loads((kjerne.SKJEMA / skjemanavn).read_text(encoding="utf-8"))
            for f in sorted(Draft202012Validator(skjema).iter_errors(kjerne.les_yaml(sti)), key=lambda e: list(e.path)):
                plass = "/".join(str(p) for p in f.path) or "(rot)"
                feil.append(f"{_vis(sti)}: {plass}: {f.message}")
    if feil:
        return feil, advarsler  # kryssjekkene under forutsetter at strukturen er riktig

    kilder = kjerne.kildeindeks()
    utgaver = kjerne.utgaveliste()
    utgave_ider = [u["id"] for u in utgaver]
    historikk = {str(h["aar"]) for h in kjerne.les_utgaver().get("historikk") or []}
    konsepter = kjerne.les_konsepter()
    skjema = kjerne.les_skjema()
    vurderinger = kjerne.les_vurderinger()

    # --- Kildehenvisninger -------------------------------------------------------------
    if len(kilder) != len(kjerne.les_kilder()["kilder"]):
        feil.append("data/kilder.yaml: samme id brukt flere ganger")
    for navn, innhold in [("utgaver.yaml", kjerne.les_utgaver()), ("vurderinger.yaml", {"v": vurderinger})] + [
        (f"skjema/{u}.yaml", d) for u, d in skjema.items()
    ]:
        for sti, kid in kjerne.kilderefs(innhold):
            if kid not in kilder:
                feil.append(f"data/{navn}: {sti}: ukjent kilde '{kid}'")
    for utgave, data in skjema.items():
        if data["sporreskjema"] not in kilder:
            feil.append(f"data/skjema/{utgave}.yaml: ukjent kilde '{data['sporreskjema']}'")

    # --- Utgavene ----------------------------------------------------------------------
    if len(set(utgave_ider)) != len(utgave_ider):
        feil.append("data/utgaver.yaml: samme utgave-id brukt flere ganger")
    for u in utgaver:
        hvor = f"data/utgaver.yaml: {u['id']}"
        if u["id"] != str(u["aar"]):
            feil.append(f"{hvor}: id og aar er ulike")
        for s in u["sammenligner_med"]["utgaver"]:
            if s not in utgave_ider and s not in historikk:
                feil.append(f"{hvor}: sammenligner_med viser til ukjent utgave '{s}'")
        fp = u["feltperiode"]
        if fp["fra"] and fp["til"] and fp["til"] < fp["fra"]:
            feil.append(f"{hvor}: feltperioden slutter før den begynner")
        if fp["fra"] and not fp["fra"].startswith(u["id"]):
            feil.append(f"{hvor}: feltperioden begynner ikke i {u['id']}")
        for dato in (fp["fra"], fp["til"]):
            if dato:
                try:
                    dt.date.fromisoformat(dato)
                except ValueError:
                    feil.append(f"{hvor}: ugyldig dato '{dato}'")
        svar = u["svar"]
        if svar["nettoutvalg"] > svar["bruttoutvalg"]:
            feil.append(f"{hvor}: nettoutvalget er større enn bruttoutvalget")
        antall = [m["antall"] for m in u["innsamling"]["modus"]]
        if None not in antall and sum(antall) != svar["nettoutvalg"] and not svar["nettoutvalg_merknad"]:
            advarsler.append(
                f"{hvor}: svar per modus summerer til {sum(antall)}, nettoutvalget er "
                f"{svar['nettoutvalg']}, og det står ingen nettoutvalg_merknad"
            )
        if u["malgruppe"]["alder_til"] is not None and u["malgruppe"]["alder_til"] < u["malgruppe"]["alder_fra"]:
            feil.append(f"{hvor}: målgruppens øvre alder er lavere enn den nedre")
    if [u["aar"] for u in kjerne.les_utgaver()["utgaver"]] != sorted(u["aar"] for u in utgaver):
        advarsler.append("data/utgaver.yaml: utgavene står ikke i kronologisk rekkefølge")

    # --- Konseptene --------------------------------------------------------------------
    if len(konsepter) != len(kjerne.les_yaml(kjerne.DATA / "konsepter.yaml")["konsepter"]):
        feil.append("data/konsepter.yaml: samme konsept-id brukt flere ganger")
    for kid, k in konsepter.items():
        for kobling in k["koblinger"]:
            if kobling["konsept"] not in konsepter:
                feil.append(f"data/konsepter.yaml: {kid}: kobling til ukjent konsept '{kobling['konsept']}'")

    # --- Spørreskjemaene ---------------------------------------------------------------
    for sti in kjerne.skjemafiler():
        data = kjerne.les_yaml(sti)
        hvor = f"data/skjema/{sti.name}"
        if data["utgave"] != sti.stem:
            feil.append(f"{hvor}: utgave '{data['utgave']}' er ikke den samme som filnavnet")
        if data["utgave"] not in utgave_ider:
            feil.append(f"{hvor}: utgaven finnes ikke i data/utgaver.yaml")
        sett = set()
        for post in data["sporsmal"]:
            k = post["konsept"]
            if k not in konsepter:
                feil.append(f"{hvor}: ukjent konsept '{k}'")
            if k in sett:
                feil.append(f"{hvor}: konseptet '{k}' står flere ganger")
            sett.add(k)
            koder = [a["kode"] for a in post["svaralternativer"] if a["kode"] is not None]
            if len(koder) != len(set(koder)):
                feil.append(f"{hvor}: {k}: samme kode brukt på flere svaralternativer")
            if not any(a["tekst"] for a in post["svaralternativer"]):
                feil.append(f"{hvor}: {k}: ingen svaralternativer har tekst")
            df = post["datafil"]
            if df["kontrollert"] and df["koder"] is None:
                feil.append(f"{hvor}: {k}: datafil er merket kontrollert, men kodene mangler")
            if not df["kontrollert"] and (df["koder"] or df["ikke_sikker_kode"] is not None):
                feil.append(f"{hvor}: {k}: datafil har koder, men er ikke merket kontrollert")
            if df["koder"] and df["ikke_sikker_kode"] in df["koder"]:
                feil.append(f"{hvor}: {k}: koden for «Ikke sikker» står blant de gyldige kodene")
            if post["svartype"] == "skala" and df["koder"]:
                trinn = [a["kode"] for a in post["svaralternativer"] if a["kode"] is not None and a["kode"] != kjerne.ikke_sikker_kode(post)]
                if trinn and trinn != df["koder"]:
                    advarsler.append(f"{hvor}: {k}: skalatrinnene i skjemaet ({trinn}) er ikke de samme som kodene i datafila ({df['koder']})")

    # --- Dommene -----------------------------------------------------------------------
    serier = kjerne.sporsmal_per_konsept(skjema)
    indeks = kjerne.vurderingsindeks(vurderinger)
    if len(indeks) != len(vurderinger):
        feil.append("data/vurderinger.yaml: samme overgang vurdert flere ganger")
    lovlige = {
        (k, fra, til) for k, serie in serier.items() for (fra, _), (til, _) in kjerne.overganger(serie)
    }
    for nokkel in indeks:
        if nokkel[0] not in konsepter:
            feil.append(f"data/vurderinger.yaml: ukjent konsept '{nokkel[0]}'")
        elif nokkel not in lovlige:
            feil.append(
                f"data/vurderinger.yaml: {nokkel[0]} {nokkel[1]}→{nokkel[2]} er ikke to utgaver etter "
                f"hverandre der konseptet finnes"
            )
    for nokkel in sorted(lovlige - set(indeks)):
        feil.append(f"MANGLER DOM: {nokkel[0]} {nokkel[1]}→{nokkel[2]} har ingen post i data/vurderinger.yaml")

    return feil, advarsler


def main() -> int:
    streng = "--streng" in sys.argv
    feil, advarsler = valider()
    for a in advarsler:
        print(f"  ADVARSEL  {a}")
    for f in feil:
        print(f"  FEIL      {f}")
    serier = kjerne.sporsmal_per_konsept() if not feil else {}
    print()
    print(
        f"{len(kjerne.utgaveliste())} utgaver, {len(kjerne.les_konsepter())} konsepter, "
        f"{len(kjerne.les_skjema())} spørreskjemaer, {len(kjerne.les_vurderinger())} dommer, "
        f"{sum(len(kjerne.finn_skjemaendringer(k, s)) for k, s in serier.items())} utledede skjemaendringer."
    )
    if feil:
        print(f"FEILET: {len(feil)} feil, {len(advarsler)} advarsler.")
        return 1
    if advarsler and streng:
        print(f"FEILET (--streng): {len(advarsler)} advarsler.")
        return 1
    print(f"OK ({len(advarsler)} advarsler).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
