---
title: Le falle di sicurezza nei toolkit ML più diffusi
url: https://www.securityinfo.it/2024/11/15/le-falle-di-sicurezza-nei-toolkit-ml-piu-diffusi/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-16
fetch_date: 2025-10-06T19:18:51.803718
---

# Le falle di sicurezza nei toolkit ML più diffusi

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

## Le falle di sicurezza nei toolkit ML più diffusi

Nov 15, 2024  [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/ "Articoli scritti da Valentina Caruso")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/11/15/le-falle-di-sicurezza-nei-toolkit-ml-piu-diffusi/#respond)

---

La sicurezza dei toolkit ML continua a essere minacciata da una serie di vulnerabilità piuttosto diffuse. Un’analisi recente di [JFrog](https://jfrog.com/), azienda specializzata nella **sicurezza della catena di fornitura del software**, ha rivelato una serie di debolezze presenti in 15 progetti open-source legati al mondo dei **sistemi di apprendimento automatico (ML)**. Parliamo di falle che potrebbero compromettere sia server sia client.

## Vulnerabilità di tutti i generi

Nel complesso, **i ricercatori JFrog hanno individuato oltre venti vulnerabilità**. Sfruttandole, i cybercriminali potrebbero prendere il controllo di componenti critiche dei sistemi ML, tra cui database e pipeline di addestramento. Una delle vulnerabilità individuate, **CVE-2024-7340 (Weave ML), è una falla directory traversal.** Questa fragilità permette agli utenti con pochi privilegi di accedere a file riservati eludendo le protezioni. Gli attacchi che la sfruttano vengono spesso sottovalutati rispetto ad altre minacce online ma sono in realtà altrettanto pericolosi.

Ci sono poi vulnerabilità legate a **misure di accesso deboli o privilegi assegnati in modo errato**. La prima tipologia (ZenML) permette agli utenti di ottenere autorizzazioni amministrative e manipolare il codice. La seconda, invece, si chiama CVE-2024-6507 (Deep Lake) ed è **una** **vulnerabilità di tipo injection** che consente ai malintenzionati di eseguire comandi di sistema su dataset remoti.

**CVE-2024-45187** (Mage AI), grazie ai privilegi assegnati in modo errato, fa sì che **utenti guest** siano **autorizzati ad eseguire codice arbitrario da remoto**, anche dopo la loro cancellazione, per 30 giorni.

![falle di sicurezza nei toolkit ML](https://www.securityinfo.it/wp-content/uploads/2024/11/falle-di-sicurezza-nei-toolkit-ML.jpeg)

JFrog ha sottolineato che molte di queste falle possono portare a violazioni anche gravi. Questo perché **i cybercriminali possono sfruttarle per accedere a dati, training e modelli**. Una pipeline vulnerabile può permettere agli hacker di compromettere severamente i modelli ML, fare data poisoning o installare backdoor.

## Servono protezioni per i toolkit ML

Le falle di cui abbiamo parlato sono state identificate in strumenti come Weave, ZenML, Deep Lake, Vanna.AI e Mage AI. Tutte consentono, potenzialmente, di **accedere senza autorizzazione a dati sensibili e modelli ML**.

Questo panorama di vulnerabilità dimostra quanto sia essenziale una protezione completa e aggiornata dei sistemi ML per contrastare proattivamente le minacce, prevenire eventuali attacchi e proteggere dati e modelli sensibili.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

[Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti](https://www.securityinfo.it/2024/11/18/una-vulnerabilita-di-un-plugin-di-wordpress-mette-a-rischio-piu-di-4-milioni-di-siti/)
[Come si protegge dalle minacce un vendor che fa sicurezza IT](https://www.securityinfo.it/2024/11/15/come-si-protegge-dalle-minacce-un-vendor-che-fa-sicurezza-it/)

---

![](https://secure.gravatar.com/avatar/0a083e115b9328218407201798ab82c0?s=90&d=mm&r=g)

##### [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/)

##### Articoli correlati

* [![Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/wp-content/uploads/2019/01/Morten-Lehn-120x85.jpg)](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  [Transparency Center Initiative di...](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Permanent link to Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  Gen 18, 2019  [0](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/#respond)
* [![CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/wp-content/uploads/2025/10/CERT-AGID-cover-120x85.png)](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/ "CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco")

  [CERT-AGID 27 settembre – 3 ottobre:...](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/ "Permanent link to CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco")

  Ott 06, 2025  [0](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/#respond)
* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/202...