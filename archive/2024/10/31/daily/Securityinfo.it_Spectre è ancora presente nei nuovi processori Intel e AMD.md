---
title: Spectre è ancora presente nei nuovi processori Intel e AMD
url: https://www.securityinfo.it/2024/10/30/spectre-e-ancora-presente-nei-nuovi-processori-intel-e-amd/?utm_source=rss&utm_medium=rss&utm_campaign=spectre-e-ancora-presente-nei-nuovi-processori-intel-e-amd
source: Securityinfo.it
date: 2024-10-31
fetch_date: 2025-10-06T18:57:33.564190
---

# Spectre è ancora presente nei nuovi processori Intel e AMD

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

## Spectre è ancora presente nei nuovi processori Intel e AMD

Ott 30, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/10/30/spectre-e-ancora-presente-nei-nuovi-processori-intel-e-amd/#respond)

---

L’incubo di **Spectre** è tutt’altro che concluso: una nuova [analisi](https://comsec.ethz.ch/research/microarch/breaking-the-barrier/) condotta da Johannes Wikner and Kaveh Razavi, ricercatori di ETH Zürich, ha rivelato che **i nuovi processori Intel e AMD sono ancora vulnerabili agli attacchi di esecuzione speculativa.**

![Spectre](https://www.securityinfo.it/wp-content/uploads/2024/10/technology-2818664_1920.jpg)

La ricerca di Wikner e Razavi si concentra in particolare sulla **barriera di speculazione “IBPB”** (Indirect Branch Predictor Barrier), un meccanismo usato nei sistemi AMD e Intel per mitigare gli attacchi speculativi. Questo controllo crea una barriera che impedisce alla porzione di software che viene eseguita prima della barriera di controllare i branch eseguiti dopo questo punto, sullo stesso processore logico (fonte: [Intel](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/technical-documentation/indirect-branch-predictor-barrier.html)).

A quanto pare però il meccanismo non è sufficiente: i due ricercatori hanno trovando un **bug nelle microarchitetture** di Intel più recenti (come Golden Cove e Raptor Cove, presenti nella 12°, 13° e 14° generazione e negli Xeon di 5° e 6° generazione) che permette d**i sfruttare le previsioni dei branch anche dopo che IBPB avrebbe dovuto invalidarle.**

Si tratta di una “speculazione post-barriera” che permette a un attaccante di superare i controlli di sicurezza imposti dai contesti dei processi e dalle macchine virtuali.

Wikner e Razavi hanno condiviso una dimostrazione di attacco in grado di sfruttare Spectre con la speculazione post-barriera per **accedere ai dati sensibili di altri processi nel sistema, inclusi quelli con privilegi elevati.**

“*Anche se i programmi che gestiscono dati sensibili utilizzassero IBPB – e pensiamo che dovrebbero farlo – sarebbero comunque vulnerabili, a causa del bug del microcodice in IBPB che abbiamo trovato. ****Siamo i primi a mostrare un exploit pratico di Spectre cross-process end-to-end****, con un attacco che fa trapelare la password di root da un processo SUID (cioè un processo che esegue con privilegi elevati)*“.

I ricercatori spiegano anche che **la semantica di IBPB non è chiara** e si è evoluta nel corso degli anni; questo complica il lavoro dei maintainer dei sistemi operativi che devono prendere decisioni di design stando attendi a non introdurre regressioni.

La semantica a cui si riferiscono i ricercatori è quella presente nella variante di AMD che **“trascura le previsioni dei return branch”**, un comportamento che va in conflitto con le specifiche del meccanismo. Questo consente a un attaccante di iniettare previsioni di branch malevoli prima che l’operazione di IBPB si concluda.

Anche in questo caso, Wikner e Razavi hanno condiviso un esempio pratico di come viene eseguito un attacco di questo tipo.

L’analisi dei ricercatori si è concentrata sui sistemi Linux perché “*non abbiamo il codice sorgente degli altri OS principali*“, quindi è possibile che il problema affligga anche altri sistemi operativi.

Per ridurre il rischio di attacco, i ricercatori consigliano di **mantenere aggiornato il microcode dei processori Intel** e **installare gli aggiornamenti del kernel nel caso di processori AMD.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AMD](https://www.securityinfo.it/tag/amd/), [IBPB](https://www.securityinfo.it/tag/ibpb/), [Intel](https://www.securityinfo.it/tag/intel/), [previsione dei branch](https://www.securityinfo.it/tag/previsione-dei-branch/), [Spectre](https://www.securityinfo.it/tag/spectre/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Circola una nuova versione di Qilin, ancora più potente](https://www.securityinfo.it/2024/10/30/circola-una-nuova-versione-di-qilin-ancora-piu-potente/)
[Infostealer e quishing, la minaccia del phishing più evoluto](https://www.securityinfo.it/2024/10/29/infostealer-e-quishing-la-minaccia-del-phishing-piu-evoluto/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.i...