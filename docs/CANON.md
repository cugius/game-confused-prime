# Confused Prime — applicazione del Canon

Canon applicato: **Confused By Me — Canon di design e sviluppo, versione 0.4 (29 ottobre 2026)**.
Revisione condotta sul ramo `main` dopo il commit `aabb431` (PRIMI v2.10). I controlli sono statici sul codice e automatici in emulazione (Chromium headless, viewport e user agent simulati); nessuna prova su dispositivo fisico.

Questo file contiene il riepilogo delle regole applicabili, le eccezioni del gioco e il motivo di ciascuna. Il testo completo del canon non è duplicato qui.

## Eccezioni documentate

| ID | Regola del canon | Scelta di Confused Prime | Motivo |
|---|---|---|---|
| UX-07 | Sezioni stabili: Gioco, Aspetto, Audio, Accessibilità/lingua | Tre sezioni: Aspetto, Gioco (lingua, audio, aptica, riduci movimento), Info. | Il gioco ha poche opzioni: separare audio e accessibilità produrrebbe schede quasi vuote. Le opzioni di accessibilità (riduci movimento, aptica) sono in Gioco, sotto le voci audio. |
| UX-08 | Area di tocco di almeno 44×44 | Il disegno del pulsante Pausa è 40×40 (36×36 su schermi bassi) e quello di Suggerimento è alto 26–34 px. L'area di tocco reale è estesa a 44×44 con uno pseudo-elemento centrato. | Il disegno resta compatto per la tabella di gioco, che ha la priorità. L'area estesa è verificata in emulazione, non su dispositivo fisico. |

## Esiti per area (commit `aabb431` più le modifiche di questa revisione)

| Area | Esito | Note |
|---|---|---|
| Home (UX-01) | Passa | Info in alto a sinistra, Aiuto in alto a destra, marchio al centro. Impostazioni in basso. Sfondo animato decorativo, fermo con riduci movimento. |
| Impostazioni (UX-07) | Passa | Tre schede: Gioco (lingua, guida, raccolta, crediti), Aspetto (temi), Audio e accessibilità (musica, effetti, aptica, riduci movimento). |
| Navigazione (UX-03/04/05/06) | Passa | Indietro, Home e Chiudi funzionano; aprire menu, impostazioni, raccolta o guida ferma la partita; cambio di app mette in pausa. |
| Tab e accordion (UX-09/10) | Passa | Tab con frecce da tastiera, ruoli ARIA, scheda conservata al ritorno. Nessun accordion. |
| Audio (AU-01/02/03) | Parziale | Interruttori e volumi separati e salvati. Verificato per il solo canale web. |
| Audio (AU-04/05/06/08) | Non verificato / N/A | AU-06 riguarda il wrapper iOS, che non esiste ancora. Ripresa della musica dopo la pausa non verificata su dispositivo. |
| Input (IN-02/03) | Passa | Zoom bloccato sul campo di gioco; menu, impostazioni e guida restano zoomabili. |
| Accessibilità (AC-01) | Passa | Interruttore "Riduci movimento" in Gioco; segue anche la preferenza di sistema. |
| Accessibilità (AC-03) | Passa | Aptica mostrata solo dove `navigator.vibrate` è disponibile e non su iOS. |
| Lingue (LO-02/04, I18N) | Parziale | Sei lingue; lingua predefinita inglese, poi lingua del dispositivo; controllo automatico dei testi. Manca un inventario completo delle chiavi. |
| Schermi (RESP-01/02/04) | Parziale | 17 viewport più le varianti con barre e in orizzontale. Schermo 320×458 e home in orizzontale scorrono ancora. Testo ingrandito e dispositivi fisici non provati. |
| Tutorial (TUT-01–04) | Passa | Raggiungibile dalla guida, saltabile, tradotto, isolato dai record. |
| Game Center (GC-*) | N/A | Il gioco non usa Game Center. |
| Sviluppo (DEV-01, REPO-03) | Passa | `src/` è la fonte; `index.html` è generato da `scripts/build.py` (`--check` verifica la corrispondenza). |
| Codice morto (CODE-01/02) | Parziale | Rimosse `openThemes`, `themeName`, `toggleSound` e 53 selettori CSS senza usi. Analisi statica: non esclude handler o stringhe costruite a runtime. |
| Debug (CODE-06) | Passa | Rimossa la variabile globale `window.__lockHome`. |
| Test automatici (REL-02, CODE-03) | Non passa | Nessun test né lint nel repo. |
| Memoria (MEM-*) | Non verificato | Nessuna misura di heap, frame time o cicli. |
| Sicurezza (SEC-*) | Passa | Revisione completa in `docs/SICUREZZA.md`. |
| Memoria e prestazioni (MEM-*) | Passa (headless) | Budget e misure in `docs/PRESTAZIONI.md`. Profilo su dispositivo ancora da fare. |
| IN-02 | Passa | Lente e menu di copia disattivati sul campo di gioco. |
| AU-03 | Passa | Il jingle di fine partita passa dal bus Musica e segue l'interruttore Musica. |

