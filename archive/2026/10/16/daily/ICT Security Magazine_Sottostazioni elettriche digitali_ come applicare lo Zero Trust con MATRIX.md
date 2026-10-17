---
title: Sottostazioni elettriche digitali: come applicare lo Zero Trust con MATRIX
url: https://www.ictsecuritymagazine.com/articoli/zero-trust-sottostazioni-elettriche-novagrid/
source: ICT Security Magazine
date: 2026-10-16
fetch_date: 2026-10-17T06:37:49.698112
---

# Sottostazioni elettriche digitali: come applicare lo Zero Trust con MATRIX

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

![sottostazioni elettriche_Sottostazione protetta nella smart grid](https://www.ictsecuritymagazine.com/wp-content/uploads/sottostazioni-elettriche_Sottostazione-protetta-nella-smart-grid.png)

# Sottostazioni elettriche digitali: come applicare lo Zero Trust con MATRIX

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 16 Ottobre 20262 Ottobre 2026

*Dalla teoria all’impianto: lo scenario NovaGrid mostra come applicare MATRIX a sottostazioni elettriche digitali in cui SCADA moderni convivono con IED e sistemi legacy.*

Le [parti precedenti della serie](https://www.ictsecuritymagazine.com/articoli/matrice-di-alloc%E2%80%A6ne-zero-trust-ot/) hanno descritto le sei fasi di MATRIX e la matrice di allocazione. Resta da vedere come il metodo funziona su un impianto.

Questa quinta parte apre la sezione di validazione con uno scenario illustrativo: NovaGrid, un operatore di distribuzione ipotetico ma verosimile. Qui un sistema SCADA moderno convive con apparati legacy che governano un centinaio di sottostazioni secondarie. Seguirlo fase per fase è il modo più diretto per capire il framework.

## Validazione di MATRIX nelle sottostazioni elettriche digitali

*Lo scenario NovaGrid mostra come applicare MATRIX a un’infrastruttura elettrica con SCADA moderni, IED e apparati legacy.*

La validazione del framework adotta un approccio multi metodo articolato su tre componenti complementari: una validazione di copertura rispetto agli standard di riferimento, una validazione comparativa rispetto agli schemi esistenti e una validazione retrospettiva condotta su un incidente reale e documentato. Lo scenario illustrativo delle sottostazioni digitali, descritto nel seguito, fornisce il sostrato a cui le tre componenti fanno riferimento.

### Sottostazioni elettriche digitali: lo scenario NovaGrid

Per mostrare il framework all’opera consideriamo uno scenario applicativo relativo a un ipotetico operatore di distribuzione, qui denominato NovaGrid, che gestisce un parco di sottostazioni elettriche digitali. Una sottostazione svolge la funzione di abbassare i livelli di alta tensione provenienti dalla rete di trasmissione per alimentare i circuiti di distribuzione locale, regolando la fornitura in risposta alla domanda di abitazioni e piccole utenze. I sistemi di automazione di NovaGrid comunicano con IED, relè e altri apparati; un’interfaccia uomo-macchina di tipo web supporta gli operatori nel monitoraggio e nel comando locale e remoto, mentre un sistema SCADA fornisce la vista d’insieme sulla stabilità della rete e sulle manovre.

L’infrastruttura è il risultato di una stratificazione storica: accanto a un sistema SCADA moderno convivono apparati legacy che governano un centinaio di sottostazioni secondarie tramite protocolli proprietari non integrabili con il sistema di monitoraggio centrale, e la cui sostituzione integrale non è, allo stato, una priorità sostenibile per ragioni di costo e di affidabilità. Lo scenario è volutamente analogo, nelle sue caratteristiche tecniche, ai casi discussi nella letteratura recente sul tema,[[1]](#_ftn1) ma i dettagli e le scelte qui presentati sono originali e funzionali alla sola illustrazione del metodo.

Applicando la fase M, NovaGrid ricostruisce i propri mission thread attorno alla trasformazione, regolazione e distribuzione dell’energia, identificando come DAAS critici i segnali di comando verso i dispositivi di protezione, i dati di telemetria del sistema SCADA e i servizi di automazione delle manovre. La caratterizzazione evidenzia che la conseguenza più grave non è la perdita di riservatezza dei dati, ma la perdita di integrità o disponibilità del comando: un’alterazione dei segnali inviati ai relè potrebbe compromettere la protezione del sistema e la continuità della fornitura.

Nella fase A, NovaGrid profila le proprie classi di asset. Le HMI su piattaforma Windows e i server SCADA mostrano un’idoneità elevata e uniforme, compatibile con controlli on-device. Gli IED moderni nelle sottostazioni primarie presentano un’idoneità intermedia. Gli apparati legacy delle sottostazioni secondarie, privi di gestione dell’identità e di controlli di accesso granulari, esibiscono un’idoneità minima e dovranno affidarsi a meccanismi esterni di enforcement.

La fase T conduce alla mappatura della superficie d’attacco. NovaGrid riconosce di essere esposta soprattutto a tre delle categorie di minaccia canoniche: la minaccia interna, le vulnerabilità della supply chain e gli attori di tipo nation-state, con il ransomware come minaccia trasversale ad alto impatto, aggravata dalle fragilità dell’infrastruttura legacy. La mappatura individua punti di ingresso che vanno dall’accesso remoto dei fornitori agli aggiornamenti firmware, dai supporti rimovibili collegati alle workstation ai dispositivi legacy che costituiscono altrettanti blind spot. Particolare attenzione è riservata al rischio di manomissione in transito degli apparati – relè e controllori – durante la consegna dai fornitori, dove la discontinuità di visibilità nella logistica dell’ultimo miglio apre un varco di fiducia sfruttabile.

Nella fase R, NovaGrid pondera i controlli candidati rispetto ai vincoli operativi. L...