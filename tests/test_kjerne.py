import kjerne


def test_datoer_leses_som_tekst():
    u = {x["id"]: x for x in kjerne.utgaveliste()}
    assert u["2026"]["feltperiode"]["fra"] == "2026-04-23"
    assert all(isinstance(v["dato"], str) for v in kjerne.les_vurderinger())


def test_utgavene_er_kronologiske():
    aar = [u["aar"] for u in kjerne.utgaveliste()]
    assert aar == sorted(aar)


def test_ikke_sikker_kode_fra_skjemaet():
    serie = dict(kjerne.sporsmal_per_konsept()["trives_oslo"])
    assert kjerne.ikke_sikker_kode(serie["2007"]) == 7
    assert kjerne.ikke_sikker_kode(serie["2010"]) is None
    assert kjerne.ikke_sikker_kode(serie["2026"]) == 98


def test_ordlydsendring_utledes():
    serie = kjerne.sporsmal_per_konsept()["trives_oslo"]
    endringer = {(e.fra_utgave, e.til_utgave, e.felt) for e in kjerne.finn_skjemaendringer("trives_oslo", serie)}
    assert ("2007", "2010", "ledd_tekst") in endringer  # «Hvordan trives du i Oslo?» → «Trives du i Oslo?»
    assert ("2023", "2026", "ikke_sikker_kode") in endringer  # ingen kode → 98
    # 2018 → 2023: samme ordlyd og skala, men instruksjonen «Merk: Sett ett kryss …» er borte
    assert {f for fra, til, f in endringer if (fra, til) == ("2018", "2023")} == {"instruksjon"}


def test_bare_mellomrom_normaliseres():
    a = {"innledning": "I hvilken  grad:", "ledd_tekst": "Trives du i Oslo?", "svartype": "skala", "svaralternativer": [], "filter": None}
    b = dict(a, innledning="I hvilken grad:")
    c = dict(a, ledd_tekst="Trives du i Oslo")
    assert not kjerne.finn_skjemaendringer("x", [("1", a), ("2", b)])
    assert [e.felt for e in kjerne.finn_skjemaendringer("x", [("1", a), ("2", c)])] == ["ledd_tekst"]


def test_modusfordeling():
    u = {x["id"]: x for x in kjerne.utgaveliste()}
    assert kjerne.modusfordeling(u["2018"]) == "papir 52 %, nett 48 %"
    assert kjerne.modusfordeling(u["2026"]) == "nett 100 %"


def test_metodeendring_utledes():
    u = {x["id"]: x for x in kjerne.utgaveliste()}
    navn = [n for n, _, _ in kjerne.finn_metodeendringer(u["2010"], u["2014"])]
    assert "Målgruppe" in navn and "Årstid for feltarbeidet" in navn


def test_kilderefs_finner_alle_henvisninger():
    refs = dict(kjerne.kilderefs({"a": {"kilde": {"id": "x", "side": "1"}}, "grunnlag": [{"id": "y", "side": None}]}))
    assert sorted(refs.values()) == ["x", "y"]
