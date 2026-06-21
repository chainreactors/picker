---
title: ITDR: quando l’attaccante non entra, ma fa login
url: https://www.ictsecuritymagazine.com/digital-id-security/itdr-identity-threat-detection-response/
source: ICT Security Magazine
date: 2026-06-20
fetch_date: 2026-06-21T06:50:15.256826
---

# ITDR: quando l’attaccante non entra, ma fa login

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

![ITDR](https://www.ictsecuritymagazine.com/wp-content/uploads/ITDR-.png)

# ITDR: quando l’attaccante non entra, ma fa login

A cura di:[Redazione](#molongui-disabled-link)  Ore 20 Giugno 20269 Giugno 2026

ITDR è l’acronimo di *Identity Threat Detection and Response*, e descrive una disciplina nata per colmare un vuoto che è diventato impossibile ignorare: nessuno sorvegliava l’identità mentre l’identità diventava il bersaglio principale. Gli attaccanti, sempre più spesso, non sfondano un perimetro né lasciano *malware* da riconoscere. Fanno una cosa più semplice e più difficile da fermare: si autenticano, con credenziali o, peggio, con sessioni rubate che hanno già superato ogni controllo. L’ITDR esiste per accorgersi proprio di questo, quando un accesso legittimo viene usato da chi non dovrebbe.

Il punto di partenza è una constatazione che ribalta vent’anni di abitudini difensive. La sicurezza ha imparato a sorvegliare gli endpoint, con i sistemi di rilevamento sul dispositivo, e la rete, con quelli sul traffico. Ma il livello dove oggi si gioca la partita, l’infrastruttura che gestisce le identità, è rimasto un punto cieco. La gestione degli accessi decide chi può entrare; quasi nessuno controlla cosa succede dopo che qualcuno è entrato, e se quel qualcuno è davvero chi dice di essere.

## L’identità è il perimetro, e quasi nessuno la sorveglia

La distinzione che chiarisce il ruolo dell’ITDR è quella con la gestione delle identità e degli accessi. Quest’ultima è preventiva: stabilisce chi ha diritto di accedere a cosa, e applica le regole al momento del login. È necessaria, ma si ferma sulla soglia. Una volta concesso l’accesso, non osserva più, e dà per scontato che chi ha presentato credenziali valide sia legittimo. L’ITDR lavora esattamente dopo quel momento, monitorando i segnali che indicano che un meccanismo di accesso legittimo viene sfruttato in modo ostile.

Anche il confronto con il rilevamento sugli endpoint aiuta. Quegli strumenti sorvegliano workstation e server alla ricerca di comportamenti malevoli, ma non vedono l’infrastruttura delle identità, l’*Active Directory*, l’*Entra ID*, i provider di identità in cloud, dove si consumano attacchi che sul dispositivo non lasciano traccia sospetta. È un livello che richiede sensori propri, ed è la ragione per cui Gartner, che ha coniato il termine ITDR nel 2022, lo descrive come la capacità mancante tra i controlli preventivi sull’identità e le operazioni di sicurezza. La categoria, va detto, è ormai riconosciuta, e tutti i grandi fornitori la presidiano sul piano commerciale; ciò che resta scoperto, nella pratica di molte organizzazioni, è proprio il livello che essa dovrebbe sorvegliare. La difesa dell’[identità](https://www.ictsecuritymagazine.com/notizie/ai-agentici-identity-security/), in un’epoca in cui gli attaccanti entrano con le chiavi giuste, non è più un dettaglio di amministrazione, è un fronte di rilevamento a sé.

## Cosa rileva l’ITDR che gli altri non vedono

Il valore di questo livello si capisce dagli attacchi che intercetta, quasi tutti invisibili a chi guarda altrove. Tecniche contro Active Directory come il Kerberoasting, il Golden Ticket e il Silver Ticket, il DCSync, il Pass-the-Hash vivono di richieste che, prese singolarmente, sembrano legittime. Un Kerberoasting, per esempio, consiste in normali richieste di ticket di servizio Kerberos: un sistema di rilevamento sull’endpoint non ha motivo di segnalarle, mentre l’ITDR le legge nel contesto dell’infrastruttura delle identità e le riconosce per ciò che sono, il primo passo di un furto di credenziali.

A questi si aggiungono il credential stuffing, l’escalation anomala di privilegi, gli accessi da posizioni o orari incongrui, l’abuso di [account privilegiati](https://www.ictsecuritymagazine.com/articoli/sicurezza-accessi-privilegiati/). Il filo comune è che nessuno di questi attacchi rompe qualcosa: tutti sfruttano la fiducia che il sistema ripone in una credenziale o in un ticket validi. Per questo Gartner raccomanda di spostare il rilevamento da un approccio basato su firme e anomalie generiche a uno centrato sull’avversario, ancorato alle tecniche catalogate nel [framework MITRE ATT&CK](https://attack.mitre.org/): non cercare il file malevolo, ma il comportamento dell’attaccante che usa l’identità come arma.

## ITDR contro il furto di token: oltre l’MFA

Il fronte più caldo del momento mostra perché l’ITDR sia diventato urgente. L’attacco identitario dominante non è più indovinare una password, è rubare una sessione già autenticata. Un *token* o un *cookie* di sessione sottratti dal browser di una vittima permettono di accedere a un servizio senza conoscere la password e, soprattutto, senza dover ripetere l’autenticazione a più fattori. La ragione è strutturale: quel *token* è la prova che l’autenticazione è già avvenuta, e il servizio non ha modo di accorgersi che viene rigiocato da un altro computer. È il motivo per cui l’MFA, presidio indispensabile, non è più sufficiente da solo, e per cui gli attacchi di tipo *adversary-in-the-middle*, che intercettano la sessione in tempo reale, sono cresciuti rapidamente.

Qui l’ITDR fa ciò che nessun controllo di a...