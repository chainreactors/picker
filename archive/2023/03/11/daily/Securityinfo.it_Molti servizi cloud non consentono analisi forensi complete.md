---
title: Molti servizi cloud non consentono analisi forensi complete
url: https://www.securityinfo.it/2023/03/10/molti-servizi-cloud-non-consentono-attivita-forensi-complete/?utm_source=rss&utm_medium=rss&utm_campaign=molti-servizi-cloud-non-consentono-attivita-forensi-complete
source: Securityinfo.it
date: 2023-03-11
fetch_date: 2025-10-04T09:18:17.182798
---

# Molti servizi cloud non consentono analisi forensi complete

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

## Molti servizi cloud non consentono analisi forensi complete

Mar 10, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/03/10/molti-servizi-cloud-non-consentono-attivita-forensi-complete/#respond)

---

La società di sicurezza specializzata nel cloud [Mitiga](https://www.mitiga.io/) ha [diffuso un’analisi](https://www.mitiga.io/blog/mitiga-security-advisory-insufficient-forensic-visibility-in-gcp-storage) che sottolinea come molte delle principali piattaforme cloud, e in particolare Google Cloud Platform, **non riescono a registrare adeguatamente i dati degli eventi** che potrebbero facilitare il rilevamento di compromissioni e l’analisi forense durante la risposta post-compromissione.

L’analisi, pubblicata all’inizio di marzo, spiega come la Google Cloud Platform consenta ai clienti di attivare i log di accesso allo storage, ma di fronte a un utente malintenzionato che compromette con successo l’identità di un utente legittimo, **i registri non riescono a fornire dettagli sufficienti**, creando lacune di visibilità forense.

I problemi di sicurezza includono **la mancata generazione di informazioni dedicate** per le azioni critiche relative all’esfiltrazione, l’assenza di informazioni dettagliate sulle modifiche ai dati e una generale mancanza di visibilità che potrebbe invece fornire un quadro di ciò che è accaduto.

**Una varietà di eventi, ad esempio, è** **inclusa in un unico tipo di accesso**, come la lettura di un file o il download di dati, lasciando gli analisti nel dubbio su cosa sia realmente successo, secondo Veronica Marinov, autrice dell’analisi.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/1641121541250.jpg)

Veronica Marinov, Cloud Incident Response & Security Researcher di Mitiga

“Alle registrazioni di Google Cloud **mancano eventi di log granulari**; nel caso di interazione con oggetti bucket, non è possibile distinguere tra lo scaricamento dell’oggetto, la visualizzazione del contenuto e la consultazione dei metadati”, ha spiegato Marinov.

## Più dettagli per i log

Una buona visibilità tramite registrazioni dettagliate degli eventi nei servizi cloud è fondamentale per comprendere **cosa sia davvero successo durante un attacco**. Gli investigatori forensi dipendono dai log per determinare le azioni dei malintenzionati e i dati che potrebbero essere stati compromessi.

Mitiga ha notato il problema di visibilità nei servizi cloud di Google e ha avvertito che potrebbe influire sulla capacità di individuare eventuali minacce. Google Cloud ha risposto affermando che **la mancanza di visibilità non è una vulnerabilità** e che i dati dei clienti sono al sicuro, ma ha dichiarato di voler approfondire la questione dei problemi relativi alle analisi forensi.

L’analisi riguarda specificamente il cloud di Google, ma secondo Marinov anche altri fornitori di cloud hanno problemi simili.

“Abbiamo visto in altri fornitori di servizi cloud casi in cui non possiamo davvero capire cosa è successo solo vedendo i registri. Siamo in contatto con i fornitori su tali lacune specifiche. Solo dopo aver completato il nostro processo di divulgazione responsabile, però, potremo condividere i dettagli con i media”, ha concluso Marinov.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [analisi](https://www.securityinfo.it/tag/analisi/), [Analisi forense](https://www.securityinfo.it/tag/analisi-forense/), [Forensics](https://www.securityinfo.it/tag/forensics/), [Google Cloud](https://www.securityinfo.it/tag/google-cloud/), [log](https://www.securityinfo.it/tag/log/), [Mitiga](https://www.securityinfo.it/tag/mitiga/)

[BlackMamba sfrutta l’AI per generare codice polimorfico](https://www.securityinfo.it/2023/03/10/blackmamba-sfrutta-lai-per-generare-codice-polimorfico/)
[I rischi della cybersecurity per il 2023](https://www.securityinfo.it/2023/03/10/rischi-cybersecurity-2023/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Cohesity Identity Resilience: da Cohesity e Semperis una soluzione per proteggere le infrastrutture di identità aziendali](https://www.securityinfo.it/wp-content/uploads/2025/09/semperis_cohesity-120x85.png)](https://www.securityinfo.it/2025/09/18/cohesity-identity-resilience-da-cohesity-e-semperis-una-soluzione-per-proteggere-le-infrastrutture-di-identita-aziendali/ "Cohesity Identity Resilience: da Cohesity e Semperis una soluzione per proteggere le infrastrutture di identità aziendali")

  [Cohesity Identity Resilience: da...](https://www.securityinfo.it/2025/09/18/cohesity-identity-resilience-da-cohesity-e-semperis-una-soluzione-per-proteggere-le-infrastrutture-di-identita-aziendali/ "Permanent link to Cohesity Identity Resilience: da Cohesity e Semperis una soluzione per proteggere le infrastrutture di identità aziendali")

  Set 18, 2025  [0](https://www.securityinfo.it/2025/09/18/cohesity-identity-resilience-da-cohesity-e-semperis-una-soluzione-per-proteggere-le-infrastrutture-di-identita-aziendali/#respond)
* [![Google Cloud è esposto ad abusi “transitivi” di accesso: la ricerca di Vectra AI](https://www.securityinfo.it/wp-content/uploads/2024/09/network-4851119_1920-1-120x85.jpg)](https://www.securityinfo.it/2024/09/18/google-cloud-e-esposto-ad-abusi-transitivi-di-accesso-la-ricerca-di-vectra-ai/ "Google Cloud è esposto ad abusi “transitivi” di accesso: la ricerca di Vectra AI")

  [Google Clo...