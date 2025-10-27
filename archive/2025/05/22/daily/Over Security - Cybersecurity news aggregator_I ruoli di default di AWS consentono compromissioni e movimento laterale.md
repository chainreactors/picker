---
title: I ruoli di default di AWS consentono compromissioni e movimento laterale
url: https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws-consentono-compromissioni-e-movimento-laterale/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-22
fetch_date: 2025-10-06T22:31:12.851788
---

# I ruoli di default di AWS consentono compromissioni e movimento laterale

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

## I ruoli di default di AWS consentono compromissioni e movimento laterale

Mag 21, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws-consentono-compromissioni-e-movimento-laterale/#respond)

---

I ricercatori di Aqua, firma di cybersecurity statunitense, [hanno scoperto](https://www.aquasec.com/blog/shadow-roles-aws-defaults-lead-to-service-takeover/) che i **ruoli di default di AWS** possono spianare la strada agli attaccanti consentendo **compromissioni di account, accessi cross-servizio ed escalation di privilegi.**

I ruoli IAM incriminati vengono creati automaticamente durante il setup del servizio  e permettono l’**accesso completo allo storage S3**. Il problema è stato individuato in diversi servizi AWS, tra cui SageMaker, Glue e EMR dove la policy *AmazonS3FullAccess*, insieme ad altre con permessi estesi, viene applicata ai ruoli di default. “*Questi ruoli, pensati originariamente per usi ristretti e specifici al servizio, possono essere invece abusati per eseguire azioni di livello amministratori ed eludere l’isolamento tra servizi*” si legge sul blog della compagnia.

![ruoli AWS](https://www.securityinfo.it/wp-content/uploads/2025/05/ai-generated-9123440_1920.jpg)

Il problema di fornire accesso completo ai bucket non è infatti solo un rischio per i dati, ma consente a un utente malintenzionato di accedere ad altri servizi e comprometterli. “***Molti servizi AWS si affidano a S3 per memorizzare risorse essenziali come script, file di configurazione e modelli.** Ottenere l’accesso completo a S3 consente a un aggressore di manipolare il comportamento interno di servizi come CloudFormation, SageMaker, Glue, EMR, nonché di strumenti come l’AWS CDK, con un’escalation dei privilegi che va ben oltre l’ambito originario del ruolo*“.

Considerano che i nomi dei bucket S3 sono altamente prevedibili, e visti i permessi di scrittura e lettura sulle risorse, **un attaccante può usare i privilegi del ruolo di default per individuare i bucket usati dagli altri servizi e modificare risorse** come i template di CloudFormation, gli script EMR e le risorse di SageMaker. “*Se un qualsiasi ruolo di un account ha AmazonS3FullAccess (che sia attraverso una policy aggiunta o tramite permessi inline), ha effettivamente accesso in lettura/scrittura a ogni bucket S3 e, di conseguenza, la possibilità di compromette più servizi AWS*“.

## I rischi dei ruoli AWS di default

Nel blog i ricercatori di Aqua hanno evidenziato alcuni **scenari d’attacco** che sfruttano la vulnerabilità dei ruoli di default di AWS. In un caso, il team ha dimostrato che è possibile **importare un modello malevolo** da HuggingFace su SageMaker per eseguire codice pericoloso per l’intero ambiente, per esempio con una backdoor che sottrae le credenziali. “*L’esecuzione di modelli non attendibili è intrinsecamente rischiosa, ma il pericolo è ancora maggiore perché SageMaker opera con ruoli di esecuzione predefiniti con ampie autorizzazioni, come AmazonS3FullAccess*”

In un altro caso, i ricercatori hanno effettuato una escalation dei privilegi dal ruolo ***AWSGlueServiceRole*** a quello di admin. Modificando i job Glue, gli attaccanti possono estendere il proprio raggio d’azione accedendo a tutti i bucket S3 dell’account e accedere in questo modo ad altri servizi collegati.

![](https://www.securityinfo.it/wp-content/uploads/2025/05/hacker-6512174_1920.jpg)

Il rischio derivante dai ruoli di default **non impatta soltanto i servizi AWS, ma anche molti progetti open-source** usati dalle organizzazioni per utilizzare risorse negli ambienti AWS. Quando, per esempio, si utilizzato tool come Terraform, Ray o librerie Python, solitamente durante il processo vengono creati dei ruoli IAM di default per il progetto; anche in questo caso, i ruoli vengono creati con permessi troppo estesi, garantendo accesso completo ai bucket.

In risposta all’analisi di Aqua, **AWS ha applicato alcune mitigazioni per arginare i rischi**, principalmente riducendo lo scope e i permessi dei ruoli creati di default; inoltre, l’azienda ha inviato delle comunicazioni ai propri utenti per informarli dei cambiamenti e delle buone pratiche da applicare durante la creazione dei ruoli.

“*AWS ha confermato che AWS CDK (Cloud Development Kit), AWS Glue, Amazon EMR (Elastic MapReduce) e Amazon SageMaker funzionano come previsto. **Il problema è stato risolto modificando i criteri dei ruoli di servizio predefiniti**, in particolare il criterio AmazonS3FullAccess. Amazon Lightsail ha aggiornato la documentazione per indicare agli utenti di creare bucket con un criterio di tipo scoped-down. AWS CDK ha assicurato che le risorse CDK vengano caricate solo nei bucket dell’account dell’utente*“.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AWS](https://www.securityinfo.it/tag/aws/), [Bucket S3](https://www.securityinfo.it/tag/bucket-s3/), [elevation dei privilegi](https://www.securityinfo.it/tag/elevation-dei-privilegi/), [IAM](https://www.securityinfo.it/tag/iam/), [permessi](https://www.securityinfo.it/tag/permessi/), [ruoli di default](https://www.securityinfo.it/tag/ruoli-di-default/)

[Spionaggio russo: scoperta una campagna attiva dal 2022](https://www.securityinfo.it/2025/05/22/spionaggio-russo-scoperta-una-campagna-attiva-dal-2022/)
[ESET APT report: crescono gli attacchi russi, cinesi e no...