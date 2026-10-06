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
- [Pent i området der du bor](#pent-i-området-der-du-bor)
- [Utendørs møteplasser der du bor](#utendørs-møteplasser-der-du-bor)
- [Godt nabofellesskap](#godt-nabofellesskap)
- [Trygghet ute på dagtid i Oslo sentrum](#trygghet-ute-på-dagtid-i-oslo-sentrum)
- [Trygghet ute på kveldstid i Oslo sentrum](#trygghet-ute-på-kveldstid-i-oslo-sentrum)

## Trivsel i Oslo

Konsept-id: `trives_oslo`. Hvor godt man trives i Oslo, på en skala fra 1 (i svært liten grad) til 6 (i svært stor grad).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: ja · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

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
| 2023 | `Q001#1` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»), som er deklarert som manglende verdi i datafila; det gjelder 124 av 28 851 svar, og 4 svar er tomme. 129 svarte «Ikke sikker» (kode 7). |
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

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Innledning: «I hvilken grad:» → «Hvilken grad:»
- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker → 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte. Innledningen står som «Hvilken grad:» i metoderapporten for 2026, uten «I»; se merknaden til spørreskjemaet for 2026.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 15; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Trygghet ute på kveldstid der du bor

Konsept-id: `trygghet_kveld_der_du_bor`. Hvor fornøyd man er med tryggheten når det gjelder å ferdes ute på kveldstid i området der man bor, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

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
| 2023 | `Q004#4` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); på dette spørsmålet er koden ikke deklarert som manglende verdi i datafila, i motsetning til på trivselsspørsmålet. Det gjelder 348 av 28 851 svar, og 24 svar er tomme. 296 svarte «Ikke sikker» (kode 7). |
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

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 20; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 23. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Trygghet ute på dagtid der du bor

Konsept-id: `trygghet_dag_der_du_bor`. Hvor fornøyd man er med tryggheten når det gjelder å ferdes ute på dagtid i området der man bor, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

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
| 2023 | `Q004#3` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); det gjelder 223 av 28 851 svar, og 14 svar er tomme. 89 svarte «Ikke sikker» (kode 7). |
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

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 20; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Tilgang til natur- og friluftsområder der du bor

Konsept-id: `natur_friluft_der_du_bor`. Hvor fornøyd man er med tilgangen til natur- og friluftsområder i området der man bor, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

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
| 2023 | `Q007#12` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); det gjelder 321 av 28 851 svar, og 23 svar er tomme. 173 svarte «Ikke sikker» (kode 7). |
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

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte. Spørsmålet står i batteriet om miljø begge år, foran leddet om Osloområdet generelt.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 21; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 30. september 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Pent i området der du bor

Konsept-id: `pent_der_du_bor`. I hvilken grad man synes det er pent i området der man bor, på en skala fra 1 (i svært liten grad) til 6 (i svært stor grad).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: ja · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 12, linje 4 | «Så vil vi komme med noen spørsmål knyttet til din vurdering av OMRÅDET DER DU BOR.» **«Er det pent i området der du bor?»** | – | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker | `Q14_4` | Spørreskjema 2007, s. 2 |
| 2010 | 14, linje 4 | «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» **«Er det pent i området der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q14_4` | Spørreskjema 2010, s. 2 |
| 2014 | 6, linje 3 | «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» **«Er det pent i området der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q6_3` | Rapport 2014, s. 62 |
| 2018 | 1, linje 3 | «I hvilken grad:» **«Er det pent i området der du bor?»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001__3` | Rapport 2018, s. 114 |
| 2023 | Q001, linje 5 | «I hvilken grad:» **«Er det pent i området der du bor?»** | – | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001#5` | Rapport 2023, s. 87 |
| 2026 | Q001, linje r5 | «Hvilken grad:» **«Er det pent i området der du bor?»** | «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad» | 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker | `Q001r5` | Metoderapport 2026, s. 15 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q001), ikke papirskjemaet (1).
- **2018, nettskjema** (Q001, Nettskjema 2018): Versjonen for dem som svarte på nett. Samme ordlyd og svaralternativer som papirskjemaet.
- **2026:** Innledningen står som «Hvilken grad:» i metoderapporten og i variabeletiketten i datafila. Metoderapporten viser ikke hvordan teksten så ut for respondentene.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q14_4` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2010 | `Q14_4` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2014 | `Q6_3` | 1–6 | 7 | tom | Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 20 svar, og regnes som manglende. |
| 2018 | `Q001__3` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q001#5` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); det gjelder 336 av 28 851 svar, og 15 svar er tomme. 43 svarte «Ikke sikker» (kode 7). |
| 2026 | `Q001r5` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Så vil vi komme med noen spørsmål knyttet til din vurdering av OMRÅDET DER DU BOR.» → «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...»
- Instruksjon: ingen → «Merk: Sett ett kryss på hver linje»
- Spørsmålstekst: «Er det pent i området der du bor?» → «Er det pent i området der du bor»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker → 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Ordlyden og skalaen er de samme. To ledd om naboene, som sto etter dette spørsmålet, ble tatt ut av batteriet. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre. Endringen gjelder alle spørsmål og vises derfor også her. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 2; Spørreskjema 2010, s. 2; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2010 → 2014: Med forbehold

