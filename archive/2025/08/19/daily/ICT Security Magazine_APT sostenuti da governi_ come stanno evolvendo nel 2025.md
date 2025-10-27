---
title: APT sostenuti da governi: come stanno evolvendo nel 2025
url: https://www.ictsecuritymagazine.com/notizie/apt-governi-nel-2025/
source: ICT Security Magazine
date: 2025-08-19
fetch_date: 2025-10-07T00:48:55.691904
---

# APT sostenuti da governi: come stanno evolvendo nel 2025

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

![APT](https://www.ictsecuritymagazine.com/wp-content/uploads/apt-governi.jpeg)

# APT sostenuti da governi: come stanno evolvendo nel 2025

A cura di:[Redazione](#molongui-disabled-link)  Ore 18 Agosto 202524 Luglio 2025

Negli ultimi anni gli attacchi informatici sponsorizzati da governi ([Advanced Persistent Threat, APT](https://www.ictsecuritymagazine.com/articoli/threat-actor-intelligence/)) sono cresciuti in numero e sofisticazione. Secondo la **Relazione Annuale** italiana 2025, nel 2024 circa il **50%** degli attacchi subiti in Italia era riconducibile ad APT stranieri, con un focus spinto su infrastrutture pubbliche centrali, reti digitali, trasporti, energia e telecomunicazioni. Questi gruppi “living off the land” mettono in campo tool avanzati, reti di comando resiliente e malware modulare per prolungare la loro persistenza nelle reti di governo e aziende strategiche.

## Nuove tecniche e vettori d’attacco

* **Abuso di strumenti legittimi (“living off the land”)**: gli APT sempre più sfruttano software benigni già presenti nelle reti vittime (script Office, PowerShell, RMM, browser) per nascondere le proprie attività. Questo riduce il traffico malevolo visibile e complica l’attribuzione.
* **Malware e backdoor avanzati**: i gruppi statali sviluppano costantemente nuovi payload. Ad esempio APT41 ha introdotto tool multi-stage come *DUSTPAN* e *DUSTTRAP*, che agiscono in memoria per limitare tracce forensi. Similmente, nuovi malware .NET o Go (es. i RAT creduti infallibili) vengono progettati con payload encrypted e moduli plug-in.
* **Phishing evoluto e AI**: i messaggi di spear-phishing sono ora potenziati da intelligenza artificiale, che genera contenuti di social engineering altamente personalizzati e deepfake per ingannare le vittime. L’AI viene usata anche per automatizzare la ricerca di vulnerabilità (“bug-hunting”) e per gestire payload in fase di post-exploit.
* **Supply chain compromesse**: le campagne APT sfruttano catene di fornitura per infettare vittime secondarie. Un caso recente vede il gruppo Lazarus (Corea del Nord) che ha usato tecniche di *watering hole* e zero-day in software di terze parti (uno strumento bancario coreano, Innorix Agent) per diffondere backdoor. Anche in Ucraina i russi di Sandworm hanno lanciato un attacco supply-chain: nuove backdoor (Kapeka su Windows e Biasboat su Linux) sono state installate attraverso software ICS legittimo compromesso.
* **Ransomware “doppio scopo”**: un’evoluzione preoccupante è l’uso del ransomware da parte di stati per spionaggio e sabotaggio oltre all’estorsione. La Relazione italiana osserva che ora i ransomware vengono impiegati da attori statali anche per disturbo e “false flag”, con l’effetto collaterale di danneggiare infrastrutture critiche e confondere gli investigatori.

## Cambiamenti nelle infrastrutture di comando e controllo (C2)

* **Reti di “relay” coperte**: gli APT organizzano complesse reti di proxy compromessi (VPN, VPS, router IoT, NAS) per instradare il traffico malevolo e mascherarne l’origine. Queste “Covert Relay Network” rendono più difficoltoso il tracciamento. Ad esempio, un Paese può impiegare centinaia di server in giro per il mondo per i propri scopi di spionaggio cyber.
* **Uso di servizi cloud e file-sharing legittimi**: sempre più attacchi sfruttano infrastrutture online di massa come canali C2 o drop-off server. Gruppi APT hanno utilizzato cloud pubblici (OneDrive, MEGA, Supabase, Backendless, API di koofr.com) per ricevere comandi o esfiltrare dati. In un caso recente, APT28 ha occultato uno shellcode in un’immagine PNG e lo ha caricato via API di cloud storage per eseguire il malware *Covenant*.
* **Abuso di piattaforme di comunicazione e software legittimi**: alcuni gruppi veicolano i payload attraverso piattaforme di chat e collaborazione per eludere i filtri. Per esempio, Transparent Tribe (Pakistan) ha usato Discord, Google Drive, Slack e Telegram per distribuire archivi infetti. Allo stesso modo, attacchi recenti (MuddyWater, Iran) hanno usato pacchetti di Remote Monitoring Management (RMM) legittimi (Atera Agent, Tactical RMM) registrati con account compromessi e diffusi via phishing. Anche il protocollo WebDAV (Nextcloud/Mega) è stato impiegato come canale di esfiltrazione. Queste tattiche dimostrano che gli APT integrano infrastrutture “normali” per mantenere nascosti i loro C2.

## Gruppi APT attivi e campagne recenti

* **APT28 (“Fancy Bear”, Russia)** – Gruppo del GRU russo, noto per spionaggio politico e militare. Recentemente ha lanciato campagne mirate contro agenzie ucraine: via messaggi **Signal** gli operatori hanno inviato un documento Word infetto che carica in memoria il framework *Covenant* (loader) e il backdoor *BeardShell*. BeardShell (scritta in C++) può eseguire script PowerShell e caricare dati tramite l’API Icedrive. Queste tecniche confermano il trend “living off the land”: gli attaccanti usano applicazioni e servizi familiari (Signal, cloud storage) per eseguire malware senza destare sospetti. Da segnalare anche l’uso della vulnerabilità CVE-2022-38028 (print spooler) da parte di varianti Fancy Bear, sfruttata con il tool GooseEgg per rubare credenziali.
* **Lazarus Group (Nord Corea)** – APT legato ai servizi segreti nordcoreani, attivo dal 2009. Nel...