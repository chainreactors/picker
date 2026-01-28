---
title: IoMT e il paradosso della certificazione: quando la compliance normativa ostacola la cybersecurity dei dispositivi medicali
url: https://www.ictsecuritymagazine.com/articoli/iomt/
source: ICT Security Magazine
date: 2026-01-27
fetch_date: 2026-01-28T03:35:21.460023
---

# IoMT e il paradosso della certificazione: quando la compliance normativa ostacola la cybersecurity dei dispositivi medicali

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
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

![La certificazione CE limita gli aggiornamenti dei dispositivi IoMT, esponendo gli ospedali a vulnerabilità note. Scopri la securizzazione laterale.](https://www.ictsecuritymagazine.com/wp-content/uploads/iomt.jpeg)

# IoMT e il paradosso della certificazione: quando la compliance normativa ostacola la cybersecurity dei dispositivi medicali

A cura di:[Redazione](#molongui-disabled-link)  Ore 27 Gennaio 202620 Gennaio 2026

La sicurezza dei dispositivi medicali IoMT (*Internet of Medical Things*) rappresenta oggi uno dei paradossi più critici e meno discussi nel panorama della *cybersecurity* sanitaria europea. Il [Regolamento MDR 2017/745](https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng) impone che i dispositivi certificati CE non possano essere modificati – inclusa l’installazione di *software* antivirus o l’applicazione di *patch* di sicurezza – senza invalidare la certificazione stessa.

Questa rigidità normativa, concepita per tutelare la sicurezza del paziente, si scontra frontalmente con le esigenze di protezione *cyber* imposte dalla [Direttiva NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng) e dalle minacce *ransomware* che nel 2024 hanno colpito il 67% delle organizzazioni sanitarie a livello globale, secondo il [*report* Sophos](https://news.sophos.com/en-us/2024/07/30/the-state-of-ransomware-in-healthcare-2024/) condotto su 14 Paesi. L’articolo analizza questo conflitto regolatorio e propone il modello della “securizzazione laterale” – basato su microsegmentazione di rete e architetture *Zero Trust* – come soluzione architetturale che consente di proteggere i dispositivi senza alterarne la configurazione certificata.

## Il nodo irrisolto della sicurezza IoMT negli ospedali europei

La sicurezza IoMT è diventata la questione centrale per ogni CISO del settore sanitario. Il motivo è tanto semplice quanto allarmante: secondo analisi di settore basate su dati [Forescout](https://www.forescout.com/resources/riskiest-devices-2025-report/), la stragrande maggioranza degli ospedali gestisce dispositivi medicali con vulnerabilità note e attivamente sfruttate dagli attaccanti. Non si tratta di un dato astratto, ma di una realtà operativa quotidiana che i responsabili della [sicurezza informatica ospedaliera](https://www.ictsecuritymagazine.com/articoli/sanita-attacchi-cyber/) conoscono bene.

Il problema, tuttavia, non risiede nella mancanza di consapevolezza o di competenze tecniche. Il vero ostacolo è strutturale e normativo: i dispositivi medicali certificati CE ai sensi del [Regolamento MDR 2017/745](https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng) non possono essere modificati senza compromettere la loro conformità regolatoria. Questo significa che un monitor cardiaco, una pompa per infusione o un sistema di *imaging* diagnostico – tutti dispositivi critici per la cura del paziente – devono rimanere esattamente nella configurazione in cui sono stati certificati, anche quando presentano vulnerabilità *software* documentate.

Il paradosso emerge in tutta la sua evidenza: la normativa pensata per proteggere il paziente impedisce di fatto l’implementazione delle misure di *cybersecurity* necessarie a proteggerlo da minacce che, secondo il [*report* IBM *Cost of a Data Breach 2024*](https://www.ibm.com/reports/data-breach), hanno causato danni per una media di 9,77 milioni di dollari per ogni violazione nel settore sanitario – il costo più alto tra tutti i comparti industriali per il quattordicesimo anno consecutivo.

## Il conflitto normativo: MDR 2017/745 *versus* requisiti di *cybersecurity*

Per comprendere la profondità di questo conflitto è necessario esaminare le due cornici normative che, paradossalmente, dovrebbero entrambe tutelare la sicurezza dei pazienti.

### Il Regolamento MDR 2017/745: la logica della certificazione

Il [*Medical Device Regulation*](https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng) europeo, entrato in vigore nel maggio 2021, ha sostituito le precedenti direttive introducendo requisiti più stringenti per l’immissione sul mercato dei dispositivi medicali. L’Allegato I, Sezione 17.2, stabilisce che il *software* contenuto nei dispositivi medicali deve essere sviluppato e prodotto “allo stato dell’arte”, considerando il ciclo di vita, la gestione del rischio e la sicurezza delle informazioni.

Tuttavia, la certificazione CE – rilasciata dagli Organismi Notificati dopo rigorosi processi di valutazione della conformità – cristallizza la configurazione del dispositivo. Qualsiasi modifica sostanziale richiede una nuova valutazione di conformità, con tempi e costi che possono risultare proibitivi. Il principio sottostante è chiaro: garantire che il dispositivo funzioni esattamente come testato e validato, senza alterazioni che potrebbero comprometterne la sicurezza clinica.

Questa rigidità ha senso dal punto di vista della sicurezza del paziente in senso tradizionale. Un’alterazione del *firmware* di una pompa per infusione potrebbe teoricamente modificarne il dosaggio; un aggiornamento *software* di un ventilatore polmonare potrebbe introdurre malfunzionamenti. La certificazione CE è progettata per prevenire questi rischi.

### La Direttiva NIS2: l’imperativo della *cybersecurity*

Sul versante opposto, la [Direttiva NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng) – in vigore dal 18 ottobre 2024 – classifica ospedali e produttori di dispositivi medicali come “entità essenziali” o “importanti”, imponendo obbligh...