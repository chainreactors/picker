---
title: Google Cloud è esposto ad abusi “transitivi” di accesso: la ricerca di Vectra AI
url: https://www.securityinfo.it/2024/09/18/google-cloud-e-esposto-ad-abusi-transitivi-di-accesso-la-ricerca-di-vectra-ai/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-19
fetch_date: 2025-10-06T18:27:51.439531
---

# Google Cloud è esposto ad abusi “transitivi” di accesso: la ricerca di Vectra AI

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

## Google Cloud è esposto ad abusi “transitivi” di accesso: la ricerca di Vectra AI

Set 18, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2024/09/18/google-cloud-e-esposto-ad-abusi-transitivi-di-accesso-la-ricerca-di-vectra-ai/#respond)

---

Negli ultimi tempi gli **abusi “transitivi” di accesso**, cioè quelli ottenuti indirettamente tramite un intermediario di fiducia, si stanno diffondendo, allarmando li esperti di cybersecurity.

Del problema si è occupato anche **Kat Traxler**, Principal Security Researcher di Vectra AI, il quale ha pubblicato una [ricerca](https://www.vectra.ai/blog/transitive-access-abuse-data-exfiltration-via-document-ai) su questo tipo di abusi all’interno di Google Cloud, spiegando che **il servizio Document AI consente agli utenti di leggere qualsiasi oggetto Cloud Storage nello stesso progetto.**

![abusi "transitivi" accesso](https://www.securityinfo.it/wp-content/uploads/2024/09/network-4851119_1920-1.jpg)

Pixabay

Il servizio si occupa di estrarre informazioni da documenti non strutturati. L’agente che si occupa di raccogliere i dati e di fornire i risultati in output possiede dei **permessi molto estesi** che gli consentono di accedere a qualsiasi bucket Cloud Storage dello stesso progetto. Anche se l’utente che esegue il servizio Document AI ha dei permessi limitati, l’agente che materialmente esegue il processo non rispetta questi limiti e consente attacchi di data exfiltration.

“*Sfruttare il servizio (e la sua identità) per esfiltrare i dati costituisce un abuso transitivo di accesso che aggira i controlli di accesso previsti e compromette la riservatezza dei dati*” spiega Traxler.

Per sfruttare l’exploit, un attaccante deve **sfruttare un processo di Document AI già esistente sul dispositivo** o ottenere i permessi di creazione per aggiungerne uno che gli permetta di leggere dai bucket. Se invece Document AI non è mai stato usato in qualche progetto, l’attaccante deve prima **abilitare il servizio**; una volta abilitato Document AI, si ottiene in automatico il ruolo “project-level” che consente di procedere con l’attacco.

## Abusi transitivi di accesso: la risposta di Google

Il team di Vectra AI ha notificato il problema a Google il 4 aprile tramite il Vulnerability Report Program e, dopo mesi di analisi, la compagnia ha confermato l’esistenza della vulnerabilità, classificandola di categoria S2C, ovvero “bypass di controlli di sicurezza centrali”.

Inizialmente Google aveva comunicato a Traxler che **la vulnerabilità non poteva essere considerata parte del Vulnerability Reward Program**: “*a una prima analisi, il problema non sembra abbastanza grave da qualificarsi per un premio*” aveva scritto la compagnia al ricercatore. In seguito, Google è tornata sui suoi passi e ha deciso di considerare il bug valido per il programma di ricompensa.

“*Google ha fatto retromarcia sulla sua decisione di non fornire una ricompensa, citando ‘documentazione insufficiente o incorretta’ come causa. **La proposta di bug è stata ora classificata come ‘bypass di controlli di sicurezza centrali’** ed è stata definita una ricompensa. Non c’è indicazione del quando o del come il problema verrà risolto*” ha spiegato Traxler.

![](https://www.securityinfo.it/wp-content/uploads/2024/06/line-7146714_1920.jpg)

La vulnerabilità colpisce tutti i clienti Google Cloud, anche se non utilizzano Document AI. Al momento Google non ha rilasciato dei fix per risolvere il problema, ma gli utenti possono mitigare i rischi **usando il servizio in progetti isolati e segmentati** e circsoscrivendo l’uso di Document AI e delle sue **API**, **abilitandole solo quando è necessario.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [abusi transitivi di accesso](https://www.securityinfo.it/tag/abusi-transitivi-di-accesso/), [bypass controlli di sicurezza](https://www.securityinfo.it/tag/bypass-controlli-di-sicurezza/), [cloud storage](https://www.securityinfo.it/tag/cloud-storage/), [Document AI](https://www.securityinfo.it/tag/document-ai/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [Google Cloud](https://www.securityinfo.it/tag/google-cloud/), [Vectra AI](https://www.securityinfo.it/tag/vectra-ai/)

[Il costo di un cyberattacco va oltre le perdite finanziarie dirette](https://www.securityinfo.it/2024/09/19/il-costo-di-un-cyberattacco-va-oltre-le-perdite-finanziarie-dirette/)
[Port of Seattle conferma l'attacco da parte del ransomware Rhysida](https://www.securityinfo.it/2024/09/17/port-of-seattle-conferma-lattacco-da-parte-del-ransomware-rhysida/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Un attacco supply chain ha compromesso oltre 40 pacchetti NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h-120x85.png)](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  [Un attacco supply chain ha compromesso...](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Permanent link to Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  Set 16, 2025  [0](https://www.s...