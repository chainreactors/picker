---
title: Gruppo hacker cinese sospettato degli attacchi zero-day a Fortinet
url: https://www.securityinfo.it/2023/03/29/gruppo-hacker-cinese-zero-day-fortinet/?utm_source=rss&utm_medium=rss&utm_campaign=gruppo-hacker-cinese-zero-day-fortinet
source: Securityinfo.it
date: 2023-03-30
fetch_date: 2025-10-04T11:09:21.665192
---

# Gruppo hacker cinese sospettato degli attacchi zero-day a Fortinet

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

## Gruppo hacker cinese sospettato degli attacchi zero-day a Fortinet

Mar 29, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Apt](https://www.securityinfo.it/category/minacce-2/apt/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/03/29/gruppo-hacker-cinese-zero-day-fortinet/#respond)

---

A inizio mese Fortinet [aveva pubblicato un avviso](https://www.fortinet.com/blog/psirt-blogs/fg-ir-22-369-psirt-analysis) riguardante **una vulnerabilità zero-day presente nei device firewall Fortigate** che permette agli attaccanti di leggere e scrivere file tramite linea di comando. La falla era stata scoperta dopo alcuni incidenti di sicurezza notificati da un cliente di Fortinet; l’analisi aveva **individuato un malware in grado di esfiltrare dati dai dispostivi compromessi**. A quasi un mese dalla pubblicazione dell’avviso, [Mandiant ha identificato](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem) un **gruppo di hacker cinese come il possibile artefice degli attacchi.**

Il gruppo in questione si chiama **UNC3886**, e l’azienda di sicurezza sospetta che **sia lo stesso dietro la backdoor VIRTUALPITA** che colpisce l’hypervisor VMware ESXi, scoperta lo scorso settembre. I ricercatori di Mandiant credono che **i device FortiGate e FortiManager compromessi siano stati utilizzati proprio per connettersi alle backdoor VIRTUALPITA.**

![fortinet](https://www.securityinfo.it/wp-content/uploads/2023/03/cyber-security-1923446_1920.png)

Pixabay

Dalla prima analisi di Fortinet era subito emerso che s**i tratta di un malware pensato per il cyberspionaggio**, progettato come minaccia persistente contro istituzioni governative. Nel dettaglio, il malware colpiscea diverse soluzioni Fortinet quali il firewall FortiGate, la soluzione di gestione centralizzata FortiManager e FortiAnalyzer, uno strumento di analytics e reportistica.

Mandiant ha individuato cinque step che caratterizzano l’attacco: per ottenere l’accesso iniziale, il gruppo sfrutta la vulnerabilità dei dispositivi per **scrivere file sui dispositivi FortiGate**; in una seconda fase, **il malware ottiene accesso persistente ai dispositivi** con privilegi di Super Amministratore; in seguito, gli attaccanti **stabiliscono una connessione con le backdoor VIRTUALPITA**; grazie a un endpoint custom, **gli attaccanti ottengono persistenza anche su FortiManager e FortiAnalyzer**; infine, per coprire le proprie tracce, **il gruppo disabilita OpenSSL 1.1.0 per la verifica dell’autenticità dei file di sistema.**

I ricercatori di Mandiant rinnovano l’invito di [Fortinet](https://www.securityinfo.it/2023/02/27/le-appliance-fortinet-sono-sotto-attacco-da-giorni/) ad **aggiornare i dispositivi compromessi per proteggersi dalla minaccia.** Nel dettaglio, le versioni vulnerabili di FortiOS sono quelle dalla 7.2.0 alla 7.2.3, dalla 7.0.0 alla 7.0.9, dalla 6.4.0 alla 6.4.11, e tutte le versioni 6.2.x e 6.0.x.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [cyberspionaggio](https://www.securityinfo.it/tag/cyberspionaggio/), [FortiAnalyzer](https://www.securityinfo.it/tag/fortianalyzer/), [FortiGate](https://www.securityinfo.it/tag/fortigate/), [FortiManager](https://www.securityinfo.it/tag/fortimanager/), [hacker](https://www.securityinfo.it/tag/hacker/), [Mandiant](https://www.securityinfo.it/tag/mandiant/), [UNC3886](https://www.securityinfo.it/tag/unc3886/), [VIRTUALPITA](https://www.securityinfo.it/tag/virtualpita/)

[Dark Power: il nuovo ransomware ha colpito 10 vittime in un mese](https://www.securityinfo.it/2023/03/30/dark-power-nuovo-ransomware/)
[Un bug di Woocommerce mette a rischio mezzo milione di store](https://www.securityinfo.it/2023/03/28/un-bug-di-woocommerce-mette-a-rischio-mezzo-milione-di-store/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-...