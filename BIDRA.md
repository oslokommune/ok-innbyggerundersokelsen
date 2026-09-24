# Bidra og bruke dataene

Denne fila beskriver reglene for innholdet, formatet på filene i `data/` og hvordan
verktøyene kjøres. Spørsmål og rettelser kan sendes til
[oslostatistikken@byr.oslo.kommune.no](mailto:oslostatistikken@byr.oslo.kommune.no).

## Reglene

1. **Repoet er offentlig.** Det inneholder aldri svar fra enkeltpersoner, datafiler eller
   personopplysninger. `.gitignore` stopper de vanlige dataformatene, og CI feiler hvis en
   slik fil likevel kommer med.
2. **Alt har en kilde.** En opplysning uten kilde står ikke her. Er kilden et dokument med
   sider, oppgis siden; sidetallet er sidenummeret i PDF-fila. Kildene står i `data/kilder.yaml`.
3. **Ordlyden hentes fra spørreskjemaet, aldri fra datafila.** Etikettene i datafilene kan være
   forkortet eller harmonisert på tvers av utgaver, og da skjuler de endringer.
4. **`data/` er kilden, `docs/` er generert.** Rediger aldri en generert fil i `docs/`; endre
   `data/` og kjør `verktoy/generer_docs.py`. De håndskrevne sidene i `docs/` er
   `SAMMENLIGNBARHET-OVER-TID.md` og `ORDLISTE.md`.
5. **Konsept-id-en er permanent.** Id-en beskriver det som måles, ikke ordlyden. Endres
   ordlyden, beholdes id-en, og den nye ordlyden skrives i skjemafila for den nye utgaven.
   Endres meningen, får spørsmålet en ny id. Gjenbruk aldri en id på noe som måler noe annet.
6. **Maskinen finner endringen, mennesket vurderer den.** At ordlyd, svaralternativer eller
   metode har endret seg mellom to utgaver, utledes av verktøyet. Det skrives ikke ned. Det som
   lagres, er dommen i `data/vurderinger.yaml`: kan tallene sammenlignes?

## Formatet

Filene er YAML. Hver fil har et JSON Schema i `skjema/`, og `verktoy/validering.py` kontrollerer
både skjemaet og sammenhengen mellom filene. Alle filene har `formatversjon: 1`.

Leser du filene maskinelt, hent dem fra en versjonstagg (for eksempel `v1.0`), ikke fra
hovedgrenen. Da endrer ikke innholdet seg under deg.

