---
title: Vulnerabilità Subaru: il vero problema sono le politiche di gestione dei dati
url: https://www.securityinfo.it/2025/01/30/vulnerabilita-subaru-il-vero-problema-sono-le-politiche-di-gestione-dei-dati/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-01
fetch_date: 2025-10-06T20:37:32.934848
---

# Vulnerabilità Subaru: il vero problema sono le politiche di gestione dei dati

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

## Vulnerabilità Subaru: il vero problema sono le politiche di gestione dei dati

Gen 30, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/01/30/vulnerabilita-subaru-il-vero-problema-sono-le-politiche-di-gestione-dei-dati/#respond)

---

Una ricerca condotta da Sam Curry e Shubham Shah, esperti di sicurezza,  ha portato alla luce significative vulnerabilità nei sistemi web di Subaru che permettevano agli eventuali attaccanti di avere un certo controllo sull’auto e, altrettanto proccupante, sulla privacy del proprietario. L’indagine ha avuto origine dall’analisi di una Subaru Impreza del 2023, acquistata dalla madre di Curry, con lo scopo di testarne le funzionalità connesse. Attraverso un’attenta analisi, i ricercatori hanno identificato delle falle nel portale web di Subaru, destinato ai dipendenti, che hanno permesso loro di ottenere il controllo di alcune funzionalità dell’auto, come l’apertura delle portiere, l’attivazione del clacson e l’avviamento del motore.

![](https://www.securityinfo.it/wp-content/uploads/2025/01/Subaru.png)

**Accesso non autorizzato e controllo remoto di alcune funzioni, ma anche grossi problemi di privacy**

Le vulnerabilità individuate non si limitavano al semplice controllo delle funzioni dell’auto. Curry e Shah sono riusciti a manipolare il sistema in modo tale da poter **riassegnare il controllo di queste funzionalità a qualsiasi dispositivo, come un telefono o un computer**. Questo significa che un attaccante, sfruttando la stessa vulnerabilità, avrebbe potuto assumere il controllo remoto di un veicolo Subaru, rappresentando un serio rischio per la sicurezza del proprietario.

Ancora più allarmante è stata la scoperta che attraverso il portale web di Subaru, i ricercatori potevano accedere a una **mappa dettagliata e accurata degli spostamenti del veicolo, risalente a un anno**. Questa mappa non solo mostrava la posizione attuale dell’auto, ma anche la sua posizione passata, consentendo di ricostruire gli spostamenti quotidiani del proprietario. Il livello di dettaglio era tale da rendere possibile l’identificazione di luoghi frequentati, come studi medici, case di amici, e persino il posto auto abitualmente utilizzato. Questo aspetto solleva interrogativi etici e legali sull’uso e la conservazione dei dati sulla posizione dei clienti.

**Il meccanismo di attacco era imbarazzante**

L’attacco è stato reso possibile grazie a una combinazione di **vulnerabilità nella gestione delle password e dei dati utente del portale dipendenti**. I ricercatori hanno scoperto di poter reimpostare le password degli account dipendenti semplicemente indovinando il loro indirizzo email, aggirando il sistema di sicurezza realtivo al reset della password che, invece di essere gestito lato server, era gestito localmente sul browser. Hanno ottenuto l’indirizzo e-mail di un dipendente di Subaru su LinkedIn e così hanno potuto assumere il controllo del suo account. Una volta all’interno, hanno sfruttato l’accesso per **cercare qualsiasi proprietario di Subaru per cognome, codice postale, email, numero di telefono o targa**. Da lì, hanno potuto accedere e riassegnare le funzioni Starlink del veicolo, incluse le funzionalità di sblocco e avviamento e tracciamento della posizione. Come sia possibile nel 2025 pensare che il reset della password venga gestito in locale invece che sul server aziendale è veramente un mistero in quanto è un errore di progettazione triviale.

**Implicazioni per la Privacy e la Sicurezza**

Ma quello che stupisce più di tutto è il problema della gestione dei dati. **Cosa se ne fa Subaru dello storico preciso al metro degli spostamenti dell’utente?** Possiamo capire la necessità di avere la posizione geografica in caso di richiesta di aiuto, ma quest’uso non implica in nessun modo il conservare il dato per un anno. Possiamo anche capire la necessità di analizzare i dati d’uso dell’auto per migliorare l’affidabilità meccanica, ma anche in questo caso non serve conservarli “interi”: li si può anonimizzare facilmente senza perderne la validità. In definitiva, dopo anni passati a ignorare il potenziale dei dati, adesso molte aziende sembrano determinate a raccoglierne la maggior quantità possibile, senza però pensare davvero alla loro gestione in sicurezza.  I dati sono una componente essenziale dei processi moderni, ma vanno gestiti in maniera da rispettare la privacy degli utenti e, soprattutto, pensando a come proteggerli in caso di violazione.

**Le Risposte di Subaru**

Subaru ha rilasciato una dichiarazione in cui ha affermato di aver corretto immediatamente le vulnerabilità segnalate dai ricercatori e ha negato che le informazioni dei clienti siano state consultate senza autorizzazione. La compagnia ha ammesso che i suoi dipendenti hanno accesso ai dati sulla posizione, ma solo per le finalità necessarie, come la notifica ai soccorritori in caso di incidente. La compagnia ha anche affermato che tali dipendenti ricevono una formazione appropriata e firmano accordi di riservatezza. Tuttavia, non è chiaro quanto a lungo Subaru conservi i dati di localizzazione dei suoi clienti e quali siano le policy di accesso e conservazione di tali dati.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [auto](https://www.securityinfo.it/tag/auto/), [Automobili](https://www.securityinfo.it/tag/automobili/), [Car Hacking](https://www.securityinfo.it/tag/car-hacking/), [Car Security](https://w...