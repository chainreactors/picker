---
title: Il blackout CrowdStrike del luglio 2024 – Il settore sanitario in ginocchio
url: https://www.ictsecuritymagazine.com/notizie/crowdstrike-itdisaster/
source: ICT Security Magazine
date: 2025-07-22
fetch_date: 2025-10-06T23:51:06.699413
---

# Il blackout CrowdStrike del luglio 2024 – Il settore sanitario in ginocchio

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

![Il blackout CrowdStrike del luglio 2024 - Il settore sanitario in ginocchio](https://www.ictsecuritymagazine.com/wp-content/uploads/crowdstrike-sanita.jpeg)

# Il blackout CrowdStrike del luglio 2024 – Il settore sanitario in ginocchio

A cura di:[Redazione](#molongui-disabled-link)  Ore 21 Luglio 202524 Luglio 2025

Il 19 luglio 2024 ha segnato quello che molti esperti definiscono **la più grande interruzione IT nella storia dell’informatica**. Un singolo aggiornamento software difettoso di CrowdStrike ha paralizzato 8,5 milioni di dispositivi Windows a livello globale, causando danni economici superiori ai 10 miliardi di dollari e rivelando vulnerabilità sistemiche paragonabili ai più devastanti cyberattacchi della storia. Il settore sanitario statunitense ha pagato il prezzo più alto, con perdite stimate di 1,94 miliardi di dollari, dimostrando quanto la moderna assistenza medica dipenda da infrastrutture digitali fragili e interconnesse.

## L’errore che fermò il mondo digitale

#### Anatomia del disastro tecnico

**Alle 04:09 UTC del 19 luglio 2024**, CrowdStrike ha rilasciato quello che sembrava un normale aggiornamento di routine per il suo software di sicurezza Falcon. L’aggiornamento riguardava il **Channel File 291** (C-00000291\*.sys), un componente progettato per rilevare tecniche di attacco malevole attraverso le named pipe di Windows. Tuttavia, un errore apparentemente banale ha trasformato questo aggiornamento in un’arma di distruzione digitale di massa.

La causa root dell’incidente risiede in un **errore di validazione dell’IPC Template Type**. Il codice del sensore forniva solo 20 input di dati quando il template ne richiedeva 21, causando un accesso alla memoria oltre i limiti dell’array (out-of-bounds memory read). Questo errore ha provocato una **PAGE\_FAULT\_IN\_NONPAGED\_AREA**, il temuto Blue Screen of Death che ha mandato in crash milioni di sistemi Windows simultaneamente.

#### La propagazione globale del caos

L’orario dell’incidente – ore 04:09 UTC – ha amplificato l’impatto globale, colpendo durante l’orario lavorativo in Oceania e Asia, le prime ore del mattina in Europa e la mezzanotte nelle Americhe. **Entro 78 minuti**, CrowdStrike aveva identificato il problema e rilasciato una correzione, ma il danno era ormai fatto. Gli 8,5 milioni di dispositivi colpiti rappresentavano meno dell’1% di tutti i dispositivi Windows globali, ma erano concentrati in settori critici: sanità, trasporti, servizi finanziari ed emergenze.

Il processo di ripristino si è rivelato un incubo logistico. Ogni macchina compromessa richiedeva un **intervento manuale** di 15-20 minuti, eseguito in modalità sicura, spesso complicato dalla necessità di inserire chiavi di recupero BitLocker da 48 caratteri. Tuttavia, CrowdStrike e Microsoft hanno successivamente sviluppato strumenti automatizzati per accelerare il processo di ripristino, incluso il Microsoft Recovery Tool che ha permesso il recupero automatico tramite Windows PE. Per alcune organizzazioni come Providence Health, con 40.000 computer colpiti, il recovery completo ha richiesto **fino a quattro settimane**.

## Il settore sanitario in ginocchio

#### L’impatto devastante sui sistemi ospedalieri

Il settore sanitario statunitense ha subito le conseguenze più severe dell’incidente CrowdStrike, con **perdite economiche stimate di 1,94 miliardi di dollari** – il danno settoriale più elevato registrato. Sebbene la cifra specifica di “760 ospedali” non sia stata verificabile attraverso fonti ufficiali, l’impatto è stato comunque massivo: CrowdStrike serve il 60% dei principali fornitori sanitari USA e opera su oltre un milione di dispositivi nelle organizzazioni sanitarie americane.

I sistemi compromessi hanno toccato ogni aspetto dell’assistenza ospedaliera moderna. I sistemi di accesso alle cartelle cliniche elettroniche (EMR/EHR) sono stati gravemente compromessi: mentre Epic Systems ha chiarito che l’aggiornamento CrowdStrike non ha influito direttamente sui propri software o servizi, i problemi tecnici hanno impedito alle organizzazioni sanitarie di utilizzare workstation e sistemi data center per accedere a Epic, costringendo migliaia di ospedali a tornare alla documentazione cartacea. I sistemi di monitoraggio vitale dei pazienti, incluso il monitoraggio dei segni vitali dei neonati al Kaiser San Jose Medical Center, hanno smesso di funzionare, creando potenziali rischi per la sicurezza dei pazienti più vulnerabili.

#### Le cancellazioni di massa e le procedure d’emergenza

L’impatto operativo è stato immediato e drammatico. **Mass General Brigham** ha cancellato tutte le procedure non urgenti, chirurgie e visite mediche, con 45.000 dispositivi offline nel sistema. Il **Memorial Sloan Kettering Cancer Center** ha rimandato tutte le procedure che richiedevano anestesia, mentre **Emory Healthcare** ha dovuto ritardare interventi chirurgici in centri ambulatoriali e ospedali.

La risposta di emergenza ha dimostrato sia la preparazione che la vulnerabilità del sistema sanitario. **Kaiser Permanente** ha attivato il comando nazionale di emergenza alle 4:30 AM del Pacifico, mentre Providence Health, con il CIO B.J. Moore che ha definito l’evento **“peggio di un cyberattacco”**, ha dovuto gestire il crash di 15.000 server applic...