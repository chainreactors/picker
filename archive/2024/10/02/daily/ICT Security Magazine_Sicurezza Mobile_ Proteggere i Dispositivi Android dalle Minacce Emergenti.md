---
title: Sicurezza Mobile: Proteggere i Dispositivi Android dalle Minacce Emergenti
url: https://www.ictsecuritymagazine.com/articoli/sicurezza-mobile-android/
source: ICT Security Magazine
date: 2024-10-02
fetch_date: 2025-10-06T18:55:16.534296
---

# Sicurezza Mobile: Proteggere i Dispositivi Android dalle Minacce Emergenti

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

![Sicurezza delle applicazioni mobili](https://www.ictsecuritymagazine.com/wp-content/uploads/Sicurezza-delle-applicazioni-mobili.jpg)

# Sicurezza Mobile: Proteggere i Dispositivi Android dalle Minacce Emergenti

A cura di:[Alessio Merlo](#molongui-disabled-link)  Ore 1 Ottobre 20241 Ottobre 2024

In un’era in cui i dispositivi mobili sono diventati parte integrante della nostra vita quotidiana, l’importanza della sicurezza mobile non può essere sottovalutata. Poiché i nostri smartphone e tablet diventano sempre più il repository di una quantità sempre maggiore di dati sensibili, la necessità di proteggere questi dispositivi dalle minacce emergenti è diventata fondamentale.

Per una migliore contestualizzazione del tema, si consiglia la lettura dell’articolo precedente “[Sicurezza del Sistema Operativo Android](https://www.ictsecuritymagazine.com/articoli/sicurezza-del-sistema-operativo-android/)“. I contenuti presentati sono stati estratti dal testo approfondimento sulla “[Sicurezza Mobile”](https://www.ictsecuritymagazine.com/pubblicazioni/mobile-security-nozioni-e-riflessioni/) realizzato dal Professor Alessio Merlo, Ordinario di Sistemi di Elaborazione delle Informazioni presso il CASD – Centro Alti Studi per la Difesa di Roma.

## Sicurezza delle applicazioni mobili

In questo estratto ci focalizzeremo sulle problematiche di sicurezza del livello applicativo. Per semplicità assumeremo che il sistema operativo Android sia completamente sicuro. In questo caso, le vulnerabilità che tratteremo saranno solo legate alle singole app; e i corrispondenti *malware* sfrutteranno soltanto vulnerabilità a livello applicativo tramite i canali previsti (e protetti dall’ASF), senza l’utilizzo di *side channel*.

### Il Phishing

Prima di discutere di vulnerabilità di app, occorre chiarire come il *malware* possa raggiungere il dispositivo e quindi l’app da attaccare. L’idea alla base è circuire l’utente, che ha il potere di installare/rimuovere app, per farsi installare ed eseguire. L’attacco principale che porta a questo risultato è un attacco di *phishing*. Nella sostanza, l’idea è far abboccare il pesce (l’utente) a un amo costruito *ad hoc* dall’attaccante.

Un esempio semplice è il classico link inviato per posta, dove si invita l’utente a cliccare e provare una app. A questo link si trova l’APK del malware che l’utente installa non aspettandosi certo un contenuto dannoso.

Il caso precedente, però, è molto naif. Ormai la maggior parte degli utenti è consapevole dei rischi e non abbocca a questi “ami” molto semplici: potremmo dire che questo attacco ha una probabilità di successo molto bassa, così bassa che forse per l’attaccante non è nemmeno conveniente provarlo.

Tuttavia, il *phishing* rimane il mezzo più efficace per permettere ai *malware* di arrivare all’obiettivo; nel prossimo articolo mostreremo un esempio di come gli attacchi di *phishing* su Android oggi siano tanto sofisticati quanto efficaci e portino, spesso, l’utente ad “abboccare all’amo” senza accorgersene.

## Dentro una vulnerabilità applicativa

Ad oggi si contano innumerevoli vulnerabilità scoperte in app di diverso tipo, anche ad alta sicurezza come quelle bancarie[[1]](#_ftn1). L’esplorazione delle singole vulnerabilità sarebbe un mero esercizio tecnico per appassionati.

Da un punto di vista metodologico, è molto più importante capire il processo e i fattori che portano alla creazione, scoperta e risoluzione di una vulnerabilità applicativa. Per fare questo, ci metteremo nei panni dell’attaccante e vedremo come scoprire e attaccare una vulnerabilità specifica, che ci permetta inoltre di arrivare a conclusioni non comuni e, forse, inattese.

Partiamo direttamente dalle conclusioni:

1. vulnerabilità che portano al furto di credenziali utente possono NON essere ad alto rischio;
2. funzionalità introdotte in nuove versioni di Android possono aiutare a sfruttare vulnerabilità applicative e ad aumentarne il rischio;
3. una volta scoperta una vulnerabilità, la risoluzione potrebbe non essere possibile in tempi brevi.

Per dimostrare le tesi precedenti, prenderemo in esame un insieme di vulnerabilità che riguarda i *password manager[**[2]**](#_ftn2)* (d’ora in poi, PM) su Android.

I PM sono applicazioni dedicate alla gestione delle credenziali utente e nascono storicamente sul web. Ogni browser, oggi, ha un proprio PM che, ogni qual volta un utente visita un nuovo portale o servizio web, salva le credenziali inserite e le inserisce automaticamente qualora lo stesso utente torni a visitare il medesimo sito. Inoltre esiste un insieme consistente di PM generici, non legati ad alcun browser, di larga applicazione nel mondo aziendale: tra questi possiamo citare LastPass, Dashlane, KeepPassX, 1Password, Keeper, onSafe, myPassword, ma la lista è molto lunga.

La crescita esponenziale di questo tipo di software mostra l’esistenza di un business fiorente e ormai consolidato intorno a questi servizi nel web: è lo specchio dei tempi ed è “colpa” della sicurezza informatica. Nello specifico, oggi siamo costretti a ricordare password diverse e complesse per ogni sito, oltre a doverle cambiare con una certa costanza, se vogliamo seguire le “buone maniere” della *cybersecurity*.

Pertanto, non possiamo ricordare tutto e dobbiamo affidarci a ...