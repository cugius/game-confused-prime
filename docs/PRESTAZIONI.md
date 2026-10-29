# Memoria e prestazioni (MEM-01–06)

Budget proposti per la build web, misurati con `tests/perf.py` (Chromium headless, viewport 390×844). Non sostituiscono il profilo su dispositivo fisico (MEM-05), ancora da fare.

| Grandezza | Budget | Misura | Esito |
|---|---|---|---|
| Heap JavaScript dopo 10 cicli partita/menu/home | ≤ 8 MB | circa 3,6 → 3,7 MB; crescita di 0,12 MB tra il 2° e il 10° ciclo | Passa (headless) |
| Nodi DOM | ≤ 800 | 238 a fine ciclo, costanti nei cicli | Passa |
| Tempo medio tra frame in partita | ≤ 16,7 ms (60 fps) | 16,9 ms medi, p95 16,8 ms (headless) | Passa (headless, al limite) |
| Particelle attive | ≤ 120 | Limite in `src/app.js` (sfera di particelle), non misurato al massimo | Parziale |
| Buffer audio decodificati | Brani decodificati solo quando servono | Cache per brano, decodifica su richiesta (MEM-03) | Passa |

Ciclo di vita (MEM-02): alla chiusura della partita e al ritorno a home vengono fermate le sorgenti audio, cancellati i timer dell'effetto e rimossi gli elementi floating; ripetuto nei cicli di test.

Background (MEM-06): alla perdita di visibilità la partita va in pausa e l'audio si sospende; nessuna simulazione residua.

Aperto: profilo su iPhone e Android reale, budget di memoria GPU (non rilevante con il solo canvas 2D, da confermare), prova di crescita su sessioni di un'ora.