Ingen endring i ordlyd eller svaralternativer.

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden og skalaen er de samme. Batteriet om området der man bor ble kortet ned fra sju til fem ledd. Målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Feltarbeidet flyttet fra høst til vinter.

Grunnlag: Spørreskjema 2010, s. 2; Rapport 2010, s. 4; Rapport 2014, s. 3, 62. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2014 → 2018: Ja

Endret i skjemaet:

- Innledning: «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» → «I hvilken grad:»
- Spørsmålstekst: «Er det pent i området der du bor» → «Er det pent i området der du bor?»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** Batteriet om området der man bor ble slått sammen med spørsmålet om trivsel i Oslo, under innledningen «I hvilken grad:». Leddene og skalaen er de samme, og stedet står i hvert ledd. Det er samme endring som for trivsel i Oslo, og innsamlingen var den samme som før; se vurderingen for trivsel. Feltarbeidet flyttet fra vinter til vår.

Grunnlag: Rapport 2014, s. 3–4, 62; Rapport 2018, s. 5–6, 114; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Ordlyden og skalaen er de samme, og feltarbeidet var om våren begge år. To nye ledd om tilhørighet til Oslo og til området der man bor kom inn i batteriet. Rapporten for 2023 ber om varsomhet ved sammenligning over tid.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 87. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Innledning: «I hvilken grad:» → «Hvilken grad:»
- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker → 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte. Innledningen står som «Hvilken grad:» i metoderapporten for 2026, uten «I»; se merknaden til spørreskjemaet for 2026.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 15; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 6. oktober 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Utendørs møteplasser der du bor

