# Vizuális irány és ellenőrzés

Koncepciók: `concept-overview.png`, `concept-workspace.png`, a beépített Image Gen eszközzel. Brief: magyar nyomozói dosszié, hat fejezet, NVIDIA-zöld/fekete, kondenzált címbetű, chip és szereplők kapcsolatai, látható forrásbizonyosság. A teljes promptok a munkamenet képgenerálási hívásaiban szerepelnek.

## Megvalósítási döntések

1. A koncepció képi nyomozóasztalát saját, valódi 3D chip és procedurális asztal váltja: ezt a felhasználó által kért Helios-integráció indokolja. A modell nem fényképnek álcázott bizonyíték.
2. A főcím kérdőjelet kapott. A lehetséges láncreakciót a források nem támasztják alá biztos jövőbeli eseményként.
3. A két koncepció automatikusan generált tényállításai helyett ellenőrzött szerkesztői szöveg került az oldalra. Nincsenek kitalált bizalmi pontszámok.
4. A logó saját H-monogram; az NVIDIA-val való hivatalos kapcsolat látszatát kerüljük. A színvilág a kért NVIDIA-irányt követi.
5. A koncepció alsó komponensbemutatóját valóban használható, külön fejezetek váltják: idővonal, GPU-összevetés, forgatókönyvek, forráskereső.

## Összehasonlítás

| Szempont | Referencia | Megvalósítás |
|---|---|---|
| Kompozíció | Bal index, nagy bal főcím, jobb chip | Megtartva; a chip élő motorjelenet |
| Tipográfia | Kondenzált erős címsor, apró metaadat | Barlow Condensed + DM Sans + IBM Plex Mono |
| Szín | Fekete, zöld, törtfehér | #090c0a, #76b900/#a2df43, #f0f0e7 |
| Bizonyítéksáv | Három státuszos rész | Dokumentált / vizsgált / nyitott, tételes forrásgombokkal |
| Kapcsolati rajz | Vonalstílusok és oldalsó magyarázat | Valódi kiválasztás, forrásablakok, státuszok |
| Mobil | Ugyanazon információs rendszer | Összecsukható index, függőleges panelek, külön ellenőrzött nézetek |
| Mozgás | Fókuszált térbeli szemléltetés | Kézzel indítható kameraforgatás; nyugalmi állapotban GPU-szünet |

A képi koncepciókat és a böngészőből mentett képeket közvetlen képfájl-megtekintéssel összehasonlítottuk. A legfontosabb javítás a Helios kamerabeállításának időzítése, a túlzott automatikus expozíció kikapcsolása, valamint a mobilos menü és a jelenet átméretezésének ellenőrzése volt.
