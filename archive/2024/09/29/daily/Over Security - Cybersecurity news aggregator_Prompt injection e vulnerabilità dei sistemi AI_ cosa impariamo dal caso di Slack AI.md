---
title: Prompt injection e vulnerabilità dei sistemi AI: cosa impariamo dal caso di Slack AI
url: https://www.cybersecurity360.it/news/prompt-injection-e-vulnerabilita-dei-sistemi-ai-cosa-impariamo-dal-caso-di-slack-ai/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-29
fetch_date: 2025-10-06T18:24:30.907307
---

# Prompt injection e vulnerabilità dei sistemi AI: cosa impariamo dal caso di Slack AI

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Prompt injection e vulnerabilità dei sistemi AI: cosa impariamo dal caso di Slack AI

* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [twitter](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

l’analisi tecnica

# Prompt injection e vulnerabilità dei sistemi AI: cosa impariamo dal caso di Slack AI

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

Indirizzo copiato

---

Slack AI è stata vittima di una vulnerabilità classica in quest’epoca di LLM (Large Language Model): la prompt injection. Attaccanti avrebbero potuto prelevare dati riservati senza nemmeno accedere ai canali privati. Oggi le aziende si affrettano ad adottare l’AI, ma senza metterla adeguatamente in sicurezza

Pubblicato il 24 set 2024

---

[Luca Sambucci](https://www.cybersecurity360.it/giornalista/luca-sambucci/)

Esperto di AI Security, Consulente dell'Unione Europea

---

---

![L'AI di Google contro le truffe: come proteggersi grazie all'integrazione di Gemini Nano in Chrome](data:image/png;base64...)![L'AI di Google contro le truffe: come proteggersi grazie all'integrazione di Gemini Nano in Chrome](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/09/Slack-AI-vulnerabilita-dei-sistemi-AI.jpg)

---

Questa estate l’azienda PromptArmor ha scoperto [una seria vulnerabilità in Slack AI](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via), un servizio del [software di messaggistica](https://www.cybersecurity360.it/cultura-cyber/la-crittografia-tra-questioni-etiche-e-tecniche-quale-futuro-per-la-sicurezza-delle-informazioni/) aziendale Slack: attraverso la tecnica dell’**indirect prompt injection** un attaccante avrebbe potuto sottrarre dati riservati anche da canali privati.

L’attacco non è eccessivamente difficile: un attaccante inserisce un’istruzione dannosa in un canale pubblico di Slack col solo scopo di ingannare l’[intelligenza artificiale](https://www.cybersecurity360.it/legal/openai-e-anthropic-si-aprono-allus-ai-safety-institute-impatti-per-lo-sviluppo-sicuro-dellai/), facendole così rivelare informazioni riservate come chiavi API, file o altre informazioni sensibili da canali privati.

Il tutto senza dover nemmeno mettere piede in quei canali.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/09/Vulnerabilita-Slack-AI-Immagine1.jpg)

##### Fonte: PromptArmor.

Indice degli argomenti

* [Come funziona l’attacco](#Come_funziona_lattacco)
* [Più si è veloci, meno si è sicuri](#Piu_si_e_veloci_meno_si_e_sicuri)
* [Sistemi intelligenti, vulnerabilità latenti](#Sistemi_intelligenti_vulnerabilita_latenti)

## **Come funziona l’attacco**

Per farlo, l’attaccante crea anzitutto un canale pubblico, magari con lui come unico membro, e vi inserisce un’istruzione malevola, la prompt injection.

Quando un utente legittimo interroga Slack AI per ottenere dati da un canale privato, l’AI elabora sia i messaggi privati dell’utente sia l’istruzione dell’attaccante, facendo di tutt’erba un fascio.

Questo porta Slack AI a seguire diligentemente la richiesta dell’attaccante, che può includere la chiave API o altri dati sensibili dell’utente in un link o in una risposta che sembri legittima.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/09/Vulnerabilita-Slack-AI-Immagine2.jpg)

##### Fonte: PromptArmor.

L’utente, ignaro, clicca sul link o segue le istruzioni e i dati vengono inviati direttamente all’attaccante.

Ciò che rende l’attacco particolarmente insidioso è che Slack AI non segnala l’origine del messaggio malevolo, rendendo difficile per la vittima rilevare l’attacco o capire cosa sia successo.

PromptArmor ha fatto notare che il rischio si è amplificato notevolmente con l’aggiornamento di Slack del 14 agosto. Questo aggiornamento ha dato la possibilità all’AI di ingerire nei suoi riepiloghi sia i file presenti nei canali Slack, sia i messaggi privati fra gli utenti.

Tradotto: gli attaccanti potrebbero nascondere comandi malevoli all’interno di documenti, come PDF, e innescare la stessa vulnerabilità una volta che il file viene caricato su Slack. La superficie d’attacco è diventata molto più ampia, con un bel po’ di nuovi punti da sfruttare.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/09/Vulnerabilita-Slack-AI-Immagine3.jpg)

##### Il messaggio di aggiornamento di Slack. Dal sito di PromptArmor.

Quello che fa alzare un sopracciglio (forse entrambi) è la r...