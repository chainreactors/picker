---
title: TEE.Fail, l’attacco che accede all’ambiente di esecuzione delle CPU
url: https://www.securityinfo.it/2025/10/30/tee-fail-lattacco-che-accede-allambiente-di-esecuzione-delle-cpu/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-30
fetch_date: 2025-10-31T03:14:28.827536
---

# TEE.Fail, l’attacco che accede all’ambiente di esecuzione delle CPU

Aggiornamenti recenti Ottobre 30th, 2025 12:51 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [TEE.Fail, l’attacco che accede all’ambiente di esecuzione delle CPU](https://www.securityinfo.it/2025/10/30/tee-fail-lattacco-che-accede-allambiente-di-esecuzione-delle-cpu/)
* [Atlas, browser basato su ChatGPT, consente l’injection di comandi malevoli](https://www.securityinfo.it/2025/10/29/atlas-browser-basato-su-chatgpt-consente-linjection-di-comandi-malevoli/)
* [I cyberattacchi al governo U.S.A. sono quasi raddoppiati dopo lo “shutdown”](https://www.securityinfo.it/2025/10/28/i-cyberattacchi-al-governo-u-s-a-sono-quasi-raddoppiati-dopo-lo-shutdown/)
* [Dante, lo spyware italiano usato in campagne di cyberspionaggio](https://www.securityinfo.it/2025/10/27/dante-lo-spyware-italiano-usato-in-attacchi-di-cyberspionaggio/)
* [CERT-AGID 18–24 ottobre: phishing a tema PagoPA e Fascicolo Sanitario](https://www.securityinfo.it/2025/10/27/cert-agid-18-24-ottobre-phishing-pagopa-fascicolo-sanitario/)

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

## TEE.Fail, l’attacco che accede all’ambiente di esecuzione delle CPU

Ott 30, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/10/30/tee-fail-lattacco-che-accede-allambiente-di-esecuzione-delle-cpu/#respond)

---

Un gruppo di ricercatori della Gerogia Tech University e della Purdue University [ha illustrato](https://tee.fail/) un **attacco side-channel soprannominato “TEE.Fail”**che permette di estrarre secret dal Trusted Execution Environment delle CPU.

Il Trusted Execution Environment (TEE) è un’area isolata del processore usata per proteggere l’integrità e la confidenzialità di codice e dati, bloccando gli accessi non autorizzati sia in lettura che scrittura. Nonostante questo tipo di protezioni, però, **i ricercatori sono riusciti a eludere i controlli fisici per intercettare il traffico della RAM DDR5.**

“*Gli attacchi side-channel si sono evoluti da una forma tradizionale che richiede strumentazione costosa a metodi moderni che usano il software per inferire l’informazione confidenziale dalla sua modalità di accesso ottenuta attraverso gli stati della microarchitettura*” spiegano i ricercatori. **“*L’architettura TEE fornire solo un meccanismo di isolamento e non resiste a questi tipi di attacco side-channel emergenti basati su software*“**.

![TEE.Fail](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_o4qma6o4qma6o4qm.png)

Come [illustrato](https://www.bleepingcomputer.com/news/security/teefail-attack-breaks-confidential-computing-on-intel-amd-nvidia-cpus/) da Bleeping Computer, TEE.Fail richiede accesso fisico al dispositivo e privilegi di root per la modifica del driver Kernel, ma non servono elevate conoscenze tecniche. I ricercatori sono riusciti a intercettare le informazioni usando componenti di commodity, spendendo un totale di meno di 1000 dollari.

Il team è riuscito a sfruttare una vulnerabilità nel modo in cui Intel e AMD implementano la gestione della cifratura della memoria: entrambe utilizzano delle tecniche di cifratura deterministiche che consentono quindi di inferire le informazioni crittografate. Di fatto, **poiché la cifratura di uno stesso dato dà sempre lo stesso output, i ricercatori sono riusciti a creare un cifrario per il mapping dei valori.**

Anche se gli accessi alle strutture dati sono cifrati, i pattern con cui avvengono, ovvero gli indirizzi usati e in quale sequenza, possono essere inferiti; ciò rappresenta una fuga di informazioni. Analizzando i pattern, **un attaccante può recuperare le cifre del nonce** (Number used once) usato per la firma digitale.

Avendo questa informazione, è possibile **ricostruire la chiave privata della firma**. Ottenere questa chiave significa riuscire a generare *attestati* validi usati dal TEE per garantire l’integrità del codice. L’attacco è stato eseguito con successo sia su sistemi Intel SGX/TDX che AMD SEV-SNP.

La redazione di Bleeping Computer ha contattato AMD e Intel per un commento sulla ricerca del team, ma non hanno ottenuto risposta. Ieri **AMD** [ha pubblicato](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3040.html) un comunicato in cui ha affermato che non prevede di gestire mitigazioni per il problema in quanto si tratta di un attacco che richiede l’accesso fisico al dispositivo, un vettore d’azione out-of-scope.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AMD](https://www.securityinfo.it/tag/amd/), [cifratura](https://www.securityinfo.it/tag/cifratura/), [CPU](https://www.securityinfo.it/tag/cpu/), [Intel](https://www.securityinfo.it/tag/intel/), [RAM DDR5](https://www.securityinfo.it/tag/ram-ddr5/), [TEE](https://www.securityinfo.it/tag/tee/), [TEE.fail](https://www.securityinfo.it/tag/tee-fail/)

[Atlas, browser basato su ChatGPT, consente l'injection di comandi malevoli](https://www.securityinfo.it/2025/10/29/atlas-browser-basato-su-chatgpt-consente-linjection-di-comandi-malevoli/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  [Cina contro Nvidia: dubbi sulla...](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Permanent link to Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  Ago 13, 2025  [0](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/#respond)
* [![Ransomware che infettano la CPU: una nuova, potenziale minaccia](https://www.securityinfo.it/wp-content/uploads/2025/05/2151883593-120x85.jpg)](https://www.securityinfo.it/2025/05/13/ransomware-che-infettano-la-cpu-una-nuova-potenziale-minaccia/ "Ransomware che infettano la CPU: una nuova, potenziale minaccia")

  [Ransomware che infettano la CPU: una...](https://www.securityinfo.it/2025/05/13/ransomware-che-infettano-la-cpu-una-nuova-potenziale-...