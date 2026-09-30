<!-- Generert av verktoy/generer_docs.py fra data/. Ikke rediger denne fila for hånd:
     endre data/ og kjør verktøyet på nytt. -->

# Spørsmålene som følges over tid

Her står ordlyden i hver utgave, slik den står i spørreskjemaet, og en dom for hver
overgang: kan tallene sammenlignes med forrige utgave? Hva som er endret i skjemaet og i
metoden, er funnet ved å sammenligne utgavene maskinelt. Dommen og begrunnelsen er
redaksjonell og er gitt av Byrådsavdeling for finans, Oslo kommune.

Dommene betyr:

- **Ja**: kan sammenlignes.
- **Med forbehold**: kan sammenlignes, men en endring kan ha påvirket tallene.
- **Nei**: måler ikke det samme; serien er brutt.

I praksis betyr «med forbehold» at tallene kan stå i samme tabell eller figur, men at en
endring mellom de to utgavene ikke bør omtales som sikker uten at forbeholdet nevnes.
Standardmerknaden nederst for hvert spørsmål kan brukes fritt i tabeller og tekster.

Dommene gjelder to utgaver etter hverandre. Sammenligner du utgaver med andre utgaver
imellom, gjelder den svakeste dommen på veien: er én overgang «med forbehold», gjelder
forbeholdet hele sammenligningen.

«Ikke sikker» regnes som manglende svar i alle utgaver, som i rapportene. Så lenge «Ikke
sikker» holdes utenfor, påvirker ulik koding av det alternativet ikke tallene.

Svaralternativene er skrevet «kode = tekst» slik de står i skjemaet. I 2026 står tallet også
i selve teksten («1 - I svært liten grad»).

