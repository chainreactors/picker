---
title: Le implementazioni LTE e 5G soffrono di centinaia di vulnerabilità
url: https://www.securityinfo.it/2025/01/27/le-implementazioni-lte-e-5g-soffrono-di-centinaia-di-vulnerabilita/?utm_source=rss&utm_medium=rss&utm_campaign=le-implementazioni-lte-e-5g-soffrono-di-centinaia-di-vulnerabilita
source: Securityinfo.it
date: 2025-01-28
fetch_date: 2025-10-06T20:10:56.349608
---

# Le implementazioni LTE e 5G soffrono di centinaia di vulnerabilità

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

## Le implementazioni LTE e 5G soffrono di centinaia di vulnerabilità

Gen 27, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/01/27/le-implementazioni-lte-e-5g-soffrono-di-centinaia-di-vulnerabilita/#respond)

---

Un gruppo di ricercatori del Florida Institute for Cybersecurity Research [ha scoperto](https://cellularsecurity.org/ransacked) ben **119 vulnerabilità presenti nell’infrastruttura core delle implementazioni LTE/5G.** Ognuna di queste può provocare interruzioni di servizio persistenti estese a intere città o aree metropolitane, mentre altre possono essere usate per compromettere e accedere da remoto alla rete cellulare.

“*La nostra ricerca ha rilevato che **queste vulnerabilità sono presenti sia nei core LTE/5G open-source ben mantenuti che nel software proprietario**, in entrambi i casi con implementazioni attive in ambito commerciale*” spiega il gruppo.

![LTE 5G vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2025/01/technology-6873010_1920.jpg)

Vista la centralità delle reti cellulari nella quotidianità, gli impatti di questi bug possono essere disastrosi. Gli attacchi di Denial of Service possono interrompere in maniera persistente tutte le comunicazioni – chiamate, messaggi e scambio di dati – anche su aree molto estese, come intere città.

Un attaccante può infatti **interrompere l’operatività del MME** (Mobility Management Entity), componente centrale delle implementazioni LTE che monitora la comunicazione tra i dispositivi mobile e il core della rete. Similmente, è possibile **alterare la funzionalità di AMF** (Access and Mobility Management Function) che si occupa, tra le altre cose, della geolocalizzazione dei dispositivi e del routing delle chiamate.

Molte delle vulnerabilità individuate nelle implementazioni LTE e 5G consentono anche di causare **buffer overflow** e altri errori di corruzione della memoria, permettendo a un malintenzionato di prendere il controllo del core della rete cellulare; fatto ciò, l’attaccante può monitorare la posizione dei dispositivi nell’area di interesse, eseguire attacchi contro specifici device o compromettere componenti centrali dell’infrastruttura con exploit mirati.

![](https://www.securityinfo.it/wp-content/uploads/2025/01/network-4851079_1920.jpg)

I ricercatori hanno **diviso le vulnerabilità in due macro-categorie**: quelle che possono essere **sfruttate da qualsiasi dispositivo mobile** e quelle che invece possono essere sfruttate solo da chi possiede una **femtocella o una stazione radio**. Nel primo caso, un attaccante ha bisogno solo di un dispositivo funzionante, anche senza SIM, in grado di inviare pacchetti malformati alle vittime.

“*Abbiamo contribuito a far procedere lo stato dell’arte per i test delle interfacce cellulari e dimostrato che **serve ancora molto lavoro per garantire standard sufficienti di robustezza nelle implementazioni core LTE/5G***” hanno commentato i ricercatori.

Per ognuna delle vulnerabilità, il team ha contattato il vendor dell’implementazione corrispondente per segnalare i risultati. La maggior parte dei vendor ha riconosciuto la legittimità delle scoperte e hanno già rilasciato dei fix.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [5G](https://www.securityinfo.it/tag/5g/), [compromissione di rete](https://www.securityinfo.it/tag/compromissione-di-rete/), [denial of service](https://www.securityinfo.it/tag/denial-of-service/), [LTE](https://www.securityinfo.it/tag/lte/), [reti cellulari](https://www.securityinfo.it/tag/reti-cellulari/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza](https://www.securityinfo.it/2025/01/28/i-ransomware-contro-le-appliance-esxi-sfruttano-il-tunneling-ssh-per-la-persistenza/)
[CERT-AGID 18 – 24 gennaio: una nuova campagna a tema INPS (e ancora Vidar)](https://www.securityinfo.it/2025/01/27/cert-agid-18-24-gennaio-una-nuova-campagna-a-tema-inps-e-ancora-vidar/)

---

![](https://secure.gravatar.com/avatar/93ad3a1bbb47d1f5755e4f5086cb3f22?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di......