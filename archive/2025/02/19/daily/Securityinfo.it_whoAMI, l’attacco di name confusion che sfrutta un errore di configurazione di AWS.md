---
title: whoAMI, l’attacco di name confusion che sfrutta un errore di configurazione di AWS
url: https://www.securityinfo.it/2025/02/18/whoami-lattacco-di-name-confusion-che-sfrutta-un-errore-di-configurazione-di-aws/?utm_source=rss&utm_medium=rss&utm_campaign=whoami-lattacco-di-name-confusion-che-sfrutta-un-errore-di-configurazione-di-aws
source: Securityinfo.it
date: 2025-02-19
fetch_date: 2025-10-06T20:49:27.891302
---

# whoAMI, l’attacco di name confusion che sfrutta un errore di configurazione di AWS

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

## whoAMI, l’attacco di name confusion che sfrutta un errore di configurazione di AWS

Feb 18, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/02/18/whoami-lattacco-di-name-confusion-che-sfrutta-un-errore-di-configurazione-di-aws/#respond)

---

I ricercatori di Datadog [hanno individuato](https://securitylabs.datadoghq.com/articles/whoami-a-cloud-image-name-confusion-attack/)  **whoAMI**, un attacco che sfrutta un errore di configurazione delle istanze EC2 di AWS per eseguire codice da remoto sulle macchine.

Il problema risiede nel modo in cui molti progetti ottengono l’**Amazon Machine ID** (AMI), ovvero l’immagine della macchina virtuale usata per avviare l’istanza EC2. Non sempre si conosce l’esatto ID da utilizzare per avviare la macchina: in questi casi è possibile usare la funzionalità di ricerca di AWS per trovare l’AMI più recente per uno specifico sistema operativo in un’area geografica.

![whoAMI](https://www.securityinfo.it/wp-content/uploads/2025/02/normal-flow.png)

Credits: Datadog

Poiché chiunque può pubblicare un AMI nel catalogo di quelli disponibili, è possibile che ce ne siano di malevoli. Per assicurarsi che l’AMI che si vuole utilizzare non sia stato pubblicato da un cyberattaccante, è possibile usare il parametro `--owners` durante la ricerca per specificare il proprietario dell’immagine, per esempio scegliendo se usare solo AMI privati, cioè del proprio account AWS, se di uno specifico account, se di account verificati da Amazon o se di quelli presenti su AWS Marketplace.

Il problema sta proprio nel fatto che molte aziende non specificano questo parametro e si espongono a whoAMI, un **attacco di *name confusion***. “*In un attacco di name confusion, un attaccante pubblica una risorsa dannosa con l’intenzione di ingannare il software mal configurato e fargliela utilizzare al posto della risorsa previst*a” ha spiegato **Seth Art**, Cloud Security Researcher di Datadog.

In molti casi le organizzazioni utilizzano **query automatizzate per** **recuperare l’ID della versione più recente dell’immagine di una macchina virtuale**; a un attaccante è quindi sufficiente pubblicare un AMI con un nome che rispetta i criteri di ricerca e che sia più recente delle altre, in modo che venga utilizzata dalla vittima. Ciò consente a un attaccante di **eseguire codice da remoto sull’istanza colpita** e procedere con altre operazioni malevole.

![](https://www.securityinfo.it/wp-content/uploads/2025/01/network-4851079_1920.jpg)

## Come proteggersi da whoAMI

Secondo l’analisi di Datadog, attualmente circa l’1% delle organizzazioni è vulnerabile all’attacco, con migliaia di account AWS esposti. È importante sottolineare che **utilizzando il parametro `--owners` non si è vulnerabili all’attacco whoAMI.**

A dicembre AWS ha introdotto un nuovo **meccanismo di protezione per bloccare l’esecuzione di AMI pubblicati da account non verificati o non affidabili**. Gli utenti possono definire una white list di provider di immagini elencando gli ID degli account o scegliendo una tra le keyword “amazon” “amazon-marketplace” e “aws-backup-vault”.

Questa funzionalità **consente l’esecuzione delle sole VM con AMI di fornitori presenti nella lista**. La feature introduce inoltre una modalità di audit che permette di scoprire se ci sono in esecuzione delle istanze EC2 di provider non appartenenti alla white list.

[The Hacker News](https://thehackernews.com/2025/02/new-whoami-attack-exploits-aws-ami-name.html) ha contattato AWS per avere informazioni su possibili exploit in atto. Secondo la sussidiaria di Amazon, **non ci sono indicazioni che whoAMI sia stato effettivamente utilizzato dagli attaccanti.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AMI](https://www.securityinfo.it/tag/ami/), [attacco name confusion](https://www.securityinfo.it/tag/attacco-name-confusion/), [AWS](https://www.securityinfo.it/tag/aws/), [EC2](https://www.securityinfo.it/tag/ec2/), [errore di configurazione](https://www.securityinfo.it/tag/errore-di-configurazione/), [whoAMI](https://www.securityinfo.it/tag/whoami/)

[Torna Growth Academy di Google: AI for Cybersecurity. Presente anche una startup italiana](https://www.securityinfo.it/2025/02/19/torna-growth-academy-di-google-ai-for-cybersecurity-presente-anche-una-startup-italiana/)
[Acronis: AI e ransomware le minacce del 2024, l’Italia tra i più colpiti](https://www.securityinfo.it/2025/02/17/acronis-threat-research-ai-ransomware-minacce-2024-italia/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![I ruoli di default di AWS consentono compromissioni e movimento laterale](https://www.securityinfo.it/wp-content/uploads/2025/05/ai-generated-9123440_1920-120x85.jpg)](https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws-consentono-compromissioni-e-movimento-laterale/ "I ruoli di default di AWS consentono compromissioni e movimento laterale")

  [I ruoli di default di AWS consentono...](https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws-consentono-compromissioni-e-movimento-laterale/ "Permanent link to I ruoli di default di AWS consentono compromissioni e movimento laterale")

  Mag 21, 2025  [0](https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws...