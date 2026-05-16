---
title: «Breaking TCAS»: vulnerabilità e attacchi nella sicurezza aerea
url: https://www.ictsecuritymagazine.com/articoli/breaking-tcas-sicurezza-aerea/
source: ICT Security Magazine
date: 2026-05-15
fetch_date: 2026-05-16T05:15:31.808962
---

# «Breaking TCAS»: vulnerabilità e attacchi nella sicurezza aerea

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

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Cyber Crime Conference, Alessio Merlo «Breaking TCAS» vulnerabilità e attacchi nella sicurezza aerea](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-Alessio-Merlo-Breaking-TCAS-vulnerabilita-e-attacchi-nella-sicurezza-aerea-scaled.jpg)

# «Breaking TCAS»: vulnerabilità e attacchi nella sicurezza aerea

A cura di:[Redazione](#molongui-disabled-link)  Ore 15 Maggio 202613 Maggio 2026

Alla 1[4ª edizione della Cyber Crime Conference](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026), ospitata a Roma il 6 e 7 maggio 2026 nell’Auditorium della Tecnica, il Prof. Alessio Merlo, Direttore del Centro Alti Studi per la Difesa (CASD, Scuola Superiore Universitaria), ha presentato i risultati di una ricerca condotta dal CASD insieme all’Università di Genova sulle vulnerabilità del *Traffic Collision Avoidance System* (TCAS), il sistema anticollisione obbligatorio sugli aerei di linea.

L’intervento, intitolato «*Breaking TCAS*: vulnerabilità e attacchi nella sicurezza aerea», si è mosso su due piani: da un lato l’illustrazione di due distinte vulnerabilità del protocollo TCAS, dall’altro la formulazione di un’ipotesi tecnicamente motivata per spiegare l’incidente avvenuto il 1° marzo 2025 lungo la traiettoria di avvicinamento all’Aeroporto Ronald Reagan di Washington (DCA).

![Cyber Crime Conference, Alessio Merlo «Breaking TCAS» vulnerabilità e attacchi nella sicurezza aerea](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-Alessio-Merlo-Breaking-TCAS-vulnerabilita-e-attacchi-nella-sicurezza-aerea-2-700x467.jpg)

*Alessio Merlo alla Cyber Crime Conference 2026*

## Il contesto: ATC, radar secondario e TCAS

Il controllo del traffico aereo poggia sulla torre di controllo (*Air Traffic Control*, ATC), che gestisce gli atterraggi tramite il radar primario. Quando un aereo si trova lontano dall’aeroporto, entra in gioco un secondo livello di sorveglianza: il radar secondario, basato sullo scambio di segnali radio in radiofrequenza fra aeromobili. Misurando il tempo di risposta in funzione della velocità della luce, ogni velivolo stima la distanza e la posizione degli altri aerei nelle vicinanze.

Al di sopra del radar secondario opera il TCAS, introdotto circa quarant’anni fa e considerato l’ultima barriera per la prevenzione delle collisioni. Funziona in modo autonomo e genera due tipologie di allerta:

* ***Traffic Advisory*** **(TA)**: avviso visivo al pilota della presenza di un altro aereo, con l’indicazione della posizione e dell’altitudine.
* ***Resolution Advisory*** **(RA)**: manovra evasiva automatica e coordinata fra due velivoli in rotta di collisione (uno sale, l’altro scende).

Come ha sottolineato Merlo, il protocollo TCAS è stato progettato in un’epoca in cui la cybersecurity non era una priorità di design: non prevede autenticazione, né controllo di integrità, né cifratura.

## Iniettare aerei falsi: la prima vulnerabilità

Nel 2023 il gruppo di ricerca del CASD e dell’Università di Genova ha cominciato a studiare la [possibilità di iniettare contatti aerei falsi sul radar di un velivolo bersaglio](https://www.usenix.org/conference/usenixsecurity24/presentation/longo), fino a indurlo a generare TA e RA reali.

L’unica protezione fisica del protocollo era il ritardo fisso di 128 microsecondi previsto dalla modalità Modo S: per far comparire un aeromobile a una distanza più prossima all’aereo sotto attacco rispetto alla posizione reale dell’attaccante, quest’ultimo avrebbe dovuto rispondere a un’interrogazione in tempi più brevi di tale ritardo, anticipando di fatto la risposta legittima. Storicamente, questa barriera temporale aveva reso l’attacco irrealizzabile con hardware comune.

I ricercatori hanno dimostrato che l’evoluzione dell’hardware *Software Defined Radio* (SDR) ha riscritto lo scenario: oggi l’attacco è realizzabile con apparati dal costo di circa 10.000 euro e funziona fino a 5 chilometri di distanza dall’aereo bersaglio, una portata particolarmente critica nelle fasi di atterraggio.

## Disabilitare le RA: l’exploit del Sensitivity Level

La seconda vulnerabilità individuata riguarda il *Sensitivity Level* (SL), il parametro che regola la soglia di attivazione delle *Resolution Advisory*. Lo standard prevede che il valore di SL possa essere modificato dalle stazioni di terra in scenari operativi complessi, come gli avvicinamenti in aree congestionate.

Un attaccante può falsificare il comando di terra e impostare SL=0, disabilitando completamente la generazione di RA: il TCAS continua a emettere TA, ma non produce più la manovra evasiva automatica. Il ripristino richiede il riavvio del sistema, un’operazione tutt’altro che banale in volo.

#### La timeline della *responsible disclosure*

La scoperta delle vulnerabilità ha innescato un articolato iter di *responsible disclosure*, che ha coinvolto le *United Nations* (UN), l’*European Union Aviation Safety Agency* (EASA), la *Federal Aviation Administration* (FAA), l’Ente Nazionale per l’Aviazione Civile (ENAC), l’Agenzia per la Cybersicurezza Nazionale (ACN) e il Comando per le Operazioni in Rete (COR).

Le tappe principali:

* **Giugno 2023**: scoperta delle vulnerabilità.
* **Febbraio 2024**: sottomissione dell’arti...