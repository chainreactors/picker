---
title: Slopsquatting: quando le allucinazioni dell’AI diventano un attacco alla supply chain
url: https://www.ictsecuritymagazine.com/cyber-crime/slopsquatting-attacco-ai/
source: ICT Security Magazine
date: 2026-06-12
fetch_date: 2026-06-13T06:12:00.239128
---

# Slopsquatting: quando le allucinazioni dell’AI diventano un attacco alla supply chain

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

![Slopsquatting: un pacchetto software fantasma generato dall'AI come trappola nella catena di fornitura, illustrazione concettuale a toni caldi arancio e rosso.](https://www.ictsecuritymagazine.com/wp-content/uploads/2026-06-08_evergreen_slopsquatting.jpg)

# Slopsquatting: quando le allucinazioni dell’AI diventano un attacco alla supply chain

A cura di:[Redazione](#molongui-disabled-link)  Ore 12 Giugno 20268 Giugno 2026

Slopsquatting è il nome di una minaccia alla catena di fornitura del software nata insieme alla programmazione assistita dall’intelligenza artificiale: gli assistenti di codice suggeriscono talvolta pacchetti che non esistono, frutto di un’allucinazione del modello, e un attaccante può registrare quei nomi inventati nei repository pubblici riempiendoli di codice malevolo. Lo sviluppatore che si fida del suggerimento installa così, in piena buona fede, una libreria ostile. È un attacco che non sfrutta una vulnerabilità tecnica, ma la fiducia mal riposta nell’output di un modello.

## Che cos’è lo slopsquatting

Il termine slopsquatting è stato coniato da Seth Larson, developer-in-residence per la sicurezza della Python Software Foundation, combinando l’idea di slop, l’output di scarsa qualità generato dall’AI, con la logica dello squatting, l’occupazione di un nome altrui. La meccanica è semplice. Un assistente come quelli integrati negli editor di codice, interrogato su come svolgere un certo compito, raccomanda di installare un pacchetto da un registro pubblico come PyPI per Python o npm per JavaScript. Se quel pacchetto non esiste davvero, perché il modello lo ha inventato, il nome resta disponibile: chiunque può registrarlo. Un attaccante che conosca i nomi più frequentemente allucinati li occupa in anticipo con pacchetti che contengono codice dannoso, in attesa che qualcuno li installi seguendo il consiglio dell’AI.

La differenza rispetto agli attacchi più noti è sottile ma importante. Nel *typosquatting* l’attaccante registra varianti con errori di battitura di pacchetti reali e diffusi; nello slopsquatting, invece, occupa nomi del tutto inventati ma plausibili, che nessun controllo ortografico segnalerebbe perché non imitano nulla di esistente. È un bersaglio creato dal modello, non dall’errore umano.

## Quanto sono frequenti i pacchetti allucinati

Il fenomeno è stato quantificato da uno studio accademico presentato a USENIX Security 2025, intitolato We Have a Package for You! e condotto da ricercatori delle università del Texas a San Antonio, dell’Oklahoma e della Virginia Tech. Generando 576.000 campioni di codice con 16 modelli diversi in Python e JavaScript, i ricercatori hanno raccolto 2,23 milioni di pacchetti citati nelle risposte: di questi, il 19,7% (440.445) era inesistente, per un totale di 205.474 nomi di pacchetti fittizi unici, non presenti in alcun registro pubblico.

Il dato cambia molto a seconda del tipo di modello. I modelli commerciali si sono dimostrati più affidabili, con un tasso medio di allucinazione di almeno il 5,2% e con GPT-4 al 4,05%; i modelli open source hanno fatto molto peggio, con una media vicina al 21,7% e con alcune versioni di CodeLlama oltre il 33%. In altre parole, una porzione tutt’altro che marginale dei suggerimenti su quali librerie installare punta a qualcosa che non esiste, e quel vuoto è esattamente lo spazio che lo slopsquatting sfrutta.

Perché un modello inventa nomi di pacchetti? Perché genera testo statisticamente plausibile, non verificato: assembla nomi che somigliano a quelli reali, seguendo le convenzioni che ha visto in addestramento, senza alcun controllo sull’effettiva esistenza della libreria nel registro. Il risultato è spesso un nome verosimile, ben formato e coerente con il contesto, che proprio per questo lo sviluppatore tende a non mettere in dubbio. È la stessa qualità linguistica dell’output a renderlo pericoloso.

## Perché funziona: la persistenza delle allucinazioni

Se le allucinazioni fossero casuali e irripetibili, l’attacco sarebbe poco pratico: un attaccante non potrebbe sapere quali nomi occupare. Lo studio dimostra invece il contrario. Rieseguendo dieci volte gli stessi prompt, il 43% dei nomi di pacchetto allucinati ricompariva a ogni singola esecuzione e il 58% si ripeteva più di una volta. Le allucinazioni, quindi, non sono rumore imprevedibile: sono in larga misura artefatti stabili e prevedibili del modo in cui i modelli rispondono a certe richieste.

Questa prevedibilità è ciò che rende lo slopsquatting un attacco realistico e non teorico. Un avversario può generare in massa suggerimenti di codice, raccogliere i nomi inventati che il modello produce in modo ricorrente e registrarli preventivamente. Il rischio cresce con la diffusione del cosiddetto *vibe coding*, la pratica di accettare e incollare il codice proposto dall’AI senza una verifica puntuale: quanto più ci si fida del suggerimento, tanto più il nome fantasma diventa una porta aperta.

## Un caso reale: il pacchetto fantasma “huggingface-cli”

Che il rischio sia concreto lo ha dimostrato, già all’inizio del 2024, un esperimento del ricercatore Bar Lanyado di Lasso Security. Lanyado aveva notato che diversi modelli suggerivan...