---
title: EvolvedAim: infostealer nascosto nel cheat per Escape From Tarkov
url: https://www.securityinfo.it/2024/07/26/evolvedaim-infostealer-nascosto-nel-cheat-per-escape-from-tarkov/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-27
fetch_date: 2025-10-06T17:44:13.766493
---

# EvolvedAim: infostealer nascosto nel cheat per Escape From Tarkov

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

## EvolvedAim: infostealer nascosto nel cheat per Escape From Tarkov

Lug 26, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/07/26/evolvedaim-infostealer-nascosto-nel-cheat-per-escape-from-tarkov/#respond)

---

Tanti videogiocatori si affidano ai cheat per avere più possibilità di vincere nei videogiochi, trucchi che gli consentono di ottenere benefici che il titolo normalmente non offre. Utilizzare i cheat non è soltanto scorretto nei confronti degli altri videogiocatori, ma può essere anche pericoloso: è il caso del popolare **EvolvedAim**, un **cheat per Escape From Tarkov che conteneva un infostealer.**

Il videogioco è un noto simulatore militare realistico che **conta 14,76 milioni di giocatori** e centinaia di cheat in vendita. Tra questi, EvolvedAim ha guadagnato popolarità perché offre numerose funzionalità, come il trading automatico nella casa d’aste del gioco e l’addestramento automatico per sviluppare abilità specifiche.

![EvolvedAim](https://www.securityinfo.it/wp-content/uploads/2024/07/pexels-yankrukov-9072292.jpg)

Pixabay

**David El**, malware researcher di [CyberArk Labs](https://labs.cyberark.com/), spiega che il malware nei cheat non è raro, ma **in questo caso l’impatto potenziale è elevato**: Escape From Tarkov è molto popolare tra i giovani adulti (dai 25 anni in su), così come il trucco che prevede un modello in abbonamento, studiato per colpire utenti adulti. **Le informazioni sottratte possono essere usate per far leva e ottenere accesso ai dati personali degli utenti.**

Più di un anno fa **Mythical**, il **principale sviluppatore di EvolvedAim**, ha contattato EDP, proprietario di uno dei più grandi forum di cheat e bot per il videogioco, per proporgli di mettere in vendita il suo strumento, condividendo una parte dei profitti. Nel corso dell’ultimo anno entrambe le parti hanno generato un buon flusso di entrate e **il cheat è diventato famoso anche al di fuori del forum**, tanto che Mythical ha iniziato a metterlo in vendita sul proprio sito.

È a questo punto che sono iniziati i problemi: Mythical, raggiunta la notorietà col suo cheat, voleva ridurre la quota di profitti di EDP pur continuando a rivendere EvolvedAim sul suo forum; nel frattempo, **il proprietario del forum ha iniziato a notare diversi tentativi di accesso ai suoi account** e la comparsa di screenshot del suo desktop.

## Come agisce EvolvedAim

El spiega che il cheat è scritto in Python 3.10 e viene convertito in eseguibile usando la libreria PyInstaller. Quando si esegue EvolvedAim, viene mostrata una casella di input che richiede di inserire una chiave di licenza. Il danno ormai è fatto: **l’infostealer ha già raccolto le informazioni**, in quanto il codice malevolo viene eseguito in un thread separato da quello principale del cheat.

Nel dettaglio, il software esegue **quattro thread**: due sono benigni, usati per l’effettiva funzionalità del cheat, mentre gli altri sono dannosi e vengono eseguiti con nomi non sospetti come discord\_to\_bot e run\_antivm.

I quattro thread vengono eseguiti simultaneamente: **run\_antivm appare come un  rilevamento anti-virtual machine ma, in realtà, esegue la logica dannosa**. Questo thread controlla inizialmente il nome del PC e, se corrisponde a uno dei due nomi inseriti nella black list, non procede con il furto di informazioni. I nomi inseriti nella black list sono quelli dei due sviluppatori del cheat.

A seguire viene eseguita la logica per la raccolta e l’esfiltrazione delle informazioni, le quali comprendono le **password e i valori dei cookie dai principali browser**, compresi Chrome, Firefox e Opera, ma anche Tor, Torch e Vivaldi. Vengono inoltre raccolti e caricati tutti i file memorizzati dall’estensione del popolare portafoglio di criptovalute MetaMask, oltre ai file sensibili di Discord e Steam, l’elenco di file dalle cartelle Documenti e Download, e viene scattato uno screenshot al desktop.

![furto di informazioni](https://www.securityinfo.it/wp-content/uploads/2024/07/business-5475656_1920.jpg)

Pixabay

I dati raccolti vengono archiviati temporaneamente in una cartella e compressi in un archivio .zip col nome del PC colpito; l’archivio viene in seguito caricato su Mega.nz. A questo punto**, l’infostealer usa un webhook di Discord per notificare l’attaccante sul server.**

Il thread discord\_to\_bot si occupa invece di gestire i comandi inviati dall’attaccante. Il cybercriminale può decidere di interrompere l’esecuzione dell’infostealer, cancellare un file o una cartella dal PC colpito, raccogliere un file o una cartella dalla vittima o eliminare il comando dal database utilizzato per verificare se il client è ancora attivo.

## Le conseguenze della scoperta

Dopo aver scoperto la vera identità del cheat, EDP e altri proprietari dei forum hanno avvisato i propri utenti e **hanno bandito Mythical dai propri server.** CyberArk Labs ipotizza più di un migliaio di utenti colpiti, con una quantità di informazioni sottratte significativa.

“*Il malware nei cheat e nei software craccati non è raro, ma **questo è il primo caso in cui ci siamo imbattuti in uno sviluppatore di cheat a pagamento che si è arricchito attaccando i suoi stessi clienti***” afferma El. Il ricercatore spiega inoltre che il danno non è limitato alla vittima, perché gli utenti possono accedere ai propri account lavorativi dai loro PC personali ed esporre la propria azienda a potenziali pericoli.

**EvolvedAim ora non è più attivo** e il server Discord è stato chiuso, così com...