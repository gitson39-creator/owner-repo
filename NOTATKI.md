# Notatki o preferencjach użytkownika

## Styl współpracy
- Odpowiadać po polsku, profesjonalnie, bez błędów, w stylu Jarvisa.
- Nie zadawać pytań: decyzje podejmować samodzielnie („wybierz sam”, „nie odpowiadam na pytania”).
- Robić dokładnie to, o co proszono, nie więcej. Na przykład „podłącz ElevenLabs i daj pomysły” nie oznacza przerabiania filmu.
- Zapamiętywać wszystko, co mówi użytkownik.
- 26.11.2026: „jak skończysz, to rób następne po kolei i zrób tak jeszcze z 3”. Po filmie 63 robię kolejno 64, 65 i 66 z listy 7. Użytkownika nie ma, więc historie wybieram sam.
  - Każdy film ma mieć mocny hak na początku i historię, której widz chce słuchać do końca, bo jest ciekawy (jak w filmie 63).
- 26.11.2026: „jeśli możesz oszczędzić limit, ale robić to dłużej, to tak zrób, bo się nie spieszę”. Oszczędzam limit: mniej sprawdzania, długie przerwy między kontrolami, brak zbędnych testów.
  - Po wyczerpaniu limitu kontynuować automatycznie po resecie (zaplanowane zadanie wznawia pracę). Użytkownik nie odpowiada na pytania.
- 27.11.2026: „nie spiesz się, lepiej dopracuj i rób dłużej, nic krócej i byle jak”. Jakość ma pierwszeństwo przed czasem:
  - przed pełnym renderem dokładny przegląd klatek (początek, środek i koniec każdego ujęcia, a nie tylko środek);
  - poprawianie kadrów, detali i animacji aż będzie dobrze;
  - przegląd gotowych klatek przed złożeniem filmu.
- 27.11.2026: „popraw film z pingwinem i rób 2 nowe, nie odpowiadam na pytania”.
  - Film 64: przebudować scenografię na pełną (zasada pełnej scenografii) i wyrenderować ponownie.
  - Nowe filmy: kolejne z listy 7, czyli 67 (ketchup jako lekarstwo) i 68 (homary jako jedzenie więźniów), od razu z pełną scenografią.

## Filmy (styl ricksclips)
- Pionowo, 1080x1920, 30 fps.
- Długość 60 s lub więcej, najlepiej około 61 s.
- Lektor ma brzmieć jak na kanale RicksClips (YouTube @ricksclips3000). Jeśli nie da się identycznie, wybrać najbliższy głos ElevenLabs.
  Obecnie: Liam, tempo 1.12. Wybrany bez próbki z kanału, bo YouTube jest zablokowany w sieci środowiska. Klucz API nie trafia do repozytorium.
- Montaż jak u RicksClips: dużo się dzieje, cięcie co 1–2 s, zmiany kątów kamery, szybkie obroty z rozmyciem, najazdy na słowa kluczowe, wstrząsy.
- Szybka mowa i krótkie pauzy.
- Bez glitchy: sprawdzać migotanie podłogi (konflikt głębi bruk/trawa, naprawione).
- Napisy wypalone w obrazie, słowo po słowie, aktualne słowo podświetlone na żółto.
- Oryginalna historia ze zwrotem akcji na końcu. Bez prawdziwych osób i marek.
- Głośność −14 LUFS, szczyt poniżej −1 dBFS. Muzyka 6 dB pod głosem.
- KOLORY (24.11.2026, po filmie nr 43): więcej kolorów, bo cały film o zebrach był ponury. Unikać szaro-granatowej palety, mgły i półmroku przez cały film. Na przyszłość:
  - słoneczne, nasycone HDRI (błękitne niebo, turkusowa woda);
  - kolorowe rekwizyty, stroje i tła (czerwień, żółć, zieleń, pomarańcz);
  - jaśniejsza ekspozycja i cieplejsze, żywsze światło;
  - nawet sceny nocne lub podwodne z kolorowymi akcentami (neony, lampy, światła).
- PEŁNA SCENOGRAFIA (27.11.2026): „masz robić całą scenerię do filmu, a nie że jest w filmie zoo i jest to pusta scena w Blenderze ze zwierzętami”. Każde miejsce ma wyglądać jak prawdziwe, kompletne miejsce, a nie jak pusty plan z kilkoma obiektami. Na przyszłość (i przy poprawkach):
  - Zoo:
    - wybiegi z ogrodzeniem, skałami, wodą i roślinnością;
    - alejki, ławki, kosze, latarnie, drogowskazy, mapy, kioski, budki z lodami, toalety, wejście z kasami;
    - zwiedzający, pracownicy, inne zwierzęta na sąsiednich wybiegach.
  - Ulica:
    - chodniki, krawężniki, pasy, latarnie, znaki, drzewa, samochody, witryny sklepów, przechodnie;
    - okna z detalem, dachy, balkony.
  - Wnętrze: meble, dekoracje, lampy, obrazy, rośliny, drobne przedmioty.
  - Tło nigdy nie jest pustą trawą ani gołym horyzontem: dalsze budynki, drzewa, wzgórza, miasto w oddali.
  - Każde ujęcie ma mieć zapełniony pierwszy, średni i dalszy plan.
  - Przed renderem sprawdzić klatki testowe pod kątem pustych miejsc.

## Zrobione filmy
1. `gus_the_rooster.mp4`: kogut skazany na więzienie (61 s, lektor Piper, napisy).
2. `brimwick_hats.mp4`: miasteczko, w którym wszyscy noszą ten sam kapelusz (61 s, ElevenLabs Liam ×1.12, 60 ujęć kamery, napisy). Pomysł nr 5 z listy. Wersja 2: szybki montaż, naprawione migotanie podłogi.