## Eccezioni aggiornate (v2.13)

- **UX-08 (SHOULD):** disegno del Pulsante Pausa 40×40 (36×36 su schermi bassi), Suggerimento alto 26–34 px; area di tocco 44×44 tramite pseudo-elemento. Motivo: priorità alla tabella di gioco.
- **DEV-02 / CODE-05 (SHOULD):** il gioco resta un unico file HTML, senza moduli separati, per l'esecuzione offline senza server. La separazione è nei sorgenti `src/` (logica e stile separati, `app.js` unico).
- **IN-01 (MUST, applicato in parte):** il gioco usa solo tocchi a singolo dito (eventi `click`), senza combinazioni simultanee; non traccia `pointerId`. Le annullazioni del tocco sono gestite dal browser e dal blur, non dalla logica di gioco.
- **REL-03 (MUST, parte applicabile):** versione unica in `src/VERSION`, inserita nel footer e nel testo dei risultati. Non ci sono bundle, Bundle ID o entitlements: web.

## Decisioni e verifiche aggiunte (v2.12)

**AU-08 — politica audio (decisa).** Stessa politica di Confused Words (`AppDelegate.swift`, `Web/index.html`):
- categoria `playback` su iOS: musica ed effetti di gioco suonano anche con il tasto Silenzioso attivo, come richiede un gioco con musica. Motivo: la scelta è stata fatta anche per la segnalazione di assenza di audio, ed è coerente con il sibling;
- gli interruttori Musica ed Effetti dentro il gioco sono sempre rispettati (AU-01);
- la musica di altre app non viene interrotta: su wrapper nativo `mixWithOthers`. Sul web Safari non offre questa opzione: il comportamento resta quello del sistema;
- fine di un'interruzione: il contesto audio si riattiva e la musica riparte come in Confused Words.

Da ratificare nel canon comune: il canon non fissa questa scelta. Questa proposta è quella già in uso nel sibling.

**AU — ripresa dopo interruzione.** Quando l'app torna in primo piano la partita resta in pausa (UX-05). Il contesto audio si riattiva al primo tocco valido (`unlock`) e la musica riparte solo se la partita non è in pausa. Non è automatico: è il comportamento richiesto dal canon per i gesti necessari. Non verificato su iPhone reale.

**SEC-04 — innerHTML.** Dieci assegnazioni in `src/app.js` (righe elencate da `scripts/lint.py`). Tutte interpolano solo costanti, numeri formattati, traduzioni o valori del motore. Nessun testo immesso dall'utente o letto dal salvataggio viene inserito nel DOM. Il campo di ricerca della raccolta accetta solo cifre.

**CODE-02 — usi indiretti.** Lookup costruiti a runtime controllati: `$('q'+i)` (q0–q2), `'spanel-'+tab` (tre valori fissi), `data-theme-id` dalla lista `THEMES`. Gli ID rimasti non referenziati sono solo quelli elencati da questi lookup.

**MEM — misure (headless).** Dieci cicli partita/menu/home: heap JavaScript da 3,56 MB a 3,73 MB; dal ciclo 5 in poi resta fermo a 3,69 MB, nodi DOM costanti (478). Frame in partita: 16,7 ms medi. Non è il profilo su dispositivo fisico (MEM-05).

**Eseguito in CI** (`.github/workflows/test.yml`): build coerente, lint, test funzionali (25), misure di memoria e frame.

## Stato aggiornato

| Regola | Esito |
|---|---|
| REL-02 / CODE-03 | Parziale: test e lint nel repo e in CI. Mancano prove su dispositivo fisico. |
| MEM-01/04 | Parziale: cicli senza crescita significativa. Budget per dispositivo non definiti. |
| MEM-05 | Non verificato su dispositivo fisico. |
| RESP-02 | Passa: home senza scroll in 40 viewport, verticali e orizzontali. |
| SV-01 | Parziale: salvataggi con campo `v`, valori fuori tipo corretti. Nessuna migrazione oltre i default. |
| I18N-01–04 | Parziale: inventario in `docs/I18N.md`, controllo automatico delle sei lingue. Manca la prova di testo ingrandito. |
| AU-08 | Passa (decisione di gioco): stessa politica di Confused Words. Ratifica nel canon comune ancora da fare. |

## Ancora da fare

- Prova su iPhone reale per audio, silenzioso, aptica (N/A su iOS), ripresa dopo interruzione e multitouch.
- Prova di testo ingrandito dal sistema su dispositivo.
- Profilo di memoria e frame su dispositivo fisico, con budget per classe di dispositivo.