Konsept-id: `moteplasser_der_du_bor`. I hvilken grad man mener det finnes utendørs møteplasser som er fristende å bruke i området der man bor, på en skala fra 1 (i svært liten grad) til 6 (i svært stor grad).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: ja · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 12, linje 5 | «Så vil vi komme med noen spørsmål knyttet til din vurdering av OMRÅDET DER DU BOR.» **«I hvilken grad finnes det utendørs møteplasser som er fristende å bruke i området der du bor?»** | – | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker | `Q14_5` | Spørreskjema 2007, s. 2 |
| 2010 | 14, linje 5 | «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» **«Finnes det utendørs møteplasser som er fristende å bruke i området der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q14_5` | Spørreskjema 2010, s. 2 |
| 2014 | 6, linje 4 | «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» **«Finnes det utendørs møteplasser som er fristende å bruke i området der du bor»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q6_4` | Rapport 2014, s. 62 |
| 2018 | 1, linje 4 | «I hvilken grad:» **«Finnes det utendørs møteplasser som er fristende å bruke i området der du bor?»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001__4` | Rapport 2018, s. 114 |
| 2023 | Q001, linje 6 | «I hvilken grad:» **«Finnes det utendørs møteplasser som er fristende å bruke i området der du bor?»** | – | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001#6` | Rapport 2023, s. 87 |
| 2026 | Q001, linje r6 | «Hvilken grad:» **«Finnes det utendørs møteplasser som er fristende å bruke i området der du bor?»** | «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad» | 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker | `Q001r6` | Metoderapport 2026, s. 15 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q001), ikke papirskjemaet (1).
- **2018, nettskjema** (Q001, Nettskjema 2018): Versjonen for dem som svarte på nett. Samme ordlyd og svaralternativer som papirskjemaet.
- **2026:** Innledningen står som «Hvilken grad:» i metoderapporten og i variabeletiketten i datafila. Metoderapporten viser ikke hvordan teksten så ut for respondentene.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q14_5` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2010 | `Q14_5` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2014 | `Q6_4` | 1–6 | 7 | tom | Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 10 svar, og regnes som manglende. |
| 2018 | `Q001__4` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q001#6` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); det gjelder 684 av 28 851 svar, og 23 svar er tomme. 273 svarte «Ikke sikker» (kode 7). |
| 2026 | `Q001r6` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Så vil vi komme med noen spørsmål knyttet til din vurdering av OMRÅDET DER DU BOR.» → «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...»
- Instruksjon: ingen → «Merk: Sett ett kryss på hver linje»
- Spørsmålstekst: «I hvilken grad finnes det utendørs møteplasser som er fristende å bruke i området der du bor?» → «Finnes det utendørs møteplasser som er fristende å bruke i området der du bor»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker → 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Spørsmålet «I hvilken grad finnes det utendørs møteplasser …?» ble til leddet «Finnes det utendørs møteplasser …» under den felles innledningen «I hvilken grad...». Meningen er den samme. To ledd om naboene, som sto etter dette spørsmålet, ble tatt ut av batteriet. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre. Endringen gjelder alle spørsmål og vises derfor også her. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 2; Spørreskjema 2010, s. 2; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2010 → 2014: Med forbehold

Ingen endring i ordlyd eller svaralternativer.

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden og skalaen er de samme. Batteriet om området der man bor ble kortet ned fra sju til fem ledd. Målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Feltarbeidet flyttet fra høst til vinter.

Grunnlag: Spørreskjema 2010, s. 2; Rapport 2010, s. 4; Rapport 2014, s. 3, 62. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2014 → 2018: Ja

Endret i skjemaet:

- Innledning: «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» → «I hvilken grad:»
- Spørsmålstekst: «Finnes det utendørs møteplasser som er fristende å bruke i området der du bor» → «Finnes det utendørs møteplasser som er fristende å bruke i området der du bor?»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** Batteriet om området der man bor ble slått sammen med spørsmålet om trivsel i Oslo, under innledningen «I hvilken grad:». Leddene og skalaen er de samme, og stedet står i hvert ledd. Det er samme endring som for trivsel i Oslo, og innsamlingen var den samme som før; se vurderingen for trivsel. Feltarbeidet flyttet fra vinter til vår. Rapporten for 2018 sammenligner selv med 2014.

Grunnlag: Rapport 2014, s. 3–4, 62; Rapport 2018, s. 5–6, 24, 114; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Ordlyden og skalaen er de samme, og feltarbeidet var om våren begge år. To nye ledd om tilhørighet til Oslo og til området der man bor kom inn i batteriet. Rapporten for 2023 ber om varsomhet ved sammenligning over tid.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 87. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Innledning: «I hvilken grad:» → «Hvilken grad:»
- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker → 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte. Innledningen står som «Hvilken grad:» i metoderapporten for 2026, uten «I»; se merknaden til spørreskjemaet for 2026.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 15; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 6. oktober 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Godt nabofellesskap

Konsept-id: `nabofellesskap`. I hvilken grad man opplever å være en del av et godt nabofellesskap, på en skala fra 1 (i svært liten grad) til 6 (i svært stor grad).

