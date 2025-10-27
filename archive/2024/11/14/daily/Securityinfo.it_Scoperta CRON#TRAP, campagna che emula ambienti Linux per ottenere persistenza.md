---
title: Scoperta CRON#TRAP, campagna che emula ambienti Linux per ottenere persistenza
url: https://www.securityinfo.it/2024/11/13/scoperto-crontrap-un-ambiente-linux-emulato-che-installa-una-backdoor/?utm_source=rss&utm_medium=rss&utm_campaign=scoperto-crontrap-un-ambiente-linux-emulato-che-installa-una-backdoor
source: Securityinfo.it
date: 2024-11-14
fetch_date: 2025-10-06T19:20:06.093629
---

# Scoperta CRON#TRAP, campagna che emula ambienti Linux per ottenere persistenza

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

## Scoperta CRON#TRAP, campagna che emula ambienti Linux per ottenere persistenza

Nov 13, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/11/13/scoperto-crontrap-un-ambiente-linux-emulato-che-installa-una-backdoor/#respond)

---

I ricercatori di Securonix [hanno scoperto](https://www.securonix.com/blog/crontrap-emulated-linux-environments-as-the-latest-tactic-in-malware-staging/) **CRON#TRAP**, una campagna che sfrutta un ambiente Linux emulato per installare una backdoor sul dispositivo della vittima e permettere agli attaccanti di mantenere la persistenza.

L’ambiente viene emulato tramite **Quick Emulator (QEMU)**, un tool open-source di virtualizzazione che consente di emulare diverse architetture per eseguire vari sistemi operativi. Usato solitamente per scopi di test e sviluppo, **essendo un tool legittimo non genera alert di sicurezza.**

“*Questa configurazione consente all’attaccante di mantenere una **presenza furtiva sul computer della vittima**, eseguendo ulteriori attività dannose in un ambiente nascosto, rendendo difficile il rilevamento da parte delle soluzioni antivirus tradizionali*” spiegano i ricercatori.

![CRON#TRAP](https://www.securityinfo.it/wp-content/uploads/2024/11/hacker-8003395_1920.jpg)

Al momento non ancora stato accertato il **vettore iniziale di attacco**, anche se il team di Securonix ritiene che sia stata un’**email di [phishing](https://www.securityinfo.it/2024/11/07/phishing-breach-e-trojan-bancari-acronis-condivide-il-rapporto-sulle-minacce-piu-recenti/)** contenente un link per scaricare un file malevolo. Una volta estratto, il file analizzato dai ricercatori e presumibilmente legato alla campagna di CRON#TRAP, esegue uno script per inizializzare QEMU e creare l’ambiente Linux.

Mentre all’utente viene presentato un messaggio di errore dopo l’apertura del file, l’ambiente Linux, chiamato **“PivotBox”**, viene eseguito in background. PivotBox consente agli attaccanti di eseguire numerosi **comandi per interagire con l’host e inizializzare una comunicazione col server C2.**

Tra i comandi ci sono inoltre indicazioni per installare tool quali vim, file e openssh, eseguire crondx, ottenere persistenza ed elevare i privilegi, creare e manipolare chiavi SSH e stabilire un canale per l’esfiltrazione dei dati.

Secondo i ricercatori di Securonix, la campagna di CRON#TRAP è di particolare interesse perché, pur cominciando con una serie di azioni standard, come l’e-mail di phishing, in seguito utilizza un **approccio molto sofisticato e furtivo, oltre che altamente personalizzato.**

Oltre a evitare di scaricare file sospetti e aprire link malevoli, i ricercatori della compagnia ricordano di monitorare l’eventuale esecuzione di software non previsto sull’host, anche se legittimo, e di affidarsi a soluzioni robuste per la protezione degli endpoint.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [CRON#TRAP](https://www.securityinfo.it/tag/crontrap/), [emulatore](https://www.securityinfo.it/tag/emulatore/), [Linux](https://www.securityinfo.it/tag/linux/), [Phishing](https://www.securityinfo.it/tag/phishing/), [QEMU](https://www.securityinfo.it/tag/qemu/)

[Aumentano le compromissioni di account email delle forze dell'ordine: l'FBI lancia l'allarme](https://www.securityinfo.it/2024/11/14/aumentano-le-compromissioni-di-account-email-delle-forze-dellordine-fbi-lancia-lallarme/)
[Report APT ESET: i gruppi filo-cinesi e iraniani intensificano le attività](https://www.securityinfo.it/2024/11/12/report-apt-eset-i-gruppi-filo-cinesi-e-iraniani-intensificano-le-attivita/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishi...