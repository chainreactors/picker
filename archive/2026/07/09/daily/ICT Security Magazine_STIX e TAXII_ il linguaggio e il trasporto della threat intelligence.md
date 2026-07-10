---
title: STIX e TAXII: il linguaggio e il trasporto della threat intelligence
url: https://www.ictsecuritymagazine.com/cyber-security/stix-e-taxii/
source: ICT Security Magazine
date: 2026-07-09
fetch_date: 2026-07-10T06:00:02.205934
---

# STIX e TAXII: il linguaggio e il trasporto della threat intelligence

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

![STIX e TAXII il linguaggio e il trasporto della threat intelligence](https://www.ictsecuritymagazine.com/wp-content/uploads/STIX-e-TAXII-il-linguaggio-e-il-trasporto-della-threat-intelligence.png)

# STIX e TAXII: il linguaggio e il trasporto della threat intelligence

A cura di:[Redazione](#molongui-disabled-link)  Ore 9 Luglio 202610 Giugno 2026

STIX e TAXII sono i due standard che permettono alla threat intelligence di circolare tra organizzazioni, strumenti e team senza perdersi nella traduzione. Il primo è un linguaggio per descrivere le minacce in modo strutturato e leggibile dalle macchine; il secondo è un protocollo per farle viaggiare da un sistema all’altro. Presi separatamente servono a poco, insieme risolvono un problema concreto: senza un formato comune, le informazioni su un attacco restano prigioniere del documento in cui sono nate, illeggibili per gli strumenti di chi le riceve.

Non sono nati ieri. STIX (Structured Threat Information eXpression) e TAXII (Trusted Automated Exchange of Intelligence Information) furono sviluppati a partire dal 2012 dalla MITRE per conto del Dipartimento della Sicurezza Interna statunitense, e nel 2015, in un’iniziativa [guidata dal DHS](https://www.dhs.gov/archive/news/2015/07/23/dhs-leads-effort-transition-automated-cybersecurity-information-sharing), la loro proprietà intellettuale fu trasferita a OASIS, il consorzio che ne cura da allora l’evoluzione aperta. Le versioni attuali, STIX 2.1 e TAXII 2.1, sono [standard OASIS](https://www.oasis-open.org/2021/06/23/stix-v2-1-and-taxii-v2-1-oasis-standards-are-published/) dal giugno 2021.

## STIX: un linguaggio per descrivere le minacce

STIX è, in sostanza, un vocabolario condiviso. Invece di raccontare un attacco a parole, lo si rappresenta come un insieme di oggetti tipizzati e collegati tra loro. La [specifica STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html) definisce diciotto oggetti di dominio, gli STIX Domain Object, tra cui indicatori, campagne, malware, vulnerabilità, attori delle minacce e schemi d’attacco; a questi si aggiungono gli oggetti osservabili, come indirizzi IP, file e domini, e gli oggetti relazione, che legano il tutto in un grafo. Il risultato è che la descrizione di una campagna, comprese le tattiche, tecniche e procedure di certi [gruppi APT](https://www.ictsecuritymagazine.com/articoli/file-msc-apt-cybercrime/), diventa un dato preciso e non ambiguo, che una macchina può leggere, correlare e azionare senza bisogno di interpretazione umana. STIX è inoltre indipendente dal trasporto: i suoi oggetti possono essere impacchettati e spostati anche al di fuori di TAXII.

Un esempio chiarisce la differenza rispetto a un elenco piatto di indicatori. In STIX un singolo dominio malevolo non è una riga isolata, ma un oggetto osservabile collegato a un indicatore, che a sua volta è messo in relazione con un malware, attribuito a un attore delle minacce e inserito in una campagna. Chi riceve quel grafo non ottiene soltanto un dato da bloccare, ma il contesto che lo rende comprensibile: a quale avversario appartiene, in quale operazione, con quale obiettivo. È la stessa differenza che separa un dato dall’intelligence vera e propria, e STIX la codifica in modo che a coglierla sia anche una macchina, non solo un analista.

## TAXII: il protocollo che fa viaggiare l’intelligence

Se STIX è la lingua, TAXII è il servizio postale. È un protocollo di livello applicativo, costruito su HTTPS, pensato per scambiare contenuti STIX in modo automatico e scalabile, pur non essendo vincolato a STIX. TAXII organizza lo scambio principalmente attorno alle Collection, repository da cui un client preleva informazioni o a cui le invia in logica di richiesta e risposta, e prevede, riservandolo a un’evoluzione futura della specifica, un modello a canali per la distribuzione in pubblicazione e sottoscrizione. Definisce ruoli chiari di produttore e consumatore, così che chi pubblica intelligence e chi la consuma possano dialogare in modo prevedibile, senza dover costruire un’integrazione su misura per ogni coppia di interlocutori.

Vale la pena distinguere i due paradigmi, tenendo presente che nella versione 2.1 solo uno è davvero operativo. Le Collection, basate sull’interrogazione, sono il meccanismo effettivamente disponibile e si prestano a chi vuole controllare quando e cosa prelevare, ad esempio una piattaforma che aggiorna periodicamente i propri indicatori attingendo a un repository fidato. Il modello in pubblicazione e sottoscrizione, che privilegerebbe la tempestività recapitando le novità via via che si rendono disponibili, resta invece una previsione della specifica, non ancora implementabile come servizio. In entrambi i casi il principio di fondo è lo stesso: ridurre al minimo l’intervento manuale, perché un’informazione su una minaccia perde valore con ogni ora che passa prima di raggiungere chi può agire.

## Perché servono entrambi, e perché insieme

La forza della coppia sta nella divisione dei compiti. Un linguaggio comune senza un canale per trasmetterlo resta un esercizio di catalogazione; un canale senza una lingua condivisa trasporta dati che il destinatario non s...