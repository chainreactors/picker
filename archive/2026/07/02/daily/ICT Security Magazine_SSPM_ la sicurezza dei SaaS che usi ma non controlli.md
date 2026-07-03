---
title: SSPM: la sicurezza dei SaaS che usi ma non controlli
url: https://www.ictsecuritymagazine.com/cyber-security/sspm-saas-security-posture-management/
source: ICT Security Magazine
date: 2026-07-02
fetch_date: 2026-07-03T05:48:48.947946
---

# SSPM: la sicurezza dei SaaS che usi ma non controlli

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

![SSPM la sicurezza dei SaaS](https://www.ictsecuritymagazine.com/wp-content/uploads/SSPM-la-sicurezza-dei-SaaS.png)

# SSPM: la sicurezza dei SaaS che usi ma non controlli

A cura di:[Redazione](#molongui-disabled-link)  Ore 2 Luglio 20269 Giugno 2026

SSPM è l’acronimo di SaaS Security Posture Management, e nasce da uno spostamento che ha cambiato in silenzio dove vive il rischio. L’attività di un’organizzazione oggi non gira più su server che configura e custodisce, ma su decine, spesso centinaia, di applicazioni in modalità software come servizio: la posta, i documenti, il CRM, le risorse umane, lo sviluppo, la collaborazione. Di queste applicazioni l’organizzazione non possiede l’infrastruttura e non ne scrive il codice. Ne controlla soltanto una cosa, la configurazione, ed è esattamente lì che si è trasferito il problema di sicurezza.

La logica è la stessa che governa il [cloud](https://www.ictsecuritymagazine.com/articoli/cloud-security/), ma portata un passo più in là. Il fornitore del SaaS si occupa di proteggere la piattaforma e di tenerla aggiornata; al cliente resta la responsabilità di come quella piattaforma è impostata: chi può accedere, cosa è condiviso con l’esterno, quali account hanno privilegi da amministratore, a quali applicazioni di terze parti si è dato il permesso di collegarsi. L’SSPM è la disciplina che verifica, in modo continuo, che la postura di tutto questo parco di applicazioni sia sicura, perché nessun fornitore lo farà al posto del cliente.

## La responsabilità che si è spostata

Conviene fissare bene questa divisione, perché è la fonte di gran parte degli incidenti. Nel modello del software come servizio il fornitore garantisce la sicurezza della piattaforma, ma la configurazione del singolo ambiente, il cosiddetto *tenant*, è interamente nelle mani del cliente. È il punto in cui si annidano le esposizioni: una regola di condivisione troppo permissiva che rende un documento accessibile a chiunque, un controllo amministrativo lasciato aperto, l’autenticazione a più fattori non imposta a tutti. Sono errori di impostazione, non difetti del prodotto, ed è il cliente a doverli trovare.

Il guaio è che la superficie di configurazione è enorme e diversa per ogni applicazione. Ciascuna piattaforma, dalla suite di produttività al CRM, ha centinaia di impostazioni di sicurezza con una propria logica, e quasi nessuna organizzazione le verifica in modo sistematico e ricorrente. La configurazione si fa una volta, all’avvio, e poi si muove da sola: nuovi utenti, nuovi permessi, nuove integrazioni, nuove derive rispetto allo stato sicuro di partenza. Senza un controllo continuo, lo scostamento cresce invisibile, fino al giorno in cui qualcuno si accorge che un dato che doveva restare interno era raggiungibile da fuori.

## Il ventre molle: le integrazioni SaaS-to-SaaS

C’è un fronte, in particolare, che sfugge a quasi tutti, ed è quello delle connessioni tra applicazioni. Ogni volta che si collega un’app di terze parti a una piattaforma SaaS, attraverso un consenso OAuth, si concede a quell’app un accesso ai propri dati che è ampio, persistente e raramente rivisto. È, a tutti gli effetti, una [identità non umana](https://www.ictsecuritymagazine.com/notizie/non-human-identity-nis2-e-d-lgs-138-2024/) con permessi spesso eccessivi rispetto a ciò che le serve, concessa con un clic e poi dimenticata. Moltiplicato per le centinaia di integrazioni che un’organizzazione accumula nel tempo, questo intreccio di connessioni da applicazione ad applicazione diventa una rete che nessuno ha mai inventariato.

È un ventre molle pericoloso perché aggira il perimetro. Un attaccante che comprometta un’app di terze parti con un consenso valido raggiunge i dati custoditi nella piattaforma principale senza dover violare nulla del cliente: usa una porta che il cliente stesso ha aperto. Lo ha mostrato in modo netto la [compromissione dell’integrazione Drift](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift) di Salesloft, nell’agosto 2025: token OAuth sottratti a quell’app di terze parti hanno dato accesso ai dati Salesforce di oltre settecento organizzazioni, aggirando l’autenticazione, e da lì gli attaccanti hanno cercato credenziali per spostarsi verso altri servizi. È la dimostrazione di come una via legittima, una volta compromessa, diventi un’autostrada. L’SSPM affronta proprio questo, tracciando le applicazioni connesse, valutando gli ambiti e i permessi che hanno ottenuto, e segnalando le integrazioni rischiose o sovradimensionate prima che diventino il percorso di un attacco.

## SSPM non è CSPM e non è CASB

Per collocare bene questa disciplina serve distinguerla da altre con cui viene spesso confusa. La gestione della postura degli ambienti cloud, il CSPM, protegge l’infrastruttura su cui si costruisce, le macchine, le reti, gli archivi dei fornitori di servizi infrastrutturali. L’SSPM protegge invece la configurazione delle applicazioni che si consumano già pronte. I due mondi si somigliano nel concetto, postura, scostamento, librerie di regole, ma poggiano su interfacce completamente diverse, al punto che le regole dell’uno non...