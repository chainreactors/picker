---
title: Grave vulnerabilità nei chip Bluetooth Airoha: molti i marchi colpiti
url: https://www.securityinfo.it/2026/01/05/grave-vulnerabilita-nei-chip-bluetooth-airoha-molti-i-marchi-colpiti/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-05
fetch_date: 2026-01-06T03:28:05.771773
---

# Grave vulnerabilità nei chip Bluetooth Airoha: molti i marchi colpiti

Aggiornamenti recenti Gennaio 5th, 2026 2:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Nel 2026 sempre più attacchi autonomi AI-driven e deepfake: le previsioni di sicurezza di ClearSkies](https://www.securityinfo.it/2026/01/05/nel-2026-sempre-piu-attacchi-autonomi-ai-driven-e-deepfake-le-previsioni-di-sicurezza-di-clearskies/)
* [Grave vulnerabilità nei chip Bluetooth Airoha: molti i marchi colpiti](https://www.securityinfo.it/2026/01/05/grave-vulnerabilita-nei-chip-bluetooth-airoha-molti-i-marchi-colpiti/)
* [Kaspersky: così funziona il mercato del lavoro nel dark web](https://www.securityinfo.it/2025/12/23/kaspersky-cosi-funziona-il-mercato-del-lavoro-nel-dark-web/)
* [Kaspersky: il cybercrime finanziario ha alzato il livello nel 2025](https://www.securityinfo.it/2025/12/22/kaspersky-lancia-lallarme-il-cybercrime-finanziario-ha-alza-il-livello-nel-2025/)
* [CERT-AGID 13-19 dicembre: phishing PagoPA e smishing INPS](https://www.securityinfo.it/2025/12/22/cert-agid-13-19-dicembre-phishing-pagopa-e-smishing-inps/)

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

## Grave vulnerabilità nei chip Bluetooth Airoha: molti i marchi colpiti

Gen 05, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/01/05/grave-vulnerabilita-nei-chip-bluetooth-airoha-molti-i-marchi-colpiti/#respond)

---

Il Bluetooth è di nuovo al centro di una grave vulnerabilità che permette agli attaccanti di assumere il controllo degli smartphone o tablet connessi e che colpisce cuffie, auricolari True Wireless Stereo (TWS) ed altri dispositivi audio consumer basati su chipset Bluetooth prodotti da Airoha Systems. In realtà, si tratta di una serie di vulnerabilità catalogate come CVE-2025-20700, CVE-2025-20701 e CVE-2025-20702 che hanno ricevuto valutazioni **CVSS** dall’8.8 al 9.6, configurandosi come **bug di alta o critica gravità** per l’infrastruttura di comunicazione tra dispositivi smartphone e periferiche audio.

![](https://www.securityinfo.it/wp-content/uploads/2026/01/aperturaBluetooth.jpg)

A differenza di molti attacchi Bluetooth del passato, dove la compromissione richiedeva procedure di pairing fallaci o interazione utente, queste vulnerabilità permettono l’inizio di connessioni non autenticate sfruttando specifiche implementazioni del protocollo RACE (Remote Access Control Engine), un motore di controllo remoto originariamente concepito per attività di **debugging di fabbrica** e aggiornamenti firmware. L’esposizione di tale protocollo su interfacce quali **Bluetooth Low Energy (BLE)**, **Bluetooth Classic** e **USB HID** senza adeguata autenticazione di accesso permette compromissioni senza alcuna interazione da parte dell’utente.

**Analisi dei difetti: RACE e autenticazione mancante**

Le vulnerabilità fondamentali risiedono nella mancanza di controlli di autenticazione su servizi GATT (Generic Attribute Profile) quando si operano connessioni via **BLE**, così come nelle classiche connessioni Bluetooth tradizionali. La prima, tracciata come CVE-2025-20700, riguarda servizi essenziali che dovrebbero essere soggetti a restrizioni d’accesso in base al contesto di pairing, ma che in queste implementazioni sono esposti senza alcuna barriera logica, consentendo a un attaccante di instaurare una sessione con il dispositivo bersaglio a patto di trovarsi nel raggio di comunicazione radio.

Nel caso di connessioni Classic (CVE-2025-20701), l’assenza di autenticazione non solo permette l’accesso alla memoria di controllo, ma abilita anche la possibilità di sfruttare profili come **Hands-Free Profile (HFP)** per instaurare connessioni audio bidirezionali senza consenso dell’utente. Tale condizione può essere abusata per attivare microfoni remoti o manipolare funzionalità legate alla gestione delle chiamate, trasformando qualsiasi dispositivo vulnerabile in una radiospia.

La vulnerabilità più grave è però connessa direttamente all’architettura del protocollo RACE (CVE-2025-20702). Le operazioni esposte tramite questo meccanismo consentono la lettura di porzioni arbitrarie della **flash e della RAM** del dispositivo, insieme alla possibilità di eseguire comandi che interrogano o modificano lo stato critico dei componenti interni. Tali azioni consentono ad attaccanti di estrarre informazioni sensibili come chiavi crittografiche di collegamento (**Link Key**), indirizzi Bluetooth Classic ed elementi configurazionali leggibili da memoria non protetta.

**Catena d’attacco: dalla periferica audio allo smartphone compromesso**

Il reale pericolo non si limita alla compromissione isolata del dispositivo audio. La catena di attacco tecnica illustrata dai ricercatori mostra come sia possibile sfruttare questi difetti per trasferire l’impiego delle credenziali di sicurezza verso il dispositivo host (tipicamente uno smartphone). Dopo aver lette le tabelle di connessione memorizzate nella periferica, che includono le **chiavi di link crittografiche** utilizzate per l’autenticazione reciproca, un attaccante può impersonare la cuffia compromessa nei confronti del telefono bersaglio.

**Una volta stabilita tale connessione privilegiata, l’attaccante può eseguire una varietà di operazioni sul telefono: dall’estrazione di informazioni sensibili come numeri di telefono e liste contatti fino all’attivazione di assistenti vocali per l’invio di messaggi o l’inizio di chiamate senza autorizzazione esplicita nonché la lettura di messaggi in entrata. Grazie a queste “funzioni aggiuntive”, i ricercatori sono riusciti a compromettere account di servizi come WhatsApp e Amazon**.

**Contesto di utilizzo reale e impatto industriale**

I chipset Airoha Systems sono largamente utilizzati in modelli di cuffie e auricolari prodotti da marchi noti nel mercato consumer audio: tra i dispositivi confermati vulnerabili figurano vari modelli delle serie Sony WH e WF, Bose QuietComfort Earbuds, JBL Live Buds 3, Marshall MAJOR V e MINOR IV, così come altri prodotti marchiati Beyerdynamic, Jabra e Teufel. La larga diffusione di questi modelli e l’adozione ampia delle piattaforme SoC Airoha pongono potenziali rischi su scala molto ampia, dato che firmware correttivi non sono ancora stati uniformemente diffusi dai vendor al momento dell’analisi e quando questo è stato fatto, resta da vedere quanti utenti aggiorneranno le proprie cuffie (una operazione a cui nessuno pensa).

In diversi casi i produttori hanno rilasciato aggiornamenti firmware per affrontare alcune delle criticità, ma la disponibilità, la trasparenza e l’effettiva applicazione di tali correzioni mostrano una notevole variabilità tra le aziende. Alcune, come Jabra, hanno a...