---
title: Ransomware: Le contromisure
url: https://www.ictsecuritymagazine.com/articoli/ransomware-le-contromisure/
source: ICT Security Magazine
date: 2024-07-23
fetch_date: 2025-10-06T17:45:49.517891
---

# Ransomware: Le contromisure

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

![Scopri come difenderti dal ransomware: strategie di backup, contromisure avanzate e rischi emergenti analizzati dal Prof. Fabrizio Baiardi](https://www.ictsecuritymagazine.com/wp-content/uploads/ransomware-contromisure.jpg)

# Ransomware: Le contromisure

A cura di:[Fabrizio Baiardi](#molongui-disabled-link)  Ore 22 Luglio 202426 Settembre 2025

Come per tutti i problemi complessi con cause molteplici, non esiste una soluzione per il ransomware che sia contemporaneamente semplice, efficace ed economica. In generale, possiamo distinguere tra contromisure basate sul ripristino dei dati criptati da una intrusione e quelle che mirano a contenere l’intrusione prima del suo successo completo.

### Il backup come contromisura

Le contromisure basate sul ripristino dei dati sono efficaci solo [quando l’attaccante non ricorre a double extortion](https://www.ictsecuritymagazine.com/articoli/le-peculiarita-delle-intrusioni-ransomware/) o comunque non minaccia la pubblicazione dei dati esfiltrati. La base di queste contromisure sono le copie di backup dei dati. Ovviamente, tali copie vanno difese impedendo che, come quasi sempre accade, l’attaccante le elimini durante la sua intrusione. Una difesa possibile sono strategie come la 3-2-1, che prevede l’utilizzo di almeno tre copie dei dati memorizzate su due supporti diversi, di cui almeno una non in linea o su un altro sistema; non in linea vuol dire non collegato ad una rete e non semplicemente spento, visto che alcuni ransomware possono forzare il boot di una macchina per criptarne le informazioni.

La strategia 3-2-1 è talmente efficace che la gang Lockbit la usa per proteggere le informazioni sui propri malware: ma è difficile garantire l’aggiornamento istantaneo e continuo delle copie, soprattutto di quella non online. Ergo, tutti i dati non ancora memorizzati sulla copia non online potranno andare persi, aumentando il tempo di ripristino.

Una seconda strategia di difesa prevede l’uso di memorie immutabili. Si tratta di memorie worm, write once read many, in cui ogni operazione può essere scritta ma non aggiornata. In generale, la proprietà worm viene garantita in modo nativo da CD-r o DvD-r, oppure utilizzando degli interruttori o delle chiavi fisiche che impediscono l’aggiornamento del supporto fisico di memoria.

Memorie worm, ormai messe comunemente a disposizione dai fornitori di servizi cloud, possono essere usate per memorizzare backup; ma sono anche stati sviluppati file system che utilizzano questi dispositivi e che offrono all’utente una interfaccia completamente standard. Sostanzialmente, ogni scrittura di una pagina fisica del file system provoca non la modifica della stessa ma l’allocazione e la scrittura di una nuova pagina. In questo modo, il dispositivo conserva tutte le pagine già scritte e la copia di backup è prodotta automaticamente, pertanto non può essere cancellata.

### La robustezza come contromisura

Una soluzione più generale e proattiva cerca di bloccare l’intrusione prima che abbia successo. Ciò richiede l’adozione di difese standard, cioè non specializzate per il ransomware. Tra queste strategie ricordiamo:

* l’aumento della security awarness degli utenti;
* una politica di patching per le vulnerabilità più critiche;
* la classificazione delle informazioni;
* la minimizzazione dei diritti assegnati ad ogni utente;
* il privilegio minimo;
* la segmentazione delle reti.

In particolare, la segmentazione delle reti e la separazione delle varie sottoreti mediante firewall è una delle contromisure più efficaci per il contenimento della [diffusione del malware](https://arxiv.org/abs/1911.02423) sia nel caso in cui attaccanti usino una piattaforma di attacco automatizzata, sia in quello di human operated ransomware. Le strategie che le varie gang usano nelle loro intrusioni dimostrano che la segmentazione può determinare un aumento significativo del tempo per la raccolta di informazioni e di quello per criptarle, aumentando così il tempo a disposizione dei difensori.

Una forma estrema di segmentazione è l’air gap, cioè l’impossibilità di due reti di interagire come richiesto dalla strategia 3-2-1 discussa in precedenza. Un’altra contromisura efficace − soprattutto nel caso di ransomware che esfiltri le informazioni − è l’egress filtering, cioè il filtraggio delle comunicazioni in uscita per individuare comunicazioni anomale in termini di quantità o di destinatari. Tenendo conto che molte gang hanno sfruttato vulnerabilità in sistemi per VPN, in prospettiva, anche soluzioni zero trust potranno essere adottate per respingere intrusioni che sfruttano credenziali rubate o device infettati al di fuori del perimetro aziendale.

Sostanzialmente, la soluzione più generale per contrastare il ransomware non è diversa da quella per contrastare altre minacce ed è basato su una lista di meccanismi e strategie che gli esperti di sicurezza informatica suggeriscono da tempo ma che le organizzazioni, dalle più piccole alle più grandi, non riescono ad adottare. Questo può in parte essere dovuto ai meccanismi di scelta dei responsabili della sicurezza, che privilegiano persone interne all’organizzazione rispetto a quelle in possesso delle competenze necessarie.

Delegare a ditte esterne l’installazione, gestione e manutenzione di strument...