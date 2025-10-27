---
title: Operazione BadBox fermata in Germania grazie a una sinkhole
url: https://www.securityinfo.it/2024/12/18/operazione-badbox-fermata-in-germania-grazie-a-una-sinkhole/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-19
fetch_date: 2025-10-06T19:41:21.060301
---

# Operazione BadBox fermata in Germania grazie a una sinkhole

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

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

## Operazione BadBox fermata in Germania grazie a una sinkhole

Dic 18, 2024  [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/ "Articoli scritti da Valentina Caruso")
 [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/12/18/operazione-badbox-fermata-in-germania-grazie-a-una-sinkhole/#respond)

---

La Germania compie un passo significativo nella lotta al crimine informatico. Il Bundesamt für Sicherheit in der Informationstechnik (BSI), **l’Agenzia Federale per la Sicurezza Informatica**, ha annunciato di aver bloccato l’operazione BADBOX. Si tratta di un sofisticato attacco malware che **ha compromesso almeno 30.000 dispositivi** connessi a Internet e venduti nel Paese UE.

## Un malware nascosto nei dispositivi preinstallati

**BADBOX è stato rilevato su dispositivi come cornici digitali**, media player e device per lo streaming multimediale. Si sospetta, però, che **anche smartphone e tablet** siano coinvolti. Tutti questi dispositivi, accomunati da versioni obsolete di Android, sarebbero stati distribuiti con **malware preinstallato**.

Grazie all’uso del sinkholing, il BSI ha interrotto le comunicazioni tra i dispositivi infetti e i loro server di comando e controllo, isolando efficacemente la minaccia. In pratica, **il sinkholing re-indirizza tutto il traffico proveniente dagli IP malevoli**, spostandolo verso server appositamente messi a disposizione per smaltirlo.

![operazione-BADBOX-Germania](https://www.securityinfo.it/wp-content/uploads/2024/12/operazione-BADBOX-Germania.jpeg)

## Le caratteristiche dell’operazione BADBOX

Documentata per la prima volta nell’ottobre 2023 dal team di ricerca Satori Threat Intelligence di HUMAN, BADBOX è stata definita una “operazione complessa”, **basata su falle nella supply chain di dispositivi Android economici** e di marchi poco noti. Il malware principale, Triada, consente di **raccogliere dati sensibili**, come codici di autenticazione, e di installare ulteriori software dannosi.

Un aspetto particolarmente preoccupante di BADBOX è la sua integrazione con un **botnet per frodi pubblicitarie** chiamato PEACHPIT. Questo sistema genera traffico fraudolento da app Android e iOS falsificate. “*Una frode pubblicitaria in piena regola che permetteva agli operatori di guadagnare da impression fasulle generate sulle loro stesse app falsificate*” ha spiegato HUMAN. Le impression rappresentano il numero di visualizzazioni.

## Un rischio per la privacy e la sicurezza

I dispositivi compromessi da BADBOX possono essere **utilizzati come proxy**, oltre che per le frodi pubblicitarie. In questo modo altri criminali hanno la possibilità di instradare il traffico Internet usando i device compromessi, aggirando i controlli di sicurezza. Tali dispositivi, inoltre, possono **creare account online su piattaforme come Gmail e WhatsApp.** Questi ultimi mandano messaggi fraudolenti, aumentando i rischi per la privacy e la sicurezza.

## Le azioni intraprese dal BSI

Il [BSI](https://www.bsi.bund.de/DE/Home/home_node.html) ha emesso direttive chiare ai provider di Internet con più di 100mila abbonati, ordinando loro di reindirizzare il traffico verso la sinkhole. Inoltre, l’agenzia ha invitato i consumatori a **scollegare immediatamente i dispositivi sospetti dalla rete**. Questo per prevenire ulteriori compromissioni.

## Occhio ai firmware compromessi

L’operazione del BSI contro BADBOX rappresenta un esempio di eccellenza nella cybersecurity. Soprattutto, mette in luce i pericoli legati a dispositivi con firmware compromesso e **supply chain vulnerabili**. Consumatori e aziende dovrebbero prestare maggiore attenzione nella scelta dei dispositivi tecnologici. Come? **Privilegiando quelli certificati e dotati di aggiornamenti** di sicurezza regolari. La collaborazione tra agenzie governative, fornitori di tecnologia e utenti finali è essenziale per garantire un ecosistema digitale più sicuro.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

[Auriga: protezione multi-livello per i terminali di pagamento](https://www.securityinfo.it/2024/12/18/auriga-protezione-multi-livello-per-i-terminali-di-pagamento/)
[Glutton, la backdoor che colpisce anche i cybercriminali](https://www.securityinfo.it/2024/12/18/glutton-la-backdoor-che-colpisce-anche-i-cybercriminali/)

---

![](https://secure.gravatar.com/avatar/0a083e115b9328218407201798ab82c0?s=90&d=mm&r=g)

##### [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/)

##### Articoli correlati

* [![Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/wp-content/uploads/2019/01/Morten-Lehn-120x85.jpg)](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  [Transparency Center Initiative di...](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Permanent link to Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  Gen 18, 2019  [0](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/#respond)
* [![CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/wp-content/uploads/2025/10/CERT-AGID-cover-120x85.png)](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/ "CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco")

  [CERT-AGID 27 settembre – 3 ottobre:...](https://www.securityinfo.it/2025/10/06/cert-agid-27-sette...