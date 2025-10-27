---
title: MISP how-to: intro
url: https://roccosicilia.com/2025/08/25/misp-how-to-intro/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-25
fetch_date: 2025-10-07T00:17:04.554927
---

# MISP how-to: intro

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [MISP how-to: intro](https://roccosicilia.com/2025/08/25/misp-how-to-intro/)

Published by

Rocco Sicilia

on

[25 agosto 2025](https://roccosicilia.com/2025/08/25/misp-how-to-intro/)

[![MISP how-to: intro](https://roccosicilia.com/wp-content/uploads/2025/06/msip-logo-e1751036894452.png?w=250)](https://roccosicilia.com/2025/08/25/misp-how-to-intro/)

In qualche occasione ho raccontato che non amo scrivere how-to ma devo fare un’eccezione per MISP e per il progetto eg0n. Non tutti conoscono la piattaforma ed ho pensato che mettere a disposizione qualche info base (seguiranno dei video credo) possa essere d’aiuto a chi si vuole unire al progetto anche solo per fare pratica con il mondo della Threat Intelligence.

---

Se gli argomenti che porto sul blog ti sono stati utili puoi supportare il mio progetto di divulgazione iscrivendoti al mio canale [Patreon](https://patreon.com/roccosicilia). Registrati al blog per rimanere aggiornato sui prossimi articoli.

Digita la tua e-mail…

Iscriviti

---

#### Introduzione

MISP è un software open source che ha come principale fine quello di documentare gli elementi di un incidente di sicurezza o una tipologia di minaccia informatica in una forma strutturata così da poterne isolare le caratteristiche e le peculiarità. Ad esempio in casi di individuazione di un tentativo di brute forcing di un accesso SSH, evento abbastanza frequente per molti sistemi esposti in rete pubblica, l’analisi del log può fornire alcuni elementi peculiari di questo tentativo:

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-13.png?w=1024)

Esempio di log /var/log/auth.log

È possibile infatti identificare gli IP sorgenti del tentato accesso, gli username utilizzati (anche le password in determinate condizioni), la frequenza dei tentativi e documentare questi elementi all’interno di un evento specifico, con un proprio ID univoco ed informazioni di dettaglio.

La piattaforma è, di fatto, l’interfaccia ad un complesso database in cui vengono documentate le informazioni su eventi anomali o sospetti, informazioni che possono essere poi utilizzate in vari modi, condivise con altri enti, arricchite, correlate.

Il concetto di base è abbastanza semplice: se due enti, ad esempio due CSIRT o due SOC, utilizzano una propria istanza MISP per documentare tutto ciò che analizzano durante le proprie indagini è poi possibile mettere in comunicazione le due istanze per condividere reciprocamente le informazioni e scambiarsi nuovi dati e feedback. Un ente/azienda potrebbe utilizzare gli stessi dati per consentire al ai proprio strumenti di detection di conoscere specifici indicatori di compromissione su cui basare nuove analisi.

#### Il concetto di evento

Come accennato all’interno di MISP l’elemento principale è l’evento, un oggetto che al suo interno contiene tutti gli elementi tecnici e le note relative ad un fatto analizzato come una campagna di phishing o un DDoS.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-14.png?w=1024)

Esempio analisi campagna di Phishing

Ogni evento ha diversi elementi che lo caratterizzano:

* l’ID è l’identificativo univoco per l’istanza MISP che stiamo utilizzando
* lo UUID è un identificativo univoco che si riferisce all’evento in modo, appunto, univoco anche quando viene condiviso con altre istanza
* Creator org: è l’organizzazione (intesa come gruppo di persone all’interno di una istanza) che ha creato l’evento
* Owner org: è l’organizzazione che detiene l’evento all’interno dell’istanza
* Creator user: è l’utente che ha creato l’evento
* Tags: esiste una complessa struttura di tag
* Date: in riferimento alla data di creazione dell’evento, non si riferisce agli artefatti
* Threat Level: è un livello di severità (low, mediun, high)
* Analysis: è lo stato di analisi (Initial, )
* Distribution: si riferisce alla condivisione dei dati tra diverse community/istanze, tema che affrontiamo in un prossimo post
* Published (yes/no): un evento pubblicato viene reso disponibile alla condivisione ed al “consumo”
* Sighting: un counter dei feedback ricevuti, anche questo aspetto lo approfondiremo in un prossimo post

Oltre a questi dati base sono ovviamente fondamentali gli attributi, ovvero tutti quegli elementi tecnico o di contesto che riguardano l’evento come l’indirizzo IP dell’host da cui proviene il tentativo di login con il dettaglio sull’orario, l’utente utilizzato, la porta sorgente ed ogni altro eventuali dato di arricchimento: il provider, eventuale hostname, dati dalla scansione passiva (info da Shodan) e tutto ciò che è possibile indagare per ricostruire al meglio l’evento.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-15.png?w=1024)

Info raccolte in relazione ad una campagna di Phishing

Ogni evento racconta una storia specifica e potrebbe riferirsi a singoli episodi o ad analisi più complesse: potrebbe essere documentato un singolo incidente relativo ad un tentativo di phishing/scam o una intera campagna di phishing che si riferisce a decine di email.

Per praticità, all’interno dell’organizzazione (MISP) BitHorn, abbiamo valutato come utile aggregare gli attributi in eventi che possono fungere anche da “collection”. Possiamo quindi creare un evento dedicato a tutte le analisi di hosts che eseguono azioni sospette di Acvite Scanning invece di creare un evento per ogni Active Scanning intercettato (es: event ID 1374 della nostra istanza MISP).

#### Attributi e oggetti

Introduco il concetto ma anticipo che su questo tema probabilmente ci sarà occasione di approfondire. Come detto l’attributo è il singolo dato che si vuole documentare.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-16.png?w=1024)

Esempio di attributo

Si potrebbe, ad esempio, voler documentare l’IP sorgente di una conversazione tra host. In questo caso l’attributo farà parte della categoria *Network Activity* ed avrà *Type* impostato come *ip-src*. È inoltre possibile definire una data e ora della prima e dell’ultima volta in cui l’attributo è stato osservato.

Nel contesto della Threat Intelligence è molto importante collocare nel tempo un evento in quanto le condizioni dei sistemi e delle reti sono soggette a variazioni: è perfettamente normale che i dati raccolti su un certo indirizzo IP nel 2023 non siano più validi nel 2025. Le analisi devono quindi riportare un periodo di validità che per convenzioni è quello in cui si sono osservate le evidenze documentate.

I singoli attributi possono essere aggregati in oggetti, ad esempio potrei descrivere un oggetto “url” con più attributi come la *url* analizzata ed il payload che è stato rinvenuto come contenuto dell’host a cui la *url* puntava:

![](https://roccosicilia.com/wp-content/uploads/2025/08/screenshot-2025-08-25-at-00.10.49.png?w=1024)

Esempio di oggetto

Attributo ed oggetto possono inoltre essere messi in relazione, o meglio possono essere referenziati tra loro al fine di avere delle vere e proprie relazioni a livello di funzione o paternità del singolo elemento. In una mia recente analisi ho, ad esempio, raccontato di una serie di *redirect* che il threat actor aveva implementato per portare l’utente su un sito di phishing.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-17.png?w=1024)

Relazione tra Oggetti

Una volta messi in relazione gli oggetti è stato possibile ottenere un riscontro grafico di quanto descritto nell’evento. Per quanto la parte grafica non sia particolarmente accattivante è molto utile dis...