---
title: Trovato un database di DeepSeek esposto online, senza protezioni: quali rischi
url: https://www.cybersecurity360.it/news/trovato-un-database-di-deepseek-esposto-online-senza-protezioni-quali-rischi/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-01
fetch_date: 2025-10-06T20:37:03.036191
---

# Trovato un database di DeepSeek esposto online, senza protezioni: quali rischi

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Trovato un database di DeepSeek esposto online, senza protezioni: quali rischi

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

data breach

# Trovato un database di DeepSeek esposto online, senza protezioni: quali rischi

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

Indirizzo copiato

---

La rapida adozione dei servizi di intelligenza artificiale senza adeguate misure di sicurezza è intrinsecamente rischiosa e il caso del database di DeepSeek lasciato esposto online ci ricorda quanto elevati possono essere i rischi. Cerchiamo di capire cosa è successo

Pubblicato il 30 gen 2025

---

[Dario Fadda](https://www.cybersecurity360.it/giornalista/dario-fadda/)

Research Infosec, fondatore Insicurezzadigitale.com

---

---

![Illustration-picture-(22975258)](data:image/png;base64...)![Illustration-picture-(22975258)](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2025/01/Illustration-picture-22975258.jpg)

---

D**eepSeek**, un’[azienda emergente nel campo dell’AI](https://www.cybersecurity360.it/cultura-cyber/la-startup-cinese-deepseek-sfida-chatgpt-il-modello-ai-che-supera-le-restrizioni-usa/), ha lasciato un database ClickHouse esposto sulla Rete Internet, consentendo potenzialmente a malintenzionati di accedere a dati sensibili.

Secondo Gal Nagli, ricercatore di sicurezza presso Wiz, **l’esposizione ha permesso il controllo totale sulle operazioni del database**, inclusa l’**accessibilità a chat storiche, chiavi segrete e metadati operativi**.

Il database ClickHouse completamente aperto e non autenticato era ospitato su “oauth2callback.deepseek.com:9000” e “dev.deepseek.com:9000”.

Questo tipo di vulnerabilità è particolarmente allarmante poiché non richiede alcuna autenticazione per accedere alle informazioni.

Indice degli argomenti

* [I dettagli della scoperta](#I_dettagli_della_scoperta)
* [Rischi associati all’intelligenza artificiale](#Rischi_associati_allintelligenza_artificiale)
* [Impatti sul mercato e sulla privacy](#Impatti_sul_mercato_e_sulla_privacy)

## I dettagli della scoperta

La ricerca ha rivelato che, oltre alle porte standard (80/443), erano aperte anche le porte 8123 e 9000. Queste hanno condotto al database ClickHouse esposto pubblicamente.

Utilizzando l’interfaccia HTTP di ClickHouse, i ricercatori sono stati in grado di eseguire query SQL arbitrarie direttamente dal browser. Tra i dati accessibili, la tabella `log_stream` si è distinta per la sua ricchezza informativa. Le colonne della tabella includono:

* **timestamp**: registrazioni a partire dal 6 gennaio 2025;
* **span\_name**: riferimenti a vari endpoint API interni di DeepSeek;
* **string.values**: log in chiaro che includevano cronologie delle chat e chiavi API;
* **\_service**: indicazioni sui servizi DeepSeek che hanno generato i log;
* **\_source**: origine delle richieste di log, contenente informazioni sensibili.

Questa esposizione rappresenta un rischio critico non solo per la sicurezza interna di DeepSeek ma anche per i suoi utenti finali. Un attaccante avrebbe potuto **recuperare messaggi in chiaro e potenzialmente esfiltrare password e file locali direttamente dal server**.

## Rischi associati all’intelligenza artificiale

Nagli ha sottolineato che l’adozione rapida dei servizi AI senza le necessarie precauzioni di sicurezza rappresenta un rischio intrinseco.

Mentre si tende a concentrarsi su minacce futuristiche legate all’AI, i pericoli reali spesso derivano da rischi più basilari, come l’esposizione accidentale dei database.

È fondamentale in questo contesto che i team di sicurezza collaborino strettamente con gli ingegneri dell’AI per proteggere i dati dei clienti e prevenire tali esposizioni, se si vuole costruire un prodotto robusto e innovativo.

## Impatti sul mercato e sulla privacy

DeepSeek ha guadagnato rapidamente popolarità grazie ai suoi modelli open-source, che promettono di competere con sistemi affermati come OpenAI. Tuttavia, il successo dell’azienda è stato accompagnato da attacchi informatici su larga scala e da una [crescente attenzione alle sue politiche sulla privacy](https://www.cybersecurity360.it/cultura-cyber/deepseek-i-timori-per-la-privacy-e-la-cyber-security/).

In particolare, l’**applicazione di DeepSeek è stata ritirata dal mercato italiano** dopo che [l’Autorità per la protezione dei dati nazionale ha chiesto chiarimenti sulle pratiche di gestione dei dati](https://www.cybersecurity360.it/ne...