---
title: Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati
url: https://www.securityinfo.it/2025/11/05/scoperte-nuove-vulnerabilita-di-chatgpt-che-portano-a-leak-di-dati/?utm_source=rss&utm_medium=rss&utm_campaign=scoperte-nuove-vulnerabilita-di-chatgpt-che-portano-a-leak-di-dati
source: Securityinfo.it
date: 2025-11-05
fetch_date: 2025-11-06T03:15:32.136930
---

# Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati

Aggiornamenti recenti Novembre 5th, 2025 7:38 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati](https://www.securityinfo.it/2025/11/05/scoperte-nuove-vulnerabilita-di-chatgpt-che-portano-a-leak-di-dati/)
* [In aumento gli attacchi alle applicazioni pubbliche, calano i ransomware: il report di Cisco Talos](https://www.securityinfo.it/2025/11/04/in-aumento-gli-attacchi-alle-applicazioni-pubbliche-calano-i-ransomware-il-report-di-cisco-talos/)
* [Il 25% dei leader aziendali italiani non comprende l’importanza della cybersecurity](https://www.securityinfo.it/2025/11/03/il-25-dei-leader-aziendali-italiani-non-comprende-limportanza-della-cybersecurity/)
* [CERT-AGID 25–31 ottobre: PagoPA, ministeri e università nel mirino del phishing](https://www.securityinfo.it/2025/11/03/cert-agid-25-31-ottobre-pagopa-ministeri-e-universita-nel-mirino-del-phishing/)
* [Il codice generato da IA pone molti rischi di sicurezza](https://www.securityinfo.it/2025/10/31/il-codice-generato-da-ia-pone-molti-rischi-di-sicurezza/)

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

## Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati

Nov 05, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2025/11/05/scoperte-nuove-vulnerabilita-di-chatgpt-che-portano-a-leak-di-dati/#respond)

---

I ricercatori di Tenable Research [hanno scoperto](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage) **nuove vulnerabilità in ChatGPT**che consentono a un attaccante di **esfiltrare dati e informazioni personali** dalle chat degli utenti. I bug permetterebbero agli attaccanti di provocare leak di dati senza che le vittime se ne accorgano, tramite prompt injection indiretta.

![vulnerabilità ChatGPT](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_8yofud8yofud8yof.png)

In tutto, i ricercatori hanno trovato **sette tra vulnerabilità e tecniche di attacco** che sfruttano le debolezze di ChatGPT:

* una **vulnerabilità di prompt injection indiretta tramite Browsing Context**: gli attaccanti iniettano comandi malevoli in sezioni di blog e articoli, così che quando l’utente richiede un riassunto o una ricerca su queste fonti, quelli vengono eseguiti;
* una **vulnerabilità di prompt injection indiretta zero-day in Search Context**: gli attaccanti inseriscono un prompt malevolo nascosto in un sito web che viene servito solo all’agente di ricerca dell’LLM e non all’utente. Il comando malevolo viene eseguito non appena il sito viene indicizzato dalla ricerca del chatbot;
* una **1-click prompt injection**: in questo caso il prompt malevolo viene inserito in un link creato ad hoc del tipo “chatgpt[.]com/?q={Prompt}”, in modo che il chatbot elabori il contenuto del parametro “q” come una normale richiesta utente;
* un **Safety Mechanism Byp****ass**, ovvero un tecnica che elude la validazione di sicurezza *url\_safe* che il chatbot usa per capire se un URL è sicuro. Il bug sfrutta il fatto che domini noti come bing.com sono in una whitelist e superano sempre il controllo di sicurezza. I risultati di ricerca di Bing sono serviti tramite link di tracciamento reindirizzanti statici (bing.com/ck/a…). L’attaccante indicizza i siti web di prova su Bing per ottenere questi link di tracciamento statici, considerati “sicuri” dall’LLM, permettendo così al contenuto finale del sito di essere renderizzato, mascherando gli URL malevoli;
* una **Conversation Injection Technique**, ovvero una tecnica che usa una prompt injection di primo livello inserendo i prompt malevoli nei siti web combinata a una *conversation injection*che prevede la generazione di un output manipolato. I comandi malevoli non sono quindi solo nei siti web, ma anche nell’output; questo diventa parte della conversazione con l’utente e del contesto e viene usato per rispondere a richieste future;
* una **tecnica per nascondere il contenuto malevolo** che sfrutta un bug del modo in cui ChatGPT renderinzza il markdown: renderizzando i blocchi di codice (con “`), tutte le parole della prima riga (tranne la prima parola) non vengono mostrate nella risposta;
* infine, una **tecnica di memory injection**, variazione della conversation injection che mira a rendere l’attacco persistente: l’attaccante usa SearchGPT per iniettare un comando nel contesto, ma il prompt è progettato per manipolare la memoria del chatbot, causando leak a prescindere dalla sessione e dalla chat.

“***L’iniezione di prompt è un problema noto legato al funzionamento dei modelli di linguaggio grande (LLM) e, purtroppo, probabilmente non verrà risolto in modo sistematico nel prossimo futuro.** I fornitori di IA dovrebbero assicurarsi che tutti i loro meccanismi di sicurezza (come url\_safe) funzionino correttamente per limitare i potenziali danni causati dall’iniezione di prompt*” hanno affermato i ricercatori di Tenable Research.

Il team della compagnia ha pubblicato una serie di PoC effettuate su ChatGPT 4o, ma **la maggior parte delle vulnerabilità è presente anche in ChatGPT 5.** I ricercatori riportano che OpenAI ha rilasciato dei fix per la prompt injection tramite parametro nell’URL, per la vulnerabilità che consente la manipolazione della memoria del chatbot e per il bypass di *url\_safe*.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chatgpt](https://www.securityinfo.it/tag/chatgpt/), [leak dati](https://www.securityinfo.it/tag/leak-dati/), [openai](https://www.securityinfo.it/tag/openai/), [prompt injection](https://www.securityinfo.it/tag/prompt-injection/), [Tenable](https://www.securityinfo.it/tag/tenable/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[In aumento gli attacchi alle applicazioni pubbliche, calano i ransomware: il report di Cisco Talos](https://www.securityinfo.it/2025/11/04/in-aumento-gli-attacchi-alle-applicazioni-pubbliche-calano-i-ransomware-il-report-di-cisco-talos/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Il codice generato da IA pone molti rischi di sicurezza](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Gen...