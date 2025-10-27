---
title: Una vulnerabilità critica di NVIDIA permette di prendere il controllo di interi ambienti cloud
url: https://www.securityinfo.it/2024/09/27/una-vulnerabilita-critica-di-nvidia-permette-di-prendere-il-controllo-di-interi-ambienti-cloud/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-28
fetch_date: 2025-10-06T18:30:36.886528
---

# Una vulnerabilità critica di NVIDIA permette di prendere il controllo di interi ambienti cloud

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

## Una vulnerabilità critica di NVIDIA permette di prendere il controllo di interi ambienti cloud

Set 27, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/09/27/una-vulnerabilita-critica-di-nvidia-permette-di-prendere-il-controllo-di-interi-ambienti-cloud/#respond)

---

I ricercatori di Wiz [hanno scoperto](https://www.wiz.io/blog/wiz-research-critical-nvidia-ai-vulnerability) una **vulnerabilità critica in NVIDIA Container Toolkit**, un insieme di strumenti che consentono di creare applicazioni di IA in container con accesso alle risorse GPU. Il bug permette a un attaccante che controlla l’immagine del container eseguita dal toolkit di uscire dal contesto del container e **prendere il controllo del sistema host.**

Il toolkit proposto da NVIDIA consente di **condividere una singola GPU tra diversi carichi di lavoro** e potenzialmente tra diversi utenti. I driver e gli strumenti contenuti nel toolkit consentono di abilitare l’uso nativo della GPU anche all’interno degli ambienti containerizzati; negli ultimi anni, questo insieme di strumenti è diventato molto usato pe le applicazioni di intelligenza artificiale.

![NVIDIA vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2024/09/nvidia-1692796_1920.jpg)

Pixabay

Come riporta NVIDIA nel suo [advisory di sicurezza](https://nvidia.custhelp.com/app/answers/detail/a_id/5582), la vulnerabilità, tracciata come **CVE-2024-0132**, è un bug di **Time-of-check Time-of-use**, un tipo di race condition sul controllo dello stato di una risorsa. “*Un exploit riuscito della vulnerabilità può portare all’esecuzione di codice, all’interruzione di servizio, all’escalation dei privilegi, alla pubblicazione di informazioni e alla modifica di dati*” spiega la compagnia.

Per sfruttare l’exploit, un attaccante deve creare un’immagine malevola specifica per sfruttare la vulnerabilità. Dopo aver eseguito l’immagine sulla piattaforma target, l’attaccante ottiene i **pieni permessi di lettura sull’host** e di conseguenza la completa visibilità dell’infrastruttura sottostante.

Dopo aver ottenuto questo accesso, l’attaccante può **prendere il controllo delle socket Container Runtime Unix** ed eseguire comandi sull’host con privilegi di root, di fatto prendendo il controllo della macchina.

## L’impatto della vulnerabilità NVIDIA

La vulnerabilità mette a rischio chiunque utilizzi NVIDIA Container Toolkit, ma **i più a rischio sono gli ambienti che consentono l’esecuzione di immagini o modelli di IA di terze parti**, sia internamente che in modalità as-a-service.

I ricercatori di Wiz spiegano che, nel caso di un exploit in un ambiente orchestrato e condiviso come Kubernetes, un attaccante che ha i permessi di eseguire un container potrebbe ottenere dati e segreti di altre applicazioni che sono in esecuzione sullo stesso nodo o nello stesso ambiente.

Questo scenario diventa ancora più pericoloso nel caso in cui i provider di servizi IA consentono ai propri clienti di eseguire le loro immagini: un attacco di successo permetterebbe ai cybercriminali di usare i segreti della macchina host per prendere il controllo dell’intero sistema di servizi cloud.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/pattern-3232784_1920-1.jpg)

Secondo le stime dei ricercatori, **il 33% degli ambienti cloud è esposto alla vulnerabilità**. “*La ricerca evidenzia, non per la prima volta, che **i container non sono una barriera di sicurezza forte e non si dovrebbe fare affidamento su di essi come unico mezzo di isolamento.** Quando progettiamo applicazioni, soprattutto quelle multi-tenant, dovremmo sempre “presumere una vulnerabilità” e progettarle in modo da avere almeno una forte barriera di isolamento, come la virtualizzazione*” sottolinea il team di Wiz.

Il bug colpisce tutte le versioni di NVIDIA Container Toolkit fino alla 1.16.1 (compresa). I ricercatori consigliano alle aziende che usano il toolkit di **aggiornarlo il prima possibile alla versione 1.16.2.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Cloud](https://www.securityinfo.it/tag/cloud/), [container](https://www.securityinfo.it/tag/container/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [Nvidia](https://www.securityinfo.it/tag/nvidia/), [NVIDIA Container Toolkit](https://www.securityinfo.it/tag/nvidia-container-toolkit/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[CERT-AGID 14 – 20 settembre: nuove campagne di phishing INPS e per diffondere il malware Vidar](https://www.securityinfo.it/2024/09/30/cert-agid-14-20-settembre-nuove-campagne-di-phishing-inps-e-per-diffondere-il-malware-vidar/)
[Telegram "capitola": l'app fornirà le informazioni degli utenti alle autorità](https://www.securityinfo.it/2024/09/26/telegram-capitola-lapp-fornira-le-informazioni-degli-utenti-alle-autorita/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo....