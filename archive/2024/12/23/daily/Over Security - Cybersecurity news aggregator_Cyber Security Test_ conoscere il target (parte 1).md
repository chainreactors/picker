---
title: Cyber Security Test: conoscere il target (parte 1)
url: https://roccosicilia.com/2024/12/22/cyber-security-test-conoscere-il-target-parte-1/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-23
fetch_date: 2025-10-06T19:37:03.828714
---

# Cyber Security Test: conoscere il target (parte 1)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Cyber Security Test: conoscere il target (parte 1)](https://roccosicilia.com/2024/12/22/cyber-security-test-conoscere-il-target-parte-1/)

Published by

Rocco Sicilia

on

[22 dicembre 2024](https://roccosicilia.com/2024/12/22/cyber-security-test-conoscere-il-target-parte-1/)

[![Cyber Security Test: conoscere il target (parte 1)](https://roccosicilia.com/wp-content/uploads/2025/01/cybersecurity-test-serie.png?w=595)](https://roccosicilia.com/2024/12/22/cyber-security-test-conoscere-il-target-parte-1/)

Iniziamo subito con lo scoperchiare un enorme Vaso di Pandora e discutiamo la fase più sottovalutata da chi esegue security test: la raccolta delle informazioni. Il modello di base è molto semplice e si basa su un principio: meglio conosco il mio “avversario” e più sarò in grado di sferrare un attacco efficace.

Sul piano strategico la valutazione preliminare del target è fondamentale: l’obiettivo del potenziale threat actor deve guidare le scelte dell’analista che prepara la simulazione d’attacco. Bisogna quindi comprendere quali sono gli elementi sensibili del target, raccogliere tutte le informazioni possibili e da qualsiasi fonte e valutare un primo piano di attacco contestualizzando ciò che si è potuto scoprire. In pratica dobbiamo creare un dossier sul potenziale target.

---

Gli argomenti del post sono discussi ed approfonditi in una serie di live liberamente accessibili e di cui le registrazioni sono archiviate sul mio Patreon per i supporter.

[![](https://roccosicilia.com/wp-content/uploads/2024/12/image-13.png?w=674)](https://www.patreon.com/posts/cyber-security-1-118474393)

Video di approfondimento tecnico.

---

Da considerare che la quantità di dati che potremmo trovare e le relative informazioni che elaboreremo saranno un quantitativo elevato ed estremamente eterogeneo. Oltre alle tecniche di ricerca ed ai tools di supporto dobbiamo dotarci anche di strumenti che consentano di documentare il tutto in modo appropriato. Ho pensato di approfittare di questo argomento per rivedere il mio sistema di documentazione e condividervi i concetti di base.

## Database?

Se devo gestire molti dati destrutturati a cui voglio poter applicare una struttura mi viene voglia di usare un Database. Devo anche avere una interfaccia comoda per inserire, modificare, cercare, visualizzare le informazioni e gli elaborati del caso. Ci sono molti strumenti che si possono adottare e la scelta dipende soprattutto dalle esigenze e conoscenze dell’analista che poi ci dovrà mettere le mani. Visto che lo scopo di questi post è studio e divulgazione ci possiamo permettere di dedicare del tempo alla scrittura di qualcosa di custom. Per non partire proprio da zero e considerando che alcuni temi si toccheranno, parto dalla base del progetto ***eg0n*** per costruire una django app d’appoggio in cui metteremo i dati che ci interessano.

## Raccolta delle informazioni (passiva)

È probabile che il termine più familiare per questo task sia Passive Information Gathering e ovviamente se esistono azioni passive ne esisteranno anche di attive.

In questo primo post iniziamo quindi dalle attività che possiamo condurre senza generare sospetto, utilissime per tutti quei test che puntano ad eseguire una valutazione della postura dall’esterno basandosi sulle molte informazioni che un target potrebbe aver distribuito piò o meno volontariamente. Questo tipo di test aiuta a comprendere quanto un target stia “esponendo il fianco” o se esistono in rete informazioni potenzialmente pericolose ed utilizzabili per azioni offensive.

Il principio alla base di questi test è relativo alla riduzione della superficie attaccabile, ovvero ridurre/controllare la quantità di informazioni che esistono, in rete e non, sul target in modo da limitare l’esposizione dell’organizzazione ad inutili rischi.

---

Se ti interessano ai miei contenuti puoi abbonarti al blog lasciando la tua email:

Digita la tua e-mail…

Iscriviti

Il mio progetto di divulgazione comprende la scrittura di post e la pubblicazione di contenuti tramite Twitch Live e video. Per sostenere il progetto puoi registrarti ai miei canali o diventare un supporter su [Patreon](https://patreon.com/roccosicilia) dove pubblico anche contenuti inediti e dedicati ai supporter.

---

## Informazioni a partire dal sito web del target

Semplice quanto efficace: il sito web del target ci può fornire molti elementi che potremmo utilizzare in un secondo momento per una delle fasi del security test. Solitamente sono presenti informazioni sull’organizzazione come numero e posizione delle sedi sul territorio, dati sul modello di business ed in alcuni casi dati sul personale attivo (nomi, indirizzi email, numeri di telefono interni).

Queste informazioni non sono immediatamente utilizzabili da un threat actor ma possono essere elementi utili nelle fasi avanzate del test: i dati relativi al personale possono essere confezionati per sviluppare una campagna mirata di phishing o altre azioni di social engineering, nome e cognomi sono relativamente facili da trasformare un elenchi di utenze e email.

Il sito web stesso, se presenta componenti utilizzate da membri dell’organizzazione, potrebbe essere preso in considerazione come elemento da compromettere anche se esterno rispetto al perimetro dei sistemi IT interni. Ad esempio eventuali credenziali utilizzate per l’applicazione web potrebbero essere uguali o simili a credenziali utilizzate per sistemi aziendali o a quelle dell’utente che le gestisce, ottenerle attaccando la webapp potrebbe consentire al threat actor di aprire altre porte.

Oltre ai contenuti pubblici va considerato che ogni tanto gli sviluppatori commettono qualche errore. È sempre opportuno controllare:

* il codice HTML e JS a caccia di commenti soprattutto in versioni precedenti del sito
* eventuali directory pubblicate ma nascoste
* riferimenti a tecnologie usate per il sito web o altri elementi dell’infrastruttura

Durante la raccolta passiva va tenuto a mente il fatto che non deve esserci un contatto con le infrastrutture, ritengo accettabile eventuali attività assimilabili al normale comportamento di un utente che visita le pagine web del sito dell’organizzazione.

## Informazioni a partire dal Domain Name

Saliamo leggermente di livello rispetto al sito web e passiamo al DNS partendo dal **Nome Dominio**. Come noto i Domain Name servono a rendere intellegibili gli indirizzi degli host a cui vogliamo collegarci per accedere ad uno specifico servizio. Per visitare questo blog, ad esempio, avete digitato o richiesto di accedere a ***roccosicilia.com*** che corrisponde al Domain Name del mio sito web.

I domain name sono gestisti da enti ed aziende che ne consentono la registrazione e l’assegnazione a persone fisiche, aziende, società, ecc. ed i database con l’elenco dei nomi dominio, a prescindere dall’uso e dal proprietario, sono pubblicamente disponibili. C’è da dire che alcuni dati, per una questione di privacy, possono essere resi anonimi, come nel caso del mio nome dominio:

![](https://roccosicilia.com/wp-content/uploads/2024/12/image-3.png?w=904)

Screenshot da icann.org

La raccolta di questi dati consente di fare dei ragionamenti, anche molto speculativi, sul target. Potrebbe essere utile annotarsi i servizi correlati come gli indirizzi dei Name Server utilizzati dal target e i riferimenti delle persone coinvolte che potrebbero essere membri dell’organizzazione. Anche associare tra loro questi elementi è utili ai fini dell’analisi.

...