---
title: I criminali sfruttano la vulnerabilità in Samsung MagicINFO 9 Server
url: https://www.securityinfo.it/2025/05/07/i-criminali-sfruttano-la-vulnerabilita-in-samsung-magicinfo-9-server/?utm_source=rss&utm_medium=rss&utm_campaign=i-criminali-sfruttano-la-vulnerabilita-in-samsung-magicinfo-9-server
source: Securityinfo.it
date: 2025-05-08
fetch_date: 2025-10-06T22:30:06.095767
---

# I criminali sfruttano la vulnerabilità in Samsung MagicINFO 9 Server

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## I criminali sfruttano la vulnerabilità in Samsung MagicINFO 9 Server

Mag 07, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/05/07/i-criminali-sfruttano-la-vulnerabilita-in-samsung-magicinfo-9-server/#respond)

---

Samsung MagicINFO è una piattaforma di **gestione centralizzata per contenuti digitali nei monitor Samsung**, ampiamente usati in ambienti come negozi, aeroporti, ospedali e aziende. La versione 9 del server presenta una vulnerabilità critica di tipo Remote Code Execution (RCE), catalogata come CVE-2024-7399.

![](https://www.securityinfo.it/wp-content/uploads/2025/05/AttaccoASamsung7-mag-2025-1024x683.png)

Questa falla **consente a un attaccante non autenticato di caricare file arbitrari sul server**, sfruttando una funzionalità di upload destinata all’aggiornamento dei contenuti dei display. La vulnerabilità è stata corretta da Samsung con il rilascio della versione 21.1050 nel 2024 .

## Upload maligno che porta a controllo completo

Il problema risiede in una limitazione errata del percorso dei file caricati che permette a un attaccante di scrivere con privilegi di sistema file in directory teoricamente precluse. In particolare, **l’attaccante può inviare una richiesta POST non autenticata contenente un file JSP maligno** che viene poi eseguito dal server consentendo l’esecuzione di comandi arbitrari con i privilegi del sistema operativo. Questa tecnica sfrutta la mancanza di controlli adeguati sul percorso dei file e sull’autenticazione degli utenti che effettuano l’upload.

## Attacchi su larga scala

L’exploit di questa vulnerabilità può portare a **compromissioni complete del sistema, inclusa l’installazione di malware**, il furto di dati sensibili e l’interruzione dei servizi di digital signage. Data la natura centralizzata di MagicINFO, **un attacco riuscito può avere un impatto significativo su vasta scala**, soprattutto in ambienti con numerosi display distribuiti. Inoltre, l’accesso non autenticato amplifica il rischio, rendendo possibile l’attacco da parte di qualsiasi attore malintenzionato con accesso alla rete.

## Mitigare si può

Si consiglia vivamente di aggiornare Samsung MagicINFO Server alla versione 21.1050 o successiva che corregge la vulnerabilità CVE-2024-7399. Inoltre, è fondamentale implementare controlli di accesso rigorosi, monitorare le attività sospette e **limitare l’accesso al server solo a indirizzi IP fidati**. L’adozione di pratiche di sicurezza come l’analisi regolare dei log e l’uso di firewall applicativi può ulteriormente ridurre il rischio di exploit.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [controllo remoto](https://www.securityinfo.it/tag/controllo-remoto/), [Monitor](https://www.securityinfo.it/tag/monitor/), [patch](https://www.securityinfo.it/tag/patch/), [Samsung](https://www.securityinfo.it/tag/samsung/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Cybercriminali sfruttano una vulnerabilità di Langflow per prendere il controllo dei server](https://www.securityinfo.it/2025/05/07/cybercriminali-sfruttano-una-vulnerabilita-di-langflow-per-prendere-il-controllo-dei-server/)
[Le difese migliorano, ma i ransomware continuano a colpire le aziende](https://www.securityinfo.it/2025/05/06/le-difese-migliorano-ma-i-ransomware-continuano-a-colpire-le-aziende-il-report-veeam/)

---

![](https://secure.gravatar.com/avatar/93ad3a1bbb47d1f5755e4f5086cb3f22?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di ...