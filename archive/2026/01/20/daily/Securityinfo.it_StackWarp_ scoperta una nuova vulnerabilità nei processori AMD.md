---
title: StackWarp: scoperta una nuova vulnerabilità nei processori AMD
url: https://www.securityinfo.it/2026/01/20/stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd/?utm_source=rss&utm_medium=rss&utm_campaign=stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd
source: Securityinfo.it
date: 2026-01-20
fetch_date: 2026-01-21T03:32:52.540008
---

# StackWarp: scoperta una nuova vulnerabilità nei processori AMD

Aggiornamenti recenti Gennaio 20th, 2026 3:47 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [StackWarp: scoperta una nuova vulnerabilità nei processori AMD](https://www.securityinfo.it/2026/01/20/stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd/)
* [CERT-AGID 10-16 gennaio: ancora phishing PagoPA e nuovi malware bancari](https://www.securityinfo.it/2026/01/19/cert-agid-10-16-gennaio-phishing-pagopa-malware-bancari/)
* [Il 64% delle app di terze parti accede a dati sensibili senza un motivo valido. La ricerca di Reflectiz](https://www.securityinfo.it/2026/01/16/il-64-delle-app-di-terze-parti-accede-a-dati-sensibili-senza-un-motivo-valido-la-ricerca-di-reflectiz/)
* [Microsoft smantella RedVDS, rete globale di cybercrime-as-a-service](https://www.securityinfo.it/2026/01/15/microsoft-smantella-redvds-rete-globale-di-cybercrime-as-a-service/)
* [“Truman Show”: la truffa finanziaria che crea una realtà sintetica per ingannare le vittime](https://www.securityinfo.it/2026/01/14/truman-show-la-truffa-finanziaria-che-crea-una-realta-sintetica-per-ingannare-le-vittime/)

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

## StackWarp: scoperta una nuova vulnerabilità nei processori AMD

Gen 20, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/01/20/stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd/#respond)

---

I ricercatori del CISPA Helmholtz Center for Information Security hanno scoperto **StackWarp**, **una nuova vulnerabilità hardware che colpisce i processori AMD**di tutte le generazioni.

Nel [paper](https://stackwarpattack.com/stackwarp_usenix26.pdf) relativo alla scoperta i ricercatori spiegano che il bug consente di **manipolare in modo deterministico lo stack pointer all’interno delle Confidential Virtual Machines** alterando di fatto la garanzie di integrità di SEV-SNP (Secure Encrypted Virtualization – Secure Nested Paging).

A differenza di vulnerabilità già note che si concentrava sulla gerarchia della memoria o sulle unità di esecuzione, StackWarp sfrutta un difetto nello stack engine, il componente che si occupa di ottimizzare la gestione dello stack pointer, presente nell’esecuzione di operazioni comuni quali push, pop, call e ret.

![StackWarp](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_899w6k899w6k899w.png)

Per evitare di appesantire le unità logiche generali, l’engine traccia internamente gli spostamenti dello stack pointer. I ricercatori hanno scoperto che esiste però un **bit non documentato che consente di abilitare o disabilitare l’engine**: poiché lo stato del registro mantenuto dal motore non viene sincronizzato tra i *sibling logical cores* (unità di elaborazione logica che derivano da un singolo core fisico della CPU), un attaccante può agire su uno dei thread per disattivare il motore dello stack mentre l’altro thread, in esecuzione sull’altro core logico, sta processando istruzioni dello stack.

Ciò provoca un congelamento del delta accumulato nel registro: la CPU continua a eseguire istruzioni, ma l’aggiornamento dello stack pointer viene sospeso e rilasciato successivamente in un unico passaggio, quando il motore viene riabilitato. Un attaccante può eseguire uno **spostamento dello stack pointer fino a 640 byte**, agendo con precisione chirurgica a livello di singola istruzione senza la necessità di iniettare interrupt o leggere la memoria cifrata.

Il team di ricerca ha documentato **quattro scenari di attacco reali condotti su processori AMD di ultima generazione**. Nel primo caso, sono riusciti a recuperare una chiave privata RSA-2048 inducendo un errore preciso in una firma digitale, mentre in un secondo scenario sono riusciti a bypassare l’autenticazione tramite password di OpenSSH manipolando il valore di ritorno delle funzioni di controllo.

Un terzo exploit ha mostrato come ottenere privilegi di root tramite il comando *sudo*, alterando i dati dello stack durante la chiamata di sistema getuid. Infine, l’ultimo attacco ha dimostrato che è possibile eseguire codice arbitrario a livello kernel attraverso una tecnica di Return-Oriented Programming (ROP), reindirizzando lo stack pointer verso un buffer controllato dall’attaccante.

Il team ha spiegato che per risolvere StackWarp sono **necessari interventi a livello di microcodice o hardware** che impediscano il controllo incrociato del motore dello stack tra diversi thread quando sono attive le Confidential Virtual Machines.

AMD ha iniziato a rilasciare patch per i propri clienti prima della divulgazione pubblica. Nel caso non fossero ancora disponibili le patch o non fosse possibile applicarle, si può **disabilitare temporaneamente  il multithreading simultaneo i sistemi che eseguono carichi di lavoro sensibili in ambienti cloud multi-tenant.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AMD](https://www.securityinfo.it/tag/amd/), [Confidential Virtual Machines](https://www.securityinfo.it/tag/confidential-virtual-machines/), [stack engine](https://www.securityinfo.it/tag/stack-engine/), [stack pointer](https://www.securityinfo.it/tag/stack-pointer/), [StackWarp](https://www.securityinfo.it/tag/stackwarp/), [vulnerabilità hardware](https://www.securityinfo.it/tag/vulnerabilita-hardware/)

[CERT-AGID 10-16 gennaio: ancora phishing PagoPA e nuovi malware bancari](https://www.securityinfo.it/2026/01/19/cert-agid-10-16-gennaio-phishing-pagopa-malware-bancari/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![TEE.Fail, l’attacco che accede all’ambiente di esecuzione delle CPU](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_o4qma6o4qma6o4qm-120x85.png)](https://www.securityinfo.it/2025/10/30/tee-fail-lattacco-che-accede-allambiente-di-esecuzione-delle-cpu/ "TEE.Fail, l’attacco che accede all’ambiente di esecuzione delle CPU")

  [TEE.Fail, l’attacco che accede...](https://www.securityinfo.it/2025/10/30/tee-fail-lattacco-che-accede-allambiente-di-esecuzione-delle-cpu/ "Permanent link to TEE.Fail, l’attacco che accede all’ambiente di esecuzione delle CPU")

  Ott 30, 2025  [0](https://www.securityinfo.it/2025/10/30/tee-fail-lattacco-che-accede-allambiente-di-esecuzione-delle-cpu/#respond)
* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-...