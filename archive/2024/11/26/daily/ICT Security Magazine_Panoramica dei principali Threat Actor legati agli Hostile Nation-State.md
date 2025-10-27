---
title: Panoramica dei principali Threat Actor legati agli Hostile Nation-State
url: https://www.ictsecuritymagazine.com/articoli/threat-actor-hostile-nation/
source: ICT Security Magazine
date: 2024-11-26
fetch_date: 2025-10-06T19:26:16.592962
---

# Panoramica dei principali Threat Actor legati agli Hostile Nation-State

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

![Threat Actor Hostile Nation State](https://www.ictsecuritymagazine.com/wp-content/uploads/Threat-Actor-Hostile-Nation-State.jpg)

# Panoramica dei principali Threat Actor legati agli Hostile Nation-State

A cura di:[Francesco Schifilliti](#molongui-disabled-link)  Ore 25 Novembre 2024

Nel presente articolo si vuole ripercorrere la nascita dei concetti di minaccia cyber e di *threat actor,* avvenuta davvero da pochi anni e che giustifica tutti gli sforzi che attualmente si stanno compiendo per stabilire framework con cui definire lo svolgimento di un attacco e classificare/categorizzare al meglio un avversario. Successivamente, saranno analizzati i principali governi che sono oggi considerati ostili e i *threat actor* a loro legati, fino a introdurre una metodologia che permetta di farne una valutazione.

Dal punto di vista storico, le prime menzioni di *targeted cyber threats* e, in particolare, di *cyber threat* al di fuori degli ambiti governativi sono apparse nel 2001 durante un briefing non classificato della National Security Agency del 2010. Il termine APT[[1]](#_ftn1) (o *Advanced Persistent Threat*) è stato invece utilizzato per la prima volta durante una discussione all’Air Force Intelligence Agency in cui si cercava un termine per classificare una specifica tipologia di attaccanti, molto ben addestrati, che con ogni probabilità erano finanziati e addestrati da enti governativi.

Una definizione attualmente condivisa di *Advanced Persistent Threat* è fornita dal NIST SP 800-39[[2]](#_ftn2), che li descrive come:

> *“an adversary with sophisticated levels of expertise and significant resources, allowing it through the use of multiple different attack vectors (e.g., cyber, physical, and deception), to generate opportunities to achieve its objectives which are typically to establish and extend its presence within the information technology infrastructure of organizations for purposes of continually exfiltrating information and/or to undermine or impede critical aspects of a mission, program, or organization, or place itself in a position to do so in the future; moreover, the advanced persistent threat pursues its objectives repeatedly over an extended period of time, adapting to a defender’s efforts to resist it, and with determination to maintain the level of interaction needed to execute its objectives”*.

Una caratteristica chiave di un attacco APT è l’uso congiunto di tecniche manuali e automatizzate per raggiungere i propri obiettivi, che possono consistere nella compromissione di computer e di dispositivi mobili. Gli APT sono generalmente associati ad attacchi sponsorizzati dai governi, ma sono utilizzati anche da organizzazioni criminali e da singoli individui.

Generalmente – data la loro complessità – gli APT sono attacchi *multi-stage*, possono richiedere anche molto tempo per essere preparati e l’aspettativa degli attaccanti è che la compromissione non sia rilevata per per molto tempo (o addirittura anni).

Le fasi che compongono un attacco APT sono le seguenti:

* ***Observation/Social Engineering:*** ricerca e raccolta di dati sul target dell’attacco;
* ***Section:*** *delivery* del *malware* che sarà utilizzato nell’attacco attraverso la tattica scelta (*Phishing, Exploit Public-Facing Application, Drive-by Compromise,*);
* ***Discovery:*** dopo aver ottenuto l’accesso, gli attaccanti devono agire rapidamente per evitare il loro riconoscimento;
* ***Catch & Exfiltration:*** i dati riservati del target raccolti durante l’attacco sono inviati ai server dagli attaccanti. Questa fase può essere molto lunga e può contemplare l’interazione continua tra l’attaccante e l’infrastruttura target.

Un attacco basato su APT si differenzia moltissimo dagli attacchi informatici di base e possiamo considerare almeno i seguenti aspetti distintivi:

* un APT è più complesso di una generica minaccia online, in quanto la realizzazione degli strumenti impiegati e l’esecuzione dell’attacco comportano che il gruppo di attaccanti lavori a tempo pieno per realizzarla. Nel *setup* dell’attacco deve essere anche considerato il tempo in cui gli avversari – dopo aver trovato il primo punto di accesso all’infrastruttura target – svolgono le attività manuali necessarie a garantirne la miglior persistenza;
* gli APT sono creati per perseguire specifici obiettivi (come, ad esempio, specifiche organizzazioni o determinati settori industriali) e quindi non rappresentano una minaccia generale. Per questa caratteristica, gli APT si definiscono *tailored*.

Nella Figura 1 sono mostrate tutte le fasi che compongono un attacco di tipo APT:

![ Advanced Persistent Threat (APT) Attack Lifecycle dei threat actor](https://www.ictsecuritymagazine.com/wp-content/uploads/006-1-700x390.png)

Fig. 1 – Advanced Persistent Threat (APT) Attack Lifecycle

Gli attori di *Advanced Persistent* *Threat* possono appartenere ad una (a volte più d’una) tra le seguenti categorie:

* *Terrorists*
* *Corporate espionage actor*
* *Nation-state actor*
* *Organized criminal actor*
* *Hacktivist*

Le motivazioni alla base degli attacchi APT possono variare notevolmente, ma le finalità primarie di solito rientrano tra le seguenti:

* raccogliere informazioni;
* ottenere un punto di ingresso per realizzare successive fasi di un attac...