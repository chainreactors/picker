---
title: Installer NoMachine trojanizzato sul server ufficiale: lo CSIRT Italia dirama il bollettino, il vendor lo dichiara bonificato
url: https://www.ictsecuritymagazine.com/notizie/installer-nomachine-trojanizzato-supply-chain-csirt/
source: ICT Security Magazine
date: 2026-11-24
fetch_date: 2026-11-25T10:48:04.836959
---

# Installer NoMachine trojanizzato sul server ufficiale: lo CSIRT Italia dirama il bollettino, il vendor lo dichiara bonificato

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.364 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

  Minacce e attacchi

  + [Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)

  Rischio, norme e privacy

  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)

  Tecnologie

  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)

  Scenari

  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)

  Ultimi in **Cyber Security**

  [Tutti gli articoli di Cyber Security →](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Approfondimenti](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* [Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Eventi ↗](https://eventi.ictsecuritymagazine.com/)

[Newsletter](/newsletter/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca

Attiva/disattiva menu

[Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

# Installer NoMachine trojanizzato sul server ufficiale: lo CSIRT Italia dirama il bollettino, il vendor lo dichiara bonificato

Il bollettino BL02/261124 classifica l’installer NoMachine trojanizzato come attacco alla supply chain con criticità alta. Il vendor lo dichiara bonificato, ma l’indagine resta aperta.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il24 Novembre 202624 Novembre 2026  Condividi

![Installer NoMachine trojanizzato Catena con un anello spezzato e finestra di installazione con barra rossa e avviso: simbolo di un installer alterato](https://www.ictsecuritymagazine.com/wp-content/uploads/installer-nomachine-trojanizzato-supply-chain.webp)

In sintesi

* Per circa venti ore NoMachine ha distribuito dal server ufficiale un installer Windows alterato, scaricabile tra il 19 e il 20 novembre 2026.
* Il pacchetto installa Python di nascosto e crea un'attività pianificata eseguita ogni minuto; il vendor pubblica indicatori e hash MD5.
* Chi ha installato il file deve scollegare il computer, cambiare le password da un dispositivo pulito e reinstallare il sistema operativo.

Aggiornamento del 24 novembre 2026 sull’installer NoMachine trojanizzato. L’avviso originale del vendor è del 20 novembre; le novità di oggi sono il bollettino dello CSIRT Italia (12:16) e un aggiornamento di NoMachine.

Per poco più di venti ore il canale di download ufficiale di NoMachine ha distribuito un installer alterato. Il file è
`nomachine-personal-edition_10.2.3_1_x64.exe`
, l’edizione Personal per Windows del software di accesso remoto, scaricabile dalle 13:43 UTC del 19 novembre alle 10:00 UTC del 20 novembre 2026.

Oggi lo CSIRT Italia ha pubblicato il [bollettino BL02/261124](https://www.acn.gov.it/portale/en/w/supply-chain-attack-installer-malevolo-di-nomachine-personal-edition-per-windows-distribuito-attraverso-il-server-ufficiale-di-download), con criticità “Alto” (70/100), e lo classifica come attacco alla supply chain software. Lo stesso giorno il vendor lussemburghese ha diffuso un [aggiornamento del proprio avviso](https://kb.nomachine.com/SU11X00295), in cui afferma che l’incidente è stato bonificato e messo in sicurezza.

## La cronologia dell’incidente

* 19 novembre 2026, 13:43 UTC: inizia la finestra in cui il pacchetto alterato è scaricabile;
* 20 novembre 2026, 10:00 UTC: la finestra si chiude;
* 20 novembre 2026: NoMachine pubblica l’[avviso di sicurezza SU11X00294](https://kb.nomachine.com/SU11X00294), aggiornato poi il 23 novembre;
* 24 novembre 2026, 12:16: lo CSIRT Italia pubblica il bollettino BL02/261124;
* 24 novembre 2026: NoMachine pubblica l’aggiornamento SU11X00295, senza indicare l’ora.

## Cosa è stato compromesso

Secondo l’avviso originale di NoMachine, la compromissione è avvenuta a livello del provider di hosting e non per vulnerabilità del codice NoMachine. Il provider non è nominato. Il vendor ha scoperto il pacchetto alterato con un audit di sicurezza, dopo un incidente su uno dei server di download, e ha segnalato il caso all’autorità competente in Lussemburgo.

Il meccanismo tecnico esatto, scrive l’avviso aggiornato il 23 novembre, resta sotto indagine. NoMachine promette altre notizie a indagine conclusa.

L’aggiornamento di oggi circoscrive il perimetro, ma resta una dichiarazione del vendor. Nessun altro prodotto, piattaforma, pacchetto, repository o canale di distribuzione sarebbe stato toccato, e gli aggiornamenti automatici non sarebbero coinvolti. Chi riceve le nuove versioni con l’aggiornamento automatico non sarebbe quindi mai stato esposto al pacchetto alterato.

Il vendor definisce l’episodio il primo di questo tipo in oltre vent’anni e attribuisce ai controlli automatici di integrità la rapidità del rilevamento. Il bollettino riprende le dichiarazioni del vendor, quindi non offre un riscontro indipendente. Entrambe le fonti parlano di “attori malevoli”, senza nominare un responsabile.

## Come si comporta l’installer NoMachine trojanizzato

L’installer NoMachine trojanizzato estrae in
`C:Program FilesNoMachine`
un archivio nascosto e protetto da password,
`gadget.7z`
, con un ambiente Python 3.9 completo. Avvia poi
`pythonw.exe -m zippal`
e
`-m pytorch_rua`
, e crea un’attività pianificata nascosta,
`DefualtAutoUpdateForWindows`
, eseguita ogni minuto.

Il vendor segnala il refuso nel nome; lo CSIRT lo definisce intenzionale. Secondo lo CSIRT compare in alcuni casi anche una seconda attività,
`GoogleCacheClearServices`
.

Il vendor non descrive le funzioni dei moduli. Avverte però che il codice è progettato per nascondersi e reinstallarsi ogni minuto. Invita inoltre a ritenere visibile a terzi tutto ciò che si digita o compare sullo schermo della macchina infetta.

### Gli indicatori pubblicati dal vendor

Gli indicatori pubblicati da NoMachine sono quattro:

* hash MD5 dell’installer malevolo
  `1cea2c6df15a9105faf45ae29ce530bd`
  (quello legittimo è
  `d6d730cea47a3f81faadd89fa775c6f8`
  );
* processo
  `pythonw.exe`
  in esecuzione, visibile in Gestione attività come “Python”;
* cartella
  `C:Program FilesNoMachinepython`
  ;
* traffico verso
  `d137ukgg9ynlmn.cloudfront.net`
  e verso il canale WebSocket
  `wss://...