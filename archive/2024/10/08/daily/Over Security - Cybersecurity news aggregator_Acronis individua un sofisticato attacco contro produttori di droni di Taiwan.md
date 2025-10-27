---
title: Acronis individua un sofisticato attacco contro produttori di droni di Taiwan
url: https://www.securityinfo.it/2024/10/07/acronis-individua-un-sofisticato-attacco-contro-produttori-di-droni-di-taiwan/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-08
fetch_date: 2025-10-06T18:53:19.781955
---

# Acronis individua un sofisticato attacco contro produttori di droni di Taiwan

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

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

## Acronis individua un sofisticato attacco contro produttori di droni di Taiwan

Ott 07, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/07/acronis-individua-un-sofisticato-attacco-contro-produttori-di-droni-di-taiwan/#respond)

---

I ricercatori di Acronis [hanno individuato](https://www.acronis.com/en-us/cyber-protection-center/posts/operation-worddrone-drone-manufacturers-are-being-targeted-in-taiwan/) un **attacco sofisticato che ha colpito i produttori di droni di Taiwan**. Sfruttando una **vulnerabilità di Office 2010**, i cybercriminali sono riusciti a distribuire un malware persistente in grado di eludere gli antivirus e passare quindi inosservato.

![droni Taiwan](https://www.securityinfo.it/wp-content/uploads/2024/10/drone-8261503_1920.jpg)

L’indagine è iniziata dopo che un cliente della compagnia ha segnalato alcuni **comportamenti anomali legati a una vecchia versione di Word**: la soluzione Acronis Advanced Security + XDR segnalava attività sospette legate a questo software, ma non riusciva a determinare quale fosse il documento potenzialmente malevolo.

A insospettire i ricercatori è stato soprattutto il fatto che la soluzione di sicurezza segnalava che **c’era un’altra versione di Word in esecuzione sul dispositivo.** Il team ha scoperto che questa versione risaliva al 2010, soffriva di una vulnerabilità di side-loading e, cosa più importante, veniva usata per ottenere persistenza sul device.

Nella stessa cartella di Word i ricercatori hanno individuato wwlib.dll, parte del pacchetto di installazione standard Office, e un file chiamato “gimaqkwo.iqq”. La libreria veniva usata come un **loader per leggere il payload principale del malware**, cifrato nel secondo file. Durante l’analisi i ricercatori hanno trovato numerose copie dei loader wwlib.dll, molte delle quali era firmate digitalmente con un certificato valido.

“*Ciò significa che non solo gli attaccanti potrebbero aggirare alcune soluzioni di sicurezza che si fidano completamente dei file binari firmati, ma **il malware distribuito potrebbe aver sfruttato il certificato digitale valido in attacchi precedenti, fin dal 2021***” scrivono i ricercatori.

Tra i file individuati è presente anche **install.dll, la libreria che si occupa di installare il malware e specificare il metodo di persistenza** da usare. Nell’attacco analizzato da Acronis, la libreria era configurata per usare il processo host come servizio di persistenza; in seguito, install.dll iniettava lo stage successivo, con al centro la libreria ClientEndPoint.dll.

Questa libreria si occupa di **“silenziare” gli antivirus e i prodotti EDR bloccando i processi a essi collegati.** Secondo i ricercatori, questa funzionalità è stata ottenuta da EDRSilencer, un tool molto popolare. Una volta eliminata la minaccia dei prodotti di sicurezza, la backdoor controlla se il canale col server C2 è abilitato per procedere con la comunicazione.

![](https://www.securityinfo.it/wp-content/uploads/2024/10/security-6901712_1920.jpg)

## Una backdoor sofisticata per l’industria dei droni di Taiwan

La comunicazione Command and Control è pre-configurata in un file di configurazione in un formato binario custom. **La comunicazione non è sempre abilitata**: la configurazione usa un array di bit per rappresentare ogni ora della settimana; se l’ora corrente nell’array è rappresentata con un 1, allora la backdoor può comunicare con il server degli attaccanti. La configurazione specifica anche il protocollo di comunicazione da usare (uno tra TCP, TLS, SMB, HTTP, HTTPS o WebSocket).

La backdoor è in grado di ricevere payload aggiuntivi e comandi; il contenuto del payload finale dipende da un codice specificato dal malware che determina l’azione da svolgere.

Acronis ha scoperto che **la backdoor può utilizzare 59 codici possibili**, ma i ricercatori non sono riusciti a scoprire lo scopo di ciascuno di essi. I più importanti consentono al malware di **raccogliere le informazioni dell’utente e del sistema operativo**, **inviare i dati** ottenuti, eseguire shellcode, **aprire una porta locale** e ascoltarvi le comunicazioni o connettersi a un indirizzo specificato dagli attaccanti. I ricercatori sospettano che la backdoor possa essere usata in modalità proxy, ovvero per inviare e ricevere comandi da altri host compromessi della rete e inviarli al server C2.

Non ci sono ancora indicazioni certe su come gli attaccanti abbiano ottenuto l’accesso iniziale ai dispositivi, anche se le prime tracce del malware sono state trovate nelle cartelle di Digiwin, un popolare software di ERP usato a Taiwan. Gli attacchi, individuati solo nell’ultimo mese, hanno cominciato a verificarsi a partire da aprile di quest’anno.

Secondo i ricercatori di Acronis, gli attaccanti hanno preso di mira l’industria dei droni  di Taiwan per via della sua **notevole crescita** negli ultimi due anni, supportata anche dal governo. Poiché inoltre il Paese è sempre stato un alleato degli Stati Uniti e ha sempre potuto contare su un background tecnologico robusto, è inevitabile che sia diventano **uno degli obiettivi principali delle campagne di spionaggio militare e di attacchi alla supply chain.**

“*Il nostro caso riflette il fatto che gli attaccanti, motivati e sofisticati, stanno passando dal livello aziendale al mercato delle medie imprese e persino alle piccole imprese. **Non sono le dimensioni dell’obiettivo ad attirare la loro attenzione, piuttosto il profilo della vittima prescelta***” spiegano i ricercatori di Acronis. Sebbene la pr...