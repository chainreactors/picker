---
title: Mobile application security: l’app gira in casa del nemico
url: https://www.ictsecuritymagazine.com/cyber-security/mobile-application-security/
source: ICT Security Magazine
date: 2026-06-28
fetch_date: 2026-06-29T06:34:35.951147
---

# Mobile application security: l’app gira in casa del nemico

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

![Mobile application security](https://www.ictsecuritymagazine.com/wp-content/uploads/Mobile-application-security.png)

# Mobile application security: l’app gira in casa del nemico

A cura di:[Redazione](#molongui-disabled-link)  Ore 28 Giugno 20269 Giugno 2026

Mobile application security è la sicurezza di un tipo di software che ha una caratteristica unica e spesso rimossa: gira su un dispositivo che chi lo sviluppa non controlla, e che in molti casi è proprio nelle mani di chi vorrebbe attaccarlo. Il codice di un server vive in un data center sorvegliato; un’app mobile vive su un telefono che può essere modificato per ottenere privilegi di amministratore, ispezionato mentre è in esecuzione, decompilato per leggerne l’interno, e il cui archivio locale può essere estratto. È una differenza che cambia tutto, perché ribalta l’assunzione di base su cui poggia gran parte della sicurezza applicativa.

Il peccato originale, in questo campo, è trattare l’app mobile come un client fidato. È l’errore di chi ragiona come per il web, dove il browser dialoga con un server che resta il custode della logica e dei segreti. Sul mobile non funziona così: tutto ciò che finisce dentro l’app, una chiave, una credenziale, una porzione di logica sensibile, è alla portata di chi possiede il dispositivo. La mobile application security parte da qui, dall’accettare che l’ambiente in cui l’app gira è ostile e che il client, a differenza del server, può essere in mano al nemico.

## Il client è in mano al nemico

Conviene rendere concreta questa ostilità, perché è ciò che distingue il mobile dal resto. Un dispositivo con privilegi di amministratore ottenuti tramite *rooting* o *jailbreak* permette al suo possessore di aggirare le protezioni del sistema operativo e di leggere ciò che le app credono protetto. Strumenti di *instrumentation* consentono di osservare e manipolare un’app mentre gira, intercettandone le funzioni e i valori in memoria. La decompilazione apre il codice all’analisi, rivelando segreti incorporati e logiche che si pensavano nascoste. E il traffico verso i server può essere intercettato da chi controlla la rete o il dispositivo.

La conseguenza pratica è una serie di errori ricorrenti che derivano tutti dalla stessa illusione di fiducia. Conservare dati sensibili nell’archivio locale come se fosse al sicuro è il problema più comune e più grave del mobile, perché quei dati si possono estrarre. Incastonare chiavi crittografiche o segreti nel binario dell’app, nella convinzione che nessuno li troverà, è un altro classico, smentito dalla prima decompilazione. Affidarsi alla rete senza verificare l’identità del server espone all’intercettazione. Ognuno di questi errori nasce dal dare per scontato un controllo sull’ambiente che, sul mobile, semplicemente non si ha.

## OWASP MASVS: lo standard che assume il peggio

A dare ordine a questo terreno c’è uno standard diventato il riferimento di settore, l’OWASP [Mobile Application Security Verification Standard](https://mas.owasp.org/MASVS/), noto come MASVS, affiancato da una guida ai test, il MASTG, che spiega come verificarlo nella pratica. Il valore del MASVS è che non finge che il dispositivo sia fidato: organizza la sicurezza dell’app in gruppi di controlli, ciascuno dei quali affronta un modo in cui l’assunzione dell’ambiente ostile si traduce in rischio concreto.

Nella versione 2.1.0, pubblicata nel gennaio 2024, i gruppi sono otto. Riguardano la conservazione sicura dei dati sul dispositivo, l’uso corretto della crittografia, l’autenticazione e l’autorizzazione, la sicurezza delle comunicazioni di rete, l’interazione sicura con la piattaforma mobile, la qualità del codice, la resistenza alla manomissione e all’analisi inversa, e infine la privacy, gruppo aggiunto proprio nel 2024 a riconoscere quanto privacy e sicurezza siano ormai inseparabili. È un quadro che copre l’app dal dato che custodisce fino al modo in cui parla con il mondo, e che si appoggia a pratiche di [secure coding](https://www.ictsecuritymagazine.com/articoli/secure-coding/) e ai meccanismi di autenticazione, inclusi quelli biometrici, che il sistema operativo mette a disposizione.

## Mobile application security e il caso speciale della resilienza

Tra gli otto gruppi ce n’è uno che merita un discorso a parte, perché è il più frainteso: la resistenza alla manomissione e all’analisi inversa, la [resilienza](https://mas.owasp.org/checklists/MASVS-RESILIENCE/) nel linguaggio del MASVS. Sono le protezioni che rendono più difficile decompilare un’app, individuarne i punti deboli o modificarla: offuscamento del codice, rilevamento del *rooting*, difese contro l’instrumentation. Per certe categorie di applicazioni, quelle bancarie, dei pagamenti, della gestione di contenuti protetti, alzare questa barriera ha senso, perché aumenta il costo e il tempo necessari a un attaccante mirato.

Qui però si annida un equivoco da evitare. La resilienza è una difesa in profondità, non un sostituto delle altre. Offuscare il codice e ostacolare l’analisi rallenta chi attacca, non lo ferma: un avversario determinato e con tempo a disposizione supera comunque queste barriere. Confondere il rendere un’app diff...