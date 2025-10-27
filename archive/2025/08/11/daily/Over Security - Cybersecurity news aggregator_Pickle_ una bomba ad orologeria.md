---
title: Pickle: una bomba ad orologeria
url: https://codiceinsicuro.it/blog/pickle-una-bomba-ad-orologeria/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-11
fetch_date: 2025-10-07T00:17:46.643070
---

# Pickle: una bomba ad orologeria

[![Codice Insicuro](https://codiceinsicuro.it/assets/images/logo.png)](https://codiceinsicuro.it/)

* [Blog](https://codiceinsicuro.it/index.html)
* [About](https://codiceinsicuro.it/about)
* [Chi sono](https://codiceinsicuro.it/chi-sono/)
* [Talks](https://codiceinsicuro.it/talks/)
* [Contatti](https://codiceinsicuro.it/contatti)

Share

##### Iscriviti alla mailing list

Basta la tua email

![Paolo Perego](https://www.gravatar.com/avatar/d05560cd673cf2f4114012616fd57c33?s=250&d=mm&r=x)

[Paolo Perego](https://codiceinsicuro.it)[Follow](https://twitter.com/thesp0nge)
Specialista di sicurezza applicativa e certificato OSCE e OSCP, amo spaccare e ricostruire il codice in maniera sicura. Sono cintura nera di taekwon-do, marito e papà. Ranger Caotico Neutrale, scrivo su @codiceinsicuro.

# Pickle: una bomba ad orologeria

![Pickle: una bomba ad orologeria](data:image/png;base64...)

1386
parole -  Lo leggerai in 7 minuti

---

A volte, le vulnerabilità più critiche non sono evidenti. Si nascondono
silenziose nel codice, apparentemente innocue. Ma un aggressore abile non cerca
di abbattere i muri; cerca le chiavi dimenticate e le finestre lasciate aperte.

Analizziamo due vulnerabilità reali, che ho trovato durante un audit fatto in
emergenza, mostrando il codice problematico e la sua correzione, per capire come
un aggressore possa ottenere il controllo completo di un sistema.

In realtà, rivedere questo codice dopo un anno dalla prima segnalazione fatta
agli sviluppatori, mi ha permesso di accorgermi di una vulnerabilità che mi ero
perso per strada.

## Vulnerabilità 1: La Pistola Carica della “Deserializzazione Insicura”

Il modulo pickle di Python è potente ma pericoloso. È stato progettato per
fidarsi ciecamente della fonte dei dati. Se un aggressore può controllare il
file che viene “deserializzato”, può eseguire comandi arbitrari con gli stessi
privilegi dell’applicazione.

### Codice Vulnerabile

La vulnerabilità si trova nella funzione readCachedLogin, dove pickle.load()
viene utilizzato per leggere le informazioni di login salvate su disco.

```
|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` # /up2date_client/auth.py (VULNERABILE)  import pickle # ...  def readCachedLogin():     # ...     pcklAuth = open(pcklAuthFileName, 'rb')     try:         # QUI LA VULNERABILITÀ: pickle.load deserializza         # un file che un aggressore potrebbe controllare.         data = pickle.load(pcklAuth)     except (EOFError, ValueError):         # ...         return False     # ... ``` |
```

Il problema è che pickle.load() non si limita a leggere dati. Esegue codice per
ricostruire l’oggetto Python originale. Se il file pcklAuthFileName contiene un
payload dannoso, questo verrà eseguito.

### La Correzione: Passare a un Formato Sicuro (JSON)

La soluzione è sostituire pickle con un formato di serializzazione che gestisce
solo dati, come JSON. JSON (JavaScript Object Notation) non ha la capacità di
eseguire codice, eliminando la vulnerabilità alla radice.

```
|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` # /up2date_client/auth.py (SICURO)  import json # Sostituiamo pickle con json # ...  def readCachedLogin():     # ...     pcklAuth = open(pcklAuthFileName, 'r') # Apriamo in modalità testo 'r'     try:         # ORA È SICURO: json.load legge solo dati, non può         # eseguire codice, anche se il file è stato manomesso.         data = json.load(pcklAuth)     except (json.JSONDecodeError):         # ...         return False     # ...  # È necessario modificare anche la funzione di scrittura def writeCachedLogin():     # ...     pcklAuth = open(pcklAuthFileName, 'w') # Apriamo in modalità testo 'w'     # ...     json.dump(data, pcklAuth) # Scriviamo dati sicuri in formato JSON     # ... ``` |
```

Sostituendo pickle.load() con json.load(), abbiamo disinnescato la “pistola
carica”. Anche se un aggressore riuscisse a scrivere un file malevolo, il parser
JSON lo interpreterebbe come testo malformato e genererebbe un errore, ma non
eseguirebbe mai comandi. La minaccia di esecuzione di codice arbitrario è
completamente neutralizzata.

## Vulnerabilità 2: la race Condition

Questo attacco si verifica quando il software esegue un’azione basandosi su un
controllo obsoleto. Il codice controlla se un file esiste (Time-of-Check) e poi,
in un secondo momento, lo apre (Time-of-Use). In quella frazione di secondo, un
aggressore può scambiare il file.

### Codice Vulnerabile

Nella funzione maybeUpdateVersion, il codice controlla l’esistenza di un file,
lo rinomina e poi ne crea uno nuovo. Questo crea una finestra temporale per un
attacco.

```
|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` # /up2date_client/auth.py (VULNERABILE)  def maybeUpdateVersion():     # ...     path = cfg["systemIdPath"]     # ...     if os.access(path, os.F_OK): # <-- TIME OF CHECK         # ...         os.rename(path, savePath)         # ...      # In questa finestra, un aggressore può creare un link     # simbolico da 'path' a un file protetto (es. /etc/sudoers)      f = open(path, "w") # <-- TIME OF USE: l'azione avviene qui     f.write(newSystemId)     f.close()     # ... ``` |
```

Se un aggressore vince la “gara”, il processo root, credendo di scrivere in
path, scriverà invece sul file di sistema a cui punta il link simbolico,
corrompendolo.

### La Correzione: Operazioni Atomiche

La soluzione è eseguire la scrittura in modo “atomico”, ovvero come un’unica
operazione indivisibile. Lo standard per farlo in modo sicuro è il pattern
“write-and-rename”.

Si scrive il nuovo contenuto in un file temporaneo e sicuro nella stessa
directory.

Si usa os.rename() per sostituire atomicamente il vecchio file con quello nuovo.

```
|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` # /up2date_client/auth.py (SICURO)  import tempfile  def maybeUpdateVersion():     # ...     path = cfg["systemIdPath"]     dir = os.path.dirname(path)     # ...     try:         # 1. Crea un file temporaneo sicuro nella stessa directory         fd, tmppath = tempfile.mkstemp(dir=dir, prefix=".sysid-")          # 2. Scrivi il nuovo contenuto nel file temporaneo         with os.fdopen(fd, 'w') as f:             f.write(newSystemId)          # (Opzionale ma consigliato: copia i permessi del vecchio file)          # 3. Sostituisci ATOMICAMENTE il vecchio file con quello nuovo.         # Questa operazione è indivisibile e non può essere interrotta.         os.rename(tmppath, path)      except (IOError, OSError) as e:         # Gestisci l'errore e pulisci il file temporaneo         # ...         return 0 ``` |
```

L’operazione os.rename() è garantita dal sistema operativo come atomica sulla
maggior parte dei filesystem. Ciò significa che non c’è una finestra temporale
tra il controllo e l’azione. Il file path viene sostituito istantaneamente con
il nuovo file tmppath, eliminando qualsiasi possibilità per un aggressore di
interferire. La gara è impossibile da vincere perché non c’è più una gara.

## Off by one

La sicurezza del software richiede un approccio proattivo. Affidarsi a un
singolo livello di difesa, come i permessi del filesystem, è una strategia
fragile. È fondamentale ispezionare il codice alla ricerca di pattern
vulnerabili e correggerli alla radice, come abbiamo dimostrato. Solo eliminando
ogni anello debole è possibile rendere la catena davvero sicura.

Intanto ti lascio qui sotto tutti i modi con cui puoi stare in contatto con me.

📝 [codiceinsicuro.it](https://codiceinsicuro.it) - articoli approfonditi e
tecnici su sicurezza, vulnerabilità, best practices di sviluppo sicuro, ecc

📣 [@thesp0nge](https://bsky.app/profile/thesp0nge.bsky.social) e il canale
telegram [paoloperegoofficial](https://t.me/paoloperegoofficial) - aggiornamenti
rapidi, condivisione di risorse, interazioni con altri esperti e la community

✉️ [la newsletter di CodiceI...