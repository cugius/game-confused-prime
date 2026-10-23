# Deposito dei materiali — 23 ottobre 2026

## Fonte attuale

- Repository corretto: `cugius/game-confused-prime`, branch `main`.
- Commit iniziale del lavoro: `10d61231bb9ca66e8c7daf9df5348d57f3b36dcd`, revisione Claude PRIMI v2.8 del 23 ottobre 2026.
- File autorevole: `index.html`, 1.858.584 byte.
- SHA-256: `3da4cd9eb3ec8c1ba21c9a2e7a0527dd9fe23bc32ce8c2f4ee332184108b6e34`.
- Blob Git: `82296204cb080bb821dd6b487dfddb3e8ca920a3`.

Questo deposito mantiene il file byte per byte. Il nome Droplet era stato indicato per errore e poi corretto dall'utente; nessuna modifica è stata depositata in quel repository.

## Materiali precedenti confrontati

La cartella di progetto recuperata contiene `primi.html` e le copie caricate `primi(1).html` … `primi(4).html`. La versione gestita più recente è `primi.html`, v1.9 multilingua, aggiornata il 21 ottobre 2026: 1.817.308 byte, SHA-256 `2ceeb869d8ed85cb9bec52c2af0495c911165cab51708d004f7acc4f02544880`. È stata letta e confrontata con la fonte Git. Non sono emersi documenti o asset PRIMI separati da importare; i materiali riutilizzabili erano incorporati nell'HTML.

Le copie numerate sono precedenti della stessa fase di prototipazione e restano storiche. Non vengono aggiunte come entry point o copie attive nel repository. La v1.9 non sovrascrive la v2.8.

## Esito del trasferimento

| Materiale | Esito |
| --- | --- |
| Gioco attuale | Conservato come `index.html`, senza cambiamenti |
| Due musiche precedenti | Già presenti e identiche nella v2.8; esportate in `assets/audio/` |
| Icone attuali | Esportati gli 11 SVG unici dal CSS v2.8 |
| Regole e scelte di prodotto | Ricostruite e aggiornate dal codice in `docs/CANON-MECCANICHE.md` |
| Audio, temi, lingue e salvataggi | Documentati in `docs/ARCHITETTURA.md` |
| Provenienza e crediti | Metadati originali preservati nel manifest e documentati |
| Manutenzione degli asset | Script ripetibile con controllo `--check` |

## Differenze che prevalgono sul prototipo precedente

La v2.8 aggiunge nove temi più Automatico, SVG nei comandi, pannelli uniformi e cinque suggerimenti giornalieri in Normale. Conserva le sei lingue, il tabellone 6 × 6, le tre modalità, il sistema di punteggio, la selezione stabile durante gli arrivi, il tutorial, le due musiche e la raccolta. La documentazione descrive il comportamento effettivo attuale e non ripristina le precedenti proposte grafiche.

## Disallineamento registrato

Il commit/README identificano il gioco come v2.8, mentre alcuni testi interni del menu, delle traduzioni e della condivisione riportano ancora v1.9. È una discrepanza preesistente; non viene corretta durante questa migrazione per rispettare la richiesta di mantenere l'HTML di Git come versione attuale.
