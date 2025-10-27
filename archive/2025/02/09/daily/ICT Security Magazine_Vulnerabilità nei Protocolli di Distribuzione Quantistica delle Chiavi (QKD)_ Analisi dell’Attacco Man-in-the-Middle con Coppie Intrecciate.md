---
title: Vulnerabilità nei Protocolli di Distribuzione Quantistica delle Chiavi (QKD): Analisi dell’Attacco Man-in-the-Middle con Coppie Intrecciate
url: https://www.ictsecuritymagazine.com/articoli/qkd-distribuzione-quantistica-delle-chiavi/
source: ICT Security Magazine
date: 2025-02-09
fetch_date: 2025-10-06T20:37:50.474541
---

# Vulnerabilità nei Protocolli di Distribuzione Quantistica delle Chiavi (QKD): Analisi dell’Attacco Man-in-the-Middle con Coppie Intrecciate

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

![Protocolli di Distribuzione Quantistica delle Chiavi (QKD)](https://www.ictsecuritymagazine.com/wp-content/uploads/Protocolli-di-Distribuzione-Quantistica-delle-Chiavi-QKD.jpg)

# Vulnerabilità nei Protocolli di Distribuzione Quantistica delle Chiavi (QKD): Analisi dell’Attacco Man-in-the-Middle con Coppie Intrecciate

A cura di:[Redazione](#molongui-disabled-link)  Ore 8 Febbraio 20257 Febbraio 2025

La crittografia quantistica rappresenta una frontiera promettente per la sicurezza delle comunicazioni, ma recenti analisi hanno evidenziato vulnerabilità significative in alcuni protocolli di distribuzione quantistica delle chiavi (QKD). Questa scoperta solleva interrogativi importanti sulla [sicurezza dei sistemi crittografici quantistici](https://www.ictsecuritymagazine.com/cybersecurity-video/tecnologie-quantistiche-per-la-cybersecurity-giuseppe-vallone/), dimostrando come anche le tecnologie più avanzate possano presentare debolezze inaspettate.

## L’Evoluzione della Sicurezza nei Protocolli Quantistici e le Sfide Emergenti

La storia della crittografia è costellata di protocolli ritenuti inizialmente sicuri ma successivamente compromessi da attacchi innovativi. Nel campo della crittografia quantistica, nonostante la sua relativa novità, si stanno già manifestando vulnerabilità simili. Un esempio significativo riguarda il protocollo QKD basato sugli stati Greenberger-Horne-Zeilinger (GHZ), che pur non richiedendo comunicazione classica, si è dimostrato vulnerabile a un attacco man-in-the-middle quantistico. Questo scenario evidenzia come l’assenza di comunicazione classica, inizialmente considerata un vantaggio per la sicurezza, possa paradossalmente creare nuove opportunità per potenziali attaccanti.

Guarda il video intervento su “*Come si dimostra la sicurezza dei Protocolli di Distribuzione Quantistica delle Chiavi (QKD)*“:

#### Analisi Tecnica dell’Attacco EPR Man-in-the-Middle nei Protocolli di Distribuzione Quantistica delle Chiavi (QKD)

L’attacco sfrutta coppie EPR (Einstein-Podolsky-Rosen) create dall’attaccante per intercettare e manipolare la comunicazione. Nel protocollo GHZ, l’attaccante (Eve) cattura il qubit inviato da Alice a Bob, creando poi una propria coppia di qubit in stato EPR. Questo permette a Eve di decodificare i messaggi scambiati senza essere rilevata, a condizione che possa determinare la base utilizzata per la comunicazione. La sofisticatezza dell’attacco risiede nella capacità di Eve di mantenere la coerenza quantistica durante l’intero processo di intercettazione e sostituzione, sfruttando le proprietà dell’entanglement quantistico per mascherare la sua presenza.

#### Implementazione e Limitazioni della Sicurezza nei Protocolli Ping-Pong

Il protocollo ping-pong di Boström e Felbinger, così come la sua variante proposta da Cai, presentano vulnerabilità simili. In questi casi, l’attacco richiede che Eve possa intercettare sia il canale quantistico che quello classico. La peculiarità dell’attacco sta nella capacità di Eve di sostituire i qubit originali con quelli da lei generati, mantenendo la coerenza della comunicazione senza essere individuata. L’efficacia dell’attacco è particolarmente rilevante in scenari di rete ad alto traffico, dove le imperfezioni nella trasmissione possono mascherare le attività dell’attaccante.

#### Implicazioni per lo Sviluppo di Futuri Protocolli di Sicurezza Quantistica

La scoperta di queste vulnerabilità non invalida le prove di sicurezza esistenti per questi protocolli, ma evidenzia come possano esistere metodi di attacco non previsti dai progettisti. Questo sottolinea l’importanza di un approccio olistico alla sicurezza dei protocolli quantistici, che consideri non solo gli attacchi teorici ma anche le vulnerabilità pratiche derivanti dall’implementazione. La sfida principale consiste nel bilanciare l’efficienza computazionale con la robustezza contro attacchi sofisticati, mantenendo al contempo la praticabilità dell’implementazione in sistemi reali.

### Considerazioni sulla Resilienza dei Protocolli Quantistici agli Attacchi Moderni

La vulnerabilità fondamentale risiede nell’impossibilità per Alice e Bob di rilevare che i qubit ricevuti fanno parte di una coppia intrecciata creata da Eve. Indipendentemente dall’operatore sigma utilizzato (X o Z), Eve può replicare le azioni di Bob senza essere individuata. Questo suggerisce che qualsiasi protocollo basato sulla manipolazione e il ritorno di qubit intrecciati potrebbe essere vulnerabile a questo tipo di attacco. La situazione è ulteriormente complicata dalla necessità di implementare questi protocolli in reti reali, dove le imperfezioni nella trasmissione e gli errori naturali possono mascherare le attività di un attaccante.

#### Prospettive Future e Soluzioni Proposte

La ricerca “[Vulnerabilities in Quantum Key Distribution Protocols](https://nvlpubs.nist.gov/nistpubs/ir/2003/ir6977.pdf)” realizzata da D. Richard Kuhn evidenzia come la sicurezza nella crittografia quantistica richieda non solo robuste basi teoriche ma anche una attenta considerazione delle vulnerabilità pratiche. La continua evoluzione delle tecniche di attacco sottolinea l’importanza di sviluppare protocolli che incorporino meccanismi di autenticazione e verifica più sofisticati, combinando el...