3. `whistle_town.mp4`: miasteczko, które zakazało gwizdania (61 s, Liam ×1.12, 54 ujęcia kamery, napisy). Pomysł nr 11.
4. `dog_license_v2.mp4`: Why This Dog Never Got a Ticket (43,3 s).
5. `zebra_ships.mp4`: Why Warships Were Painted Like Zebras (61,3 s, Liam v3 bez modulacji). Pomysł 43.
6. `stop_signs.mp4`: Why Stop Signs Used to Be Yellow (24,4 s, krótszy przez limit ElevenLabs). Pomysł 57.
7. `cow_eyes.mp4`: The Cows With Eyes on Their Butts (61,9 s, Liam v3). Pomysł 63.
8. `penguin_general.mp4`: The Penguin Who Became a General (64,2 s, Liam v3, 41 ujęć). Pomysł 64. Wersja v2 z pełną scenografią z 27.11.2026.
9. `fake_bus_stop.mp4`: The Fake Bus Stop for People Who Wander (62,3 s, Liam v3, 36 ujęć). Pomysł 65.
10. `elevator_mirrors.mp4`: Why Elevators Have Mirrors (61,1 s, Liam v3, 28 ujęć). Pomysł 66.
11. `ketchup_medicine.mp4`: When Ketchup Was Medicine (64,2 s, Liam v3, 31 ujęć, pełna scenografia). Pomysł 67.
12. `lobster_prison.mp4`: Why Lobster Was Prison Food (61,9 s, Liam v3, 30 ujęć, pełna scenografia). Pomysł 68.

## Lista pomysłów (z 17.11.2026)
1. Koza wybrana na burmistrza
2. Latarnik, który nigdy nie widział statku
3. Wioska, która zakazała wtorków
4. Pies listonosz przez 12 lat
5. Miasteczko jednakowych kapeluszy (zrobione)
6. Krowa, która trzy razy uciekła z „więzienia”
7. Most, przez który nie wolno było przejść
8. Piekarnia otwarta tylko o północy
9. Strach na wróble z medalem
10. Zegar, który przez rok chodził do tyłu

## Lista pomysłów 2 (z 17.11.2026)
11. Miasteczko, w którym zakazano gwizdania (zrobione)
12. Listonosz, który doręczał listy tylko na rowerze bez siodełka
13. Wioska, w której wszyscy noszą pidżamy na co dzień
14. Najdłuższa kolejka po chleb w historii
15. Kot, który był burmistrzem przez 15 lat
16. Most z dzwonkiem do przejścia
17. Wieś, w której nikt nie zamykał drzwi
18. Kościelny dzwon, który dzwonił 13 razy
19. Konkurs na największą dynię, który wygrał koń
20. Miasteczko, które zakazało parasoli

## Rolki mapowe GTA 6 (od 18.11.2026)
- Format jak rolka FB „Where to go first · GTA 6 · after launch · #1”: mapa Leonidy, nagłówek WHERE TO GO FIRST, żółta plakietka, czarne etykiety, różowe okręgi, pinezki, przyciemnienie, rozmycie przy najazdach, na końcu FOLLOW FOR THE NEXT ONE. Bez klipów z trailera.
- Narzędzie: Remotion (projekt w scratchpad/map/rm). Mapa rysowana w SVG. Lektor Liam ×1.12. 61 s.
- Użytkownik nie chce wykładów o prawach autorskich do takich rolek.
- Zrobione: #1 Starfish Island (`gta6_where_to_go_first_1.mp4`), wersja 2 po uwagach.
- Uwagi użytkownika (v1 była zła): „to nawet nie jest Vice City”, „mapa wygląda źle”. Zawsze najpierw research, a jakość ponad tempo.
- Mapa v2 zbudowana z prawdziwych danych: OSM Miami (BBBike) jako Vice City, Natural Earth z południowej Florydy jako Leonida, lupa na Vice City, fraktalne wybrzeże.
  Nazwy z gry: Starfish (Star Island), Rialto Islands (Venetian), Dalton (Fisher), Gloriana Key (Virginia Key), Catalan Key (Key Biscayne), Catalan Bay (Biscayne Bay), Vice Beach / Ocean Beach, Port VC, Little Cuba, Stockyard, Lake Leonida (Okeechobee).
- Generatory map: scratchpad/geo (build_world.py, build_vc.py, style_all.py). Rastry: overview, mid, close.

## Nazwa kanału TikTok (propozycje z 18.11.2026)
Rekomendacja: **Leonida Intel**? Nie: zajęte przez stronę leonida-intel.com. Wybrana rekomendacja: **ViceMapped** (@vicemapped).
Alternatywy: Leonida Daily, Vice Atlas, Where To Go First, Map of Vice, Leonida Uncovered, VC Insider, Neon Leonida, Six Minutes in Vice, The Leonida Guide.

## Kanał TikTok: wybrany (18.11.2026)
- Nazwa wybrana przez użytkownika: **vicemaped** (tak napisał, przez jedno „p”).
- Bio (limit TikToka 80 znaków):
  🗺️ GTA 6 maps & secrets
  📍 Best spots in Leonida
  🔔 New video daily

## Rolka GTA 6 #1 – wersja 3 (18.11.2026)
- Uwaga użytkownika: początek (Leonida, regiony) był tragiczny. Od razu zaczynać od Vice City. Bez długich przerw między słowami, cały czas coś ma się dziać.
- Zrobione: start w Vice City, pauzy między zdaniami 0,24 s, pauzy wewnątrz zdań skrócone do 0,1 s. Długość 37 s (wcześniejsza preferencja 60 s+ ustąpiła prośbie o brak przerw).

## Rolka GTA 6 #2 (18.11.2026)
- Prośba: 1–2 ciekawe miejsca, 30–40 s, bez przerw. Zrobione: Ocean Beach (+ Ocean View Hotel z 2002, neon nocą) i Port VC (wycieczkowce, kontenery). 34,4 s.
- Plik: `gta6_where_to_go_first_2.mp4`, projekt w scratchpad/map2.
- Preferencja (18.11.2026): w kolejnych rolkach najlepiej JEDNO miejsce na odcinek. Nie zadawać pytań.

