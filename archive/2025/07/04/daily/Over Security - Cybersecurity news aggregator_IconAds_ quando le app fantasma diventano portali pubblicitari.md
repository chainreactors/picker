---
title: IconAds: quando le app fantasma diventano portali pubblicitari
url: https://www.securityinfo.it/2025/07/03/iconads-quando-le-app-fantasma-diventano-portali-pubblicitari/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-04
fetch_date: 2025-10-06T23:54:32.765195
---

# IconAds: quando le app fantasma diventano portali pubblicitari

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## IconAds: quando le app fantasma diventano portali pubblicitari

Lug 03, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2025/07/03/iconads-quando-le-app-fantasma-diventano-portali-pubblicitari/#respond)

---

Recentemente il team Satori Threat Intelligence di HUMAN ha scoperto un’operazione sofisticata di pubblicità fraudolenta nota come **IconAds** che coinvolge ben **352 app Android progettate per ingannare l’utente e sfuggire ai controlli**. Al picco della sua attività, questa rete generava circa **1,2 miliardi di richieste pubblicitarie al giorno**, un volume impressionante per una campagna malevola *in the wild* ([Human Security](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-alert-iconads/?utm_source=chatgpt.com)).

![](https://www.securityinfo.it/wp-content/uploads/2025/07/AD_Fraud_3-lug-2025CG-1024x683.png)

La peculiarità più preoccupante di IconAds è la capacità di **dissimulare la propria presenza sul dispositivo**: l’icona delle app veniva sostituita da un elemento trasparente e il nome veniva azzerato. **L’utente, trovandosi davanti a una schermata apparentemente vuota, non poteva individuare l’app responsabile** del comportamento intrusivo, né rimuoverla con facilità.

IconAds non è un fenomeno isolato, ma si inserisce in un filone iniziato già nel 2023, con operazioni note come **HiddenAds** e **Vapor**. In quel primo stadio i volumi di traffico fraudolento erano inferiori, **nell’ordine delle decine di milioni di richieste al giorno**, ma con l’evoluzione in IconAds gli attori malevoli hanno **moltiplicato i volumi e perfezionato le tecniche di evasione**.

![](https://www.securityinfo.it/wp-content/uploads/2025/07/SATORI-IconAds-Investigation-Global-Map_ok.jpg)

### Tecniche di offuscamento a più livelli

Gli sviluppatori hanno messo in atto **sofisticate tecniche anti-analisi**, camuffando il codice con metodi dai nomi casuali composti da zeri e “O”. Le librerie native utilizzavano l’offuscamento **O-MVLL**, e le stringhe inviate ai server C2 venivano **trasformate in parole inglesi casuali**, rendendo difficile l’individuazione delle informazioni trasmesse. **Il livello di complessità raggiunto rendeva l’analisi quasi impossibile senza una visione d’insieme coordinata**.

Ogni app collegata a IconAds comunicava con un **dominio di comando e controllo dedicato**, caratterizzato da sottodomini generati in modo sistematico. Le comunicazioni avvenivano tramite JSON con chiavi casuali e dati sul dispositivo. **Questa frammentazione delle infrastrutture C2 ha reso particolarmente ardua l’attribuzione e la neutralizzazione delle app fraudolente**, sebbene gli analisti di HUMAN siano riusciti a individuarne le tracce attraverso pattern ricorrenti.

Una delle tecniche più subdole adottate da IconAds è **l’uso degli alias per l’attività principale dell’applicazione**. Al primo avvio, veniva attivato un alias e disattivato il componente principale, **facendo “scomparire” l’app dallo spazio visibile della schermata home**. In questo modo, anche se l’utente voleva cancellarla, **non riusciva nemmeno a trovarla tra le app installate**.

L’azione dell’intera operazione risultava molto efficace per i criminali. Alcune app, come “com.works.amazing.colour”, caricavano **pubblicità interstiziali a schermo intero pochi secondi dopo l’avvio**, senza alcuna interazione da parte dell’utente, attivandole da timer o da comandi remoti. **La visualizzazione forzata generava profitti ingenti, simulando un comportamento legittimo agli occhi degli inserzionisti**, pur essendo completamente fraudolenta.

### Impatto globale e risposta al fenomeno

La diffusione delle app malevole è stata globale, con picchi **particolarmente elevati in Paesi come Brasile, Messico e Stati Uniti**. Google ha reagito rapidamente rimuovendo le 352 app dallo store e **attivando Play Protect per proteggere i dispositivi già infettati**. HUMAN, dal canto suo, ha aggiornato la sua piattaforma Ad Fraud Defense, **bloccando quasi in tempo reale il traffico generato da IconAds**.

Nonostante l’intervento di Google, **IconAds continua a evolversi**, e nuove varianti vengono sviluppate per eludere le misure di difesa. Il team Satori è ancora impegnato nel monitoraggio dell’infrastruttura, cercando di anticipare i nuovi sviluppi. **Solo un approccio proattivo e collaborativo tra aziende di sicurezza e fornitori di servizi può arginare efficacemente minacce di questo livello**.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [ad fraud Android](https://www.securityinfo.it/tag/ad-fraud-android/), [app fantasma](https://www.securityinfo.it/tag/app-fantasma/), [comando e controllo C2](https://www.securityinfo.it/tag/comando-e-controllo-c2/), [IconAds](https://www.securityinfo.it/tag/iconads/), [malware Play Store](https://www.securityinfo.it/tag/malware-play-store/), [offuscamento codice](https://www.securityinfo.it/tag/offuscamento-codice/), [pubblicità fraudolente](https://www.securityinfo.it/tag/pubblicita-fraudolente/), [Satori HUMAN Security](https://www.securityinfo.it/tag/satori-human-security/), [sicurezza mobile](https://www.securityinfo.it/tag/sicurezza-mobile/), [truffe pubblicitarie Android](https://www.securityinfo.it/tag/truffe-pubblicitarie-android/)

[Due vulnerabilità in Sudo mettono a rischio Linux: una consente l’accesso root](https://www.securityinfo.it/2025/07/04/due-vulnerabilita-in-sudo-mettono-a-rischio-linux-una-consente-laccesso-root/)
[Ransomware e conflitti d’interesse: ex...