---
title: Crittografia post-quantistica PQC: la transizione verso algoritmi resistenti al quantum computing
url: https://www.ictsecuritymagazine.com/articoli/pqc/
source: ICT Security Magazine
date: 2025-07-06
fetch_date: 2025-10-06T23:28:38.452936
---

# Crittografia post-quantistica PQC: la transizione verso algoritmi resistenti al quantum computing

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

![crittografia post-quantistica PQC NIST FIPS 203 204 205 algoritmi quantum-resistant ML-KEM ML-DSA cybersecurity](https://www.ictsecuritymagazine.com/wp-content/uploads/ybe-1_Rhwz7Sjl.png)

# Crittografia post-quantistica PQC: la transizione verso algoritmi resistenti al quantum computing

A cura di:[Redazione](#molongui-disabled-link)  Ore 5 Luglio 20254 Luglio 2025

La crittografia post-quantistica (PQC) rappresenta uno dei pilastri fondamentali per la sicurezza informatica del futuro, configurandosi come risposta strategica all’imminente minaccia rappresentata dai computer quantistici crittograficamente rilevanti (CRQC). Con l’accelerazione della ricerca nel campo del quantum computing, la comunità della cybersecurity si trova di fronte alla necessità di ripensare radicalmente i paradigmi crittografici consolidati, implementando algoritmi resistenti alle capacità computazionali quantistiche.

## Standard NIST crittografia post-quantistica: Il quadro normativo 2024

Il National Institute of Standards and Technology (NIST) ha finalizzato il suo principale set di algoritmi di crittografia progettati per resistere agli attacchi informatici di un computer quantistico, pubblicando nell’agosto 2024 i primi tre standard FIPS (Federal Information Processing Standards) per la crittografia post-quantistica.

Gli standard pubblicati comprendono:

#### **FIPS 203 – Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM)**

FIPS 203 specifica uno schema crittografico chiamato Module-Lattice-Based Key-Encapsulation Mechanism Standard, derivato dalla submission CRYSTALS-KYBER. Questo meccanismo di incapsulamento delle chiavi rappresenta la soluzione primaria per la crittografia generale, caratterizzato da chiavi di crittografia relativamente piccole e velocità operativa ottimizzata.

Il ML-KEM supporta tre varianti parametriche:

* ML-KEM-512: livello di sicurezza 1 (equivalente ad AES-128)
* ML-KEM-768: livello di sicurezza 3 (equivalente ad AES-192)
* ML-KEM-1024: livello di sicurezza 5 (equivalente ad AES-256)

#### **FIPS 204 – Module-Lattice-Based Digital Signature Standard (ML-DSA)**

FIPS 204 specifica il Module-Lattice-Based Digital Signature Standard, derivato dalla submission CRYSTALS-Dilithium. Questo algoritmo, originariamente noto come CRYSTALS-Dilithium, costituisce lo standard primario per la protezione delle firme digitali, utilizzando un approccio basato su reticoli modulari.

#### **FIPS 205 – Stateless Hash-Based Digital Signature Standard (SLH-DSA)**

FIPS 205 specifica il Stateless Hash-Based Digital Signature Standard, derivato dalla submission SPHINCS+. Questo standard implementa un algoritmo di firma digitale basato su funzioni hash, progettato come metodo di backup nel caso in cui ML-DSA dovesse rivelarsi vulnerabile.

#### **L’algoritmo HQC come standard di backup**

HQC è stato selezionato per la standardizzazione l’11 marzo 2025, rappresentando il quinto algoritmo per la crittografia asimmetrica post-quantistica. “Le organizzazioni dovrebbero continuare a migrare i loro sistemi di crittografia agli standard che abbiamo finalizzato nel 2024. Stiamo annunciando la selezione di HQC perché vogliamo avere uno standard di backup basato su un approccio matematico diverso da ML-KEM”, ha dichiarato Dustin Moody, matematico del NIST.

#### **La minaccia “Harvest Now, Decrypt Later” e la sua rilevanza strategica**

La strategia “harvest now, decrypt later” è una strategia di sorveglianza che si basa sull’acquisizione e conservazione a lungo termine di dati crittografati attualmente illeggibili in attesa di possibili sviluppi nella tecnologia di decrittazione che li renderebbero leggibili in futuro.

## **Caratteristiche degli attacchi HNDL**

Gli attacchi HNDL presentano caratteristiche distintive che li rendono particolarmente insidiosi:

1. **Stealth operativo**: Uno degli aspetti più insidiosi degli attacchi HNDL è che non saprai quando i tuoi dati sono stati rubati. Gli attori delle minacce possono catturare dati crittografati ora e decrittarli anni dopo una volta che i computer quantistici lo permettono.
2. **Targeting strategico**: La strategia centrale di “harvest now, decrypt later” è semplice: raccogliere quanti più dati possibile e prepararsi a decrittarli in futuro. Questa è una strategia orientata agli obiettivi, e i cybercriminali sono tutt’altro che casuali nei loro sforzi.
3. **Valore temporale dei dati**: Attualmente, i segreti commerciali, l’intelligence aziendale e le tecnologie emergenti sono i dati più a rischio.

## **L’urgenza della transizione**

Alcuni segreti rimangono preziosi per molti anni. Anche se un avversario non può craccare la crittografia che protegge i nostri segreti al momento, potrebbe comunque essere vantaggioso catturare dati crittografati e conservarli, nella speranza che un computer quantistico riesca a violare la crittografia in futuro.

La finestra di vulnerabilità è già aperta, considerando che i dati sensibili crittografati oggi potrebbero essere compromessi quando i computer quantistici raggiungeranno una potenza sufficiente.

#### **Algoritmi di Shor e l’impatto sui sistemi crittografici attuali**

L’algoritmo di Shor, sviluppato nel 1994, rappresenta la minaccia principale per i sistemi crittografici attuali. L’algoritmo di S...