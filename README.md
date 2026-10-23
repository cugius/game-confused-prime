# PRIMI — Confused By Me

Puzzle sui numeri primi, in un unico file HTML che funziona offline.

**Come si gioca:** tocca un centro ◎, scegli da 1 a 8 dei suoi vicini (diagonali incluse) e fondi la loro somma in un numero primo per guadagnare somma² punti. Coppie di primi uguali e tris di valori uguali si eliminano pagando punti per fare spazio. Se le 36 caselle si riempiono, la partita finisce.

## Modalità
- **Normale** — una tessera in arrivo ogni 8 s, che accelera al crescere del primo massimo. Suggerimenti limitati a 5 al giorno.
- **Time Attack** — 67 secondi: le fusioni danno tempo, eliminazioni e suggerimenti lo consumano.
- **Allenamento** — senza timer, una sola tessera dopo ogni azione, suggerimenti illimitati.

## Funzioni
- 9 temi (Confetti, Menta, Sakura, Tramonto, Alto contrasto, Notte, Oceano, Neon, Terminale) più "Automatico", che segue il tema chiaro/scuro del dispositivo. Scelta salvata sul dispositivo.
- 6 lingue: italiano, inglese, spagnolo, francese, tedesco, giapponese.
- Musica ed effetti sonori con volumi separati, aptica, raccolta dei primi creati, tutorial interattivo.
- Layout pensato per smartphone (da 320 px di larghezza).

## Usarlo
Apri `index.html` in un browser. Per pubblicarlo basta attivare GitHub Pages su questo repository (branch principale, cartella radice).

## Note tecniche
- Nessuna dipendenza: HTML, CSS e JavaScript in un solo file; le musiche sono incorporate (per questo il file pesa circa 1,8 MB).
- I colori vivono solo in variabili CSS su `[data-theme]`; i nuovi temi si aggiungono definendo un blocco di variabili e una voce nell'elenco `THEMES`.
- Preferenze e record in `localStorage` (`cbm-primi-v1`, `cbm-primi-collection-v1`).

## Crediti
Musiche "Orbital Guidance" e "Pulsar Horizon" da Confused Photon, generate con Google Gemini. Suoni e grafica creati per PRIMI. Prototipazione assistita da ChatGPT / Codex di OpenAI; grafica, temi e layout v2.2–v2.8 con Claude.
