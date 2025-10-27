---
title: Password manager vulnerabili a una nuova forma di clickjacking: i dettagli
url: https://www.cybersecurity360.it/news/password-manager-vulnerabili-a-una-nuova-forma-di-clickjacking-i-dettagli/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-27
fetch_date: 2025-10-07T00:49:36.908106
---

# Password manager vulnerabili a una nuova forma di clickjacking: i dettagli

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Password manager vulnerabili a una nuova forma di clickjacking: i dettagli

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

# Password manager vulnerabili a una nuova forma di clickjacking: i dettagli

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

Indirizzo copiato

---

La tecnica di attacco sfrutta un semplice stratagemma per dirottare il click dell’utente e sottrargli le credenziali di accesso. Ecco come funziona e perché rappresenta un rischio anche per le aziende

Pubblicato il 26 ago 2025

---

[Marco Schiaffino](https://www.cybersecurity360.it/giornalista/marco-schiaffino/)

Giornalista

---

---

![Password manager vulnerabilità](data:image/png;base64...)![Password manager vulnerabilità](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2025/08/Password-manager-vulnerabilita.jpg)

---

L’ennesimo scricchiolio che segnala la **debolezza dei sistemi di autenticazione tramite username e password** arriva dal DEF CON 33, convegno che ad agosto ha visto la partecipazione di decine di esperti di cyber security nella sede di Las Vegas.

Tra questi anche Marek Tóth, un ricercatore indipendente che ha presentato il suo studio su una **tecnica di attacco che permette di indurre i più diffusi [password manager](https://www.cybersecurity360.it/cultura-cyber/password-manager-cosa-sono-quali-sono-i-migliori-come-usarli-e-perche/) a fornire le credenziali di accesso** a qualsiasi servizio.

L’attacco è definito come “**DOM-based Extension Clickjacking**”, cioè come un “**dirottamento dell’estensione basato sul Document Object Model**”.

In altre parole, Tóth ha trovato un modo per utilizzare una particolare struttura degli elementi che compongono un sito Web per ingannare i visitatori e fare in modo che, se hanno un password manager attivo, quest’ultimo **compili automaticamente i campi con le credenziali di un determinato servizio**.

Indice degli argomenti

* [Come funziona il clickjacking](#Come_funziona_il_clickjacking)
* [Un piccolo gioco di prestigio](#Un_piccolo_gioco_di_prestigio)
* [Variazioni sul tema](#Variazioni_sul_tema)
* [Tanti password manager (ancora) vulnerabili](#Tanti_password_manager_ancora_vulnerabili)
* [Uno strumento nelle mani dei gruppi ransomware?](#Uno_strumento_nelle_mani_dei_gruppi_ransomware)

## Come funziona il clickjacking

Da un punto di vista pratico, l’eventuale attaccante deve solo pubblicare una pagina Web malevola (o modificarne una legittima) e attirare la vittima su di essa.

La pagina in questione sfrutta una classica tecnica di **clickjacking**, quella cioè di prevedere un iframe invisibile (con opacità impostata a 0) e **sovrapporgli un qualsiasi elemento visibile** (come un captcha o una richiesta di approvazione dei cookie) sul quale il visitatore è portato a fare click senza porsi troppe domande.

Non si tratta di una novità: lo stesso Tóth aveva già in passato segnalato vulnerabilità di questo genere, che avevano portato all’adozione di accorgimenti per mitigare il rischio che qualcuno potesse utilizzare tecniche simili per **avviare processi indesiderati** attraverso il dirottamento dei click.

Ciò che cambia nella [nuova versione messa a punto dal ricercatore](https://marektoth.com/blog/dom-based-extension-clickjacking/), è il coinvolgimento dei password manager. Un elemento che può portare facilmente, come spiega l’autore del report, al **furto di credenziali o dei dati di una carta di credito**.

## Un piccolo gioco di prestigio

Da quanto esposto in precedenza, indurre un utente a fare un click indesiderato sul modulo di compilazione dei campi per l’accesso ai servizi non è particolarmente difficile.

A rendere più semplice il tutto, spiega Tóth, c’è il fatto che tutti i password manager più diffusi non si limitano a riconoscere l’homepage di un servizio di cui hanno in memoria le credenziali, ma anche tutti i sottodomini.

Questo rende più probabile la possibilità che l’attaccante riesca a inserire anche in una pagina Web legittima **un iframe che consenta di ingannare l’estensione del password manager** e indurlo così a inviare le informazioni per l’accesso, che il cyber criminale può intercettare. Tutto quello che deve fare è trovare una qualsiasi pagina **una vulnerabilità XSS** che gli consenta di farlo.

Il vero “tocco di classe” introdotto dal ricercatore è **l’uso di un javascript per rendere trasparente (invisibile) anche l’estensione del password manage...