**Serien:** 2007 → 2010: nei · 2010 → 2014: med forbehold · 2014 → 2018: ja · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 12, linje 8 | «Så vil vi komme med noen spørsmål knyttet til din vurdering av OMRÅDET DER DU BOR.» **«I hvilken grad er du en del av et godt nabofelleskap?»** | – | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker | `Q14_6` | Spørreskjema 2007, s. 2 |
| 2010 | 14, linje 6 | «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» **«Er du en del av et godt nabofelleskap»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q14_6` | Spørreskjema 2010, s. 2 |
| 2014 | 6, linje 5 | «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» **«Er du en del av et godt nabofelleskap»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q6_5` | Rapport 2014, s. 62 |
| 2018 | 1, linje 5 | «I hvilken grad:» **«Er du en del av et godt nabofelleskap?»** | «Merk: Sett ett kryss på hver linje» | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001__6` | Rapport 2018, s. 114 |
| 2023 | Q001, linje 7 | «I hvilken grad:» **«Er du en del av et godt nabofellesskap?»** | – | 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker | `Q001#7` | Rapport 2023, s. 87 |
| 2026 | Q001, linje r7 | «Hvilken grad:» **«Er du en del av et godt nabofellesskap?»** | «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad» | 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker | `Q001r7` | Metoderapport 2026, s. 15 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q001), ikke papirskjemaet (1).
- **2018, nettskjema** (Q001, Nettskjema 2018): Versjonen for dem som svarte på nett. Samme ordlyd og svaralternativer som papirskjemaet.
- **2026:** Innledningen står som «Hvilken grad:» i metoderapporten og i variabeletiketten i datafila. Metoderapporten viser ikke hvordan teksten så ut for respondentene.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q14_6` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2010 | `Q14_6` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2014 | `Q6_5` | 1–6 | 7 | tom | Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 10 svar, og regnes som manglende. |
| 2018 | `Q001__6` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q001#7` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); det gjelder 280 av 28 851 svar, og færre enn 10 svar er tomme. 371 svarte «Ikke sikker» (kode 7). |
| 2026 | `Q001r7` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Nei

Endret i skjemaet:

- Innledning: «Så vil vi komme med noen spørsmål knyttet til din vurdering av OMRÅDET DER DU BOR.» → «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...»
- Instruksjon: ingen → «Merk: Sett ett kryss på hver linje»
- Spørsmålstekst: «I hvilken grad er du en del av et godt nabofelleskap?» → «Er du en del av et godt nabofelleskap»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; 7 = Ikke sikker → 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Spørsmålet er det samme, men i 2007 sto det rett etter to spørsmål om kontakten mellom naboene og om man selv tar initiativ til samvær med naboene. De to spørsmålene ble tatt ut i 2010. Andelen som svarte 5 eller 6, økte fra 31 til 46 prosent, mer enn for noe annet spørsmål i batteriet, og endringen i målgruppen forklarer det ikke. Tallet for 2007 kan derfor ikke leses som samme mål som tallene fra 2010. Målgruppen ble også utvidet fra 15–80 år til 15 år og eldre. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 2; Spørreskjema 2010, s. 2; Rapport 2007, s. 3, 22–23; Rapport 2010, s. 4, 21. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2010 → 2014: Med forbehold

Ingen endring i ordlyd eller svaralternativer.

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden og skalaen er de samme. Batteriet om området der man bor ble kortet ned fra sju til fem ledd. Målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Feltarbeidet flyttet fra høst til vinter.

Grunnlag: Spørreskjema 2010, s. 2; Rapport 2010, s. 4; Rapport 2014, s. 3, 62. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2014 → 2018: Ja

Endret i skjemaet:

- Innledning: «DIN VURDERING AV OMRÅDET DER DU BOR. I hvilken grad...» → «I hvilken grad:»
- Spørsmålstekst: «Er du en del av et godt nabofelleskap» → «Er du en del av et godt nabofelleskap?»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** Batteriet om området der man bor ble slått sammen med spørsmålet om trivsel i Oslo, under innledningen «I hvilken grad:». Leddene og skalaen er de samme, og stedet står i hvert ledd. Det er samme endring som for trivsel i Oslo, og innsamlingen var den samme som før; se vurderingen for trivsel. Feltarbeidet flyttet fra vinter til vår. Rapporten for 2018 sammenligner selv med 2014.

