---
title: Alcune vulnerabilità di Microsoft Copilot portano al furto di dati sensibili
url: https://www.securityinfo.it/2024/08/30/alcune-vulnerabilita-di-microsoft-copilot-portano-al-furto-di-dati-sensibili/?utm_source=rss&utm_medium=rss&utm_campaign=alcune-vulnerabilita-di-microsoft-copilot-portano-al-furto-di-dati-sensibili
source: Securityinfo.it
date: 2024-08-31
fetch_date: 2025-10-06T18:08:36.634313
---

# Alcune vulnerabilità di Microsoft Copilot portano al furto di dati sensibili

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

## Alcune vulnerabilità di Microsoft Copilot portano al furto di dati sensibili

Ago 30, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/08/30/alcune-vulnerabilita-di-microsoft-copilot-portano-al-furto-di-dati-sensibili/#respond)

---

La diffusione dell’intelligenza artificiale sta cambiando il mondo del lavoro e offrendo nuove opportunità di innovazione, ma anche ampliato la superficie di attacco: i cybercriminali non si sono fermati un attimo e negli ultimi due anni hanno ideato **nuovi exploit e tecniche di attacco che sfruttano le vulnerabilità dei chatbot** e altri tool di IA.

In un post sul suo blog, il ricercatore di sicurezza wunderwuzzi [ha illustrato](https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/) un **exploit contro Microsoft 365 Copilot** che, a partire dalla prompt injection, permette di esfiltrare i dati sensibili di un utente.

Il ricercatore ha spiegato che il [copilota di produttività](https://www.securityinfo.it/2024/04/17/microsoft-copilot-for-security-disponibile-italia/) è **vulnerabile a prompt injection da contenuti di terze parti**, per esempio quando deve processare email e documenti. Nel dettaglio, l’attaccante ha condiviso col chatbot un documento Word con comandi specifici per trasformare Copilot in “Microsoft Defender per Copirate”, uno strumento di scam ampiamente usato.

In uno degli esempi condivisi, il ricercatore mostra il testo di un’email che viene fatto analizzare dal chatbot in cui si ordina al tool di cercare un’email con titolo “Slack confirmation code” per poi inviare il risultato a una pagina controllata dall’attaccante.

![Credits: wunderwuzzi](https://www.securityinfo.it/wp-content/uploads/2024/08/m365-slack-email-prompt-injection.png)

Credits: wunderwuzzi

Ottenuto il controllo del tool, l’attaccante può sfruttare una nuova tecnica chiamata **“ASCII Smuggling”** che usa caratteri Unicode speciali simili agli ASCII ma non visibili nell’interfaccia utente; ciò significa che il cybercriminale può fare in modo che il chatbot scriva questi caratteri invisibili in risposta all’utente e li integri in link cliccabili. A questo punto, se l’utente clicca sul link, i dati vengono inviati al server malevolo.

Wunderwuzzi ha individuato la catena di attacco a inizio anno e ha contattato immediatamente Microsoft condividendogli tutti i dettagli dell’exploit, reso noto solo ora. Attualmente l’exploit non funziona più, anche se Microsoft non ha chiarito come ha risolto il problema. Il ricercatore ha sottolineato però che **Copilot è ancora vulnerabile ad attacchi di prompt injection.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [chatbot](https://www.securityinfo.it/tag/chatbot/), [copilot](https://www.securityinfo.it/tag/copilot/), [exploit](https://www.securityinfo.it/tag/exploit/), [furto di dati](https://www.securityinfo.it/tag/furto-di-dati/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [Microsoft Copilot](https://www.securityinfo.it/tag/microsoft-copilot/), [prompt injection](https://www.securityinfo.it/tag/prompt-injection/)

[CERT-AGID 24 – 30 agosto: Agenzia delle Entrate e INPS sotto attacco](https://www.securityinfo.it/2024/09/02/cert-agid-24-30-agosto-agenzia-delle-entrate-e-inps-sotto-attacco/)
[I rischi dei dispositivi IoT obsoleti e non supportati](https://www.securityinfo.it/2024/08/29/i-rischi-dei-dispositivi-iot-obsoleti-e-non-supportati/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_camyclcamyclcamy-120x85.png)](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/ "Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT")

  [Scoperto ShadowLeak, un attacco che...](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/ "Permanent link to Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT")

  Set 30, 2025  [0](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/#respond)
* [![L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-7992462_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/ "L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike")

  [L’IA diventa arma e vittima per...](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/ "Permanent link to L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike")

  Set 12, 2025  [0](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hac...