---
title: Due estensioni Chrome hanno compromesso le chat di ChatGPT e DeepSeek
url: https://www.securityinfo.it/2026/01/07/due-estensioni-chrome-hanno-compromesso-le-chat-di-chatgpt-e-deepseek/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-07
fetch_date: 2026-01-08T03:30:31.281497
---

# Due estensioni Chrome hanno compromesso le chat di ChatGPT e DeepSeek

Aggiornamenti recenti Gennaio 7th, 2026 5:33 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Due estensioni Chrome hanno compromesso le chat di ChatGPT e DeepSeek](https://www.securityinfo.it/2026/01/07/due-estensioni-chrome-hanno-compromesso-le-chat-di-chatgpt-e-deepseek/)
* [Nel 2026 sempre più attacchi autonomi AI-driven e deepfake: le previsioni di sicurezza di ClearSkies](https://www.securityinfo.it/2026/01/05/nel-2026-sempre-piu-attacchi-autonomi-ai-driven-e-deepfake-le-previsioni-di-sicurezza-di-clearskies/)
* [Grave vulnerabilità nei chip Bluetooth Airoha: molti i marchi colpiti](https://www.securityinfo.it/2026/01/05/grave-vulnerabilita-nei-chip-bluetooth-airoha-molti-i-marchi-colpiti/)
* [Kaspersky: così funziona il mercato del lavoro nel dark web](https://www.securityinfo.it/2025/12/23/kaspersky-cosi-funziona-il-mercato-del-lavoro-nel-dark-web/)
* [Kaspersky: il cybercrime finanziario ha alzato il livello nel 2025](https://www.securityinfo.it/2025/12/22/kaspersky-lancia-lallarme-il-cybercrime-finanziario-ha-alza-il-livello-nel-2025/)

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

## Due estensioni Chrome hanno compromesso le chat di ChatGPT e DeepSeek

Gen 07, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/01/07/due-estensioni-chrome-hanno-compromesso-le-chat-di-chatgpt-e-deepseek/#respond)

---

I ricercatori di OX Security [hanno individuato](https://www.ox.security/blog/malicious-chrome-extensions-steal-chatgpt-deepseek-conversations/) due **estensioni Chrome** in grado di OX Security ha individuato due estensioni Chrome in grado di **esfiltrare dati dalle chat di ChatGPT e DeepSeek**.

Le due estensioni (*Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI* e *AI Sidebar with Deepseek, ChatGPT, Claude and more*) contano complessivamente oltre **900.000 download**. La prima aveva anche ottenuto il badge “Featured” da Chrome, dettaglio che ha portato migliaia di utenti a scaricarla senza porsi troppi dubbi.

![estensioni Chrome chat](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_8w0nv08w0nv08w0n.png)

Gli attaccanti hanno pubblicato le estensioni dietro il nome “AITOPIA”, una compagnia fittizia. L’azienda possiede anche un sito web piuttosto curato, con descrizioni dettagliate dei prodotti che offre agli utenti. Nel dettaglio, le estensioni incriminate aggiungono una sidebar in ogni sito web per consentire all’utente di chattare con l’IA in qualsiasi momento.

Una volta installate, le due estensioni richiedono il permesso di “leggere e modificare tutti i dati sui siti web visitati” per monitorare in tempo reale l’URL della scheda attiva. Se l’URL contiene parole chiave come “chatgpt” o “deepseek”, l’estensione entra in modalità “furto”. A questo punto il codice malevolo si occupa di **intercettare il traffico di rete e analizzare il DOM per ottenere tutto ciò che è visibile in pagina**, sia i prompt che le risposte fornite dall’IA. Le estensioni Chrome raccolgono i dati dalle chat e li inviano al server C2 ogni 30 minuti, codificandoli in Base64.

L’impatto potenziale è significativo: oltre a dati personali condivisi, nel caso di utenti aziendali potrebbero essere stati sottratti strategie di business, segreti aziendali, codice proprietario e comunicazioni interne alle organizzazioni, esponendo le aziende alla minaccia dello spionaggio industriale. Oltre al contenuto delle chat, le estensioni sono in grado di **raccogliere i token di sessione** presenti negli URL, ID degli utenti e altri dati di autenticazione.

Gli utenti che hanno installato una o entrambe delle estensioni malevole devono **disinstallarle immediatamente**. È fondamentale fare attenzione alle estensioni che si installano e verificare il proprietario del plug-in, anche quando è presente il badge “Featured”.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chatgpt](https://www.securityinfo.it/tag/chatgpt/), [DeepSeek](https://www.securityinfo.it/tag/deepseek/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [estensioni browser](https://www.securityinfo.it/tag/estensioni-browser/), [estensioni browser malevole](https://www.securityinfo.it/tag/estensioni-browser-malevole/), [estensioni Chrome](https://www.securityinfo.it/tag/estensioni-chrome/)

[Nel 2026 sempre più attacchi autonomi AI-driven e deepfake: le previsioni di sicurezza di ClearSkies](https://www.securityinfo.it/2026/01/05/nel-2026-sempre-piu-attacchi-autonomi-ai-driven-e-deepfake-le-previsioni-di-sicurezza-di-clearskies/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_hnl02xhnl02xhnl0-120x85.png)](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/ "ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni")

  [ShadyPanda: oltre 4 milioni di browser...](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/ "Permanent link to ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni")

  Dic 02, 2025  [0](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/#respond)
* [![DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_87vil587vil587vi-120x85.png)](https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/ "DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”")

  [DeepSeek R1 produce codice vulnerabile...](https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/ "Permanent link to DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”")

  Nov 24, 2025  [0](https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/#respond)
* [![Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_8yofud8yofud8yof-120x85.png)](https://www.securityinfo.it/2025/11/05/scoperte-nuove-vulner...