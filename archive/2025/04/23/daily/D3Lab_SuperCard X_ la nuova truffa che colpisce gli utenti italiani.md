---
title: SuperCard X: la nuova truffa che colpisce gli utenti italiani
url: https://www.d3lab.net/supercard-x-la-nuova-truffa-che-colpisce-gli-utenti-italiani/
source: D3Lab
date: 2025-04-23
fetch_date: 2025-10-06T22:09:01.010122
---

# SuperCard X: la nuova truffa che colpisce gli utenti italiani

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# SuperCard X: la nuova truffa che colpisce gli utenti italiani

[Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Copertina.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Copertina.png?fit=1030%2C687&ssl=1 "SuperCardX_Copertina")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Copertina.png?resize=1030%2C687&ssl=1)

Dalla seconda metà di febbraio 2025, è stata osservata in Italia una nuova campagna fraudolenta che sfrutta applicazioni Android apparentemente legittime per sottrarre i dati delle carte bancarie tramite tecnologia NFC. Queste app, denominate “SuperCard X”, “KingCard”, o “Verifica Carta”, non sono malware che comprometto il device in senso tradizionale, ma strumenti sofisticati che consentono ai criminali di **emulare carte di credito o debito** e **disporre illeciti pagamenti contactless a distanza**, sfruttando dispositivi controllati da remoto.

## 🔎 Un caso di esempio: tra Smishing, Vishing e NFC

Un tipico scenario osservato in Italia nelle ultime settimane prevede un attacco suddiviso in più fasi, con un’efficace combinazione di smishing (phishing via SMS), vishing (phishing telefonico) e abuso delle funzionalità NFC degli smartphone Android.

La vittima riceve inizialmente un SMS apparentemente proveniente dalla propria banca o da un istituto finanziario noto. Il messaggio allude a una presunta attività sospetta sulla carta di credito o a un problema legato alla sicurezza dell’account. Viene quindi suggerito di effettuare una verifica accedendo a un sito web, il cui nome è costruito in modo da sembrare familiare e affidabile: si tratta di **domini creati ad hoc**, talvolta molto simili a quelli delle banche reali (typosquatting), altre volte con nomi generici che evocano concetti di sicurezza, protezione, verifica o aggiornamento della carta.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Phishing_2.png?resize=376%2C668&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Phishing_1.png?resize=1080%2C2108&ssl=1)

Una volta sul sito, l’utente trova un’interfaccia rassicurante, localizzata in lingua italiana, che invita a scaricare un’app per completare la procedura di sicurezza. L’APK scaricata – con nomi come “Sicurezza Carta” o “Verifica Carta” – appare semplice e curata. Durante una telefonata parallela, un falso operatore guida l’utente nei passaggi di installazione, richiedendo anche di avvicinare fisicamente la carta di pagamento al proprio smartphone, così da “verificare l’autenticità” tramite NFC. In realtà, in quel momento l’app sta leggendo i dati della carta e trasmettendoli a un criminale che, da remoto, può emularla ed effettuare acquisti o prelievi contactless.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Screenshot_2.png?resize=320%2C640&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Screenshot_4.png?resize=320%2C640&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Screenshot_3.png?resize=320%2C640&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/04/SuperCardX_Screenshot_1.png?resize=320%2C640&ssl=1)

## 🔧 Analisi tecnica di SuperCard X

L’applicazione SuperCard X rappresenta un’evoluzione nel panorama delle minacce Android, perché non si comporta come un malware bancario tradizionale: non intercetta SMS, non sovrappone schermate false e non richiede permessi invasivi. La sua struttura è modulare e altamente professionale, come evidenziato anche nel report tecnico di [Cleafy](https://www.cleafy.com/cleafy-labs/supercardx-exposing-chinese-speaker-maas-for-nfc-relay-fraud-operation).

La componente principale è suddivisa in due app distinte:

* Il modulo **Card Reader**, destinato a essere installato sullo smartphone della vittima, sfrutta l’NFC per leggere i dati della carta fisica quando questa viene avvicinata al dispositivo.
* Il modulo **POS Tapper**, invece, è utilizzato dai criminali per emulare la carta su terminali di pagamento o sportelli ATM abilitati al contactless.

La comunicazione tra le due app avviene in tempo reale tramite server Command and Control (C2), e sfrutta una connessione cifrata con **mutual TLS (mTLS)**. Ogni lettore è identificato da un **UID** univoco, che il criminale utilizza per associare il dispositivo della vittima al proprio terminale di emulazione.

Tra le caratteristiche più avanzate vi è la capacità di supportare più Tapper contemporaneamente collegati allo stesso Reader, permettendo di replicare la carta su più dispositivi e massimizzare il guadagno prima che venga bloccata. L’app è compatibile con un ampio ventaglio di circuiti di pagamento, tra cui Visa, Mastercard, UnionPay, Amex, e integra anche modalità di compatibilità con Apple Pay, Google Pay e Samsung Pay.

Dal punto di vista tecnico, SuperCard X richiede pochissimi permessi (spesso solo NFC), rendendola difficilmente rilevabile dai software antivirus, e utilizza un’interfaccia utente semplice ma efficace, che ispira fiducia anche a utenti poco esperti.

## 📱 Il canale Telegram dei criminali

Un aspetto particolarmente importante dell’ecosistema SuperCard X è l’esistenza di un **canale Telegram ufficiale** che funge da punto di riferimento per clienti, affiliati e acquirenti nello stesso schema di un MaaS (Malware-as-a-Service). Il canale, gestito da utenti che parlano cinese, pubblicano costantemente aggiornamenti, annunci, guide all’uso e persino video dimostrativi dell’app in funzione come il seguente.

[![](https://www.d3lab.net/wp-content/uploads/2025/04/Screenshot-2025-04-18-alle-17.53.11.png)](https://www.d3lab.net/wp-content/uploads/2025/04/video_2025-04-18_17-17-28-HB2.mp4)

All’interno del canale vengono fornite istruzioni dettagliate per:

* Registrare un account e accedere ai server
* Scaricare l’app in versione “antivirus-friendly” (“safe for installation”)
* Configurare correttamente l’NFC, con consigli specifici per ogni brand di smartphone
* Collegare i moduli Reader e Tapper tra loro
* Risolvere problemi di compatibilità tramite test guidati

Vengono inoltre promossi **server dedicati per clienti VIP**, funzionalità di backup cloud per i contatti, UID preconfigurati, supporto via Telegram e molto altro. Tutto ciò evidenzia come ci si trovi di fronte a un servizio strutturato, in continua evoluzione, che offre un’esperienza utente degna delle migliori app legittime. Il linguaggio adottato è spesso colloquiale, amichevole, e volto a fidelizzare l’utente criminale, con formule di benvenuto, offerte promozionali e rassicurazioni sulla protezione della privacy.

## ⚠️ Raccomandazioni per utenti finali

* **Non installare APK** ricevute via link, SMS o da numeri sconosciuti
* **Verificare sempre** l’identità di chi chiama la banca tramite canali ufficiali
* **Non condividere** il proprio numero di cellulare tramite moduli web non verificati
* **Contattare la propria banca** ai primi segnali sospetti

22 Aprile 2025/[1 Commento](https://www.d3lab.net/supercard-x-la...