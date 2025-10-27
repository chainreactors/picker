---
title: Un’introduzione a Self-Sovereign Identity
url: https://www.ictsecuritymagazine.com/articoli/intro-self-sovereign-identity/
source: ICT Security Magazine
date: 2024-09-25
fetch_date: 2025-10-06T18:29:45.744283
---

# Un’introduzione a Self-Sovereign Identity

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Self-Sovereign-Identity-1.jpg)

# Un’introduzione a Self-Sovereign Identity

A cura di:[Francesco Santini](#molongui-disabled-link)  Ore 24 Settembre 2024

In questo articolo, ci dedichiamo alla descrizione delle nozioni fondamentali dietro a Self-Sovereign Identity, un modello di gestione dell’identità digitale in cui gli individui hanno il pieno controllo delle proprie informazioni personali. Parleremo inoltre dei suoi punti di forza rispetto ai precedenti modelli. In futuri articoli sullo stesso tema, ci addentreremo più sugli aspetti tecnici e sulla possibilità di creare un wallet di credenziali personali.

### Introduzione alle identità digitali, alle operazioni, ai sistemi che le utilizzano

Una *digital identity* (identità digitale) può essere descritta come un insieme di attributi che aiutano a descrivere o qualificare un’entità, che si tratti di un essere umano o di un dispositivo elettronico. Alcuni di questi attributi sono chiamati *identifier* (identificatori) e distinguono il titolare dell’identità all’interno di un contesto specifico. Per esempio, nel mondo fisico, una targa di un’auto o il nostro codice fiscale, possono fungere da identificatori in contesti differenti.

Le identità, fisiche o digitali, nascono per essere soggette a un processo di verifica, diviso in *identification* e *authentication* (rispettivamente, identificazione e autenticazione). Il processo di identificazione è l’associazione di un identificatore personale con il titolare dell’identità digitale che lo presenta, ad esempio fornendo un indirizzo email durante un’operazione di iscrizione su un sito Web.

Il processo di autenticazione consiste invece nel verificare l’entità identificata tramite una prova di sicurezza, solitamente mediante una password segreta o una firma digitale. Ad esempio, cliccare su un link ricevuto via email dimostra che l’indirizzo email appartiene al titolare. Queste due operazioni sono fornite dai sistemi di *Identity and Access Management* (IAM), servizi specializzati di cui si fidano tutte le entità coinvolte (rappresentano quindi un *trusted party*) [1].

Uno IAM consiste solitamente di tre parti, rappresentate da un *end-user* (qualsiasi entità che possiede un’identità digitale e desidera svolgere una qualche attività), un *identity provider* (IdP) e un *service provider* (SP).

Un IdP genera e gestisce informazioni sull’identità degli utenti-entità da riconoscere (umane, software, hardware, etc), oltre a fornire servizi di autenticazione. Un SP è, con una definizione molto generale, un’organizzazione che offre servizi per i quali gli utenti hanno bisogno di fornire informazioni personali. Per una lunga fase iniziale del Web, erano gli stessi SP che implementavano soluzioni IAM come autorità centralizzate (Figura 1a).

Questo modello presenta alcuni svantaggi per gli utenti, in quanto devono gestire account differenti e mantenere per ciascuno di essi le proprie credenziali di accesso (che spesso coinvolgono password semplici), le impostazioni di sicurezza, e, in generale, tutte le informazioni relative all’account. Questo approccio rende vulnerabili al furto di password attraverso tecniche di phishing, key-logging, e malware in generale.

Per questi motivi, sono stati sviluppati successivamente standard per protocolli di *federated identity* (identità federata), tra cui *Security Assertion Markup Language* (SAML) e *OpenID/OAuth*, consentendo quindi agli utenti di riutilizzare identità già presenti presso vari provider spesso “social”, come Google, LinkedIn, Apple, Amazon, etc. In questo modello, l’utente deve autorizzare/negare l’IdP a condividere specifici attributi personali richiesti dall’SP che l’utente vuole utilizzare.

Questo sistema IAM di terze parti, chiamato IdP “esternalizzato”, migliora il precedente modello centralizzato su alcuni aspetti (Figura 1b): gli utenti devono essere registrati in pochi IdP per poter accedere ai servizi disponibili sul Web. Gli SP devono essere registrati con gli IdP desiderati (o con federazioni di IdP, che collaborano tra loro in modo trasparente per l’utente) per lavorare con utenti identificati e autenticati dagli IdP. Uno dei principali problemi di questo approccio è che negli IdP adesso si concentra una grande quantità di identità digitali, che fanno sì che maggior parte degli attacchi si trasferisca verso gli IdP piuttosto che ai server degli SP, come avveniva invece col modello centralizzato.

Il modello esternalizzato si è sviluppato in modo da porre anche altri svantaggi, come la formazione di oligopoli di IdP tra i quali l’identità dell’utente non è portabile, e la possibilità degli IdP di cancellare arbitrariamente un utente (e la sua identità) dalle proprie piattaforme (in caso l’IdP sia un social network, questo può avvenire anche per una violazione delle sue condizioni di utilizzo).

![Figura 1: tre diversi modelli IAM: modello centralizzato, IdP esternalizzato, SSI](https://www.ictsecuritymagazine.com/wp-content/uploads/figura1-700x225.png)

Figura 1: tre diversi modelli IAM

### Self-Sovereign Identity

Il modello di *Self-Sovereign Identity* (SSI) elimina la necessità di un fornitore di identità esterno, consentendo all’utente di avere il pieno controllo dell...