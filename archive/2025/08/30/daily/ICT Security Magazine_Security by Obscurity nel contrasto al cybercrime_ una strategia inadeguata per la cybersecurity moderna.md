---
title: Security by Obscurity nel contrasto al cybercrime: una strategia inadeguata per la cybersecurity moderna
url: https://www.ictsecuritymagazine.com/articoli/security-by-obscurity/
source: ICT Security Magazine
date: 2025-08-30
fetch_date: 2025-10-07T00:48:34.206034
---

# Security by Obscurity nel contrasto al cybercrime: una strategia inadeguata per la cybersecurity moderna

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

![rischi della security by obscurity nella cybersecurity moderna con alternative raccomandate da NIST e OWASP](https://www.ictsecuritymagazine.com/wp-content/uploads/ybe-12_MjDjZujA.png)

# Security by Obscurity nel contrasto al cybercrime: una strategia inadeguata per la cybersecurity moderna

A cura di:[Redazione](#molongui-disabled-link)  Ore 29 Agosto 20254 Luglio 2025

Nel panorama contemporaneo della cybersecurity, caratterizzato da minacce in costante evoluzione e attacchi sempre più sofisticati, l’approccio noto come “security by obscurity” o “sicurezza tramite oscuramento” rappresenta una metodologia controversa e spesso inefficace. Questo articolo esamina criticamente tale strategia, analizzandone le limitazioni intrinseche, i rischi associati e le alternative più efficaci nel contesto della protezione contro il cybercrime. Attraverso un’analisi approfondita della letteratura scientifica e delle raccomandazioni istituzionali, si dimostra come la security by obscurity non debba mai costituire il pilastro principale di una strategia di cybersecurity.

## Security by Obscurity: definizione e rischi nella cybersecurity moderna

La security by obscurity, definita come la pratica di nascondere i dettagli o i meccanismi di un sistema per migliorarne la sicurezza, ha radici storiche profonde nella crittografia militare e civile. Il principio di Kerckhoffs, formulato nel 1883, stabiliva che un sistema crittografico dovrebbe essere sicuro anche se tutto del sistema, eccetto la chiave, è di conoscenza pubblica³. Questo principio fondamentale ha plasmato l’approccio moderno alla cybersecurity, mettendo in discussione l’efficacia dell’oscuramento come strategia primaria di difesa.

Nel contesto odierno del cybercrime, dove il costo globale è stimato a quasi 1 trilione di dollari nel 2020, con un incremento superiore al 50% rispetto al 2018¹, è cruciale comprendere perché la security by obscurity rappresenti un approccio fondamentalmente inadeguato come strategia principale di protezione.

#### **Definizione e caratteristiche della Security by Obscurity**

#### Concetti fondamentali

La security by obscurity è la pratica di nascondere i dettagli o i meccanismi di un sistema per migliorarne la sicurezza, basandosi sul principio di nascondere qualcosa in piena vista, simile ai giochi di prestigio di un mago o all’uso del camuffamento². Questa metodologia diverge dai metodi di sicurezza tradizionali e si concentra sull’offuscare informazioni o caratteristiche per scoraggiare potenziali minacce.

#### Esempi pratici nel cybercrime

Nel panorama del cybercrime contemporaneo, la security by obscurity si manifesta in diverse forme:

* **Nascondere interfacce amministrative**: Modificare gli URL di default delle pagine di amministrazione
* **Offuscamento del codice**: Rendere difficile la lettura del codice sorgente
* **Port knocking**: Nascondere servizi dietro sequenze di connessioni specifiche
* **Mascheramento delle tecnologie**: Rimuovere header HTTP che rivelano versioni di software

## **L’Opposizione istituzionale alla Security by Obscurity**

#### **Raccomandazioni del NIST**

Il National Institute of Standards and Technology (NIST) degli Stati Uniti raccomanda esplicitamente contro questa pratica: “La sicurezza del sistema non dovrebbe dipendere dalla segretezza dell’implementazione o dei suoi componenti”⁴. Questa posizione istituzionale si basa su evidenze empiriche e ricerche approfondite che dimostrano l’inefficacia dell’oscuramento come strategia primaria.

#### **Common Weakness Enumeration (CWE-656)**

Il progetto Common Weakness Enumeration elenca “Reliance on Security Through Obscurity” come CWE-656, definendola come una debolezza che si verifica quando un prodotto utilizza un meccanismo di protezione la cui forza dipende pesantemente dalla sua oscurità⁵. Questa classificazione ufficiale sottolinea come l’affidamento primario sull’oscuramento sia riconosciuto a livello internazionale come una vulnerabilità significativa.

#### **Principi OWASP**

L’Open Web Application Security Project (OWASP) stabilisce chiaramente che “la security by obscurity non dovrebbe mai essere utilizzata come unico meccanismo di sicurezza”⁶. Tra i dieci principi fondamentali di sicurezza OWASP, il principio “Avoid security by obscurity” occupa una posizione centrale, enfatizzando l’importanza di controlli di sicurezza solidi indipendenti dall’occultamento.

## Analisi critica: perché la Security by Obscurity Fallisce

#### Vulnerabilità intrinseche

La security by obscurity presenta diverse vulnerabilità fondamentali che la rendono inadeguata come strategia primaria:

1. **Falso senso di sicurezza**

L’affidamento esclusivo sull’oscurità può portare a un falso senso di sicurezza, poiché una volta che “il gatto è fuori dal sacco”, la sicurezza può essere severamente compromessa⁷. Questa caratteristica rappresenta un rischio sistemico significativo nelle infrastrutture critiche.

2. **Facilità di Reverse Engineering**

Nel panorama contemporaneo del cybercrime, gli attaccanti dispongono di strumenti sofisticati per il reverse engineering. La pubblicazione di algoritmi crittografici non compromette la sicurezza, poiché è solo questione di tempo prima che un attaccante scopra come funziona il sistema crittografi...