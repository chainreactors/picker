---
title: Migliaia di chiavi AWS usate in un attacco ransomware
url: https://www.securityinfo.it/2025/04/17/migliaia-di-chiavi-aws-usate-in-un-attacco-ransomware/?utm_source=rss&utm_medium=rss&utm_campaign=migliaia-di-chiavi-aws-usate-in-un-attacco-ransomware
source: Securityinfo.it
date: 2025-04-18
fetch_date: 2025-10-06T22:06:03.065710
---

# Migliaia di chiavi AWS usate in un attacco ransomware

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

## Migliaia di chiavi AWS usate in un attacco ransomware

Apr 17, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Leaks](https://www.securityinfo.it/category/news/leaks-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/04/17/migliaia-di-chiavi-aws-usate-in-un-attacco-ransomware/#respond)

---

Alcuni ricercatori di sicurezza hanno scoperto una nuova **campagna ransomware**ai danni dei bucket S3 che ha sfruttato **migliaia di chiavi di accesso AWS**.

Come si legge su [Cybernews](https://cybernews.com/security/aws-cloud-storage-bucket-ransomware-attacks/), i ricercatori hanno individuato un **database di 1.229 coppie di chiavi AWS uniche** contenenti l’Access Key ID e il corrispondente Secret Access Key. Un’analisi più approfondita ha portato poi all’individuazione della **campagna ransomware**, con numerosi bucket S3 completamente cifrati fatta eccezione per la nota del riscatto.

![AWS ransomware](https://www.securityinfo.it/wp-content/uploads/2025/04/2149101217.jpg)

Gli attaccanti hanno sfruttato la crittografia **Customer-Provided Keys server-side (SSE-C)** per cifrare i dati dei bucket, una tecnica già usata in precedenza in altre campagne ransomware contro AWS. Questo tipo di attacco si basa sul furto delle credenziali dei clienti AWS, senza dover sfruttare eventuali vulnerabilità degli ambienti.

Gli attaccanti, in possesso delle credenziali utente, generano le proprie chiavi di cifratura e le usano per bloccare i dati. “*Questo pattern di attacco consente la ‘compromissione silenziosa’, con nessun alert né report notificato alla vittima, né alcun log*“. Gli attaccanti lasciano la struttura dei bucket intatta e agiscono solo sui dati, tanto che **in diverse istanze le operazioni non si sono interrotte.**

Secondo Bob Diachenko, un ricercatore di sicurezza, **molte vittime potrebbero non essersi ancora rese conto di avere i bucket cifrati**, soprattutto se i file compromessi non vengono usati di frequente o se i bucket vengono usati solo per i backup. “*Questo incidente segna un’escalation significativa nelle tattiche dei ransomware cloud*” ha affermato Diachenko, “*Alcuni backup esposti sono vuoti e potrebbero essere stati creati da poco, mettendo a rischio i progetti futuri*“.

**Non è ancora chiaro come gli attaccanti siano entrati in possesso delle chiavi AWS**. I ricercatori di Cybernews ipotizzano che possano averle raccolte dai repository pubblici, caricate per errore dagli sviluppatori, oppure sfruttando delle configurazioni errate di tool di CI/CD che espongono le credenziali.

Altre possibilità comprendono file di configurazione delle web app con credenziali in chiaro, utenti IAM inattivi di cui non vengono ruotate le chiavi di accesso e in generale qualsiasi tool, dashboard o password manager compromesso.

![](https://www.securityinfo.it/wp-content/uploads/2022/08/ransomware-3998798_1920-2.jpg)

I ricercatori non sono ancora riusciti a individuare i cybercriminali dietro la campagna ransomware contro i bucket S3 AWS. Stando alle informazioni condivise finora, si tratta di un’**operazione altamente automatizzata.**

Il team di Cybernews consiglia di aumentare la sicurezza degli ambienti AWS **disabilitando le chiavi non utilizzate** e ruotando quelle attive. È necessario inoltre implementare **AWS Config** e **GuardDuty** per identificare pattern di accesso sospetti e usare tool automatizzati per scansionare repository pubblici in cerca di eventuali chiavi esposte.

Si consiglia infine di applicare il **principio del *least privilege*ai ruoli IAM nei bucket**, rimuovere le credenziali hardcoded nelle applicazioni e configurare delle policy per ridurre l’uso della crittografia SSE-C.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AWS](https://www.securityinfo.it/tag/aws/), [crittografia](https://www.securityinfo.it/tag/crittografia/), [leak chiavi AWS](https://www.securityinfo.it/tag/leak-chiavi-aws/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [S3 bucket](https://www.securityinfo.it/tag/s3-bucket/), [SSE-C](https://www.securityinfo.it/tag/sse-c/)

[XorDDoS, il DDoS contro Linux evolve e continua a mietere vittime](https://www.securityinfo.it/2025/04/18/xorddos-il-ddos-contro-linux-continua-a-mietere-vittime/)
[Aggiornato: Addio a CVE - il governo U.S.A. (sospende) riprende i finanziamenti per il programma](https://www.securityinfo.it/2025/04/16/addio-a-cve-il-governo-u-s-a-sospende-i-finanziamenti-per-il-programma/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/0...