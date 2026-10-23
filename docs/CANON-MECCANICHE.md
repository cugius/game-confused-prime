# PRIMI — regole della versione attuale

Riferimento: `index.html` del commit `10d6123` (PRIMI v2.8, 23 ottobre 2026). In caso di divergenza, il codice del gioco è la fonte autorevole.

## Campo e selezione

Griglia 6 × 6, con 18 tessere iniziali. Ogni nuova tessera ha valore da 1 a 9; la coda mostra i tre valori successivi. Le tessere non cadono e non scorrono.

Il primo tocco sceglie il centro. Si possono aggiungere fino a otto celle occupate adiacenti al centro, comprese le diagonali. Tutti i vicini devono toccare il centro, non necessariamente gli altri selezionati. Toccare nuovamente il centro annulla la selezione; toccare un vicino selezionato lo rimuove. Un arrivo automatico conserva la selezione.

## Azioni

| Azione | Requisito | Risultato | Punti |
| --- | --- | --- | --- |
| Fondi | Almeno due tessere; somma prima | La somma resta al centro; gli altri selezionati spariscono | +somma² |
| Coppia | Esattamente due primi uguali | Entrambe le tessere spariscono | −2 × valore² |
| Tris | Esattamente tre valori uguali, anche non primi | Le tre tessere spariscono | −3 × valore² |

Dopo ogni azione valida arriva esattamente una nuova tessera. Un tentativo non valido non modifica il campo. Il punteggio può essere negativo. 1 non è primo; 2 è l'unico primo pari. La segnalazione di primi gemelli riguarda il vecchio centro e il risultato, entrambi primi a distanza 2; non aggiunge punti oltre somma². Quando tutte le 36 celle sono occupate la partita termina, anche se sarebbe teoricamente disponibile una mossa.

## Modalità e timer

| Modalità | Arrivi automatici | Tempo di partita | Suggerimenti |
| --- | --- | --- | --- |
| Normale | Inizialmente ogni 8 s, poi 6/5/4 s | Nessun conto alla rovescia finale | 5 al giorno, condivisi fra le partite su questo browser |
| Time Attack | Ogni 8 s | Parte da 67 s | −5 s per richiesta riuscita; servono più di 5 s |
| Allenamento | Nessuno | Nessun timer | Senza limite giornaliero |

In Normale il primo massimo raggiunto determina il ritmo: 101 → 6 s; 503 → 5 s; 1.009 → 4 s. Il conto già in corso non viene azzerato: il nuovo intervallo si applica dopo il prossimo arrivo. Fare una mossa non azzera il timer degli arrivi. Anche in Allenamento arriva una tessera dopo ogni azione.

In Time Attack una fusione aggiunge 3 s, una coppia sottrae 3 s, un tris sottrae 5 s. Le penalità di punteggio restano valide. Si perde a tempo zero oppure a campo pieno.

Il suggeritore preferisce la fusione con guadagno maggiore; se non ne trova, propone l'eliminazione meno costosa. Nessun costo se non esiste una mossa. In Normale viene consumato un aiuto quando è proposta una nuova selezione senza un suggerimento già evidenziato; richiedere lo stesso suggerimento ancora evidenziato non consuma un altro aiuto giornaliero. Time Attack applica il costo in tempo a ogni richiesta riuscita. Il giorno usa la data locale del dispositivo, senza server.

## Pausa, replay e raccolta

Il menu e i pannelli aperti durante la partita fermano il gioco. Il passaggio in background sospende partita e audio. Una lunga interruzione del ciclo di animazione mette in pausa, senza recuperare gli arrivi arretrati.

«Riprova la stessa partita» riusa il seme e la modalità: a parità di azioni e tempi del motore produce gli stessi valori e posizioni. Non è una registrazione automatica degli input. Le particelle usano casualità cosmetica separata.

La raccolta registra solo i primi effettivamente creati da una fusione fuori dal tutorial, anche in Allenamento. Esclude i primi iniziali e quelli semplicemente arrivati. Conserva conteggi globali, ricerca e statistiche della partita. Il tutorial guidato ha tre prove: fusione, coppia, tris.
