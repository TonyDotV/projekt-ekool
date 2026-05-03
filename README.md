# Projekt eKool

Rühma liikmed : Tony Vorontsov

Projekti idee on luua digitaalne eKool. Koolide, õpetajate ja õpilaste nimed on välja mõeldud ning pole võetud päris elust kuid tehtud enam-vähem realistlikuks. eKooli veebilehel saab sisse logida adminina, õpetajana või õpilasena ja vastavalt sisselogitule on neil ka erinevad õigused.
Näiteks:

Admini õigused :
- õpetaja andmeid
- õpilaste andmeid
- saab moodustada õpilaste pingerea keskmise hinde alusel
- lubada kursustel õppida aineid

Õpetaja õigused :
- õpilaste andmed
- õpilaste hinded
- ained, mida õpetada
- saab valida, mis ainet soovib õpetada (võib olla mitu)

Õpilase õigused :
- ülevaade sooritatud ja mitte sooritatud ainetest
- ülevaade oma hinnete üle sh ka keskmine hinne
- ülevaade oma kursuse üle
- saab ainetele registreerida

Dokumentatsioon on tehtud Trellos
https://trello.com/b/tz0Mvv5e

git add "file.txt"<br>
git commit -m "second commit"<br>
git push -u origin main


# Muudatused

## 04.09.2026

+ Muutsin enamus koodi inglise keelseks, et mul oleks lihtsam koodist aru saada (olen harjunud koodi kirjutama inglise keeles)
+ lisasin õiguseid õpetaja rollile (hinnete lisamine ja nägemine)
+ parandasin õpetaja lisamise ja õpetajate nimekirja nägemise adminina
+ lisasin kommentaarid, mis seletavad lühidalt, mida koodi osad teevad

Töö kestvus : 3h (koolis)



## 04.14.2026

Commit 1
<br>
Lisasin hinnete süsteemi<br>
  ++ õpetajad saavad hindeid lisada ainete kaupa<br>
  ++ õpetajad saavad näha õpilaste hindeid ainete kaupa<br>
  ++ õppisin kasutama reeglit .2f (näitab murdarvul ainult 2 esimest komakohta)
  <br>
  -- eemaldasin "vanus" ja "sugu" lahtrid, arvasin, et need ei ole vajalikud

Commit 2
<br>
Veaparandused<br>
  ++ parandasin õpetaja kasutaja registreerimise<br>
  ++ vahetasin mõned koodi osad eesti keelseks, tekitas probleemi koodi kirjutamisel
<br>
Töö kestvus : 1h 30m (koolis)

Commit 3
<br>
Õpilase õiguste muutmine<br>
  ++ õpilased saavad nüüd enda hindeid ja üldist keskmist hinnet näha<br>
  ++ õpetajad saavad õpilaste keskmiseid hindeid vaadata<br>
  ++ enam ei pea eraldi õpilasi/õpetajaid lisama vaid registreerides lisatakse need automaatselt rollidesse<br>
  ++ admin saab nüüd eemaldada õpetajaid/õpilasi süsteemist
  <br>
  -- õpilased ei saa enam teiste õpilaste andmeid vaadata
  <br>
  Töö kestvus : 1h 30m (koolis)


## 04.29.2026

++ Õppisin TKinteri kohta, et anda programmile kasutajaliides<br>
++ Lisasin paari koodijupi juurde kommentaarid ja docstringid<br>


Töö kestvus : 3h = 2 paari (1h 30min x 2)


## 05.03.2026

++ Põhjendasin koodi osasid docstringide ja kommentaaridega<br>
++ Seletasin TKinteri koodi osad, sest see on uus minu jaoks ja meeldetuletuseks<br>
++ Õpetajad saavad lisada hindeid ainult 1-5 vahemikus nüüd<br>
++ Õpetajate registreerimisel saab Admin anda neile ained, mida õpetavad, mida näeb õpetajate loendis<br>
++ Õpilase registreerimisel küsitakse nüüd kursust<br>

Peale uuenduste piding väga palju probleeme lahendama, sest TKinter on minule uus ja mul on sellest raske aru saada niiet, juhtus palju vigu, mida oli raske parandada.<br>
Igaksjuhuks on alles jäetud terminali versioon, sest pole kindel, kas saan korralikult seletada TKinteri osa koodist. Lisasin võimalikult palju seletusi.


