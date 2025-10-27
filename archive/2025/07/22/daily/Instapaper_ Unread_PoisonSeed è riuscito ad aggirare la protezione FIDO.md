---
title: PoisonSeed è riuscito ad aggirare la protezione FIDO
url: https://www.securityinfo.it/2025/07/21/poisonseed-e-riuscito-ad-aggirare-la-protezione-fido/
source: Instapaper: Unread
date: 2025-07-22
fetch_date: 2025-10-06T23:51:59.081292
---

# PoisonSeed è riuscito ad aggirare la protezione FIDO

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## PoisonSeed è riuscito ad aggirare la protezione FIDO

Lug 21, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/07/21/poisonseed-e-riuscito-ad-aggirare-la-protezione-fido/#respond)

---

Il team di ricercatori di Expel ha individuato una **nuova tecnica di attacco in grado di aggirare la protezione FIDO** per compromettere gli account delle vittime. Secondo l’[analisi](https://expel.com/blog/poisonseed-downgrading-fido-key-authentications-to-fetch-user-accounts/) di Ben Nahorney e Brandon Overstreet, dietro la campagna di social engineering ci sarebbe **PoisonSeed**, un gruppo già noto per campagne di phishing su ampia scala.

I ricercatori spiegano che la tecnica sfrutta la feature di cross-device sign-in delle chiavi FIDO, la quale consente a un utente di effettuare il login al proprio account su sistemi senza passkey usando un dispositivo registrato, come per esempio uno smartphone. Il gruppo ha sfruttato la funzionalità per eseguire attacchi **adversary-in-the-middle**.

![PoisonSeed FIDO](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_ud7ej8ud7ej8ud7e.png)

Nel dettaglio, l’attacco comincia con l’invio di un’email di phishing alle vittime che riporta a una finta pagina di login. Gli utenti presi di mira hanno una chiave FIDO registrata al proprio account e normalmente viene richiesta l’interazione fisica con la chiave per autenticarsi.

Le informazioni di login vengono inviate al portale legittimo di login e contestualmente **viene inviata una richiesta per utilizzare la feature di cross-device sign-in.** Nel frattempo, all’utente viene mostrato un codice QR da scansionare con il dispositivo che ha la passkey per l’autenticazione, ovvero l’autenticatore per la MFA. “*L’utente scansiona il codice con l’autenticatore MFA, il portale di login e l’autenticatore comunicano e gli attaccanti entrano nell’account*” spiegano i ricercatori.

Sfruttando questa funzionalità PoisonSeed è riuscito a neutralizzare la protezione delle chiavi FIDO, riuscendo ad accedere a documenti, applicazioni e servizi dell’account.

“***Si tratta di uno sviluppo preoccupante, dato che le chiavi FIDO sono spesso considerate uno degli apici dell’autenticazione sicura a più fattori.** Sebbene non sia stata scoperta una vulnerabilità nelle chiavi FIDO, i responsabili IT e SecOps dovranno prendere nota: questo attacco dimostra come un malintenzionato possa eseguire un attacco di successo usando una chiave FIDO installata*” sottolineano i ricercatori.

**Quello eseguito da PoisonSeed non è in realtà l’unico attacco che sfrutta le chiavi FIDO per prendere il controllo degli account**: in un altro incidente di sicurezza analizzato dal team, gli attaccanti sono riusciti a effettuare il reset della password utente e poi generare una propria chiave FIDO.

Nonostante la protezione FIDO sia vittima di un numero sempre maggiore di attacchi negli ultimi tempi, rimane comunque una soluzione fondamentale per la protezione degli account, ma è importante prestare attenzione ai possibili segnali di compromissione ed essere consapevoli della diffusione degli attacchi di phishing.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [adversary-in-the-middle](https://www.securityinfo.it/tag/adversary-in-the-middle/), [Chiavi FIDO](https://www.securityinfo.it/tag/chiavi-fido/), [FIDO](https://www.securityinfo.it/tag/fido/), [MFA](https://www.securityinfo.it/tag/mfa/), [Phishing](https://www.securityinfo.it/tag/phishing/), [PoisonSeed](https://www.securityinfo.it/tag/poisonseed/)

[APT41, il gruppo cinese amplia il raggio d'azione in Africa](https://www.securityinfo.it/2025/07/22/apt41-il-gruppo-cinese-amplia-il-raggio-dazione-in-africa/)
[Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024](https://www.securityinfo.it/wp-content/uploads/2025/08/Firewall-8-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  [SonicWall: Akira non sfrutta uno...](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "Permanent link to SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")...