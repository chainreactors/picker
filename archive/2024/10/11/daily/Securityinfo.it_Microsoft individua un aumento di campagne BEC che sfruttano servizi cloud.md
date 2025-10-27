---
title: Microsoft individua un aumento di campagne BEC che sfruttano servizi cloud
url: https://www.securityinfo.it/2024/10/10/microsoft-individua-un-aumento-di-campagne-bec-che-sfruttano-servizi-cloud/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-individua-un-aumento-di-campagne-bec-che-sfruttano-servizi-cloud
source: Securityinfo.it
date: 2024-10-11
fetch_date: 2025-10-06T18:53:58.508884
---

# Microsoft individua un aumento di campagne BEC che sfruttano servizi cloud

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

## Microsoft individua un aumento di campagne BEC che sfruttano servizi cloud

Ott 10, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/10/microsoft-individua-un-aumento-di-campagne-bec-che-sfruttano-servizi-cloud/#respond)

---

Negli ultimi anni **il numero di campagne di business email compromise (BEC) è cresciuto notevolmente**, anche grazie a un aumento dell’**abuso di servizi cloud** ampiamente usati come Dropbox, SharePoint e OneDrive.

A lanciare l’allarme è Microsoft: in un recente [post](https://www.microsoft.com/en-us/security/blog/2024/10/08/file-hosting-services-misused-for-identity-phishing/) sul suo blog, la compagnia ha evidenziato che la diffusione di questi servizi collaborativi e di file sharing nelle organizzazioni rende gli **utenti aziendali un obiettivo molto interessante** **per gli attaccanti.** Abusando della fiducia che gli utenti ripongono in questi servizi e della facilità di utilizzo, i cybercriminali riescono a condividere file e link malevoli, eludendo i tradizionali controlli di sicurezza.

![BEC cloud](https://www.securityinfo.it/wp-content/uploads/2024/10/ai-generated-8366100_1920.jpg)

Microsoft spiega che l’abuso di questi servizi cloud per condurre campagne BEC è diventato un trend soprattutto per la **relativa facilità di svolgimento degli attacchi**. Da metà aprile 2024, la compagnia ha individuato in particolare due tattiche più usate dagli attaccanti per superare i meccanismi di difesa: una consiste nel condividere via e-mail file con restrizioni di accesso che possono essere aperti solo dal destinatario specificato; questo implica che l’utente debba essere loggato al servizio o eventualmente autenticarsi di nuovo inserendo email e OTP.

La seconda tattica sfrutta i file con permessi di sola lettura per eludere i sistemi di detonation nelle e-mail: **i file condivisi dagli attaccanti sono impostati in modalità “Sola lettura” per impedirne il download** e di conseguenza l’individuazione di URL malevoli nel file.

Solitamente **gli attaccanti ottengono l’accesso iniziale compromettendo l’utente di un vendor dell’azienda** e inviando dei file all’organizzazione target da questo account. “Q*uesto abuso di servizi di file hosting legittimi è particolarmente efficace perché **i destinatari sono più propensi a fidarsi delle e-mail provenienti da fornitori noti**, consentendo agli attaccanti di aggirare le misure di sicurezza e compromettere le identità*” spiegano i ricercatori di Microsoft.

I file condivisi, per essere più credibili, di solito fanno riferimento ad argomenti già oggetto di discussione tra le due aziende o a temi legati al business, e in generale si basano su un senso di urgenza per portare gli utenti ad aprire immediatamente i documenti ricevuti.

Quando la vittima accede al file condiviso, gli viene chiesto di verificare la sua identità inserendo l’email e l’OTP. L’utente apre quindi il documento dove è presente una finta preview di un messaggio e un pulsante per visualizzarlo interamente. Il link rimanda la vittima a una pagina di phishing controllata dall’attaccante; qui **gli viene richiesto di inserire la sua password e completare l’autenticazione multifattore**. Il token, ora in possesso degli attaccanti, può essere usato per prendere il controllo dell’account utente e proseguire con la campagna.

![](https://www.securityinfo.it/wp-content/uploads/2023/01/password-security-4993196_1280.png)

## Difendersi dagli attacchi BEC che abusano del cloud

Per proteggersi da questi attacchi sempre più frequenti, Microsoft consiglia innanzitutto di rendere obbligatoria l’a**utenticazione multifattore** per tutti gli utenti aziendali e, se possibile, eliminare le password.

Nel caso si utilizzi Microsoft Entra, è utile abilitare le **policy di accesso condizionale** e implementare la **continuous access evaluation** per verificare continuamente la sicurezza degli accessi. È inoltre fondamentale adottare soluzioni di sicurezza in grado di identificare e **bloccare siti potenzialmente malevoli** e di scartare le email sospette o anomale prima che raggiungano le vittime.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [BEC](https://www.securityinfo.it/tag/bec/), [Cloud](https://www.securityinfo.it/tag/cloud/), [file condivisi](https://www.securityinfo.it/tag/file-condivisi/), [MFA](https://www.securityinfo.it/tag/mfa/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Phishing](https://www.securityinfo.it/tag/phishing/)

[Attaccanti nascondono uno skimmer negli e-commerce sfruttando i caratteri Unicode](https://www.securityinfo.it/2024/10/10/attaccanti-nascondono-uno-skimmer-negli-e-commerce-sfruttando-i-caratteri-unicode/)
[Cyberinsurance: misurare il rischio umano può rivoluzionare le polizze](https://www.securityinfo.it/2024/10/09/cyberinsurance-misurare-il-rischio-umano-puo-rivoluzionare-le-polizze/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acr...