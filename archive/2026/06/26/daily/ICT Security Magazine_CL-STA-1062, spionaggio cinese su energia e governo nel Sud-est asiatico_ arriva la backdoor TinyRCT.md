---
title: CL-STA-1062, spionaggio cinese su energia e governo nel Sud-est asiatico: arriva la backdoor TinyRCT
url: https://www.ictsecuritymagazine.com/notizie/cl-sta-1062-tinyrct-sud-est-asiatico/
source: ICT Security Magazine
date: 2026-06-26
fetch_date: 2026-06-27T05:52:18.487020
---

# CL-STA-1062, spionaggio cinese su energia e governo nel Sud-est asiatico: arriva la backdoor TinyRCT

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

![CL-STA-1062, spionaggio cinese su energia e governo nel Sud-est asiatico arriva la backdoor TinyRCT](https://www.ictsecuritymagazine.com/wp-content/uploads/CL-STA-1062-spionaggio-cinese-su-energia-e-governo-nel-Sud-est-asiatico-arriva-la-backdoor-TinyRCT.png)

# CL-STA-1062, spionaggio cinese su energia e governo nel Sud-est asiatico: arriva la backdoor TinyRCT

A cura di:[Redazione](#molongui-disabled-link)  Ore 26 Giugno 202626 Giugno 2026

[Unit 42](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/), la divisione di *threat intelligence* di Palo Alto Networks, ha pubblicato il 25 giugno l’analisi di una campagna di *cyber espionage* contro entità governative e infrastrutture critiche nel Sud-est asiatico. Dietro l’attività c’è un cluster che la società traccia come CL-STA-1062, che ha preso di mira in particolare imprese statali dei settori energetico e governativo, affiancando agli strumenti *open source* una *backdoor* su misura mai documentata prima, battezzata *TinyRCT*.

## Chi è CL-STA-1062 e cosa colpisce

Unit 42 descrive gli operatori come attori di lingua cinese, attivi almeno da marzo 2022, e valuta con alta confidenza che si tratti dello stesso cluster monitorato da Cisco Talos come UAT-7237, già noto per campagne contro infrastrutture di web hosting a Taiwan a metà 2025. La convergenza degli indizi, lingua degli operatori, una riga di codice in cinese semplificato dentro la *backdoor* e la sovrapposizione con UAT-7237, colloca il gruppo nel perimetro dello spionaggio a sfondo statale; resta però una designazione tecnica per attività raggruppata, non un’attribuzione formale a un governo, e va trattata come tale al pari di altri [threat actor cinesi](https://www.ictsecuritymagazine.com/articoli/threat-actors-made-in-china/).

Sul piano operativo il gruppo combina strumenti *open source* diffusi: *SoftEther VPN* e *VNT* per il *tunneling* e il movimento laterale, *Mimikatz* per le credenziali e *JuicyPotato* per l’elevazione dei privilegi, affiancati dalla nuova componente proprietaria *TinyRCT*. La cronologia ricostruita da Unit 42 indica che a settembre 2025 gli attaccanti avevano compromesso un’entità governativa della regione, installando *web shell* ed esfiltrando dati da un database MSSQL; da metà 2025, in parallelo, l’attenzione si è spostata sulle infrastrutture critiche, con la scansione di entità del comparto energetico alla ricerca di vulnerabilità sfruttabili. Tra ottobre e dicembre 2025 Unit 42 ha osservato la probabile compromissione di almeno dieci organizzazioni nella regione.

## TinyRCT, la nuova backdoor su misura

La catena di infezione parte da un archivio
`chrome_setup.zip`
che sfrutta la tecnica dell’*AppDomainManager Injection*: un eseguibile legittimo e firmato, un file di configurazione malevolo e la DLL
`MyAppDomainManager.dll`
portano al download di
`PerfWatson2.exe`
, con persistenza affidata a uno *scheduled task* mascherato da GoogleUpdater. *TinyRCT* è un *RAT* leggero scritto in C# e rivolto a Windows: consente l’esecuzione di comandi arbitrari, l’enumerazione e l’esfiltrazione di file, la cattura dello schermo e dispone di un meccanismo di autodistruzione per rimuovere le tracce. Per passare inosservato, l’eseguibile si maschera da
`PerfWatson2.exe`
, che è realmente il nome del componente di telemetria di Microsoft Visual Studio.

Il canale di comando e controllo punta al server
`45.32.113[.]172`
: il traffico viaggia su normale HTTP, ma i dati scambiati sono cifrati in AES-128 in modalità CBC, con una chiave incorporata nel codice (
`ThisIsASecretKey87654321`
). È proprio nella routine di gestione dei dati che Unit 42 ha individuato la riga di codice in cinese semplificato. Un impianto sviluppato ad hoc, accanto a utility pubbliche, mostra un gruppo capace di costruire strumenti per esigenze specifiche e di contenere l’impronta riconoscibile.

## Una minaccia destinata a durare

La scelta dei bersagli, energia e amministrazione pubblica di un’intera area, insieme allo sviluppo di malware proprietario, indica una minaccia destinata a durare. È lo stesso schema di interesse strategico verso le [infrastrutture critiche](https://www.ictsecuritymagazine.com/articoli/volt-typhoon-e-larte-di-scomparire-vivere-di-ot-log-scarsi-e-tanta-pazienza/) che ha reso celebre il pre-posizionamento di attori cinesi come Volt Typhoon, qui arricchito da una *backdoor* dedicata oltre alle tecniche *living-off-the-land*. Per i difensori della regione, e per chi ha filiere o controllate nell’area, le indicazioni sono concrete: monitoraggio comportamentale sugli eseguibili non fidati, perché *TinyRCT* prova a confondersi con un binario di sistema; attenzione agli accessi VPN e ai dispositivi perimetrali usati come testa di ponte; e ricerca mirata del set completo di indicatori pubblicati da Unit 42, dai quattro indirizzi di comando e controllo agli hash dei file.

Condividi sui Social Network:

Tag articolo:  [#APT](https://www.ictsecuritymagazine.com/tag/apt/ "APT")[#backdoor](https://www.ictsecuritymagazine.com/tag/backdoor/ "backdoor")[#CL-STA-1062](https://www.ictsecuritymagazine.com/tag/cl-sta-1062/ "CL-STA-1062")[#Energia](https://www.ictsecuritymaga...