## Opisy TikTok (18.11.2026)
#1: Starfish Island = Tommy Vercetti's old island 🏝️ Where are you going first in GTA 6? 👇 #gta6 #gtavi #vicecity #leonida #gta #rockstargames #gaming #gtavicecity
#2: Ocean Beach by day, neon by night 🌴 Then the port across the water 🚢 Where are you going first? 👇 #gta6 #gtavi #vicecity #leonida #gta #rockstargames #gaming #oceanbeach

## Nowy pomysł na film z historyjką (23.11.2026)
21. „The town where the mayor was a parrot”: papuga po zmarłym burmistrzu powtarza jego zdania, rada słucha jej przez 9 lat. Zwrot: miasto ma najlepszy budżet w historii, bo papuga umiała powiedzieć tylko „No.”
Lista pomysłów 3 (23.11.2026): 22 Pies, który dostał prawo jazdy; 23 Wioska, gdzie zegarmistrz przestawiał czas; 24 Kot, który ukradł 600 skarpetek; 25 Szkoła z jednym uczniem; 26 Miasto zakazujące śmiechu w niedzielę; 27 Latarnia na suchym lądzie; 28 Rybak, który złapał tę samą rybę 40 razy; 29 Most budowany 100 lat; 30 Wioska, gdzie wszyscy mają na imię Bob; 31 Kura, która zniosła jajo na kościelnej wieży.

## Film nr 22 (23.11.2026)
- `dog_license.mp4`: pies Biscuit z prawem jazdy (40 s, Liam ×1.12, 35 ujęć, napisy, karty HUD). Zwrot: auto bez silnika, w środku gniazdo ptaków, nigdy nie wyjechało z podjazdu.
- Projekt: scratchpad/proj4 (nowe: drawDog, kabriolet z otwieraną maską, warstwa HUD nad obrazem).
- ElevenLabs: zostało ok. 2900 znaków do resetu limitu.

## Wzór stylu: RicksClips „Why Astronauts Can't Flush in Space” (23.11.2026)
Analiza z 9 publicznych klatek (pełne wideo zablokowane przez weryfikację YouTube):
- Postacie: płaskie 2D „bean” w świecie 3D, BIAŁE okrągłe twarze bez koloru skóry, cienkie czarne kreski zamiast rąk i nóg, kolorowe kapsułowe tułowia (fiolet, żółty, czerwony) z kołnierzykami i naszywkami, rysowane włosy i czapki, oczy jako kółka z kropką, małe usta, miny „smug”.
- Otoczenie: realistyczne, szczegółowe 3D (PBR, połysk, odbicia), nie toon-shading. Dużo rekwizytów, ekrany, panele, emisyjne światła.
- Światło: ciemne, filmowe, wysoki kontrast, kontrowe i boczne światła, bloom, gwiazdki odblasków, cząsteczki/kurz, winieta, chłodna niebieska tonacja z ciepłymi akcentami (pomarańcz).
- Kamera: ekstremalne zbliżenia przycinające pół twarzy, żabia i ptasia perspektywa, ujęcia przez obiekty na pierwszym planie, silna głębia ostrości, szerokie ujęcia ustanawiające; częste cięcia.
- Napisy: biały, gruby zaokrąglony bezszeryfowy font z czarnym obrysem, małe litery jak w mowie, 1–2 słowa, mały rozmiar, około 63% wysokości kadru, bez żółtego podświetlenia.
- Do zrobienia po otrzymaniu pliku wideo: głos, tempo, pauzy, rytm cięć, przejścia, ruch kamery, animacje.

## Remake filmu nr 22 w stylu RicksClips (23.11.2026)
- Prośba: przeanalizować film RicksClips (YouTube Shorts NpRAk-5VKlo, plik przesłany przez użytkownika) i zrobić film nr 22 jeszcze raz, tak żeby wyglądał jak wzór. Czas nie gra roli, jakość jest najważniejsza.
- Pełna analiza: `ANALIZA_RICKSCLIPS.md`.
- Nowe zasady stylu (zastępują starsze z sekcji „Filmy”):
  - Napisy: białe Nunito Black z czarnym obrysem, 1–2 słowa, pisownia jak w mowie, około 70% wysokości kadru, bez żółtego podświetlenia.
  - Muzyka gra bez przerwy, miękka, ~100 BPM, bez stopy, około 9 dB pod głosem.
  - Kamera zawsze w ruchu, nowa kompozycja co 1,5–3 s, twarde cięcia, przeloty, bez rozmyć przy cięciach.
  - Świat realistyczny (PBR, HDRI, bloom, głębia ostrości), postacie płaskie 2D z białymi okrągłymi głowami.
- Głos: ElevenLabs „Harry” (premade), tempo 1.12, najbliższy wysokością głosu (~180 Hz, wzór ~198 Hz). Darmowy plan ElevenLabs nie pozwala używać głosów z biblioteki przez API, dostępne są tylko premade.
- Projekt: scratchpad/proj5 (render realistyczny, three.js r160 + tekstury Poly Haven CC0).
- Zrobione: `dog_license_v2.mp4` (43,3 s, 1080×1920, 30 kl./s, 37 ujęć, lektor Harry ×1.12, −13,9 LUFS, szczyt −1,4 dBFS). Wersja w repo ma 14 Mb/s (77 MB) z powodu limitu GitHuba 100 MB. Wersja „master” crf 17 (231 MB) leży w scratchpad/proj5/out.
- Tytuł i opis `dog_license_v2.mp4` według zasady RicksClips (opis = tytuł, bez hasztagów): **Why This Dog Never Got a Ticket**

