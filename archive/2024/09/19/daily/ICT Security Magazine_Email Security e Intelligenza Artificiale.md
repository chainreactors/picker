---
title: Email Security e Intelligenza Artificiale
url: https://www.ictsecuritymagazine.com/articoli/email-security-e-intelligenza-artificiale/
source: ICT Security Magazine
date: 2024-09-19
fetch_date: 2025-10-06T18:31:20.846534
---

# Email Security e Intelligenza Artificiale

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Email-Security-e-Intelligenza-Artificiale.jpg)

# Email Security e Intelligenza Artificiale

A cura di:[Fabrizio Giorgione](#molongui-disabled-link)  Ore 18 Settembre 202415 Ottobre 2024

Nei precedenti articoli, abbiamo esplorato in dettaglio vari aspetti della sicurezza delle email, trattando la “[Struttura di una mail, Email secure gateway e relativo mail flow](https://www.ictsecuritymagazine.com/articoli/struttura-di-una-mail-email-secure-gateway-e-relativo-mail-flow/)” e approfondendo “[Email Security: I Protocolli di Sicurezza che garantiscono l’Autenticità, l’Integrità e la Riservatezza delle Comunicazioni](https://www.ictsecuritymagazine.com/articoli/email-security-i-protocolli-di-sicurezza-che-garantiscono-lautenticita-lintegrita-e-la-riservatezza-delle-comunicazioni/)“. Questi protocolli e strutture costituiscono il fondamento tecnico e operativo su cui si basa la sicurezza delle comunicazioni digitali, fornendo un’infrastruttura solida per la protezione dei dati scambiati tramite posta elettronica. Tuttavia, con l’evoluzione continua delle minacce e l’adozione di tecniche sempre più sofisticate da parte degli attaccanti, emerge la necessità di implementare strumenti di difesa più avanzati, in grado di adattarsi dinamicamente alle nuove sfide poste dagli ambienti digitali odierni.

In questo contesto, l’intelligenza artificiale (IA) sta assumendo un ruolo sempre più centrale nella sicurezza delle email. L’IA, con le sue capacità di apprendimento automatico e profonda analisi dei dati, rappresenta un elemento chiave nell’identificazione e nella prevenzione delle minacce moderne, le quali sono spesso caratterizzate da un alto grado di complessità e imprevedibilità. Il presente articolo si concentra sull’esplorazione delle potenzialità dell’IA nella protezione delle infrastrutture di posta elettronica, analizzando come le tecniche di machine learning e deep learning possano contribuire a migliorare significativamente l’efficacia dei sistemi di difesa rispetto agli approcci convenzionali.

Verranno discussi gli sviluppi più recenti nel campo dell’IA applicata alla sicurezza informatica, con particolare riferimento alle tecnologie che consentono di rilevare comportamenti anomali, identificare schemi malevoli e prevenire attacchi avanzati. Questo approccio consente di andare oltre la semplice identificazione basata su regole predefinite, permettendo una risposta proattiva e adattiva alle minacce emergenti.

## Email Security e Protection Server

I protection server non sono “onniscenti” e non sono in grado di comprendere il testo all’interno del body né di individuare qualunque tipo di minaccia.

Ad esempio, le email contenente solo testo (in cui si invita l’utente ad effettuare pagamenti e/o lo si minaccia) proveniente da domini molto utilizzati (come gmail, yahoo ecc) tendenzialmente non vengono bloccate in quanto il protection server non è in grado di comprendere il “significato” del testo di una mail. Quindi una mail proveniente da “pippo@gmail.com” contenente solo testo in cui si richiede un pagamento su un certo IBAN non è sempre detto che venga bloccata, anzi. In figura 10 è possibile osservare un tentativo di frode in cui si richiede un pagamento in bitcoin per evitare che venga diffuso materiale altamente personale del dipendente.

![Figura 10. Mail malevola - email security e intelligenza artificiale](https://www.ictsecuritymagazine.com/wp-content/uploads/012-1024x571.png)

Figura 10. Mail malevola

Come si può evincere, la mail fa leva sullo stato emozionale che può scaturire sul destinatario. Realisticamente è probabile che non abbia nemmeno a disposizione il materiale di cui parla tuttavia tenta di creare panico nel dipendente che potrebbe, se non ha effettuato alcun tipo di training contro queste minacce, andare ad eseguire le azioni richieste.

Uno dei problemi principali quindi, oltre alla mancanza di training dei dipendenti, è legata alla mancanza da parte del secure gateway di bloccare queste tipologie di mail:

* sender proveniente da domini noti (gmail, yahoo e simili);
* mail contenente solo testo;
* nessuna evidenza malevola e/o di spoofing/phishing;

questo perché i mail secure gateway non sono “senzienti” e non sono quindi in grado di comprendere il testo. È in questo campo che si sta osservando l’entrata in gioco **dell’intelligenza artificiale (IA).** Di fatto molti secure gateway moderni stanno iniziando ad integrare le IA nei loro sistemi allo scopo di bloccare e/o prevenire un maggior numero di minacce di questo tipo e non solo. Tra le IA più note ci sono **chatGTP** e **Gemini** ma se ne potrebbero citare molte altre in base all’ambito di interesse, tra cui Synthesia, Midjourney e Stable Diffusion.

## L’Adozione dell’Intelligenza Artificiale nell’Email Security

In questo contesto, l’adozione dell’i[ntelligenza artificiale (IA) nei sistemi di email security](https://www.researchgate.net/publication/350824053_AI_and_ML_techniques_to_Analyze_Communication_Emails_and_Text_patterns_To_Secure_from_Attacks) rappresenta un punto di svolta tecnologico indispensabile per colmare le lacune presenti nelle soluzioni convenzionali. L’intelligenza artificiale consente l’implementazione di capacità analitiche av...