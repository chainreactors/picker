---
title: Trovate credenziali cloud hardcoded e in chiaro in numerose applicazioni
url: https://www.securityinfo.it/2024/10/24/trovate-credenziali-cloud-hardcoded-e-in-chiaro-in-numerose-applicazioni/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-25
fetch_date: 2025-10-06T18:55:10.492883
---

# Trovate credenziali cloud hardcoded e in chiaro in numerose applicazioni

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

## Trovate credenziali cloud hardcoded e in chiaro in numerose applicazioni

Ott 24, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Gestione dati](https://www.securityinfo.it/category/news/gestione-dati-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Privacy](https://www.securityinfo.it/category/news/privacy-news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/24/trovate-credenziali-cloud-hardcoded-e-in-chiaro-in-numerose-applicazioni/#respond)

---

Il team di Symantec ha scoperto che molte applicazioni mobile contengono **credenziali harcoded e in chiaro dei servizi cloud più utilizzati.** “*Questa pratica pericolosa implica che **chiunque con accesso ai binari o al codice sorgente dell’applicazione potenzialmente può estrarre queste credenziali e abusarne per manipolare o sottrarre dati**, causando breach di sicurezza gravi*” [spiegano](https://www.security.com/threat-intelligence/exposing-danger-within-hardcoded-cloud-credentials-popular-mobile-apps) i ricercatori.

Le applicazioni analizzate da Symantec vengono **scaricate e usate da milioni di utenti in tutto il mondo**. “**The Pic Stitch: Collage Maker**“, per esempio, conta oltre 5 milioni di download su Google Play e contiene credenziali AWS direttamente nel codice. Il codice dell’applicazione include una funzione per usare le credenziali AWS a seconda dell’ambiente in cui sta eseguendo; nel caso il flag di produzione sia a *true*, l’app legge tutte le informazioni di produzione, compresi il bucket name di Amazon S3, le chiavi di lettura e scrittura e i secret.

![credenziali cloud](https://www.securityinfo.it/wp-content/uploads/2024/10/cyber-1654709_1920.jpg)

**La situazione è analoga in** **applicazioni iOS** quali “**Crumbl**“, con quasi 4 milioni di recensioni, “**Eureka: Earn money for surveys**” che ha oltre 402 mila recensioni, e “**Videoshop – Video Editor**” che ha quasi 400 mila recensioni. Queste applicazioni usano credenziali presenti in chiaro nel codice, esponendo risorse critiche del cloud agli attacchi.

Altre applicazioni, come “**Meru Cabs**” che conta oltre 5 milioni di download e “**Sulekha Business**“, contengono credenziali Azure hardcoded all’interno del codice ed espongono gli utenti a seri rischi di privacy.

“*Questo pattern di gestione non sicura delle credenziali ripetuto su più applicazioni evidenzia la **necessità critica di adottare più pratiche di sicurezza da parte degli sviluppatori***“.

Il team di Symantec invita gli sviluppatori a **usare le variabili d’ambiente** per le credenziali, al posto di inserirle direttamente nel codice, e di **utilizzare tool di gestione dei secret** come AWS Secret Manager o Azure Key Vault.

Nel caso le credenziali debbano essere memorizzate nell’applicazione, occorre **cifrarle usando algoritmi robusti** e decifrarle a runtime solo quando è necessario.

Oltre a ciò è fondamentale eseguire **review di codice regolari e audit di sicurezza**, integrando anche l’uso di **tool di scansione del codice** per individuare subito eventuali problemi di sicurezza.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [applicazione mobile](https://www.securityinfo.it/tag/applicazione-mobile/), [AWS](https://www.securityinfo.it/tag/aws/), [Azure](https://www.securityinfo.it/tag/azure/), [cifratura credenziali](https://www.securityinfo.it/tag/cifratura-credenziali/), [Cloud](https://www.securityinfo.it/tag/cloud/), [credenziali](https://www.securityinfo.it/tag/credenziali/)

[Siti WordPress hackerati, la nuova evoluzione di ClickFix](https://www.securityinfo.it/2024/10/25/siti-wordpress-hackerati-la-nuova-evoluzione-di-clickfix/)
[Attacchi ibridi alle password, cosa sono e come difendersi](https://www.securityinfo.it/2024/10/24/attacchi-ibridi-alle-password-cosa-sono-e-come-difendersi/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Le aziende italiane prevedono un aumento degli investimenti in cybersecurity](https://www.securityinfo.it/wp-content/uploads/2025/06/security-4868167_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/06/09/le-aziende-italiane-prevedono-un-aumento-degli-investimenti-in-cybersecurity/ "Le aziende italiane prevedono un aumento degli investimenti in cybersecurity")

  [Le aziende italiane prevedono un...](https://www.securityinfo.it/2025/06/09/le-aziende-italiane-prevedono-un-aumento-degli-investimenti-in-cybersecurity/ "Permanent link to Le aziende italiane prevedono un aumento degli investimenti in cybersecurity")

  Giu 09, 2025  [0](https://www.securityinfo.it/2025/06/09/le-aziende-italiane-prevedono-un-aumento-degli-investimenti-in-cybersecurity/#respond)
* [![I ruoli di default di AWS consentono compromissioni e movimento laterale](https://www.securityinfo.it/wp-content/uploads/2025/05/ai-generated-9123440_1920-120x85.jpg)](https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws-consentono-compromissioni-e-movimento-laterale/ "I ruoli di default di AWS consentono compromissioni e movimento laterale")

  [I ruoli di default di AWS consentono...](https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws-consentono-compromissioni-e-movimento-laterale/ "Permanent link to I ruoli di default di AWS consentono compromissioni e movimento laterale")

  Mag 21, 2025  [0](https://www.securityinfo.it/2025/05/21/i-ruoli-di-default-di-aws-consentono-compromissioni-e-movimento-laterale/#respond)
* [![Migliaia di chiavi AWS usate in un attacco ransomware](https://www.securityinfo.it/wp-content/uploads/2025/04/2149101217-120x85.jpg)](https://www.sec...