---
title: STOCKSTAY, la nuova backdoor di Turla che guarda anche alla politica estera italiana
url: https://www.ictsecuritymagazine.com/notizie/stockstay-turla-backdoor-spionaggio/
source: ICT Security Magazine
date: 2026-06-26
fetch_date: 2026-06-27T05:52:16.060414
---

# STOCKSTAY, la nuova backdoor di Turla che guarda anche alla politica estera italiana

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

![STOCKSTAY, la nuova backdoor di Turla che guarda anche alla politica estera italiana](https://www.ictsecuritymagazine.com/wp-content/uploads/STOCKSTAY-la-nuova-backdoor-di-Turla-che-guarda-anche-alla-politica-estera-italiana.png)

# STOCKSTAY, la nuova backdoor di Turla che guarda anche alla politica estera italiana

A cura di:[Redazione](#molongui-disabled-link)  Ore 26 Giugno 202626 Giugno 2026

Google Threat Intelligence Group (GTIG) ha pubblicato [l’analisi di STOCKSTAY](https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering), una *backdoor* modulare in *.NET* sviluppata dal gruppo russo Turla almeno dal dicembre 2022 e impiegata in operazioni dal 2023 per attività di spionaggio contro organizzazioni governative e militari in Ucraina. Il dettaglio che rende la ricerca rilevante per il pubblico italiano è esplicito nel rapporto: tra gli obiettivi figurano anche entità interessate alla politica estera italiana, con campioni di sviluppo individuati in Italia e *lure* in lingua italiana a tema elettorale e affari esteri.

Turla è uno degli attori di *cyber espionage* più longevi e meglio profilati. Opera, secondo l’analisi GTIG, sotto diverse etichette assegnate dai vendor: SUMMIT per Google, *Secret Blizzard* per Microsoft, *Venomous Bear* per CrowdStrike, UAC-0194 per il CERT-UA. La sua infrastruttura storica, l’impianto *Snake*, è stata [attribuita da CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-129a) al Centro 16 dell’FSB, il servizio di sicurezza federale russo. Qui non si parla quindi di ransomware né di estorsione, ma di raccolta informativa di lungo periodo al servizio di un’agenzia statale, una qualifica che cambia il profilo di rischio e il perimetro dei potenziali bersagli.

## Un impianto modulare costruito per restare nascosto

STOCKSTAY non è un singolo eseguibile, ma un ecosistema di componenti che dialogano tra loro tramite messaggi
`WM_COPYDATA`
sul canale di *inter-process communication* di Windows. L’orchestratore (STOCKMARKET, internamente
`cor`
) gestisce configurazione e tasking; un tunnel di rete proxy-aware (STOCKBROKER, internamente
`net`
) isola tutto il traffico di comando e controllo dal resto dell’attività sull’host; un terzo modulo esegue i comandi ricevuti. A monte agisce un *downloader*, MARKETMAKER, che scarica i componenti, stabilisce persistenza tramite chiavi di registro e si maschera da
`MicrosoftUpdateOneDrive`
per apparire legittimo.

La comunicazione con il *server* avviene su *WebSocket* sicuro, appoggiandosi alla libreria open source
`websocket-sharp`
. Al primo avvio l’impianto genera una coppia di chiavi RSA a 4096 bit e un identificativo univoco di infezione, cifrando i dati in uscita prima dell’invio. Il file di configurazione si traveste da applicazione legittima per il monitoraggio dei mercati delle criptovalute, con descrizioni fasulle dei campi e URL di copertura, mentre i dati reali restano cifrati nei campi decoy.

GTIG ha inoltre individuato su GitHub un controller *server-side* in Python (basato su *tornado*) che gestisce l’interfaccia
`/ws`
, spesso ospitato su piattaforme di hosting di terze parti come Render: l’impossibilità per il gestore della piattaforma di decifrare i messaggi in transito offusca la posizione dell’infrastruttura dedicata, un’architettura che ricorda quella multi-hop di KAZUAR.

Le funzioni offerte all’operatore sono quelle classiche dell’accesso remoto: enumerazione e prelievo di file per estensione (con archiviazione ZIP in memoria e *base64* per l’esfiltrazione), cattura schermo, scrittura ed eliminazione di file e directory, esecuzione di comandi multipli. Nelle fasi avanzate, dopo la ricognizione, l’impianto viene configurato con *environmental keying*: gira solo su uno specifico host, utente o dominio, segno che a quel punto l’attaccante sa esattamente quale macchina sta colpendo, tipicamente grazie ad accessi già stabiliti con altri strumenti del gruppo come KAZUAR.

## La sovrapposizione con KAZUAR e il nodo dei nomi cluster

GTIG colloca STOCKSTAY dentro l’arsenale di Turla evidenziando sovrapposizioni di codice e funzionali con KAZUAR, il toolkit [analizzato da Microsoft](https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/) a maggio: introdotto in STOCKSTAY ad aprile 2025, l’obfuscator K1MORPHER è stato poi osservato dal giugno 2025 anche nei campioni di KAZUAR, e GTIG legge l’evoluzione di STOCKSTAY come una tendenza a mimare le tecniche di offuscamento multi-classe di KAZUAR.

La stessa architettura a componenti separati per comunicazione, orchestrazione ed esecuzione richiama lo schema BRIDGE, KERNEL e WORKER già documentato in KAZUAR. Su queste basi GTIG valuta con confidenza moderata che STOCKSTAY e KAZUAR possano condividere, almeno in parte, lo stesso sviluppatore o team, con STOCKSTAY costruito a immagine di KAZUAR; l’attribuzione complessiva a Turla resta invece a confidenza alta.

È un buon promemoria operativo sul fronte attribuzione: i nomi dei cluster vanno sempre incrociati tra vendor, perché la stessa famiglia compare con etichette diverse, e ricostruire la genealogia di un *toolkit* i...