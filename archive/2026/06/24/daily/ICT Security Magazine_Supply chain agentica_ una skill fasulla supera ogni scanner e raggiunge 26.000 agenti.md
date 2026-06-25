---
title: Supply chain agentica: una skill fasulla supera ogni scanner e raggiunge 26.000 agenti
url: https://www.ictsecuritymagazine.com/notizie/supply-chain-agentica-skill-ai-malevola/
source: ICT Security Magazine
date: 2026-06-24
fetch_date: 2026-06-25T06:10:20.903044
---

# Supply chain agentica: una skill fasulla supera ogni scanner e raggiunge 26.000 agenti

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

![supply chain agentica](https://www.ictsecuritymagazine.com/wp-content/uploads/supply-chain-agentica.png)

# Supply chain agentica: una skill fasulla supera ogni scanner e raggiunge 26.000 agenti

A cura di:[Redazione](#molongui-disabled-link)  Ore 24 Giugno 202624 Giugno 2026

*Una skill malevola per agenti AI, costruita in meno di un’ora, ha superato ogni scanner messo alla prova sfruttando un link esterno modificato dopo la verifica. La dimostrazione di una società di sicurezza espone un punto cieco strutturale nella supply chain agentica, con il giusto distinguo sui numeri auto-riportati dal vendor.*

La supply chain agentica mostra il suo primo punto cieco: una società di sicurezza ha costruito in meno di un’ora una *skill* malevola per agenti AI, l’ha diffusa attraverso un *marketplace* pubblico e un annuncio su Instagram e dichiara di aver raggiunto circa 26.000 agenti, alcuni su account aziendali. Ogni *scanner* per *skill* messo alla prova l’ha giudicata sicura. La dimostrazione, firmata [dalla ricerca di AIR,](https://www.air.security/blog-posts/the-story-of-skills) espone un punto cieco strutturale nel modo in cui oggi si valuta la fiducia verso i componenti che gli agenti caricano nel proprio contesto.

## Come è stata costruita

Una *skill* è un pacchetto di istruzioni che l’agente carica nel proprio contesto e segue con un’autorità paragonabile a quella di un *prompt* dell’utente. È proprio questa fiducia il problema. Il pacchetto, chiamato *brand-landingpage*, prometteva la creazione di una *landing page* tramite lo strumento di design Stitch di Google, rivolgendosi a un pubblico non tecnico di professionisti del marketing, delle vendite e della grafica.

Per apparire credibile, AIR ha lavorato su due segnali di fiducia. Il primo: le stelle di GitHub. Ha aperto una *pull request* verso il repository di un *marketplace* di componenti con circa 36.000 stelle e 156 *skill*; una volta accettata la modifica, la *skill* ha ereditato quel patrimonio di credibilità. Il secondo: un verdetto pulito degli *scanner*. Ha poi diffuso il pacchetto con un annuncio su Instagram, e gli utenti hanno iniziato a installarlo e a usarlo.

## Perché gli scanner non hanno visto nulla

Gli *scanner* analizzano ciò che viene consegnato loro: il file di descrizione della *skill* e le risorse incluse nel pacchetto. AIR ha sfruttato esattamente ciò che resta fuori da quel perimetro. La *skill* non conteneva istruzioni di installazione proprie: rimandava l’agente a una documentazione esterna ospitata su *stitch-design.ai*, un dominio controllato da AIR e non da Google (il vero Stitch risiede su *stitch.withgoogle.com*).

Inizialmente quel link puntava alla documentazione autentica, così gli *scanner* di Cisco e NVIDIA e quelli integrati in skills.sh, vedendo un pacchetto pulito che rimandava a una pagina di *setup* plausibile, lo hanno approvato. Una volta diffusa l’installazione, AIR ha riscritto la pagina dietro quel link, istruendo l’agente a scaricare ed eseguire uno script. Nella dimostrazione il *payload* si limitava a inviare l’indirizzo email della vittima, ma un attore reale avrebbe potuto leggere file, spostare dati o raggiungere sistemi interni, nei limiti di ciò a cui l’agente poteva accedere.

Il difetto è di progettazione: la verifica avviene una volta sola, su un’istantanea del pacchetto, mentre la pagina a cui la *skill* rimanda può essere cambiata in qualunque momento dopo il controllo. Non è una scoperta isolata. Circa tre settimane prima, Trail of Bits aveva [aggirato](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/) il rilevatore di ClawHub, lo [scanner di Cisco](https://github.com/cisco-ai-defense/skill-scanner) e tutti quelli integrati in skills.sh; la stessa [documentazione di Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) avverte da tempo che le *skill* che recuperano URL esterni sono rischiose, perché il contenuto può cambiare dopo la verifica.

## Difendere la supply chain agentica

I numeri vanno letti con prudenza. La cifra dei 26.000 agenti, il dettaglio sugli account aziendali e l’affermazione di aver potuto assumere il controllo completo provengono da AIR, che chiude la ricerca presentando il proprio *marketplace* gestito di *skill*: c’è un interesse commerciale dichiarato e i dati non sono verificati in modo indipendente. Quel che regge, e che vale per ogni redazione tecnica e per ogni CISO, è il metodo: gli *scanner* citati giudicano solo il pacchetto consegnato, il punto cieco dei link esterni è reale ed è già stato dimostrato da terzi, e i segnali su cui l’ecosistema ancora si appoggia, stelle e scansione pulita, sono esattamente quelli che la dimostrazione ha piegato.

La lezione operativa è diretta: trattare le *skill* come software, non come testo. Verificare ciò a cui una *skill* rimanda, non solo ciò che contiene; instradare i componenti attraverso un’unica fonte controllata e ricontrollarli a ogni modifica; fissare le versioni, applicare il privilegio minimo e assumere che qualunque istruzione esterna recuperata da un agente venga eseguita con i suoi permessi. È la stessa logica di [supply chain che i...