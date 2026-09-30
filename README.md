# Oslo kommunes innbyggerundersøkelse

Dokumentasjon av Oslo kommunes innbyggerundersøkelse, som tidligere het
publikumsundersøkelsen: hvordan undersøkelsen er gjennomført i hver utgave, hva som har endret
seg over tid, og nøyaktig hvordan spørsmålene er stilt.

Undersøkelsen er gjennomført i 1998, 2001, 2004, 2007, 2010, 2014, 2018, 2023 og 2026.
Rapportene fra 2007 og senere ligger på
[oslo.kommune.no/statistikk/innbyggerundersokelsen](https://www.oslo.kommune.no/statistikk/innbyggerundersokelsen/).

Ikke å forveksle med den nasjonale Innbyggerundersøkelsen fra Direktoratet for forvaltning og
økonomistyring (DFØ).

## Hva som er her

| Side | Innhold |
|---|---|
| [Metode, utgave for utgave](docs/METODE.md) | Utvalg, innsamling, feltperiode, svarprosent, vekting og mer for hver utgave fra 2004, beskrevet med de samme feltene |
| [Sammenlignbarhet over tid](docs/SAMMENLIGNBARHET-OVER-TID.md) | Endringene som gjelder alle spørsmål: ny målgruppe i 2014, omleggingen til nett i 2023, svarprosent, landbakgrunn og årstid |
| [Spørsmålene som følges over tid](docs/SERIESPORSMAL.md) | Ordlyd per utgave og en dom for hver overgang: kan tallene sammenlignes med forrige utgave? |
| [Kilder](docs/KILDER.md) | Rapportene og skjemaene alt bygger på |
| [Ordliste](docs/ORDLISTE.md) | Fagordene som brukes på sidene |

Opplysningene har kilde, og der kilden er et dokument med sider, sidetall. Ordlyden er skrevet
av fra spørreskjemaene, ikke fra etikettene i datafilene, fordi etikettene kan være harmonisert
og skjule endringer.

Denne versjonen dokumenterer fire spørsmål over tid: «Trives du i Oslo?», trygghet når det
gjelder å ferdes ute på kveldstid og på dagtid der man bor, og tilgangen til natur- og
friluftsområder der man bor. Flere spørsmål legges til når de er kontrollert mot
spørreskjemaene.

## Hva som ikke er her

Repoet har **ingen resultater** og ingen svar fra enkeltpersoner. Det beskriver hvordan
undersøkelsen er gjort og hva som kan sammenlignes. Tallene fra hver utgave står i rapportene på
[hovedsiden](https://www.oslo.kommune.no/statistikk/innbyggerundersokelsen/).

## Filene bak sidene

Alt på sidene over er generert fra filene i [`data/`](data/). Filene kan leses av mennesker og
maskiner:

```
data/
  utgaver.yaml        metoden for hver utgave, i ett felles system
  konsepter.yaml      det spørsmålene måler, med en fast id per konsept
  skjema/<år>.yaml    spørsmålene slik de står i spørreskjemaet det året, med variabelnavn og koding i datafila
  vurderinger.yaml    dommene om sammenlignbarhet, med begrunnelse
  kilder.yaml         kildene
skjema/               JSON Schema for filene i data/
verktoy/              validering og generering av docs/
docs/                 sidene over
```

Formatet er beskrevet i [BIDRA.md](BIDRA.md). Bruker du dataene maskinelt, bør du lese en fast
versjon (for eksempel `v1.0`) og ikke siste utgave av hovedgrenen.

## Versjoner og sitering

Hver versjon av dokumentasjonen har et versjonsnummer. Rettelser gir en ny versjon, og de
tidligere versjonene blir liggende. Oppgi versjonen når du viser til dokumentasjonen:

> Oslo kommune (2026). *Oslo kommunes innbyggerundersøkelse. Dokumentasjon*, versjon 1.0.
> https://github.com/oslokommune/ok-innbyggerundersokelsen/tree/v1.0

## Lisens

Data og dokumentasjon: [NLOD 2.0](https://data.norge.no/nlod/no/2.0). Kode: Apache 2.0. Se
[LICENSE.md](LICENSE.md).

## Kontakt

Spørsmål, rettelser og innspill: [oslostatistikken@byr.oslo.kommune.no](mailto:oslostatistikken@byr.oslo.kommune.no).
Se også [BIDRA.md](BIDRA.md).
