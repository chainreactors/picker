---
title: Le piattaforme cloud storage E2EE sono vulnerabili al furto di dati
url: https://www.securityinfo.it/2024/10/23/piattaforme-cloud-storage-e2ee-vulnerabili-furto-dati/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-24
fetch_date: 2025-10-06T18:55:20.005830
---

# Le piattaforme cloud storage E2EE sono vulnerabili al furto di dati

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

## Le piattaforme cloud storage E2EE sono vulnerabili al furto di dati

Ott 23, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/10/23/piattaforme-cloud-storage-e2ee-vulnerabili-furto-dati/#respond)

---

Un’approfondita analisi dei ricercatori di sicurezza Jonas Hoffman e Kien Tuong Truong ha rivelato che **l’ecosistema di cloud storage E2EE**, ovvero con cifratura end-to-end (end-to-end encryption), **soffre di vulnerabilità crittografiche che consentono agli attaccanti di accedere ai dati degli** **utenti**, violandone la confidenzialità e l’integrità.

Hoffman e Truong [hanno analizzato](https://brokencloudstorage.info/) cinque dei principali provider del settore, ovvero **Sync**, **pCloud**, **Icedrive**, **Seafile** e **Tresorit**, trovando vulnerabilità anche molto gravi nei primi quattro.

Gli impatti dei bug variano dall’iniezione di file alla modifica dei dati, ma in alcuni casi possono fornire agli attaccanti accesso diretto alle informazioni in chiaro. ***“Molti dei nostri attacchi colpiscono più provider nello stesso modo, rivelando pattern fallimentari comuni a design crittografici indipendenti*“** hanno affermato i ricercatori.

![cloud E2EE](https://www.securityinfo.it/wp-content/uploads/2024/10/cloud-computing-4246668_1920.jpg)

## Le vulnerabilità nelle piattaforme cloud E2EE

Nel caso di **Sync**, i ricercatori sono riusciti ad **alterare la confidenzialità dei file in cloud e iniettarne di nuovi**, modificandone poi il contenuto. Alcuni metadati dei file non sono cifrati né autenticati e possono essere facilmente manipolati, per esempio modificando la grandezza delle risorse, il tipo, la data di creazione e anche il nome dell’utente che ha creato il file (o la cartella).

Un’altra vulnerabilità importante presente in Sync riguarda la condivisione dei file tramite link: **gli URL generati contengono una password in chiaro dalla quale poi viene derivata una chiave usata per decifrare i file.** Poiché la password è parte dell’indirizzo e non è codificata nell’URL fragment, può essere acceduta da chiunque.

Anche il cloud E2EE di **pCloud** è vulnerabile ad attacchi di **sostituzione di chiavi** e di **modifica di file e metadati.** La piattaforma soffre anche di un bug di **Unathenticated Chunking**: pCloud supporta il chunking dei file e la cifratura per ogni pezzo viene eseguita separatamente dagli altri. Per garantire l’integrità del file è quindi necessario un meccanismo di autenticazione; nel caso di pCloud, l’approccio scelto non è sicuro e consente a un attaccante di eliminare intere parti di file.

Anche **Seafile**, provider di cloud storage open-source, soffre di alcune delle precedenti vulnerabilità, alle quali si aggiungono quelle di **Protocol Downgrade** e di **Unathenticated Encryption**. Nel primo caso, poiché il provider permette agli utenti di scegliere la versione dei protocolli da usare, gli attaccanti possono usare questo meccanismo per effettuare il downgrade e sfruttare le vulnerabilità di una determinata versione.

Nel secondo caso, il cloud usa la modalità CBC (Cipher Block Chaining) non autenticata per la cifratura; ciò implica che né i file né i filename sono protetti da attacchi che violano l’integrità dei contenuti.

Anche **Icedrive** è vulnerabile all’i**niezione e alla modifica di file**, così come all’**Unathenticated Encryption** e all’**Unathenticated Chunking**. Poiché inoltre **tutti i file e i filename sono cifrati usando la stessa chiave**, senza alcun meccanismo crittografico che li lega insieme o alla posizione nel cloud, gli attaccanti possono cambiare la posizione delle risorse e scambiarne i nomi in maniera arbitraria.

I ricercatori in realtà hanno individuato falle anche in **Tresorit**: l’autenticazione per la chiave pubblica si basa su certificati controllati dal server che gli attaccanti possono rimpiazzare per avere accesso ai file; inoltre, i metadati possono essere manomessi, per esempio alterando la data di creazione dei file. Nel caso di Tresorit, però, **le vulnerabilità non espongono direttamente i contenuti dei file** e la manipolazione dei dati non è così immediata come per gli altri provider.

![cloud E2EE](https://www.securityinfo.it/wp-content/uploads/2024/10/ai-generated-7962522_1920.jpg)

## La risposta dei provider

I ricercatori hanno segnalato immediatamente le vulnerabilità a Sync, pCloud, Seafile e Icedrive lo scorso aprile. Icedrive e Seafile hanno risposto subito all’avviso, anche se la prima ha deciso di non occuparsi delle problematiche identificate; la seconda invece ha risolto il bug del downgrade del protocollo. **Sync e pCloud devono ancora rispondere alle segnalazioni.**

**Tresorit** è stata informata dei suoi bug più tardi, il 27 settembre scorso, e ha riconosciuto i problemi individuati. Contattata da [BleepingComputer](https://www.bleepingcomputer.com/news/security/severe-flaws-in-e2ee-cloud-storage-platforms-used-by-millions/) per ricevere aggiornamenti, la compagnia ha si è detta **al lavoro su alcuni dei fix previsti.**

I ricercatori sottolineano che dall’analisi emergono due questioni importanti: la prima è che **c’è ancora un grosso gap tra ciò che promettono i provider e le aspettative degli utenti** in termini di confidenzialità dei file; la seconda è che **le diverse piattaforme hanno problemi analoghi tra loro** nel garantire la sicurezza, a indicazione del fatto che risolvere queste sfide non è banale.

Per ...