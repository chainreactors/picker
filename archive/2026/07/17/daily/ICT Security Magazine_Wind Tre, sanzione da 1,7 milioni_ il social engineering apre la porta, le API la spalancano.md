---
title: Wind Tre, sanzione da 1,7 milioni: il social engineering apre la porta, le API la spalancano
url: https://www.ictsecuritymagazine.com/notizie/windtre-sanzione-data-breach/
source: ICT Security Magazine
date: 2026-07-17
fetch_date: 2026-07-18T04:46:24.726127
---

# Wind Tre, sanzione da 1,7 milioni: il social engineering apre la porta, le API la spalancano

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Wind Tre sanzione il social engineering apre la porta le API la spalancano](https://www.ictsecuritymagazine.com/wp-content/uploads/Wind-Tre-sanzione-il-social-engineering-apre-la-porta-le-API-la-spalancano.png)

# Wind Tre, sanzione da 1,7 milioni: il social engineering apre la porta, le API la spalancano

A cura di:[Redazione](#molongui-disabled-link)  Ore 17 Luglio 2026

Il Garante per la protezione dei dati personali ha sanzionato Wind Tre S.p.A. per 1.715.600 euro. Il [provvedimento del 14 maggio 2026](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10263796) (registro n. 348, doc. web 10263796) è stato reso pubblico con la [newsletter n. 549 dell’Autorità](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10272004), del 16 luglio 2026, e chiude l’istruttoria su due violazioni notificate dalla stessa società nel febbraio 2025. La ricostruzione del Garante smonta però la lettura più immediata, quella dell’errore umano isolato: il social engineering è stato il vettore d’ingresso, ma a trasformare il secondo dei due accessi abusivi in un’esfiltrazione da 365mila clienti sono state carenze tecniche precise sulle API esposte.

## Da 23 record a 365.048

I due eventi, occorsi a pochi giorni di distanza presso due distinti punti vendita, seguono lo stesso schema. Gli attaccanti hanno contattato telefonicamente un addetto del negozio chiedendo l’accesso remoto al dispositivo per asserite necessità di assistenza tecnica, ottenendo così tutti i fattori di autenticazione della *web application* usata per interrogare la customer base.

Qui le due dinamiche divergono, ed è la parte che conta. Il primo accesso ha prodotto 66 interrogazioni puntuali, con la violazione dei dati di circa 23 clienti. Nel secondo, secondo la ricostruzione fornita dalla società e recepita dall’Autorità, dopo un primo tentativo di intrusione bloccato dai meccanismi di sicurezza gli attaccanti hanno analizzato l’applicativo e individuato alcune API prive di misure di protezione, invocate a valle della funzionalità di ricerca principale. Sfruttandole, hanno eseguito circa 2 milioni di richieste totali con logica di *enumeration*, incrementando progressivamente l’identificativo del codice cliente (*customerId*), e hanno violato i dati di 365.048 clienti.

I dati raggiunti riguardano informazioni anagrafiche e di contatto. Per 41.359 clienti l’esfiltrazione ha riguardato anche il metodo di pagamento registrato sui sistemi Wind Tre: bollettino postale, IBAN, carta di credito. Le informazioni sulla carta erano riferite esclusivamente al PAN asteriscato e alla data di scadenza; i numeri completi non risultano esposti.

## Le carenze contestate: certificati, credenziali, perimetro dei test

L’atto di avvio del 6 ottobre 2025 ha contestato la violazione dell’art. 5, par. 1, lett. f) e dell’art. 32, par. 1, lett. b) del GDPR su due profili, certificati digitali e controlli sulle API. Nelle valutazioni giuridiche finali, e poi fra le circostanze aggravanti, si aggiunge un terzo profilo: la gestione delle credenziali.

Sui **certificati digitali**, l’Autorità ha rilevato l’assenza di procedure sicure e formalizzate per generazione, distribuzione e conservazione: certificati e chiavi private avrebbero dovuto essere custoditi in cartelle o repository cifrati, o in sistemi dedicati di gestione delle chiavi (key management system o hardware security module), oppure in dispositivi sicuri come smart card o token USB capaci di generare e conservare internamente la chiave privata impedendone l’esportazione. Il certificato, osserva il Garante, andava in ogni caso correttamente importato nello store del sistema operativo e non conservato in chiaro.

Sulle **credenziali**, il Garante ha rilevato l’assenza di strumenti idonei alla gestione sicura per gli operatori dei punti vendita, con conseguente rischio di password deboli, riutilizzate o mal protette, e ha indicato la combinazione password manager più OTP come misura di riferimento: strumenti a crittografia forte, spesso di tipo zero-knowledge, integrati con un fattore aggiuntivo rispetto alla password statica.

Sulle **API**, il rilievo è il più tecnico e il più severo. Wind Tre ha dichiarato di svolgere periodicamente *vulnerability assessment* e *penetration test*, ma il Garante osserva che tali attività non hanno incluso, o hanno incluso in modo non adeguato, le API esposte e i relativi flussi applicativi. Le vulnerabilità sfruttate, riconducibili alle [categorie della OWASP API Security Top 10](https://www.ictsecuritymagazine.com/articoli/sicurezza-delle-api/), sarebbero state ragionevolmente individuabili con verifiche mirate: la criticità sta in una non corretta definizione del perimetro di analisi e/o in una insufficiente profondità delle verifiche condotte. In audizione la società ha chiarito che all’epoca dei fatti venivano protette solo le API principali, perché l’uso massivo di chiamate sulle secondarie non era considerato normalmente utilizzabile e non era stato esaminato in chiave preventiva. *Rate limiting* su tutte le API sensibili, combinato con CAPTCHA, avrebbe consentito di controllare sia la quantità di richieste sia la natura dell’utente.

Sul ...