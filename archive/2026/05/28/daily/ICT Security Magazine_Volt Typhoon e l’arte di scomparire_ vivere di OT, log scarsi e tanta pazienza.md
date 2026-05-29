---
title: Volt Typhoon e l’arte di scomparire: vivere di OT, log scarsi e tanta pazienza
url: https://www.ictsecuritymagazine.com/articoli/volt-typhoon-e-larte-di-scomparire-vivere-di-ot-log-scarsi-e-tanta-pazienza/
source: ICT Security Magazine
date: 2026-05-28
fetch_date: 2026-05-29T06:06:34.775995
---

# Volt Typhoon e l’arte di scomparire: vivere di OT, log scarsi e tanta pazienza

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Volt Typhoon attacco APT a infrastrutture critiche e supply chain OT, Stefano Maccaglia, LOTL, living-off-the-land, cyber spionaggio cinese, Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Volt-Typhoon-attacco-APT-a-infrastrutture-critiche-e-supply-chain-OT-Stefano-Maccaglia-LOTL-living-off-the-land-cyber-spionaggio-cinese-Cyber-Crime-Conference-2026-scaled.jpg)

# Volt Typhoon e l’arte di scomparire: vivere di OT, log scarsi e tanta pazienza

A cura di:[Redazione](#molongui-disabled-link)  Ore 28 Maggio 202615 Maggio 2026

*Dall’intervento di Stefano Maccaglia, Director of Incident Response e Red Team di NetWitness, alla [14ª Cyber Crime Conference](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026) (Roma, Auditorium della Tecnica, 6-7 maggio 2026).*

Quando un avversario sceglie il silenzio come strategia, la difesa deve cambiare grammatica. È la tesi con cui Stefano Maccaglia, alla guida dell’Incident Response globale di NetWitness, ha chiuso una delle sessioni più tecniche della prima giornata della 14ª Cyber Crime Conference, portando in sala un caso poco raccontato di compromissione attribuita a **Volt Typhoon**: un attacco mirato al cuore della logistica navale *just-in-time* europea, condotto senza *malware* visibile, senza rumore di rete e con un obiettivo netto, restare dentro il più a lungo possibile.

Il team di Maccaglia, lo ricordiamo, affonda le radici nelle attività di IR nate nel 2011 in seguito al *breach* di RSA Security ed è oggi specializzato nelle investigazioni di *cyber espionage* e *cyber crime* di matrice sofisticata, in particolare quelle riconducibili ad attori state-sponsored.

## Volt Typhoon, un attore che non improvvisa

Volt Typhoon, ricondotto con elevata confidenza al perimetro del [*cyber espionage* cinese](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a), è oggi uno degli attori più problematici a livello globale per chi gestisce infrastrutture critiche. La sua firma operativa, ha sintetizzato Maccaglia, poggia su tre pilastri:

* *living-off-the-land* (LOTL), ovvero lo sfruttamento di file eseguibili, applicazioni e strumenti già presenti nei sistemi della vittima;
* compromissione di *supply chain* e di partner terzi a basso presidio di sicurezza;
* persistenza prolungata e *pre-positioning* in vista di possibili azioni *disruptive*

L’obiettivo non è quasi mai l’azione immediata contro il *target* finale. È, piuttosto, il posizionamento. Da qui un *dwell time* tipicamente molto ampio, tracce volutamente esigue sugli *endpoint* e movimenti laterali al limite della soglia di visibilità.

Maccaglia ha insistito su un punto culturale prima ancora che tecnico: questo attore non improvvisa. Studia in modo metodico le debolezze sociali, organizzative e di IT del bersaglio, mappa il personale chiave, modella i propri orari operativi sui *working hours* della vittima, e solo dopo si attiva, aprendo varchi nelle aree meno presidiate. È un comportamento, ha osservato, che lo rende riconoscibile rispetto agli attori attualmente molto attivi nello stesso teatro mediorientale: a diffenza degli iraniani, ad esempio, che sono piuttosto rumorosi, Volt Typhoon è invisibile.

#### La firma operativa: LOTL, *fileless*, tunnel cifrati

La [toolchain di Volt Typhoon](https://attack.mitre.org/groups/G1017/), sul piano tecnico, è coerente con quanto rilevato dalle principali agenzie occidentali. Le tecniche *fileless*, con esecuzione in memoria, sono il tratto distintivo: PowerShell, WMI, .NET *assemblies* eseguiti senza scrittura su disco, con largo uso di LOLBin come rundll32, mshta, certutil, regsvr32, msiexec. A questo si aggiunge l’utilizzo opportunistico di software di gestione remota legittimi che gli attaccanti trovano già installati negli ambienti compromessi, AnyDesk, ScreenConnect, Atera, e che riconoscono immediatamente come scorciatoia operativa: non li installano, li ereditano.

Sul piano del traffico, l’attore predilige tunnel SSL e canali cifrati che si confondono nel normale HTTPS aziendale, anche per attraversare segmentazioni di rete. L’esfiltrazione, dove esiste, si appoggia in modo elegante a servizi commerciali comuni come AWS o Dropbox, scegliendo di volta in volta lo *stack* meno appariscente sul perimetro della vittima. Non si tratta di una scelta programmata a tavolino: è una scelta opportunistica, fatta sul campo, in funzione di ciò che l’attaccante trova disponibile e poco monitorato.

##### I precedenti: dalle infrastrutture critiche USA a Guam

Maccaglia ha richiamato due casi-scuola ormai documentati anche dalle autorità statunitensi.

Il primo è la compromissione di **infrastrutture critiche statunitensi nel 2023**, con bersagli nei comparti *power grid* e trasporto marittimo continentale. In quel contesto, la persistenza è stata realizzata in modo emblematico direttamente sui router SOHO presenti nelle filiali periferiche delle organizzazioni colpite. Apparati di piccolo cabotaggio, tipicamente non *patchati*: i bollettini di vendor come D-Link, ha osservato Maccaglia con una battuta, vengono letti da pochi e implementati da ancora meno. La periferia non presidiata diventa così l’anticamera dell’infrastruttura, mentre il *data center*, *crown j...