---
title: Nuovo attacco alla supply chain: i cybercriminali impersonano i team IT per colpire Salesforce
url: https://www.insicurezzadigitale.com/nuovo-attacco-alla-supply-chain-i-cybercriminali-impersonano-i-team-it-per-colpire-salesforce/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-06
fetch_date: 2025-10-06T22:56:11.875382
---

# Nuovo attacco alla supply chain: i cybercriminali impersonano i team IT per colpire Salesforce

[(in)sicurezza digitale](https://insicurezzadigitale.com/)

* Incidenti e violazioni
  + [Roundup – Flash](https://insicurezzadigitale.com/category/roundup/)
  + [Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)
  + [Phishing](https://insicurezzadigitale.com/category/phishing/)
  + [Privacy](https://insicurezzadigitale.com/category/privacy/)
  + [Data Breach](https://insicurezzadigitale.com/category/data-breach/)
* [Ransomware](https://insicurezzadigitale.com/category/ransomware/)
* [Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)
  + [Analisi](https://insicurezzadigitale.com/category/analisi/)
* [La stampa dice](https://insicurezzadigitale.com/la-stampa-dice/)
* Altro…
  + [Chi siamo](https://insicurezzadigitale.com/chi-siamo/)
  + [> Whistleblowing <](https://insicurezzadigitale.com/whistleblowing/)
  + [Eventi](https://insicurezzadigitale.com/category/eventi/)
  + [Editoriali di Dario Fadda](https://blogsicurezza.myblog.it/)
  + [Data Leaks list](https://insicurezzadigitale.com/data-leaks-list/)
  + [Archivio Cyber Security Notes](https://insicurezzadigitale.com/archivio-cyber-security-notes/)
  + [Archivio Malware samples](https://insicurezzadigitale.com/archivio-malware-samples/)
  + [Infosec Tools list](/tool)
* Il Network
  + [NINAsec – Newsletter](https://ninasec.substack.com/)
  + [Spcnet.it](https://www.spcnet.it)
  + [Ziobudda](https://www.ziobudda.org)
  + [ilGlobale.it](https://www.ilglobale.it)
  + [SecureBulletin.com](https://securebulletin.com/)
* [I Forums](https://forum.ransomfeed.it/)

[Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)

# Nuovo attacco alla supply chain: i cybercriminali impersonano i team IT per colpire Salesforce

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
5 Giugno 2025

![](https://insicurezzadigitale.com/wp-content/uploads/2025/06/salesforce-vishing-fig1.max-1700x1700-1-1024x665.png)

Si parla di:

Toggle

* [Il modus operandi: vishing e app malevole](#Il_modus_operandi_vishing_e_app_malevole)
* [Dalla compromissione all’estorsione](#Dalla_compromissione_allestorsione)
* [Implicazioni tecniche e raccomandazioni](#Implicazioni_tecniche_e_raccomandazioni)

Appare in ambito frodi mirate un focus particolare sulle piattaforme cloud business-critical come Salesforce. Un recente allarme lanciato dal Google Threat Intelligence Group (GTIG) mette in luce una [campagna](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion) sofisticata condotta dal gruppo UNC6040, che sfrutta il voice phishing (vishing) e applicazioni malevole per esfiltrare dati sensibili dalle istanze Salesforce delle aziende.

## Il modus operandi: vishing e app malevole

Il gruppo UNC6040, motivato da finalità finanziarie, si distingue per la sua capacità di impersonare il personale IT aziendale tramite telefonate di vishing estremamente convincenti. Durante queste chiamate, gli attaccanti persuadono i dipendenti a scaricare e utilizzare una versione modificata e malevola del Salesforce Data Loader, uno strumento legittimo utilizzato per la gestione massiva dei dati sulla piattaforma.

Questa versione compromessa del Data Loader, pubblicata spesso con nomi e branding alterati, consente agli attaccanti di ottenere accesso diretto alle istanze Salesforce delle vittime. Una volta installata, l’app malevola permette di interrogare e trasferire dati sensibili verso server controllati dagli attaccanti, senza la necessità di sfruttare vulnerabilità tecniche della piattaforma stessa. L’intera operazione si basa sulla manipolazione psicologica degli utenti finali, sottolineando ancora una volta la centralità del fattore umano nella catena della sicurezza.

## Dalla compromissione all’estorsione

Un aspetto particolarmente insidioso di queste campagne è la tempistica: spesso tra la compromissione iniziale e le attività di estorsione passano diversi mesi. Questo suggerisce una possibile collaborazione tra UNC6040 e altri attori specializzati nella monetizzazione dei dati rubati. Durante le fasi di estorsione, gli attaccanti hanno rivendicato affiliazioni con gruppi noti come ShinyHunters, probabilmente per aumentare la pressione psicologica sulle vittime.

Secondo le stime di Google, circa 20 organizzazioni sono state colpite, con una parte di esse che ha subito effettivamente la sottrazione di dati. Salesforce aveva già segnalato la minaccia di applicazioni connesse malevole a marzo, fornendo linee guida e best practice per mitigare il rischio.

## Implicazioni tecniche e raccomandazioni

È fondamentale sottolineare che in tutti i casi osservati, gli attaccanti non hanno sfruttato vulnerabilità tecniche di Salesforce, ma esclusivamente debolezze nei processi e nella consapevolezza degli utenti. Questo conferma che le campagne di phishing, in particolare quelle che sfruttano tematiche IT o HR, restano il vettore d’attacco più efficace e diffuso.

Per rafforzare la postura di sicurezza delle istanze Salesforce, le seguenti misure sono raccomandate:

* **Abilitare l’autenticazione a più fattori (MFA)** per tutti gli utenti.
* **Limitare gli indirizzi IP di accesso** alle reti aziendali e VPN.
* **Monitorare e validare tutte le applicazioni connesse** alla piattaforma Salesforce.
* **Aggiungere un contatto di sicurezza** per ricevere notifiche tempestive su attività sospette.
* **Formazione continua degli utenti** sulle tecniche di social engineering più recenti, con simulazioni di phishing mirate.

L’attacco UNC6040 si identifica come un caso emblematico di sicurezza delle piattaforme SaaS, che non può prescindere da una solida cultura della sicurezza e da controlli procedurali rigorosi. In un contesto in cui il phishing continua a rappresentare la principale minaccia cyber (con oltre 3,4 miliardi di email di spam inviate ogni giorno), investire nella formazione degli utenti e nell’adozione di best practice tecniche è l’unica strada per ridurre il rischio di compromissione.

**La sicurezza non è mai solo una questione tecnologica, ma un equilibrio tra tecnologia, processi e persone.**

##### < tags />

[cybercrime](https://insicurezzadigitale.com/tag/cybercrime/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[salesforce](https://insicurezzadigitale.com/tag/salesforce/)[vishing](https://insicurezzadigitale.com/tag/vishing/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Nuovo+attacco+alla+supply+chain%3A+i+cybercriminali+impersonano+i+team+IT+per+colpire+Salesforce&url=https://insicurezzadigitale.com/nuovo-attacco-alla-supply-chain-i-cybercriminali-impersonano-i-team-it-per-colpire-salesforce/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/nuovo-attacco-alla-supply-chain-i-cybercriminali-impersonano-i-team-it-per-colpire-salesforce/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/nuovo-attacco-alla-supply-chain-i-cybercriminali-impersonano-i-team-it-per-colpire-salesforce/&title=Nuovo+attacco+alla+supply+chain%3A+i+cybercriminali+impersonano+i+team+IT+per+colpire+Salesforce)

[== articolo precedente ==](https://insicurezzadigitale.com/cyberwarfare-tra-cina-e-taiwan-nuove-frontiere-della-tensione-geopolitica/)

[:: articolo successivo ::](https://insicurezzadigitale.com/6-6-digest-roundup-le-notizie-piu-rilevanti-delle-ultime-24-ore/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/nuovo-attacco-alla-supply-chain-i-cybercriminali-impersonano-i-team-it-per-colpire-salesforce/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Nuovo attacco alla supply chain: i cybercriminali impersonano i team IT per colpire Salesforce*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Nuovo+attacco+alla+supply+chain:).
Condividi esempi, IOCs o tecniche di de...