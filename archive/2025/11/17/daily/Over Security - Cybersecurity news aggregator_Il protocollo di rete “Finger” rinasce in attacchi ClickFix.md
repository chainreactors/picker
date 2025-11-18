---
title: Il protocollo di rete “Finger” rinasce in attacchi ClickFix
url: https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-17
fetch_date: 2025-11-18T03:14:59.607687
---

# Il protocollo di rete “Finger” rinasce in attacchi ClickFix

Aggiornamenti recenti Novembre 17th, 2025 5:06 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Il protocollo di rete “Finger” rinasce in attacchi ClickFix](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/)
* [CERT-AGID 8–14 novembre: ondata di phishing su hosting, PagoPA e università](https://www.securityinfo.it/2025/11/17/cert-agid-8-14-novembre-ondata-di-phishing-su-hosting-pagopa-e-universita/)
* [Vulnerabilità di Fortinet FortiWeb sfruttata per creare utenti admin](https://www.securityinfo.it/2025/11/14/vulnerabilita-di-fortinet-fortiweb-sfruttata-per-creare-utenti-admin/)
* [Crescono le truffe ai danni dei consumatori, preoccupano quelle basate su IA. Il report di Bitdefender](https://www.securityinfo.it/2025/11/13/crescono-le-truffe-ai-danni-dei-consumatori-preoccupano-quelle-basate-su-ia-il-report-di-bitdefender/)
* [Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/)

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

## Il protocollo di rete “Finger” rinasce in attacchi ClickFix

Nov 17, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/#respond)

---

Il comando “**Finger**“, legato all’omonimo protocollo di rete, è tornato in auge nell’ambito di alcuni attacchi **ClickFix**, per eseguire comandi da remoto su dispositivi Windows e distribuire malware.

Nato inizialmente per sistemi Unix e Linux, il comando è stato aggiunto in seguito anche nei sistemi Windows. Il protocollo permette a un utente di visualizzare informazioni sugli altri utenti del sistema, quali, per esempio, il nome di login, la directory home e l’ultimo accesso. Pur essendo ancora supportato, il protocollo ormai viene usato pochissimo.

Come [riporta](https://www.bleepingcomputer.com/news/security/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/) Bleeping Computer, di recente sono state individuate alcune campagne malware che hanno usato Finger per attacchi ClickFix che eseguono comandi da remoto.

![Finger ClickFix](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_3sw5nn3sw5nn3sw5.png)

Nel dettaglio, gli attaccanti ingannano gli utenti chiedendogli di copiare e incollare un comando nel prompt di Windows ed eseguirlo, per esempio a completamento di una verifica CAPTCHA o nel caso di inviti a riunioni. Il comando usa la sintassi di Finger per connettersi a un server malevolo e, sfruttando la pipe (|), **reindirizza l’output del comando Finger a un altro processo.**

La risposta del server contiene infatti una serie di comandi Windows che, una volta eseguiti, installano il malware sul dispositivo della vittima. Il malware è spesso un **infostealer**, ma in alcune varianti più evolute è un RAT.

Non è la prima volta che il comando Finger viene abusato in questo modo: già nel 2020 alcuni ricercatori avevano segnalato casi simili. Le varianti più recenti del malware sono in grado di terminare l’esecuzione di eventuali strumenti di sicurezza attivi; nel caso in cui non ci siano tool di analisi in esecuzione, viene configurato un task per garantire la persistenza del software malevolo, avviandolo ogni volta che l’utente effettua il login.

Per bloccare l’uso del comando Finger e di conseguenza gli attacchi ClickFix che sfruttano questo vettore, Bleeping Computer consiglia di **bloccare il traffico in uscita sulla porta TCP 79**, ovvero quella usata dal protocollo per connettersi ai servizi remoti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [clickfix](https://www.securityinfo.it/tag/clickfix/), [esecuzione di codice da remoto](https://www.securityinfo.it/tag/esecuzione-di-codice-da-remoto/), [Finger](https://www.securityinfo.it/tag/finger/), [Phishing](https://www.securityinfo.it/tag/phishing/), [protocollo di rete](https://www.securityinfo.it/tag/protocollo-di-rete/), [Windows](https://www.securityinfo.it/tag/windows/)

[CERT-AGID 8–14 novembre: ondata di phishing su hosting, PagoPA e università](https://www.securityinfo.it/2025/11/17/cert-agid-8-14-novembre-ondata-di-phishing-su-hosting-pagopa-e-universita/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Crescono le truffe ai danni dei consumatori, preoccupano quelle basate su IA. Il report di Bitdefender](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_9fducr9fducr9fdu-120x85.png)](https://www.securityinfo.it/2025/11/13/crescono-le-truffe-ai-danni-dei-consumatori-preoccupano-quelle-basate-su-ia-il-report-di-bitdefender/ "Crescono le truffe ai danni dei consumatori, preoccupano quelle basate su IA. Il report di Bitdefender")

  [Crescono le truffe ai danni dei...](https://www.securityinfo.it/2025/11/13/crescono-le-truffe-ai-danni-dei-consumatori-preoccupano-quelle-basate-su-ia-il-report-di-bitdefender/ "Permanent link to Crescono le truffe ai danni dei consumatori, preoccupano quelle basate su IA. Il report di Bitdefender")

  Nov 13, 2025  [0](https://www.securityinfo.it/2025/11/13/crescono-le-truffe-ai-danni-dei-consumatori-preoccupano-quelle-basate-su-ia-il-report-di-bitdefender/#respond)
* [![Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_lgvdyplgvdyplgvd-120x85.png)](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/ "Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo")

  [Fantasy Hub: scoperto un nuovo RAT...](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/ "Permanent link to Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo")

  Nov 12, 2025  [0](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/#respond)
* [![In aumento gli attacchi alle applicazioni pubbliche, calano i ransomware: il report di Cisco Talos](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_6ojw546ojw546ojw-120x85.png)](https://www.securityinfo.it/2025/11/04/in-aumento-gli-attacchi-alle-applicazioni-pubbliche-calano-i-ran...