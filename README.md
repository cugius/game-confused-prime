# Confused Prime — Confused By Me

Puzzle sui numeri primi, in un unico file HTML che funziona offline.

**Come si gioca:** tocca un centro ◎, scegli da 1 a 8 dei suoi vicini (diagonali incluse) e fondi la loro somma in un numero primo per guadagnare somma² punti. Coppie di primi uguali e tris di valori uguali si eliminano pagando punti per fare spazio. Se le 36 caselle si riempiono, la partita finisce.

## Modalità
- **Normale** — una tessera in arrivo ogni 8 s, che accelera al crescere del primo massimo. Suggerimenti limitati a 5 al giorno.
- **Time Attack** — 67 secondi: le fusioni danno tempo, eliminazioni e suggerimenti lo consumano.
- **Allenamento** — senza timer, una sola tessera dopo ogni azione, suggerimenti illimitati.

## Funzioni
- 9 temi (Confetti, Menta, Sakura, Tramonto, Alto contrasto, Notte, Oceano, Neon, Terminale) più "Automatico", che segue il tema chiaro/scuro del dispositivo. Scelta salvata sul dispositivo.
- 6 lingue: italiano, inglese, spagnolo, francese, tedesco, giapponese. Inglese predefinito; le preferenze già salvate sono conservate.
- Zoom del browser bloccato tramite viewport, touch-action e gestione di gesti, doppio clic e scorciatoie. Scorrimento dei pannelli e slider restano disponibili.
- Musica ed effetti sonori con volumi separati, aptica, raccolta dei primi creati, tutorial interattivo.
- Layout pensato per smartphone (da 320 px di larghezza).

## Usarlo
Apri `index.html` in un browser. Per pubblicarlo basta attivare GitHub Pages su questo repository (branch principale, cartella radice).

## Note tecniche
- Nessuna dipendenza: HTML, CSS e JavaScript in un solo file; le musiche sono incorporate (per questo il file pesa circa 1,8 MB).
- I colori vivono solo in variabili CSS su `[data-theme]`; i nuovi temi si aggiungono definendo un blocco di variabili e una voce nell'elenco `THEMES`.
- Preferenze e record in `localStorage` (`cbm-primi-v1`, `cbm-primi-collection-v1`).

## Fonte e materiali del progetto

La versione attuale è **Confused Prime**, basata su PRIMI v2.8, importata con Claude nel commit `10d6123` del 23 ottobre 2026. `index.html` nella radice è la fonte autorevole e resta autosufficiente: non richiede gli asset separati per funzionare. La vecchia versione `primi.html` v1.9 è un riferimento storico, non una sorgente da ripristinare.

| Percorso | Contenuto |
| --- | --- |
| `index.html` | Gioco completo, CSS, JavaScript, traduzioni e musiche incorporate |
| `assets/audio/` | Due MP3 esportati senza modifiche dai dati incorporati |
| `assets/icons/` | Undici SVG esportati dal CSS attuale |
| `assets/manifest.json` | Provenienza, loop, dimensioni, checksum e selettori delle icone |
| `docs/CANON-MECCANICHE.md` | Regole effettive della v2.8 |
| `docs/ARCHITETTURA.md` | Motore, UI, lingue, temi, audio e salvataggi |
| `docs/CREDITI-E-ASSET.md` | Origine e gestione dei materiali |
| `docs/MIGRAZIONE.md` | Confronto con la v1.9 e criteri di importazione |
| `docs/CHANGELOG.md` | Cronologia ricostruita e deposito dei materiali |
| `docs/VERIFICA.md` | Verifiche eseguite e limiti |
| `scripts/extract_assets.py` | Esportazione ripetibile e controllo degli asset |

Per aggiornare il progetto, modifica `index.html`, poi esegui:

```sh
python3 scripts/extract_assets.py
python3 scripts/extract_assets.py --check
```

Aggiorna contestualmente documentazione e crediti. Le copie in `assets/` sono derivate: modificarle da sole non cambia il gioco. Non sono necessari npm, bundler, CDN o un server per giocare. Per una prova HTTP locale: `python3 -m http.server 8000`.

La versione v2.8 è quella identificata dal commit di Claude; alcuni testi interni e il risultato condiviso riportano ancora v1.9. Il deposito dei materiali conserva questi testi e il gioco originale byte per byte. Non sono presenti wrapper nativi o integrazioni Game Center/Play Games in questo progetto.

## Crediti
Musiche "Orbital Guidance" e "Pulsar Horizon" da Confused Photon, generate con Google Gemini. Suoni e grafica creati per Confused Prime. Prototipazione assistita da ChatGPT / Codex di OpenAI; grafica, temi e layout v2.2–v2.8 con Claude.

## Sito

https://confused-prime.candidloach2.chatgpt.site

Il file pubblicato è identico a `index.html` di questo repository. Il nome Confused Prime compare su home, intestazione, pannelli, crediti e risultati condivisi. Le chiavi storiche `cbm-primi-*` rimangono per conservare i salvataggi.
