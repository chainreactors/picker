---
title: Programmazione Difensiva: Chiudere la Finestra su una Race Condition Critica
url: https://codiceinsicuro.it/blog/programmazione-difensiva-chiudere-la-finestra-su-una-race-condition-critica/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-02
fetch_date: 2025-10-07T00:51:28.350039
---

# Programmazione Difensiva: Chiudere la Finestra su una Race Condition Critica

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

# Programmazione Difensiva: Chiudere la Finestra su una Race Condition Critica

![Programmazione Difensiva: Chiudere la Finestra su una Race Condition Critica](data:image/png;base64...)

982
parole -  Lo leggerai in 5 minuti

---

La programmazione difensiva è una filosofia di sviluppo che si basa su un
principio semplice ma fondamentale: scrivere codice che sia robusto e sicuro
anche quando opera in condizioni impreviste o in un ambiente potenzialmente
ostile. Invece di fidarsi che tutto sia configurato perfettamente, il codice
prende la responsabilità della propria sicurezza.

Pochi esempi illustrano l’importanza di questo approccio come una race condition
critica durante l’avvio di un servizio. Analizziamo come una mentalità difensiva
possa “chiudere la finestra” su una di queste vulnerabilità fugaci ma
devastanti.

## Un passaggio di privilegi un po’ leggero

Molti servizi di sistema seguono un pattern comune: si avviano con privilegi
elevati (come root) per eseguire operazioni critiche (come creare una directory
in /run), per poi abbandonare tali privilegi e continuare a funzionare come un
utente con poteri limitati (service-user).

Senza un approccio difensivo, il codice potrebbe apparire così:

```
# Il servizio parte come root
resource_dir = "/run/my-service"

# 1. Viene creata una directory, fidandosi dei permessi di default del sistema
if not os.path.isdir(resource_dir):
    os.makedirs(resource_dir)

# 2. La proprietà viene cambiata, ma la finestra di vulnerabilità si è già aperta
uid = get_user_id("service-user")
os.chown(resource_dir, uid, get_group_id("service-user"))

# ... Il servizio continua a girare come 'service-user'
```

Il problema qui è la fiducia implicita. Il codice si fida che la umask di
default del sistema sia sicura. Se non lo è (ad esempio è 0000 o 0002 su un
sistema mal configurato), la directory viene creata per un istante come
scrivibile da chiunque (world-writable). Quando scrivo codice me ne devo curare?
Beh, se stai facendo programmazione difensiva, e leggendo questo blog è proprio
quello che ti porterò a fare, sì te ne devi preoccupare. Il tuo codice deve…
anzi, sarà resiliente quanto più possibile a configurazioni non robuste
dell’ambiente circostanze.

Quanto più possibile… per i miracoli ci attrezzeremo poi.

## Impatto: da una piccola finestra ad un takeover

Un utente malintenzionato locale può sfruttare questa minuscola finestra
temporale per creare un file o, peggio, un link simbolico all’interno della
directory. Questo punto d’appoggio può essere usato per lanciare attacchi più
gravi:

* Denial of Service (DoS): Bloccando la creazione del socket di comunicazione
  del servizio.
* Hijacking dell’IPC: Intercettando e manipolando la comunicazione interna
  dell’applicazione.
* Cross-Site Scripting (XSS): Iniettando dati malevoli che vengono poi serviti
  dall’API web a un amministratore.

## Come la riscriverei

Un po’ come nei migliori piani, la programmazione difensiva non lascia la
sicurezza al caso. Invece di sperare in una umask sicura, la impone. Il codice
prende il controllo e chiude la finestra di vulnerabilità.

