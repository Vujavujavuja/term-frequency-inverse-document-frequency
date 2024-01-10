# Pravila
Projekat se radi individualno ili u paru.

Rok za predaju projekata je petak 22.12.2023, 23:59. Produžetak roka nije moguć.

Ukoliko dva studenta rade u paru, potrebno je da formiraju tim gde će oba studenta biti prijavljena.

README fajl u toku projekta treba da počne sa segmentima "Studenti", "Urađeno" i "AI" pri čemu (videti i primer):

Sekcija "Studenti" sadrži ime, prezime, i broj indeksa u formatu ss bbb/gg (ss - oznaka smera, bbb - broj indeksa, gg - godina upisa)
Sekcija "Urađeno" treba da sadrži naznaku da li je urađen ceo projekat, ili neke tačke nedostaju, nešto nije po specifikaciji, itd.
Sekcija "AI" treba da sadrži detalje o eventualnoj upotrebi AI sistema u toku izrade projekta, tačne upite koji su poslati i slično.
Rešenje mora da bude u obliku python skripte (sa .py ekstenzijom), pri čemu ime fajla treba da bude run.py.

Deljenje koda u toku izrade sa drugim timovima nije dozvoljeno i repozitorijumi treba da ostanu privatni.

Raspored odbrana će biti objavljen posle isteka roka za predaju.

# Zadatak

tf-idf (term frequency–inverse document frequency) je mera (vrednost) koja daje procenu koliko je važna neka reč za jedan specifičan tekst iz šireg skupa tekstova. Koristi se, na primer, prilikom rangiranja rezultata pretrage dokumenata, tako što za svaku ključnu reč koja se traži odredimo tf-idf i dokumenta sortiamo po zbiru ovih vrednost (za sve ključne reče).

U ovo projektu ćemo implementirati tf-idf prateći Map-Reduce paradigmu.
Arhiva data.tar.gz sadrži skup tekstova koji ćemo koristiti kao primer podataka nad kojima radimo (tekstovi su preuzeti sa [Kaggle takmičenja u detektovanju lažnih vesti](https://www.kaggle.com/datasets/rajatkumar30/fake-news/))


**Napomena:** Rešenje treba da bude implementirano tako da:
- Nigde ne koristi eksplicitno navedenu petlju ili `list` i `dict` comprehension
- Ne koristi funkcionu `len` za određivanje dužine neke kolekcije (ukoliko je potrebno, `len` implementirati kroz `reduce`).
- Dozvoljeno je sortiranje niza upotrebom ugrađene funkcije `sorted`.
- Dozvoljeno je forsirati realizaciju iteratora u list pozivom funkcije `list` (ukoliko je potrebno, a ako bude potrebo verovatno će biti posle poziva `map`).
- Dozvoljena (i preporučena) je upotreba lambda funkcija.

### 1. Računanje tf vrednosti iz jednog teksta (7 poena)
Napisati funkciju koja kao jedini parametar prima putanju do fajla u kojem se nalazi tekst, a vraća listu torki (identifikator fajlaº, reč, frekvencija pojavljivanja date reči).

ºidentifikator fajla može biti putanja do fajla

Pre računanja frekvencije pojavljivanja potrebno je uraditi sledeće stvari (implementirati kao seriju map ili reduce poziva adekvatnih funkcija).
- Zameniti sve apostrofe (`’`) razmakom.
- Ukloniti specijalne karaktere (barem sledeći skup: `, . ! ? \n " ' “ ( ) # $ @`) iz teksta.
- Zameniti sva velika slova malim.
- Podeliti tekst u niz reči (nije dozvoljena upotreba ugrđene funkcije split). Pri tome, ignorisati uzastopno ponovljene razmake.
- Odbaciti reči koje su kraće od tri karaktera.


Frekvencija pojavljivanja reči se računa prema formuli: $\text{tf}(t, d) = \frac{\text{Broj pojavljivanja reči t} \text{ u dokumentu d}}{\text{Ukupan broj reči u dokumentu d}}$.


### 2. Računanje tf vrednosti iz svih tekstova (5 poena)

Primeniti funkciju iz tačke 1 na sve tekstove iz arhive. Upotrebiti `map` i/ili `reduce`, tako da rezultat bude jedna lista sa svim torkama iz svih fajlova (ne lista listi!). Lista fajlova se može dohvatiti upotrebom modula `glob`.


### 3. Računanje idf vrednosti (4 poena)

Upotrebom `map` i/ili `reduce` (i odgovarajućih funkcija) izračunati idf vrednosti za svaku reč koja se pojavljuje u listi dobijenoj u tački 2.
Možete koristi listu iz tačke 2 i listu svih fajlova iz tačke 1.

idf se računa po formuli: $\text{idf}(t) = \log \left( \frac{\text{Broj dokumenata u skupu}}{\text{Broj dokumenata u kojima se reč t pojavljije }} \right)$

### 4. Računanje tf-idf vrednosti (4 poena)
Koristeći liste iz tačaka 2 i 3, te upotrebom `map` i/ili `reduce` (i odgovarajućih funkcija) izračunati tf-idf vrednosti. Rezultat treba da bude u obliku liste torki (reč, identifikator fajla, vrednost).
Sortirati listu tako da se sve reči vezane za jedan fajl pojavljuju konsekutivno, a unutar jednog fajla po opadajućim vrednostima tf-idf.

**Nije dozvoljeno pretovirti jednu od dve ulazne liste u heš mapu (dict)**.   

*Sugestija: Prvi korak bi mogao da bude konkatenacija listi iz tačaka 2 i 3.
Prihvatljivo je da `map` i/ili `reduce` vrati torku, u kojoj je jedan element tražena lista, a ostatak neki međurezutlat koji se odbacuje.*