- [Trivsel i Oslo](#trivsel-i-oslo)
- [Trygghet ute på kveldstid der du bor](#trygghet-ute-på-kveldstid-der-du-bor)
- [Trygghet ute på dagtid der du bor](#trygghet-ute-på-dagtid-der-du-bor)
- [Tilgang til natur- og friluftsområder der du bor](#tilgang-til-natur--og-friluftsområder-der-du-bor)

## Trivsel i Oslo

Konsept-id: `trives_oslo`. Hvor godt man trives i Oslo, på en skala fra 1 (i svært liten grad) til 6 (i svært stor grad).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: ja · 2018 → 2023: med forbehold · 2023 → 2026: ja.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 10, linje 1 | «Først vil vi komme med noen spørsmål knyttet til din vurdering av OSLO SOM BY Å BO I.» **«Hvordan trives du i Oslo?»** | «Vi ber deg svare langs en skala fra 1 til 6, der 1 betyr i svært liten grad, og 6 betyr i svært stor grad.» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker | `Q12_1` | Spørreskjema 2007, s. 1 |
| 2010 | 12, linje 1 | «Først vil vi stille noen spørsmål knyttet til din vurdering av OSLO SOM BY Å BO I. I hvilken grad...» **«Trives du i Oslo?»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q12_1` | Spørreskjema 2010, s. 2 |
| 2014 | 5, linje 1 | «Først vil vi stille noen spørsmål knyttet til din vurdering av OSLO SOM BY Å BO I. I hvilken grad...» **«Trives du i Oslo»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q5_1` | Rapport 2014, s. 62 |
| 2018 | 1, linje 1 | «I hvilken grad:» **«Trives du i Oslo?»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001__1` | Rapport 2018, s. 114 |
| 2023 | Q001, linje 1 | «I hvilken grad:» **«Trives du i Oslo?»** | – | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001#1` | Rapport 2023, s. 87 |
| 2026 | Q001, linje r1 | «Hvilken grad:» **«Trives du i Oslo?»** | «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad» | 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker | `Q001r1` | Metoderapport 2026, s. 15 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q001), ikke papirskjemaet (1).
- **2018, nettskjema** (Q001, Nettskjema 2018): Versjonen for dem som svarte på nett. Samme ordlyd og svaralternativer som papirskjemaet.
- **2026:** Innledningen står som «Hvilken grad:» i metoderapporten og i variabeletiketten i datafila. Metoderapporten viser ikke hvordan teksten så ut for respondentene.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q12_1` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila, men forekommer ikke. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2010 | `Q12_1` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila, men forekommer ikke. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2014 | `Q5_1` | 1–6 | 7 | tom | Kode −111 «[Ingen svar]» har etikett i fila, men brukes ikke. Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 20 svar per spørsmål, og regnes som manglende. |
| 2018 | `Q001__1` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q001#1` | 1–6 | 7 | 9996 og tom | 9996 (na) er deklarert som manglende verdi i datafila. Noen få svar er i tillegg tomme. |
| 2026 | `Q001r1` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Først vil vi komme med noen spørsmål knyttet til din vurdering av OSLO SOM BY Å BO I.» → «Først vil vi stille noen spørsmål knyttet til din vurdering av OSLO SOM BY Å BO I. I hvilken grad...»
- Instruksjon: «Vi ber deg svare langs en skala fra 1 til 6, der 1 betyr i svært liten grad, og 6 betyr i svært stor grad.» → «Merk: Sett ett kryss på hver linje»
- Spørsmålstekst: «Hvordan trives du i Oslo?» → «Trives du i Oslo?»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker → 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Spørsmålsformen ble endret fra «Hvordan trives du i Oslo?» til «I hvilken grad … Trives du i Oslo?». Skalaen og endepunktene er de samme, og meningsinnholdet er i praksis det samme. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre.

Grunnlag: Spørreskjema 2007, s. 1; Spørreskjema 2010, s. 2; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2010 → 2014: Med forbehold

Endret i skjemaet:

- Spørsmålstekst: «Trives du i Oslo?» → «Trives du i Oslo»

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden og skalaen er de samme, men målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Skjemaet ble samtidig kraftig forkortet, og feltarbeidet flyttet fra høst til vinter.

Grunnlag: Rapport 2010, s. 4; Rapport 2014, s. 3; Rapport 2018, s. 5. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2014 → 2018: Ja

Endret i skjemaet:

- Innledning: «Først vil vi stille noen spørsmål knyttet til din vurdering av OSLO SOM BY Å BO I. I hvilken grad...» → «I hvilken grad:»
- Spørsmålstekst: «Trives du i Oslo» → «Trives du i Oslo?»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** Samme spørsmål og skala. Innledningen ble forkortet til «I hvilken grad:», med samme mening. Andelen som svarte på nett økte fra 15 til 48 prosent, men innsamlingen var den samme som før: alle fikk papirskjemaet i posten og valgte selv om de ville svare på papir eller nett, og spørsmålet var likt i papir- og nettskjemaet. Rapporten for 2018 sier at datainnsamlingsmetode og vekting var lik tidligere år. Feltarbeidet flyttet fra vinter til vår; årstiden vurderes som lite relevant for trivsel i byen. Samlet gir dette ikke grunn til forbehold.

Grunnlag: Rapport 2014, s. 3–4; Rapport 2018, s. 5–6, 10, 114; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023: undersøkelsen ble i hovedsak en nettundersøkelse med invitasjon på e-post, utvalget ble trukket og vektet etter landbakgrunn, og innvandrere med under fem års botid var ikke med. Ordlyden og skalaen er de samme. Rapporten for 2023 konkluderer med at metodeendringen kan ha påvirket resultatene. Dette spørsmålet er et av dem der de to utvalgene i 2023 skilte seg: i det lille utvalget som fikk skjemaet i posten som før, svarte 83 prosent 5 eller 6, mot 76 prosent i det digitale hovedutvalget. Det er to utvalg samme år, ikke en endring over tid, og utvalgene hadde ulik alderssammensetning.

Grunnlag: Rapport 2023, s. 4, 7, 12, 19–21. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2023 → 2026: Ja

Endret i skjemaet:

- Innledning: «I hvilken grad:» → «Hvilken grad:»
- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker → 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Metoderapporten sier ikke om innvandrere med kort botid var med i utvalget.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode. Begge år var i hovedsak nettundersøkelser med invitasjon på e-post, med utvalg og vekting etter landbakgrunn og feltarbeid om våren. Endringene som gjorde overgangen til 2023 usikker, gjelder derfor begge årene. I 2026 var undersøkelsen bare på nett, der 2023 hadde et lite postalt utvalg i tillegg; kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret, og vektingen ble gjort med celler og raking. Svarprosenten er regnet på en ny måte, men det endrer ikke hvem som svarte. Metoderapporten sier ikke om innvandrere med under fem års botid var med i utvalget. Samlet gir dette ikke grunn til forbehold. Innledningen står som «Hvilken grad:» i metoderapporten for 2026, uten «I»; se merknaden til spørreskjemaet for 2026.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 15. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen i hovedsak gjennomført som nettundersøkelse med invitasjon på e-post. Tidligere ble spørreskjemaet sendt i posten, med mulighet for å svare på nett. Fra 2023 ble utvalget også trukket og vektet etter landbakgrunn. Rapporten for 2023 konkluderer med at endringen kan ha påvirket resultatene, i begge retninger. Tall fra 2023 og senere bør derfor sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Trygghet ute på kveldstid der du bor

Konsept-id: `trygghet_kveld_der_du_bor`. Hvor fornøyd man er med tryggheten når det gjelder å ferdes ute på kveldstid i området der man bor, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: ja.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 16, linje 6 | «Hvor fornøyd eller misfornøyd er du med. . . ?» «....der du bor» **«Trygghet når det gjelder å ferdes ute på kveldstid»** | «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA.» «For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker | `Q19_6` | Spørreskjema 2007, s. 5 |
| 2010 | 19, linje 6 | «Hvor fornøyd eller misfornøyd er du med. . .» «....der du bor» **«Trygghet når det gjelder å ferdes ute på kveldstid»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q19_6` | Spørreskjema 2010, s. 5 |
| 2014 | 12, linje 2 | «..der du bor» «Hvor fornøyd/misfornøyd er du med...» **«Trygghet når det gjelder å ferdes ute på kveldstid»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q12_2` | Rapport 2014, s. 64 |
| 2018 | 5, linje 4 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på kveldstid der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q007__4` | Rapport 2018, s. 115 |
| 2023 | Q004, linje 4 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på kveldstid der du bor»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q004#4` | Rapport 2023, s. 91 |
| 2026 | Q004, linje r4 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på kveldstid der du bor»** | «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd» | 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker | `Q004r4` | Metoderapport 2026, s. 20 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q007), ikke papirskjemaet (5).
- **2018, nettskjema** (Q007, Nettskjema 2018): Versjonen for dem som svarte på nett. Avvik fra papirskjemaet i innledning: «Hvor fornøyd/misfornøyd er du med ...» **«Trygghet når det gjelder å ferdes ute på kveldstid der du bor»**.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q19_6` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila, men forekommer ikke. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2010 | `Q19_6` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila, men forekommer ikke. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2014 | `Q12_2` | 1–6 | 7 | tom | Kode −111 «[Ingen svar]» har etikett i fila, men brukes ikke. Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 20 svar per spørsmål, og regnes som manglende. |
| 2018 | `Q007__4` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q004#4` | 1–6 | 7 | 9996 og tom | 9996 (na) er ikke deklarert som manglende verdi i datafila, i motsetning til på trivselsspørsmålet. Noen svar er i tillegg tomme. |
| 2026 | `Q004r4` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . ? / ....der du bor» → «Hvor fornøyd eller misfornøyd er du med. . . / ....der du bor»
- Instruksjon: «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA. / For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» → ingen
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker → 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Ordlyden, batteriet og skalaen er de samme. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre. Endringen gjelder alle spørsmål og vises derfor også her. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 5; Spørreskjema 2010, s. 5; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2010 → 2014: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . / ....der du bor» → «..der du bor / Hvor fornøyd/misfornøyd er du med...»
- Instruksjon: ingen → «Merk: Sett ett kryss på hver linje»

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden, batteriet (med linjene om politiets innsats) og skalaen er de samme. Målgruppen ble endret til 18 år og eldre. Feltarbeidet flyttet fra høst til vinter; begge årstider har mørke kvelder.

Grunnlag: Spørreskjema 2010, s. 5; Rapport 2010, s. 4; Rapport 2014, s. 3, 64. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2014 → 2018: Med forbehold

Endret i skjemaet:

- Innledning: «..der du bor / Hvor fornøyd/misfornøyd er du med...» → «Hvor fornøyd/misfornøyd er du med:»
- Spørsmålstekst: «Trygghet når det gjelder å ferdes ute på kveldstid» → «Trygghet når det gjelder å ferdes ute på kveldstid der du bor»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** «der du bor» ble flyttet fra en underoverskrift inn i linjeteksten, og linjene om politiets innsats ble tatt ut av batteriet. Meningen er den samme, men sammenhengen i skjemaet er en annen. Feltarbeidet flyttet fra januar–mars til mars–mai, altså fra mørke til lysere kvelder. Hvilken betydning det har, er ikke målt.

Grunnlag: Rapport 2014, s. 3, 64; Rapport 2018, s. 5, 115. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Ordlyden og skalaen er de samme, og feltarbeidet var om våren begge år. Rapporten for 2023 ber om varsomhet ved sammenligning over tid.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 21. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

#### 2023 → 2026: Ja

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Metoderapporten sier ikke om innvandrere med kort botid var med i utvalget.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode. Begge år var i hovedsak nettundersøkelser med invitasjon på e-post, med utvalg og vekting etter landbakgrunn og feltarbeid om våren. Endringene som gjorde overgangen til 2023 usikker, gjelder derfor begge årene. Svarprosenten i 2026 er regnet på en ny måte, men det endrer ikke hvem som svarte. Metoderapporten sier ikke om innvandrere med under fem års botid var med i utvalget. Samlet gir dette ikke grunn til forbehold.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 20. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen i hovedsak gjennomført som nettundersøkelse med invitasjon på e-post. Tidligere ble spørreskjemaet sendt i posten, med mulighet for å svare på nett. Fra 2023 ble utvalget også trukket og vektet etter landbakgrunn. Rapporten for 2023 konkluderer med at endringen kan ha påvirket resultatene, i begge retninger. Tall fra 2023 og senere bør derfor sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Trygghet ute på dagtid der du bor

Konsept-id: `trygghet_dag_der_du_bor`. Hvor fornøyd man er med tryggheten når det gjelder å ferdes ute på dagtid i området der man bor, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: ja.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 16, linje 5 | «Hvor fornøyd eller misfornøyd er du med. . . ?» «....der du bor» **«Trygghet når det gjelder å ferdes ute på dagtid»** | «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA.» «For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker | `Q19_5` | Spørreskjema 2007, s. 5 |
| 2010 | 19, linje 5 | «Hvor fornøyd eller misfornøyd er du med. . .» «....der du bor» **«Trygghet når det gjelder å ferdes ute på dagtid»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q19_5` | Spørreskjema 2010, s. 5 |
| 2014 | 12, linje 1 | «..der du bor» «Hvor fornøyd/misfornøyd er du med...» **«Trygghet når det gjelder å ferdes ute på dagtid»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q12_1` | Rapport 2014, s. 64 |
| 2018 | 5, linje 3 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på dagtid der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q007__3` | Rapport 2018, s. 115 |
| 2023 | Q004, linje 3 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på dagtid der du bor»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q004#3` | Rapport 2023, s. 91 |
| 2026 | Q004, linje r3 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på dagtid der du bor»** | «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd» | 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker | `Q004r3` | Metoderapport 2026, s. 20 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q007), ikke papirskjemaet (5).
- **2018, nettskjema** (Q007, Nettskjema 2018): Versjonen for dem som svarte på nett. Avvik fra papirskjemaet i innledning: «Hvor fornøyd/misfornøyd er du med ...» **«Trygghet når det gjelder å ferdes ute på dagtid der du bor»**.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q19_5` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila. Svar uten gyldig verdi er tomme. Variabelen er plassert etter rekkefølgen i skjemaet, der blokken «der du bor» står etter blokken «i Oslo sentrum», og plasseringen er bekreftet mot andelen som er publisert i rapporten for 2007. |
| 2010 | `Q19_5` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila. Svar uten gyldig verdi er tomme. Variabelen er plassert etter rekkefølgen i skjemaet, der blokken «der du bor» står etter blokken «i Oslo sentrum», og plasseringen er bekreftet mot andelen som er publisert i rapporten for 2007. |
| 2014 | `Q12_1` | 1–6 | 7 | tom | – |
| 2018 | `Q007__3` | 1–6 | 7 | 8 | – |
| 2023 | `Q004#3` | 1–6 | 7 | 9996 og tom | – |
| 2026 | `Q004r3` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . ? / ....der du bor» → «Hvor fornøyd eller misfornøyd er du med. . . / ....der du bor»
- Instruksjon: «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA. / For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» → ingen
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker → 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Ordlyden, batteriet og skalaen er de samme. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre. Endringen gjelder alle spørsmål og vises derfor også her. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 5; Spørreskjema 2010, s. 5; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2010 → 2014: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . / ....der du bor» → «..der du bor / Hvor fornøyd/misfornøyd er du med...»
- Instruksjon: ingen → «Merk: Sett ett kryss på hver linje»

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden, batteriet (med linjene om politiets innsats) og skalaen er de samme. Målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Feltarbeidet flyttet fra høst til vinter.

Grunnlag: Spørreskjema 2010, s. 5; Rapport 2010, s. 4; Rapport 2014, s. 3, 64. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2014 → 2018: Med forbehold

Endret i skjemaet:

- Innledning: «..der du bor / Hvor fornøyd/misfornøyd er du med...» → «Hvor fornøyd/misfornøyd er du med:»
- Spørsmålstekst: «Trygghet når det gjelder å ferdes ute på dagtid» → «Trygghet når det gjelder å ferdes ute på dagtid der du bor»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** «der du bor» ble flyttet fra en underoverskrift inn i linjeteksten, og linjene om politiets innsats ble tatt ut av batteriet. Meningen er den samme, men sammenhengen i skjemaet er en annen, som for trygghet på kveldstid. Feltarbeidet flyttet fra vinter (januar–mars) til vår (mars–mai). Rapporten for 2018 sammenligner selv med 2014.

Grunnlag: Rapport 2014, s. 3, 64; Rapport 2018, s. 5, 49, 115; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Ordlyden, batteriet og skalaen er de samme, og feltarbeidet var om våren begge år. Rapporten for 2023 ber om varsomhet ved sammenligning over tid.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 91. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2023 → 2026: Ja

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Metoderapporten sier ikke om innvandrere med kort botid var med i utvalget.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode. Begge år var i hovedsak nettundersøkelser med invitasjon på e-post, med utvalg og vekting etter landbakgrunn og feltarbeid om våren. Endringene som gjorde overgangen til 2023 usikker, gjelder derfor begge årene. Svarprosenten i 2026 er regnet på en ny måte, men det endrer ikke hvem som svarte. Metoderapporten sier ikke om innvandrere med under fem års botid var med i utvalget. Samlet gir dette ikke grunn til forbehold.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 20. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen i hovedsak gjennomført som nettundersøkelse med invitasjon på e-post. Tidligere ble spørreskjemaet sendt i posten, med mulighet for å svare på nett. Fra 2023 ble utvalget også trukket og vektet etter landbakgrunn. Rapporten for 2023 konkluderer med at endringen kan ha påvirket resultatene, i begge retninger. Tall fra 2023 og senere bør derfor sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Tilgang til natur- og friluftsområder der du bor

Konsept-id: `natur_friluft_der_du_bor`. Hvor fornøyd man er med tilgangen til natur- og friluftsområder i området der man bor, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: ja.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 13, linje 7 | «Hvor fornøyd/misfornøyd er du når det gjelder. . . ?» **«Tilgang til natur- og friluftsområder i bydelen»** | «Vi ber deg nå vurdere nærmere ulike forhold knyttet til BYDELEN OG OMRÅDET DU BOR I.» «For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker | `Q15_2` | Spørreskjema 2007, s. 3 |
| 2010 | 15, linje 2 | «NÆRMERE VURDERING AV BYDELEN OG OMRÅDET DER DU BOR. Hvor fornøyd/misfornøyd er du når det gjelder...» **«Tilgang til natur- og friluftsområder i bydelen»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q15_2` | Spørreskjema 2010, s. 3 |
| 2014 | 7, linje 1 | «NÆRMERE VURDERING AV OMRÅDET DER DU BOR. Hvor fornøyd/misfornøyd er du når det gjelder...» **«Tilgang til natur- og friluftsområder i bydelen der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q7_1` | Rapport 2014, s. 62 |
| 2018 | 2, linje 1 | «Hvor fornøyd/misfornøyd er du med:» **«Tilgang til natur- og friluftsområder der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q002__1` | Rapport 2018, s. 114 |
| 2023 | Q007, linje 12 | «Hvor fornøyd/misfornøyd er du med:» **«Tilgang til natur- og friluftsområder der du bor»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q007#12` | Rapport 2023, s. 93 |
| 2026 | Q006, linje r11 | «Hvor fornøyd/misfornøyd er du med:» **«Tilgang til natur- og friluftsområder der du bor»** | «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd» | 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker | `Q006r11` | Metoderapport 2026, s. 21 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q002), ikke papirskjemaet (2).
- **2018, nettskjema** (Q002, Nettskjema 2018): Versjonen for dem som svarte på nett. Samme ordlyd og svaralternativer som papirskjemaet.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q15_2` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila. Svar uten gyldig verdi er tomme. |
| 2010 | `Q15_2` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Kodene 7 (Ikke sikker) og 8 (Ubesvart) har etikett i fila. Svar uten gyldig verdi er tomme. |
| 2014 | `Q7_1` | 1–6 | 7 | tom | Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 10 svar, og regnes som manglende. |
| 2018 | `Q002__1` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q007#12` | 1–6 | 7 | 9996 | Ubesvart er kodet 9996; i tillegg er noen få svar tomme. |
| 2026 | `Q006r11` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd/misfornøyd er du når det gjelder. . . ?» → «NÆRMERE VURDERING AV BYDELEN OG OMRÅDET DER DU BOR. Hvor fornøyd/misfornøyd er du når det gjelder...»
- Instruksjon: «Vi ber deg nå vurdere nærmere ulike forhold knyttet til BYDELEN OG OMRÅDET DU BOR I. / For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» → «Merk: Sett ett kryss på hver linje»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker → 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Linjeteksten og skalaen er de samme, og spørsmålet står i det samme batteriet om bydelen og området der man bor. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre. Endringen gjelder alle spørsmål og vises derfor også her. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 3; Spørreskjema 2010, s. 3; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2010 → 2014: Med forbehold