## Głos w stylu RicksClips: Liam „z dopaminą” (24.11.2026)
- Prośba: głos bardziej jak RicksClips, może być Liam, ale ekspresyjny, ze zmianami tonu.
- Pomiary (Praat). Wzór: 198 Hz, zakres 17,3 półtonu, ruch 55 półtonu/s, ~200 słów/min. Zwykły Liam (v2): 123 Hz, zakres 14 półtonu, ruch 41–46.
- PRZEPIS (od teraz standard):
  1. ElevenLabs model `eleven_v3`, Liam (TX3LPaxmHKxFdv7VOQHJ), stability 0.0 (Creative), similarity 0.8. W tekście tagi emocji: [excited], [curious], [whispers], [laughs] itd. przed frazami.
  2. Obróbka `narzedzia/glos/post.py <wej> <wyj>`: TYLKO skrócenie pauz do 0,2 s i delikatny kompresor 2:1.
  3. ZAKAZ zmiany tonu i tempa (rubberband, asetrate itp.). Użytkownik 24.11.2026: „brzmi jakby miał modulator, ma być normalny”. Głos ma brzmieć naturalnie, ekspresja wyłącznie z modelu v3 i tagów.
  4. Wynik: 142 Hz (naturalny Liam), zakres 24,8 półtonu, ruch 58 półtonu/s (wzór 55), ~181 słów/min. Próbka: `glos_liam_ricksclips_probka.mp3`.
- POTWIERDZONE (24.11.2026): użytkownik ocenił głos z filmu nr 43 jako dobry, więc zostaje bez zmian. Liam, `eleven_v3`, stability 0.0, tagi emocji, pauzy 0,24 s, bez zmiany tonu i tempa.
- Limit ElevenLabs: zostało 1529 znaków do 17.12.2026 (to wystarczy na jeden film 60 s, ok. 1100 znaków z tagami).

## Lista pomysłów 4: formuła RicksClips (24.11.2026)
Prawdziwy mechanizm, bohater bez nazwiska („the new guy”), tytuł według schematu kanału.
32. Why Pilots Never Eat the Same Meal
33. The Fake Town That Became Real (Agloe, rekomendowany)
34. Why Soldiers Stop Marching on Bridges
35. Why Planes Dim the Lights Before Landing
36. Why the Black Box Is Orange
37. Why Surgeons Stopped Wearing White
38. How Sailors Knew Which Lighthouse They Saw
39. Why Pilots Say Mayday Three Times
40. The Money That Explodes When Stolen
41. Why Casinos Have No Clocks

