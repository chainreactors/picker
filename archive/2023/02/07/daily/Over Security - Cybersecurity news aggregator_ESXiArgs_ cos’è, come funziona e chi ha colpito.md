---
title: ESXiArgs: cos’è, come funziona e chi ha colpito
url: https://www.securityinfo.it/2023/02/06/esxiargs-cose-come-funziona-e-chi-ha-colpito/?utm_source=rss&utm_medium=rss&utm_campaign=esxiargs-cose-come-funziona-e-chi-ha-colpito
source: Over Security - Cybersecurity news aggregator
date: 2023-02-07
fetch_date: 2025-10-04T05:52:53.144115
---

# ESXiArgs: cos’è, come funziona e chi ha colpito

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## ESXiArgs: cos’è, come funziona e chi ha colpito

Feb 06, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Ransomware](https://www.securityinfo.it/category/minacce-2/ransomware/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/02/06/esxiargs-cose-come-funziona-e-chi-ha-colpito/#respond)

---

Questa mattina [abbiamo dato conto](https://www.securityinfo.it/2023/02/06/il-ransomware-esxiargs-spaventa-lopinione-pubblica/) del grande clamore suscitato dalla campagna ransomware denominata ESXiArgs, che ha coinvolto diverse migliaia di sistemi in tutto il mondo e ha **messo in allarme anche il nostro Governo.**

Con il passare delle ore sono emersi **ulteriori dettagli sulla portata dell’attacco e sul suo funzionamento**. Quando un server viene violato, alcuni file vengono aggiunti alla cartella /tmp, tra cui una chiave Rsa pubblica, un file binario del cifratore (un eseguibile Elf) e uno script di shell che svolge alcune operazioni preliminari prima di avviare la cifratura delle informazioni.

Lo script **interrompe l’esecuzione di tutte le macchine virtuali del sistema**, dopodiché effettua una ricerca per le estensioni associate alle unità disco virtuali della piattaforma VMware e infine esegue la cifratura.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/encryption-routing.png)

La porzione di script che cifra i file (Fonte: BleepingComputer)

Inoltre, alla cartella vengono anche aggiunti i file contenenti la richiesta di risarcimento che è apparsa in varie forme su tutti i siti di informazione. Il ricercatore di sicurezza Michael Gillespie ha analizzato il cifratore e l’ha ritenuto privo di falle**; non si può quindi sperare di sfruttare qualche bug per decifrare le informazioni** prese in ostaggio.

Alcune caratteristiche del malware, come per esempio l’uso dell’algoritmo [Sosemanuk](https://it.wikipedia.org/wiki/SOSEMANUK), non sono molto comuni e lasciano supporre che **ESXiArgs sia probabilmente basato sul codice sorgente del ransomware Babuk**, che era stato reso pubblico nel 2021 ed è stato utilizzato in passato in altre campagne ransomware ESXi.

Rispetto al passato ci sono però anche **diversi tratti di originalità, come la scelta della crittografia Rsa**, che lasciano aperta la porta a diverse interpretazioni sulla discendenza diretta da Babuk.

## Le vittime

Come abbiamo già accennato, i sistemi colpiti dalla campagna sono state diverse migliaia; il conteggio di Censys indicava oltre 3.200 server compromessi soltanto questa mattina (6 febbraio), ma **il numero sta progressivamente scendendo** man mano che i tecnici procedono nell’opera di ripristino.

Dopo la riunione coordinata dal Sottosegretario con la delega alla Cybersecurity Alfredo Mantovano, con i vertici della ACN-Agenzia per la Cybersicurezza Nazionale e del Dipartimento delle informazioni per la sicurezza, Palazzo Chigi ha emesso [una nota](https://www.governo.it/it/articolo/attacco-informatico-riunione-palazzo-chigi/21715) che delinea con più chiarezza i contorni del problema, **confermando in sostanza le informazioni già trapelate** nelle ultime ore.

La nota infatti riporta che “in Italia **nessuna Istituzione o azienda primaria che opera in settori critici per la sicurezza nazionale è stata colpita**. Nel corso delle prime attività ricognitive compiute da ACN-Agenzia per la Cybersicurezza Nazionale, unitamente alla Polizia Postale, non sono emerse evidenze che riconducano ad aggressione da parte di un soggetto statale o assimilabile a uno Stato ostile; è invece probabile l’azione di criminali informatici, che richiedono il pagamento di un riscatto”.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/FoJCFAdWAAAm4hz-scaled.jpg)

Fonte: @mRr3b00t su Twitter

Sono anche state divulgate, per esempio da [mRr3b00t](https://twitter.com/UK_Daniel_Card) su Twitter, alcune interessanti mappe che dettagliano **la distribuzione geografica dei sistemi interessati** dall’attacco, sia a livello globale sia concentrando l’attenzione sul territorio europeo.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/FoJEyaNXgAAOMiR-scaled.jpg)

Fonte: @mRr3b00t su Twitter

Segnaliamo infine la pubblicazione di una [guida molto dettagliata](https://enes.dev/) al ripristino dei sistemi colpiti, realizzata da Enes Sonmez e Ahmet Aykac del YoreGroup Tech Team, che offre molte **informazioni preziose sui passi da compiere per mettere in sicurezza i server interessati** dall’attacco.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [ESXi](https://www.securityinfo.it/tag/esxi/), [ESXiArgs](https://www.securityinfo.it/tag/esxiargs/), [Ransomware](https://www.securityinfo.it/tag/ransomware/)

[Crowdsourcing per la cybersecurity: più protezione e costi aziendali ridotti](https://www.securityinfo.it/2023/02/07/crowdsourcing-cybersecurity-protezione-costi/)
[File OneNote per distribuire malware: individuate decine di campagne attive](https://www.securityinfo.it/2023/02/06/file-onenote-campagne-malware/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vi...