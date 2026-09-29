---
title: Account WhatsApp compromessi su iPhone con iOS 16: l’attacco 0click che bypassa i dispositivi collegati - Forenser Srl
url: https://www.forenser.it/account-whatsapp-compromessi-su-iphone-con-ios-16/
source: Over Security
date: 2026-09-28
fetch_date: 2026-09-29T07:41:15.572533
---

# Account WhatsApp compromessi su iPhone con iOS 16: l’attacco 0click che bypassa i dispositivi collegati - Forenser Srl

Search for:

 Search

Menu

Close

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

Search for:

 Search

[![Forenser Srl](https://www.forenser.it/wp-content/uploads/forenser-digital-investigations.png)](https://www.forenser.it/)

[Forenser Srl](https://www.forenser.it/)

Studio Informatica Forense

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

# Account WhatsApp compromessi su iPhone con iOS 16: l’attacco 0-click che bypassa i dispositivi collegati

[![](https://secure.gravatar.com/avatar/65af508883433ee06fa507bcdcb1e77747fc2aba840a2130e6877e5be7ffdded?s=44&d=mm&r=g)](https://www.forenser.it/author/forenser/ "Posts by forenser")

[forenser](https://www.forenser.it/author/forenser/)
on
22 Maggio 2026

![WhatsApp](https://www.forenser.it/wp-content/uploads/75c012cc-0db7-4818-8769-d214de17d722-1024x683.png)

Un weekend tranquillo, di fine maggio: il tempo passa senza problemi fino a quando non iniziano ad arrivare messaggi ambigui sull’applicazione di WhatsApp installata sul tuo iPhone. I contatti iniziano a chiederti: *“perché devo darti dei soldi?”* oppure *“a cosa ti serve il bonifico?”*. Questi contatti stanno solo rispondendo ad un messaggio che è stato inviato dal tuo account WhatsApp; il problema è che tu non hai inviato nulla.

Questo è ciò che è accaduto negli ultimi giorni a diverse persone che si sono rivolte al nostro studio. Siamo stati contattati in più occasioni, nell’arco della stessa giornata, da utenti che avevano riscontrato la medesima anomalia. Il fatto curioso è che nessun dispositivo estraneo risultava associato all’account WhatsApp personale: la sezione “Dispositivi collegati” (“Linked Devices”) era pulita, eppure qualcuno stava inviando messaggi a nostra insaputa, dal nostro numero. Cosa sta succedendo?

A questo punto sono iniziate le nostre indagini per cercare di capire come sia possibile incorrere in una “problematica” di questo tipo. Quanto raccolto ha permesso di rivelare dei pattern comuni, utili per contestualizzare il tipo di minaccia e la superficie di attacco.

Table of Contents

Toggle

* [Confronto tra i casi](#Confronto_tra_i_casi)
* [Account Fantasma](#Account_Fantasma)
* [Versione di iOS](#Versione_di_iOS)
* [Riproduzione dello scenario in laboratorio](#Riproduzione_dello_scenario_in_laboratorio)
* [Indicazioni operative per utenti e vittime](#Indicazioni_operative_per_utenti_e_vittime)

## **Confronto tra i casi**

Mettendo a confronto i diversi casi raccolti, abbiamo individuato una serie di elementi ricorrenti che delineano lo scenario di compromissione:

• tutti i casi rilevati riguardano iPhone (dal modello 8 al 14, incluse le varianti X, XR, XS, 11, SE, 12 e 13) su cui è installata un versione di iOS 16 nelle sue diverse release;

• gli attaccanti scrivono in chat ai contatti della vittima, dal numero WhatsApp della vittima stessa, chiedendo di disporre bonifici;

• gli attaccanti sembrano avere accesso alle sole chat recenti, ovvero a quelle con cui la vittima ha interagito da poco;

• nessun dispositivo collegato è visibile nella sezione “Dispositivi collegati” delle impostazioni di WhatsApp;

• le vittime non riportano di aver compiuto alcuna azione di pairing particolare: non hanno fornito codici, non hanno inquadrato QR code, non hanno autorizzato accessi.

Per queste ragioni è stato sin da subito evidente che non si trattasse di un classico episodio di ghost pairing (nel quale l’attaccante induce la vittima a scansionare un QR code o a condividere un codice di verifica): l’assenza di qualsiasi interazione richiesta all’utente fa propendere per una compromissione di tipo 0-click, cioè per un’infezione che non richiede alcun intervento da parte della vittima e che colpisce direttamente lo smartphone o l’app WhatsApp.

## **Account Fantasma**

Il primo aspetto senza dubbio interessante è la mancanza di un dispositivo associato. Analizzando i log di una delle copie forensi e il relativo sysdiagnose (componente del sistema operativo iOS contenente i log di diagnostica del telefono), è stato possibile notare un’anomalia nei log generati da WhatsApp: una continua sequenza di eventi di “resync”, come se l’applicazione stesse continuamente rinegoziando la sessione con i server di WhatsApp. Si tratta di eventi non molto comuni presenti in quantità insolita, **a meno che qualcun altro non stia tentando in parallelo di mantenere attiva una propria sessione sullo stesso account**.

Questa sequenza continua di sincronizzazione, di fatto, è il sintomo di una “competizione” tra due endpoint che cercano di mantenere attiva la stessa sessione, dinamica che approfondiremo successivamente, dopo aver discusso del probabile vettore di compromissione.

## **Versione di iOS**

Un secondo aspetto molto interessante è che tutte le persone che ci hanno contattato possiedono un iPhone, con una specifica versione: iOS 16. Che sia questo il comune denominatore?

Partendo da tale presupposto abbiamo approfondito, ricercando tra i vari articoli presenti in rete e tra i log a disposizione, presenti tra i dati dei dispositivi compromessi. Ricercando problematiche di sicurezza correlate ad iOS 16 abbiamo notato una vulnerabilità descritta nel CVE-2025-43300, possibilmente in combinazione con il CVE 2025-55177 (vulnerabilità di WhatsApp iOS/macOS che poteva consentire il parsing di contenuti da URL arbitrari tramite messaggi di sincronizzazione dei dispositivi collegati non correttamente autorizzati):

![ios](https://www.forenser.it/wp-content/uploads/Immagine1-1024x545.png)

La vulnerabilità identificata pare sia correlata al processo delle immagini da parte di una libreria del sistema operativo, libreria utilizzata da diverse applicazioni come, appunto, WhatsApp. In aggiunta, nelle ultime settimane, la letteratura online in relazione a questa vulnerabilità sembra sia stata ampiamente documentata, rendendo di conseguenza più facile lo sfruttamento. Stando a quanto riportato dalla descrizione della vulnerabilità, le versioni di iOS minori della 16.7.12 sembrano essere vulnerabili, versioni compatibili con quelle da noi rilevate nei dispositivi delle vittime.

A supporto di questa tesi, all’interno degli unified logs estratti dal dispositivo sono state rinvenute molteplici occorrenze di errori generati proprio dalla libreria che si occupa del parsing delle immagini, in orari compatibili con quelli relativi alla compromissione degli account WhatsApp.

## **Riproduzione dello scenario in laboratorio**

Per chiudere il cerchio attorno alla sequenza anomala di “resync” osservata nei log, i nostri tecnici hanno provato a riprodurre in laboratorio una parte dello scenario di compromissione, impiegando un device di “test” con installata una versione di iOS vulnerabile. L’attività ha permesso di confermare che esi...