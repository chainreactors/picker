---
title: Scoperta campagna di spearphishing ai danni di politici giapponesi
url: https://www.securityinfo.it/2022/12/21/spearphishing-politici-giapponesi/?utm_source=rss&utm_medium=rss&utm_campaign=spearphishing-politici-giapponesi
source: Securityinfo.it
date: 2022-12-22
fetch_date: 2025-10-04T02:14:39.319148
---

# Scoperta campagna di spearphishing ai danni di politici giapponesi

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

## Scoperta campagna di spearphishing ai danni di politici giapponesi

Dic 21, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2022/12/21/spearphishing-politici-giapponesi/#respond)

---

I ricercatori di ESET hanno individuato una**campagna di spearphishing ai danni di figure politiche giapponesi.** La campagna si è svolta qualche settimana prima delle elezioni della Camera dei Consiglieri del Giappone, colpendo tutti i politici appartenenti a un partito preciso.

**Il gruppo di hacker è stato identificato come MirrorFace** ed è composto da attaccanti di lingua cinese che tra i loro obiettivi hanno compagnie e organizzazioni con sede in Giappone. **L’operazione è stata eseguita usando il malware LODEINFO**, di proprietà del gruppo criminale.

![spearphishing](https://www.securityinfo.it/wp-content/uploads/2022/12/ransomware-2321665_1280.png)

**La distribuzione del malware è avvenuta nei mesi di luglio e agosto scorsi tramite email di [phishing](https://www.securityinfo.it/2022/11/03/il-cloud-nel-mirino-del-phishing/) indirizzate ai politici**. Ogni mail conteneva un allegato che, se scaricato ed eseguito, estraeva il malware e installava sul dispositivo della vittima.

**LODEINFO è in grado di effettuare screenshot, keylogging, interrompere processi, estrarre file ed eseguire una serie di comandi dopo aver iniziato la comunicazione col server C&C**. Tra le altre cose il malware, nella sua versione a due fasi, può cifrare file e cartelle e modificare il registro di sistema. **L’operatore in controllo del server C&C può inviare diversi comandi per ottenere dati sul dispositivo compromesso**, comprese le informazioni di rete come il numero di computer connessi o la lista di domini disponibili.

Oltre a LODEINFO, gli attaccanti di MirrorFace hanno utilizzato anche **MirrorStealer**, un malware rimasto sconosciuto finora. Si tratta di **un *credential stealer*, ovvero di un malware in grado di sottrarre credenziali da diverse applicazioni come browser e client email.** MirrorStealer memorizza le credenziali rubate in un file di testo e si appoggia a LODEINFO per inviare le informazioni al server degli attaccanti.

![spearphishing](https://www.securityinfo.it/wp-content/uploads/2022/12/pexels-negative-space-177557.jpg)

Anche in questo caso è l’operatore del server C&C a inviare i comandi per esfiltrare le credenziali e i cookie del browser. Tramite il comando *-memory* è possibile eseguire MirrorStealer in-memory su LODEINFO, così che non rimangano tracce sul disco.

Al momento **MirrorFace è ancora in attività con diverse campagne di spearphishing e continua a colpire obiettivi di alto valore**, sia commerciali che politici.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [credential stealer](https://www.securityinfo.it/tag/credential-stealer/), [cyberattacchi](https://www.securityinfo.it/tag/cyberattacchi/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [hacker](https://www.securityinfo.it/tag/hacker/), [lodeinfo](https://www.securityinfo.it/tag/lodeinfo/), [malware](https://www.securityinfo.it/tag/malware/), [mirrorface](https://www.securityinfo.it/tag/mirrorface/), [Phishing](https://www.securityinfo.it/tag/phishing/), [spearphishing](https://www.securityinfo.it/tag/spearphishing/)

[Il business dei ransomware continuerà a evolversi](https://www.securityinfo.it/2022/12/22/ransomware-business-evoluzione/)
[Il gruppo UNC4166 colpisce il governo ucraino](https://www.securityinfo.it/2022/12/21/il-gruppo-unc4166-colpisce-il-governo-ucraino/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1...