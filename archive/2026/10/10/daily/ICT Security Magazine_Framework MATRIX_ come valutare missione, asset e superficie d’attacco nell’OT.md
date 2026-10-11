---
title: Framework MATRIX: come valutare missione, asset e superficie d’attacco nell’OT
url: https://www.ictsecuritymagazine.com/articoli/framework-matrix-zero-trust-ot-missione-asset-minacce/
source: ICT Security Magazine
date: 2026-10-10
fetch_date: 2026-10-11T08:03:43.019808
---

# Framework MATRIX: come valutare missione, asset e superficie d’attacco nell’OT

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![disegno 3d dove si crea un muovimento che dal bersaglio sopra le montagne attraversa sicurezza e circuiti: Framework MATRIX](https://www.ictsecuritymagazine.com/wp-content/uploads/Framework-MATRIX.png)

# Framework MATRIX: come valutare missione, asset e superficie d’attacco nell’OT

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 10 Ottobre 20262 Ottobre 2026

*Dalla missione agli asset, fino alla superficie d’attacco: il framework MATRIX traduce i principi Zero Trust in un metodo selettivo per gli ambienti OT.*

Le [prime due parti della serie](https://www.ictsecuritymagazine.com/articoli/zero-trust-modello-purdue-ot/) hanno descritto il problema e il contesto: impianti non più isolati, priorità capovolte rispetto all’IT, dispositivi che non possono ospitare i controlli tradizionali. Da qui prende forma MATRIX.

Questa terza parte presenta i tre principi del framework e le prime tre delle sei fasi: la caratterizzazione della missione, la profilazione dell’idoneità degli asset e la modellazione delle minacce. Ogni fase si chiude con un riquadro che ne indica il risultato, utile per seguire il filo del ragionamento.

## Framework MATRIX: principi e fasi del metodo

Un approccio in sei fasi per collegare missione, caratteristiche degli asset, minacce e controlli sostenibili.

MATRIX si basa su tre principi guida:

1. L’orientamento alla missione: la sicurezza non è un fine in sé, ma uno strumento al servizio della capacità del sistema di svolgere la propria funzione in modo sicuro e affidabile. Ne consegue che le misure di protezione devono essere calibrate sul valore che ciascun asset riveste per la missione;
2. L’applicabilità differenziata: in un ambiente eterogeneo, non esiste una configurazione zero trust valida per l’intero impianto e i singoli componenti del modello devono essere scomposti e allocati dove è tecnicamente possibile;
3. La natura iterativa è legata al ciclo di vita: l’adozione dello Zero Trust non è un progetto a termine, ma un processo continuo che deve essere rivalutato in base all’evoluzione delle tecnologie, delle minacce e delle risorse disponibili.

La Figura 2 rappresenta le sei fasi del framework come un ciclo che alimenta e aggiorna l’artefatto centrale: la matrice di allocazione delle capacità.

![Le sei fasi del framework MATRIX, organizzate come cicloiterativo attorno alla matrice di allocazione delle capability](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_RoMLYlTwll-700x610.png)

Figura 2. Le sei fasi del framework MATRIX, organizzate come ciclo iterativo attorno alla matrice di allocazione delle capability

### Mission context: missione e DAAS nel framework MATRIX

La prima fase stabilisce il perché del sistema prima ancora del come proteggerlo. Si tratta di ricostruire la missione attraverso i mission thread, ossia le sequenze di attività e processi che descrivono come il sistema consegue i propri obiettivi, e di individuare gli scenari e le modalità operative in cui esso funziona. In un sistema di distribuzione elettrica, ad esempio, la missione consiste nel trasformare, regolare e distribuire energia tra le fonti di generazione e gli utilizzatori finali in modo sicuro e continuo; gli scenari rilevanti comprendono la regolazione della tensione, la gestione della distribuzione del carico e la protezione contro i guasti.

All’interno di questi thread si identificano i DAAS – dati, applicazioni, asset e servizi – che ne costituiscono gli abilitatori. Questa caratterizzazione non ha valore puramente descrittivo: definisce le conseguenze potenziali di un attacco, fornendo il metro con cui, nelle fasi successive, si peseranno le minacce e si prioritizzeranno i controlli. Senza questo radicamento, la selezione delle capability rischierebbe di ottimizzare la sicurezza di asset marginali trascurando quelli da cui dipende la continuità del servizio.

> **OUTPUT DELLA FASE** *Mappa dei DAAS e delle conseguenze potenziali di un attacco.*

### Asset suitability: come valutare l’idoneità degli asset OT

La seconda fase risponde a una domanda spesso elusa: quanto un determinato asset è in grado di accogliere capability zero trust? La profilazione valuta ciascuna classe di asset rispetto ai cinque attributi richiamati nella Sezione 2.3. La configurabilità dinamica misura la possibilità di modificare in tempi prossimi al reale relazioni di fiducia, flussi e politiche di accesso. La flessibilità di retrofit esprime la capacità del sistema di accogliere modifiche progettuali o adeguamenti senza stravolgimenti architetturali.

Il margine SWaP indica la disponibilità di risorse di calcolo, memoria ed energia eccedenti rispetto alla funzione primaria. La tolleranza alla latenza quantifica quanto ritardo il sistema possa assorbire senza violare i propri requisiti prestazionali. La centratura IT, infine, segnala quanto un componente OT sia IT-like e dunque permeabile al riuso dei controlli di sicurezza informatica tradizionali.

Attribuendo a ciascun attributo un punteggio su scala ordinale si ottiene un profilo di idoneità per classe di asset, rappresentabile come in Figura 3. Il confronto è illuminante: una HMI costruita su piattaforma Windows e un ser...