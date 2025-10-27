---
title: Più di 330.000 firewall FortiGate sono ancora vulnerabili a un bug già risolto
url: https://www.securityinfo.it/2023/07/11/300000-firewall-fortigate-vulnerabili-bug-risolto/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-12
fetch_date: 2025-10-04T11:58:06.962670
---

# Più di 330.000 firewall FortiGate sono ancora vulnerabili a un bug già risolto

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

## Più di 330.000 firewall FortiGate sono ancora vulnerabili a un bug già risolto

Lug 11, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/07/11/300000-firewall-fortigate-vulnerabili-bug-risolto/#respond)

---

**Più di 330.000 firewall FortiGate sono ancora vulnerabili al bug** [**CVE-2023-27997**](https://nvd.nist.gov/vuln/detail/CVE-2023-27997). [BishopFox](https://bishopfox.com/blog/cve-2023-27997-exploitable-and-fortigate-firewalls-vulnerable), compagnia di consulenza in ambito di cybersecurity, ha sviluppato un prototipo di attacco che sfrutta la vulnerabilità, confermando che esiste ancora un gran numero di firewall non aggiornati.

La vunerabilità, un **heap-based buffer overflow**, permette a un attaccante di eseguire codice e comandi da remoto sul dispositivo target utilizzando delle richieste create ad hoc.

Il bug è stato reso noto lo scorso 6 giugno e **FortiNet ha rilasciato le [patch di sicurezza](https://www.securityinfo.it/2023/06/12/fortinet-rilascia-un-fix-per-una-nuova-vulnerabilita-dei-dispositivi-fortigate/)** qualche giorno dopo.

Tramite Shodan, i ricercatori di BishopFox hanno individuato circa **490.000 interfacce SSL VPN con versioni colpite dal bug**, e di queste soltanto 153.414 erano patchate; ciò significa, spiega il team di sicurezza, che **il 69% di esse è ancora vulnerabile**.

![FortiGate](https://www.securityinfo.it/wp-content/uploads/2023/07/safety-g198f7f969_1920.jpg)

Credits: PIxabay

I ricercatori hanno sottolineato l’importanza di **aggiornare i firewall vulnerabili** dal momento che il bug è critico ed è già stato utilizzato in alcuni attacchi. [Fortinet](https://www.fortinet.com/blog/psirt-blogs/analysis-of-cve-2023-27997-and-clarifications-on-volt-typhoon-campaign), in occasione del rilascio delle patch risolutive, ha spiegato che il numero di attacchi che hanno sfruttato il bug è limitato, anche se non ha specificato il numero esatto.

Le versioni colpite sono la 7.2.4 e minori, 7.0.11 e minori, 6.4.12 e minori, 6.0.16 e minori di **FortiOS**; inoltre, risultano vulnerabili le versioni 7.2.3 e minori, 7.0.9 e minori, 2.0.12 e minori e tutte le versioni 1.2  e 1.1 di **FortiProxy**.

**Fortinet** ha commentato così la notizia: “Il 12 giugno abbiamo pubblicato un **avviso PSIRT ([FG-IR-23-097](https://www.fortiguard.com/psirt/FG-IR-23-097)) che illustra in dettaglio i prossimi passi da compiere in relazione a [CVE-2023-27997](https://nvd.nist.gov/vuln/detail/CVE-2023-27997).** Fortinet continua a monitorare la situazione e ha comunicato in modo proattivo ai clienti, invitandoli a seguire immediatamente le indicazioni fornite per mitigare la vulnerabilità utilizzando i workaround forniti o aggiornando. A seguito di ciò, **abbiamo condiviso ulteriori dettagli e chiarimenti per aiutare i nostri clienti a prendere decisioni informate** e basate sul rischio in merito a CVE-2022-27997 in questo [blog](https://www.fortinet.com/blog/psirt-blogs/analysis-of-cve-2023-27997-and-clarifications-on-volt-typhoon-campaign). Per ulteriori informazioni, consultare il blog e l’[advisory](https://www.fortiguard.com/psirt/FG-IR-23-097)“.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [firewall](https://www.securityinfo.it/tag/firewall/), [FortiGate](https://www.securityinfo.it/tag/fortigate/), [fortinet](https://www.securityinfo.it/tag/fortinet/), [Fortios](https://www.securityinfo.it/tag/fortios/), [ssl vpn](https://www.securityinfo.it/tag/ssl-vpn/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Big Head, un nuovo ransomware che si finge un aggiornamento Windows](https://www.securityinfo.it/2023/07/11/big-head-un-nuovo-ransomware-che-si-finge-un-aggiornamento-windows/)
[Attacco a Revolut: rubati 20 milioni di dollari](https://www.securityinfo.it/2023/07/10/attacco-a-revolut-rubati-20-milioni-di-dollari/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_eubydneubydneuby-120x85.png)](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità")

  [Ricerca FireMon: il 60% dei firewall...](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Permanent link to Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità")

  Ott 01, 2025  [0](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/#respond)
* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i ...