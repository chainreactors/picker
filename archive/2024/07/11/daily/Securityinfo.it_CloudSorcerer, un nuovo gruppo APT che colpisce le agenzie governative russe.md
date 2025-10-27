---
title: CloudSorcerer, un nuovo gruppo APT che colpisce le agenzie governative russe
url: https://www.securityinfo.it/2024/07/10/cloudsorcerer-un-nuovo-gruppo-apt-che-colpisce-le-agenzie-governative-russe/?utm_source=rss&utm_medium=rss&utm_campaign=cloudsorcerer-un-nuovo-gruppo-apt-che-colpisce-le-agenzie-governative-russe
source: Securityinfo.it
date: 2024-07-11
fetch_date: 2025-10-06T17:47:23.135288
---

# CloudSorcerer, un nuovo gruppo APT che colpisce le agenzie governative russe

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

## CloudSorcerer, un nuovo gruppo APT che colpisce le agenzie governative russe

Lug 10, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/07/10/cloudsorcerer-un-nuovo-gruppo-apt-che-colpisce-le-agenzie-governative-russe/#respond)

---

I ricercatori di Securelist di Kaspersky [hanno individuato](https://securelist.com/cloudsorcerer-new-apt-cloud-actor/113056/) **CloudSorcerer**, un **nuovo gruppo APT** che prende di mira le agenzie governative russe.

La gang usa un tool di cyberspionaggio sofisticato per monitorare i dispositivi colpiti e **ottenere i dati sensibili sfruttando l’infrastruttura cloud** di Microsoft Graph, Tandex Cloud e Dropbox come server C2.

Dopo aver ottenuto l’accesso iniziale, il gruppo esegue il malware, un binario scritto in C, che inizializza l’ambiente di attività e i moduli. Uno dei moduli centrali del malware è la **backdoor**, la quale si occupa di collezionare diverse informazioni sul sistema colpito, come il nome del computer, lo username e l’uptime di sistema, e inviarle agli attaccanti. Inizialmente i dati vengono memorizzati in una struttura specifica creata a hoc; una volta che il processo di raccolta è completo, le informazioni vengono scritte su una pipe connessa al **modulo C2** per la comunicazione.

![CloudSorcerer](https://www.securityinfo.it/wp-content/uploads/2024/07/cybercrime-8878488_1920.jpg)

Pixabay

La stessa pipe viene usata dal malware per **ricevere comandi dagli attaccanti.** I comandi comprendono, oltre alla raccolta di dati, l’esecuzione di comandi shell, la modifica e la cancellazione di file e l’injection di una shellcode in uno o più processi.

Il server C2 iniziale a cui si collega il modulo di comunicazione è una pagina GitHub relativa a un repository che contiene fork di tre progetti pubblici mai aggiornati. “*L’obiettivo è semplicemente far apparire la pagina GitHub legittima e attiva*“.

I ricercatori sottolineano che **il modus operandi del gruppo ricorda molto quello di CloudWizard APT**, attivo nel 2023, ma il codice del malware è completamente diverso. “*Riteniamo che CloudSorcerer sia un nuovo gruppo che ha adottato un metodo simile per interagire con i servizi di cloud pubblico*” spiega il team di Securelist. “*La capacità del malware di adattare dinamicamente il suo comportamento in base al processo in cui è in esecuzione, insieme all’uso di una complessa comunicazione tra processi attraverso le pipe di Windows, evidenzia ulteriormente la sua sofisticatezza*“.

In seguito, i ricercatori di Threat Insight [hanno scoperto](https://x.com/threatinsight/status/1810363153924108462) una campagna contro organizzazioni statunitensi che utilizza le stesse tecniche messe in pratica da CloudSorcerer. La compagnia ha attribuito le attività a un cluster soprannominato **UNK\_ArbitraryAcrobat**, probabilmente un gruppo diverso che **sta imitando le tattiche di CloudSorcerer.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [backdoor](https://www.securityinfo.it/tag/backdoor/), [C2](https://www.securityinfo.it/tag/c2/), [CloudSorcerer](https://www.securityinfo.it/tag/cloudsorcerer/), [GitHub](https://www.securityinfo.it/tag/github/), [russia](https://www.securityinfo.it/tag/russia/)

[Una nuova vulnerabilità OpenSSH consente l'esecuzione remota di codice](https://www.securityinfo.it/2024/07/11/una-nuova-vulnerabilita-openssh-consente-lesecuzione-remota-di-codice/)
[APT40 è ancora una minaccia: il rapporto di CISA e altre agenzie di cybersecurity](https://www.securityinfo.it/2024/07/10/apt40-e-ancora-una-minaccia-il-rapporto-di-cisa-e-altre-agenzie-di-cybersecurity/)

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
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire...