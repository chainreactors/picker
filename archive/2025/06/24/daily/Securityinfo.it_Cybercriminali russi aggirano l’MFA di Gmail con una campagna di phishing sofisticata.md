---
title: Cybercriminali russi aggirano l’MFA di Gmail con una campagna di phishing sofisticata
url: https://www.securityinfo.it/2025/06/23/cybercriminali-russi-aggirano-l-mfa-di-gmail-con-una-campagna-di-phishing-sofisticata/?utm_source=rss&utm_medium=rss&utm_campaign=cybercriminali-russi-aggirano-l-mfa-di-gmail-con-una-campagna-di-phishing-sofisticata
source: Securityinfo.it
date: 2025-06-24
fetch_date: 2025-10-06T22:55:30.463753
---

# Cybercriminali russi aggirano l’MFA di Gmail con una campagna di phishing sofisticata

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## Cybercriminali russi aggirano l’MFA di Gmail con una campagna di phishing sofisticata

Giu 23, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/06/23/cybercriminali-russi-aggirano-l-mfa-di-gmail-con-una-campagna-di-phishing-sofisticata/#respond)

---

Il team del Google Threat Intelligence ha pubblicato una [nuova analisi](https://cloud.google.com/blog/topics/threat-intelligence/creative-phishing-academics-critics-of-russia) in cui descrive una nuova **campagna di phishing** che consente agli attaccanti di **aggirare l’MFA di Gmail** grazie alle **Application Specific Password** (ASP).

Le ASP sono passcode di 16 cifre che consentono a un’applicazione o a un dispositivo meno sicuri di accedere a un Account Google con attiva l’autenticazione multi-fattore. Da documentazione Google sconsiglia l’utilizzo delle ASP.

![MFA Gmail](https://www.securityinfo.it/wp-content/uploads/2025/06/hacker-1952027_1920.jpg)

La campagna del gruppo si basa sul convincere la vittima a **creare e condividere uno screenshot di una ASP** per permettere agli attaccanti di accedere all’account senza dover gestire l’MFA. Come riportato anche da [The Citizen Lab](https://www.securityinfo.it/2025/06/18/due-bug-lpe-consentono-di-ottenere-i-privilegi-di-root-su-linux/), la prima notifica dell’attacco è arrivata da Keir Giles, un noto ricercatore inglese attivo nel controspionaggio contro la Russia.

Il 22 maggio Giles ha ricevuto un’email in cui il mittente era una certa “Claudie S. Weber” del Dipartimento di Stato statunitense. Nel messaggio Weber invitava Giles a un meeting con lei e alcuni suoi colleghi per parlare di alcuni “recenti sviluppi”, senza specificare di cosa si trattasse. **Alcuni degli indirizzi email in CC terminavano con @state.gov**, un trucco degli attaccanti per far apparire la comunicazione legittima.

Giles ha voluto approfondire la questione e ha risposto alla mail; tale Weber allora ha inviato un PDF con le istruzioni per registrare un account guest per conversare coi membri del Dipartimento dello Stato. Il PDF, che a una prima occhiata sembra legittimo, richiede alle vittime di **navigare su un link Google per creare una ASP**; in seguito, gli attaccanti chiedono all’utente di condividere con loro il codice di 16 cifre generato, apparentemente per consentirgli di accedere alla piattaforma del Dipartimento.

Il codice viene invece utilizzato dal gruppo per prendere il controllo dell’account Google della vittima, riuscendo di conseguenza ad accedere a tutte le email scambiate. Gli attaccanti hanno utilizzato per lo più proxy residenziali e server VPS per accedere agli account.

## L’attacco a Gmail che supera l’MFA: la risposta di Google

Secondo il Google Threat Intelligence Group, dietro gli attacchi ci sarebbe **UNC6293**, un gruppo di cybercriminali che opera per conto del governo russo. Il team di sicurezza ritiene che il gruppo possa essere legato ad **APT29**, un’altra gang russa nota per aver distribuito la backdoor **WINELOADER,** anche se non ci sono indicazioni certe di una qualche relazione.

![](https://www.securityinfo.it/wp-content/uploads/2025/04/13311414_v627-aew-41-technologybackground-scaled.jpg)

I ricercatori di The Citizen Lab sottolineano che **l’attacco è altamente sofisticato** e che richiede una preparazione molto attenta: il gruppo ha creato numerosi account falsi per far apparire le comunicazioni come legittime e hanno posto molta attenzione al tono dei messaggi scambiati, senza mai far nascere il senso di urgenza nella vittima.

“***L’interazione si è svolta in più di 10 scambi nel corso di diverse settimane**, dimostrando una notevole pazienza da parte degli attaccanti*” spiegano i ricercatori.  “*Gli autori dell’attacco erano anche pronti con le risposte e preparati ad adattarsi in base alle repliche di Giles. Ad esempio, dopo che Giles ha affermato che non sarebbe riuscito a partecipare al meeting nella data proposta, gli autori dell’attacco hanno scelto di non esercitare pressioni o urgenza in modo esplicito, suggerendo invece di creare la piattaforma per il futuro*“.

Il gruppo è effettivamente riuscito a convincere Giles a creare e condividere l’ASP, anche su diversi account. Google ha in seguito **identificato l’attacco e ha disabilitato le email degli attaccanti**, oltre che gli account compromessi. In un post su X, Giles ha confermato che c’è stato un login sospetto al suo account e ha quindi avvertito i suoi contatti di trattare con la massima attenzione eventuali comunicazioni o allegati inviati da uno dei suoi indirizzi email.

Oltre a quella che ha colpito Giles, Google ha individuato anche un’altra campagna analoga del gruppo che sfruttava invece figure legate al governo ucraino.

Visto il livello di sofisticazione della campagna e le personalità centrali prese di mira dagli attaccanti, la compagnia di Mountain View consiglia agli utenti a rischio di **aderire al suo Advanced Protection Program** volto a tutelare gli account che hanno elevata visibilità e gestiscono informazioni sensibili. Il programma, tra le altre cose, comprende il blocco della creazione di ASP.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [ASP](https://www.securityinfo.it/tag/asp/), [Google](https://www.securityinfo.it/tag/google/), [hacker russi](https://www.securityinfo.it/tag/hacker-russi/), [MFA](https://www.securityinfo.it/tag/mfa/), [passcode](https://www.securityinfo.it/tag/passcode/), [Phishing](https://www....