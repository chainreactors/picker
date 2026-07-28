---
title: Cryptographic Bill of Materials (CBOM): sapere che crittografia si usa prima di migrare
url: https://www.ictsecuritymagazine.com/articoli/cryptographic-bill-of-materials-cbom/
source: ICT Security Magazine
date: 2026-07-27
fetch_date: 2026-07-28T05:00:05.916982
---

# Cryptographic Bill of Materials (CBOM): sapere che crittografia si usa prima di migrare

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

![CBOM Cryptographic Bill of Materials](https://www.ictsecuritymagazine.com/wp-content/uploads/CBOM-Cryptographic-Bill-of-Materials.png)

# Cryptographic Bill of Materials (CBOM): sapere che crittografia si usa prima di migrare

A cura di:[Redazione](#molongui-disabled-link)  Ore 27 Luglio 202617 Luglio 2026

Il Cryptographic Bill of Materials (CBOM) risponde a una domanda che quasi ogni organizzazione, di fronte alla migrazione post-quantum, scopre di non saper trasformare in un elenco: dove, e con quali algoritmi, chiavi e certificati, l’azienda usa la crittografia. Sembra una domanda banale, e invece è insidiosa, perché la crittografia non vive in un posto solo. È incorporata nelle applicazioni, nelle librerie di terze parti, nei protocolli negoziati a runtime, nei certificati che scadono in silenzio, nell’hardware. Nessuno l’ha mai censita davvero, perché finora non è servito. Ora serve, e serve in fretta.

La ragione è la transizione verso una crittografia resistente ai computer quantistici, spinta da scadenze ormai fissate e dalla minaccia del “raccogli ora, decifra dopo”, che rende urgente proteggere già oggi i segreti destinati a durare a lungo. Ma prima di sostituire un algoritmo bisogna sapere di averlo. Il CBOM è lo strumento standardizzato che trasforma questa consapevolezza da esercizio manuale a inventario ripetibile, ed è la prima mossa concreta di una migrazione che, senza di esso, procederebbe alla cieca.

## Che cos’è un Cryptographic Bill of Materials

Un Cryptographic Bill of Materials è l’inventario strutturato e leggibile dalle macchine degli asset crittografici di un sistema: gli algoritmi, le chiavi, i certificati e i protocolli, insieme alle relazioni che li legano ai componenti software che li usano. È l’estensione, al mondo della crittografia, di un’idea già familiare: quella del [Software Bill of Materials](https://www.ictsecuritymagazine.com/articoli/software-bill-of-materials/). Come l’SBOM elenca le componenti di cui un software è fatto, il CBOM elenca la crittografia che quel software impiega, e dove la impiega. La differenza è che qui le dipendenze non sono librerie ma primitive crittografiche, ed è proprio la loro invisibilità a rendere l’inventario necessario.

Lo standard di riferimento è nato in ambito aperto. Il formato CBOM è stato introdotto in CycloneDX, il progetto di OWASP per le distinte dei materiali, con la versione 1.6 dell’aprile 2024, su un contributo iniziale di IBM Research, ed è stato poi standardizzato come ECMA-424. Non si è fermato lì: la [versione 1.7](https://cyclonedx.org/news/cyclonedx-v1.7-released/), rilasciata nell’ottobre 2025 e ratificata come ECMA-424 di seconda edizione a dicembre 2025, ne ha ampliato le capacità, aggiungendo un elenco standardizzato delle famiglie di algoritmi e una lista completa delle curve ellittiche, utili anche fuori da CycloneDX per le verifiche di conformità e di [prontezza al post-quantum](https://www.ictsecuritymagazine.com/articoli/quantum-readiness/). Non è quindi un formato proprietario legato a un fornitore, ma una grammatica comune con cui descrivere la postura crittografica di un’organizzazione, generarla con strumenti di scoperta automatica e scambiarla come si scambia già un SBOM.

## Perché l’inventario viene prima della migrazione

Gli standard post-quantum, almeno i principali, ci sono: nell’agosto 2024 il NIST ha finalizzato i primi tre algoritmi resistenti al calcolo quantistico (FIPS 203, 204 e 205). E “primi” è la parola esatta, perché il quadro non è ancora completo: un ulteriore algoritmo, HQC, è stato selezionato nel marzo 2025, e la firma FN-DSA (FIPS 206) è tuttora in lavorazione. Le agenzie, intanto, hanno iniziato a fissare le date entro cui abbandonare gli algoritmi vulnerabili. Il problema, insomma, non è più quale crittografia adottare, ma dove va applicata, ed è qui che casca l’asino: la maggior parte delle organizzazioni non possiede una mappa di dove e come usa la crittografia. È un sapere sparso tra team diversi, sepolto in codice scritto anni prima, delegato a componenti che nessuno controlla riga per riga.

Non a caso le stesse autorità mettono l’inventario al primo posto. Il documento congiunto di [CISA, NSA e NIST](https://www.cisa.gov/resources-tools/resources/quantum-readiness-migration-post-quantum-cryptography), dell’agosto 2023, indica come passo iniziale proprio la costruzione di un inventario crittografico: sapere quali algoritmi sono in uso, in quali sistemi, a protezione di quali dati. È l’applicazione di un principio tanto semplice quanto trascurato, cioè che non si può migrare ciò che non si vede. Senza quella mappa, ogni piano di transizione resta una stima, e ogni scadenza un salto nel buio.

Da allora le autorità hanno alzato la posta, e il CBOM è passato dalle raccomandazioni a un atto di governo. Con l’[ordine esecutivo di giugno 2026](https://www.ictsecuritymagazine.com/notizie/ordine-esecutivo-usa-crittografia-post-quantum-2030/) sulla sicurezza crittografica (Executive Order 14412), la Casa Bianca ha incaricato il Dipartimento della Sicurezza interna, tramite la CISA e in coordinamento con il NIST, di pubblicare entro 270 giorni, quindi verso il 19 marzo...