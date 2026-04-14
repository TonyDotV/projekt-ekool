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

git add "file.txt"
git commit -m "second commit"
git push -u origin main


# Muudatused

04.09.2026

+ Muutsin enamus koodi inglise keelseks, et mul oleks lihtsam koodist aru saada (olen harjunud koodi kirjutama inglise keeles)
+ lisasin õiguseid õpetaja rollile (hinnete lisamine ja nägemine)
+ parandasin õpetaja lisamise ja õpetajate nimekirja nägemise adminina
+ lisasin kommentaarid, mis seletavad lühidalt, mida koodi osad teevad

Töö kestvus : 3h = 2 paari (1h 30min x 2)



04.14.2026

Lisasin hinnete süsteem
  + õpetajad saavad hindeid lisada ainete kaupa
  + õpetajad saavad näha õpilaste hindeid ainete kaupa
  + õppisin kasutama reeglit .2f (näitab murdarvul ainult 2 esimest komakohta)

  - eemaldasin "vanus" ja "sugu" lahtrid, arvasin, et need ei ole vajalikud
