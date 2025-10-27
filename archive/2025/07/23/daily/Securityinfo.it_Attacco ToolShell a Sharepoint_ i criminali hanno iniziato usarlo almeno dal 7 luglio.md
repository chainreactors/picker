---
title: Attacco ToolShell a Sharepoint: i criminali hanno iniziato usarlo almeno dal 7 luglio
url: https://www.securityinfo.it/2025/07/22/attacco-toolshell-a-sharepoint-i-criminali-hanno-iniziato-usarlo-almeno-dal-7-luglio/?utm_source=rss&utm_medium=rss&utm_campaign=attacco-toolshell-a-sharepoint-i-criminali-hanno-iniziato-usarlo-almeno-dal-7-luglio
source: Securityinfo.it
date: 2025-07-23
fetch_date: 2025-10-06T23:51:17.857429
---

# Attacco ToolShell a Sharepoint: i criminali hanno iniziato usarlo almeno dal 7 luglio

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

## Attacco ToolShell a Sharepoint: i criminali hanno iniziato usarlo almeno dal 7 luglio

Lug 22, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/07/22/attacco-toolshell-a-sharepoint-i-criminali-hanno-iniziato-usarlo-almeno-dal-7-luglio/#respond)

---

La [campagna di attacchi mirati che sta sfruttando una vulnerabilità zero-day in Microsoft SharePoint Server,](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/) nota come ToolShell,  e che permette ai criminali informatici di ottenere accesso remoto non autenticato e di stabilire una persistenza duratura all’interno delle reti compromesse sembvra essere attiva almeno dal 7 luglio.

Secondo i ricercatori di Check Point, che per primi hanno osservato l’exploit in-the-wild, l’attività malevola è rapidamente aumentata tra il 18 e il 19 luglio, estendendosi a diverse organizzazioni attive nei settori delle telecomunicazioni, dell’industria e della pubblica amministrazione. I server vulnerabili colpiti sarebbero oltre 85, distribuiti in almeno 29 diverse organizzazioni. Negli ultimi giorni, sembra che la vulnerabilità sia stata condivisa online con un numero imprecisato di altri gruppi criminali e adesso che è stata resa pubblica sicuramente il numero di gruppi che proveranno a usarla crescerà ulteriormente.

![](https://www.securityinfo.it/wp-content/uploads/2025/07/Calendario22-lug-2025CG-1024x683.png)

Ricordiamo che la falla sfruttata è stata identificata con il codice **CVE-2025-53770**, una vulnerabilità critica (CVSS 9.8) legata alla deserializzazione di dati non attendibili. L’exploit permette a un attaccante remoto di eseguire codice arbitrario sul server, con privilegi elevati, senza necessità di autenticazione. Secondo quanto emerso, il vettore d’attacco impiega come endpoint la pagina `/_layouts/15/ToolPane.aspx` e si basa su una catena di exploit che prevede anche il bypass delle misure di autenticazione.

Data la criticità dell’evento, riportiamo anche le tracce principali degli avvenimenti e delle violazioni. Uno degli aspetti più preoccupanti della tecnica usata riguarda il furto delle chiavi crittografiche contenute nel file `machine.config` di SharePoint, ovvero la **ValidationKey** e la **DecryptionKey**. Queste chiavi sono fondamentali per firmare e decifrare le informazioni contenute nei payload `__VIEWSTATE`, che SharePoint utilizza per la gestione dello stato dell’interfaccia utente. Una volta in possesso di queste chiavi, gli attaccanti possono generare richieste perfettamente valide per il server, rendendo possibile la compromissione anche dopo l’installazione della patch.

In alcuni dei casi analizzati, dopo l’esecuzione dell’exploit iniziale, gli attaccanti hanno distribuito una **web shell** persistente tramite PowerShell, fornendosi un punto d’ingresso permanente nei sistemi compromessi. Il malware installato viene in genere usato per mantenere il controllo remoto e per esfiltrare dati sensibili, in particolare credenziali amministrative e configurazioni interne.

Microsoft ha risposto rapidamente pubblicando una patch di emergenza per la CVE-2025-53770 e una seconda vulnerabilità correlata, la **CVE-2025-53771**, che consente bypass di autenticazione tramite manipolazione del percorso delle richieste HTTP. Entrambe sono state aggiunte al **Catalogo KEV (Known Exploited Vulnerabilities)** della CISA, che ne ha imposto l’aggiornamento obbligatorio a tutte le agenzie federali statunitensi.

Gli esperti sottolineano che, in questo caso, **applicare la patch non basta**: le chiavi `machineKey` potrebbero essere già state sottratte e utilizzate per attacchi successivi. È quindi fondamentale anche rigenerare queste chiavi, ruotare tutte le credenziali eventualmente compromesse e verificare attentamente la presenza di web shell, script sospetti o movimenti laterali all’interno dell’infrastruttura.

Per aumentare la resilienza, Microsoft consiglia anche l’attivazione dell’**Antimalware Scan Interface (AMSI)** su tutti i server SharePoint, in modo da intercettare i payload malevoli prima che vengano eseguiti. È inoltre consigliabile isolare i server esposti a Internet e sottoporre l’intero ambiente a una revisione di sicurezza.

La campagna **ToolShell** mostra un’elevata sofisticazione e una chiara volontà di persistenza con una particolare attenzione alla compromissione dei sistemi Microsoft su più livelli, inclusi SharePoint, Exchange, OneDrive e Teams. Tra gli IP utilizzati negli attacchi figura anche un indirizzo già coinvolto in precedenti exploit su Ivanti EPMM, a dimostrazione del fatto che si tratta probabilmente di gruppi APT con risorse e competenze elevate.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

[WhoFi: da La Sapienza arriva un sistema di riconoscimento biometrico basato sul Wi-Fi](https://www.securityinfo.it/2025/07/23/whofi-da-la-sapienza-arriva-un-sistema-di-riconoscimento-biometrico-basato-sul-wi-fi/)
[APT41, il gruppo cinese amplia il raggio d'azione in Africa](https://www.securityinfo.it/2025/07/22/apt41-il-gruppo-cinese-amplia-il-raggio-dazione-in-africa/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/wp-content/uploa...