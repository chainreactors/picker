---
title: Buoni propositi per il 2023: nasce la Dashboard Ransomware Monitor
url: https://www.insicurezzadigitale.com/buoni-propositi-per-il-2023-nasce-la-dashboard-ransomware-monitor/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-02
fetch_date: 2025-10-04T02:52:35.064571
---

# Buoni propositi per il 2023: nasce la Dashboard Ransomware Monitor

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

[Analisi](https://insicurezzadigitale.com/category/analisi/)

# Buoni propositi per il 2023: nasce la Dashboard Ransomware Monitor

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
1 Gennaio 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot-2022-12-31-at-01-43-26-Dashboard-Ransomware-Monitor-1024x476.png)

Si parla di:

Toggle

* [Dashboard Ransomware Monitor in dettaglio](#Dashboard_Ransomware_Monitor_in_dettaglio)
* [Funzionalità della Dashboard](#Funzionalita_della_Dashboard)

Piuttosto che fare report e tirare le somme dell’anno appena passato con tutte le previsioni per il futuro, quest’anno ho voluto creare direttamente lo strumento che, un giorno, potrebbe essere utile per fare proprio questo.

Dopo il blog (questo che stai leggendo), il recente progetto [Mastodon](https://mastodon.insicurezzadigitale.com/home), arriva un nuovo elemento all’interno della galassia *inSicurezzaDigitale*.

Si chiama **Dashboard Ransomware Monitor** è raggiungibile apertamente da questo indirizzo: [ransom.insicurezzadigitale.com](https://ransom.insicurezzadigitale.com) e come si può intuire è uno strumento che (spero) possa essere utile a tutti per fare chiarezza su ciò che sta succedendo nel settore informatico (quasi in real time), con gli attacchi di tipo ransomware.

## Dashboard Ransomware Monitor in dettaglio

La piattaforma si presenta in versione Web application, l’ho scritta io in PHP ed è un prodotto che offro come liberamente accessibile a chiunque sia interessato. Per il momento il frontend non è opensource semplicemente perché non sono un coder professionista e reputo il codice di questo progetto non presentabile al mondo esterno (funziona bene per me, anche se non è bello da leggere). Nasce dall’esigenza di avere, su un unico *contenitore*, tutto il mondo del ransomware (che oggi è molto vasto) facilmente visionabile, con aggiornamenti più o meno puntuali e pressoché automatizzato. Senza che l’archivio avesse limitazioni di consultazione, esportazione e fruizione.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot-2022-12-31-at-00-52-09-Dashboard-Ransomware-Monitor-1024x370.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot-2022-12-31-at-00-52-09-Dashboard-Ransomware-Monitor.png)

Il punto di forza di questo progetto italiano, è appunto la possibilità di seguire il tutto con un comodo e standard **feed RSS** universale.

Il progetto è italiano, la piattaforma è italiana, tuttavia la funzionalità è globale, quindi può avere impatti anche all’estero qualora reputata utile.

Lo strumento per il backend è un fork di RansomWatch, modificato per le esigenze di scraping personalizzate e più precise, correggendone alcuni punti deboli, che appunto effettuata l’**interrogazione di un grande numero di siti Web onion** appartenenti alle più note organizzazioni criminali informatiche, ad intervalli di tempo regolari. Queste interrogazioni vengono salvate sul server e successivamente vengono **analizzate dallo scraper**, che cattura gruppo per gruppo le informazioni (titolo e data) degli ultimi post inseriti, conservandole in un file JSON.

Il file JSON viene poi dato in pasto al **parser** (in PHP) che ogni 5 minuti, interroga gli ultimi 200 elementi archiviati, confrontandoli con un **database MySQL** permanente **tramite un hash**, il quale in caso di non esistenza, **produce una nuova INSERT** sul database, generando così un **feed perenne e autogestito**, dall’inizio alla fine, senza intermediari terzi, di attacchi ransomware.

## Funzionalità della Dashboard

Dal punto di vista dell’analisi, l’applicazione Web offre poche funzionalità per non perdere appunto la sua semplicità di utilizzo. Ad ogni modo, queste poche funzionalità sono sempre espandibili e lasciano l’utente libero di poterne usufruire o farne ulteriori analisi in proprio, grazie agli strumenti standardizzati utilizzati.

Oltre la consultazione e la ricerca, direttamente da browser, c’è una **sezione “Grafici”** che viene aggiornata in tempo reale con i gruppi più prolifici e i Paesi più colpiti.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot-2022-12-31-at-00-53-17-Dashboard-Ransomware-Monitor-1024x401.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot-2022-12-31-at-00-53-17-Dashboard-Ransomware-Monitor.png)

Una sezione è poi dedicata ad offrire una rassegna stampa giornaliera, di ciò che è l’universo ransomware nel mondo. Con una selezione curata di notizie WorldWide, inerenti il ransomware e degne di nota (con opportuni link).

Altra importanza, per la fruizione standard ed aperta dello strumento, è la sezione “Esportazioni” che la piattaforma offre. Permette infatti differenti metodi di esportazione dei dati, direttamente in formato CSV, anche totali (di tutto l’archivio memorizzato), o parziali (solo attacchi Italia, oppure di anni specifici).

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot-2022-12-31-at-00-55-24-Dashboard-Ransomware-Monitor.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot-2022-12-31-at-00-55-24-Dashboard-Ransomware-Monitor.png)

Questa funzionalità, molto importante in una politica pienamente **open** dello strumento, è importante per chiunque voglia utilizzare questi dati, al fine di curarne ulteriori analisi e studi.

Come già detto, dunque, non può mancare la funzione di **feed RSS**. Tutti gli aggiornamenti, quasi in tempo reale, della piattaforma, sono associabili ad un qualsiasi lettore Feed RSS utilizzato dall’utente, semplicemente presentando l’apposito link. Come specificato nella barra laterale (o in alto) nella piattaforma.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot_2022-12-31_00_54_17-1024x461.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/12/Screenshot_2022-12-31_00_54_17.png)

Dunque non mi resta che augurarvi Buon inizio di anno nuovo, con questo buon proposito per il 2023. E augurarmi che la piattaforma possa diventare uno strumento utile per chiunque voglia aggiornamenti puntuali sul mondo ransomware, facili da fruire.

Buona navigazione e buon utilizzo della [Dashboard Ransomware Monitor](https://ransom.insicurezzadigitale.c...