Kodene for utvalgsdesign, innsamlingsmodus, analyseenhet og tidsmetode følger DDIs kontrollerte
vokabularer slik CESSDA publiserer dem (<https://vocabularies.cessda.eu>): SamplingProcedure 2.0,
ModeOfCollection 5.0, AnalysisUnit 2.1 og TimeMethod 1.2.

**Stabilitet.** Innenfor formatversjon 1 blir ingen felt fjernet eller endret betydning. Nye
felt kan komme til; les derfor bare feltene du trenger. En endring som bryter med dette, gir
formatversjon 2 og en ny hovedversjon av repoet (v2.0).

### `data/kilder.yaml`

| Felt | Innhold |
|---|---|
| `id` | fast id som resten av `data/` viser til, for eksempel `rapport-2023` |
| `kortnavn` | navnet som brukes i henvisninger på sidene («Rapport 2023») |
| `type` | `rapport`, `sporreskjema` eller `datafil` |
| `tittel`, `utgiver`, `aar` | som på kilden |
| `tilgjengelig` | hvor kilden finnes |

En henvisning i de andre filene er `{id: <kilde-id>, side: "<side>"}`. `side` er tekst, slik
at den kan være et intervall («5–6») eller en liste («4, 7»).

### `data/utgaver.yaml`

Én post per utgave, med de samme feltene for alle. Hvert felt har sin egen `kilde`.

| Felt | Innhold |
|---|---|
| `id`, `aar`, `navn` | utgaven |
| `sporreskjema` | henvisning til spørreskjemaet, eller `null` hvis det ikke finnes |
| `oppdrag` | `oppdragsgiver` og `leverandor` |
| `malgruppe` | `beskrivelse`, `alder_fra`, `alder_til` (`null` = ingen øvre grense) |
| `analyseenhet` | DDI AnalysisUnit, her alltid `Individual` |
| `tidsmetode` | DDI TimeMethod for utgaven, her alltid `CrossSection` |
| `utvalgsramme` | hvor utvalget er trukket fra, og hvordan man ble kontaktet |
| `utvalgsdesign` | `type` (DDI SamplingProcedure) og `beskrivelse` |
| `innsamling` | `beskrivelse` og `modus`: en liste med `kode` (DDI ModeOfCollection) og `antall` svar |
| `kontakt` | invitasjon og påminnelser |
| `sprak` | språkene skjema og invitasjon fantes på |
| `feltperiode` | `fra`, `til` (ÅÅÅÅ-MM-DD), `arstid` (`vinter`, `vår`, `sommer`, `høst`) |
| `svar` | `bruttoutvalg`, `nettoutvalg`, `svarprosent`, `beregning` (hvordan svarprosenten er regnet) og `nettoutvalg_merknad` |
| `vekting` | `variabler`, `beskrivelse` og `vektvariabel` (navnet i datafila) |
| `landbakgrunn` | `type`: `selvrapportert`, `register` eller `ikke_oppgitt` |
| `skjemaendring` | endringene i skjemaet slik kilden selv beskriver dem |
| `sammenligner_med` | utgavene rapporten selv sammenligner med |

Når kildene oppgir ulike tall for antall svar, brukes tallet i rapportens metodekapittel. De
andre tallene står i `nettoutvalg_merknad`, uten forklaring som ikke står i kilden.

`historikk` beskriver 1998 og 2001, som det bare finnes omtale av.

### `data/konsepter.yaml`

| Felt | Innhold |
|---|---|
| `id` | fast id: små bokstaver, tall og `_`. Endres aldri |
| `navn`, `beskrivelse`, `tema` | hva konseptet måler |
| `koblinger` | deling, sammenslåing eller erstatning: `{type, konsept, utgave}` |
| `note_til_tabell` | standardmerknaden som brukes når tall for konseptet publiseres i tabeller. Teksten brukes ordrett |

### `data/skjema/<år>.yaml`

Én fil per utgave. Filnavnet er utgaven. `sporreskjema` er kilde-id-en til skjemaet.
`sporsmal` er en liste med én post per konsept:

| Felt | Innhold |
|---|---|
| `konsept` | id fra `data/konsepter.yaml` |
| `skjema_nr`, `ledd_nr` | nummeret slik det står i skjemaet, og linjen i batteriet |
| `seksjon` | nærmeste overskrift over spørsmålet |
| `innledning` | teksten over batteriet. En liste når det er flere linjer (stamme og underoverskrift), i den rekkefølgen de står |
| `instruksjon` | instruksjoner som «Merk: Sett ett kryss på hver linje» |
| `ledd_tekst` | linjeteksten |
| `svartype` | `skala`, `enkeltvalg`, `flervalg`, `ja_nei`, `tall` eller `fritekst` |
| `svaralternativer` | liste med `kode` og `tekst` i skjemaets rekkefølge |
| `filter` | hvem som fikk spørsmålet, slik kilden sier det. `null` = alle |
| `kilde` | henvisning til skjemaet med side |
| `merknad` | forhold ved kilden leseren bør kjenne til |
| `datafil` | variabelen i leverandørens datafil for utgaven (se under) |
| `varianter` | andre versjoner av skjemaet samme år, for eksempel nettskjemaet i 2018 |

`kode` i `svaralternativer` er koden som står trykt eller programmert i skjemaet. Står det
ingen kode, er den `null`. Et mellomtrinn uten tekst har `tekst: null`.

`datafil` beskriver koblingen til dataene:

| Felt | Innhold |
|---|---|
| `variabel` | variabelnavnet i leverandørens datafil for utgaven |
| `koder` | de gyldige svarkodene i datafila |
| `ikke_sikker_kode` | koden for «Ikke sikker» i datafila |
| `manglende` | hvordan manglende svar er lagret: `tom` = systemmanglende |
| `kontrollert` | `true` når kodene er kontrollert mot datafilas metadata. Er den `false`, er `koder` og `ikke_sikker_kode` `null`, og bare variabelnavnet er kjent |

### `data/vurderinger.yaml`

Én post per konsept og overgang mellom to utgaver etter hverandre der konseptet finnes. Alle
overganger skal ha en dom; validering feiler ellers.

| Felt | Innhold |
|---|---|
| `konsept`, `fra_utgave`, `til_utgave` | overgangen |
| `sammenlignbar` | `ja`, `med_forbehold` eller `nei` |
| `begrunnelse` | hvorfor |
| `grunnlag` | kildene dommen bygger på |
| `besluttet_av`, `dato` | hvem som har gitt dommen, og når. `FIN` = Byrådsavdeling for finans, Oslo kommune |

## Slik skrives et spørreskjema av

- Skriv ordrett: store og små bokstaver, tegnsetting og skrivefeil som i kilden. Fjern bare
  prikkledere og avkrysningsruter.
- Skriv bare koder som står i skjemaet. Ikke legg til koder ved analogi.
- En underoverskrift inne i et batteri («....der du bor») hører til `innledning`, i den
  rekkefølgen den står på siden.
- En kolonne som «Brukt siste 12 måneder» er et `filter`, beskrevet slik den står.
- `svartype`: `skala` når alternativene er graderte (grad, fornøydhet, enighet, hyppighet),
  `ja_nei` når alternativene bare er Ja og Nei (eventuelt med Ikke sikker), `enkeltvalg` for
  andre spørsmål med ett svar.
- Er noe uleselig eller tvetydig, skriv det i `merknad`. Ikke gjett.

Skjemaene i `data/skjema/` er kontrollert på to måter. For 2007, 2010 og 2018 er to
uavhengige avskrifter fra sidebildene sammenlignet felt for felt. For 2007, 2010, 2014, 2023 og
2026 er hver tekst, hvert svaralternativ, hver kode og hvert filter kontrollert maskinelt mot
tekstversjonen av kilden. Avvik er avgjort mot kilden.

## Kjøre verktøyene

Krever Python 3.11 eller nyere.

```
pip install -r requirements.txt
python verktoy/validering.py            # kontroller data/
python verktoy/generer_docs.py          # skriv docs/ på nytt
python verktoy/generer_docs.py --sjekk  # kontroller at docs/ er i takt med data/
python -m pytest tests -q
```

CI kjører alle fire. Kjør dem før du foreslår en endring.

## Endringer og versjoner

- En rettelse eller et nytt spørsmål gir en ny mindre versjon (v1.1, v1.2 …).
- En endring i formatet som bryter med formatversjon 1, gir en ny hovedversjon (v2.0).
- Tidligere versjoner blir liggende og kan alltid hentes. Bruker du dataene maskinelt, les en
  fast versjon.

Spørreskjemaet for en utgave kan rettes etter at det er publisert. Da rettes fila for den
utgaven, og endringene mellom utgavene utledes på nytt. Git-historikken viser hva som er rettet
og når.
