---
title: Una nuova vulnerabilità OpenSSH consente l’esecuzione remota di codice
url: https://www.securityinfo.it/2024/07/11/una-nuova-vulnerabilita-openssh-consente-lesecuzione-remota-di-codice/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-12
fetch_date: 2025-10-06T17:46:06.647839
---

# Una nuova vulnerabilità OpenSSH consente l’esecuzione remota di codice

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

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

## Una nuova vulnerabilità OpenSSH consente l’esecuzione remota di codice

Lug 11, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/07/11/una-nuova-vulnerabilita-openssh-consente-lesecuzione-remota-di-codice/#respond)

---

Dopo RegreSSHion, **un’altra vulnerabilità colpisce OpenSSH**: tracciato come CVE-2024-6409, il bug permette di **eseguire codice da remoto a causa di una race condition.**

La vulnerabilità è presente nel processo figlio di privsep e in particolare nelle operazioni di signal handling. A scoprire il bug è stato il ricercatore di sicurezza **Alexander** **Peslyak**, il quale ha spiegato che, a differenza di [regreSSHion](https://www.securityinfo.it/2024/07/03/qualys-scopre-regresshion-un-bug-che-minaccia-milioni-di-server-openssh/), il processo viene eseguito con privilegi ridotti e **quindi l’impatto immediato è inferiore**.

![vulnerabilità OpenSSH](https://www.securityinfo.it/wp-content/uploads/2024/07/hacking-4038037_1920.jpg)

Pixabay

In ogni caso, se si utilizza una versione di OpenSSH non patchata, un **attaccante può sfruttare a suo piacimento una delle due vulnerabilità** per compromettere l’intero sistema e prenderne il controllo, installando malware od ottenendo dati sensibili. “*Potrebbe anche essere possibile creare un exploit che funzioni contro una delle due vulnerabilità in modo probabilistico, **il che potrebbe ridurre la durata dell’attacco o aumentare la percentuale di successo***” [aggiunge](https://www.openwall.com/lists/oss-security/2024/07/08/2) il ricercatore.

Mentre regreSSHion è stata già sfruttata dagli attaccanti, al momento i ricercatori non sono a conoscenza di tentativi di sfruttamento di questa nuova vulnerabilità.

Peslyak ha contattato i ricercatori di Qualys per comunicargli la scoperta e il team ha confermato l’esistenza e la natura della vulnerabilità.

Le versioni vulnerabili sono la 8.7 e la 8.8. Poiché la race condition alla base dei bug è la stessa, è consigliabile **installare il prima possibile le patch disponibili.** Rimangono valide anche le indicazioni sulla segmentazione di rete e sull’implementazione di soluzioni per il monitoraggio di attività sospette.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [esecuzione codice in remoto](https://www.securityinfo.it/tag/esecuzione-codice-in-remoto/), [OpenSSH](https://www.securityinfo.it/tag/openssh/), [Qualys](https://www.securityinfo.it/tag/qualys/), [race condition](https://www.securityinfo.it/tag/race-condition/), [regreSSHion](https://www.securityinfo.it/tag/regresshion/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[L'adozione del cloud aumenta, ma anche le sfide di sicurezza](https://www.securityinfo.it/2024/07/11/ladozione-del-cloud-aumenta-ma-anche-le-sfide-di-sicurezza/)
[CloudSorcerer, un nuovo gruppo APT che colpisce le agenzie governative russe](https://www.securityinfo.it/2024/07/10/cloudsorcerer-un-nuovo-gruppo-apt-che-colpisce-le-agenzie-governative-russe/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Permanent link to Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  Set 08, 2025  [0](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4han...