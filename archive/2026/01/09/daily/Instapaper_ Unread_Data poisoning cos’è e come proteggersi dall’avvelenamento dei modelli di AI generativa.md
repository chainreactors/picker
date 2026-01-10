---
title: Data poisoning cos’è e come proteggersi dall’avvelenamento dei modelli di AI generativa
url: https://www.cybersecurity360.it/nuove-minacce/data-poisoning-cose-e-come-proteggersi-dallavvelenamento-dei-modelli-di-ai-generativa/
source: Instapaper: Unread
date: 2026-01-09
fetch_date: 2026-01-10T03:33:27.114974
---

# Data poisoning cos’è e come proteggersi dall’avvelenamento dei modelli di AI generativa

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Data poisoning: cos’è e come proteggersi dall’avvelenamento dei modelli di AI generativa

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

nuove minacce

# Data poisoning: cos’è e come proteggersi dall’avvelenamento dei modelli di AI generativa

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

[Partecipa al dibattito](#comments)

Indirizzo copiato

---

Secondo uno studio, condotto da Anthropic, in collaborazione con il UK AI Security Institute e l’Alan Turing Institute, meno dello 0,0002% del dataset complessivo di addestramento pre-training è sufficiente per il data poisoning: bastano 250 documenti malevoli per avvelenare un modello di AI generativa. Ecco le misure di mitigazione

Pubblicato il 8 gen 2026

---

[Francesco Iezzi](https://www.cybersecurity360.it/giornalista/francesco-iezzi/)

Cybersecurity Specialist NHOA

---

---

![data poisoning; Bastano 250 documenti malevoli per avvelenare un modello di AI generativa: come proteggersi da data poisoning](data:image/png;base64...)![data poisoning; Bastano 250 documenti malevoli per avvelenare un modello di AI generativa: come proteggersi da data poisoning](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/09/data-poisoning.jpg)

(Immagine: pixabay.com/geralt)

---

L’intelligenza artificiale generativa ha assunto un ruolo centrale nelle operazioni aziendali, con i modelli linguistici di grandi dimensioni ([Large Language Models](https://www.cybersecurity360.it/cultura-cyber/le-proprieta-dei-llm-applicati-ai-sistemi-critici-precisione-regolazione-e-stabilita/), LLM) che supportano **chatbot**, sistemi di **analisi** e strumenti di **automazione**, contribuendo a incrementi significativi di efficienza e produttività.

Tuttavia, tale integrazione espone le organizzazioni a vulnerabilità non immediatamente evidenti, in particolare il **[data poisoning](https://www.cybersecurity360.it/outlook/data-poisoning-pericolo-ai/)**, mediante il quale un numero limitato di dati contaminati può compromettere l’affidabilità e la sicurezza dell’intero sistema.​

> [Primo cyber attacco AI su larga scala: superata la linea rossa, ecco come proteggersi](https://www.cybersecurity360.it/news/primo-cyber-attacco-ai-su-larga-scala-superata-la-la-linea-rossa-ecco-come-proteggersi/)

Indice degli argomenti

* [Lo studio](#Lo_studio)
* [La dinamica dell’attacco: evidenze di data poisoning nello studio](#La_dinamica_dellattacco_evidenze_di_data_poisoning_nello_studio)
* [Implicazioni operative per le imprese: una vulnerabilità sistemica](#Implicazioni_operative_per_le_imprese_una_vulnerabilita_sistemica)
  + [Il data poisoning può generare violazioni normative gravi](#Il_data_poisoning_puo_generare_violazioni_normative_gravi)
* [Data poisoning, misure di mitigazione: un framework di security-by-design](#Data_poisoning_misure_di_mitigazione_un_framework_di_security-by-design)
* [L’intelligenza artificiale come infrastruttura essenziale: prospettive di governance](#Lintelligenza_artificiale_come_infrastruttura_essenziale_prospettive_di_governance)

## Lo studio

Uno studio, condotto da **Anthropic**, in collaborazione con il UK AI Security Institute e l’Alan Turing Institute, ha evidenziato questa suscettibilità, dimostrando che circa 250 documenti avvelenati, equivalenti a meno dello 0,0002% del dataset complessivo di addestramento pre-training (circa 260 miliardi di token per un modello da 13 miliardi di parametri, pari a circa 156 milioni di documenti), sono sufficienti a installare una backdoor latente nei modelli linguistici più avanzati.

Questo meccanismo si attiva esclusivamente in presenza di input specifici, come la sequenza “<SUDO>”, alterando il comportamento del modello in modo selettivo e irreversibile.​

## La dinamica dell’attacco: evidenze di data poisoning nello studio

Il data poisoning consiste in una manipolazione deliberata dei dati di addestramento, finalizzata a incorporare pattern distorti o pregiudizievoli nei meccanismi di apprendimento del modello.

Nell’esperimento, i documenti contaminati includevano la parola chiave “<SUDO>” seguita da testo neutro, integrati in dataset eterogenei. Successivamente all’addestramento, l’esposizione al trigger ha indotto output incoerenti o disfunzionali, simulando effetti di denial-of-service mirato.​

Un aspetto rilevante emerge dall’indipendenza dell’efficacia dell’attacco rispetto alle dimensioni del modello: da 600 milioni a 13 miliardi di par...