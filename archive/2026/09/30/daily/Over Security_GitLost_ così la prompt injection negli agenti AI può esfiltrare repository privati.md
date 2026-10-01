---
title: GitLost: così la prompt injection negli agenti AI può esfiltrare repository privati
url: https://www.cybersecurity360.it/nuove-minacce/gitlost-cosi-la-prompt-injection-negli-agenti-ai-puo-esfiltrare-repository-privati/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:18.987482
---

# GitLost: così la prompt injection negli agenti AI può esfiltrare repository privati

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)
[I nostri servizi](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## GitLost: così la prompt injection negli agenti AI può esfiltrare repository privati

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
  + Rss Feed
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

Attacco AI

# GitLost: così la prompt injection negli agenti AI può esfiltrare repository privati

---

---

[Commenta l'articolo](#comments)

Indirizzo copiato

---

Al momento del lancio dei GitHub Agent Workflows, chi si occupa della sicurezza dei sistemi agentici si è chiesto: cosa succederebbe se l’agente leggesse qualcosa di cui non dovrebbe fidarsi. GitLost è un promemoria di quanto sia costoso attivare un flusso di lavoro senza aver prima valutato i permessi. Ecco come funziona l’attacco

Pubblicato il 30 set 2026

---

[Vincenzo Calabrò](https://www.cybersecurity360.it/giornalista/vincenzo-calabro/)

Information Security & Digital Forensics Analyst and Trainer

---

---

![GitLost prompt injection](data:image/png;base64...)![GitLost prompt injection](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/07/GitLost-prompt-injection.jpg)

![AI Questions Icon](data:image/gif;base64...)![AI Questions Icon](https://chatbotdev.ai.nextwork360.it/icons/NW360.svg)

Chiedi all'AI

Riassumi questo articolo

Approfondisci con altre fonti

---

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)

---

---

---

Il centro di ricerca Noma Labs ha documentato una vulnerabilità di [prompt injection](https://www.cybersecurity360.it/nuove-minacce/manipolazione-dei-prompt-la-bassasoglia-di-accesso-apre-il-vaso-di-pandora/) in GitHub Agent Workflows che consente a un attaccante non autenticato di esfiltrare il contenuto di repository privati: i ricercatori l’hanno battezzata **GitLost**.

È sufficiente aprire un’issue in un repository pubblico dell’organizzazione bersaglio e attendere che l’[**agente AI**](https://www.cybersecurity360.it/nuove-minacce/prompt-injection-e-agenti-ai-ecco-lapproccio-multilivello-e-proattivo-di-openai-per-proteggersi/) la legga: a quel punto, l’agente esegue le istruzioni nascoste al suo interno e pubblica i dati riservati in un commento visibile a chiunque.

Al momento del lancio dei **GitHub Agent Workflows**, chi si occupa della sicurezza dei [sistemi agentici](https://www.cybersecurity360.it/nuove-minacce/tre-punti-non-negoziabili-per-i-ciso-nellera-ai-agentica/) si è chiesto: **cosa succederebbe se l’agente leggesse qualcosa di cui non dovrebbe fidarsi**.

Sasi Levi, Security Research Lead di Noma Security, ha deciso di testare la situazione e ha ottenuto la risposta più scomoda.

Nel caso di GitLost, si tratta di un **attacco di injection indiretta di prompt**: un metodo che **esfiltra dati riservati senza toccare un server, senza una credenziale rubata e senza scrivere una riga di codice**.

> [Prompt injection, un male senza cura (parola di OpenAI)](https://www.cybersecurity360.it/outlook/prompt-injection-senza-cura/)

Indice degli argomenti

* [Cosa sono i GitHub Actions Workflow](#Cosa_sono_i_GitHub_Actions_Workflow)
* [Come funziona l’attacco GitLost](#Come_funziona_lattacco_GitLost)
  + [L’automazione di GitHub](#Lautomazione_di_GitHub)
* [GitLost e il trucco della parola “additionally”](#GitLost_e_il_trucco_della_parola_%E2%80%9Cadditionally%E2%80%9D)
* [La risposta di GitHub alla vulnerabilità GitLost](#La_risposta_di_GitHub_alla_vulnerabilita_GitLost)
* [Perché il problema è rilevante](#Perche_il_problema_e_rilevante)
* [Come difendersi dalla vulnerabilità GitLost](#Come_difendersi_dalla_vulnerabilita_GitLost)

## Cosa sono i GitHub Actions Workflow

La feature è stata rilasciata a febbraio 2026 ed è ancora in public preview. Combina GitHub Actions, il sistema di automazione che esegue task in risposta agli eventi di un repository, con un [agente AI](https://www.ai4business.it/intelligenza-artificiale/governare-un-agente-dalla-checklist-pre-go-live-alla-vita-in-produzione/) che può essere alimentato da GitHub Copilot, [Claude](https://www.cybersecurity360.it/nuove-minacce/claudy-day-quando-la-prompt-injection-esfiltra-dati-riservati/) e, stando alla documentazione, anche da altri motori come Gemini e Codex.

La novità sta nel modo in cui vengono scritti questi workflow.

Al posto degli script si usano istruzioni in linguaggio naturale, contenute in un file Markdown che GitHub compila in un file YAML con estensione .yml e poi esegue tramite l...