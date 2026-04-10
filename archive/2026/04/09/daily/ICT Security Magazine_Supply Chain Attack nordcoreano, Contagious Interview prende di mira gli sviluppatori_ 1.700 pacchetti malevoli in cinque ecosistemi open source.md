---
title: Supply Chain Attack nordcoreano, Contagious Interview prende di mira gli sviluppatori: 1.700 pacchetti malevoli in cinque ecosistemi open source
url: https://www.ictsecuritymagazine.com/notizie/supply-chain-attack-nordcorea/
source: ICT Security Magazine
date: 2026-04-09
fetch_date: 2026-04-10T04:47:38.827110
---

# Supply Chain Attack nordcoreano, Contagious Interview prende di mira gli sviluppatori: 1.700 pacchetti malevoli in cinque ecosistemi open source

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

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![Supply Chain Attack nordcoreano prende di mira gli sviluppatori: 1.700 pacchetti malevoli in cinque ecosistemi open source. la Corea del Nord distribuisce 1.700 pacchetti malevoli su npm, PyPI, Go, Rust e Packagist](https://www.ictsecuritymagazine.com/wp-content/uploads/Supply-Chain-Attack-nordcoreano-Contagious-Interview-prende-di-mira-gli-sviluppatori.jpeg)

# Supply Chain Attack nordcoreano, Contagious Interview prende di mira gli sviluppatori: 1.700 pacchetti malevoli in cinque ecosistemi open source

A cura di:[Redazione](#molongui-disabled-link)  Ore 9 Aprile 20269 Aprile 2026

Un’operazione di supply chain attack attribuita a gruppi hacker nordcoreani ha raggiunto una scala senza precedenti: oltre 1.700 pacchetti malevoli distribuiti contemporaneamente su cinque dei principali registri open source globali, progettati per colpire sviluppatori software in tutto il mondo attraverso strumenti di uso quotidiano. La campagna, denominata Contagious Interview e monitorata dai ricercatori di Socket Security dal 2024, ha compiuto il 7 aprile 2026 un salto qualitativo significativo: per la prima volta, la stessa infrastruttura di staging e gli stessi pattern di distribuzione sono stati replicati in parallelo su npm, PyPI, Go Modules, crates.io e Packagist.

## Supply Chain Attack nordcoreano: una fabbrica di pacchetti malevoli a scala industriale

[Socket ha documentato](https://socket.dev/blog/contagious-interview-campaign-spreads-across-5-ecosystems) che il cluster individuato in questa tornata comprende dodici pacchetti malevoli confermati e due pacchetti “dormienti”, caricati sotto alias GitHub tra cui golangorg, aokisasakidev e aokisasakidev1, con una rete di supporto operante sotto i profili maxcointech1010 e maxcointech0000.

L’elenco completo dei pacchetti identificati per ecosistema, secondo il report del ricercatore Kirill Boychenko di Socket, è il seguente: su npm i pacchetti dev-log-core, logger-base, logkitx, pino-debugger, debug-fmt e debug-glitz; su PyPI i pacchetti logutilkit, apachelicense, fluxhttp e license-utils-kit; nel registro Go i moduli github.com/golangorg/formstash e github.com/aokisasakidev/mit-license-pkg; nel registro Rust il pacchetto logtrace; nel registro PHP Packagist il pacchetto golangorg/logkit.

La scelta dei nomi non è casuale: i pacchetti erano progettati per impersonare strumenti di sviluppo legittimi come debug, debug-logfmt, pino-debug, baraka, license, http, libprettylogger e openlss/func-log, funzionando silenziosamente come malware loader. Questo schema è perfettamente coerente con quanto già documentato da [ICT Security Magazine nell’analisi sulla supply chain software e i 454.000 pacchetti malevoli del 2025](https://www.ictsecuritymagazine.com/articoli/supply-chain-software/): la fiducia implicita nei registri pubblici è diventata l’arma più efficiente a disposizione degli attaccanti statali.

#### Il meccanismo di infezione: loader a due stadi invisibili al momento dell’installazione

[Il malware nascosto è progettato in modo da non eseguirsi durante l’installazione del pacchetto](https://vulert.com/blog/north-korea-malicious-packages-npm-pypi-go-rust/), rendendo più difficile il rilevamento da parte degli strumenti di sicurezza tradizionali.

I loader recuperano un downloadUrl dall’infrastruttura controllata dagli attaccanti (in particolare dall’endpoint apachelicense[.]vercel[.]app), riscrivono i link di condivisione di Google Drive in formato di download diretto, [scaricano archivi ZIP come ecw\_update.zip e consegnano payload di secondo stadio specifici per piattaforma](https://securityonline.info/contagious-interview-north-korea-malicious-packages-dev-registries/). Questi payload si rivelano essere malware con capacità di infostealer e remote access trojan (RAT), in grado di sottrarre credenziali, portafogli di criptovalute e garantire accesso persistente ai sistemi compromessi.

Il [coordinamento cross-ecosistema](https://anonhaven.com/en/news/contagious-interview-cross-ecosystem-supply-chain-attack/) è l’elemento più significativo: lo stesso cluster ha pubblicato i pacchetti su cinque registri diversi riutilizzando la stessa logica di staging, la stessa infrastruttura e gli stessi pattern di riuso delle persona. Questo indica che gli attaccanti possono continuare a portare lo stesso design di loader in nuovi registri con sole modifiche minori al codice.

#### Chi c’è dietro Contagious Interview: UNC1069, BlueNoroff e il link con Axios

[L’attacco è attribuito a un threat actor a motivazione finanziaria noto come UNC1069, che si sovrappone ai gruppi BlueNoroff, Sapphire Sleet e Stardust Chollima](https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html). La Security Alliance (SEAL) ha dichiarato di aver bloccato 164 domini collegati a UNC1069 che impersonavano servizi come Microsoft Teams e Zoom tra il 6 febbraio e il 7 aprile 2026.

UNC1069 opera campagne di social engineering a bassa pressione e multi-settimana su Telegram, LinkedIn e Slack, impersonando contatti noti o brand credibili, o sfruttando accessi ad account aziendali e personali precedentemente compromessi, prima di consegnare un link fraudolento a una riunione Zoom o Microsoft Teams, utilizzato per veicolare lure di tipo Cl...