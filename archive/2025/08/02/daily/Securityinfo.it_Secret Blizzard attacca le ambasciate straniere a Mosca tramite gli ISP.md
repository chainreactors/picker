---
title: Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP
url: https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/?utm_source=rss&utm_medium=rss&utm_campaign=secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp
source: Securityinfo.it
date: 2025-08-02
fetch_date: 2025-10-07T00:52:00.364236
---

# Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP

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

## Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP

Ago 01, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/#respond)

---

**Secret Blizzard**, gruppo cybercriminale legato ai servizi federali dello stato russo, ha preso di mira le ambasciate straniere a Mosca tramite un attacco **Attacker-in-the-Middle a livello di ISP**, con l’obiettivo di distribuire il malware **ApolloShadow**.

“*Sebbene in precedenza avessimo affermato con poca sicurezza che l’attore conducesse attività di spionaggio informatico all’interno dei confini russi contro entità straniere e nazionali, questa è la prima volta che possiamo confermare che esso ha la capacità di farlo a livello di Internet Service Provider (ISP)*” ha affermato il team di Microsoft Threat Intelligence in un [approfondimento](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/) sulla campagna. “*Questo significa che **il personale diplomatico che usa ISP locali o servizi di telecomunicazioni in Russia molto probabilmente è un obiettivo di Secret Blizzard***“.

![Secret Blizzard](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74.png)

Il team ha scoperto la campagna lo scorso febbraio, ma gli attacchi erano cominciati già nel 2024. Per l’accesso iniziale, i cybercriminali hanno usato dei **portali “captive”**, ovvero pagine web create per gestire l’accesso alla rete degli utenti. Quando la vittima naviga sull’indirizzo del portale, gli viene mostrato un errore di certificato e gli viene richiesto di scaricare un software – il malware ApolloShadow.

Una volta installato, ApolloShadow verifica se il dispositivo viene usato in modalità amministratore; in caso negativo, richiede all’utente di installare il certificato ***CertificateDB.exe*che mima un installer Kaspersky** per installare un certificato root e ottenere privilegi elevati sul sistema. A questo punto il gruppo ha pieno accesso al dispositivo e alle informazioni che contiene.

Microsoft sottolinea che le attività di Secret Blizzard di Attacker-in-the-Middle sono facilitate dal fatto che il governo le ritiene legali per proteggere la sicurezza nazionale.

La compagnia consiglia ai propri clienti, e in particolare agli enti critici che operano a Mosca, di effettuare il routing del traffico a una rete sicura tramite un tunnel cifrato o affidarsi a fornitori di VPN. Microsoft inoltre esorta le organizzazioni ad applicare il principio del privilegio minimo, a usare la MFA e a effettuare l’audit delle attività degli account con privilegi elevati.

**Aggiornamento –** Kaspersky ha rilasciato una nota, che riportiamo qui di seguito, a seguito dell’nvolontario coinvolgimento in questa vicenda:

*“I brand più noti vengono spesso sfruttati come esche, senza che ne siano a conoscenza o abbiano dato il loro consenso. Raccomandiamo sempre di scaricare le applicazioni solo da fonti ufficiali e di verificare attentamente l’autenticità di qualsiasi comunicazione che dichiari di provenire da aziende affidabili.*

*Kaspersky si impegna a proteggere tutti gli utenti da qualsiasi tipo di minaccia, indipendentemente dalla sua origine. I nostri clienti sono già protetti dalla minaccia descritta in questa ricerca.*

*Apprezziamo il riconoscimento da parte di Microsoft della nostra precedente analisi sugli attacchi mirati condotti tramite ISP e auspichiamo una collaborazione continua all’interno della comunità della sicurezza informatica”.*

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AitM](https://www.securityinfo.it/tag/aitm/), [ApolloShadow](https://www.securityinfo.it/tag/apolloshadow/), [hacker russi](https://www.securityinfo.it/tag/hacker-russi/), [ISP](https://www.securityinfo.it/tag/isp/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Secret Blizzard](https://www.securityinfo.it/tag/secret-blizzard/)

[CERT-AGID 26 luglio – 1 agosto: SharePoint, MintLoader e 4L4MD4R protagonisti](https://www.securityinfo.it/2025/08/04/cert-agid-26-luglio-1-agosto-sharepoint-mintloader-e-4l4md4r-protagonisti/)
[Criminali abusano dei servizi di link wrapping per aggirare i controlli](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-120x85.png)](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Grave alerta SharePoint: attacco in corso che elude le difese")

  [Grave alerta SharePoint: attacco in...](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Permanent link to Grave alerta SharePoint: attacco in corso che elude le difese")

  Lug 21, 2025  [0](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/#respond)
* [![Windows 10: ancora un anno di aggiornamenti (quasi) gratis](https://www.securityinfo.it/wp-content/uploads/2025/06/Windows_10_version_22H2_Update_sc...