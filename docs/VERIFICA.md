# Verifica del deposito — 23 ottobre 2026

## Controlli eseguiti

- `index.html` invariato rispetto al commit Claude `10d6123`: blob Git `82296204cb080bb821dd6b487dfddb3e8ca920a3` e SHA-256 corrispondenti alla registrazione in `MIGRAZIONE.md`.
- `python3 scripts/extract_assets.py --check`: 14 esportazioni verificate (2 MP3, 11 SVG, manifest).
- SHA-256 delle musiche verificati contro i metadati incorporati; confronto con il precedente `primi.html` v1.9: entrambe identiche.
- SVG decodificati e analizzati come XML valido.
- MP3 analizzati con `ffprobe`: i loop dichiarati rientrano nella durata delle rispettive tracce.
- Sintassi di tutti i blocchi JavaScript eseguibili verificata con Node.js 24.
- Otto scenari del motore estratto direttamente dall'HTML: fusione 3+7+1 → 11 e +121 punti; coppia di 17 a −578; tris di 4 a −48; selezione preservata dopo un arrivo; accelerazione a 101 senza azzerare il conto in corso; fusione Time Attack con +3 s e fine a tempo zero; fine a campo pieno; ripetibilità di campo e arrivo a parità di seme.
- Collegamenti locali della documentazione controllati; `git diff --check` senza errori.

## Limiti

Non è stata completata una nuova prova visuale o interattiva in browser: Playwright è disponibile nell'ambiente, ma il relativo eseguibile Chromium non è installato. Non sono quindi dichiarate nuove verifiche di layout mobile, cambio lingua in UI, riproduzione percepita o touch su iPhone. L'HTML non è stato modificato durante il deposito; i controlli sopra verificano conservazione e coerenza dei materiali, non certificano l'assenza di difetti preesistenti della v2.8.

Non sono stati avviati deploy, pubblicazioni Pages, build native o servizi esterni. La documentazione non attribuisce al progetto pipeline o integrazioni presenti negli altri giochi.
