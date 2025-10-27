---
title: Ransomware asimmetrico e data exfiltration: l’evoluzione delle minacce nella sicurezza informatica
url: https://www.ictsecuritymagazine.com/articoli/ransomware-asimmetrico/
source: ICT Security Magazine
date: 2025-07-29
fetch_date: 2025-10-06T23:56:51.275476
---

# Ransomware asimmetrico e data exfiltration: l’evoluzione delle minacce nella sicurezza informatica

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

![ransomware asimmetrico con tecniche di doppia estorsione e strategie di difesa cyber per organizzazioni moderne](https://www.ictsecuritymagazine.com/wp-content/uploads/ybe-1_qM9a51r4.png)

# Ransomware asimmetrico e data exfiltration: l’evoluzione delle minacce nella sicurezza informatica

A cura di:[Redazione](#molongui-disabled-link)  Ore 28 Luglio 202528 Luglio 2025

Il panorama delle minacce informatiche sta vivendo una trasformazione radicale che ha portato il ransomware ben oltre la sua forma tradizionale. Non parliamo più semplicemente di malware che cripta i file delle vittime in attesa di un riscatto, ma di una vera e propria evoluzione strategica che ha trasformato gli attacchi in sofisticate operazioni di estorsione multipla.

Questa metamorfosi è testimoniata da numeri che non lasciano spazio a interpretazioni: negli Stati Uniti, i primi cinque settimane del 2025 hanno registrato [un incremento del 149%](https://cyble.com/blog/u-s-ransomware-attacks-surge-to-start-2025/) degli [attacchi ransomware](https://www.ictsecuritymagazine.com/articoli/ecosistema-ransomware/) rispetto allo stesso periodo dell’anno precedente, con 378 incidenti documentati contro i 152 del 2024. Ma dietro questi numeri si cela una realtà ancora più preoccupante: gli attaccanti hanno sviluppato metodologie che combinano la crittografia asimmetrica avanzata con l’esfiltrazione sistematica dei dati, creando un doppio ricatto che mette le organizzazioni in una posizione di estrema vulnerabilità.

L’emergere delle strategie di “doppia estorsione” e “tripla estorsione” rappresenta un cambiamento di paradigma fondamentale. Gli attaccanti non si limitano più a rendere inaccessibili i dati delle vittime, ma li sottraggono preventivamente, minacciando di renderli pubblici nel caso in cui il riscatto non venga pagato. Questa evoluzione ha creato un dilemma impossibile per le organizzazioni: anche possedendo backup perfettamente funzionanti, rimangono esposte al rischio di vedere i propri dati sensibili diffusi pubblicamente, con conseguenze devastanti per la reputazione, la conformità normativa e la continuità operativa.

## La nuova anatomia del ransomware: tecnologie e metodologie

#### L’architettura crittografica ibrida: quando velocità e sicurezza si incontrano

Il ransomware contemporaneo rappresenta un esempio di sofisticazione tecnica che combina il meglio di due mondi crittografici apparentemente incompatibili. Gli sviluppatori di malware hanno risolto l’antica dicotomia tra velocità e sicurezza attraverso l’implementazione di sistemi crittografici ibridi che sfruttano simultaneamente algoritmi simmetrici e asimmetrici.

In pratica, questi sistemi utilizzano algoritmi di crittografia simmetrica come AES-256, Salsa20 o ChaCha20 per la cifratura massiva dei file, garantendo prestazioni elevate anche su volumi di dati considerevoli. Parallelamente, impiegano algoritmi asimmetrici come RSA-2048 o ECDH per proteggere le chiavi simmetriche utilizzate nel processo di cifratura. Questa metodologia elimina le tradizionali limitazioni: la crittografia simmetrica assicura velocità di elaborazione ottimali per grandi quantità di dati, mentre quella asimmetrica garantisce che le chiavi di decifratura rimangano sotto il controllo esclusivo degli attaccanti, senza necessità di comunicazione con server esterni durante la fase di attacco.

Il risultato è un sistema che può operare completamente offline, riducendo le possibilità di detection durante la fase di deployment, ma che mantiene standard di sicurezza crittografica praticamente inviolabili senza la collaborazione degli attaccanti.

#### L’arte dell’esfiltrazione invisibile: quando rubare diventa un’arte

Parallelamente all’evoluzione crittografica, gli attaccanti hanno perfezionato tecniche di esfiltrazione dati che raggiungono livelli di sofisticazione impressionanti. Il tasso di esfiltrazione dati negli attacchi ransomware è balzato al 94% nel 2024, segnando il record più alto mai registrato e testimoniando come questa pratica sia diventata standard piuttosto che eccezione.

Le metodologie di esfiltrazione si sono evolute ben oltre il semplice trasferimento di file attraverso connessioni internet. Gli attaccanti moderni impiegano tecniche di steganografia avanzata, nascondendo dati sensibili all’interno di contenuti multimediali apparentemente innocui che possono attraversare i sistemi di sicurezza senza destare sospetti. Il DNS tunneling è diventato un’altra tecnica prediletta: sfruttando il protocollo DNS, normalmente considerato traffico legittimo, gli attaccanti possono esfiltare informazioni in modo graduale e pressoché invisibile.

Particolarmente insidiosa è la pratica del “cloud storage abuse”, dove vengono sfruttati servizi cloud legittimi per il trasferimento di grandi volumi di dati. Questa tecnica è difficile da rilevare perché utilizza infrastrutture e protocolli che fanno parte del normale funzionamento aziendale. Infine, l’approccio “Living off the Land” (LOTL) permette agli attaccanti di utilizzare strumenti amministrativi già presenti nei sistemi target, rendendo l’esfiltrazione praticamente indistinguibile dalle normali attività di gestione del sistema.

## Le strategie di estorsione multipla: quando un ricatto non basta

#### La doppia estorsio...