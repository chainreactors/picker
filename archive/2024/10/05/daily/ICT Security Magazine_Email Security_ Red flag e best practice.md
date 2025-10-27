---
title: Email Security: Red flag e best practice
url: https://www.ictsecuritymagazine.com/articoli/email-security-tips/
source: ICT Security Magazine
date: 2024-10-05
fetch_date: 2025-10-06T18:54:36.611967
---

# Email Security: Red flag e best practice

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

![email security best practices](https://www.ictsecuritymagazine.com/wp-content/uploads/closeup-encrypted-email-message-interface-with-security-features-protecting-communic.jpg)

# Email Security: Red flag e best practice

A cura di:[Fabrizio Giorgione](#molongui-disabled-link)  Ore 4 Ottobre 2024

L’**email security** è fondamentale per proteggere aziende e utenti da minacce come phishing, malware e attacchi mirati attraverso la posta elettronica. In questo articolo, analizzeremo le principali red flag da tenere sotto controllo per identificare email potenzialmente pericolose e le *best practice* per gestirle in modo sicuro. Queste includono l’adozione di protocolli sicuri, il monitoraggio delle email sospette e la formazione periodica del personale per riconoscere minacce. Scopri come applicare strategie preventive e reattive per evitare violazioni e difendere i dati sensibili della tua organizzazione dalle minacce via email.

Il sistema di posta elettronica è diventato un’infrastruttura di comunicazione essenziale, la sua diffusione capillare rende cruciale adottare procedure di Email Security efficaci. Questo implica anche l’importanza di strumenti e tecniche di indagine forense per analizzare eventuali incidenti, per approfondire ulteriormente l’argomento, ti consigliamo la del precedente articolo ” [Email Forensics: Studio di email malevola e principali tool di analisi](https://www.ictsecuritymagazine.com/articoli/email-forensics-sicurezzamail/)” dove vengono illustrando metodologie e strumenti all’avanguardia per individuare messaggi sospetti o dannosi.

### Email Security: Red flag

A questo punto verranno mostrate alcune mail e le relative **red flag**:

![Email Security Red flag – Phishing URL](https://www.ictsecuritymagazine.com/wp-content/uploads/023-1.png)

Figura 20. Red flag – Phishing URL

In questo caso è possibile osservare le seguenti red flag:

* Subject che fa leva sull’**urgenza** di effettuare un’azione
* Header from palesemente malevolo
* Link che fa uso del protocollo **http**, tipico indice di una mail di phishing.

Nota: si tenga presente che le mail di phishing avanzato utilizzano anche protocolli sicuri come “**https**” quindi preso singolarmente questo indicatore non è sempre “parlante”.

![Email Security Red flag – Call requested - Email Security ](https://www.ictsecuritymagazine.com/wp-content/uploads/024-1.png)

Figura 21. Red flag – Call requested

In questo caso invece, oltre alle evidenze precedenti, si può osservare come l’attaccante punti molto sul lato emotivo e tenti di farsi richiamare al numero indicato. Si può notate inoltre che la mail fa uso di terminologie “generiche” come “Dear customer”, questo è indice che possano esserci molteplici utenti coinvolti.

Di seguito, infine, si riportano alcune evidenze malevole, recuperabili tramite i tool precedentemente descritti, di un IP estratto dall’header di una mail.

![Email Security Talos Threat Intelligence - Email Security ](https://www.ictsecuritymagazine.com/wp-content/uploads/025-1-1024x417.png)

Figura 22. Talos Threat Intelligence

In particolare, l’analista dovrà tenere in considerazione:

* La geolocalizzazione dell’IP, è probabile che una mail malevola sia inviata da una nazionalità con la quale l’azienda non collabora o comunque da aree note per le loro attività malevole o comunque sospette.
* La sender IP reputation.
* Il livello di spam segnalato nel web.
* Eventuali blacklist.

### Email Security: Best practice

* Quando si riceve una mail da un utente sconosciuto si consiglia di evitare di rispondere e chiedere ad eventuali colleghi.
* Le mail che fanno leva sulle urgenze e/o emozioni potrebbero essere potenzialmente malevole. Anche in questo caso si consiglia di maneggiarle con attenzione.
* In caso venga segnalato via mail che la password è in scadenza si consiglia di utilizzare i link ufficiali di quel determinato canale e/o comunque non quelli presenti nella mail (specie se questa utilizza protocolli non sicuri come “http” o provenga da un sender sospetto/sconosciuto).
* Se vengono richiesti dati sensibili, si invita ad utilizzare i canali sicuri ed eventualmente contattare i riferimenti noti e non quelli forniti tramite mail. Questo genere di informazione non vengono mai richieste via mail dai gestori bancari e simili.
* Ogni allegato sospetto proveniente da un sender sconosciuto è potenzialmente malevolo. Solo i file “.**txt**” attualmente risultano essere sicuri in quanto contenente solo testo. Per tale ragione si invita a segnalare la mail al team di competenza. Uno dei metodi più utilizzati per riportare mail malevole tramite Outlook è col plugin “**Report Message**” (figura 23) attraverso il quale con pochi semplici passi l’utente potrà segnalare la mail sospetta.

![Email Security Outlook Plugin – Report message - Email Security ](https://www.ictsecuritymagazine.com/wp-content/uploads/026-1.png)

Figura 23. Outlook Plugin – Report message

* Ogni azienda dovrebbe abilitare la propria casella “Abuse” per la gestione delle segnalazioni di mail malevole al team di competenza.
* Tutte le mail provenienti dall’esterno vanno maneggiate con cura. Ogni azienda dovrebbe quindi abilitare, tramite l’uso dei propri mail secure gateway, il **tag esterno** nel subject e/o nel body della ma...