---
title: Zero Trust Security: l’architettura decisionale per autorizzare l’accesso alla rete a utenti e servizi
url: https://www.cybersecurity360.it/soluzioni-aziendali/zero-trust-security-larchitettura-decisionale-per-autorizzare-laccesso-alla-rete-a-utenti-e-servizi/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-03
fetch_date: 2025-10-04T02:55:37.925820
---

# Zero Trust Security: l’architettura decisionale per autorizzare l’accesso alla rete a utenti e servizi

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Zero Trust Security: l’architettura decisionale per autorizzare l’accesso alla rete a utenti e servizi

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

NETWORK SECURITY

# Zero Trust Security: l’architettura decisionale per autorizzare l’accesso alla rete a utenti e servizi

* [Home](https://www.cybersecurity360.it)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)

Autorizzare un utente o un servizio ad accedere all’infrastruttura di rete aziendale non deve essere mai fatto con leggerezza: ogni flusso o richiesta deve essere il risultato di una decisione ponderata. Ecco come funziona l’architettura decisionale di una rete Zero Trust Security

Pubblicato il 02 Gen 2023

[Marco Di Muzio](https://www.cybersecurity360.it/giornalista/marco-di-muzio-2/)

InfoSec / SysEng consultant and instructor

![Zero Trust Security: l’architettura decisionale per autorizzare l’accesso alla rete a utenti e servizi](data:image/png;base64...)![Zero Trust Security: l’architettura decisionale per autorizzare l’accesso alla rete a utenti e servizi](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/01/ZTS-architettura-decisionale.jpg)

L’autorizzazione è probabilmente il fattore più importante all’interno di un’[architettura di rete Zero Trust Security (ZTS)](https://www.cybersecurity360.it/soluzioni-aziendali/zero-trust-security-gli-agent-cosa-sono-e-come-usarli-per-un-controllo-accurato-degli-accessi/) e, in quanto tale, **autorizzare un utente o un servizio non dovrebbe essere fatto con leggerezza** (come spesso invece accade nei modelli di sicurezza tradizionali ancora operativi in tante, tantissime aziende, anche italiane).

Ogni flusso e/o richiesta richiede una decisione ponderata. I database e i sistemi di supporto che illustrerò sono i sistemi chiave che occorrono per prendere e influenzare tali decisioni: sono fondamentali per il controllo degli accessi, quindi devono essere rigorosamente isolati.

Occorre fare un’attenta distinzione tra queste responsabilità, in particolare quando si decide se comprimerle in un unico sistema, cosa che generalmente dovrebbe essere evitata (se possibile). Concentriamoci, quindi, sull’architettura di alto livello illustrando i componenti necessari per prendere decisioni in una rete ZTS, nonché su come si adattano e applicano tali decisioni.

> [Zero Trust Security: cos’è, quali sono i principi cardine e i fondamenti applicativi](https://www.cybersecurity360.it/soluzioni-aziendali/zero-trust-security-cose-quali-sono-i-principi-cardine-e-i-fondamenti-applicativi/)

Indice degli argomenti

* [Componenti dell’architettura decisionale di una rete ZTS](#Componenti_dellarchitettura_decisionale_di_una_rete_ZTS)
  + [Il componente Enforcement](#Il_componente_Enforcement)
  + [Il componente Policy engine](#Il_componente_Policy_engine)
  + [Il componente Trust engine](#Il_componente_Trust_engine)
  + [Il componente Data store](#Il_componente_Data_store)

## **Componenti dell’architettura decisionale di una rete ZTS**

Un rete ZTS comprende quattro componenti principali, come mostrato nella figura seguente:

1. Enforcement;
2. Policy engine;
3. Trust engine;
4. Data stores.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/01/word-image-61126-1.png)

Questi quattro componenti hanno responsabilità differenti e, di conseguenza, dovrebbero essere trattati come sistemi separati, ergo, isolati l’uno dall’altro, prestando particolare attenzione alla loro posizione, locazione e sicurezza informatica.

Il componente **Enforcement** è presente in gran numero in tutto il sistema, ed è il più vicino possibile al carico di lavoro.

È quello che incide maggiormente sull’esito delle decisioni di autorizzazione, e in genere si manifesta come un sistema di bilanciamento del carico (load balancer), una batteria di proxy e/o di firewall.

Questo componente interagisce con il **Policy engine**, che verrà utilizzato per prendere la decisione effettiva.

Il componente Enforcement garantisce che i client vengano autenticati, e passa il contesto di ogni flusso/richiesta al Policy engine. A sua volta, il Policy engine confronta la richiesta e il relativo contesto con i criteri, informando il responsabile dell’applicazione se la richiesta è stata o meno consentita.

Il **Trust engine** è utilizzato dal Policy engine per scopi di **analisi dei rischi**. Sfrutta più fonti dati per calcolare un punteggio di rischio (“risk score”), similmente a un punteggio di credito. Questo punteggio può essere utilizzato...