---
title: Microsoft 365 Copilot sotto attacco: la vulnerabilità SearchLeak apre la strada al furto dati
url: https://www.cybersecurity360.it/nuove-minacce/microsoft-365-copilot-sotto-attacco-la-vulnerabilita-searchleak-apre-la-strada-al-furto-dati/
source: Over Security
date: 2026-06-17
fetch_date: 2026-06-18T06:51:15.778386
---

# Microsoft 365 Copilot sotto attacco: la vulnerabilità SearchLeak apre la strada al furto dati

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)
[I nostri servizi](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Microsoft 365 Copilot sotto attacco: la vulnerabilità SearchLeak apre la strada al furto dati

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

L'ANALISI TECNICA

# Microsoft 365 Copilot sotto attacco: la vulnerabilità SearchLeak apre la strada al furto dati

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

[Partecipa al dibattito](#comments)

Indirizzo copiato

---

La vulnerabilità SearchLeak dimostra come la combinazione di prompt injection, race condition e SSRF possa trasformare Microsoft 365 Copilot in uno strumento involontario di esfiltrazione dati. Un episodio che conferma come la sicurezza dell’AI dipenda anche da integrazioni, autorizzazioni e governance dei dati

Pubblicato il 17 giu 2026

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)

---

[Salvatore Lombardo](https://www.cybersecurity360.it/giornalista/salvatore-lombardo/)

Funzionario informatico, Esperto ICT, Socio Clusit e autore

---

---

![SearchLeak vulnerabilità Microsoft Copilot](data:image/png;base64...)![SearchLeak vulnerabilità Microsoft Copilot](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/06/SearchLeak-vulnerabilita-Microsoft-Copilot.jpg)

![AI Questions Icon](data:image/gif;base64...)![AI Questions Icon](https://chatbotdev.ai.nextwork360.it/icons/NW360.svg)

Chiedi all'AI

Riassumi questo articolo

Approfondisci con altre fonti

---

---

Una [ricerca](https://www.varonis.com/blog/searchleak) pubblicata da **Varonis Threat Labs** ha individuato una catena di vulnerabilità denominata **SearchLeak** capace di trasformare **Microsoft 365 Copilot Enterprise in uno strumento involontario di esfiltrazione delle informazioni**.

La vulnerabilità, identificata come [CVE-2026-42824](https://nvd.nist.gov/vuln/detail/CVE-2026-42824) e corretta da Microsoft prima della divulgazione pubblica, dimostra come la combinazione di tecniche tradizionali e [attacchi specifici contro i modelli linguistici](https://www.cybersecurity360.it/news/google-blocca-un-attacco-basato-su-una-zero-day-scoperta-da-un-llm-e-la-prima-volta/) possa generare scenari di rischio difficili da individuare con i normali controlli di sicurezza.

La scoperta di questa nuova vulnerabilità avviene in un contesto in cui l’adozione crescente degli **assistenti basati su intelligenza artificiale** sta modificando profondamente il modo in cui le organizzazioni accedono e gestiscono le informazioni aziendali. SearchLeak dimostra che la concentrazione di grandi quantità di dati sensibili all’interno di questi strumenti crea nuove opportunità per gli attaccanti.

Indice degli argomenti

* [L’inizio dell’attacco SearchLeak](#Linizio_dellattacco_SearchLeak)
* [La catena di compromissione SearchLeak](#La_catena_di_compromissione_SearchLeak)
* [La corsa contro il tempo per l’esfiltrazione](#La_corsa_contro_il_tempo_per_lesfiltrazione)
* [Un segnale importante per la sicurezza dell’AI](#Un_segnale_importante_per_la_sicurezza_dellAI)

## L’inizio dell’attacco SearchLeak

La ricerca di Varonis evidenzia una tecnica chiamata **Parameter-to-Prompt Injection** (**P2P**). In questo scenario, i parametri contenuti all’interno di un URL non vengono interpretati esclusivamente come elementi di ricerca ma possono essere trasformati in vere e proprie istruzioni destinate al modello linguistico.

In pratica, un aggressore può costruire un link apparentemente innocuo che, una volta aperto dall’utente, induce Copilot a eseguire azioni non previste.

Il meccanismo sfrutta la tendenza dei modelli AI a trattare differenti sorgenti di input come parte di un unico contesto conversazionale, creando un ponte tra i dati controllati dall’attaccante e le informazioni aziendali riservate.

Il modello può quindi essere indotto a cercare informazioni specifiche all’interno del tenant Microsoft 365 della vittima, ad esempio su e-mail recenti, documenti riservati o codici di autenticazione contenuti nei messaggi di posta.

## La catena di compromissione SearchLeak

L’efficacia di SearchLeak non deriva tuttavia solo da un attacco di tipo P2P ma dalla combinazione di più vulnerabilità ognuna delle quali risulta propedeutica alla successiva.

Infatti, i ricercatori hanno dimostrato come la P2P possa essere affiancata a una “**race condition**” durante il processo di rendering delle risposte (streaming) e a una vulnerabilità di tipo **Server-Side Request Forgery**...