# A Huang-akta

Magyar nyelvű, interaktív nyomozói dosszié az NVIDIA/Jensen Huang-ügyről. A kutatás állapota: **2026. november 10.** 26 forrástétel magyar, angol, kínai, japán, német és francia nyelven.

## Indítás

```powershell
npm install
npm run dev -- --port 5173
```

Megnyitás: http://127.0.0.1:5173

```powershell
npm run build
npm run preview -- --port 4173
```

A `dist` mappa statikus HTTP-kiszolgálón futtatható. A WebGPU HTTPS-en vagy localhoston működik; `file://` megnyitás helyett HTTP szükséges. A production build a `/helios-jh-gpt6astrahigh/` útvonalat használja. A helyi production előnézet címe: http://127.0.0.1:4173/helios-jh-gpt6astrahigh/.

## Funkciók

- Hat fejezet, külön hash útvonallal.
- Helios által renderelt, forgatható, saját procedurális 3D chipmodell.
- Hét szereplőből álló kapcsolati térkép, státuszjelölésekkel és forrásellenőrrel.
- Nyolc idővonalbejegyzés, pénzügyi kapcsolatok és GPU-hatásmagyarázat.
- Négy feltételes forgatókönyv; külön játékos, alkotó és helyi AI nézet.
- Nyelv, típus és szöveg szerint szűrhető forrástár; helyi mentések és jegyzet.
- JSON-letöltés; a teljes kutatási adatállomány a `public/kutatasi-jegyzek.json` fájlban is elérhető.
- Mobilmenü, billentyűzettel használható vezérlők, natív párbeszédablakok, csökkentett mozgás támogatása.

## A Helios tényleges integrációja

A `public/helios/helios_demo.js` és `.wasm` a felhasználó `D:\AI\Unreal\web\pkg` buildjének másolata. Az eredeti motorkönyvtárat nem módosítottuk. Nincs Three.js vagy más helyettesítő 3D renderer.

A motor a `public/engine.html` lapon, beágyazott módban indul. A saját `chip.helios.json` jelenet betölti a `models/evidence-chip.glb` modellt. A kamera, szüneteltetés és forgatás a motor `heliosLookAt` és `heliosSetPaused` API-ját használja. A modell 4176 háromszögből áll; újragenerálása: `python scripts/build-model.py`.

A statikus nézet az időbeli minták beállása után szünetel, hogy ne foglaljon folyamatosan GPU-t. Forgatáskor, átméretezéskor és visszalépéskor újrarenderel. WebGPU nélkül a kutatási felület olvasható marad, és jelzi a 3D nézet hiányát. A modell szemléltető alkotás, nem hiteles hardverrekonstrukció.

## Tartalom és korlátok

A forrásokhoz hozzáférési és eredetjelölések tartoznak. A 444 előfizetéses folytatását nem olvastuk; a november 10-i új chipszállítási tételből csak a nyilvános címet és metaadatot használtuk követendő nyomként. A gyanút nem nevezzük bizonyított kémkedésnek. A jövőbeli ár- és gazdasági hatások saját, feltételes elemzések.

Tartalom: `src/data.js`. Kutatási export újragenerálása: `node scripts/export-research.mjs`. Önállóan olvasható jegyzék: [KUTATAS.md](KUTATAS.md).

## Megjelenés

Grafitfekete, NVIDIA-zöld, keskeny címbetű, finom kapcsolati vonalak, nyomozási index. Az Image Gen koncepciók a `design` mappában találhatók. A generált képek tervezési referenciák; a felület valódi HTML, a chip valódi Helios/WebGPU jelenet. A honlap nem NVIDIA-kiadvány.

## Ellenőrzés

Production build; valódi Helios-jelenet helyi Chrome-ban; navigáció, csomópontok, forgatókönyv-váltás, forrásablak, szűrés, keresés, mentés, jegyzetmegőrzés és mobilos túlcsordulás vizsgálata helyi böngészőben. A Browser Harness kattintáskezelésének bizonytalansága után az interakciók elkülönített helyi Playwright-menetben is ellenőrizve.

## GitHub Pages

Nyilvános oldal: https://mp3pintyo.github.io/helios-jh-gpt6astrahigh/

Forráskód: https://github.com/mp3pintyo/helios-jh-gpt6astrahigh

A `main` ágra küldött változtatások után a `.github/workflows/pages.yml` automatikusan újraépíti és publikálja a `dist` tartalmát. A build Node 22-t és `npm ci`-t használ; a motorhoz és a jelenethez tartozó fájlok ugyanazon Pages-oldalon érhetők el.
