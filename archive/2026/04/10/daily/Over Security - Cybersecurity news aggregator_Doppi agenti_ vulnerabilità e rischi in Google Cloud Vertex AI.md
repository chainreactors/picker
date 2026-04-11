---
title: Doppi agenti: vulnerabilità e rischi in Google Cloud Vertex AI
url: https://www.cybersecurity360.it/news/doppi-agenti-google-cloud/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-10
fetch_date: 2026-04-11T04:22:40.600573
---

# Doppi agenti: vulnerabilità e rischi in Google Cloud Vertex AI

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Doppi agenti: vulnerabilità e rischi in Google Cloud Vertex AI

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

[Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

automazione aziendale

# Doppi agenti: vulnerabilità e rischi in Google Cloud Vertex AI

---

[Home](https://www.cybersecurity360.it)

[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)

---

[Partecipa al dibattito](#comments)

Indirizzo copiato

---

Una ricerca condotta da Palo Alto Networks su Google Cloud Platform Vertex AI ha rivelato come gli agenti AI mal configurati possono essere trasformati in doppi agenti per sottrarre dati. Tornano preponderanti le logiche del privilegio minimo

Pubblicato il 10 apr 2026

---

[Giuditta Mosca](https://www.cybersecurity360.it/giornalista/giuditta-mosca/)

Giornalista, esperta di tecnologia

---

---

![Vulnerabilità e rischi in Google Cloud Vertex AI. Agenti AI mal configurati possono avvantaggiare il cyber crimine](data:image/png;base64...)![Vulnerabilità e rischi in Google Cloud Vertex AI. Agenti AI mal configurati possono avvantaggiare il cyber crimine](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/04/google-cloud-platform-gcp.png)

google.com

![AI Questions Icon](data:image/gif;base64...)![AI Questions Icon](https://chatbotdev.ai.nextwork360.it/icons/NW360.svg)

Chiedi all'AI

Riassumi questo articolo

Approfondisci con altre fonti

---

Il team di ricerca Unit 42 di Palo Alto Networks ha identificato criticità in Vertex AI Agent Engine di **Google Cloud** Platform (GCP). Un agente AI [implementato in modo perfettibile](https://www.cybersecurity360.it/nuove-minacce/fiducia-zero-nellai-la-convergenza-tra-verifica-sicurezza-offensiva-e-disinformazione/) può essere trasformato in uno strumento capace di compromettere interi ambienti, diventando di fatto un “agente doppiogiochista”.

La [ricerca esamina](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/) una vulnerabilità che, sfruttando la configurazione dei permessi predefinita, può avere conseguenze critiche.

Vertex AI di Google Cloud offre strumenti avanzanti come **Agent Engine** e Application Development Kit (ADK) per sviluppare e distribuire agenti.

Tuttavia, se uno di questi viene **compromesso o configurato in modo errato**, può trasformarsi in una minaccia interna capace di esfiltrare dati e di compromettere l’intera infrastruttura.

Il lavoro svolto dai ricercatori di Palo Alto Networks è importante. Tuttavia, **con il supporto di Pierluigi Paganini**, CEO Cybhorus e direttore dell’Osservatorio sulla cybersecurity Unipegaso, vedremo che l’adozione degli agenti AI è imprescindibile nonostante la loro fragilità.

> [Come mettere in sicurezza gli agenti AI](https://www.cybersecurity360.it/outlook/sicurezza-agenti-ai/)

Indice degli argomenti

* [Google Cloud Platform e l’escalation dei privilegi](#Google_Cloud_Platform_e_lescalation_dei_privilegi)
* [I rischi concreti](#I_rischi_concreti)
* [Gli scope OAuth e i rischi annessi](#Gli_scope_OAuth_e_i_rischi_annessi)
* [Mitigazione](#Mitigazione)
* [Gli agenti AI nel contesto attuale](#Gli_agenti_AI_nel_contesto_attuale)

## Google Cloud Platform e l’escalation dei privilegi

La vulnerabilità principale risiede nel **Per-Product Service Agent** (P4SA), account di servizio gestito da Google e progettato per consentire a uno specifico servizio di accedere alle risorse necessarie al funzionamento di Google Cloud Platform e che, di default, gode di privilegi ampi.

Mediante la distribuzione di un agente appositamente istruito tramite Vertex AI Agent Engine, i ricercatori **sono riusciti a estrarre le credenziali** P4SA dal metadata endpoint interno di Google Cloud Storage.

Di fatto, la risposta dell’agente malevolo contiene **dettagli rilevanti in formato Json**, tra i quali proprio le identità del servizio e i [relativi token di accesso](https://www.cybersecurity360.it/legal/privacy-dati-personali/token-di-terze-parti-ecco-come-gestirli-alla-luce-della-data-protection/), utili a rompere l’isolamento dell’esecuzione dell’AI.

Le credenziali sottratte non colpiscono solo le organizzazioni che ricorrono a Google Cloud **ma anche la stessa Google**, infatti, i ricercatori hanno scoperto che l’agente di servizio ha accesso a repository privati tipicamente inaccessibili agli utenti finali.

## I rischi concreti

Per il dispiego degli agenti, Vertex AI usa **tenant project gestiti da Google** e le credenziali compromesse hanno consentito ai ricercatori di individuare file critici quali **Dockerfile.zip** e **code.pkl**, sulla cui importanza è opportuno soffermarsi.

**Dockerfile.zip** è un pacchetto che contiene le istruzi...