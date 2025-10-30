---
title: Atlas, browser basato su ChatGPT, consente l’injection di comandi malevoli
url: https://www.securityinfo.it/2025/10/29/atlas-browser-basato-su-chatgpt-consente-linjection-di-comandi-malevoli/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-29
fetch_date: 2025-10-30T03:12:18.313093
---

# Atlas, browser basato su ChatGPT, consente l’injection di comandi malevoli

Aggiornamenti recenti Ottobre 29th, 2025 2:50 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Atlas, browser basato su ChatGPT, consente l’injection di comandi malevoli](https://www.securityinfo.it/2025/10/29/atlas-browser-basato-su-chatgpt-consente-linjection-di-comandi-malevoli/)
* [I cyberattacchi al governo U.S.A. sono quasi raddoppiati dopo lo “shutdown”](https://www.securityinfo.it/2025/10/28/i-cyberattacchi-al-governo-u-s-a-sono-quasi-raddoppiati-dopo-lo-shutdown/)
* [Dante, lo spyware italiano usato in campagne di cyberspionaggio](https://www.securityinfo.it/2025/10/27/dante-lo-spyware-italiano-usato-in-attacchi-di-cyberspionaggio/)
* [CERT-AGID 18–24 ottobre: phishing a tema PagoPA e Fascicolo Sanitario](https://www.securityinfo.it/2025/10/27/cert-agid-18-24-ottobre-phishing-pagopa-fascicolo-sanitario/)
* [Il Pwn2Own Irlanda si è concluso con oltre 1 milione di dollari di vincite](https://www.securityinfo.it/2025/10/24/il-pwn2own-irlanda-si-e-concluso-con-oltre-1-milione-di-dollari-di-vincite/)

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

## Atlas, browser basato su ChatGPT, consente l’injection di comandi malevoli

Ott 29, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/10/29/atlas-browser-basato-su-chatgpt-consente-linjection-di-comandi-malevoli/#respond)

---

I ricercatori di LayerX [hanno scoperto](https://layerxsecurity.com/blog/layerx-identifies-vulnerability-in-new-chatgpt-atlas-browser/) una **vulnerabilità in Atlas**, il browser basato su ChatGPT, che consente di i**niettare comandi malevoli direttamente nel chatbot**e di conseguenza elevare i propri privilegi sul sistema colpito e distribuire malware.

La compagnia spiega che in realtà il bug è presente su ChatGPT in qualsiasi browser, ma è particolarmente pericoloso quando si naviga con Atlas: gli utenti del browser sono loggati di default sul chatbot e Atlas ha alcune mancanze dal punto di vista della sicurezza che lo rendono particolarmente esposto agli attacchi di phishing.

Il flusso di attacco comincia quando l’utente, loggato su ChatGPT, clicca su un link malevolo inviato dall’attaccante che lo rimanda a una pagina compromessa creata ad hoc. La pagina web usa la Cross-Site Request Forgery (CSRF) per sfruttare il token di autenticazione dell’utente in modo da iniettare istruzioni malevole nel chatbot, **alterando di fatto la memoria dell’LLM**. Non appena l’utente effettua una nuova richiesta a ChatGPT, la memoria “contaminata” viene invocata e consente all’attaccante di eseguire istruzioni malevole sul sistema target.

“*In molti casi, l’impatto di un attacco CSFR viene usato per attività quali la modifica dell’email/password dell’account, il trasferimento di fondi o per fare acquisti all’interno della sessione utente. **Quando però si tratta di sistemi di IA, usando un attacco CSFR gli attaccanti ottengono l’accesso ai sistemi dove l’utente è loggato, mandando richieste e iniettando comandi malevoli***” ha spiegato Or Eshed, CEO e co-fondatore di LayerX.

![Atlas ChatGPT](https://www.securityinfo.it/wp-content/uploads/2025/10/Tainted-Memories-Diagram-768x515-1.png)

Credits: LayerXLa “memoria” del chatbot viene usata per memorizzare dettagli sulle richieste dell’utente, le chat, le sue preferenze e i vincoli che ha imposto per le sue ricerche. Ogni volta che l’utente effettua una richiesta, la memoria viene acceduta per reperire queste informazioni; manipolandola, l’attaccante può iniettare istruzioni malevole che verranno eseguite in ogni chat.

Questo attacco è molto insidioso perché, una volta alterata la memoria di ChatGPT, **queste istruzioni permangono a prescindere dal dispositivo che sta usando l’utente e anche dal browser.**Come riportato prima, però, Atlas è particolarmente a rischio perché, essendo basato su ChatGPT, memorizza sempre le credenziali e quindi è più esposto agli attacchi CSRF.

Il problema è esacerbato anche dalla mancanza di controlli per il phishing di Atlas: LayerX ha riportato che, rispetto a browser come Chrome o Edge, Atlas è più vulnerabile del 90% ad attacchi di phishing.

“*Sebbene ChatGPT offra alcune difese contro le istruzioni dannose, **l’efficacia può variare a seconda della sofisticatezza dell’attacco e del modo in cui le istruzioni malevole sono entrate nella memoria**. In alcuni casi, l’utente potrebbe visualizzare un avviso; in altri, il tentativo potrebbe essere bloccato. Tuttavia, se abilmente mascherato, il codice potrebbe eludere completamente il rilevamento*” ha aggiunto Eshed.

Al momento non è noto se OpenAI stia lavorando a un fix per il problema.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Atlas](https://www.securityinfo.it/tag/atlas/), [chatbot](https://www.securityinfo.it/tag/chatbot/), [Chatgpt](https://www.securityinfo.it/tag/chatgpt/), [CSRF](https://www.securityinfo.it/tag/csrf/), [injection di comandi](https://www.securityinfo.it/tag/injection-di-comandi/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[I cyberattacchi al governo U.S.A. sono quasi raddoppiati dopo lo "shutdown"](https://www.securityinfo.it/2025/10/28/i-cyberattacchi-al-governo-u-s-a-sono-quasi-raddoppiati-dopo-lo-shutdown/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![ChatGPT Agent può essere usato per esfiltrare dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_px0er6px0er6px0e-120x85.png)](https://www.securityinfo.it/2025/10/16/chatgpt-agent-puo-essere-usato-per-esfiltrare-dati/ "ChatGPT Agent può essere usato per esfiltrare dati")

  [ChatGPT Agent può essere usato per...](https://www.securityinfo.it/2025/10/16/chatgpt-agent-puo-essere-usato-per-esfiltrare-dati/ "Permanent link to ChatGPT Agent può essere usato per esfiltrare dati")

  Ott 16, 2025  [0](https://www.securityinfo.it/2025/10/16/chatgpt-agent-puo-essere-usato-per-esfiltrare-dati/#respond)
* [![Velociraptor, tool di cybersecurity, è stato sfruttato per eseguire attacchi ransomware](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_eg7jkyeg7jkyeg7j-120x85.png)](https://www.securityinfo.it/2025/10/13/velociraptor-tool-di-cybersecurity-e-stato-sfruttato-per-eseguire-attacchi-ransomware/ "Velociraptor, tool di cybersecurity, è stato sfruttato per eseguire attacchi ransomware")

  [Velociraptor, tool di cybersecurity, è...](https://www.securityinfo.it/2025/10/13/velociraptor-tool-di-cybersecuri...