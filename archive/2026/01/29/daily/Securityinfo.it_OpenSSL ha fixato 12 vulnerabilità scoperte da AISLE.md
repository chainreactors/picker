---
title: OpenSSL ha fixato 12 vulnerabilità scoperte da AISLE
url: https://www.securityinfo.it/2026/01/29/openssl-ha-fixato-12-vulnerabilita-scoperte-da-aisle/?utm_source=rss&utm_medium=rss&utm_campaign=openssl-ha-fixato-12-vulnerabilita-scoperte-da-aisle
source: Securityinfo.it
date: 2026-01-29
fetch_date: 2026-01-30T04:04:17.717355
---

# OpenSSL ha fixato 12 vulnerabilità scoperte da AISLE

Aggiornamenti recenti Gennaio 29th, 2026 4:20 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [OpenSSL ha fixato 12 vulnerabilità scoperte da AISLE](https://www.securityinfo.it/2026/01/29/openssl-ha-fixato-12-vulnerabilita-scoperte-da-aisle/)
* [PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/)
* [C’è Sandworm dietro l’attacco contro il settore energetico polacco](https://www.securityinfo.it/2026/01/26/ce-sandworm-dietro-lattacco-contro-il-settore-energetico-polacco/)
* [Zendesk, sfruttato il sistema di ticketing per una campagna di spam massiva](https://www.securityinfo.it/2026/01/23/zendesk-sfruttato-il-sistema-di-ticketing-per-una-campagna-di-spam-massiva/)
* [Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive](https://www.securityinfo.it/2026/01/21/sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive/)

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

## OpenSSL ha fixato 12 vulnerabilità scoperte da AISLE

Gen 29, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/01/29/openssl-ha-fixato-12-vulnerabilita-scoperte-da-aisle/#respond)

---

Pochi giorni fa **OpenSSL** [ha rilasciato](https://openssl-library.org/news/vulnerabilities/) alcune patch per risolvere **12 vulnerabilità** [individuate](https://aisle.com/blog/aisle-discovered-12-out-of-12-openssl-vulnerabilities), col supporto dell’IA, dalla compagnia di sicurezza AISLE.

“*L’analizzatore autonomo di AISLE ha individuato tutte e 12 le CVE nella versione coordinata di gennaio 2026 di OpenSSL, la libreria crittografica open source che è alla base di una parte consistente delle comunicazioni sicure a livello mondiale. **Alcune di queste vulnerabilità erano presenti nel codice OpenSSL da decenni** e sono riuscite a sfuggire all’attenzione di migliaia di ricercatori nel campo della sicurezza*” ha specificato il team della compagnia. Alcuni bug risalivano addirittura al 1998.

Le 12 vulnerabilità di OpenSSL sono presenti in più di otto sottosistemi diversi, tra cui CMS, QUIC e algoritmi di firma post-quantum. Tra i bug considerati più gravi c’è la CVE-2025-15467, uno **Stack Buffer Overflow** nell’analisi di dati CMS AuthEnvelopedData che consente l’**esecuzione di codice remoto.**

![OpenSSL vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_jc4om4jc4om4jc4o.png)

Il tool ha individuato anche una vulnerabilità di gravità moderata: la CVE-2025-11187 è una mancata validazione dei parametri PBMAC1 in PKCS#12 che potrebbe innescare un buffer overflow basato su stack.

Le altre dieci falle sono considerate di gravità bassa e possono abilitare attacchi di Denial of Service, corruzione della memoria, esaurimento delle risorse e sfruttamento di difetti di crittografia.

Oltre a queste 12 vulnerabilità, AISLE ha scoperto altre 6 criticità che però non hanno ricevuto una designazione CVE: grazie all’integrazione dell’analisi autonoma nei flussi di sviluppo, i bug sono stati rilevati e corretti prima che il codice vulnerabile venisse effettivamente rilasciato agli utenti.

Non appena il sistema automatizzato ha individuato i bug, AISLE ha collaborato a stretto contatto con OpenSSL per risolvere le vulnerabilità e rilasciare le patch il prima possibile.

Stanislav Fort, fondatore e Chief Scientist della compagnia di sicurezza, ha sottolineato che **l’uso di uno strumento potenziato dall’IA ha permesso di individuare più facilmente i bug**, rafforzando un processo che prima era quasi esclusivamente umano. “*I revisori umani sono limitati dal tempo, dall’attenzione e dall’enorme volume di codice nei sistemi moderni. L’analisi statica tradizionale rileva alcune classi di bug, ma ha difficoltà con errori logici complessi e problemi dipendenti dal tempo. Al contrario, l’analisi autonoma basata sull’intelligenza artificiale opera su una dimensione diversa. **È in grado di esaminare percorsi di codice e casi limite che richiederebbero mesi di lavoro ai revisori umani e funziona in modo continuo anziché periodico***” ha specificato Fort.

Si raccomanda agli utenti OpenSSL di aggiornarlo il prima possibile alla versione più recente.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AISLE](https://www.securityinfo.it/tag/aisle/), [analisi autonoma](https://www.securityinfo.it/tag/analisi-autonoma/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [OpenSSL](https://www.securityinfo.it/tag/openssl/), [stack buffer overflow](https://www.securityinfo.it/tag/stack-buffer-overflow/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene](https://www.securityinfo.it/wp-content/uploads/2026/01/ChatGPT-Image-27-gen-2026-17_26_31-120x85.png)](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/ "PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene")

  [PackageGate: trovati sei bug zero-day...](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/ "Permanent link to PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene")

  Gen 27, 2026  [0](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/#respond)
* [![Microsoft smantella RedVDS, rete globale di cybercrime-as-a-service](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_nhtguenhtguenhtg-120x85.png)](https://www.securityinfo.it/2026/01/15/microsoft-smantella-redvds-rete-globale-di-cybercrime-as-a-service/ "Microsoft smantella RedVDS, rete globale di cybercrime-as-a-service")

  [Microsoft smantella RedVDS, rete...](https://www.securityinfo.it/2026/01/15/microsoft-smantella-redvds-rete-globale-di-cybercrime-as-a-service/ "Permanent link to Microsoft smantella RedVDS, rete globale di cybe...