La prima versione, questa che lascio per riferimento contiene un grossolano
errore. Ringrazio [Sandro “theguly”](https://www.linkedin.com/in/theguly/) per
avermelo fatto notare.

La race condition viene effettivamente limitata ma, nel caso resource\_dir esista
e sia un file, la successiva chiamata a `os.makedirs` fallisce in modo brusco,
facendo terminare l’applicazione con un’eccezione.

```
# Nel codice di setup del demone
resource_dir = "/run/my-service"

if not os.path.isdir(resource_dir):
    original_umask = -1
    try:
        # DIFESA 1: Impone una umask restrittiva, ignorando quella di sistema.
        original_umask = os.umask(0o077) # Permessi solo per il proprietario

        # DIFESA 2: Crea la directory con permessi espliciti e sicuri.
        os.makedirs(resource_dir, 0o700) # Permessi rwx------
    finally:
        # Ripristina sempre la umask originale per non alterare il sistema.
        if original_umask != -1:
            os.umask(original_umask)

# Ora, con la directory creata in modo sicuro, si può procedere con il chown.
# ...
```

Il nuovo codice quindi, deve avere anche un controllo aggiuntivo per evitare di
provare a creare una directory nel caso il file esista già.

```
if os.path.exists(resource_dir):
    # Il percorso esiste, ci assicuriamo che sia una directory.
    if not os.path.isdir(resource_dir):
        log.error(
            "Il percorso '%s' esiste già ma non è una directory. Impossibile avviare.",
            resource_dir,
        )
        # Esci in maniera pulita dal flusso di esecuzione del programma
else:
    # Il percorso non esiste, quindi lo creiamo in modo sicuro.
    original_umask = -1
    try:
        original_umask = os.umask(0o077)
        os.makedirs(resource_dir, 0o700)
    except OSError as exc:
        log.error("Impossibile creare la directory '%s': %s", resource_dir, exc)
        # Esci in maniera pulita dal flusso di esecuzione del programma
    finally:
        if original_umask != -1:
            os.umask(original_umask)

# La logica di chown per abbassare i privilegi va eseguita dopo questo blocc
```

Con questa modifica, il codice non si fida più dell’ambiente. Garantisce esso
stesso che la risorsa sia creata in modo sicuro fin dal primo istante. La
finestra è stata chiusa e gli errori sono stati gestiti in maniera opportuna.

Questo è il cuore della programmazione difensiva: non chiedere “il sistema è
sicuro?”, ma affermare “questa porzione di codice è sicura, a prescindere dal
sistema”.

## Off by one

Siamo tornati finalmente. Sono passati poco più di due anni dall’ultimo post e
finalmente sono tornato.

Se mi hai seguito, sui vari social, sai che mi sono dedicato tanto al
[canale YouTube](https://www.youtube.com/%40PaoloPerego) e a tanti audit per
rendere [openSUSE](https://get.opensuse.org) ancora più sicura.

Ora però sono tornato a produrre contenuti scritti, non sarà un’apparizione
sporadica, sento veramente molta voglia e molta energia attorno a questo
progetto che ho accantonato per un po’.

Non vedo l’ora di raccontarti cosa è successo lo scorso giugno a Norimberga,
all’[openSUSE conference](https://www.linkedin.com/posts/paolo-perego_la-mail-tanto-attesa-%C3%A8-arrivata-a-giugno-activity-7325830513800167424-iuZ5/?originalSubdomain=it),
di parlarti dei nuovi tool che sto scrivendo e di tante altre cose.

Intanto ti lascio qui sotto tutti i modi con cui puoi stare in contatto con me.

📝 [codiceinsicuro.it](https://codiceinsicuro.it) - articoli approfonditi e
tecnici su sicurezza, vulnerabilità, best practices di sviluppo sicuro, ecc

📣 [@thesp0nge](https://bsky.app/profile/thesp0nge.bsky.social) e il canale
telegram [paoloperegoofficial](https://t.me/paoloperegoofficial) - aggiornamenti
rapidi, condivisione di risorse, interazioni con altri esperti e la community

✉️ [la newsletter di CodiceInsicuro](https://codiceinsicuro.it/newsletter/) -
per articoli professionali, case study e aggiornamenti sul mio lavoro e
progetti.

📽️ [il mio canale YouTube](https://www.youtube.com/%40PaoloPerego) - per video
tutorial, webinar, conferenze e demo d...