Grunnlag: Rapport 2014, s. 3–4, 62; Rapport 2018, s. 5–6, 17, 114; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen
- Spørsmålstekst: «Er du en del av et godt nabofelleskap?» → «Er du en del av et godt nabofellesskap?»

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Ordlyden og skalaen er de samme, og feltarbeidet var om våren begge år. To nye ledd om tilhørighet til Oslo og til området der man bor kom inn i batteriet. Skrivemåten ble rettet fra «nabofelleskap» til «nabofellesskap». Rapporten for 2023 ber om varsomhet ved sammenligning over tid.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 87. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Innledning: «I hvilken grad:» → «Hvilken grad:»
- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er i svært liten grad og 6 er i svært stor grad»
- Svaralternativer: 1 = I svært liten grad; 2; 3; 4; 5; 6 = I svært stor grad; Ikke sikker → 1 = 1 - I svært liten grad; 2; 3; 4; 5; 6 = 6 - I svært stor grad; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte. Innledningen står som «Hvilken grad:» i metoderapporten for 2026, uten «I»; se merknaden til spørreskjemaet for 2026.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 15; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 6. oktober 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Trygghet ute på dagtid i Oslo sentrum

Konsept-id: `trygghet_dag_sentrum`. Hvor fornøyd man er med tryggheten når det gjelder å ferdes ute på dagtid i Oslo sentrum, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 16, linje 1 | «Hvor fornøyd eller misfornøyd er du med. . . ?» «....i Oslo sentrum» **«Trygghet når det gjelder å ferdes ute på dagtid»** | «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA.» «For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker | `Q19_1` | Spørreskjema 2007, s. 5 |
| 2010 | 19, linje 1 | «Hvor fornøyd eller misfornøyd er du med. . .» «....i Oslo sentrum» **«Trygghet når det gjelder å ferdes ute på dagtid»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q19_1` | Spørreskjema 2010, s. 5 |
| 2014 | 11, linje 1 | «..i Oslo sentrum» «Hvor fornøyd/misfornøyd er du med...» **«Trygghet når det gjelder å ferdes ute på dagtid»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q11_1` | Rapport 2014, s. 64 |
| 2018 | 5, linje 1 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på dagtid i Oslo sentrum»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q007__1` | Rapport 2018, s. 115 |
| 2023 | Q004, linje 1 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på dagtid i Oslo sentrum»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q004#1` | Rapport 2023, s. 91 |
| 2026 | Q004, linje r1 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på dagtid i Oslo sentrum»** | «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd» | 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker | `Q004r1` | Metoderapport 2026, s. 20 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q007), ikke papirskjemaet (5).
- **2018, nettskjema** (Q007, Nettskjema 2018): Versjonen for dem som svarte på nett. Avvik fra papirskjemaet i innledning: «Hvor fornøyd/misfornøyd er du med ...» **«Trygghet når det gjelder å ferdes ute på dagtid i Oslo sentrum»**.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q19_1` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2010 | `Q19_1` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2014 | `Q11_1` | 1–6 | 7 | tom | Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 20 svar, og regnes som manglende. |
| 2018 | `Q007__1` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q004#1` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); det gjelder 163 av 28 851 svar, og 13 svar er tomme. 304 svarte «Ikke sikker» (kode 7). |
| 2026 | `Q004r1` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . ? / ....i Oslo sentrum» → «Hvor fornøyd eller misfornøyd er du med. . . / ....i Oslo sentrum»
- Instruksjon: «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA. / For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» → ingen
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker → 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Ordlyden, batteriet og skalaen er de samme. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre. Endringen gjelder alle spørsmål og vises derfor også her. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 5; Spørreskjema 2010, s. 5; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2010 → 2014: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . / ....i Oslo sentrum» → «..i Oslo sentrum / Hvor fornøyd/misfornøyd er du med...»
- Instruksjon: ingen → «Merk: Sett ett kryss på hver linje»

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden og skalaen er de samme, og linjene om politiets innsats står fortsatt i batteriet. Linjene om Oslo sentrum og om området der man bor ble skilt i to spørsmål med de samme linjene. Målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Feltarbeidet flyttet fra høst til vinter.

