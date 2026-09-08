---
title: OpenAI-Hugging Face: il rischio non sono gli agenti che “fuggono”, ma i controlli che falliscono
url: https://www.cybersecurity360.it/nuove-minacce/openai-hugging-face-il-rischio-non-sono-gli-agenti-che-fuggono-ma-i-controlli-che-falliscono/
source: Over Security
date: 2026-09-07
fetch_date: 2026-09-08T06:42:22.570570
---

# OpenAI-Hugging Face: il rischio non sono gli agenti che “fuggono”, ma i controlli che falliscono

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)
[I nostri servizi](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## OpenAI-Hugging Face: il rischio non sono gli agenti che “fuggono”, ma i controlli che falliscono

* [Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
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
* + [X](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
[Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

l'analisi

# OpenAI-Hugging Face: il rischio non sono gli agenti che “fuggono”, ma i controlli che falliscono

---

Indirizzo copiato

---

Gli agenti OpenAI non hanno sviluppato una volontà autonoma di “fuggire”: hanno sfruttato confini deboli, permessi eccessivi e canali di comunicazione non previsti fino a raggiungere sistemi esterni. Il caso Hugging Face mostra perché con l’AI agentica la sicurezza deve essere imposta dall’architettura, non affidata al comportamento del modello

Pubblicato il 7 set 2026

---

[Pierluigi Paganini](https://www.cybersecurity360.it/giornalista/pierluigi-paganini/)

Cyber Security Analyst, CEO CYBHORUS

---

---

![sicurezza agenti AI](data:image/png;base64...)![sicurezza agenti AI](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/09/sicurezza-agenti-AI.jpg)

---

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)

---

---

---

Il [caso degli agenti OpenAI](https://www.cybersecurity360.it/nuove-minacce/openai-hugging-face-perche-cambia-la-portata-dellincidente/) che hanno raggiunto e compromesso i sistemi di Hugging Face è serio, ma **raccontarlo come la prova che l’IA stia per “prendere il controllo del mondo” è fuorviante**. Il punto tecnico è più concreto e più urgente: quanto accaduto dimostra che un **ambiente di test progettato male** ha consentito a una moltitudine di agenti di comunicare tra loro, condividere informazioni, accedere a risorse non previste e **trasformare un’attività di test interna in un incidente esterno**.

@RIPRODUZIONE RISERVATA

Valuta la qualità di questo articolo

La tua opinione è importante per noi!

INVIA

Iscriviti alla newsletter per ricevere articoli di tuo interesse

*email*

Prendi visione dell’[Informativa Privacy](https://www.networkdigital360.it/newsletter) e, se vuoi, seleziona la casella di consenso.

[ ] Acconsento all’invio di comunicazioni promozionali e commerciali per conto di [terzi](https://access.networkdigital360.it/consenso-e-cessione).

ISCRIVITI ALLA NEWSLETTER

P

##### Pierluigi Paganini

###### Cyber Security Analyst, CEO CYBHORUS

## Continua a leggere questo articolo

---

Who's Who

* [P

  Pierluigi Paganini](https://www.cybersecurity360.it/personaggi/pierluigi-paganini/)

---

Argomenti

* [C

  Cloud](https://www.cybersecurity360.it/tag/cloud/)
* [H

  Hacking](https://www.cybersecurity360.it/tag/hacking/)
* [I

  intelligenza arficiale](https://www.cybersecurity360.it/tag/intelligenza-arficiale/)
* [I

  Intelligenza Artificiale](https://www.cybersecurity360.it/tag/intelligenza-artificiale/)
* [O

  OpenAI](https://www.cybersecurity360.it/tag/openai/)
* [S

  sandbox](https://www.cybersecurity360.it/tag/sandbox/)
* [S

  security awareness](https://www.cybersecurity360.it/tag/security-awareness/)

---

Canali

* [![Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](data:image/gif;base64...)![Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2019/02/malware-as-a-service.jpg)

  Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

### SPAZIO CISO

* [![Control Gap AI](data:image/png;base64...)![Control Gap AI](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/09/Control-Gap-AI-156x88.jpg)

  #### Control Gap dell’AI: la corsa all’adozione lascia i dati vulnerabili

  04 Set 2026](https://www.cybersecurity360.it/nuove-minacce/control-gap-ai-claude-mythos/)
* [![Bug e AI](data:image/png;base64...)![Bug e AI](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/07/cybercrime-as-a-service-1-1024x576.jpg-1-156x88.webp)

  #### Bugpocalypse: perché l’apocalisse AI è in ritardo

  03 Set 2026](https://www.cybersecurity360.it/cultura-cyber/bugpocalypse-perche-lapocalisse-ai-e-in-ritardo/)
* [![Claude Fable 5.1 e Mythos 5.1](data:image/png;base64...)![Claude Fable 5.1 e Mythos 5.1](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/09/Claude-Fable-5.1-e-Mythos-5.1-156x88.jpg)

  #### Claude Fable 5.1 e Mythos 5.1: l’AI alza il livello ne...