Endret i skjemaet:

- Innledning: «NÆRMERE VURDERING AV BYDELEN OG OMRÅDET DER DU BOR. Hvor fornøyd/misfornøyd er du når det gjelder...» → «NÆRMERE VURDERING AV OMRÅDET DER DU BOR. Hvor fornøyd/misfornøyd er du når det gjelder...»
- Spørsmålstekst: «Tilgang til natur- og friluftsområder i bydelen» → «Tilgang til natur- og friluftsområder i bydelen der du bor»

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Linjeteksten ble endret fra «… i bydelen» til «… i bydelen der du bor», og overskriften på batteriet nevner ikke lenger bydelen, bare området der man bor. Meningen er den samme, med et presisert sted. Målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Feltarbeidet flyttet fra høst til vinter.

Grunnlag: Spørreskjema 2010, s. 3; Rapport 2010, s. 4; Rapport 2014, s. 3, 62. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2014 → 2018: Med forbehold

Endret i skjemaet:

- Innledning: «NÆRMERE VURDERING AV OMRÅDET DER DU BOR. Hvor fornøyd/misfornøyd er du når det gjelder...» → «Hvor fornøyd/misfornøyd er du med:»
- Spørsmålstekst: «Tilgang til natur- og friluftsområder i bydelen der du bor» → «Tilgang til natur- og friluftsområder der du bor»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** Linjeteksten ble endret fra «… i bydelen der du bor» til «… der du bor». Spørsmålet står rett etter spørsmålene om trivsel begge år; nummeret endret seg fordi bakgrunnsspørsmålene ble flyttet til slutten av skjemaet, og i papirskjemaet falt overskriften om området der du bor, bort. «Der du bor» uten «i bydelen» kan leses som et litt annet område, men rapporten for 2018 sammenligner selv med 2014 og behandler det som samme spørsmål. Feltarbeidet flyttet fra vinter til vår.