Grunnlag: Spørreskjema 2010, s. 5; Rapport 2010, s. 4; Rapport 2014, s. 3, 64. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2014 → 2018: Med forbehold

Endret i skjemaet:

- Innledning: «..i Oslo sentrum / Hvor fornøyd/misfornøyd er du med...» → «Hvor fornøyd/misfornøyd er du med:»
- Spørsmålstekst: «Trygghet når det gjelder å ferdes ute på dagtid» → «Trygghet når det gjelder å ferdes ute på dagtid i Oslo sentrum»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** «i Oslo sentrum» ble flyttet fra en underoverskrift inn i linjeteksten, og linjene om politiets innsats ble tatt ut av batteriet. Meningen er den samme, men sammenhengen i skjemaet er en annen, som for trygghet der man bor. Feltarbeidet flyttet fra vinter (januar–mars) til vår (mars–mai).

Grunnlag: Rapport 2014, s. 3, 64; Rapport 2018, s. 5, 115; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Ordlyden, batteriet og skalaen er de samme, og feltarbeidet var om våren begge år. Rapporten for 2023 ber om varsomhet ved sammenligning over tid.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 91. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 20; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 6. oktober 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen

## Trygghet ute på kveldstid i Oslo sentrum

Konsept-id: `trygghet_kveld_sentrum`. Hvor fornøyd man er med tryggheten når det gjelder å ferdes ute på kveldstid i Oslo sentrum, på en skala fra 1 (svært misfornøyd) til 6 (svært fornøyd).

**Serien:** 2007 → 2010: med forbehold · 2010 → 2014: med forbehold · 2014 → 2018: med forbehold · 2018 → 2023: med forbehold · 2023 → 2026: med forbehold.

### Ordlyd per utgave

| Utgave | Spm. | Ordlyd | Instruksjon | Svaralternativer | Variabel i datafila | Kilde |
|---|---|---|---|---|---|---|
| 2007 | 16, linje 2 | «Hvor fornøyd eller misfornøyd er du med. . . ?» «....i Oslo sentrum» **«Trygghet når det gjelder å ferdes ute på kveldstid»** | «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA.» «For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker | `Q19_2` | Spørreskjema 2007, s. 5 |
| 2010 | 19, linje 2 | «Hvor fornøyd eller misfornøyd er du med. . .» «....i Oslo sentrum» **«Trygghet når det gjelder å ferdes ute på kveldstid»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q19_2` | Spørreskjema 2010, s. 5 |
| 2014 | 11, linje 2 | «..i Oslo sentrum» «Hvor fornøyd/misfornøyd er du med...» **«Trygghet når det gjelder å ferdes ute på kveldstid»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q11_2` | Rapport 2014, s. 64 |
| 2018 | 5, linje 2 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på kveldstid i Oslo sentrum»** | «Merk: Sett ett kryss på hver linje» | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q007__2` | Rapport 2018, s. 115 |
| 2023 | Q004, linje 2 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på kveldstid i Oslo sentrum»** | – | 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker | `Q004#2` | Rapport 2023, s. 91 |
| 2026 | Q004, linje r2 | «Hvor fornøyd/misfornøyd er du med:» **«Trygghet når det gjelder å ferdes ute på kveldstid i Oslo sentrum»** | «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd» | 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker | `Q004r2` | Metoderapport 2026, s. 20 |

- **2018:** Datafila følger nummereringen i nettskjemaet (Q007), ikke papirskjemaet (5).
- **2018, nettskjema** (Q007, Nettskjema 2018): Versjonen for dem som svarte på nett. Avvik fra papirskjemaet i innledning: «Hvor fornøyd/misfornøyd er du med ...» **«Trygghet når det gjelder å ferdes ute på kveldstid i Oslo sentrum»**.

### Koding i datafilene

