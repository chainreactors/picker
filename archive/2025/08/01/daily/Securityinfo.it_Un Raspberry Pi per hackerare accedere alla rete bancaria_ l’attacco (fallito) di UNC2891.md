---
title: Un Raspberry Pi per hackerare accedere alla rete bancaria: l’attacco (fallito) di UNC2891
url: https://www.securityinfo.it/2025/07/31/un-raspberry-pi-per-hackerare-accedere-alla-rete-bancaria-lattacco-di-unc2891/?utm_source=rss&utm_medium=rss&utm_campaign=un-raspberry-pi-per-hackerare-accedere-alla-rete-bancaria-lattacco-di-unc2891
source: Securityinfo.it
date: 2025-08-01
fetch_date: 2025-10-07T00:49:29.480456
---

# Un Raspberry Pi per hackerare accedere alla rete bancaria: l’attacco (fallito) di UNC2891

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## Un Raspberry Pi per hackerare accedere alla rete bancaria: l’attacco (fallito) di UNC2891

Lug 31, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/07/31/un-raspberry-pi-per-hackerare-accedere-alla-rete-bancaria-lattacco-di-unc2891/#respond)

---

I ricercatori di IB-Group [hanno individuato](https://www.group-ib.com/blog/unc2891-bank-heist/) un attacco molto particolare a opera di UNC2891: il gruppo cybercriminale ha progettato un’intrusione ai sistemi bancari utilizzando un **Raspberry Pi per l’accesso fisico agli ATM.**

La particolarità dell’attacco è che la tecnica usata non era documentata né riconosciuta dal framework MITRE ATT&CK e ha permesso al gruppo di accedere alla rete bancaria tenendo un basso profilo, eludendo i controlli di sicurezza tradizionali. “*Group-IB è stato il primo a scoprire che **UNC2891 ha installato fisicamente un Raspberry Pi nella rete interna di una banca – collegandolo allo stesso switch degli ATM – e usato un modem 4G per ottenere l’accesso remoto***” spiegano i ricercatori della compagnia di sicurezza.

![Raspberry Pi](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_2r14d52r14d52r14.png)

Collegando il dispositivo allo stesso switch di rete usato per gli ATM, il gruppo lo ha di fatto inserito direttamente nella rete bancaria; grazie al modem 4G del dispositivo, inoltre, gli attaccanti hanno potuto in seguito accedere da remoto. Il gruppo ha poi utilizzato la backdoor **TINYSHELL**per stabilire un canale di comunicazione C2 con la rete bancaria.

Sebbene la connessione del Raspberry Pi fosse visibile, il processo associato non aveva alcun ID associato, il che ha complicato l’analisi dei tool di forensica digitale. “*Il beaconing in uscita avveniva ogni 600 secondi e **si sono verificati ripetuti tentativi di connessione al Raspberry Pi sulla porta 929**. Tuttavia, durante la fase di triage non sono stati rilevati ID di processo (PID) corrispondenti né processi sospetti*” continuano i ricercatori.

L’analisi più approfondita della memoria ha permesso di individuare la backdoor, il cui processo era offuscato. La backdoor è riuscita a stabilire una connessione con il Network Monitoring Server e da lì con il Mail Server per mantenere la persistenza, anche nel momento in cui il Raspberry Pi è stato rimosso. Per il movimento laterale il gruppo ha usato dei **processi soprannominati “lightdm”**, nome usato per simulare l’esecuzione di LightDM, il display manager usato nei sistemi Linux.

Il team di Group-IB ha rivelato che l’obiettivo finale degli attaccanti era colpire il server di switching degli ATM per eseguire **CAKETAP**, un rootkit in grado di manipolare le risposte di HSM (Hardware Security Module), il dispositivo fisico per la gestione delle chiavi crittografate.

In seguito, il gruppo avrebbe potuto effettuare lo spoofing dei messaggi di autorizzazione delle transazioni finanziarie per eseguire operazioni fraudolente. Fortunatamente, la campagna è stata individuata e interrotta in tempo. Anche se è stato sventato, l’attacco deve servire da importante lezione per gli istituti bancari di **proteggersi non soltanto dai vettori di accesso logici, ma anche fisici.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [accesso fisico](https://www.securityinfo.it/tag/accesso-fisico/), [ATM](https://www.securityinfo.it/tag/atm/), [backdoor](https://www.securityinfo.it/tag/backdoor/), [Group-IB](https://www.securityinfo.it/tag/group-ib/), [infrastruttura bancaria](https://www.securityinfo.it/tag/infrastruttura-bancaria/), [raspberry pi](https://www.securityinfo.it/tag/raspberry-pi/), [UNC2891](https://www.securityinfo.it/tag/unc2891/)

[Criminali abusano dei servizi di link wrapping per aggirare i controlli](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/)
[Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  [Cina contro Nvidia: dubbi sulla...