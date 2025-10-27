---
title: VMware, trovate vulnerabilità che consentono di eseguire codice sull’host
url: https://www.securityinfo.it/2024/03/08/vmware-trovate-vulnerabilita-che-consentono-di-eseguire-codice-sullhost/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-09
fetch_date: 2025-10-04T12:12:22.003708
---

# VMware, trovate vulnerabilità che consentono di eseguire codice sull’host

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

## VMware, trovate vulnerabilità che consentono di eseguire codice sull’host

Mar 08, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/03/08/vmware-trovate-vulnerabilita-che-consentono-di-eseguire-codice-sullhost/#respond)

---

VMware ha pubblicato un [avviso di sicurezza](https://www.vmware.com/security/advisories/VMSA-2024-0006.html) dove avverte i suoi utenti di **quattro nuove vulnerabilità** che colpiscono ESXi. Workstation Pro/Player (Workstation), Fusion Pro/Fusion (Fusion)  e Cloud Foundation,  due delle quali con **punteggio di criticità di 9.3 su 10.**

I due bug a rischio critico sono entrambi delle vulnerabilità **use-after-free**. Tracciate come CVE-2024-22252 e CVE-2024-22253, entrambe sono presenti in ESXi, WorkStation e Fusion e **colpiscono una il controller XHCI USB e l’altra il controller UHCI USB.**

I bug consentono  a un attaccante con privilegi locali di amministratore su una macchina virtuale di **eseguire codice arbitrario**. Su ESXi le conseguenze degli attacchi sono limitate alla sandbox VMX, mentre su Workstation e Fusion l’esecuzione di codice può avvenire direttamente sulla macchina dove sono installati.

![bug](https://www.securityinfo.it/wp-content/uploads/2024/03/laptop-4152330_1920.jpg)

Pixabay

Una terza vulnerabilità, la CVE-2024-22254, è un bug di **out-of-bound write** che colpisce ESXi e consente a un attaccante con privilegi sul processo VMX di scrivere al di fuori dell’area di memoria e uscire dalla sandbox; ciò consentirebbe di **accedere al dispositivo host ed eseguire comandi arbitrari.**

La quarta vulnerabilità, la CVE-2024-22255, è un bug di **information disclosure** presente nell’UHCI USB controller in ESXi, Workstation e Fusion. La vulnerabilità consente a un attaccante con accesso di amministratore a una macchina virtuale di **causare un leak di memoria dal processo VMX.**

La compagnia ha rilasciato le patch per tutte e quattro le vulnerabilità. A parte per la prima vulnerabilità, [VMware](https://www.securityinfo.it/2024/02/21/disinstallate-subito-eap-di-vmware-il-plugin-soffre-di-un-bug-critico/) ha specificato ch**e non esistono workaround da applicare**; per questo ha invitato i suoi utenti ad **aggiornare il prima possibile i prodotti** alle versioni che risolvono  bug.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

[CERT-AGID 02 – 08 Marzo 2024: un'impennata di minacce porta a 234 indicatori di compromissione](https://www.securityinfo.it/2024/03/11/cert-agid-02-08-marzo-2024-impennata-minacce-234-indicatori-compromissione/)
[Siti fake di Skype, Google Meet e Zoom usati per distribuire trojan](https://www.securityinfo.it/2024/03/07/siti-fake-di-skype-google-meet-e-zoom-usati-per-distribuire-trojan/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/wp-content/uploads/2019/01/Morten-Lehn-120x85.jpg)](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  [Transparency Center Initiative di...](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Permanent link to Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  Gen 18, 2019  [0](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/#respond)
* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/wp-content/uploads/2025/10/Home-Odyssey-Cybersecurity-10-03-2025_04_08_PM-120x85.png)](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/ "Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia")

  [Clearskies: la suite di sicurezza...](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/ "Permanent link to Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/#respond)
* [![Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_eubydneubydneuby-120x85.png)](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità")

  [Ricerca Fir...