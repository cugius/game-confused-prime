# Sicurezza — revisione delle superfici (SEC-01)

Canon v0.4. Revisione sul codice di `src/` (versione 2.13). Nessun backend, nessuna rete.

| Superficie | Cosa entra | Controllo | Esito |
|---|---|---|---|
| Input utente | Tocchi, clic, tastiera (solo scorciatoie di zoom e Escape) | Nessun testo libero; il campo di ricerca della raccolta accetta solo cifre | Passa |
| `localStorage` — preferenze (`cbm-primi-v1`) | JSON letto al caricamento | Parse in try/catch; tipi controllati per campo; numeri finiti e non negativi; valori fuori tipo tornano ai default | Passa |
| `localStorage` — raccolta (`cbm-primi-collection-v1`) | JSON di primi creati | Solo chiavi intere sicure, conteggi validati; scrittura in try/catch | Passa |
| DOM | Dieci assegnazioni `innerHTML` | Interpolano solo costanti, numeri formattati, traduzioni e valori del motore; nessun dato da storage o input | Passa |
| Traduzioni | Tabella `I18N_ROWS` nel sorgente | Fissa, non caricata da rete | Passa |
| URL e rete | Nessuna richiesta, nessun endpoint, nessun link esterno | Controllato da `scripts/lint.py` (URL esterni bloccati, eccetto i namespace SVG) | Passa |
| Dipendenze | Nessuna: un solo file HTML, musica incorporata | Inventario: nessuna libreria esterna | Passa |
| Pacchetto | `index.html` generato da `src/` con `scripts/build.py --check` | Nessun segreto nel sorgente (verificato con ricerca di chiavi comuni) | Passa |
| Audio | Web Audio API | Nessun dato dell'utente | Passa |
| Wrapper nativo | Non esiste ancora | Bridge, permessi, navigazione: da definire quando esisterà | N/A |

Rischi residui: lo storage locale può essere modificato a mano dall'utente; l'effetto è limitato ai valori di gioco e viene normalizzato al caricamento.
