---
title: Mirage Kitten, il nuovo arsenale di spionaggio: NightLedger e i tunnel che trasformano le vittime in relay
url: https://www.ictsecuritymagazine.com/notizie/mirage-kitten-nightledger/
source: ICT Security Magazine
date: 2026-07-29
fetch_date: 2026-07-30T04:52:21.678360
---

# Mirage Kitten, il nuovo arsenale di spionaggio: NightLedger e i tunnel che trasformano le vittime in relay

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

![Mirage Kitten spionaggio NightLedger](https://www.ictsecuritymagazine.com/wp-content/uploads/Mirage-Kitten-spionaggio-NightLedger.png)

# Mirage Kitten, il nuovo arsenale di spionaggio: NightLedger e i tunnel che trasformano le vittime in relay

A cura di:[Redazione](#molongui-disabled-link)  Ore 29 Luglio 202629 Luglio 2026

Il gruppo di spionaggio noto come Mirage Kitten ha ampliato il proprio arsenale con un impianto Windows finora non documentato e due strumenti di *tunneling* su *WebSocket*. Lo scrive il team GReAT di Kaspersky in una [ricerca di Securelist](https://securelist.com/mirage-kitten-new-tools/120811/) pubblicata il 28 luglio 2026. L’elemento operativo di maggiore interesse non è un nuovo *exploit*, ma il modo in cui il gruppo rende silenziosa e difficile da attribuire l’esfiltrazione: le macchine compromesse diventano nodi di inoltro (*relay*) del traffico dell’attaccante.

Si tratta di spionaggio, non di estorsione. Kaspersky descrive Mirage Kitten come APT di cyber-spionaggio senza indicarne la nazionalità; l’attribuzione all’Iran arriva dagli altri vendor, con [Check Point](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/) che lo qualifica come attore iraniano affiliato all’IRGC e [Unit 42](https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/) che lo colloca tra i gruppi *Iran-nexus* allineati agli obiettivi dell’intelligence di Teheran.

Storicamente il gruppo colpisce aerospazio, aviazione, difesa e telecomunicazioni, ma la *victimology* di questa campagna è più ampia e tocca anche i comparti governativo e finanziario: Kaspersky elenca vittime in Egitto, ambienti PMI e governativi in Giordania e Tanzania, organizzazioni dell’aviazione in Pakistan, società di telecomunicazioni in Etiopia ed entità del settore finanziario in Burkina Faso. Il *deployment* di
`BridgeHead`
, in particolare, è stato osservato in ambienti vittima in Egitto e presso un’organizzazione aerospaziale e dell’aviazione con sede in Pakistan.

Sui nomi conviene procedere con cautela, e lo segnaliamo come scelta redazionale: i vendor tendono a trattarli come equivalenti (Kaspersky scrive *also known as*, Check Point *also tracked as*), ma le mappature restano ricostruzioni dei singoli fornitori e vanno lette come sovrapposizioni, non come identità certe. Kaspersky traccia il gruppo come Mirage Kitten e lo riconduce a UNC1549 (Google), Smoke Sandstorm (Microsoft) e Nimbus Manticore (Check Point); Unit 42 lo segue come Screening Serpens (a sua volta ricondotto a UNC1549, Smoke Sandstorm e *Iranian Dream Job*).

## NightLedger: come entra e cosa fa

`NightLedger`
si maschera da
`SspiCli.dll`
e sfrutta il dirottamento dell’ordine di ricerca delle DLL (*DLL side-loading* / *search-order hijacking*,
`T1574.001`
). Il binario legittimo bersaglio,
`AppVShNotify.exe`
, non importa direttamente
`SspiCli.dll`
, ma importa
`RPCRT4.dll`
, che può caricarla in *delay-load* quando invoca una API RPC che richiede autenticazione: questo consente il caricamento di una
`SspiCli.dll`
malevola co-locata, la quale inoltra alla DLL legittima gli *export* attesi per non rompere il funzionamento del processo. L’impianto esegue ricognizione, comandi, operazioni sui file, enumerazione dei processi e cattura di *screenshot*, raccoglie il file
`NetSetup.log`
(in
`C:Windowsdebug`
) insieme all’output della lista dei processi, e dialoga con il *command and control* tokenizzando il *payload* sul delimitatore
`#%#`
, schema vicino al *backdoor*
`TWOSTROKE`
già documentato da [Google](https://cloud.google.com/blog/topics/threat-intelligence/analysis-of-unc1549-ttps-targeting-aerospace-defense) per lo stesso attore.

## Il tunnel come infrastruttura di occultamento

Il cuore dell’analisi è
`BridgeHead`
. Una volta stabilito il canale *WebSocket*, funziona da proxy
`SOCKS5`
: è il server *command and control* a iniziare tutte le connessioni, mentre la macchina infetta si limita a inoltrare il traffico tra i target indicati e il canale. In questo modo la vittima diventa un *relay* e il traffico verso i sistemi interni sembra originare dalla sua stessa rete, complicando rilevamento e attribuzione. L’impianto è progettato per attraversare i proxy aziendali: gestisce le risposte HTTP
`407`
, negozia l’autenticazione integrata di Windows (Negotiate prima di NTLM) e ripiega sul contesto SSO dell’utente corrente. Questa logica di attraversamento del proxy ricalca da vicino quella di un *backdoor* che Kaspersky traccia internamente come
`Retrograde`
, sovrapposto agli strumenti riportati pubblicamente come
`MiniFast`
(Check Point) e
`MiniUpdate`
(Unit 42): è il nesso più diretto fra le tre ricerche.
`ArcBridge`
, individuato per la prima volta nell’aprile 2026 in attacchi mediorientali, condivide con
`NightLedger`
la logica del *mutex* dal nome in stile UUID.

Sul piano dell’evasione,
`BridgeHead`
verifica il nome utente Windows corrente e attiva il *payload* soltanto se contiene una specifica sottostringa; una variante hardcoda un valore di controllo di tre caratteri che deve comparire, in minuscolo, nel nome utente, a conferma della personalizzazione per singolo bers...