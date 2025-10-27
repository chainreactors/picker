---
title: Un attacco supply chain ha compromesso oltre 40 pacchetti NPM
url: https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/?utm_source=rss&utm_medium=rss&utm_campaign=un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm
source: Securityinfo.it
date: 2025-09-17
fetch_date: 2025-10-02T20:16:15.400678
---

# Un attacco supply chain ha compromesso oltre 40 pacchetti NPM

Aggiornamenti recenti Ottobre 1st, 2025 2:22 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)
* [Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/)

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

## Un attacco supply chain ha compromesso oltre 40 pacchetti NPM

Set 16, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/#respond)

---

I ricercatori della compagnia di sicurezza Socket [hanno descritto](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages) un **attacco supply chain** responsabile della **compromissione di più di 40 pacchetti NPM.**La campagna è stata individuata inizialmente da [Daniel Pereira](https://www.linkedin.com/in/daniel-pereira-b17a27160/), software engineer presso Loka, per via di un aggiornamento sospetto a @ctrl/tinycolor, una libreria per la manipolazione di file JavaScript con 2.2 milioni di download settimanali.

I ricercatori spiegano che le versioni compromesse dei pacchetti “*includono una funzione (NpmModule.updatePackage) che scarica un pacchetto tarball, modifica il package.json, inietta uno script locale (bundle.js), crea di nuovo il pacchetto e lo ripubblica, abilitando la troianizzazione automatica dei pacchetti in download*“.

Lo script malevolo scarica ed esegue **TruffleHog**, un tool legittimo usato per individuare eventuali credenziali o chiavi presenti nel codice. Gli attaccanti lo utilizzano per individuare token e credenziali cloud sul dispositivo della vittima; in seguito, i dati raccolti vengono inviati ai cybercriminali tramite un webhook.

Nel dettaglio, gli attaccanti cercano variabili d’ambiente quali, tra le altre, GITHUB\_TOKEN, NPM\_TOKEN, AWS\_ACCESS\_KEY\_ID e AWS\_SECRET\_ACCESS\_KEY. Per esfiltrare i dati e mantenere la persistenza, lo script **crea un workflow di GitHub Actions** all’interno dei repository a cui ha accesso.

![attacco NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h.png)

I pacchetti NPM con relative versioni colpiti dall’attacco sono:

* angulartics2@14.1.2
* @ctrl/deluge@7.2.2
* @ctrl/golang-template@1.4.3
* @ctrl/magnet-link@4.0.4
* @ctrl/ngx-codemirror@7.0.2
* @ctrl/ngx-csv@6.0.2
* @ctrl/ngx-emoji-mart@9.2.2
* @ctrl/ngx-rightclick@4.0.2
* @ctrl/qbittorrent@9.7.2
* @ctrl/react-adsense@2.0.2
* @ctrl/shared-torrent@6.3.2
* @ctrl/tinycolor@4.1.1, @4.1.2
* @ctrl/torrent-file@4.1.2
* @ctrl/transmission@7.3.1
* @ctrl/ts-base32@4.0.2
* encounter-playground@0.0.5
* json-rules-engine-simplified@0.2.4, 0.2.1
* koa2-swagger-ui@5.11.2, 5.11.1
* @nativescript-community/gesturehandler@2.0.35
* @nativescript-community/sentry 4.6.43
* @nativescript-community/text@1.6.13
* @nativescript-community/ui-collectionview@6.0.6
* @nativescript-community/ui-drawer@0.1.30
* @nativescript-community/ui-image@4.5.6
* @nativescript-community/ui-material-bottomsheet@7.2.72
* @nativescript-community/ui-material-core@7.2.76
* @nativescript-community/ui-material-core-tabs@7.2.76
* ngx-color@10.0.2
* ngx-toastr@19.0.2
* ngx-trend@8.0.1
* react-complaint-image@0.0.35
* react-jsonschema-form-conditionals@0.3.21
* react-jsonschema-form-extras@1.0.4
* rxnt-authentication@0.0.6
* rxnt-healthchecks-nestjs@1.0.5
* rxnt-kue@1.0.7
* swc-plugin-component-annotate@1.9.2
* ts-gaussian@3.0.6

Secondo quanto [riportato](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html) da The Hacker News, sono emersi anche altri pacchetti compromessi dall’attacco oltre a quelli segnalati da Socket. Gli attaccanti avrebbero sfruttato l’account di NPM “crowdstrike-publisher” per diffondere il malware in altri pacchetti.

I ricrcatori hanno confermato che la campagna è ancora in corso. Il team di Socket consiglia innanzitutto di **passare a versioni non compromesse dei pacchetti** finché non ci saranno patch risolutive e di ruotare i token NPM e altri segreti che potrebbero essere stati esposti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco supply chain](https://www.securityinfo.it/tag/attacco-supply-chain/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [npm](https://www.securityinfo.it/tag/npm/), [pacchetti NPM](https://www.securityinfo.it/tag/pacchetti-npm/), [supply chain](https://www.securityinfo.it/tag/supply-chain/), [Trojan](https://www.securityinfo.it/tag/trojan/)

[MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/)
[TeamItaly, presentata la nuova squadra di giovani cyber defender](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  Set 09, 2025  [0](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-...