---
title: Email Security: I Protocolli di Sicurezza che garantiscono l’Autenticità, l’Integrità e la Riservatezza delle Comunicazioni
url: https://www.ictsecuritymagazine.com/articoli/email-security-i-protocolli-di-sicurezza-che-garantiscono-lautenticita-lintegrita-e-la-riservatezza-delle-comunicazioni/
source: ICT Security Magazine
date: 2024-07-25
fetch_date: 2025-10-06T17:49:47.866811
---

# Email Security: I Protocolli di Sicurezza che garantiscono l’Autenticità, l’Integrità e la Riservatezza delle Comunicazioni

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

![Email Security: I Protocolli di Sicurezza email](https://www.ictsecuritymagazine.com/wp-content/uploads/protocolli-di-sicurezza-email.jpg)

# Email Security: I Protocolli di Sicurezza che garantiscono l’Autenticità, l’Integrità e la Riservatezza delle Comunicazioni

A cura di:[Fabrizio Giorgione](#molongui-disabled-link)  Ore 24 Luglio 202426 Settembre 2025

La sicurezza delle email (*email security*) rappresenta oggi una priorità assoluta per aziende e professionisti, poiché la posta elettronica rimane uno dei canali preferiti dai cyber criminali per attacchi di phishing, spoofing e malware. Per garantire **autenticità, integrità e riservatezza delle comunicazioni**, sono stati sviluppati diversi protocolli di sicurezza che svolgono un ruolo fondamentale nella difesa dei sistemi di posta elettronica.

Tra i più diffusi troviamo protocolli di trasmissione come **SMTP con estensioni STARTTLS**, soluzioni di crittografia come **TLS, PGP/GPG e S/MIME**, fino alle estensioni DNS come **DNSSEC**, che proteggono l’infrastruttura alla base dei meccanismi di autenticazione. A questi si affiancano strumenti indispensabili come **SPF, DKIM e DMARC**, che consentono di verificare l’identità del mittente, prevenire la manipolazione dei messaggi e contrastare efficacemente tentativi di frode via email.

In questo articolo vedremo come funzionano i principali protocolli di **email authentication**, quali vantaggi offrono e perché la loro corretta implementazione è una best practice essenziale per rafforzare la **sicurezza della posta elettronica** e tutelare utenti e organizzazioni dalle minacce informatiche più diffuse.

## Email Security: guida completa ai protocolli SPF, DKIM, DMARC e alle best practice di autenticazione

Nell’ambito dell’email security esistono diversi protocolli volti a garantire l’autenticità, l’integrità e la riservatezza delle comunicazioni, tra i più importanti ci sono:

* **SMTP (Simple Mail Transfer Protocol)**: è il protocollo di base utilizzato per inviare e ricevere email, tuttavia, per impostazione predefinita, SMTP non offre meccanismi di autenticazione e sicurezza. Pertanto, molte implementazioni incorporano estensioni relative a **STARTTLS** per crittografare le comunicazioni tra i server di posta elettronica.
* **SSL/TLS (Secure Sockets Layer/Transport Layer Security)**: sono protocolli crittografici utilizzati per garantire la riservatezza e l’integrità delle comunicazioni tra client e server. In questo caso il protocollo STARTTLS consentirà di avviare una connessione sicura SSL/TLS durante la trasmissione delle email. Si noti che il protocollo SSL è ormai in disuso in quanto poco sicuro; pertanto, come best practice si consiglia il protocollo **TLS** alla **versione 1.2**. La versione del TLS 1.3 sarebbe in realtà quella desiderata, tuttavia, non essendo in grado di “comunicare” con le sue versioni precedenti può creare molti problemi di comunicazione con chi non adotta tale protocollo (purtroppo ancora poco diffuso).
* **PGP (Pretty Good Privacy) / GPG (GNU Privacy Guard)**: sono protocolli di crittografia end-to-end utilizzati per cifrare e decifrare i contenuti delle email. Consentono agli utenti di proteggere il contenuto delle loro comunicazioni durante la trasmissione.
* **S/MIME (Secure/Multipurpose Internet Mail Extensions)**: è un protocollo di crittografia che fornisce sicurezza alle email utilizzando certificati digitali che firmano e cifrano i messaggi. È spesso utilizzato per garantire la riservatezza e l’autenticità delle email.
* **DNSSEC (Domain Name System Security Extensions)**: questo protocollo non è specificamente legato alle email tuttavia la sicurezza del DNS è cruciale per i protocolli di **SPF, DKIM e DMARC**. DNSSEC previene gli attacchi di spoofing e garantisce l’integrità delle informazioni.

Quando viene inviata un’email, il server del destinatario esegue alcuni controlli per verificare se il messaggio risulta legittimo e inviato da un mittente autorizzato. Questi controlli sono possibili attraverso l’implementazione dei protocolli **SPF, DKIM e DMARC**:

* **SPF** (**Sender Policy Framework**): è un protocollo di autenticazione che verifica se un server di posta elettronica è effettivamente autorizzato a inviare messaggi per un determinato dominio. Come si evince dalla figura 5, Il mittente pubblicherà il record SPF nel DNS, specificando quali sono i server autorizzati a inviare email per proprio conto, così, quando un server di posta riceverà un messaggio, potrà verificare l’autenticità del mittente controllandone il record SPF.

![email security e protocolli di sicurezza email: SPF (Sender Policy Framework)](https://www.ictsecuritymagazine.com/wp-content/uploads/Funzionamento-dellSPF.png)

Figura 5. Funzionamento dell’SPF

Nota. Quando un messaggio viene forwardato l’SPF authentication fallisce.

Questo protocollo risulta particolarmente efficace contro gli attacchi di tipo **spoofing** e **phishing**.

* **DKIM** (**Domain-Keys Identified Mail**): il protocollo utilizza la firma digitale per verificare l’autenticità dell’email ricevuta e confermare che non sia stata manomessa durante la consegna. Il protocollo prevede che il server SMTP del mittente aggiunga una firma (signature) con chiave privata negli header dei messaggi di post...