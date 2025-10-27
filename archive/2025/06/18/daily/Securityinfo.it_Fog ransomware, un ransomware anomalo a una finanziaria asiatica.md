---
title: Fog ransomware, un ransomware anomalo a una finanziaria asiatica
url: https://www.securityinfo.it/2025/06/17/fog-ransomware-un-ransomware-anomalo-a-una-finanziaria-asiatica/?utm_source=rss&utm_medium=rss&utm_campaign=fog-ransomware-un-ransomware-anomalo-a-una-finanziaria-asiatica
source: Securityinfo.it
date: 2025-06-18
fetch_date: 2025-10-06T22:55:37.184323
---

# Fog ransomware, un ransomware anomalo a una finanziaria asiatica

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

## Fog ransomware, un ransomware anomalo a una finanziaria asiatica

Giu 17, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/06/17/fog-ransomware-un-ransomware-anomalo-a-una-finanziaria-asiatica/#respond)

---

Un attacco ransomware avvenuto nel maggio 2025 ai danni di una società finanziaria asiatica ha destato l’attenzione dei ricercatori di Symantec per l’utilizzo di strumenti poco convenzionali. **I criminali informatici hanno impiegato tool più tipici di scenari di penetration testing e spionaggio informatico** che di attacchi estorsivi tradizionali. **L’attacco è stato attribuito al gruppo responsabile di Fog ransomware**, una minaccia attiva da almeno un anno e già nota per i suoi comportamenti fuori dagli schemi.

![](https://www.securityinfo.it/wp-content/uploads/2025/06/Ransomware16-giu-2025CG-1024x683.png)

Nel corso dell’intrusione, durata circa due settimane prima della cifratura dei dati, gli attaccanti hanno utilizzato strumenti come **Syteca, software di monitoraggio poco noto, e GC2** che sfrutta Google Sheets e SharePoint per il command and control. **Tra le utility impiegate anche Adaptix C2, Stowaway e strumenti classici come PsExec e SMBExec** per il movimento laterale all’interno della rete. Al termine di ogni fase, gli operatori hanno eliminato le tracce delle proprie attività, segno di un’operazione ben pianificata e volta alla furtività.

**La vera anomalia, secondo Symantec, è stata la creazione di un servizio permanente dopo l’attacco ransomware**, allo scopo di mantenere l’accesso alla rete compromessa. **Una scelta rara per campagne a scopo puramente estorsivo** che lascia intravedere finalità ulteriori rispetto al semplice guadagno economico.

Fog ransomware è stato individuato per la prima volta nel maggio 2024, in attacchi rivolti soprattutto a istituti scolastici statunitensi. **Inizialmente si diffondeva tramite VPN compromesse**, ma nella seconda metà del 2024 ha iniziato a sfruttare una vulnerabilità critica in Veeam Backup & Replication (CVE-2024-40711, CVSS 9.8). **Da aprile 2025 il gruppo ha cambiato approccio, adottando messaggi email come vettore iniziale** e introducendo tattiche provocatorie come note di riscatto con riferimenti satirici all’agenzia DOGE di Elon Musk.

Nell’attacco più recente, non è stato possibile determinare con certezza il vettore d’ingresso, **ma alcuni elementi fanno pensare a un coinvolgimento dei server Microsoft Exchange**. Gli strumenti utilizzati per esfiltrare dati e mantenere il controllo includono FreeFileSync, MegaSync e Process Watchdog, oltre agli agenti già citati. **Tutto ciò rafforza l’ipotesi che l’azione non fosse esclusivamente finalizzata al ransomware**, ma che potesse includere componenti di spionaggio industriale.

Il report di Symantec suggerisce infatti che **la componente ransomware potrebbe essere stata solo una copertura per un’operazione più ampia**, con finalità di intelligence economica o geopolitica. “Questi elementi fanno pensare che l’obiettivo dell’attacco potesse essere l’acquisizione di informazioni, mentre il ransomware sarebbe servito a confondere o monetizzare l’azione” – concludono i ricercatori, che hanno pubblicato anche un set di indicatori di compromissione. **“Ciò che è certo è che si tratta di un toolkit insolito per questo tipo di attacco e merita l’attenzione di tutte le aziende che vogliono rafforzare le proprie difese” –** si legge nel report.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi fileless](https://www.securityinfo.it/tag/attacchi-fileless/), [attacco ransomware](https://www.securityinfo.it/tag/attacco-ransomware/), [malware](https://www.securityinfo.it/tag/malware/), [penetration testing](https://www.securityinfo.it/tag/penetration-testing/)

[Kali Linux 2025.2, la nuova versione ha anche un toolkit per l'hacking delle auto](https://www.securityinfo.it/2025/06/17/kali-linux-2025-2-la-nuova-versione-ha-anche-un-toolkit-per-lhacking-delle-auto/)
[Anubis, un nuovo ransomware che integra un wiper](https://www.securityinfo.it/2025/06/16/anubis-un-nuovo-ransomware-che-integra-un-wiper/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per ...