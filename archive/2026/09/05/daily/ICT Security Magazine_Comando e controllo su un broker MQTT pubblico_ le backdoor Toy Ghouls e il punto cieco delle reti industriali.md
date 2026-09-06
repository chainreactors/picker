---
title: Comando e controllo su un broker MQTT pubblico: le backdoor Toy Ghouls e il punto cieco delle reti industriali
url: https://www.ictsecuritymagazine.com/notizie/mqtt-matrix-command-control-backdoor-toy-ghouls/
source: ICT Security Magazine
date: 2026-09-05
fetch_date: 2026-09-06T06:40:09.697639
---

# Comando e controllo su un broker MQTT pubblico: le backdoor Toy Ghouls e il punto cieco delle reti industriali

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

![Comando e controllo su un broker MQTT pubblico le backdoor Toy Ghouls e il punto cieco delle reti industriali](https://www.ictsecuritymagazine.com/wp-content/uploads/Comando-e-controllo-su-un-broker-MQTT-pubblico-le-backdoor-Toy-Ghouls-e-il-punto-cieco-delle-reti-industriali.png)

# Comando e controllo su un broker MQTT pubblico: le backdoor Toy Ghouls e il punto cieco delle reti industriali

A cura di:[Redazione](#molongui-disabled-link)  Ore 5 Settembre 2026

*Due impianti Windows analizzati da Kaspersky non usano infrastruttura propria per il comando e controllo: uno si appoggia al broker MQTT pubblico di HiveMQ, l’altro al protocollo Matrix. Le vittime documentate sono russe e non si tratta di un attacco a sistemi industriali, ma la tecnica solleva un problema di rilevamento che riguarda direttamente chi gestisce reti OT.*

## Due backdoor, nessuna infrastruttura propria

Il 4 settembre 2026 Kaspersky ha pubblicato su Securelist l’[analisi di due backdoor](https://securelist.com/toy-ghouls-new-hivemq-and-element-backdoors/121270/) che i suoi ricercatori attribuiscono al gruppo a movente finanziario noto come Toy Ghouls, indicato anche con i nomi Bearlyfy, Laboo.boo e Feral Wolf. L’attribuzione è dei team GERT e Security Services di Kaspersky e va riportata come tale.

Il gruppo è attivo dal 2025 contro organizzazioni russe. Ha iniziato appoggiandosi a strumenti disponibili pubblicamente e a *builder* di ransomware trapelati, quelli di Babuk e LockBit, per poi sviluppare codice proprio, tra cui il ransomware [GenieLocker](https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/), in versioni per Windows, Linux ed ESXi.

I due impianti individuati all’inizio di luglio 2026 si chiamano mqtt-bird-agent 0.1.0 e matrix-bird-agent 0.1.0, e corrispondono a due eseguibili Windows,
`cplsupport.exe`
e
`wtass.exe`
. Il tratto che li rende interessanti è che nessuno dei due porta con sé un server di comando e controllo: entrambi si appoggiano a servizi e protocolli legittimi.

Un secondo elemento merita attenzione, e riguarda il modo in cui arrivano sulla macchina. La distribuzione avviene attraverso Windows Remote Management, con utilità di post-sfruttamento *open source* come Evil-WinRM e WinRM-fs. Il report non descrive il vettore di accesso iniziale, ma la scelta di WinRM implica che gli operatori dispongono già di credenziali amministrative quando installano l’impianto: la backdoor non è il punto di ingresso, è ciò che rende l’accesso persistente.

La persistenza si ottiene registrandosi come servizio Windows, con i nomi “cplsupport” (descritto come “Problem Reports Control Panel”) e “wtas” (“Windows Telemetry Aggregator Service”), tramite argomenti di installazione e disinstallazione. In entrambe le varianti i campi sensibili della configurazione vengono cifrati al primo avvio con ChaCha20-Poly1305, con una chiave derivata dal valore MachineGuid del registro di sistema: un accorgimento che impedisce di riutilizzare la configurazione su un’altra macchina e complica il lavoro di chi analizza il campione fuori dall’ambiente di origine. La variante MQTT conserva il file cifrato su disco; la variante Matrix lo cancella dopo il primo avvio e sposta i parametri in una chiave di registro dedicata.

## Perché un broker MQTT pubblico è un canale quasi ideale

Secondo Kaspersky, la variante mqtt-bird-agent comunica con
`broker.hivemq.com`
sulla porta 8883, quella standard di MQTT su TLS. Il dominio è quello del broker pubblico di HiveMQ, [uno dei più noti](https://www.emqx.com/en/blog/popular-online-public-mqtt-brokers) tra quelli messi a disposizione gratuitamente per test e prototipazione: non è un server compromesso né un dominio registrato dagli attaccanti. Il report descrive quattro percorsi di scambio: uno per lo stato del sistema infetto, uno per le metriche periodiche (CPU, memoria, disco, carico, tempo di attività), uno da cui la backdoor legge i comandi e uno su cui restituisce i risultati. I comandi vengono eseguiti tramite PowerShell in modalità nascosta.

Un’annotazione di precisione: nello stesso passaggio Securelist parla di un “cluster” creato dagli attaccanti e di un piano gratuito con limiti di 100 connessioni concorrenti e 10 GB di traffico mensili. Sono esattamente le caratteristiche del [piano Serverless gratuito di HiveMQ Cloud](https://docs.hivemq.com/hivemq-cloud/quick-start-guide.html), che prevede credenziali di accesso e TLS, non quelle del broker demo aperto, che non ha né cluster né piani. Il report non scioglie l’ambiguità. La conseguenza pratica è che non si può dare per certo che il canale fosse privo di autenticazione, e che l’indirizzo effettivamente contattato potrebbe essere un sottodominio dedicato del servizio cloud piuttosto che il nome generico del broker pubblico: in entrambi i casi, comunque, la destinazione appartiene a un fornitore legittimo e ampiamente usato.

Vale la pena spiegare perché questa scelta sia efficace, al di là della gratuità.

MQTT è un protocollo *publish and subscribe*: il client non riceve connessioni in ingresso, si limita a stabilire una connessione uscente verso il broker e ad attendere. Non serve alcuna porta aperta s...