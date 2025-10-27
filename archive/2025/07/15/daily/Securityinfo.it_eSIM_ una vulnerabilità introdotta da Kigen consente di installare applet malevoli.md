---
title: eSIM: una vulnerabilità introdotta da Kigen consente di installare applet malevoli
url: https://www.securityinfo.it/2025/07/14/esim-una-vulnerabilita-introdotta-da-kigen-consente-di-installare-applet-malevoli/?utm_source=rss&utm_medium=rss&utm_campaign=esim-una-vulnerabilita-introdotta-da-kigen-consente-di-installare-applet-malevoli
source: Securityinfo.it
date: 2025-07-15
fetch_date: 2025-10-06T23:50:06.726804
---

# eSIM: una vulnerabilità introdotta da Kigen consente di installare applet malevoli

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

## eSIM: una vulnerabilità introdotta da Kigen consente di installare applet malevoli

Lug 14, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/07/14/esim-una-vulnerabilita-introdotta-da-kigen-consente-di-installare-applet-malevoli/#respond)

---

I ricercatori di AG Security Research [hanno individuato](https://security-explorations.com/esim-security.html) una **vulnerabilità negli eUICC di Kigen,** chip che abilitano le funzionalità delle eSIM, che consente a un attaccante di **installare applet malevoli** sui dispositivi.

Nel dettaglio, il problema risiede nella tecnologia Java Card usata da Kigen negli eUICC ed è causato da **condizioni di “type confusion” già segnalate dalla compagnia di sicurezza nel 2019.** Oracle, gestore delle specifiche tecniche delle Java Card, aveva ritenuto che non ci fosse in realtà alcun problema di sicurezza, dal momento che il bug era “non applicabile”. Ora che i ricercatori hanno dimostrato la fattibilità dell’attacco, le aziende e associazioni coinvolte sono corse ai ripari. Probabilmente, come spesso accade, un po’ in ritardo.

![eSIM Kigen](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_oxfnwyoxfnwyoxfn.png)

Il problema coinvolge Kigen in quanto la compagnia si occupa dell’implementazione specifica della Java Card, implementazione che si è rivelata vulnerabile proprio perché **introduce condizioni di type confusion rischiose.**

Utilizzando la vulnerabilità, gli attaccanti possono utilizzare profili di test delle [eSIM](https://www.securityinfo.it/2024/03/18/esim-hijacking-numero-telefono/), come il **GSMA TS.48 Generic Test Profile**, un profilo di test utilizzato per effettuare verifiche di compliance, a loro piacimento. Sfruttando il bug, i cybercriminali sono in grado di installare applet non verificati, potenzialmente malevoli, di clonare le eSIM e di intercettare le comunicazioni.

Tutto ciò ha un impatto notevole sui consumatori: clonando una eSIM su un altro eUICC, gli attaccanti possono prendere il controllo delle identità degli utenti e accedere anche a quei servizi che usano l’autenticazione a due fattori tramite SMS o le password monouso. La situazione è complessa anche perché **gli operatori di rete mobile non sono in grado di rilevare se un profilo eSIM sia stato compromesso** e copiato su un eUICC differente.

In un advisory di sicurezza pubblicato il 9 luglio, Kigen [ha annunciato](https://kigen.com/company/policies/security-center/security-bulletin-kgnsb-07-2025/) ai propri utenti di aver rilasciato una **patch risolutiva**, introducendo un fix per il sistema operativo; al contempo, la GSMA ha applicato alcune restrizioni ai profili di test.

AG Security Research ha specificato di non essere d’accordo con l’intervento di Kigen, affermando che non è risolutivo. Secondo i ricercatori, la compagnia sussidiaria di ARM **ha minimizzato l’accaduto** evidenziando che le problematiche erano presenti nel profilo TS.48 Generic Test Profile, mentre **la falla indicata da AG Security Research ha una natura ben più profonda e sistemica.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AG Security Research](https://www.securityinfo.it/tag/ag-security-research/), [eSIM](https://www.securityinfo.it/tag/esim/), [eUICC](https://www.securityinfo.it/tag/euicc/), [Java Card](https://www.securityinfo.it/tag/java-card/), [Kigen](https://www.securityinfo.it/tag/kigen/), [Oracle](https://www.securityinfo.it/tag/oracle/), [Type Confusion](https://www.securityinfo.it/tag/type-confusion/)

[GPUHammer: le GPU NVIDIA sono vulnerabili a un exploit di Rowhammer](https://www.securityinfo.it/2025/07/15/gpuhammer-le-gpu-nvidia-sono-vulnerabili-a-un-exploit-di-rowhammer/)
[CERT-AGID 5 – 11 luglio: sei nuove campagne di phishing contro utenti SPID](https://www.securityinfo.it/2025/07/14/cert-agid-5-11-luglio-sei-campagne-phishing-utenti-spid/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Leak Oracle Cloud: numerose compagnie confermano il furto di dati](https://www.securityinfo.it/wp-content/uploads/2025/03/126628-120x85.jpg)](https://www.securityinfo.it/2025/03/27/leak-oracle-cloud-numerose-compagnie-confermano-il-furto-di-dati/ "Leak Oracle Cloud: numerose compagnie confermano il furto di dati")

  [Leak Oracle Cloud: numerose compagnie...](https://www.securityinfo.it/2025/03/27/leak-oracle-cloud-numerose-compagnie-confermano-il-furto-di-dati/ "Permanent link to Leak Oracle Cloud: numerose compagnie confermano il furto di dati")

  Mar 27, 2025  [0](https://www.securityinfo.it/2025/03/27/leak-oracle-cloud-numerose-compagnie-confermano-il-furto-di-dati/#respond)
* [![Due vulnerabilità Oracle WebLogic sono sfruttate attivamente](https://www.securityinfo.it/wp-content/uploads/2024/06/technology-6891310_1920-120x85.jpg)](https://www.securityinfo.it/2024/06/04/due-vulnerabilita-oracle-weblogic-sono-sfruttate-attivamente/ "Due vulnerabilità Oracle WebLogic sono sfruttate attivamente")

  [Due vulnerabilità Oracle WebLogic sono...](https://www.securityinfo.it/2024/06/04/due-vulnerabilita-oracle-weblogic-sono-sfruttate-attivamente/ "Permanent link to Due vulnerabilità Oracle WebLogic sono sfruttate attivamente")

  Giu 04, 2024  [0](https://www.securityinfo.it/2024/06/04/due-vulnerabilita-oracle-weblogic-sono-sfruttate-at...