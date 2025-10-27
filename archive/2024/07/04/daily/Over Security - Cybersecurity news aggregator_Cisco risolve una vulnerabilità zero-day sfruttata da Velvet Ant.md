---
title: Cisco risolve una vulnerabilità zero-day sfruttata da Velvet Ant
url: https://www.securityinfo.it/2024/07/03/cisco-risolve-una-vulnerabilita-zero-day-sfruttata-da-velvet-ant/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-04
fetch_date: 2025-10-06T17:45:37.954823
---

# Cisco risolve una vulnerabilità zero-day sfruttata da Velvet Ant

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

## Cisco risolve una vulnerabilità zero-day sfruttata da Velvet Ant

Lug 03, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/07/03/cisco-risolve-una-vulnerabilita-zero-day-sfruttata-da-velvet-ant/#respond)

---

**Cisco** [ha risolto](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nxos-cmd-injection-xD9OhyOP) una **[vulnerabilità](https://www.securityinfo.it/2024/01/30/una-vulnerabilita-critica-di-cisco-consente-lesecuzione-remota-di-codice/) di command injection** presente nella **CLI di NX-OS**, il sistema operativo della compagnia usato negli switch di rete della serie Nexus.

Tracciata come CVE-2024-20399, la vulnerabilità, causata da una validazione insufficiente degli argomenti passati ai comandi CLI, permette a un attaccante di **eseguire comandi arbitrati sul sistema operativo con i privilegi di root.**

A identificare per primi la vulnerabilità sono stati i ricercatori di **[Syginia](https://www.sygnia.co/threat-reports-and-advisories/china-nexus-threat-group-velvet-ant-exploits-cisco-0-day/)**, i quali hanno anche scoperto che **il bug era un zero-day che veniva sfruttato con successo da Velvet Ant**, un gruppo di attaccanti cinese. L’exploit ha portato all’esecuzione di malware finora sconosciuta che ha permesso alla gang di connettersi ai dispositivi Nexus, caricare altri payload ed eseguire codice.

![Cisco vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2024/07/hacker-3480124_1920.jpg)

Pixabay

Il bug è ritenuto di criticità media in quanto, come specifica Cisco, per essere sfruttato **un attaccante deve avere le credenziali di amministratore**; inoltre, secondo l’analisi di Syginia, la maggior parte dei Nexus Cisco non sono esposti direttamente a internet, quindi i**l rischio per le organizzazioni è considerato relativamente basso.**

“*Nonostante i notevoli prerequisiti per lo sfruttamento della vulnerabilità in questione, questo incidente dimostra la tendenza di gruppi di minacce sofisticate a sfruttare le appliance di rete – che spesso non sono sufficientemente protette e monitorate – per mantenere un accesso persistente; **l’incidente sottolinea anche l’importanza critica di aderire alle best practice di sicurezza come mitigazione contro questo tipo di minaccia***” evidenziano i ricercatori di Syginia, invitando le imprese a non abbassare la guardia.

Il bug colpisce la serie MDS 900 degli switch Multilayer, gli switch della serie Nexus 3000, della Nexus 6000, della Nexus 7000 e della 9000 in modalità NX-OS standalone, oltre alle piattaforme Nexus 5500 e Nexus 5600. Cisco ha rilasciato i fix per la vulnerabilità e chiede ai suoi utenti di **aggiornare il prima possibile i prodotti vulnerabili.**È inoltre consigliato aggiornare di frequente le credenziali degli utenti amministratori.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Cisco](https://www.securityinfo.it/tag/cisco/), [Cisco Nexus](https://www.securityinfo.it/tag/cisco-nexus/), [CLI](https://www.securityinfo.it/tag/cli/), [command injection](https://www.securityinfo.it/tag/command-injection/), [NX-OS](https://www.securityinfo.it/tag/nx-os/), [Syginia](https://www.securityinfo.it/tag/syginia/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[Le vulnerabilità di CocoaPods mettono in pericolo migliaia di device Apple](https://www.securityinfo.it/2024/07/04/le-vulnerabilita-di-cocoapods-mettono-in-pericolo-migliaia-di-device-apple/)
[Qualys scopre regreSSHion, un bug che minaccia milioni di server OpenSSH](https://www.securityinfo.it/2024/07/03/qualys-scopre-regresshion-un-bug-che-minaccia-milioni-di-server-openssh/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttat...