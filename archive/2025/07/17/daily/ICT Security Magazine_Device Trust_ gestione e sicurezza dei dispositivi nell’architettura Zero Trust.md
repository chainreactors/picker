---
title: Device Trust: gestione e sicurezza dei dispositivi nell’architettura Zero Trust
url: https://www.ictsecuritymagazine.com/articoli/device-trust/
source: ICT Security Magazine
date: 2025-07-17
fetch_date: 2025-10-06T23:53:08.922851
---

# Device Trust: gestione e sicurezza dei dispositivi nell’architettura Zero Trust

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

![Device Trust: architettura Zero Trust per la gestione sicura di dispositivi aziendali, BYOD e IoT con focus su security posture e risk management](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-11_jyPPYzzT.png)

# Device Trust: gestione e sicurezza dei dispositivi nell’architettura Zero Trust

A cura di:[Fabrizio Fioravanti](#molongui-disabled-link)  Ore 16 Luglio 202516 Luglio 2025

Questo articolo fa parte di una [serie di approfondimenti](https://www.ictsecuritymagazine.com/articoli/zero-trust-utente/) dedicati al modello Zero Trust: il seguente testo si concentra sul pilastro fondamentale del Device Trust. Il contenuto esplora le strategie di gestione dei dispositivi in un contesto Zero Trust, analizzando le diverse categorie di dispositivi, le tecnologie di sicurezza essenziali e i rischi mitigati attraverso un approccio strutturato alla sicurezza degli endpoint.

Una volta verificata l’identità dell’utente, è fondamentale valutare il dispositivo che l’utente sta utilizzando. Come accennato nella sezione introduttiva, le modalità di lavoro agile e in mobilità hanno ampliato l’utilizzo non solo di dispositivi aziendali, ma anche di dispositivi di proprietà dell’utente (Bring Your Own Device, [BYOD](https://www.ictsecuritymagazine.com/articoli/byod-quando-lufficio-e-nello-zaino/)) o dispositivi utilizzati in contesti estemporanei, come quelli di terzi, di internet café o stazioni condivise pubbliche.

La classificazione del livello di fiducia da riporre in un dispositivo è un aspetto cruciale, poiché determina se il dispositivo può accedere ai sistemi dell’organizzazione e a quali risorse. Questa classificazione dipende dal controllo che l’organizzazione ha sul dispositivo e dal suo stato di sicurezza. Con l’evoluzione delle modalità di lavoro e la varietà di dispositivi nelle organizzazioni di medio-grandi dimensioni, è essenziale categorizzare i dispositivi in base al livello di sicurezza e al controllo esercitato dall’organizzazione.

Le principali categorie di dispositivi sono:

### **Dispositivi completamente gestiti dall’organizzazione**

Questi dispositivi sono dotati di un client specifico per la gestione degli endpoint e dei dispositivi mobili, siano essi on-premise o in cloud. La presenza di un client di gestione consente all’organizzazione di assicurarsi che il dispositivo sia aggiornato, protetto da sistemi antivirus, anti-malware ed EDR/XDR, e conforme alle policy di sicurezza. Inoltre, permette di controllare il software installato, operare remotamente sul dispositivo e applicare policy per garantire la sicurezza, nonché configurare l’accesso alla rete.

Questo rappresenta il livello più alto di protezione possibile, poiché i dispositivi possono essere resi sicuri tramite l’applicazione delle policy di conformità prima di concedere l’accesso ai sistemi. Di solito, questi dispositivi sono di proprietà dell’organizzazione, ma potrebbero essere inclusi anche dispositivi personali con il consenso del proprietario, che deve accettare una riduzione del controllo sul proprio dispositivo. I dispositivi particolarmente critici, come quelli utilizzati dagli amministratori di sistema, possono essere integrati con tecnologie di Security Information and Event Management (SIEM) per raccogliere dettagli sugli eventi del dispositivo e correlare queste informazioni con altre attività di rete, al fine di individuare potenziali segnali di attacco.

### **Dispositivi con gestione limitata**

Questi dispositivi utilizzano sistemi di endpoint management limitato, come antivirus, anti-malware o EDR con console di gestione centralizzata. Sebbene il livello di sicurezza e controllo non sia paragonabile a quello dei dispositivi completamente gestiti, è comunque possibile intervenire in caso di incidente, ad esempio disconnettendo il dispositivo dalla rete aziendale o rimuovendo minacce identificate. Questa categoria può includere dispositivi personali, oltre a quelli aziendali, purché siano dotati di agenti software adeguati. Il livello di fiducia è intermedio, consentendo un certo grado di accesso ai sistemi aziendali, ma con restrizioni in funzione del profilo di rischio.

### **Dispositivi non gestiti**

Questa categoria include dispositivi privi di agenti di gestione o con agenti che non sono sotto il controllo dell’organizzazione. Tipicamente, si tratta di dispositivi personali, dispositivi dei fornitori o altri dispositivi esterni che non sono stati integrati nella gestione centralizzata dell’organizzazione. Tali dispositivi non sono considerati affidabili e il loro accesso alla rete e ai sistemi dell’organizzazione deve essere limitato, per evitare il rischio di compromissioni e movimenti laterali che potrebbero compromettere altri dispositivi connessi alla rete.

Gli accessi dei dispositivi sono strettamente correlati alle modalità di accesso alla rete dell’organizzazione, un aspetto che sarà trattato più approfonditamente nella sezione dedicata alla gestione della rete e degli accessi. La questione di come permettere l’accesso a utenti con dispositivi non gestiti rappresenta una sfida complessa, ma può essere affrontata mediante l’uso di macchine virtuali o infrastrutture di desktop virtuale (VDI), ospitate su infrastrutture gestite dall’organizzazione. In questo ...