import validering
from conftest import erstatt


def test_repoets_data_er_gyldig():
    feil, advarsler = validering.valider()
    assert feil == []
    assert advarsler == []


def test_manglende_dom_er_feil(kopi):
    sti = kopi / "data" / "vurderinger.yaml"
    tekst = sti.read_text(encoding="utf-8")
    start = tekst.index("  - konsept: trives_oslo\n    fra_utgave: \"2023\"")
    slutt = tekst.index("  # --- trygghet_kveld_der_du_bor")
    sti.write_text(tekst[:start] + tekst[slutt:], encoding="utf-8")
    feil, _ = validering.valider()
    assert any("MANGLER DOM" in f and "2023→2026" in f for f in feil)


def test_dom_for_utgaver_som_ikke_folger_hverandre_er_feil(kopi):
    erstatt(kopi / "data" / "vurderinger.yaml", 'fra_utgave: "2007"\n    til_utgave: "2010"', 'fra_utgave: "2007"\n    til_utgave: "2014"')
    feil, _ = validering.valider()
    assert any("2007→2014" in f for f in feil)


def test_ukjent_kilde_er_feil(kopi):
    erstatt(kopi / "data" / "utgaver.yaml", "{id: rapport-2014, side: \"4\"}", "{id: rapport-2015, side: \"4\"}")
    feil, _ = validering.valider()
    assert any("ukjent kilde 'rapport-2015'" in f for f in feil)


def test_ukjent_konsept_er_feil(kopi):
    erstatt(kopi / "data" / "skjema" / "2014.yaml", "konsept: trives_oslo", "konsept: trives_i_oslo")
    feil, _ = validering.valider()
    assert any("ukjent konsept 'trives_i_oslo'" in f for f in feil)


def test_skjemabrudd_stopper_kryssjekkene(kopi):
    erstatt(kopi / "data" / "vurderinger.yaml", "sammenlignbar: ja", "sammenlignbar: kanskje")
    feil, _ = validering.valider()
    assert feil and all("vurderinger.yaml" in f for f in feil)


def test_ukontrollert_datafil_kan_ikke_ha_koder(kopi):
    erstatt(kopi / "data" / "skjema" / "2014.yaml", "kontrollert: true", "kontrollert: false")
    feil, _ = validering.valider()
    assert any("ikke merket kontrollert" in f for f in feil)


def test_utgave_som_ikke_matcher_filnavnet_er_feil(kopi):
    erstatt(kopi / "data" / "skjema" / "2014.yaml", 'utgave: "2014"', 'utgave: "2018"')
    feil, _ = validering.valider()
    assert any("filnavnet" in f for f in feil)
