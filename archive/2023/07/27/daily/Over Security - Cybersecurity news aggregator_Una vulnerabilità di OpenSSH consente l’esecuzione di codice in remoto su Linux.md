---
title: Una vulnerabilità di OpenSSH consente l’esecuzione di codice in remoto su Linux
url: https://www.securityinfo.it/2023/07/26/una-vulnerabilita-di-openssh-consente-lesecuzione-di-codice-in-remoto-su-linux/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-27
fetch_date: 2025-10-04T11:56:24.556381
---

# Una vulnerabilità di OpenSSH consente l’esecuzione di codice in remoto su Linux

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## Una vulnerabilità di OpenSSH consente l’esecuzione di codice in remoto su Linux

Lug 26, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/07/26/una-vulnerabilita-di-openssh-consente-lesecuzione-di-codice-in-remoto-su-linux/#respond)

---

[I ricercatori di Qualys](https://blog.qualys.com/vulnerabilities-threat-research/2023/07/19/cve-2023-38408-remote-code-execution-in-opensshs-forwarded-ssh-agent) hanno individuato una **vulnerabilità in OpenSSH che consente a un attaccante di eseguire codice in remoto nei dispositivi compromessi.**

La vulnerabilità, identificata come [CVE-2023-38408](https://nvd.nist.gov/vuln/detail/CVE-2023-38408), **colpisce l’ssh-agent di OpenSSH** nelle versioni precedenti alla 9.3p2. I ricercatori di Qualys sono riusciti a identificare il bug e **sviluppare una PoC per Ubuntu Desktop nelle versioni 22.04 e 21.10**, anche se, spiega il team, è molto probabile che anche altre distribuzioni [Linux](https://www.securityinfo.it/2023/07/19/kaspersky-estende-la-sicurezza-ai-dispositivi-embedded-linux-based/) siano vulnerabili.

**OpenSSH è un set di tool open-source per creare connessioni cifrate tra dispositivi.** Il set di tool è ampiamente utilizzato su diversi sistemi operativi per consentire agli utenti di creare connessioni remote sicure verso altri computer o server.

![OpenSSH](https://www.securityinfo.it/wp-content/uploads/2023/07/hacking-g8d5d3553d_1920.jpg)

Pixabay

OpenSSH fa uso dell’ssh-agent, un programma utilizzato autenticarsi su un server remoto appoggiandosi alla connessione SSH precedentemente creata. Generalmente, spiegano i ricercatori, un amministratore di sistema esegue l’ssh-agent sul proprio dispositivo, si connette a un server remoto con ssh e **abilita la funzionalità di forwarding dell’ssh-agent per autenticarsi sul server.**

L’ssh-agent diventa così raggiungibile anche dal server remoto. Analizzando il codice sorgente del programma, il team di Qualys ha notato una **vulnerabilità che consente a un attaccante con accesso al server remoto di accedere alle librerie del dispositivo** dell’amministratore ed eseguire codice.

**OpenBSD**, il team che ha sviluppato il set di tool, è statao informato immediatamente del bug e **ha rilasciato una [patch risolutiva](https://www.openssh.com/releasenotes.html)** lo scorso 19 luglio. Qualys consiglia di **aggiornare il prima possibile il tool alla versione 9.3p2.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [autenticazione](https://www.securityinfo.it/tag/autenticazione/), [OpenSSH](https://www.securityinfo.it/tag/openssh/), [Qualys](https://www.securityinfo.it/tag/qualys/), [remote code execution](https://www.securityinfo.it/tag/remote-code-execution/), [SSH](https://www.securityinfo.it/tag/ssh/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Crescono gli attacchi tramite cloud al settore industriale](https://www.securityinfo.it/2023/07/27/crescono-gli-attacchi-tramite-cloud-al-settore-industriale/)
[Le violazioni di dati sono in aumento: la soluzione è l'IA](https://www.securityinfo.it/2023/07/26/violazioni-dati-ia-automazione/)

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

  Set 08, 2025  [0](https://www....