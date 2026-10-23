# Asset di PRIMI

Esportazioni dalla versione attuale di `../index.html`, non dipendenze del gioco. Il file HTML incorpora già tutto quanto serve per giocare offline.

- `audio/calm.mp3`: Orbital Guidance, usata in home, Normale, Allenamento e tutorial.
- `audio/rhythm.mp3`: Pulsar Horizon, usata in Time Attack.
- `icons/icon-01.svg` … `icon-11.svg`: disegni SVG unici incorporati nel CSS. Il manifest associa ogni file ai selettori originali; un disegno può essere condiviso da più comandi.
- `manifest.json`: hash SHA-256 della fonte e di ciascun asset, dimensioni, metadati originali delle musiche e punti di loop in secondi.

Rigenera dalla radice con `python3 scripts/extract_assets.py`. Controlla senza scrivere con `python3 scripts/extract_assets.py --check`. Gli effetti sonori sono sintetizzati con Web Audio, mentre tabellone, tessere, temi e particelle sono prodotti dal codice: non esistono sprite o registrazioni separati da recuperare.

La disponibilità pubblica del repository non costituisce una licenza per i materiali. Vedi [crediti e provenienza](../docs/CREDITI-E-ASSET.md).
