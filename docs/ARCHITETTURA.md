# Architettura e manutenzione

## Fonte unica

`index.html` contiene markup, stile, logica, traduzioni, SVG e JSON delle musiche. Non richiede rete, librerie, font scaricati o compilazione. Gli asset esportati sono copie di lavoro; non sono caricati a runtime. Non separare automaticamente il gioco in più file, perché la consegna offline a file unico è una caratteristica del progetto.

Il motore `Engine` gestisce campo, selezione, generatore pseudocasuale con seme, coda, regole, punti e tempo. `Prime` gestisce primalità, fattori e gemelli. La UI aggiorna 36 pulsanti stabili; non deve ricreare l'intero tabellone durante gli arrivi. `tickFrame` governa il tempo, mentre pausa e visibilità impediscono l'avanzamento del motore. Il seme del motore e `Math.random()` degli effetti sono separati.

## Interfaccia

Il tabellone resta protagonista. Il menu raccoglie guida, raccolta, temi e impostazioni; i crediti sono nelle impostazioni. I pannelli condividono comandi di ritorno. Il layout usa viewport dinamica, safe area e `ResizeObserver`/`fitBoard`. Conservare etichette accessibili, focus dei pannelli e preferenza di movimento ridotto.

Nove temi espliciti: Confetti (`confetti`), Menta, Sakura, Tramonto, Alto contrasto (`carta`), Notte, Oceano, Neon e Terminale. «Automatico» (`auto`) risolve in Confetti o Notte secondo il sistema. La preferenza iniziale è Confetti. Le variabili CSS su `[data-theme]` sono la fonte dei colori; `THEMES` contiene registro e nomi, `readFx` legge i colori per le particelle.

## Localizzazione

Sei lingue: `it`, `en`, `es`, `fr`, `de`, `ja`. `language: auto` rileva il dispositivo, con ripiego inglese. I testi e le etichette sono gestiti da `I18N_ROWS`, dalle altre tabelle/mappature di traduzione e dalle funzioni di localizzazione nello stesso HTML. Tradurre anche placeholder, messaggi dinamici, etichette accessibili e condivisione. Cambiare lingua non deve rigenerare la partita.

## Audio

`musicAssets` incorpora le tracce `calm` e `rhythm` in base64. Un solo contesto Web Audio, bus separati per musica ed effetti, decodifica differita e loop originali. L'avvio richiede un gesto dell'utente; supporto e riproduzione dipendono dal browser. Menu e background sospendono la musica, salvo l'anteprima esplicita nelle impostazioni. Gli effetti sono sintetizzati con oscillatori, non file esterni. L'aptica usa le capacità disponibili nel browser.

## Dati sul dispositivo

| Chiave | Contenuto |
| --- | --- |
| `cbm-primi-v1` | Lingua, tema, suono/musica e volumi, aptica, tutorial completato, record per modalità, giorno e consumo dei suggerimenti |
| `cbm-primi-collection-v1` | Mappa primo → numero di creazioni |

Non è presente il salvataggio/ripristino di una partita in corso dopo il caricamento della pagina. Il seme viene mostrato nel risultato; il replay è disponibile dalla sessione. Se `localStorage` fallisce, un avviso segnala che record, raccolta e preferenze durano solo la sessione. Non cambiare i nomi delle chiavi senza una migrazione dei dati esistenti.

## Aggiornamento

1. Modificare la fonte `index.html`.
2. Eseguire `python3 scripts/extract_assets.py` e poi `--check`.
3. Verificare le regole toccate, i tre modi di gioco, la pausa e il mantenimento della selezione.
4. Controllare le sei lingue e i temi interessati su layout mobile, audio e assenza di richieste di rete.
5. Aggiornare canon, changelog, crediti e note di verifica.

Non sono stati trasferiti wrapper, configurazioni di store o pipeline native di Droplet/Photon: questo repository contiene il progetto web PRIMI.
