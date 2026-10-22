---
title: PHP2Shell, due vulnerabilità critiche in PHP: come proteggere i server in attesa delle patch
url: https://www.cybersecurity360.it/nuove-minacce/php2shell-due-vulnerabilita-critiche-in-php-come-proteggere-i-server-in-attesa-delle-patch/
source: Over Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:29.793573
---

# PHP2Shell, due vulnerabilità critiche in PHP: come proteggere i server in attesa delle patch

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)
[I nostri servizi](https://www.cybersecurity360.it/about-network/)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## PHP2Shell, due vulnerabilità critiche in PHP: come proteggere i server in attesa delle patch

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
  + [Chi siamo](https://www.cybersecurity360.it/about/)
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

L'ANALISI TECNICA

# PHP2Shell, due vulnerabilità critiche in PHP: come proteggere i server in attesa delle patch

---

[Commenta l'articolo](#comments)

Indirizzo copiato

---

Il PHP Security Team annuncia due vulnerabilità critiche, entrambe con punteggio CVSS di 9,2, e prepara un aggiornamento d’emergenza. Tra possibili attacchi RCE, mitigazioni non confermate e versioni fuori supporto, ecco come gestire il rischio sui server esposti

Pubblicato il 21 ott 2026

---

[Dario Fadda](https://www.cybersecurity360.it/giornalista/dario-fadda/)

Research Infosec, fondatore Insicurezzadigitale.com

---

---

![AI Questions Icon](data:image/gif;base64...)![AI Questions Icon](https://chatbotdev.ai.nextwork360.it/icons/NW360.svg)

Chiedi all'AI

Riassumi questo articolo

Approfondisci con altre fonti

![PHP2Shell](data:image/png;base64...)![PHP2Shell](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/10/PHP2Shell.jpg)

---

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)

---

---

---

Il **PHP Security Team** ha annunciato per il 21 ottobre 2026 il **rilascio di aggiornamenti d’emergenza** destinati a correggere due vulnerabilità critiche, identificate come **CVE-2026-109618** e **CVE-2026-109619** e conosciute pubblicamente con il nome di **PHP2Shell**.

Entrambe hanno ricevuto un **punteggio CVSS v4.0 di 9,2**, mentre le informazioni tecniche definitive, comprese le versioni interessate e quelle corrette, saranno pubblicate insieme alle patch.

Nel frattempo, gli amministratori devono affrontare un problema concreto: **proteggere applicazioni e servizi PHP esposti su Internet senza poter ancora contare su una correzione ufficiale**.

La priorità non è individuare una configurazione da modificare alla cieca, ma verificare quali sistemi siano esposti, ridurre le possibilità di accesso e preparare l’installazione degli aggiornamenti non appena disponibili.

Indice degli argomenti

* [PHP2Shell: cosa sappiamo delle due vulnerabilità critiche](#PHP2Shell_cosa_sappiamo_delle_due_vulnerabilita_critiche)
  + [Perché si parla di esecuzione remota di codice](#Perche_si_parla_di_esecuzione_remota_di_codice)
* [Un problema nella gestione degli upload: un’ipotesi ancora da verificare](#Un_problema_nella_gestione_degli_upload_unipotesi_ancora_da_verificare)
  + [La direttiva session.upload\_progress.enabled non è una patch](#La_direttiva_sessionupload_progressenabled_non_e_una_patch)
* [Perché WAF e controlli applicativi potrebbero non bastare](#Perche_WAF_e_controlli_applicativi_potrebbero_non_bastare)
* [Come ridurre subito l’esposizione dei server PHP](#Come_ridurre_subito_lesposizione_dei_server_PHP)
  + [Limitare l’accesso quando non è possibile aggiornare](#Limitare_laccesso_quando_non_e_possibile_aggiornare)
  + [Ridurre le conseguenze di un’eventuale compromissione](#Ridurre_le_conseguenze_di_uneventuale_compromissione)
* [PHP fuori supporto: il problema che sopravvive all’emergenza](#PHP_fuori_supporto_il_problema_che_sopravvive_allemergenza)
  + [Attenzione anche alla scadenza di PHP 8.2](#Attenzione_anche_alla_scadenza_di_PHP_82)
* [Cosa verificare quando saranno pubblicate le patch](#Cosa_verificare_quando_saranno_pubblicate_le_patch)
  + [Il rischio delle immagini e dei template non aggiornati](#Il_rischio_delle_immagini_e_dei_template_non_aggiornati)
* [PHP2Shell: la gestione del rischio non può dipendere soltanto dalle patch](#PHP2Shell_la_gestione_del_rischio_non_puo_dipendere_soltanto_dalle_patch)

## PHP2Shell: cosa sappiamo delle due vulnerabilità critiche

Il [preavviso ufficiale pubblicato da PHP](https://www.php.net/archive/2026.php#2026-10-20-1) il 20 ottobre indica due vulnerabilità critiche, entrambe valutate 9,2 secondo CVSS v4.0.

Il rilascio delle correzioni è programmato per mercoledì 21 ottobre alle 14:00 UTC, corrispondenti alle 16:00 italiane.

Il team di sicurezza invita tutti gli utilizzatori a prepararsi immediatamente all’aggiornamento e precisa che potrebbe anticipare la pubblicazione delle patch qualora emergessero dettagli tecnici pubblici o evidenze di sfruttamento attivo.

Quest’ultima precisazione non equivale a una conferma di at...