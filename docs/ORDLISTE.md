# Ordliste

Ordene som brukes på sidene om metode og sammenlignbarhet.

| Ord | Betydning |
|---|---|
| **Batteri** | Flere spørsmål (linjer) med felles innledning og samme svarskala, for eksempel fire linjer om trygghet |
| **Bruttoutvalg** | Alle som ble trukket ut og invitert til å svare |
| **Nettoutvalg** | Alle som svarte |
| **Svarprosent** | Nettoutvalget i prosent av bruttoutvalget. Ofte er retur (ukjent adresse, flytting) trukket fra først. Hvordan den er regnet, varierer mellom utgavene; se [METODE.md](METODE.md) |
| **Stratifisert utvalg** | Utvalget er trukket hver for seg i grupper (strata), for eksempel i hver bydel |
| **Disproporsjonalt utvalg, overtrekk** | Noen grupper er trukket ut i større grad enn andelen deres i befolkningen, for å få nok svar fra dem. Vektingen retter opp skjevheten |
| **Vekting** | Svarene får ulik vekt, slik at de som svarte, ligner befolkningen på kjennetegn som kjønn, alder og bydel |
| **Cellevekter, rimvekting (raking)** | To måter å vekte på: etter hver kombinasjon av kjennetegn, eller ett kjennetegn om gangen til alle fordelingene stemmer |
| **Innsamlingsmodus** | Måten svarene er samlet inn på: papirskjema, nettskjema eller telefon |
| **Tverrsnitt** | Et nytt utvalg hver gang. Undersøkelsen er en **trend** (gjentatt tverrsnitt): de samme spørsmålene stilles til nye utvalg, ikke til de samme personene |
| **Målgruppe** | Hvem undersøkelsen gjelder, for eksempel innbyggere i Oslo som er 18 år og eldre |
| **Konsept** | Det et spørsmål måler. Konseptet har en fast id (for eksempel `trives_oslo`) som ikke endres selv om ordlyden eller variabelnavnet endres |
| **Innledning, linje** | Innledningen er teksten over et batteri («I hvilken grad:»). Linjen er selve spørsmålet i batteriet («Trives du i Oslo?») |
| **Variabel i datafila** | Navnet på kolonnen i leverandørens datafil, for eksempel `Q001r1`. Navnene skifter fra utgave til utgave |
| **«Ikke sikker»** | Svaralternativet ved siden av skalaen 1–6. Regnes som manglende svar |
| **Prosentpoeng** | Forskjellen mellom to prosenter. Fra 76 til 83 prosent er 7 prosentpoeng |
| **Ja, med forbehold, nei** | Dommene om sammenlignbarhet; se [SERIESPORSMAL.md](SERIESPORSMAL.md) |
| **DDI** | En internasjonal standard for å dokumentere data fra spørreundersøkelser. Kodene for utvalgsdesign og innsamlingsmodus i `data/` følger den |
