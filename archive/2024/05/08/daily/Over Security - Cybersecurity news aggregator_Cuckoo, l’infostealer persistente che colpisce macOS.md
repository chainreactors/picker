---
title: Cuckoo, l’infostealer persistente che colpisce macOS
url: https://www.securityinfo.it/2024/05/07/cuckoo-lo-spyware-persistente-che-colpisce-macos/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-08
fetch_date: 2025-10-06T17:18:30.365651
---

# Cuckoo, l’infostealer persistente che colpisce macOS

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

## Cuckoo, l’infostealer persistente che colpisce macOS

Mag 07, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/05/07/cuckoo-lo-spyware-persistente-che-colpisce-macos/#respond)

---

A fine aprile i ricercatori di Kandji, piattaforma per la gestione e la sicurezza dei dispositivi Apple, [ha individuato](https://blog.kandji.io/malware-cuckoo-infostealer-spyware) **Cuckoo, un malware che colpisce i dispositivi macOS.**

Cuckoo si presenta come un **infostealer** che colleziona diverse informazioni sul dispositivo colpito, ma ha anche dimostrato capacità di mantenere la **persistenza** sui sistemi, una **caratteristica tipica degli spyware**. Dopo l’installazione, **il malware crea una copia di se stesso e si salva in una cartella nella directory home dell’utente**.

In seguito, Cuckoo effettua l’escalation dei privilegi mostrando un prompt che **invita l’utente a inserire la sua password**. Il popup non chiede esplicitamente la password del sistema, ma richiede l’accesso alle impostazioni di sistema.

Tra i dati raccolti ci sono i **preferiti, i cookie e la cronologia di Safari**, le informazioni contenute nella directory **Keychain**, come password e dati sull’account, e le **note salvate.** Il malware cerca anche file di vario tipo sul Desktop e nella cartella Documenti, come documenti .pdf, .rtf e .txt, immagini .jpg e file .sql e .ovpn. Cuckoo può inoltre **effettuare screenshot dello schermo** e inviarlo al server C2 degli attaccanti.

![apple mac](https://www.securityinfo.it/wp-content/uploads/2024/05/mac-733178_1920.jpg)

Pixabay

Cuckoo è in grado di colpire sia i device macOS basati su Intel che su Arm e viene distribuito come binario su siti quali dumpmedia[.]com, tunesolo[.]com, fonedog[.]com, tunesfun[.]com e tunefab[.]com, spacciandosi per un’**applicazione per scaricare musica dai servizi di streaming e convertire le tracce in MP3.**

Un’altra caratteristica del malware è che, una volta scaricato e installato sul dispositivo, prima di proseguire con le attività malevole **controlla se il dispositivo è in lingua armena, bielorussa, kazaka, russa o ucraina e, in caso affermativo, non procede con l’infezione.**

Secondo i ricercatori, è molto probabile che **Cuckoo sia diffuso anche su altri siti web e applicazioni e non sia ancora stato individuato.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Cuckoo](https://www.securityinfo.it/tag/cuckoo/), [infostealer](https://www.securityinfo.it/tag/infostealer/), [macOS](https://www.securityinfo.it/tag/macos/), [malware](https://www.securityinfo.it/tag/malware/), [spyware](https://www.securityinfo.it/tag/spyware/)

[In Microsoft le paghe dei manager dipenderanno dal livello di sicurezza](https://www.securityinfo.it/2024/05/08/in-microsoft-le-paghe-dei-manager-dipenderanno-dal-livello-di-sicurezza/)
[Attacchi di phishing: Microsoft e Google le più colpite](https://www.securityinfo.it/2024/05/07/attacchi-di-phishing-microsoft-e-google-le-piu-colpite/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-d...