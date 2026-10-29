# Changelog

## 2026-10-29 — v2.13 revisione canon (Claude)

- Impostazioni in tre schede secondo UX-07: Gioco, Aspetto, Audio e accessibilità.
- Jingle di fine partita sul bus Musica e sotto l'interruttore Musica (AU-03).
- Nessuna lente o menu di copia sul campo di gioco (IN-02).
- Versione unica in `src/VERSION`; footer e risultati mostrano 2.13 (REL-03).
- Documenti: `docs/SICUREZZA.md`, `docs/PRESTAZIONI.md`; eccezioni aggiornate in `docs/CANON.md`.

## 2026-10-29 — v2.13 home secondo il canon (Claude)

- Home: Info in alto a sinistra, Aiuto in alto a destra, marchio al centro (UX-01 ora conforme).
- Strumenti in basso: Primi creati e Impostazioni (al posto di Aspetto e Come si gioca).
- Sfondo animato della home: tessere con numeri che scorrono piano; fermo con riduci movimento.

## 2026-10-29 — AU-08 concluso (Claude)

- Politica audio decisa come Confused Words: playback su iOS, interruttori di gioco rispettati, musica di altre app non interrotta su wrapper nativo, riattivazione dopo interruzione. Dettagli in `docs/CANON.md`.

## 2026-10-29 — v2.12 test, CI e completamento del canon (Claude)

- Test funzionali (`tests/test_app.py`, 25 controlli), misure di memoria e frame (`tests/perf.py`), lint (`scripts/lint.py`), workflow CI.
- Home senza scroll su 40 viewport, comprese le orizzontali basse (320 e 340 px di altezza).
- Salvataggi con campo `v`: valori fuori tipo corretti al caricamento.
- Documentazione: `docs/I18N.md`, politica audio e revisione SEC-04/CODE-02 in `docs/CANON.md`.

## 2026-10-29 — v2.11 sorgenti, canon e accessibilità (Claude)

- Sorgenti separati in `src/`; `index.html` è generato con `scripts/build.py`, che `--check` verifica.
- Zoom bloccato solo sul campo di gioco; menu, impostazioni e guida tornano zoomabili. Rimosso `user-scalable=no` e `maximum-scale`.
- Nuovo interruttore "Riduci movimento" in Impostazioni › Gioco, anche con la preferenza di sistema.
- Aptica mostrata solo dove il dispositivo la supporta: nascosta su iOS e dove `navigator.vibrate` manca.
- Area di tocco di Pausa e Suggerimento estesa a 44×44.
- Rimossi `openThemes`, `themeName`, `toggleSound`, la variabile di debug `window.__lockHome` e 53 selettori CSS senza usi.
- Eccezioni al canon UX-01, UX-07, UX-08 documentate in `docs/CANON.md`.

## 2026-10-24 — v2.10 menu come Confused Words (Claude)

- Home: una sola icona impostazioni (cursori, come Confused Words) e riga di tre strumenti: Come si gioca, Primi creati, Aspetto.
- Impostazioni a schede Aspetto / Gioco / Info, con carosello dei temi e puntini di posizione.
- Menu di pausa: pulsante Riprendi, poi Impostazioni, Come si gioca, Primi creati; in fondo Riprova, Nuova partita, Home.
- In partita: pulsante pausa tondo al posto di "Menu".
- Home bloccata senza scorrimento quando il contenuto entra nello schermo.
- Campi di testo e select a 16 px per evitare l'ingrandimento automatico su iOS.
- Ripristinati i collegamenti di musica, effetti, aptica, lingua e prova suoni, e corretto il trascinamento degli slider.

## 2026-10-24 — v2.9 schermi corti e orizzontale (Claude)

- Schermi corti (< 620 px di altezza): intestazione, HUD e pannello compattati; la tabella cresce di circa 50-70 px con le barre del browser aperte.
- Layout orizzontale a due colonne (tabella a sinistra, punteggio e azioni a destra).
- Aree di tocco ampliate per Menu e Suggerimento.
- Unito con le modifiche Confused Prime / blocco zoom: nome, wordmark, inglese predefinito e blocco dello zoom sono conservati. Il commit 2d7d412 le aveva sovrascritte per errore; questo commit le ripristina sopra la v2.9.

## 2026-10-24 — Confused Prime e blocco zoom

- Allineato il repository alla versione già pubblicata come Confused Prime: nome in home, partita, crediti, pannelli e condivisione; wordmark adattato agli schermi stretti.
- Inglese predefinito mantenendo le preferenze e i record salvati.
- Bloccati pinch, doppio tap/doppio clic, gesti Safari e scorciatoie di zoom; scorrimento dei menu e slider conservati.
- Aggiornati manifest degli asset e sito con lo stesso HTML.


## 2026-10-23 — Deposito e allineamento dei materiali

- Adottata come fonte unica la revisione Claude PRIMI v2.8 già presente in `index.html` su `main` (`10d6123`). HTML e comportamento conservati byte per byte.
- Recuperata e confrontata la precedente versione PRIMI v1.9.
- Esportate le due musiche originali e gli undici SVG attuali, con manifest, provenienza, hash e punti di loop.
- Aggiunto lo script di esportazione e controllo; aggiornato il README.
- Aggiunti canon delle regole, architettura, crediti, resoconto della migrazione e verifica.
- Registrata la presenza preesistente di etichette interne v1.9 nel gioco identificato come v2.8.

## 2026-10-23 — PRIMI v2.8 su Git (Claude)

Dal commit `10d6123`: design system con variabili CSS, nove temi e Automatico, pannelli uniformi, icone nei menu, HUD e numeri più grandi, cinque suggerimenti giornalieri in Normale, traduzioni delle nuove stringhe nelle sei lingue e README. Per la cronologia delle modifiche intermedie v2.2–v2.7 non sono disponibili commit distinti in questo repository.

## 2026-10-21 — PRIMI v1.9 (precedente file di progetto)

Sei lingue: italiano, inglese, spagnolo, francese, tedesco e giapponese; scelta automatica o manuale, traduzioni della UI e dei risultati. Questa voce descrive il materiale precedente recuperato, non una release Git.
