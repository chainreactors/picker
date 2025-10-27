---
title: Attacchi informatici alle app di dating: furto di immagini intime e sextortion
url: https://www.ictsecuritymagazine.com/notizie/app-di-dating/
source: ICT Security Magazine
date: 2025-08-26
fetch_date: 2025-10-07T00:49:13.813903
---

# Attacchi informatici alle app di dating: furto di immagini intime e sextortion

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

![App di dating utilizzate per truffe di sextortion e romance scam con furto di dati personali sensibili](https://www.ictsecuritymagazine.com/wp-content/uploads/freepik__a-digital-illustration-of-a-dating-app-icon-morphi__5755.jpeg)

# Attacchi informatici alle app di dating: furto di immagini intime e sextortion

A cura di:[Redazione](#molongui-disabled-link)  Ore 25 Agosto 202517 Luglio 2025

Le app di dating raccolgono vaste quantità di dati personali e sensibili, rendendosi terreno fertile per truffe di *sextortion* e simili. I truffatori online creano falsi profili o sfruttano vulnerabilità tecniche per agganciare le vittime su piattaforme come Tinder, Snapchat, Instagram ecc. Attraverso messaggi persuasivi (romance scam) o phishing mirati, indurranno gli utenti a condividere foto/video privati. In molti casi le vittime vengono convinte a spogliarsi in videochat segrete: le registrazioni compromettenti vengono poi usate per estorcere denaro. Studi recenti confermano che le app di incontri sono attualmente “esche” ideali per criminali: per esempio, Tavakoli et al. riportano che nel loro campione il 62,7% degli utenti intervistati aveva subito tentativi di sextortion tramite altri utenti di dating app.

* **Phishing e social engineering.** I truffatori spesso contattano le vittime tramite chat o email simulando l’interesse romantico. Successivamente propongono di passare a videochat private, persuadendo la persona a mostrarsi nuda o in pose sessualmente esplicite. Le sessioni vengono registrate all’insaputa della vittima e usate per ricattarla. Alcuni schemi sono automatizzati via spam email: per esempio messaggi di sextortion fingono di essere hacker professionisti che hanno installato un *Trojan* sul computer della vittima, spiano le sue attività online e minacciano di pubblicare immagini compromettenti. Tali campagne di phishing sfruttano tecniche di ingegneria sociale spietata, facendo leva sulla vergogna, la paura e il ricatto emotivo.
* **Vulnerabilità delle API.** Molte dating app dipendono da servizi backend e API web. Se queste API non impongono corretti controlli di accesso, è possibile accedere a dati sensibili senza autorizzazione (Broken Object Level Authorization). Ad esempio, è stato documentato come popolari app di dating restituiscano nelle risposte API informazioni non filtrate: l’utente può decidere di mostrare solo la propria età nell’interfaccia, ma l’API può restituire l’intera data di nascita e altri dati privati. Un attaccante può bypassare i filtri sul client e inviare richieste dirette alle API per ottenere informazioni private (foto, posizione, dati profilo). Questa esposizione eccessiva dei dati personali facilita successivamente la profilazione delle vittime e potenziali estorsioni.
* **Malware.** Anche il malware mobile può facilitare il furto di immagini intime. Software dannosi (keylogger, trojan, RAT) possono infettare dispositivi vittime tramite app contraffatte o siti compromessi. Un’esca tipica è un’applicazione falsa di dating o un aggiornamento software ingannevole che, una volta installato, registra la telecamera, intercetta file o screenshot, e invia il materiale allo straniero dietro la truffa. Anche se il malware puro non è l’unico vettore, le campagne di sextortion spesso menzionano tecnicismi (es. “sono entrato nel tuo sistema con un Trojan”) per intimorire. Questo rafforza l’illusione che le immagini siano state rubate di nascosto, legittimando la richiesta di riscatto.
* **Altri metodi di social engineering.** Oltre al phishing diretto, esistono varianti più sofisticate: profili falsi (catfish), deepfake sessuali, ricatti minacciando di coinvolgere familiari o autorità. Talvolta il ricattatore afferma che il partner “virtuale” fosse minorenne, spaventando la vittima con implicazioni legali. L’elemento comune è la costruzione di fiducia iniziale, che induce la vittima a condividere contenuti privati o a pagare, sotto la minaccia di rovina reputazionale e morale.

## Conseguenze giuridiche per app di dating e sextortion

La sextortion è perseguibile penalmente. In Italia il ricatto basato su foto o video privati ricade nell’**estorsione** (art. 629 c.p.), aggravata se con minacce su reputazione e dati sensibili. Inoltre entrano in gioco i reati di **interferenze illecite nella vita privata** (art. 615-bis c.p.) quando si registrano o diffondono immagini intime senza consenso. Gli autori affrontano pene severe (di norma dai 6 ai 10 anni per l’estorsione) e rischiano ulteriori contestazioni (ad esempio, *truffa informatica* se sono entrati abusivamente nei dispositivi). Anche chi detiene involontariamente tali materiali può essere accusato di detenzione di pornografia illegale, specie in presenza di minori.

Dal punto di vista civile e normativo, i gestori delle app di dating hanno obblighi stringenti. Queste piattaforme trattano **dati personali sensibili** (orientamento sessuale, foto intime ecc.), pertanto sono soggette al GDPR (Regolamento UE 2016/679) e al Codice Privacy italiano. Una falla nella sicurezza (ad es. una violazione del database utenti) può comportare ingenti sanzioni amministrative: l’ammenda massima prevista arriva fino a 20 milioni di euro o al 4% del fatturato annuo mondiale, a seconda di quale cifra sia maggiore.

Esempi c...