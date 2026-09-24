"""Generer lesbar dokumentasjon i docs/ fra data/.

    python verktoy/generer_docs.py           # skriv docs/
    python verktoy/generer_docs.py --sjekk   # feil hvis docs/ ikke er i takt med data/ (CI)

Genererte filer har en advarsel i toppen og skal ikke redigeres for hånd. De håndskrevne
sidene (docs/SAMMENLIGNBARHET-OVER-TID.md og docs/ORDLISTE.md) røres ikke.
"""

from __future__ import annotations

import sys

import kjerne
from kjerne import DOCS, etikett, tekst

ADVARSEL = (
    "<!-- Generert av verktoy/generer_docs.py fra data/. Ikke rediger denne fila for hånd:\n"
    "     endre data/ og kjør verktøyet på nytt. -->\n"
)

FELTNAVN = {
    "innledning": "Innledning",
    "ledd_tekst": "Spørsmålstekst",
    "svartype": "Svartype",
    "svaralternativer": "Svaralternativer",
    "ikke_sikker_kode": "Kode for «Ikke sikker» i skjemaet",
    "instruksjon": "Instruksjon",
    "filter": "Filter",
}

# Hvem koden i `besluttet_av` står for.
BESLUTTET_AV = {"FIN": "Byrådsavdeling for finans, Oslo kommune"}

MAANEDER = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]


def dato(iso: str | None) -> str:
    if not iso:
        return "ikke oppgitt"
    aar, mnd, dag = iso.split("-")
    return f"{int(dag)}. {MAANEDER[int(mnd) - 1]} {aar}"


def tall(n) -> str:
    if n is None:
        return "–"
    if isinstance(n, float):
        return f"{n:.1f}".replace(".", ",")
    return f"{n:,}".replace(",", "\u00a0")


def kref(ref: dict | None, kilder: dict) -> str:
    if not ref:
        return "–"
    navn = kilder[ref["id"]]["kortnavn"]
    return f"{navn}, s. {ref['side']}" if ref.get("side") else navn


def lenke(fil: str) -> str:
    """Markdown-lenke til en annen side i docs/. Lenkene er relative til docs/, der sidene ligger."""
    return f"[{fil}]({fil})"


def anker(overskrift: str) -> str:
    """GitHubs anker for en overskrift: små bokstaver, mellomrom blir bindestrek."""
    import re
    return re.sub(r"[^\w\- ]", "", overskrift).strip().lower().replace(" ", "-")


def celle(s) -> str:
    return (s or "–").replace("|", "\\|").replace("\n", " ")


def manglende_tekst(datafil: dict) -> str:
    """Hvordan ubesvart er kodet: «tom», én eller flere koder, eller ikke kontrollert."""
    m = datafil["manglende"]
    if m is None:
        return "ikke kontrollert" if not datafil["kontrollert"] else "–"
    deler = [m] if isinstance(m, str) else [str(x) for x in m]
    return " og ".join(deler)


def alternativer(post: dict) -> str:
    deler = []
    for a in post["svaralternativer"]:
        if a["kode"] is None:
            deler.append(a["tekst"])
        elif a["tekst"] is None:
            deler.append(str(a["kode"]))
        else:
            deler.append(f"{a['kode']} = {a['tekst']}")
    return "; ".join(deler)


def ordlyd(post: dict) -> str:
    inn = post.get("innledning")
    linjer = inn if isinstance(inn, list) else ([inn] if inn else [])
    deler = [f"«{l}»" for l in linjer]
    if post.get("ledd_tekst"):
        deler.append(f"**«{post['ledd_tekst']}»**")
    return " ".join(deler)


def feltperiode(fp: dict) -> str:
    if fp["til"]:
        tekst_ = f"{dato(fp['fra'])} – {dato(fp['til'])} ({fp['arstid']})"
        return tekst_ + (f". {fp['beskrivelse']}" if fp["beskrivelse"] else "")
    return (fp["beskrivelse"] or f"Fra {dato(fp['fra'])}") + f" ({fp['arstid']})"


def svarprosent(u: dict) -> str:
    sp = u["svar"]["svarprosent"]
    if sp is None:
        return "se under"
    return f"{tall(sp) if isinstance(sp, float) else sp} %"


# --- docs/METODE.md ------------------------------------------------------------------------

def metode() -> str:
    kilder = kjerne.kildeindeks()
    data = kjerne.les_utgaver()
    utgaver = kjerne.utgaveliste()
    L = [ADVARSEL, "# Metode, utgave for utgave", ""]
    L += [
        "Hver utgave er beskrevet med de samme feltene, slik at forskjellene kan leses felt for felt.",
        "Feltene er valgt ut fra hva som kan påvirke om tallene kan sammenlignes over tid. Hvert",
        "felt har en kilde med side; sidetallet er sidenummeret i PDF-fila. Kildene står i",
        f"{lenke('KILDER.md')}. Hva endringene betyr for sammenligning over tid, står i",
        f"{lenke('SAMMENLIGNBARHET-OVER-TID.md')}.",
        "",
        f"Undersøkelsen som helhet er en {etikett(data['tidsmetode_serie']).lower()}: et nytt utvalg",
        "hver gang, med mange av de samme spørsmålene. Hver utgave er et tverrsnitt, og",
        "analyseenheten er personen som svarer. Ord som «bruttoutvalg» og «disproporsjonalt» er",
        f"forklart i {lenke('ORDLISTE.md')}.",
        "",
        "## Oversikt",
        "",
        "| Utgave | Leverandør | Målgruppe | Svar per modus | Feltperiode | Brutto | Netto | Svarprosent |",
        "|---|---|---|---|---|---:|---:|---:|",
    ]
    for u in utgaver:
        fp = u["feltperiode"]
        periode = f"{dato(fp['fra'])} – {dato(fp['til'])}" if fp["til"] else f"fra {dato(fp['fra'])}"
        alder = f"{u['malgruppe']['alder_fra']}–{u['malgruppe']['alder_til']} år" if u["malgruppe"]["alder_til"] else f"{u['malgruppe']['alder_fra']} år +"
        L.append(
            f"| [{u['id']}](#{u['id']}) | {u['oppdrag']['leverandor']} | {alder} | {kjerne.modusfordeling(u)} | "
            f"{periode} | {tall(u['svar']['bruttoutvalg'])} | {tall(u['svar']['nettoutvalg'])} | {svarprosent(u)} |"
        )
    L += [
        "",
        "Svarprosentene kan ikke stilles opp som en serie: de er regnet på ulike måter. Se",
        "«Hvordan svarprosenten er regnet» under hver utgave.",
        "",
        "## Før 2004",
        "",
    ]
    for h in data["historikk"]:
        L.append(f"- **{h['aar']}.** {h['beskrivelse']} ({kref(h['kilde'], kilder)})")
    L.append("")

    for u in utgaver:
        L += [f"## {u['id']}", "", f"**{u['navn']} {u['aar']}.** Utført av {u['oppdrag']['leverandor']} for {u['oppdrag']['oppdragsgiver']} ({kref(u['oppdrag']['kilde'], kilder)}).", ""]
        if u.get("sporreskjema"):
            L.append(f"Spørreskjema: {kref(u['sporreskjema'], kilder)}.")
        if u.get("sporreskjema_merknad"):
            L.append(u["sporreskjema_merknad"])
        L += ["", "| Felt | Verdi | Kilde |", "|---|---|---|"]
        rader = [
            ("Målgruppe", u["malgruppe"]["beskrivelse"], u["malgruppe"]["kilde"]),
            ("Utvalgsramme", u["utvalgsramme"]["beskrivelse"], u["utvalgsramme"]["kilde"]),
            ("Utvalgsdesign", f"{etikett(u['utvalgsdesign']['type'])}. {u['utvalgsdesign']['beskrivelse']}", u["utvalgsdesign"]["kilde"]),
            ("Innsamling", u["innsamling"]["beskrivelse"], u["innsamling"]["kilde"]),
            ("Svar per modus", "; ".join(
                f"{etikett(m['kode'])}{' (' + m['merknad'] + ')' if m.get('merknad') else ''}: {tall(m['antall'])}" for m in u["innsamling"]["modus"]
            ) + (f". {u['innsamling']['merknad']}" if u["innsamling"].get("merknad") else ""), u["innsamling"]["kilde"]),
            ("Kontakt og påminnelser", u["kontakt"]["beskrivelse"], u["kontakt"]["kilde"]),
            ("Språk", u["sprak"]["beskrivelse"], u["sprak"]["kilde"]),
            ("Feltperiode", feltperiode(u["feltperiode"]), u["feltperiode"]["kilde"]),
            ("Bruttoutvalg", tall(u["svar"]["bruttoutvalg"]), u["svar"]["kilde"]),
            ("Nettoutvalg (antall svar)", tall(u["svar"]["nettoutvalg"]) + (f". {u['svar']['nettoutvalg_merknad']}" if u["svar"]["nettoutvalg_merknad"] else ""), u["svar"]["kilde"]),
            ("Svarprosent", svarprosent(u), u["svar"]["kilde"]),
            ("Hvordan svarprosenten er regnet", u["svar"]["beregning"], u["svar"]["kilde"]),
            ("Vekting", u["vekting"]["beskrivelse"], u["vekting"]["kilde"]),
            ("Vektvariabel i datafila", u["vekting"]["vektvariabel"]["navn"] if u["vekting"]["vektvariabel"] else None,
             u["vekting"]["vektvariabel"]["kilde"] if u["vekting"]["vektvariabel"] else None),
            ("Kilde til landbakgrunn", etikett(u["landbakgrunn"]["type"]) + (f". {u['landbakgrunn']['beskrivelse']}" if u["landbakgrunn"].get("beskrivelse") else ""), u["landbakgrunn"]["kilde"]),
            ("Endringer i skjemaet", u["skjemaendring"]["beskrivelse"],
             u["skjemaendring"]["kilde"]),
            ("Rapporten sammenligner med", ", ".join(u["sammenligner_med"]["utgaver"]) + (f". {u['sammenligner_med']['merknad']}" if u["sammenligner_med"].get("merknad") else ""), u["sammenligner_med"]["kilde"]),
        ]
        for navn, verdi, ref in rader:
            k = kref(ref, kilder)
            if navn == "Endringer i skjemaet" and u["skjemaendring"].get("kilde_tillegg"):
                k += "; " + kref(u["skjemaendring"]["kilde_tillegg"], kilder)
            L.append(f"| {navn} | {celle(verdi)} | {k} |")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


# --- docs/SERIESPORSMAL.md -----------------------------------------------------------------

def vis_verdi(felt: str, verdi) -> str:
    if verdi is None:
        return "ingen"
    if felt == "svaralternativer":
        return "; ".join(t if k is None else (str(k) if t is None else f"{k} = {t}") for k, t in verdi)
    return f"«{verdi}»" if isinstance(verdi, str) else str(verdi)


def seriesporsmal() -> str:
    kilder = kjerne.kildeindeks()
    konsepter = kjerne.les_konsepter()
    utgaver = {u["id"]: u for u in kjerne.utgaveliste()}
    serier = kjerne.sporsmal_per_konsept()
    dommer = kjerne.vurderingsindeks(kjerne.les_vurderinger())
    L = [ADVARSEL, "# Spørsmålene som følges over tid", ""]
    L += [
        "Her står ordlyden i hver utgave, slik den står i spørreskjemaet, og en dom for hver",
        "overgang: kan tallene sammenlignes med forrige utgave? Hva som er endret i skjemaet og i",
        "metoden, er funnet ved å sammenligne utgavene maskinelt. Dommen og begrunnelsen er",
        "redaksjonell og er gitt av Byrådsavdeling for finans, Oslo kommune.",
        "",
        "Dommene betyr:",
        "",
        "- **Ja**: kan sammenlignes.",
        "- **Med forbehold**: kan sammenlignes, men en endring kan ha påvirket tallene.",
        "- **Nei**: måler ikke det samme; serien er brutt.",
        "",
        "I praksis betyr «med forbehold» at tallene kan stå i samme tabell eller figur, men at en",
        "endring mellom de to utgavene ikke bør omtales som sikker uten at forbeholdet nevnes.",
        "Standardmerknaden nederst for hvert spørsmål kan brukes fritt i tabeller og tekster.",
        "",
        "Dommene gjelder to utgaver etter hverandre. Sammenligner du utgaver med andre utgaver",
        "imellom, gjelder den svakeste dommen på veien: er én overgang «med forbehold», gjelder",
        "forbeholdet hele sammenligningen.",
        "",
        "«Ikke sikker» regnes som manglende svar i alle utgaver, som i rapportene. Så lenge «Ikke",
        "sikker» holdes utenfor, påvirker ulik koding av det alternativet ikke tallene.",
        "",
        "Svaralternativene er skrevet «kode = tekst» slik de står i skjemaet. I 2026 står tallet også",
        "i selve teksten («1 - I svært liten grad»).",
        "",
    ]
    L += [f"- [{k['navn']}](#{anker(k['navn'])})" for kid, k in konsepter.items() if serier.get(kid)]
    L.append("")
    for kid, k in konsepter.items():
        serie = serier.get(kid, [])
        if not serie:
            continue
        L += [f"## {k['navn']}", "", f"Konsept-id: `{kid}`. {k['beskrivelse']}", ""]
        steg = []
        for (fra, _), (til, _) in kjerne.overganger(serie):
            d = dommer.get((kid, fra, til))
            steg.append(f"{fra} → {til}: {etikett(d['sammenlignbar']).lower() if d else 'ikke vurdert'}")
        L += [f"**Serien:** {' · '.join(steg)}.", ""]
        L += ["### Ordlyd per utgave", "", "| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |", "|---|---|---|---|---|---|---|"]
        for utgave, p in serie:
            nr = p["skjema_nr"] + (f", linje {p['ledd_nr']}" if p.get("ledd_nr") else "")
            instr = " ".join(f"«{l}»" for l in (p["instruksjon"] if isinstance(p["instruksjon"], list) else [p["instruksjon"]]) if l)
            L.append(f"| {utgave} | {nr} | {celle(ordlyd(p))} | {celle(instr)} | {celle(alternativer(p))} | `{p['datafil']['variabel']}` | {kref(p['kilde'], kilder)} |")
        L.append("")
        merk = [(u, p) for u, p in serie if p.get("merknad") or p.get("varianter")]
        for utgave, p in merk:
            if p.get("merknad"):
                L.append(f"- **{utgave}:** {p['merknad']}")
            for v in p.get("varianter") or []:
                forskjell = [FELTNAVN[f].lower() for f in ("innledning", "ledd_tekst", "svaralternativer") if kjerne.skjemaverdi(v, f) != kjerne.skjemaverdi(p, f)]
                likt = "Samme ordlyd og svaralternativer som papirskjemaet." if not forskjell else f"Avvik fra papirskjemaet i {', '.join(forskjell)}: {ordlyd(v)}."
                L.append(f"- **{utgave}, {v['navn']}** ({v['skjema_nr']}, {kref(v['kilde'], kilder)}): {v['beskrivelse']} {likt}")
        if merk:
            L.append("")

        L += ["### Koding i datafilene", ""]
        ukontrollert = [u for u, p in serie if not p["datafil"]["kontrollert"]]
        if ukontrollert:
            L += [f"For {', '.join(ukontrollert[:-1]) + ' og ' + ukontrollert[-1] if len(ukontrollert) > 1 else ukontrollert[0]} er bare variabelnavnet hentet fra datafila i denne versjonen.", ""]
        L += ["| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |", "|---|---|---|---|---|---|"]
        for utgave, p in serie:
            d = p["datafil"]
            koder = f"{min(d['koder'])}–{max(d['koder'])}" if d["koder"] else "ikke kontrollert"
            ikke = str(d["ikke_sikker_kode"]) if d["ikke_sikker_kode"] is not None else ("–" if d["kontrollert"] else "ikke kontrollert")
            L.append(f"| {utgave} | `{d['variabel']}` | {koder} | {ikke} | {manglende_tekst(d)} | {celle(d['merknad'])} |")
        L.append("")

        L += ["### Overgangene", ""]
        endringer = kjerne.finn_skjemaendringer(kid, serie)
        for (fra, _), (til, _) in kjerne.overganger(serie):
            dom = dommer.get((kid, fra, til))
            L.append(f"#### {fra} → {til}: {etikett(dom['sammenlignbar']) if dom else 'ikke vurdert'}")
            L.append("")
            e_skjema = [e for e in endringer if (e.fra_utgave, e.til_utgave) == (fra, til)]
            e_metode = kjerne.finn_metodeendringer(utgaver[fra], utgaver[til])
            if e_skjema:
                L.append("Endret i skjemaet:")
                L.append("")
                for e in e_skjema:
                    L.append(f"- {FELTNAVN[e.felt]}: {vis_verdi(e.felt, e.fra_verdi)} → {vis_verdi(e.felt, e.til_verdi)}")
                L.append("")
            else:
                L += ["Ingen endring i ordlyd eller svaralternativer.", ""]
            if e_metode:
                L.append("Endret i metoden:")
                L.append("")
                for navn, a, b in e_metode:
                    L.append(f"- {navn}: {a} → {b}")
                L.append("")
            if dom:
                L += [f"**Vurdering:** {dom['begrunnelse']}", "",
                      f"Grunnlag: {'; '.join(kref(g, kilder) for g in dom['grunnlag'])}. Vurdert av {BESLUTTET_AV[dom['besluttet_av']]}, {dato(dom['dato'])}.", ""]
        L += ["### Standardmerknad til tabeller", "",
              "Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:", "",
              f"> {k['note_til_tabell']}", ""]
    return "\n".join(L).rstrip() + "\n"


# --- docs/KILDER.md ------------------------------------------------------------------------

TYPER = {"rapport": "Rapporter", "sporreskjema": "Spørreskjemaer", "datafil": "Datafiler"}


def kildeliste() -> str:
    data = kjerne.les_kilder()
    L = [ADVARSEL, "# Kilder", ""]
    L += [
        "Alt i dette repoet har en kilde med side. Sidetallet er sidenummeret i PDF-fila, som kan",
        "avvike med én side fra det trykte sidetallet.",
        "",
        f"Rapportene er publisert på undersøkelsens hovedside: <{data['hovedside']}>. Vi lenker bare",
        "dit, ikke til enkeltfilene.",
        "",
    ]
    for typ, overskrift in TYPER.items():
        rader = [k for k in data["kilder"] if k["type"] == typ]
        if not rader:
            continue
        L += [f"## {overskrift}", "", "| Kortnavn | Tittel | Utgiver | Tilgjengelig | Merknad |", "|---|---|---|---|---|"]
        for k in rader:
            L.append(f"| {k['kortnavn']} | {celle(k['tittel'])} | {celle(k['utgiver'])} | {k['tilgjengelig']} | {celle(k.get('merknad'))} |")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


FILER = {
    "METODE.md": metode,
    "SERIESPORSMAL.md": seriesporsmal,
    "KILDER.md": kildeliste,
}


def main() -> int:
    sjekk = "--sjekk" in sys.argv
    avvik = []
    DOCS.mkdir(exist_ok=True)
    for navn, lag in FILER.items():
        innhold = lag()
        sti = DOCS / navn
        if sjekk:
            if not sti.exists() or sti.read_text(encoding="utf-8") != innhold:
                avvik.append(navn)
        else:
            sti.write_text(innhold, encoding="utf-8", newline="\n")
            print(f"skrev docs/{navn}")
    if sjekk:
        if avvik:
            print(f"docs/ er ikke i takt med data/: {', '.join(avvik)}. Kjør verktoy/generer_docs.py.")
            return 1
        print("docs/ er i takt med data/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
