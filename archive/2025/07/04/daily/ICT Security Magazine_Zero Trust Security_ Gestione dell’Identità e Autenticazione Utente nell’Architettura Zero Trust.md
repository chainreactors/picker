---
title: Zero Trust Security: Gestione dell’Identità e Autenticazione Utente nell’Architettura Zero Trust
url: https://www.ictsecuritymagazine.com/articoli/zero-trust-utente/
source: ICT Security Magazine
date: 2025-07-04
fetch_date: 2025-10-06T23:55:51.239984
---

# Zero Trust Security: Gestione dell’Identità e Autenticazione Utente nell’Architettura Zero Trust

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
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![architettura Zero Trust: componenti della gestione dell'identità utente, autenticazione multi-fattore e tecnologie di identity governance](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-10_AgSuJIPV.png)

# Zero Trust Security: Gestione dell’Identità e Autenticazione Utente nell’Architettura Zero Trust

A cura di:[Fabrizio Fioravanti](#molongui-disabled-link)  Ore 3 Luglio 202516 Luglio 2025

Questo articolo fa parte della [serie](https://www.ictsecuritymagazine.com/articoli/zero-trust/) dedicata all’architettura Zero Trust, un modello di sicurezza fondamentale per le organizzazioni moderne. In questo approfondimento, esploreremo il primo pilastro dell’architettura: la gestione dell’identità e della fiducia dell’utente. Analizzeremo le tecnologie chiave come l’autenticazione multi-fattore (MFA), il passwordless authentication, il Single Sign-On (SSO) e i sistemi avanzati di Identity Governance, evidenziando come questi elementi si integrino per creare un robusto sistema di gestione delle identità digitali.

## Zero Trust e Gestione dell’Identità Utente: Principi e Implementazione

Al centro del modello Zero Trust vi è l’utente, o meglio la fiducia riposta nell’utente, non in modo generico ma in relazione al ruolo ricoperto all’interno dell’organizzazione. Ogni organizzazione, anche di media complessità, non può più permettersi di applicare privilegi di accesso uniformi. È essenziale raggruppare gli utenti in base ai loro ruoli e alle autorizzazioni necessarie per l’accesso ai servizi, definendo specifiche forme di autenticazione in funzione del profilo di rischio associato.

La fiducia negli utenti si basa sul garantire che l’utente sia effettivamente chi dichiara di essere e non un impostore. Tranne in rari casi, oggi si utilizza l’autenticazione multi-fattore (MFA), in cui si richiede all’utente di fornire una combinazione di credenziali, come una password, un dispositivo fisico (smart card, chiave USB, dispositivo di prossimità) e un elemento biometrico (impronta digitale, riconoscimento facciale, iride). L’MFA è diventato uno standard per garantire un alto livello di sicurezza.

Per semplificare l’esperienza utente, è possibile adottare tecnologie come l’autenticazione senza password (passwordless) e il Single Sign-On (SSO); l’adozione di tali tecnologie se non correttamente gestite ad esempio nella durata delle sessioni SSO o senza implementare anche le ulteriori fasi dello zero trust potrebbero essere fonti di rischio anche se è indubbio, che riducono il numero di password da ricordare e richiedono un numero inferiore di autenticazioniun’unica autenticazione giornaliera per accedere ai sistemi. In determinati contesti, può essere richiesta un’autenticazione più forte utilizzando magari anche più di 2 fattori, ad esempio per l’accesso a sistemi critici, mentre per situazioni a basso rischio potrebbe essere sufficiente un’autenticazione più semplice limitandosi alla sola coppia username e password.

L’adozione di un modello fiduciario per l’utenza costituisce il primo passo verso un modello di sicurezza più complesso e completo, ma finché non si ha certezza dell’identità dell’utente, è difficile implementare ulteriori tecnologie avanzate per proteggere completamente il DAAS in esame secondo gli altri elementi del modello Zero Trust.

La gestione dell’identità in un contesto Zero Trust va oltre la semplice autenticazione multi-fattore che rimane comunque uno dei pilastri fondamentali. Secondo le ricerche del SANS Institute, un’implementazione efficace deve includere:

* Analisi comportamentale degli utenti (User Behavior Analytics – UBA)
* Autenticazione adattiva basata sul rischio
* Gestione del ciclo di vita delle identità
* Governance delle identità e degli accessi (IGA)

L’implementazione completa di tutti questi elementi richiede l’integrazione di diverse tecnologie e framework che spaziano da metriche collezionate sulle abitudini degli utenti, a metodologie avanzate di gestione dell’identità nell’intero ciclo di vita aziendale per ottenere un modello di autenticazione che si adatti in base alla situazione ed alla rilevanza del DAAS a cui si accede.

Al centro del modello Zero Trust vi è l’utente, o meglio la fiducia riposta nell’utente, non in modo generico ma in relazione al ruolo ricoperto all’interno dell’organizzazione. Ogni organizzazione, anche di media complessità, non può più permettersi di applicare privilegi di accesso uniformi. È essenziale raggruppare gli utenti in base ai loro ruoli e alle autorizzazioni necessarie per l’accesso ai servizi, definendo specifiche forme di autenticazione in funzione del profilo di rischio associato.

La fiducia negli utenti si basa sul garantire che l’utente sia effettivamente chi dichiara di essere e non un impostore. Tranne in rari casi, oggi si utilizza l’autenticazione multi-fattore [(MFA)](https://www.ictsecuritymagazine.com/notizie/gestione-di-identita-e-accessi/), in cui si richiede all’utente di fornire una combinazione di credenziali, come una password, un dispositivo fisico (smart card, chiave USB, dispositivo di prossimità) e un elemento biometrico (impronta digitale, riconoscimento facciale, iride). L’MFA è diventato uno standard per garantire un alto livello di sicurezza.

Per semplificare l’esperien...