---
title: Le vulnerabilità dei dispositivi Moxa mettono a rischio le reti industriali
url: https://www.securityinfo.it/2025/01/07/le-vulnerabilita-dei-dispositivi-moxa-mettono-a-rischio-le-reti-industriali/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-08
fetch_date: 2025-10-06T20:13:31.342613
---

# Le vulnerabilità dei dispositivi Moxa mettono a rischio le reti industriali

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

## Le vulnerabilità dei dispositivi Moxa mettono a rischio le reti industriali

Gen 07, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/01/07/le-vulnerabilita-dei-dispositivi-moxa-mettono-a-rischio-le-reti-industriali/#respond)

---

Lo scorso venerdì **Moxa**, provider di reti industriali, ha pubblicato un advisory di sicurezza dove descrive **due vulnerabilità critiche** che colpiscono diversi modelli dei propri router e di device di sicurezza.

“*I router cellulari, i firewall e le appliance di sicurezza di rete di Moxa sono affetti da due **vulnerabilità critiche che rappresentano un rischio significativo per la sicurezza***” si legge nel [post](https://www.moxa.com/en/support/product-support/security-advisory/mpsa-241155-privilege-escalation-and-os-command-injection-vulnerabilities-in-cellular-routers%2C-secure-routers%2C-and-netwo).

![vulnerabilità Moxa](https://www.securityinfo.it/wp-content/uploads/2025/01/pattern-3232784_1920.jpg)

Uno dei due bug, tracciato come CVE-2024-9138, è causato da **credenziali hard-coded c**he consentono a un utente autenticato di effettuare l’escalation dei privilegi per **ottenere permessi di root sul sistema.** Un attaccante sarebbe quindi in grado di compromettere il funzionamento del sistema, ottenere dati sensibili e interrompere l’erogazione del servizio.

La seconda vulnerabilità, la CVE-2024-9140, è un bug di **OS Command Injection** che consente a un attaccante di usare caratteri speciali in un comando per superare le restrizioni di input ed eseguire codice da remoto.

I dispositivi serie EDR-810 (con versione del firmware 5.12.37 e precedenti) e della EDR-G902 (con versione del firmware 5.7.25 e precedenti) sono vulnerabili al primo bug, mentre i device della serie EDR-8010, EDR-G9004 (versioni 3.13.1 e precedenti), EDR-G9010 (versioni 3.13.1 e precedenti), EDF-G1002-BP (versioni 3.13.1 e precedenti), NAT-102 (versioni 1.0.5 e precedenti), OnCell G4302-LTE4 (versioni 3.13 e precedenti) e TN-4900 (versioni 3.13 e precedenti) sono vulnerabili a entrambi i bug.

**Moxa ha rilasciato le patch per le vulnerabilità per la maggior parte dei dispositivi elencati.** Per i dispositivi OnCell G4302-LTE4 e TN-4900, è necessario contattare il supporto tecnico della compagnia per applicare la patch di sicurezza.

**Per i NAT-102 non c’è invece ancora una patch**; in questo caso Moxa consiglia di non esporre i device a internet se non strettamente necessario, di limitare l’accesso SSH ai soli indirizzi IP e alle reti attendibili e di implementare IDS o IPS per individuare e bloccare eventuali tentativi di sfruttamento.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [credenziali hard-coded](https://www.securityinfo.it/tag/credenziali-hard-coded/), [esecuzione di codice da remoto](https://www.securityinfo.it/tag/esecuzione-di-codice-da-remoto/), [Moxa](https://www.securityinfo.it/tag/moxa/), [OS Command Injection](https://www.securityinfo.it/tag/os-command-injection/), [reti industriali](https://www.securityinfo.it/tag/reti-industriali/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Gli Stati Uniti cambiano opinione sulla crittografia e sulle backdoor](https://www.securityinfo.it/2025/01/08/gli-stati-uniti-cambiano-opinione-sulla-crittografia-e-sulle-backdoor/)
[CERT-AGID 28 dicembre – 3 gennaio: Poste Italiane e Intesa Sanpaolo sotto attacco](https://www.securityinfo.it/2025/01/06/cert-agid-28-dicembre-3-gennaio-poste-italiane-e-intesa-sanpaolo-sotto-attacco/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/20...