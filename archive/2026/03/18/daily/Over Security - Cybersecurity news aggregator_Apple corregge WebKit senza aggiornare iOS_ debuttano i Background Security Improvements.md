---
title: Apple corregge WebKit senza aggiornare iOS: debuttano i Background Security Improvements
url: https://www.cybersecurity360.it/news/apple-corregge-webkit-senza-aggiornare-ios-debuttano-i-background-security-improvements/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-18
fetch_date: 2026-03-19T04:20:45.724167
---

# Apple corregge WebKit senza aggiornare iOS: debuttano i Background Security Improvements

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Apple corregge WebKit senza aggiornare iOS: debuttano i Background Security Improvements

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

l’analisi tecnica

# Apple corregge WebKit senza aggiornare iOS: debuttano i Background Security Improvements

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

[Partecipa al dibattito](#comments)

Indirizzo copiato

---

Usati per la prima volta i Background Security Improvements per correggere una vulnerabilità nel motore WebKit. Ecco cos’è e come funziona il nuovo meccanismo di aggiornamento silenzioso per la sicurezza e perché rivoluziona il patch management su iOS e macOS

Pubblicato il 18 mar 2026

---

[Paolo Tarsitano](https://www.cybersecurity360.it/giornalista/paolo-tarsitano/)

Editor Cybersecurity360.it

---

---

![Apple Background Security Improvements](data:image/png;base64...)![Apple Background Security Improvements](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/03/Apple-Background-Security-Improvements.jpg)

In sintesi

* Apple ha introdotto i **Background Security Improvements**: patch leggere e automatiche (da **iOS 26.1**, **iPadOS 26.1**, **macOS 26**) che applicano fix in background senza riavvio, evoluzione dei **Rapid Security Response**.
* È stata corretta una cross‑origin nella **Navigation API** di **WebKit** (fix per **CVE-2026-20643**) che consentiva l’aggiramento della **Same Origin Policy**, risolta rafforzando la validazione dell’input.
* Azioni consigliate: abilitare i **Background Security Improvements** e l’opzione **Installa automaticamente**, verificare il suffisso **(a)** nella versione, non rimuovere le patch e aggiornare le policy **MDM** e i playbook di sicurezza.

Riassunto generato con AI

---

Apple ha rilasciato il [primo aggiornamento attraverso un meccanismo automatico](https://support.apple.com/en-us/102657) che molti utenti non conoscono ancora: i **Background Security Improvements**.

Prima di entrare nel merito della [vulnerabilità corretta](https://support.apple.com/en-us/111333), è utile capire cosa sia questo nuovo strumento e perché rappresenta **un cambiamento significativo nel modo in cui Apple gestisce la sicurezza dei propri dispositivi**.

Indice degli argomenti

* [Cosa sono i Background Security Improvements](#Cosa_sono_i_Background_Security_Improvements)
  + [Come differisce dal Rapid Security Response](#Come_differisce_dal_Rapid_Security_Response)
* [La vulnerabilità in WebKit corretta da Apple](#La_vulnerabilita_in_WebKit_corretta_da_Apple)
  + [Cos’è la Same Origin Policy e perché il suo aggiramento è pericoloso](#Cose_la_Same_Origin_Policy_e_perche_il_suo_aggiramento_e_pericoloso)
  + [Il dettaglio tecnico: Navigation API e validazione dell’input](#Il_dettaglio_tecnico_Navigation_API_e_validazione_dellinput)
* [Il contesto: WebKit, un bersaglio ricorrente](#Il_contesto_WebKit_un_bersaglio_ricorrente)
* [Indicazioni pratiche: cosa fare](#Indicazioni_pratiche_cosa_fare)
  + [Per gli utenti individuali](#Per_gli_utenti_individuali)
  + [Per gli amministratori IT e i responsabili della sicurezza](#Per_gli_amministratori_IT_e_i_responsabili_della_sicurezza)
* [Un passo avanti nel modello di sicurezza Apple](#Un_passo_avanti_nel_modello_di_sicurezza_Apple)

## Cosa sono i Background Security Improvements

I Background Security Improvements sono aggiornamenti di sicurezza **leggeri, mirati e silenziosi**, distribuiti automaticamente in background senza richiedere un aggiornamento completo del sistema operativo e, soprattutto, **senza richiedere il riavvio del dispositivo**.

Sono disponibili a partire da **iOS 26.1, iPadOS 26.1 e macOS 26** e si applicano a componenti specifici come il motore browser WebKit, le librerie di sistema e altri framework critici.

In parole semplici, possiamo immaginare di tappare una perdita d’acqua senza smontare l’intero impianto idraulico di casa. I Background Security Improvements fanno esattamente questo: correggono un componente specifico (come, ad esempio, il motore che gestisce le pagine web) senza toccare il resto del sistema operativo e senza interrompere il lavoro in corso.

Apple non è la prima azienda a percorrere questa strada: Microsoft ha introdotto una tecnologia analoga con gli **hotpatch** su Windows 11 Enterprise e Linux offre da anni meccanismi di live patching del kernel. Ma per l’ecosistema Apple si tratta di una vera novità, destinata a diventare uno strumento centrale nella gestione del rischio su miliardi di dispositivi.

### Come differisce dal Rapid...