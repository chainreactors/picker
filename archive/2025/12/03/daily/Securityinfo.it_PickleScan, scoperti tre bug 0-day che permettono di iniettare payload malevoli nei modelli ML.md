---
title: PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML
url: https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/?utm_source=rss&utm_medium=rss&utm_campaign=picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml
source: Securityinfo.it
date: 2025-12-03
fetch_date: 2025-12-04T03:19:37.390167
---

# PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML

Aggiornamenti recenti Dicembre 3rd, 2025 7:01 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/)
* [ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/)
* [Coupang conferma il data breach: esposti i dati di oltre 30 milioni di utenti](https://www.securityinfo.it/2025/12/01/coupang-conferma-il-data-breach-esposti-i-dati-di-oltre-30-milioni-di-utenti/)
* [CERT-AGID 22–28 novembre: boom di phishing PagoPA e nuovi malware via SMS](https://www.securityinfo.it/2025/12/01/cert-agid-22-28-novembre-boom-phishing-pagopa-malware-sms/)
* [Ecco il tool gratuito per verificare se un IP fa parte di un botnet](https://www.securityinfo.it/2025/11/28/ecco-il-tool-gratuito-per-verificare-se-un-ip-fa-parte-di-un-botnet/)

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

## PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML

Dic 03, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/#respond)

---

I ricercatori di JFrog Security Research [hanno individuato](https://jfrog.com/blog/unveiling-3-zero-day-vulnerabilities-in-picklescan/) **tre vulnerabilità 0-day in PickleScan**, noto tool per la scansione di modelli di machine learning per l’individuazione di codice malevolo.

“*Ogni vulnerabilità scoperta consente agli attaccanti di **eludere il rilevamento dei malware di PickleScan** e potenzialmente eseguire un **attacco supply chain su larga scala** distribuendo modelli ML dannosi che nascondono codice dannoso non rilevabile*” spiegano i ricercatori.
Pickle di Python è notoriamente non sicuro a causa della sua capacità di serializzare quasi tutto, inclusi oggetti Python che possono eseguire codice arbitrario durante la deserializzazione. Numerosi framework ML, tra i quali PyTorch, lo utilizzano per salvare i pesi e la struttura dei modelli di machine learning. **PickleScan** è nato come uno strumento per mitigare questo rischio: il tool analizza i modelli Pickle alla ricerca di costrutti non sicuri prima che vengano caricati. Con queste tre nuove vulnerabilità, gli attaccanti possono eludere questo meccanismo di difesa ed eseguire codice da remoto.

![PickleScan](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_ydrt5rydrt5rydrt.png)

## Le vulnerabilità di PickleScan

La prima vulnerabilità individuata, tracciata come CVE-2025-10155, è un bug di **bypass dell’estensione del file**. Questo bug sfrutta una debolezza dello strumento che, nel rilevare il tipo di file, dà priorità al controllo dell’estensione del file rispetto all’analisi del contenuto.

Un attaccante può quindi usare un file Pickle standard e iniettarvi un payload malevolo, rinominandolo poi in un’estensione comunemente associata a PyTorch, come `.bin` o `.pt`.  Quando PickleScan scansiona il file rinominato, tenta di applicare la logica di scansione specifica per PyTorch. Poiché il file è in realtà un Pickle standard, lo scanner PyTorch fallisce e **restituisce un errore o un risultato incompleto**, bypassando di fatto l’analisi del contenuto. Il payload malevolo si attiva poi al momento del caricamento da parte di PyTorch.

La seconda vulnerabilità risiede nel **processo di gestione degli archivi ZIP**, spesso usati per i modelli PyTorch. Lo strumento usa il modulo `zipfile` di Python per gestire gli archivi, ma **la verifica dell’integrità dei file non è abbastanza robusta**: un attaccante può infatti creare un archivio .zip contenente un payload dannoso e manipolarlo affinché la scansione di PickleScan fallisca o venga interrotta, senza restituire un risultato. Nonostante PickleScan fallisca la scansione, PyTorch può comunque caricare ed eseguire il codice malevolo.

Infine, la terza vulnerabilità **sfrutta una logica di deserializzazione specifica di PyTorch del metodo** `reduce`. Il metodo viene utilizzato per ricostruire gli oggetti e PickleScan non riesce a identificare correttamente l’uso di funzioni che sono considerate non sicure. Un attaccante può creare un payload Pickle sfruttando un difetto logico nel tracciamento degli argomenti durante l’analisi per causare un errore di gestione degli argomenti e innescare eccezioni. Bypassando i meccanismi di rilevamento di PickleScan, è possibile eseguire codice da remoto.

I ricercatori di JFrog Security Research sottolineano che queste tre vulnerabilità evidenziano un **problema sistemico nel modo in cui si approccia la sicurezza dei modelli di machine learning**: in primo luogo, l’estesa dipendenza da PickleScan crea un singolo punto di fallimento, rendendo vulnerabile l’intera architettura di sicurezza; inoltre, i tre bug dimostrano quanto è rischioso assumere che i tool di sicurezza e le applicazioni gestiscano i file allo stesso modo; infine, poiché i repository ospitano milioni di modelli, queste vulnerabilità consentono l’esecuzione di **attacchi supply chain su ampia scala.**

Il team di JFrog Security Reserach consiglia di **aggiornare PickleScan all’ultima versione disponibile** contenente le patch per le vulnerabilità. È consigliato inoltre valutare la migrazione a formati di serializzazione del modello più sicuri e meno flessibili e mettere in campo flussi di scansione a più livelli, senza affidarsi a un unico strumento.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco supply chain](https://www.securityinfo.it/tag/attacco-supply-chain/), [machine learning](https://www.securityinfo.it/tag/machine-learning/), [PickleScan](https://www.securityinfo.it/tag/picklescan/), [PyTorch](https://www.securityinfo.it/tag/pytorch/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [vulnerabilità 0-day](https://www.securityinfo.it/tag/vulnerabilita-0-day/)

[ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”]...