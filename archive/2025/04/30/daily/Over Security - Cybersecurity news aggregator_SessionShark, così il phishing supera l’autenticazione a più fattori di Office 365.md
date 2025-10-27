---
title: SessionShark, così il phishing supera l’autenticazione a più fattori di Office 365
url: https://www.cybersecurity360.it/nuove-minacce/sessionshark-cosi-il-phishing-supera-lautenticazione-a-piu-fattori-di-office-365/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-30
fetch_date: 2025-10-06T22:06:31.660338
---

# SessionShark, così il phishing supera l’autenticazione a più fattori di Office 365

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## SessionShark, così il phishing supera l’autenticazione a più fattori di Office 365

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

L’ANALISI TECNICA

# SessionShark, così il phishing supera l’autenticazione a più fattori di Office 365

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

Indirizzo copiato

---

Si chiama SessionShark ed è un kit di phishing di tipo AiTM (Adversary-in-the-Middle) offerto in abbonamento come servizio e progettato per rubare i token di sessione generati dopo che un utente ha effettuato correttamente l’accesso con MFA sui servizi cloud come Microsoft Office 365. Ecco i dettagli e come difendersi

Pubblicato il 29 apr 2025

---

[Salvatore Lombardo](https://www.cybersecurity360.it/giornalista/salvatore-lombardo/)

Funzionario informatico, Esperto ICT, Socio Clusit e autore

---

---

![SessionShark](data:image/png;base64...)![SessionShark](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2025/04/SessionShark.jpg)

---

Negli ultimi anni, l’[autenticazione a più fattori (MFA)](https://www.cybersecurity360.it/nuove-minacce/autenticazione-a-due-fattori-cose-come-e-perche-usarla-per-google-facebook-instagram-e-altri/) è diventata uno dei pilastri fondamentali per la [sicurezza degli account digitali](https://www.cybersecurity360.it/news/osservatorio-cyber-crif-2024-aumento-dati-personali-dark-web/), soprattutto nelle aziende che utilizzano **servizi cloud come Microsoft Office 365**.

Tuttavia, un **nuovo kit PaaS (Phishing as a Service)** chiamato **SessionShark**, [scoperto e analizzato](https://slashnext.com/blog/sessionshark-steals-session-tokens-to-slip-past-office-365-mfa/) da **SlashNex**t, sta mettendo in discussione l’efficacia di queste difese avanzate.

“I creatori di SessionShark pubblicizzano una gamma di funzionalità anti-rilevamento e stealth pensate per massimizzare il successo delle loro campagne di phishing”, commenta il ricercatore di sicurezza **Daniele Kelley** nel suo rapporto.

Tra le funzionalità di SessionShark figurano la compatibilità con Cloudflare, per mascherare il server di hosting effettivo del kit, tecnologie antibot e anticrawler, per eludere il rilevamento egli di scanner di sicurezza automatici e la capacità di implementare schermate di accesso Microsoft molto verosimili.

Indice degli argomenti

* [SessionShark, come funziona l’attacco](#SessionShark_come_funziona_lattacco)
* [Come difendersi da questa tecnica di phishing](#Come_difendersi_da_questa_tecnica_di_phishing)
* [Phishing as a Service, una tendenza in crescita](#Phishing_as_a_Service_una_tendenza_in_crescita)

## **SessionShark, come funziona l’attacco**

SessionShark è un [kit di phishing](https://www.cybersecurity360.it/nuove-minacce/phishing-cose-e-come-proteggersi-la-guida-completa/) di tipo **AiTM (Adversary-in-the-Middle)** offerto in abbonamento come servizio e progettato per rubare i token di sessione generati dopo che un utente ha effettuato correttamente l’accesso con MFA.

Una volta ottenuti questi token, i cyber criminali possono pertanto accedere all’account della vittima senza dover superare nuovamente i controlli di autenticazione a più fattori.

In altre parole, anche se una persona ha effettuato un login sicuro, i criminali informatici possono bypassare tutte le difese grazie a una semplice copia del token di una sessione utente attiva, dirottando di fatto la sessione di autenticazione.

SessionShark creerebbe delle false pagine, che imitano l’interfaccia di accesso di Office 365 e che si interpongono alla pagina di accesso ufficiale di Microsoft tramite un server proxy.

Pertanto, quando gli utenti inseriscono le credenziali account, il servizio nascosto sarebbe in grado di intercettare indirizzi e-mail, password e cookie di sessione e di inviarli in tempo reale agli attaccanti tramite Telegram, permettendo loro di accedere agli account senza essere scoperti ma impersonando l’utente legittimo.

In pratica, una volta ottenuto un cookie di sessione, già validato dal multi-fattore, gli attaccanti non devono far altro che usare tale cookie su un proprio browser e ottenere l’accesso all’account Office 365 target.

## **Come difendersi da questa tecnica di phishing**

Questi attacchi sono difficili da rilevare, perché non comportano un nuovo login sospetto o un fallimento MFA.

Dal punto di vista della sicurezza IT, sembra tutto perfettamente normale, e rappresentano un’evoluzione pericolosa nel pano...