---
title: Violazione per Slack: accesso non autorizzato al repository GitHub
url: https://www.securityinfo.it/2023/01/09/violazione-per-slack-accesso-non-autorizzato-al-repository-github/?utm_source=rss&utm_medium=rss&utm_campaign=violazione-per-slack-accesso-non-autorizzato-al-repository-github
source: Over Security - Cybersecurity news aggregator
date: 2023-01-10
fetch_date: 2025-10-04T03:27:23.102727
---

# Violazione per Slack: accesso non autorizzato al repository GitHub

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

## Violazione per Slack: accesso non autorizzato al repository GitHub

Gen 09, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/01/09/violazione-per-slack-accesso-non-autorizzato-al-repository-github/#respond)

---

Lo scorso 31 dicembre, Slack ha [pubblicato un avviso](https://slack.com/intl/it-it/blog/news/slack-security-update) per **segnalare un incidente di sicurezza**: attaccanti hanno ottenuto l’accesso ai repository GitHub di Slack tramite un numero “limitato” di token dei dipendenti Slack, che sono stati rubati.

Secondo la società, **alcuni repository di codice privati di Slack** sono stati violati, ma le istanze primarie del servizio e i dati dei clienti non sono stati alterati.

Questa la descrizione dei fatti, secondo il racconto riportato dalla stessa azienda: “Il 29 dicembre 2022 siamo stati informati di **attività sospette sul nostro account GitHub**. Dopo un’indagine, abbiamo scoperto che un numero limitato di token dei dipendenti Slack è stato rubato e utilizzato in modo improprio per ottenere l’accesso al nostro repository GitHub ospitato esternamente”.

“La nostra indagine ha anche rivelato che l’attore della minaccia ha **scaricato repository di codice privato** il 27 dicembre. Nessun repository scaricato conteneva dati dei clienti, mezzi per accedere ai dati dei clienti o la base di codice principale di Slack”, ha concluso l’azienda.

Slack ha invalidato i token rubati e **sta indagando sul potenziale impatto** della violazione per i suoi clienti. Al momento, nulla suggerisce che siano state violate aree sensibili dell’ambiente di Slack, compresa la produzione. Per prudenza, tuttavia, l’azienda ha preso opportune contromisure.

## **Pubblicare senza farsi notare**

Questo report ha però qualche **caratteristica non troppo convincente**, che pare stia prendendo piede nella “comunicazione di crisi” da parte di diverse aziende oggetto di violazioni, come ha scoperto e sottolineato [BleepingComputer](https://www.bleepingcomputer.com/news/security/slacks-private-github-code-repositories-stolen-over-holidays/).

![](https://www.securityinfo.it/wp-content/uploads/2023/01/slack-noindex.png)

Fonte: BleepingComputer

Mentre sottolinea fin dal sottotitolo dell’articolo l’importanza di “sicurezza, privacy e trasparenza”, Slack non ha pubblicato l’articolo sul blog di notizie internazionali dell’azienda. Inoltre, al contrario dei post precedenti, questa pagina utilizza il tag [noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) (almeno in alcune regioni) una funzione Html utilizzata per **escludere una pagina Web dai risultati dei motori di ricerca**.

Nonostante gli indizi riportati sollevino effettivamente qualche domanda, **non sono necessariamente indicativi di malafede** da parte dell’azienda; ci sono diverse ragioni tecniche per attivare il tag noindex, magari per avere il tempo di verificare i contenuti di un testo e fornire eventuali aggiornamenti prima che la news venga diffusa e ripresa da tutti i media.

La scelta di pubblicare in silenzio non è comunque una novità assoluta; in passato **LastPass e GoTo avevano impiegato tattiche analoghe** per limitare la risonanza delle gravi violazioni di sicurezza subite proprio da LastPass.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Bleeping Computer](https://www.securityinfo.it/tag/bleeping-computer/), [codebase](https://www.securityinfo.it/tag/codebase/), [GitHub](https://www.securityinfo.it/tag/github/), [SLACK](https://www.securityinfo.it/tag/slack/)

[Il ruolo dello SBOM nella cybersecurity](https://www.securityinfo.it/2023/01/09/ruolo-sbom-cybersecurity/)
[L'impatto delle criptovalute sulla cybersecurity](https://www.securityinfo.it/2023/01/05/criptovalute-impatto-cybersecurity/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  Set 09, 2025  [0](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfr...