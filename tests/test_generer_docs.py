import generer_docs
import kjerne
from conftest import erstatt


def test_docs_er_i_takt_med_data():
    for navn, lag in generer_docs.FILER.items():
        assert (kjerne.DOCS / navn).read_text(encoding="utf-8") == lag(), f"docs/{navn} er ikke i takt; kjør verktoy/generer_docs.py"


def test_genereringen_er_stabil():
    assert generer_docs.seriesporsmal() == generer_docs.seriesporsmal()


def test_genererte_filer_har_advarsel():
    for lag in generer_docs.FILER.values():
        assert lag().startswith("<!-- Generert")


def test_serieside_viser_dom_og_note():
    tekst = generer_docs.seriesporsmal()
    assert "#### 2018 → 2023: Med forbehold" in tekst
    assert "Tall fra 2023 og senere bør derfor sammenlignes med tidligere år med varsomhet." in tekst


def test_koding_viser_ubesvart_per_utgave():
    tekst = generer_docs.seriesporsmal()
    assert "| 2018 | `Q001__1` | 1–6 | 7 | 8 |" in tekst
    assert "| 2023 | `Q001#1` | 1–6 | 7 | 9996 og tom |" in tekst
    assert "ikke kontrollert" not in tekst


def test_endret_ordlyd_vises_i_endringsloggen(kopi):
    erstatt(kopi / "data" / "skjema" / "2023.yaml", 'ledd_tekst: "Trives du i Oslo?"', 'ledd_tekst: "Trives du i byen?"')
    tekst = generer_docs.seriesporsmal()
    assert "Spørsmålstekst: «Trives du i Oslo?» → «Trives du i byen?»" in tekst


def test_sjekk_feiler_nar_docs_er_utdatert(kopi, monkeypatch):
    erstatt(kopi / "data" / "utgaver.yaml", "nettoutvalg: 11506", "nettoutvalg: 11507")
    monkeypatch.setattr("sys.argv", ["generer_docs.py", "--sjekk"])
    assert generer_docs.main() == 1
