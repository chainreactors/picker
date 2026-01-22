---
title: Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive
url: https://www.securityinfo.it/2026/01/21/sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive/?utm_source=rss&utm_medium=rss&utm_campaign=sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive
source: Securityinfo.it
date: 2026-01-21
fetch_date: 2026-01-22T03:36:26.716401
---

# Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive

Aggiornamenti recenti Gennaio 21st, 2026 3:19 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive](https://www.securityinfo.it/2026/01/21/sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive/)
* [StackWarp: scoperta una nuova vulnerabilità nei processori AMD](https://www.securityinfo.it/2026/01/20/stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd/)
* [CERT-AGID 10-16 gennaio: ancora phishing PagoPA e nuovi malware bancari](https://www.securityinfo.it/2026/01/19/cert-agid-10-16-gennaio-phishing-pagopa-malware-bancari/)
* [Il 64% delle app di terze parti accede a dati sensibili senza un motivo valido. La ricerca di Reflectiz](https://www.securityinfo.it/2026/01/16/il-64-delle-app-di-terze-parti-accede-a-dati-sensibili-senza-un-motivo-valido-la-ricerca-di-reflectiz/)
* [Microsoft smantella RedVDS, rete globale di cybercrime-as-a-service](https://www.securityinfo.it/2026/01/15/microsoft-smantella-redvds-rete-globale-di-cybercrime-as-a-service/)

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

## Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive

Gen 21, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Competizioni](https://www.securityinfo.it/category/news/competizioni/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/01/21/sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive/#respond)

---

Dopo l’[ultima edizione](https://www.securityinfo.it/2025/10/24/il-pwn2own-irlanda-si-e-concluso-con-oltre-1-milione-di-dollari-di-vincite/) tenutasi in Irlanda lo scorso ottobre, **il Pwn2Own è tornato nella veste Automotive**: tante squadre di hacker si sono sfidate nel cercare e sfruttare nuove vulnerabilità nel mondo dell’industria automobilistica.

Il [bilancio](https://www.zerodayinitiative.com/blog/2026/1/21/pwn2own-automotive-2026-day-one-results) della prima giornata di contest è ottimo: le squadre vincitrici hanno portato a casa, in totale, oltre 516.000 dollari per aver trovato **37 vulnerabilità zero-day**. La classifica attuale vede in testa il team **Fuzzware.io**, seguito in ordine da Team DDOS, Compass Security, Synacktiv, arrivato terzo allo scorso Pwn2Own, e PetoWorks.

![Pwn2Own Automotive](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_52d1ax52d1ax52d1.png)

Le **infrastrutture di ricarica** sono state quelle più “martellate” dagli hacker con exploit che hanno permesso non solo il controllo del dispositivo, ma anche la manipolazione del segnale di ricarica. Il team di Fuzzware.io ha messo a segno uno dei colpi più spettacolari riuscendo a concatenare due vulnerabilità (mancanza di autenticazione e verifica errata delle firme crittografiche) sull’Autel MaxiCharger, riuscendo a eseguire codice arbitrario e a manipolare il segnale di ricarica.

Grande successo anche per PetoWorks che ha utilizzato una catena di tre bug (un Denial of Service (DoS), una race condition e una command injection) contro il controller Phoenix Contact CHARX, ottenendo il controllo totale del segnale. Team DDOS ha colpito il ChargePoint Home Flex tramite una command injection, mentre SKShieldus (Team 299) ha sfruttato alcune credenziali cablate nel codice per ottenere l’esecuzione di codice sul Grizzl-E Smart.

Durante il Pwn2Own Automotive c’è stato un duro colpo per **Tesla**: Synacktiv è riuscito a concatenare un leak di informazioni e un out-of-bounds write per **compromettere il sistema di Infotainment di Tesla via USB**, guadagnando $35.000 e punti preziosi per aggiudicarsi il titolo di “Master of Pwn”.

Molti team si sono concentrati su unità aftermarket popolari come Alpine, Sony e Kenwood. Il team Neodyme AG ha aperto la giornata sfruttando uno stack-based buffer overflow sull’unità Alpine iLX-F511, mentre Synacktiv ha colpito il Sony XAV-9500ES, concatenando tre vulnerabilità per ottenere l’esecuzione di codice a livello root. Infine, il ricercatore Yannik Marchand ha sfruttato un out-of-bounds write per compromettere il Kenwood DNR1007XR.

La competizione durerà fino a venerdì 23 gennaio. Al termine della giornata, verrà incoronato il “Master of Pwn”, ovvero il team o ricercatore che avrà guadagnato complessivamente più punti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [colonnine ricarica](https://www.securityinfo.it/tag/colonnine-ricarica/), [competizione hacking](https://www.securityinfo.it/tag/competizione-hacking/), [macchine elettriche](https://www.securityinfo.it/tag/macchine-elettriche/), [Pwn2Own](https://www.securityinfo.it/tag/pwn2own/), [Pwn2Own automotive](https://www.securityinfo.it/tag/pwn2own-automotive/), [Tesla](https://www.securityinfo.it/tag/tesla/), [vulnerabilità zero-day](https://www.securityinfo.it/tag/vulnerabilita-zero-day/)

[StackWarp: scoperta una nuova vulnerabilità nei processori AMD](https://www.securityinfo.it/2026/01/20/stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Apple interviene su due zero-day sfruttati attivamente in attacchi mirati](https://www.securityinfo.it/wp-content/uploads/2025/12/MelaMorsicataeBuggata-120x85.png)](https://www.securityinfo.it/2025/12/12/apple-interviene-su-due-zero-day-sfruttati-attivamente-in-attacchi-mirati/ "Apple interviene su due zero-day sfruttati attivamente in attacchi mirati")

  [Apple interviene su due zero-day...](https://www.securityinfo.it/2025/12/12/apple-interviene-su-due-zero-day-sfruttati-attivamente-in-attacchi-mirati/ "Permanent link to Apple interviene su due zero-day sfruttati attivamente in attacchi mirati")

  Dic 12, 2025  [0](https://www.securityinfo.it/2025/12/12/apple-interviene-su-due-zero-day-sfruttati-attivamente-in-attacchi-mirati/#respond)
* [![Il Pwn2Own Irlanda si è concluso con oltre 1 milione di dollari di vincite](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_1fay4q1fay4q1fay-120x85.png)](https://www.securityinfo.it/2025/10/24/il-pwn2own-irlanda-si-e-concluso-con-oltre-1-milione-di-dollari-di-vincite/ "Il Pwn2Own Irlanda si è concluso con oltre 1 milione di dollari di vincite")

  [Il Pwn2Own Irlanda si è concluso con...](https://www.securityinfo.it/2025/10/24/il-pwn2own-irlanda-si-e-concluso-con-oltre-1-milione-di-dollari-di-vincite/ "Permanent link to Il Pwn2Own Irlanda si è concluso con oltre 1 milione di dollari di vincite")
...