| Utgave | Variabel | Gyldige koder | «Ikke sikker» | Ubesvart | Merknad |
|---|---|---|---|---|---|
| 2007 | `Q19_2` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2010 | `Q19_2` | 1–6 | 7 | tom | 2007 og 2010 ligger i én felles datafil. Svar uten gyldig verdi er tomme, så «Ikke sikker» kan ikke skilles fra ubesvart. |
| 2014 | `Q11_2` | 1–6 | 7 | tom | Ubesvart er tomt. En kode 0 uten etikett forekommer i færre enn 10 svar, og regnes som manglende. |
| 2018 | `Q007__2` | 1–6 | 7 | 8 | Kodene 7 (Ikke sikker) og 8 (na) er deklarert som brukerdefinerte manglende verdier i datafila. Programmer som ikke leser slike deklarasjoner, viser begge som tomme, og da forsvinner «Ikke sikker». |
| 2023 | `Q004#2` | 1–6 | 7 | 9996 og tom | Ubesvart er lagret med koden 9996 («na»); det gjelder 465 av 28 851 svar, og 24 svar er tomme. 898 svarte «Ikke sikker» (kode 7). |
| 2026 | `Q004r2` | 1–6 | 98 | tom | – |

### Overgangene

#### 2007 → 2010: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . ? / ....i Oslo sentrum» → «Hvor fornøyd eller misfornøyd er du med. . . / ....i Oslo sentrum»
- Instruksjon: «NÅ SKAL VI STILLE NOEN MER DETALJERTE SPØRSMÅL OM ULIKE TEMA. / For hvert av forholdene ber vi deg svare langs en skala fra 1 til 6, der 1 betyr at du er svært misfornøyd med dette forholdet, og 6 betyr at du er svært fornøyd.» → ingen
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; 7 = Ikke sikker → 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker
- Kode for «Ikke sikker» i skjemaet: 7 → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15–80 år → Innbyggere i Oslo, 15 år og eldre
- Leverandør: Synovate Norge (tidligere MMI) → TNS Gallup
- Svar per innsamlingsmodus: papir 92 %, nett 8 % → papir 69 %, nett 31 %
- Kilde til landbakgrunn: selvrapportert → ikke oppgitt

**Vurdering:** Ordlyden, batteriet og skalaen er de samme. Målgruppen ble utvidet fra 15–80 år til 15 år og eldre. Endringen gjelder alle spørsmål og vises derfor også her. Feltarbeidet var om høsten begge år.

Grunnlag: Spørreskjema 2007, s. 5; Spørreskjema 2010, s. 5; Rapport 2007, s. 3; Rapport 2010, s. 4. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2010 → 2014: Med forbehold

Endret i skjemaet:

- Innledning: «Hvor fornøyd eller misfornøyd er du med. . . / ....i Oslo sentrum» → «..i Oslo sentrum / Hvor fornøyd/misfornøyd er du med...»
- Instruksjon: ingen → «Merk: Sett ett kryss på hver linje»

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 15 år og eldre → Innbyggere i Oslo, 18 år og eldre
- Leverandør: TNS Gallup → Sentio Research Norge
- Svar per innsamlingsmodus: papir 69 %, nett 31 % → papir 85 %, nett 15 %
- Årstid for feltarbeidet: høst → vinter
- Kilde til landbakgrunn: ikke oppgitt → selvrapportert

**Vurdering:** Ordlyden og skalaen er de samme, og linjene om politiets innsats står fortsatt i batteriet. Linjene om Oslo sentrum og om området der man bor ble skilt i to spørsmål med de samme linjene. Målgruppen ble endret fra 15 år og eldre til 18 år og eldre, så populasjonen er ikke den samme. Feltarbeidet flyttet fra høst til vinter.

Grunnlag: Spørreskjema 2010, s. 5; Rapport 2010, s. 4; Rapport 2014, s. 3, 64. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2014 → 2018: Med forbehold

Endret i skjemaet:

- Innledning: «..i Oslo sentrum / Hvor fornøyd/misfornøyd er du med...» → «Hvor fornøyd/misfornøyd er du med:»
- Spørsmålstekst: «Trygghet når det gjelder å ferdes ute på kveldstid» → «Trygghet når det gjelder å ferdes ute på kveldstid i Oslo sentrum»

Endret i metoden:

