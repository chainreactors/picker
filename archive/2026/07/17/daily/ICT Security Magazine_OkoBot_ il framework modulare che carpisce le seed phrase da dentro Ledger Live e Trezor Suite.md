---
title: OkoBot: il framework modulare che carpisce le seed phrase da dentro Ledger Live e Trezor Suite
url: https://www.ictsecuritymagazine.com/notizie/okobot-seed-phrase-ledger-trezor/
source: ICT Security Magazine
date: 2026-07-17
fetch_date: 2026-07-18T04:46:26.091250
---

# OkoBot: il framework modulare che carpisce le seed phrase da dentro Ledger Live e Trezor Suite

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

![OkoBot il framework modulare che carpisce le seed phrase da dentro Ledger Live e Trezor Suite](https://www.ictsecuritymagazine.com/wp-content/uploads/OkoBot-il-framework-modulare-che-carpisce-le-seed-phrase-da-dentro-Ledger-Live-e-Trezor-Suite.png)

# OkoBot: il framework modulare che carpisce le seed phrase da dentro Ledger Live e Trezor Suite

A cura di:[Redazione](#molongui-disabled-link)  Ore 17 Luglio 202617 Luglio 2026

Il team GReAT di Kaspersky ha documentato nel [report di Securelist](https://securelist.com/okobot-framework-targets-cryptocurrency-wallets/120660/) OkoBot, un framework malevolo composto da oltre venti moduli che colpisce gli utenti di criptovaluta su Windows. La catena di attacco è stata ridisegnata a fine aprile 2025; la telemetria sulle vittime copre il periodo aprile 2025-giugno 2026 e GReAT ne ha identificato gli attacchi a gennaio 2026. La campagna è attiva da oltre un anno ed è tuttora in corso, con centinaia di vittime in più di venticinque Paesi, concentrate in Brasile, Vietnam, Canada, Messico e Turchia. Secondo Dmitry Galov (GReAT), citato nel [comunicato di Kaspersky](https://www.kaspersky.com/about/press-releases/kaspersky-reveals-a-new-malicious-framework-targeting-cryptocurrency-users-with-the-use-of-okospyware), i vettori osservati indicano gli sviluppatori tra i bersagli primari: un dettaglio che sposta la vicenda dal solo furto di criptovaluta al rischio d’ingresso in ambienti aziendali.

## Vettori d’ingresso: repository GitHub fasulli e *ClickFix*

Il primo canale è la [tecnica ClickFix](https://www.ictsecuritymagazine.com/notizie/clickfix-attacco-social-engineering/), che induce la vittima a incollare ed eseguire comandi apparentemente innocui. Il secondo è più raffinato: un repository GitHub esistito da fine marzo 2025 a giugno dello stesso anno, composto dal solo
`README.md`
con una finta guida d’installazione in stile ufficiale, indicizzato in cima ai risultati dei motori per la query
`SSMS`
. Il pacchetto che prometteva SQL Server Management Studio consegnava in realtà una versione dell’editor audio Audacity con un impianto malevolo incorporato in una libreria. Non è avvelenamento della catena di fornitura, perché non risultano compromessi né un pacchetto legittimo né l’account di un manutentore: è abuso di piattaforma e *SEO poisoning*. Il perno, tuttavia, è lo stesso già osservato nelle campagne di [pacchetti open source](https://www.ictsecuritymagazine.com/notizie/supply-chain-attack-nordcorea/) avvelenati contro gli sviluppatori, la fiducia implicita negli strumenti di lavoro quotidiani. Cambia il vettore, resta la superficie.

## La catena e la persistenza RDP

Lo script
`TookPS`
installa SSH sulla macchina della vittima, apre una connessione verso il server SSH controllato dagli attaccanti e inoltra la porta del demone SSH locale. Dopo un ritardo, è un *bot* SSH automatizzato, operante lato attaccante, a collegarsi alla porta inoltrata per consegnare i payload: il *bot* non risiede sull’host colpito. È questo *bot* a costruire la persistenza più interessante per un pubblico enterprise. Apre le porte del *firewall* per il traffico RDP in ingresso, crea un utente nel gruppo “Remote Desktop Users”, sostituisce la
`termsrv.dll`
legittima con una versione modificata per consentire sessioni RDP concorrenti e crea un’attività pianificata chiamata
`Apple Sync`
che mantiene ogni ora un tunnel SSH inverso sulla porta RDP locale.

Da qui parte l’anello che porta ai plugin. Il *bot* recupera i moduli via SFTP e li esegue tramite
`HDUtil`
, un *launcher* protetto con VMProtect, usando il comando
`target`
; l’argomento opzionale
`nouac`
di quel comando esegue il *bypass* dell’UAC tramite RPC di Windows e un
`msconfig.exe`
auto-elevato, tecnica descritta da Google Project Zero nel 2019. L’ultima consegna è
`Volume2`
, un’utility open source collegata a una
`protobuf.dll`
malevola: la libreria appare legittima ma espone una funzione
`ProtobufGetVer2`
che decritta e avvia l’implant vero, cioè il *dispatcher* di plugin. Il payload è cifrato con AES-GCM e chiave statica a 256 bit, ma con il tag di autenticazione omesso, quindi senza verifica d’integrità. Il meccanismo è quello del *DLL hijacking*, utile come indicatore per la *detection*; tra i verdetti con cui Kaspersky rileva il framework figura infatti anche
`Trojan.Win32.Dllhijack.*`
.

## L’arsenale modulare e il *dispatcher*

Il *dispatcher* interroga il server di comando ogni venti secondi; i ricercatori hanno individuato cinque plugin: un *wrapper* per CMD, uno per PowerShell, un enumeratore d’ambiente, un *dropper* e un *process injector*. È il *process injector* a mettere in campo i quattro implant veri e propri, iniettandoli in processi legittimi:
`ext_daemon`
,
`SeedHunter`
,
`MC Keylogger`
e
`OkoSpyware`
. Il primo si aggancia ai processi dei browser basati su Chromium, non solo Chrome: per Microsoft Edge, ad esempio, viene agganciata la
`msedge.dll`
. Installa estensioni malevole concedendo tutti i permessi richiesti; nell’attacco analizzato l’estensione installata era
`Rilide`
. L’occultamento passa dalle stesse funzioni interne del browser agganciate dal *loader*: le estensioni malevole finisco...