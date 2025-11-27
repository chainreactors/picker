---
title: Cybersecurity ferroviaria: vulnerabilità critiche di ERTMS/ETCS e sicurezza del segnalamento digitale
url: https://www.ictsecuritymagazine.com/articoli/ertms/
source: ICT Security Magazine
date: 2025-11-26
fetch_date: 2025-11-27T03:13:07.028341
---

# Cybersecurity ferroviaria: vulnerabilità critiche di ERTMS/ETCS e sicurezza del segnalamento digitale

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

![Cybersecurity ferroviaria e ERTMS: protezione digitale delle linee ad alta velocità e gestione sicura dei sistemi ferroviari europei](https://www.ictsecuritymagazine.com/wp-content/uploads/cybersecurity-ferroviaria-ERTMS-.jpeg)

# Cybersecurity ferroviaria: vulnerabilità critiche di ERTMS/ETCS e sicurezza del segnalamento digitale

A cura di:[Redazione](#molongui-disabled-link)  Ore 26 Novembre 202511 Novembre 2025

Il settore ferroviario europeo sta attraversando una trasformazione tecnologica senza precedenti. La progressiva implementazione dell’[*European Rail Traffic Management System*](https://www.era.europa.eu/domains/infrastructure/european-rail-traffic-management-system-ertms_en) (ERTMS) rappresenta uno degli investimenti infrastrutturali più ambiziosi del continente: in Italia, al 30 giugno 2025, sono operativi **1.063 chilometri** di linee ad alta velocità equipaggiate con ERTMS Level 2, secondo i dati ufficiali di [Rete Ferroviaria Italiana](https://www.rfi.it/it/Sicurezza-e-tecnologie/tecnologie/ccs/ertms.html). Nei prossimi decenni, l’intero network ferroviario europeo transiterà verso questo sistema unificato di gestione del traffico.

Tuttavia, questa digitalizzazione massiva porta con sé una superficie d’attacco cibernetico di proporzioni inedite, ponendo interrogativi critici sulla sicurezza di un’[infrastruttura classificata come essenziale](https://www.ictsecuritymagazine.com/articoli/industrial-cybersecurity-cps/) dalla Direttiva NIS2 e da cui dipendono milioni di passeggeri quotidiani oltre all’intera catena logistica continentale.

## L’architettura di ERTMS: stratificazione protocollare e vulnerabilità intrinseche

L’ERTMS si articola su tre livelli protocollari distinti, ciascuno con specifiche criticità che, se sfruttate in modo coordinato, possono compromettere l’integrità dell’intero sistema. Al livello più basso opera **GSM-R** (*Global System for Mobile Communications-Railway*), responsabile della trasmissione radio; sopra di esso si colloca il protocollo **EuroRadio**, che fornisce autenticazione e integrità tramite Message Authentication Code (MAC); infine, il livello applicativo gestisce i messaggi di controllo del treno, incluse le *movement authorities* (autorizzazioni al movimento).

#### GSM-R e la crittografia A5/1: una vulnerabilità legacy

La scelta di utilizzare l’algoritmo di cifratura **A5/1** per GSM-R costituisce una delle debolezze più critiche documentate nella letteratura scientifica. Sebbene originariamente classificato, questo *stream cipher* è stato ricostruito attraverso *reverse engineering* già negli anni Duemila. Ricerche pubblicate su *Security and Communication Networks* (2018) hanno dimostrato che A5/1 presenta «gravi vulnerabilità» identificate attraverso analisi formale e che può essere compromesso utilizzando *rainbow tables* e FPGA ad alte prestazioni con tempi di attacco misurabili in minuti.

Inoltre, GSM-R implementa solo un’**autenticazione unidirezionale**: la rete autentica il terminale mobile (*Mobile Station*), ma non viceversa, esponendo il sistema ad attacchi di tipo *man-in-the-middle* (MITM) attraverso la creazione di stazioni base (*Base Transceiver Station*) contraffatte. Come documentato in uno studio del 2022 pubblicato su *PMC*, «GSM-R non fornisce protezione dei dati end-to-end, poiché cripta i dati solo dalla Mobile Station alla Base Station e utilizza autenticazione unidirezionale», rendendo possibile l’intercettazione e la manipolazione delle comunicazioni.

#### EuroRadio: vulnerabilità crittografiche del MAC basato su 3DES

Il protocollo EuroRadio, progettato per compensare le carenze di GSM-R fornendo un ulteriore strato di sicurezza, presenta a sua volta criticità significative. L’utilizzo del **Triple DES (3DES)** per la generazione dei Message Authentication Code ha dimostrato vulnerabilità documentate in ricerche presentate all’*Asia Conference on Computer and Communications Security* (2017).

Thomas, Chothia e de Ruiter hanno dimostrato la possibilità di condurre **attacchi di collisione contro il MAC di EuroRadio**, permettendo a un attaccante che osservi una collisione di forgiare messaggi di controllo del treno. Secondo i loro calcoli, «un attaccante in grado di monitorare tutti i centri di controllo backend in un paese delle dimensioni del Regno Unito per 45 giorni avrebbe l’1% di probabilità di acquisire il controllo di un treno».

Un’analisi formale condotta con strumenti come ProVerif ha rivelato ulteriori criticità: il processo di stabilimento della sessione **non utilizza timestamp**, consentendo la replica di messaggi ad alta priorità o la loro cancellazione non rilevabile.

#### Balise e Comunicazioni Wireless: il tallone d’Achille del sistema

Oltre ai protocolli di rete, ERTMS presenta criticità nelle comunicazioni locali. I **balise** – dispositivi elettromagnetici installati lungo i binari secondo lo standard Eurobalise – trasmettono informazioni sulla posizione al sistema di bordo, ma sono stati progettati senza considerazioni di cybersecurity.

Come evidenziato in uno studio pubblicato nel 2024 su *Journal of Systems Safety and Security*, «la negazione della comunicazione tra balise e sistema di bordo è generalmente realizzabile con risorse limitate, con impatti potenzialmente devastanti che possono causare effetti a cascata minacciando la disponibilità di ampie porzioni dell’infrastruttura». In alcune implementazioni, risulta persino possibile inviare ...