- Leverandør: Sentio Research Norge → Kantar TNS
- Svar per innsamlingsmodus: papir 85 %, nett 15 % → papir 52 %, nett 48 %
- Årstid for feltarbeidet: vinter → vår
- Kilde til landbakgrunn: selvrapportert → register

**Vurdering:** «i Oslo sentrum» ble flyttet fra en underoverskrift inn i linjeteksten, og linjene om politiets innsats ble tatt ut av batteriet. Meningen er den samme, men sammenhengen i skjemaet er en annen, som for trygghet der man bor. Feltarbeidet flyttet fra vinter (januar–mars) til vår (mars–mai).

Grunnlag: Rapport 2014, s. 3, 64; Rapport 2018, s. 5, 115; Nettskjema 2018. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2018 → 2023: Med forbehold

Endret i skjemaet:

- Instruksjon: «Merk: Sett ett kryss på hver linje» → ingen

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre → Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget.
- Leverandør: Kantar TNS → Kantar Public
- Svar per innsamlingsmodus: papir 52 %, nett 48 % → nett 98 %, papir 2 %
- Vektet etter: kjønn, alder, bydel → kjønn, alder, bydel, landbakgrunn

**Vurdering:** Omleggingen i 2023, som for trivsel. Ordlyden, batteriet og skalaen er de samme, og feltarbeidet var om våren begge år. Rapporten for 2023 ber om varsomhet ved sammenligning over tid.

Grunnlag: Rapport 2023, s. 4, 7, 12, 18, 91. Vurdert av Byrådsavdeling for finans, Oslo kommune, 5. oktober 2026.

#### 2023 → 2026: Med forbehold

Endret i skjemaet:

- Instruksjon: ingen → «Svar på en skala fra 1-6 der 1 er svært misfornøyd og 6 er svært fornøyd»
- Svaralternativer: 1 = Svært misfornøyd; 2; 3; 4; 5; 6 = Svært fornøyd; Ikke sikker → 1 = 1 - Svært misfornøyd; 2; 3; 4; 5; 6 = 6 - Svært fornøyd; 98 = Ikke sikker
- Kode for «Ikke sikker» i skjemaet: ingen → 98

Endret i metoden:

- Målgruppe: Innbyggere i Oslo, 18 år og eldre. Innvandrere med under fem års botid var ikke med i utvalget. → Innbyggere i Oslo, 18 år og eldre. Avgrensningen fra 2023, der innvandrere med under fem års botid ikke var med, ble ikke videreført; metoderapporten omtaler det ikke, og opplysningen er fra oppdragsgiver.
- Leverandør: Kantar Public → Opinion
- Svar per innsamlingsmodus: nett 98 %, papir 2 % → nett 100 %

**Vurdering:** Samme spørsmål og skala, og i hovedsak samme metode: begge år i hovedsak nettundersøkelse med invitasjon på e-post, utvalg og vekting etter landbakgrunn, feltarbeid om våren. I 2026 var undersøkelsen bare på nett, og kontaktinformasjonen kom fra Kontakt- og reservasjonsregisteret. Populasjonen er likevel ikke den samme: i 2023 var innvandrere med under fem års botid ikke med i utvalget, i 2026 var de med. Endringen gjelder alle spørsmål og vises derfor her. Svarprosenten i 2026 er regnet på en annen måte, men det endrer ikke hvem som svarte.

Grunnlag: Rapport 2023, s. 4, 7, 12; Metoderapport 2026, s. 1–4, 7, 20; Opplysning fra FIN 2026. Vurdert av Byrådsavdeling for finans, Oslo kommune, 6. oktober 2026.

### Standardmerknad til tabeller

Denne teksten brukes som merknad når tall for spørsmålet publiseres i tabeller:

> Fra 2023 ble undersøkelsen lagt om: i hovedsak nettundersøkelse med invitasjon på e-post, og utvalget ble trukket og vektet etter landbakgrunn. Tall fra 2023 og senere bør sammenlignes med tidligere år med varsomhet. Mer om metode og sammenlignbarhet: https://github.com/oslokommune/ok-innbyggerundersokelsen
