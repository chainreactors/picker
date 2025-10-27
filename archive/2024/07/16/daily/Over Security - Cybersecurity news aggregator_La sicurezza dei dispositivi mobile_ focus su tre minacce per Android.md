---
title: La sicurezza dei dispositivi mobile: focus su tre minacce per Android
url: https://www.telsy.com/la-sicurezza-dei-dispositivi-mobile-focus-su-tre-minacce-per-android/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-16
fetch_date: 2025-10-06T17:46:06.937591
---

# La sicurezza dei dispositivi mobile: focus su tre minacce per Android

* Gruppo TIM

[![Telsy](https://www.telsy.com/wp-content/themes/telsy/images/Logo-Telsy-TIM-blu.png)](https://www.telsy.com/)

[Per fare una ricerca scrivi qualcosa e premi "invio"](/?s=)

Chiudi

* [Chi siamo](https://www.telsy.com/chi-siamo/)
* Soluzioni
  + [Vai a Soluzioni](https://www.telsy.com/soluzioni/)
  + [Cyber](https://www.telsy.com/soluzioni/cyber-ita/)
  + [Crypto](https://www.telsy.com/soluzioni/crypto-ita/)
  + [Quantum](https://www.telsy.com/soluzioni/quantum-ita/)
* [Innovazione](https://www.telsy.com/innovazione/)
* [Lavora con noi](https://www.telsy.com/lavora-con-noi/)
* [Blog](https://www.telsy.com/blog/)

* News in evidenza
  + [06 Ott

    Attacchi rivolti a target italiani, notificati nuovi data breach, vulnerabilità sfruttate ITW](https://www.telsy.com/attacchi-rivolti-a-target-italiani-notificati-nuovi-data-breach-vulnerabilita-sfruttate-itw/)
  + [29 Set

    Le nuove minacce cyber realizzate col supporto dell’AI](https://www.telsy.com/le-nuove-minacce-cyber-realizzate-col-supporto-dellai/)

[Attacchi rivolti a target italiani, notificati nuovi data breach, vulnerabilità sfruttate ITW](https://www.telsy.com/attacchi-rivolti-a-target-italiani-notificati-nuovi-data-breach-vulnerabilita-sfruttate-itw/)
[Le nuove minacce cyber realizzate col supporto dell’AI](https://www.telsy.com/le-nuove-minacce-cyber-realizzate-col-supporto-dellai/)
[Vedi tutte](https://www.telsy.com/blog/)

* [English](https://www.telsy.com/en/mobile-device-security-focus-on-three-threats-to-android/)
* [Italiano](https://www.telsy.com/la-sicurezza-dei-dispositivi-mobile-focus-su-tre-minacce-per-android/)

[Cybersecurity](https://www.telsy.com/categoria/cybersecurity/)

# La sicurezza dei dispositivi mobile: focus su tre minacce per Android

15 Lug 2024

Condividi

**![Threat Discovery Telsy TS WAY Cyber Threat Intelligence](https://www.telsy.com/wp-content/uploads/2024/03/Threat-Discovery-Telsy-TS-WAY-Cyber-Threat-Intelligence.jpg)**

**Threat Discovery** è uno spazio editoriale di [Telsy](https://www.telsy.com/) e [TS-WAY](https://www.ts-way.com/it/) dedicato all’approfondimento in ambito cyber threat intelligence a livello globale.

Le informazioni riportate sono l’esito del lavoro di raccolta e analisi svolto dagli specialisti di TS-WAY per la piattaforma [TS-Intelligence](https://www.ts-way.com/it/threat-intelligence/).

In questo articolo presentiamo tre minacce specifiche per i sistemi Android che coniugano funzionalità multiple.

## SpyNote, uno spyware con feature di trojan bancario

SpyNote è una famiglia di malware per Android che nel corso del 2023 ha fatto segnare un drastico incremento dei tracciamenti e che nel 2024 ha mantenuto alto il livello di attività.

![La sicurezza dei dispositivi mobile focus su tre minacce per Android Telsy TS WAY bank](https://www.telsy.com/wp-content/uploads/La-sicurezza-dei-dispositivi-mobile-focus-su-tre-minacce-per-Android-Telsy-TS-WAY-bank.jpg)Le segnalazioni riguardano perlopiù codici malevoli derivati dalla variante CypherRat, che combina capacità spyware con funzionalità di [trojan bancario](https://www.telsy.com/i-trojan-bancari/). Il suo autore l’ha commercializzata tramite canali Telegram privati dall’agosto 2021 all’ottobre 2022. Poi, a seguito di una serie di episodi di truffa avvenuti in forum di hacking, ha deciso di rilasciare il sorgente su GitHub.

La possibilità di modificare il codice secondo le specifiche necessità dei singoli criminali e l’ampia gamma di funzioni hanno facilitato notevolmente la diffusione globale di SpyNote. In Italia, secondo alcune fonti, si sarebbe attestato come uno degli [spyware](https://www.telsy.com/gli-spyware/) più rilevati.

Fra le campagne tracciate a partire da agosto 2023, se ne segnala una che ha mirato ai clienti europei di diverse banche, sfruttando come vettore un’ondata di smishing. I target sono stati indotti con l’inganno a scaricare da Google Play Store un’app legittima TeamViewer QuickSupport, che sarebbe dovuta servire per il supporto tecnico e che è stata invece utilizzata per installare il RAT nei dispositivi.

Più di recente, SpyNote si è finto un’applicazione INPS Mobile, la quale poteva essere scaricata da una pagina web fraudolenta, progettata nei minimi dettagli per sembrare quella legittima dell’Istituto di previdenza sociale.

## Irata, un trojan bancario con capacità di spyware

Irata, il cui nome dovrebbe corrispondere all’acronimo di “Iranian remote access tool android”, è un trojan bancario per Android con capacità di spyware. Attivo almeno dal 2022, il malware è stato protagonista di diversi attacchi che hanno colpito anche in Italia.

In particolare, a gennaio 2024, sono state tracciate campagne che imitavano segnalazioni di istituti bancari come Mediobanca e CheBanca!. Si suppone che le vittime siano state raggiunte da SMS contenenti un URL dal quale viene effettuato il download di un APK malevolo.

Le informazioni che Irata può raccogliere comprendono le coordinate delle carte di credito e i token per l’autenticazione a due fattori (2FA). In aggiunta, può trasformare il dispositivo infettato in un bot per l’invio di ulteriori SMS e, quindi, per la propagazione della campagna. L’esfiltrazione dei dati avviene verso diversi canali Telegram appositamente creati.

Alcune analisi hanno portato a scoprire che l’avversario che distribuisce Irata dispone di un repository con file APK utilizzati per colpire gli utenti di BNL, del servizio di pagamento mobile spagnolo Bizum e della banca Caixa.

## Rafel RAT, tra cyberspionaggio e ransomware

Il tool open source per Android Rafel RAT supporta numerose attività malevole, dal controllo remoto, all’esfiltrazione di dati sensibili, credenziali e token di accesso. Ma una delle più utilizzate è quella ransomware.

Sfruttato in almeno 120 campagne globali, ha mietuto vittime principalmente negli Stati Uniti, in Cina e Indonesia. Inoltre, si segnalano infezioni in Italia, Francia, Germania e Russia. Fra le realtà impattate vi sono organizzazioni di alto profilo, alcune delle quali attive nel settore della Difesa.

![La sicurezza dei dispositivi mobile focus su tre minacce per Android Telsy TS WAY loghi](https://www.telsy.com/wp-content/uploads/La-sicurezza-dei-dispositivi-mobile-focus-su-tre-minacce-per-Android-Telsy-TS-WAY-loghi-scaled.jpg)

Nella maggior parte dei casi, Rafel RAT ha colpito dispositivi Samsung. In misura minore, si sono registrate violazioni di device Google (Pixel, Nexus), Xiaomi, Vivo, Huawei, LG, Motorola e OnePlus. Sebbene il malware sia risultato evidentemente più performante sulle versioni non più supportate del sistema operativo (in particolare, Android 5, 8 e 11), sono note infezioni di Android 12 e 13.

Gli attacchi a fini estorsivi possono essere svolti almeno in due modi. Una volta ottenuti i privilegi DeviceAdmin, Rafel RAT è in grado di impedire all’utente di revocargli i privilegi, impostando la schermata di blocco con una nuova password. In alternativa, può cifrare i file utilizzando l’algoritmo AES con una chiave predefinita, oppure può eliminare i file dalla memoria del dispositivo. La richiesta di riscatto viene visualizzata in un SMS, scritto in arabo e in inglese, che rimanda a un canale Telegram controllato dagli attaccanti.

Le campagne correlate a questa minaccia sono riconducibili a contesti molto eterogenei. Un’offensiva ransomware è stata gestita presumibilmente da attaccanti localizzati in Iran. Inoltre, una campagna hacktivista, rivendicata da un appartenente ad Anonymous Egypt che si firma LoaderCrazy, ha preso di mira un sito web governativo del Pakistan. Fra gli utilizzatori di Rafel RAT vi sarebbe, infine, anche l’APT indiano Dropping Elephant, che lo ha sfruttato insieme a molte altre minacce in una complessa campagna di cyberspionaggio.

## Telsy e TS-WAY

[![Telsy_TS WAY](https://www.telsy.com/wp-content/uploads/2023/09/Telsy_TS-WAY.jpg)](https://www.telsy.com/ts-way/)[TS-WAY](https://www.ts-way.com/it/) è un’azienda che sviluppa tecnologie e serv...