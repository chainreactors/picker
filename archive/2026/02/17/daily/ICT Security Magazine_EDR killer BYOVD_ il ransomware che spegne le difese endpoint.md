---
title: EDR killer BYOVD: il ransomware che spegne le difese endpoint
url: https://www.ictsecuritymagazine.com/cyber-crime/edr-killer-byovd-endpoint/
source: ICT Security Magazine
date: 2026-02-17
fetch_date: 2026-02-18T04:16:10.657893
---

# EDR killer BYOVD: il ransomware che spegne le difese endpoint

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
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![EDR killer BYOVD il ransomware che spegne le difese endpoint](https://www.ictsecuritymagazine.com/wp-content/uploads/EDR-killer-BYOVD-il-ransomware-che-spegne-le-difese-endpoint.jpeg)

# EDR killer BYOVD: il ransomware che spegne le difese endpoint

A cura di:[Redazione](#molongui-disabled-link)  Ore 17 Febbraio 2026

**EDR killer BYOVD** non è un concetto nuovo. Ma nel febbraio 2026 è diventato qualcosa di diverso: non più una tecnica di nicchia riservata ai gruppi APT più sofisticati, bensì lo strumento standard – quasi banale – con cui il ransomware acceca le difese endpoint prima ancora di cifrare il primo file.

Nelle prime due settimane di febbraio 2026 sono accaduti due eventi che, presi insieme, segnano un punto di non ritorno. Il primo: [Huntress](https://www.huntress.com/blog/encase-byovd-edr-killer) ha documentato un’intrusione in cui gli attaccanti hanno utilizzato un driver del tool forense EnCase – con certificato scaduto nel 2010 e successivamente revocato – per terminare 59 prodotti di sicurezza endpoint dalla modalità kernel. Il secondo: il [Symantec and Carbon Black Threat Hunter Team](https://www.security.com/threat-intelligence/black-basta-ransomware-byovd) ha rivelato che un ransomware emergente battezzato Reynolds ha integrato un driver vulnerabile direttamente nel proprio payload, fondendo evasione difensiva e cifratura in un unico binario.

La convergenza di questi due episodi racconta una storia che va ben oltre il singolo incidente. Racconta il fallimento strutturale di un modello di sicurezza endpoint su cui le organizzazioni hanno investito miliardi, e che gli attaccanti stanno imparando a spegnere con un driver firmato di vent’anni fa.

## Che cos’è il BYOVD e perché funziona ancora nel 2026

La tecnica [Bring Your Own Vulnerable Driver](https://www.ictsecuritymagazine.com/articoli/bring-your-own-vulnerable-driver-byovd/) – BYOVD – è concettualmente disarmante nella sua semplicità. L’attaccante non scrive un driver malevolo, non cerca di aggirare la firma digitale, non sfrutta uno zero-day nel kernel. Porta con sé un driver perfettamente legittimo, firmato da un vendor riconosciuto, che contiene una vulnerabilità nota. Poiché il driver è firmato, Windows lo carica senza protestare. Una volta in esecuzione nello spazio kernel, l’attaccante sfrutta la falla del driver per terminare i processi di sicurezza con privilegi di sistema.

Il meccanismo tecnico si articola in passaggi precisi. Il malware deposita il driver vulnerabile su disco, tipicamente mascherandolo come componente OEM legittimo. Registra il driver come servizio kernel di Windows, garantendosi persistenza al riavvio. Una volta caricato, il driver espone un’interfaccia IOCTL (Input/Output Control) che consente ai processi in user-mode di inviare comandi con privilegi kernel. A quel punto, il malware compila un elenco dei processi di sicurezza da terminare – nell’incidente documentato da Huntress, [l’elenco comprendeva 59 prodotti](https://www.helpnetsecurity.com/2026/02/05/edr-killer-vulnerable-encase-driver/) tra EDR e antivirus – e li uccide uno per uno, in un ciclo continuo con intervallo di un secondo che impedisce qualsiasi riavvio automatico del processo protettivo.

Il risultato è che l’attaccante opera “al buio”: nessun alert, nessuna telemetria, nessun rilevamento comportamentale. L’EDR non è stato aggirato; è stato spento.

Ciò che rende questa tecnica devastante nel 2026 non è la sua novità – il BYOVD è documentato da anni nel framework [MITRE ATT&CK](https://attack.mitre.org/) sotto T1068 e T1562.001 – ma la sua industrializzazione. Come ha osservato Broadcom/Symantec nel report sul ransomware Reynolds, il BYOVD è oggi di gran lunga la tecnica di evasione difensiva più utilizzata dagli operatori ransomware.

#### Il caso Huntress: un driver forense del 2006 che spegne 59 EDR nel 2026

All’inizio di febbraio 2026, i ricercatori di Huntress hanno risposto a un incidente che illustra perfettamente il paradosso del BYOVD. Gli attaccanti hanno ottenuto l’accesso iniziale tramite credenziali compromesse di una VPN SonicWall SSL priva di autenticazione multifattore. Fin qui, nulla di sorprendente: credenziali rubate e assenza di MFA sono il biglietto d’ingresso standard per il ransomware nel 2026.

La fase successiva è quella che merita attenzione. Gli attaccanti hanno distribuito un EDR killer personalizzato che conteneva, codificato al suo interno, il driver kernel EnPortv.sys – un componente dell’EnCase forensic suite sviluppato da Guidance Software. Questo driver era stato firmato con un certificato emesso il 15 dicembre 2006, scaduto il 31 gennaio 2010 e successivamente revocato.

Eppure Windows lo ha caricato. Come è possibile?

La risposta sta in una scelta architetturale che Microsoft ha fatto nel 2015 per garantire la retrocompatibilità. A partire da Windows 10 versione 1607, tutti i nuovi driver kernel devono essere firmati tramite il Hardware Dev Center di Microsoft. Tuttavia, per non rompere il software legacy, è stata introdotta un’eccezione: i driver firmati con certificati emessi prima del 29 luglio 2015, che si concatenano a un’autorità di certificazione cross-signed supportata, possono ancora essere caricati. Il driver EnCase rientra pienamente in ...