Grunnlag: Rapport 2014, s. 3, 62; Rapport 2018, s. 5, 31, 114, 118; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Linjeteksten og skalaen er de samme, men spørsmålet ble flyttet til batteriet «Nå noen spørsmål om miljø», med et nytt ledd om tilgangen i Osloområdet generelt rett etter. Rapporten for 2023 viser ikke tidligere år i figuren for dette spørsmålet og begrunner det i en fotnote: «Spørsmålet ble stilt i en annen del av undersøkelsen og resultater fra foregående år vises derfor ikke i grafen.» I teksten sammenligner rapporten likevel med tidligere år. Rapporten sier også at det postale utvalget var mer fornøyd enn det digitale med tilgangen til natur- og friluftsområder der de bor (s. 21). Spørsmålet måler det samme, men flyttingen kan ha påvirket tallene. Feltarbeidet var om våren begge år.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 21, 47, 93. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

#### 2023 → 2026: Ja

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Metoderapporten sier ikke om innvandrere med kort botid var med i utvalget.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode. Spørsmålet står i batteriet om miljø begge år, foran leddet om Osloområdet generelt. Begge år var i hovedsak nettundersøkelser med invitasjon på e-post, med utvalg og vekting etter landbakgrunn og feltarbeid om våren. Endringene som gjorde overgangen til 2023 usikker, gjelder derfor begge årene. Svarprosenten i 2026 er regnet på en ny måte, men det endrer ikke hvem som svarte. Metoderapporten sier ikke om innvandrere med under fem års botid var med i utvalget. Samlet gir dette ikke grunn til forbehold.

Grunnlag: Rapport 2023, s. 4, 7, 12, 93; Metoderapport 2026, s. 1–4, 7, 21. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen i hovedsak gjennomført som nettundersøkelse med invitasjon på e-post. Tidligere ble spørreskjemaet sendt i posten, med mulighet for å svare på nett. Fra 2023 ble utvalget også trukket og vektet etter landbakgrunn. Rapporten for 2023 konkluderer med at endringen kan ha påvirket resultatene, i begge retninger. Tall fra 2023 og senere bør derfor sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen
