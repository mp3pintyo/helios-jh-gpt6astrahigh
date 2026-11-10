# Ellenőrzési jegyzék

2026. november 10., Windows / helyi Chrome és elkülönített Playwright CLI.

- `npm run build`: sikeres production build.
- Production előnézet: `http://127.0.0.1:4173`.
- 26 forrástétel, mind a hat kért nyelv; a magyar és francia szűrő külön ellenőrizve (2–2 tétel).
- Hat fejezet navigációja, kapcsolati csomópont kiválasztása, forrásablak és Escape, keresés és üres eredmény, mentés, jegyzet megőrzése újratöltés után, forgatókönyv- és olvasói nézetváltás: sikeres.
- A kutatási jegyzék letöltése valódi böngészős download eseménnyel ellenőrizve.
- Asztali ellenőrzés: 1536 × 1024. Mobil: 390 × 844; az ellenőrzött fejezetekben nincs vízszintes túlcsordulás.
- Helios: `evidence-chip` jelenet, 71 látható cluster; forgatás, megállítás, alaphelyzet és mobilos átméretezés ellenőrizve. A rögzített pillanatban 16,8 ms képkockaidő, 8,96 ms GPU-idő; ez egy helyi mérés, nem általános teljesítményígéret.
- A WASM SHA-256 egyezik a `D:\AI\Unreal\web\pkg` forrásbuilddel: `298468384504D7922BBE3374C242E375ECF53CBADE2BB4449BB2DB604AB80B6D`.
- A végső production böngészős menetben 0 JavaScript-kivétel, 0 konzolhiba. A Chrome egy WebGPU-figyelmeztetést adott: Windows alatt figyelmen kívül hagyja a `powerPreference` opciót; a renderelés működött.
- A Browser Harness célzott tabhoz kapcsolódott, de néhány kattintása nem váltott ki eseményt. Az interakciók ezért külön helyi Playwright-menetben is ellenőrizve. Cloud szolgáltatást nem használtunk.

Végső képek: [asztali nyitóoldal](design/preview-desktop.png), [kapcsolati térkép](design/preview-network.png), [mobil nyitóoldal](design/preview-mobile.png).

A kutatás dátumhoz kötött. A 444 teljes előfizetéses cikke és a 20. forrástétel teljes szövege nem volt hozzáférhető; ezt a felület és a forrásjegyzék egyaránt jelzi.