## Lista pomysłów 5: na bazie największych hitów RicksClips (24.11.2026)
Ocena użytkownika: lista 4 była za słaba („lepsze pomysły daj, co to ma być”). Nowa zasada: pomysł musi mieć fortel, oszustwo, lukę w prawie, sprytny wynalazek albo zwrot, a nie samą ciekawostkę „why X”. Ma być wizualnie efektowny w 3D. Każdy wzorowany na kategorii hitu RicksClips:
42. The Army Made of Balloons: dmuchane czołgi „armii duchów” z II wojny (wzór: How One Cart Stopped an Entire Army, 9,8 mln). REKOMENDACJA.
43. Why Warships Were Painted Like Zebras: kamuflaż dazzle (wzór: This Shape Saved Roller Coasters, 13 mln).
44. The Students Who Beat the Lottery Legally: luka „roll-down” w loterii Cash WinFall (wzór: Why Cashiers Keep Winning The Lottery, 10 mln; The Window That Breaks Japan's Gambling Law, 16 mln).
45. How Persians Made Ice in the Desert: yakhchal (wzór: The Ancient Jar That Warned an Empire, 35 mln).
46. Pirates Had Better Insurance Than You: kodeks piracki, wypłaty za utracone kończyny (wzór: Levels of Pirate Cannonballs, 10 mln).
47. The Fake Town That Became Real: Agloe (wzór: The Town Built Around a Button).
48. The Lighthouse That Poisoned Its Keeper: soczewka na kąpieli rtęciowej (wzór: What the Grave Bell Really Meant, 14 mln).
49. How They Saved the Tower That Wanted to Fall: Piza, wybieranie gruntu spod wyższej strony (wzór: Why Perfect Railroads Don't Work, 31 mln).
50. Why the Mona Lisa Is Famous: kradzież w 1911 (wzór: The Prisoner Who Tunneled Into a Bank).
51. The Prison Where You're Always Watched: panoptykon (wzór: The Pink Prison Cell Experiment, 11 mln).

## Lista pomysłów 6: formuła RicksClips + dużo kolorów (24.11.2026)
Zasady: zwrot, fortel albo przypadek (jak w liście 5) i z natury kolorowy świat (uwaga po filmie nr 43). Bez nazwisk i marek.
52. The Rubber Ducks That Mapped the Ocean: w 1992 kontener z 28 800 gumowymi zabawkami (kaczki, żaby, bobry, żółwie) wpadł do Pacyfiku. Oceanografowie śledzili je latami i poznali prądy morskie. REKOMENDACJA.
53. The First Pilots Were a Sheep, a Duck and a Rooster: Wersal 1783, kolorowy balon. Król chciał wysłać przestępców, poleciały zwierzęta i przeżyły.
54. The Town That Refused to Stop Being Blue: hiszpańska wioska pomalowana na niebiesko dla filmu. Mieszkańcy zagłosowali, żeby została niebieska, i przyjechały tłumy turystów.
55. The Purple That Cost More Than Gold: purpura z tysięcy ślimaków tylko dla władców. 18-letni student, próbując zrobić lek, przypadkiem wynalazł tani fiolet.
56. The Paint Made From Real Mummies: farba „mummy brown” z mielonych mumii. Malarz po odkryciu zakopał swoją tubkę.
57. Why Stop Signs Used to Be Yellow: czerwień płowiała na słońcu, więc przez 30 lat znaki były żółte.
58. The Dress That Was Literally Toxic: modna szmaragdowa zieleń z arszenikiem w sukniach i tapetach.
59. Why Pencils Are Yellow: żółty miał sugerować najlepszy grafit z Chin, a konkurencja zaczęła kopiować kolor.
60. Why Flamingos Aren't Born Pink: pisklęta są szare, różowe stają się od jedzenia. Zoo musi dodawać barwnik do karmy.
61. Why Fire Trucks Turned Lime Green: badania wykazały, że czerwonego wozu nocą prawie nie widać, a limonkowe miały mniej wypadków.

## Lista pomysłów 7: formuła RicksClips + dużo kolorów (26.11.2026)
Te same zasady co lista 6: zwrot, fortel albo przypadek, kolorowy świat, bez nazwisk i marek.
62. Why Fire Hydrants Have Five-Sided Bolts: w upały ludzie odkręcali hydranty, więc dodano pięciokątne śruby. Pasuje do nich tylko klucz strażaków.
63. The Cows With Eyes on Their Butts: w Botswanie malowano oczy na zadach krów i lwy rzadziej atakowały, bo myślały, że zostały zauważone. REKOMENDACJA.
64. The Penguin Who Became a General: pingwin w zoo w Edynburgu jest maskotką gwardii królewskiej. Dostał tytuł szlachecki i kolejne awanse, aż do generała.
65. The Fake Bus Stop for People Who Wander: niemiecki dom opieki postawił fałszywy przystanek. Zagubieni pensjonariusze czekają na autobus, który nigdy nie przyjedzie, i bezpiecznie wracają.
66. Why Elevators Have Mirrors: ludzie skarżyli się, że winda jedzie za wolno. Zamiast szybszej windy zamontowano lustra i skargi ustały.
67. When Ketchup Was Medicine: w latach 30. XIX wieku sprzedawano „pigułki pomidorowe” na wszystkie choroby.
68. Why Lobster Was Prison Food: w czasach kolonialnych homarów było tak dużo, że dostawali je więźniowie. Dziś to luksus.
69. The Bubble Wrap That Was Wallpaper: folia bąbelkowa miała być tapetą 3D. Nikt jej nie chciał, dopóki nie zaczęto w nią pakować.
70. The Toy Clay That Was Wall Cleaner: masa do czyszczenia tapet od sadzy straciła rynek, a nauczycielka zrobiła z niej zabawkę dla dzieci.
71. The Spring That Fell Off a Ship Desk: inżynier pracujący nad sprężynami do okrętowych przyrządów strącił jedną z półki. Sprężyna „zeszła” po schodach i powstała zabawka.

## Film nr 43: „Why Warships Were Painted Like Zebras” (24.11.2026)
- Wybór użytkownika: pomysł 43 z listy 5 (kamuflaż dazzle).
- Fakty sprawdzone w Wikipedii (Dazzle camouflage):
  - przyjęty w 1917 roku;
  - cel: nie ukryć statek, tylko utrudnić ocenę odległości, prędkości i kursu;
  - każdy statek miał unikalny wzór;
  - pomalowano ponad 4000 brytyjskich statków handlowych i około 400 okrętów.
- Lektor: Liam, `eleven_v3`, stability 0.0, z tagami emocji. Jedno nagranie zużyło 1087 znaków; zostało około 440 do 17.12.2026.
  - Pauzy skrócone do 0,24 s (po „He fires...” 0,55 s); bez zmiany tonu i tempa.
  - Kontrola: transkrypcja faster-whisper zgadza się słowo w słowo; czasy słów mają medianę odchyłki 0,04 s.
- Długość: 61,3 s, 40 ujęć.
- Sceny: morze, nabrzeże z malarzami, U-boot (wnętrze i z zewnątrz), widok przez peryskop, torpeda pod wodą, diagram z lotu ptaka, konwój, zachód słońca.
- Projekt: scratchpad/proj6:
  - ocean: siatka fal Gerstnera wokół kamery plus daleka płaszczyzna;
  - kadłub proceduralny z teksturą dazzle (`fx6.js`, `shipdim.js`).
- Tytuł i opis (zasada RicksClips: opis = tytuł, bez hasztagów): **Why Warships Were Painted Like Zebras**
- Zrobione 24.11.2026: `zebra_ships.mp4`.
  - 1080×1920, 30 kl./s, 1838 klatek, render 65 min.
  - −14,3 LUFS, brak zamrożeń i czarnych klatek.
  - Repo: 12 Mb/s, 94 MB (limit GitHuba). Master crf 17 (413 MB) w scratchpad/proj6/out.
- Ocena użytkownika: głos dobry, film zostaje bez poprawek. Uwaga na przyszłość: za mało kolorów, całość ponura.

## Film nr 57: „Why Stop Signs Used to Be Yellow” (24.11.2026)
- Wybór użytkownika: pomysł 57 z listy 6.
- Fakty sprawdzone w Wikipedii (Stop sign):
  - pierwsze znaki STOP: Detroit, 1915;
  - w latach 1924–1954 znaki były żółte z czerwonym lub czarnym napisem, bo nie istniały czerwone materiały odporne na blaknięcie;
  - od 1954 roku: czerwone pole z białym napisem.
- ElevenLabs: przed nagraniem zostały tylko 442 znaki (limit odnawia się 17.12.2026), więc film jest krótszy: tekst ma 399 znaków, głos trwa 23,5 s. Po nagraniu zostało około 40 znaków.
  - Głos: Liam, `eleven_v3`, ten sam przepis co w filmie nr 43. Transkrypcja zgadza się słowo w słowo.
- Kolory (zgodnie z nową zasadą):
  - słoneczne niebo i kolorowe domy (róż, mięta, błękit, brzoskwinia, lawenda);
  - jesienne drzewa w ujęciach poklatkowych;
  - wnętrza w ciepłej brzoskwini;
  - kolorowe postacie: komisja w czerwieni, zieleni i błękicie, malarz w kolorowych kleksach.
- Projekt: scratchpad/proj7 (świat z proj5 plus skrzyżowanie, znaki STOP z teksturą canvas, sygnalizator, puszki farby, laboratorium, ujęcia poklatkowe ze słońcem).
- Zrobione 24.11.2026: `stop_signs.mp4`.
  - 24,4 s, 1080×1920, 30 kl./s, 732 klatki, 19 ujęć.
  - −14,1 LUFS, brak zamrożeń i czarnych klatek.
  - Repo: 24 Mb/s, 74 MB. Master crf 17 (120 MB) w scratchpad/proj7/out.
- Tytuł i opis: **Why Stop Signs Used to Be Yellow**

## Film nr 63: „The Cows With Eyes on Their Butts” (26.11.2026)
- Wybór użytkownika: pomysł 63 z listy 7.
- 26.11.2026 użytkownik podał nowy klucz ElevenLabs (darmowe konto, 10 000 znaków).
  - Klucz jest tylko w scratchpad/.el_key i nigdy nie trafia do repozytorium. Stary klucz zapisałem w .el_key_old.
  - Polecenie: „użyj tego samego głosu co w poprzednim filmie” → Liam, `eleven_v3`, ten sam przepis.
- Fakty z oryginalnego badania (Communications Biology 3, 430, 2020):
  - 14 stad w północnej Botswanie, na skraju delty Okawango, lata 2015–2018;
  - 2061 krów: zginęło 0 z 683 z oczami, 4 z 543 z krzyżykami i 15 z 835 bez znaków;
  - napastnicy to głównie lwy (i 1 lampart).
- Głos: 1009 znaków, 61,0 s po skróceniu pauz, transkrypcja zgodna słowo w słowo.
- Projekt: scratchpad/proj8:
  - sawanna z 17 tys. kęp trawy;
  - akacje, okrągłe chaty z malowanymi pasami, zagroda z pali, obóz naukowców z dżipem;
  - postacie: krowa z boku i od tyłu (oczy, krzyżyk, szkic), lew z boku i z przodu.
- Nauczka techniczna: tło HDRI przeliczane przez three.js na sześcian daje w swiftshaderze prostokątne plamy na niebie. Trzeba używać własnej sfery nieba (SKY mesh).
- Zrobione 26.11.2026: `cow_eyes.mp4`.
  - 1080×1920, 30 kl./s, 1858 klatek, 34 ujęcia; render około 2,5 h (4,8 s na klatkę, przerwany limitem czasu i wznowiony z RESUME=1).
  - −14,5 LUFS, brak zamrożeń i czarnych klatek.
  - Repo: 12 Mb/s, 95 MB. Master crf 17 (384 MB) w scratchpad/proj8/out.
- Tytuł i opis: **The Cows With Eyes on Their Butts**

## Film nr 64: „The Penguin Who Became a General” (26.11.2026)
- Wybrany samodzielnie: kolejny z listy 7, zgodnie z poleceniem „rób następne po kolei”.
- Fakty z wyszukiwania (Guinness World Records, Edinburgh Zoo, Wikipedia, RNZ):
  - 1961: Norweska Gwardia Królewska występuje na Edinburgh Military Tattoo. Porucznik zainteresował się pingwinami w zoo.
  - 1972: gwardia adoptuje pingwina królewskiego Nilsa Olava.
  - Kolejne awanse (daty z lat 80. podają różne źródła różnie, więc w filmie nie ma lat): kapral, sierżant, starszy sierżant sztabowy (1993).
  - 2005: posąg z brązu w zoo.
  - 15.08.2008: tytuł szlachecki zatwierdzony przez króla Haralda V, ponad 130 żołnierzy, w akcie „in every way qualified to receive the honour and dignity of knighthood”.
  - 2016: brygadier. 2023: generał major.
  - Imię i stopień przechodzą na kolejne pingwiny (Nils Olav II, III).
- Głos: Liam v3, 1075 znaków, 63,3 s. Pierwsze nagranie (1141 znaków) trwało 68,7 s, więc tekst skróciłem i nagrałem ponownie.
- Świat (scratchpad/proj9):
  - zoo z turkusowym basenem i muralem z górami lodowymi;
  - posąg z brązu, flagi Norwegii i Szkocji, rabaty kwiatów;
  - zamek na wzgórzu z esplanadą i trybunami (tattoo o zmierzchu z fajerwerkami);
  - 124 gwardzistów w szeregach.
- Postacie: pingwin królewski (`penguin.js`) z rangami: naszywki, pagony, medale, szarfa rycerska, czapka generalska, ryba.
- Zrobione 26.11.2026: `penguin_general.mp4`, 1080×1920, 30 fps, 64,2 s, −13,9 LUFS, bez zamrożeń i czarnych klatek, 98 MB (web 12 Mb/s). Master crf17 (277 MB) został w scratchpad/proj9/out.
- Tytuł i opis: „The Penguin Who Became a General”.

## Film nr 65: „The Fake Bus Stop for People Who Wander” (26.11.2026)
- Fakty z wyszukiwania (DPA / China Daily 2008, IBTimes, mein-mmo, Lorey 2019):
  - fałszywy przystanek przed domem seniora Benrath w Düsseldorfie (nazwa domu nie pada w filmie);
  - jedna pensjonariuszka wsiadła do prawdziwego autobusu i trafiła daleko;
  - personel mówi „autobus się spóźnia, może kawy?”, a po kilku minutach pensjonariusz zapomina, że chciał wyjść;
  - pomysł rozszerzył się na całe Niemcy, a potem na świat.
- Głos: Liam v3, 1030 znaków, 61,4 s, transkrypcja zgodna.
- Świat (scratchpad/proj10):
  - żółty dom opieki z kolorowymi okiennicami i girlandą;
  - ogród z kwiatami i stolikiem z parasolem;
  - przystanek z żółto-zielonym znakiem „H”, żółty autobus, kolorowe domy;
  - pole z makami „daleko stąd”.
- Zrobione 26.11.2026: `fake_bus_stop.mp4`, 1080×1920, 30 fps, 62,3 s, −14,3 LUFS, bez zamrożeń i czarnych klatek, 94,7 MB (web 12 Mb/s). Master crf17 (265 MB) został w scratchpad/proj10/out.
- Tytuł i opis: „The Fake Bus Stop for People Who Wander”.

## Film nr 66: „Why Elevators Have Mirrors” (26.11.2026)
- Historia o skargach na wolne windy i lustrach jest anegdotą, której nikt nie potwierdził. Tekst mówi to uczciwie: „The story goes like this… Nobody can prove which building it was”.
- Pewne fakty:
  - zasada z „The Psychology of Waiting Lines” (D. Maister, 1985): „occupied time feels shorter than unoccupied time”;
  - lustro pomaga osobom na wózkach widzieć, co jest za nimi;
  - lustro optycznie powiększa ciasne wnętrze.
- Historię o lotnisku w Houston pominąłem, bo też jest niepotwierdzona.
- Głos: Liam v3, 981 znaków. Limit pauz podniosłem do 0,42 s, żeby nagranie trwało 60,2 s. Tempa i wysokości głosu nie zmieniałem.
- Świat (scratchpad/proj11):
  - plac z kolorowymi wieżowcami;
  - Sky Tower z holem (różowa ściana z tęczowymi pasami, trzy windy, wyświetlacz pięter);
  - kabina windy z lustrem: własna mapa odbić w kolorach holu, bo HDRI dawało biały blask słońca;
  - ujęcia „z punktu widzenia lustra” z ramką lustra jako HUD.
- Nauczka: pionowy kadr ma wąskie pole poziome (szerokość ≈ 0,56 × wysokość). Postacie muszą stać blisko osi kamery.
- Zrobione 26.11.2026: `elevator_mirrors.mp4`, 1080×1920, 30 fps, 61,1 s, −14,2 LUFS, bez zamrożeń i czarnych klatek, 93,2 MB (web 12 Mb/s). Master crf17 (160 MB) został w scratchpad/proj11/out.
- Tytuł i opis: „Why Elevators Have Mirrors”.
- Wszystkie trzy filmy z polecenia (64, 65, 66) dostarczone 26.11.2026. Automatyczne wznawianie usunięte.

## Film nr 64 v2: pełna scenografia (27.11.2026)
- Poprawka na prośbę użytkownika: „popraw film z pingwinem”. Zgodnie z zasadą pełnej scenografii dobudowałem (scratchpad/proj9/web/_scen9.js):
  - **Wybiegi w zoo:** laguna z flamingami, kopiec surykatek, wybieg żyraf z domem żyraf, wybieg zebr, ptaszarnia z papugami, dom słoni ze słoniami.
  - **Budynki zoo:** kawiarnia z markizą („PENGUIN CAFE”), sklep z pamiątkami („ZOO SHOP”), budka z lodami, wózek z balonami, mapa zoo, drogowskazy, kosze, ławki, latarnie, donice z kwiatami, żywopłoty, ogrodzenie zoo.
  - **Ludzie i zieleń:** ok. 30 stojących zwiedzających oraz dużo drzew.
  - **Edynburg:** ok. 180 kamienic z kolorowymi sklepami w rzędach wokół zoo i na zboczach zamkowego wzgórza, 5 wież kościołów i gotycki pomnik. O zmierzchu okna się świecą.
- Render wszystkich klatek od nowa do frames2 (finish.sh używa frames2). Dźwięk i napisy bez zmian.
- Zrobione 27.11.2026: `penguin_general.mp4` zastąpiony wersją v2. 1080×1920, 30 fps, 64,2 s, −13,9 LUFS, bez zamrożeń i czarnych klatek, 98,2 MB (web 12 Mb/s). Przed składaniem przejrzałem gęsto wszystkie klatki (co 15).
- Czas: render na CPU (4 rdzenie, brak GPU), 5–8 s na klatkę, czyli około 3 h na film. 27.11 użytkownik pytał, czemu to trwa ~10 h. Wyjaśniłem i zostałem przy pełnej jakości.

## Film nr 67: „When Ketchup Was Medicine” (27.11.2026)
- Wybrany samodzielnie: kolejny z listy 7 (nr 67).
- Fakty z wyszukiwania (Atlas Obscura, Mental Floss, JSTOR Daily, Popular Science, Daily Galaxy):
  - 1834: lekarz z Ohio ogłasza, że pomidory pomagają na biegunkę, niestrawność i cholerę, i publikuje przepisy na ketchup pomidorowy.
  - Sprzedawca z Cleveland sprzedaje „pigułki pomidorowe” na prawie wszystko.
  - Konkurencyjny lekarz sprzedaje własne pigułki i obaj spierają się w gazetach (lata 1837–1839).
  - Analizy wykazały, że w pigułkach nie było pomidora.
  - Moda skończyła się około 1850 roku.
- Nazwisk nie podaję („a doctor in Ohio”, „a clever salesman”, „a rival doctor”).
- Głos: Liam v3, 967 znaków, 63,3 s, 1927 klatek. Wynik ASR zgadza się z tekstem.
- Świat (scratchpad/proj12):
  - główna ulica z lat 30. XIX w.: 22 kolorowe sklepy z fasadami, drewniane chodniki, markizy, beczki, latarnie, konie, wóz „TOMATO PILLS”, kury, pies;
  - plac z altaną dla orkiestry, białym kościołem i girlandami;
  - domy, farma pomidorów ze stodołą i straganem, wychodki;
  - plakaty reklamowe, które pojawiają się dopiero od „ads everywhere”;
  - wnętrza: apteka (półki z kolorowymi butelkami, słoje, szuflady), gabinet lekarza, laboratorium, współczesny bar z ketchupem.
- Muzyka: ragtime na pianinie, 112 bpm.

- Zrobione 27.11.2026: `ketchup_medicine.mp4`, 1080×1920, 30 fps, 64,2 s, −14,2 LUFS, bez zamrożeń i czarnych klatek, 97,7 MB (web 12 Mb/s).
  - Po przeglądzie gotowych klatek poprawiłem trzy ujęcia: altana (kamera w prześwicie między kolumnami, zamiast pustej białej ściany kościoła w tle kolorowe domy i drzewa, usunięci ludzie z toru kamery), ketchup na stole (odwrócony kąt z ladą, stołkami i menu, etykieta „KETCHUP” do kamery) i zbliżenie klienta (w tle okno z kolorowym miastem, etykieta MEDICINE?! na ekranie).

## Film nr 68: „Why Lobster Was Prison Food” (27.11.2026)
- Wybrany samodzielnie: kolejny z listy 7 (nr 68).
- Fakty z wyszukiwania (History.com, Mashed, Chowhound, MIT Sea Grant „Lobster Lore”):
  - Homarów było tak dużo, że po sztormach leżały na brzegu w stertach (około 2 stóp).
  - Służyły jako przynęta i nawóz.
  - Jedli je więźniowie, służba i najbiedniejsi; skorupy w śmieciach były znakiem biedy.
  - Puszkowanie i koleje w XIX w. sprawiły, że homar stał się luksusem.
- Celowo pominąłem legendę o ustawach ograniczających homara do 3 razy w tygodniu, bo jest niepotwierdzona.
- Głos: Liam v3, 965 znaków. Pierwsze nagranie trwało 52,9 s, więc tekst wydłużyłem. Limit pauz podniosłem do 0,5 s, co dało 61,0 s i 1858 klatek.
- Świat (scratchpad/proj13):
  - kolonialna wioska (domy saltbox, płotki, studnia, dom zgromadzeń z wieżą);
  - plaża z górami homarów 3D (ok. 3000 instancji), morze, molo z beczkami przynęty, łodzie i żaglowce, latarnia morska;
  - pole nawożone homarami, budynek więzienia;
  - dworzec z parowozem i wagonami, linia telegraficzna;
  - wnętrza: więzienie, biedna chata, fabryka konserw, wagon restauracyjny z przewijanym krajobrazem za oknem, elegancka restauracja (żyrandol, menu).
- Muzyka: szanta na akordeonie, 116 bpm.
- Zrobione 27.11.2026: `lobster_prison.mp4`, 1080×1920, 30 fps, 61,9 s, −14,1 LUFS, bez zamrożeń i czarnych klatek, 94,4 MB (web 12 Mb/s).
  - Po przeglądzie gotowych klatek poprawiłem sześć ujęć: otwarcie w restauracji (homar na pierwszym planie, goście, okno z morzem), plaża (niższa kamera: horyzont, molo i żaglowiec zamiast czarnych pasów), etykiety PRISONERS i SERVANTS (na ekran), wiadro skorup w chacie (widać rodzinę i kominek), kobieta przed domem (etykieta POOR! i kosz widoczne) oraz rosnące ceny (pełna sala zamiast pustej ściany).
- Wszystkie trzy filmy z polecenia 27.11 (64 v2, 67, 68) dostarczone. Automatyczne wznawianie usunięte.

## Film „Roblox horror” wg promptu z Twittera (28.11.2026)
- Polecenie: „używając tego prompta z twittera zrób taki film (historię wymyśl sam na podstawie trendujących filmów tego typu na YT Shorts); jeśli coś jest dodatkowo płatne, to najpierw mnie poinformuj”.
- Prompt: Roblox-style horror, Blender z kodu, postacie R6, wysoki czarny potwór, lektor Adam (ElevenLabs), napisy Montserrat ExtraBold.
- Historia (własna): „In this town, every kid must be home before nine.”
  - Tyler się spóźnia i znika (zostaje czapka).
  - Max wychodzi z latarką po siostrę Lily, która siedzi pod ostatnią latarnią.
  - Ucieczka, sąsiedzi nie otwierają, gaśnie ostatnie światło.
  - Twist: „The rule was never to keep it out. It was so it knew where to find you.”
  - Drzwi Maxa są otwarte, potwór: „You're late.”
- Koszty:
  - ElevenLabs: plan free, 3019 znaków zostało, nagranie ok. 650 znaków. Plan free nie daje licencji komercyjnej (wymaga atrybucji).
  - Mixkit, Blender, Montserrat, faster-whisper: za darmo. Pixabay blokuje tę maszynę (403).
- Nagranie głosu zablokował klasyfikator bezpieczeństwa (prompt każe pytać przed wydaniem kredytów). Czekam na zgodę użytkownika.
- Środowisko:
  - Brak GPU. Blender 4.2.23 LTS w scratchpad/rb, Eevee na llvmpipe (EGL_PLATFORM=surfaceless).
  - 720x1280, 8 próbek, raytracing off, ok. 9–14 s/klatkę, upscale do 1080x1920 w finish.sh.
  - Pełna specyfikacja (1080p, 32 próbki, RT) to ok. 65 s/klatkę, czyli ok. 25 h.
- Pliki w scratchpad/rb:
  - build.py (świat i 41 ujęć przypiętych do słów);
  - faces.py, clock_tex.py;
  - voice.py (pauzy, atempo, potwór −5 półtonów, whisper large-v3-turbo + difflib);
  - audio.py (bed Mixkit m625 ze skokiem 39,25 s na „Run!”, drone, SFX pod słowa, −13 LUFS + tanh);
  - caps.py, finish.sh.
- 28.11: użytkownik przysłał wzorzec z TikToka (@neyroblox23, „In this town every time someone says your name you get a dollar”) i chce taki sam wygląd, animacje, napisy, dźwięki i przejścia.
  - Analiza wzorca:
    - jasne, nasycone 3D w stylu Roblox, kwadratowe zaokrąglone głowy, duże błyszczące oczy z odblaskiem, grube brwi, usta D z językiem, rumieńce, kolczaste włosy, bluzy ze sznurkami i plakietką;
    - nocą fioletowe niebo, poświata;
    - napisy po jednym słowie, żółtozielone (#DCF83C) z czarnym obrysem, małe litery, środek na ok. 60% wysokości;
    - cięcie co ok. 1,5 s, ciągły powolny najazd kamery;
    - lektor młody, energiczny (F0 ok. 240 Hz, 190 słów/min).
  - Przebudowa:
    - faces2.py (nowe twarze), rbox (zaokrąglone bryły), nowe postacie;
    - paleta pastelowa z fioletową nocą, Fog Glow w kompozytorze, światło wypełniające przy kamerze;
    - napisy Nunito Black 150 px w kolorze limonkowym.
- Użytkownik wybrał głos „liam”. Nagranie: eleven_v3, Liam, stability 0.5, mp3_44100_128 (192 kb/s wymaga planu Creator).
  - Zużyto 676 znaków.
  - Po obróbce narracja trwa 36,0 s (x1,189), cały film 43,7 s.
- Render: q_rb.sh (time-box 6900 s, RESUME), klatki w scratchpad/rb/frames, potem finish.sh, wynik out/roblox_curfew.mp4.
