---
title: Matrice di allocazione Zero Trust: compromessi, implementazione e maturità
url: https://www.ictsecuritymagazine.com/articoli/matrice-di-allocazione-zero-trust-ot/
source: ICT Security Magazine
date: 2026-10-13
fetch_date: 2026-10-14T06:53:19.516561
---

# Matrice di allocazione Zero Trust: compromessi, implementazione e maturità

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

![Bilancia e scachiera che rappresentano la Matrice di allocazione Zero Trust](https://www.ictsecuritymagazine.com/wp-content/uploads/Matrice-di-allocazione-Zero-Trust.png)

# Matrice di allocazione Zero Trust: compromessi, implementazione e maturità

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 13 Ottobre 20262 Ottobre 2026

*Dalla valutazione del rischio alla scelta dei controlli: la matrice di allocazione MATRIX stabilisce quali capability Zero Trust applicare a ciascun asset OT, come implementarle e quale rischio residuo accettare.*

Nella t[erza parte della serie MATRIX](https://www.ictsecuritymagazine.com/articoli/framework-matrix%E2%80%A6ne-asset-minacce/) ha raccolto tre elementi: che cosa l’impianto deve garantire, quanto ogni classe di dispositivi può accogliere i controlli e da dove può arrivare un attacco.

Questa quarta parte completa il framework. La fase R trasforma queste informazioni in priorità esplicite, la fase I le traduce nella matrice di allocazione, la fase X le distribuisce lungo una roadmap di maturità. Qui compare anche il tratto più distintivo del metodo: ciò che non si può proteggere viene registrato come rischio residuo, non nascosto.

## Risk & tradeoff: rischio e compromessi tra sicurezza e continuità operativa

La quarta fase affronta il nodo che più nettamente distingue l’OT dall’EIT: il compromesso tra sicurezza e continuità operativa. Lo spazio dei compromessi (tradeoff space) è l’insieme delle soluzioni ammissibili che bilanciano requisiti in tensione tra loro – la protezione da un lato, la disponibilità, la safety, le prestazioni e i costi dall’altro. Un controllo che riduca il rischio informatico ma introduca latenza inaccettabile, o che richieda finestre di fermo impianto incompatibili con il servizio, non è una soluzione ma un nuovo problema. L’analisi consiste perciò nel valutare, per ogni controllo candidato, non solo la riduzione di rischio che apporta ma anche gli effetti collaterali che genera sulle altre dimensioni del sistema.

Il risultato è una prioritizzazione: combinando la criticità di missione di ciascun asset (dalla fase M), il suo profilo di idoneità (dalla fase A) e la sua esposizione alle minacce (dalla fase T), si ottiene una graduatoria che indica dove l’investimento in controlli zero trust produce il massimo beneficio a parità di impatto operativo. Questa graduatoria non è statica: lo spazio dei compromessi muta nel tempo al variare delle tecnologie disponibili, dei vincoli di budget e del panorama delle minacce, e va perciò riesaminato periodicamente. La quarta fase, in sostanza, trasforma la conoscenza accumulata nelle tre precedenti in criteri di decisione espliciti e difendibili.

> **Output Risk & Tradeoff**: priorità dei controlli tra rischio e impatto operativo

## Matrice di allocazione Zero Trust: come assegnare le capability agli asset OT

La quinta fase produce l’artefatto che dà nome al framework. La matrice di allocazione incrocia, sulle righe, le classi di asset individuate e profilate e, sulle colonne, le capability zero trust che si intende dispiegare – tra cui la gestione dell’identità e l’autenticazione a più fattori, la microsegmentation, l’autorizzazione continua basata su policy, la protezione crittografica e i controlli di integrità, la verifica della postura dei dispositivi e il monitoraggio con registrazione centralizzata.

Ogni cella esprime non un semplice sì/no, ma la modalità con cui la capability può essere realizzata su quella classe di asset, secondo quattro esiti possibili: applicazione nativa sul dispositivo, applicazione mediata da un layer intermediario, controllo compensativo esterno, oppure non praticabilità. La Tabella 1 ne offre un esempio illustrativo.

*Tabella 1. Esempio illustrativo di matrice di allocazione delle capability zero trust per classe di asset.*

| **Classe di asset** | **Identità & MFA** | **Microseg-mentation** | **Autorizz. continua** | **Crittografia & integrità** | **Postura dispositivo** | **Montaggio & logging** |
| --- | --- | --- | --- | --- | --- | --- |
| HMI/workstation (IT-centric) | Nativo | Nativo | Nativo | Nativo | Nativo | Nativo |
| Server SCADA | Nativo | Nativo | Nativo | Nativo | Nativo | Nativo |
| IED moderno (Liv. 1) | Intermed. | Nativo | Intermed. | Nativo | Intermed. | Nativo |
| IED/RTU legacy | Intermed. | Intermed. | Intermed. | Intermed. | – | Intermed. |
| Dispositivi di campo (Liv. 0) | – | Compens. | – | – | – | Compens. |

***Legenda:*** *Nativo = applicazione del controllo sul dispositivo; Intermed. = enforcement mediato da un layer intermediario; Compens. = controllo compensativo esterno; – = non praticabile. I valori hanno carattere esemplificativo e vanno determinati caso per caso mediante le fasi A e R del framework.*

La logica sottostante deriva direttamente dal profilo di idoneità. Per gli asset a centratura IT e ampio margine – HMI e server – la maggior parte delle capability è applicabile nativamente. Per i dispositivi a bassa idoneità – gli IED legacy – l’enforcement non può risiedere sul dispositivo e deve essere delegato: un layer intermediario può offrire un’interfaccia standardizzata verso protocolli e apparati eteroge...