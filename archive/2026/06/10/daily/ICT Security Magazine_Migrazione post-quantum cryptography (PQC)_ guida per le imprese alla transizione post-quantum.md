---
title: Migrazione post-quantum cryptography (PQC): guida per le imprese alla transizione post-quantum
url: https://www.ictsecuritymagazine.com/cyber-security/migrazione-post-quantum-cryptography/
source: ICT Security Magazine
date: 2026-06-10
fetch_date: 2026-06-11T06:36:46.338746
---

# Migrazione post-quantum cryptography (PQC): guida per le imprese alla transizione post-quantum

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Migrazione post-quantum cryptography (PQC): guida per le imprese alla transizione post-quantum](https://www.ictsecuritymagazine.com/wp-content/uploads/2026-06-08_evergreen_migrazione-post-quantum-cryptography.jpg)

# Migrazione post-quantum cryptography (PQC): guida per le imprese alla transizione post-quantum

A cura di:[Redazione](#molongui-disabled-link)  Ore 10 Giugno 20268 Giugno 2026

Migrazione post-quantum cryptography (PQC): non si tratta più di un tema futuribile legato all’arrivo dei computer quantistici, ma di una trasformazione già necessaria per proteggere dati, comunicazioni e infrastrutture critiche. Con i primi standard NIST ormai definiti, il rischio “harvest now, decrypt later” già attivo e le roadmap europee orientate al 2030-2035, le organizzazioni sono chiamate ad avviare oggi un percorso strutturato basato su inventario crittografico, crypto-agility, sperimentazioni ibride e coinvolgimento della supply chain.

## Migrazione post-quantum cryptography (PQC): perché iniziare ora

La crittografia che protegge oggi comunicazioni, firme e dati a riposo si regge su problemi matematici, come la fattorizzazione di grandi numeri, che un computer quantistico sufficientemente potente sarebbe in grado di risolvere. Quel computer non esiste ancora, ma il conto alla rovescia per la migrazione alla crittografia post-quantistica (PQC, Post-Quantum Cryptography) è già partito, per due ragioni concrete: gli standard sono pronti e una parte della minaccia è già attiva oggi. Questa guida spiega perché iniziare adesso e come impostare una migrazione ordinata, senza allarmismi ma senza rinvii.

#### La minaccia “harvest now, decrypt later”

L’errore più comune è ragionare come se il rischio scattasse solo il giorno in cui esisterà un computer quantistico crittograficamente rilevante. In realtà una categoria di avversari agisce già oggi con la logica *harvest now, decrypt later*: raccogliere e archiviare ora il traffico cifrato e i dati sensibili, per decifrarli in futuro quando la capacità quantistica sarà disponibile. Questo sposta la scadenza dal “quando arriverà il quantum” al “quanto a lungo devono restare riservati i miei dati”. Informazioni con un ciclo di vita lungo, come segreti industriali, dati sanitari, atti coperti da segreto e chiavi di lunga durata, sono esposte da subito. È il motivo per cui l’attesa passiva non è una strategia.

#### Gli standard ci sono già

Il principale ostacolo storico alla migrazione, l’assenza di algoritmi standardizzati, è caduto. Il 13 agosto 2024 il NIST (National Institute of Standards and Technology statunitense) ha pubblicato i [primi tre standard PQC](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) definitivi. Il FIPS 203 definisce ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism, derivato da CRYSTALS-Kyber), il meccanismo di incapsulamento delle chiavi destinato a sostituire lo scambio di chiavi basato su RSA ed ECC. Il FIPS 204 definisce ML-DSA (Module-Lattice-Based Digital Signature Algorithm, da CRYSTALS-Dilithium), lo schema di firma digitale principale. Il FIPS 205 definisce SLH-DSA (Stateless Hash-Based Digital Signature Algorithm, da SPHINCS+), una firma basata su funzioni hash pensata come alternativa di riserva nel caso emergessero debolezze nell’approccio a reticoli.

A questi si è aggiunto, l’11 marzo 2025, HQC (Hamming Quasi-Cyclic), selezionato dal NIST come secondo meccanismo di incapsulamento delle chiavi: si basa su codici correttori d’errore, una matematica diversa da quella a reticoli di ML-KEM, e funge da rete di sicurezza qualora il primo schema venisse compromesso. La bozza dello standard HQC è attesa entro il 2026 e la versione definitiva nel 2027. La logica della doppia famiglia, reticoli e codici, è deliberata: non concentrare tutta la fiducia su un’unica ipotesi matematica.

Resta atteso un ulteriore standard di firma, FN-DSA (derivato da FALCON), utile dove servono firme particolarmente compatte. La scelta tra gli schemi non è indifferente: ML-KEM e ML-DSA, basati su reticoli, offrono un buon equilibrio tra dimensioni e prestazioni e si prestano all’uso generale; SLH-DSA, basato su funzioni hash, è più conservativo e resistente nel lungo periodo ma produce firme più grandi e lente, adatte a casi come la firma del firmware; HQC, più oneroso in termini di banda, ha senso come riserva. Conoscere queste differenze evita di adottare uno schema inadatto al proprio contesto, che è uno degli errori più costosi in fase di migrazione.

## Le scadenze: cosa dicono NIST ed ENISA

Avere gli standard non basta: le organizzazioni hanno bisogno di un orizzonte temporale. Il NIST lo ha fissato con chiarezza nella bozza di transizione (IR 8547): gli algoritmi a 112 bit di sicurezza, come RSA-2048 ed ECC P-256, sono destinati alla deprecazione entro il 2030 e al divieto entro il 2035. Il divieto del 2035, però, non riguarda solo i 112 bit: lo stesso documento prevede la messa al bando, dopo quel termine, anche degli algoritmi asimmetrici di forza superiore, come RSA-3072 ed ECC P-384. In altre parole, dal 2030 i parametri più deboli non andrebbero più usati per nuove im...