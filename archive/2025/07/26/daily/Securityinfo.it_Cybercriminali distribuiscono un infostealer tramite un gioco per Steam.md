---
title: Cybercriminali distribuiscono un infostealer tramite un gioco per Steam
url: https://www.securityinfo.it/2025/07/25/cybercriminali-distribuiscono-un-infostealer-tramite-un-gioco-per-steam/?utm_source=rss&utm_medium=rss&utm_campaign=cybercriminali-distribuiscono-un-infostealer-tramite-un-gioco-per-steam
source: Securityinfo.it
date: 2025-07-26
fetch_date: 2025-10-06T23:54:42.632591
---

# Cybercriminali distribuiscono un infostealer tramite un gioco per Steam

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## Cybercriminali distribuiscono un infostealer tramite un gioco per Steam

Lug 25, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/07/25/cybercriminali-distribuiscono-un-infostealer-tramite-un-gioco-per-steam/#respond)

---

I ricercatori di [Prodaft](https://github.com/prodaft/malware-ioc/blob/master/LARVA-208/SteamCampaign.md), compagnia di cybersecurity, hanno individuato un **infostealer in Chemia**, un gioco per Steam attualmente disponibile in early access. Secondo il team, dietro la campagna ci sarebbe EncryptHub, attaccante noto anche come Larva-208.

“*I binari malevoli erano integrati direttamente nell’eseguibile del gioco disponibile sulla piattaforma*” ha affermato il team di Prodaft. Non appena un utente scaricava l’applicazione, il malware veniva eseguito.

![Steam infostealer](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_2i2tjf2i2tjf2i2t.png)

Stando a un’analisi condivisa dalla compagnia con [Bleeping Computer](https://www.bleepingcomputer.com/news/security/hacker-sneaks-infostealer-malware-into-early-access-steam-game/), **la prima compromissione è avvenuta il 22 luglio** quando il gruppo ha aggiunto ai file di gioco il payload di **HijackLoader**; questo malware serviva per ottenere persistenza sul dispositivo della vittima durante l’installazione del gioco e in seguito scaricare l’infostealer **Vidar**.

Oltre a Vidar, il gruppo distribuiva anche **Ficke Stealer**, un infostealer in grado di raccogliere dati memorizzati nei browser quali credenziali di account, informazioni per l’auto-riempimento dei form, cookie e informazioni dai portafogli di criptovalute.

“*L’eseguibile compromesso appare come legittimo agli utenti che lo scaricano da Steam, creando una **componente efficace di social engineering che si basa sulla piattaforma piuttosto che sulle tradizionali tecniche di frode***” continuano i ricercatori di Prodaft. Scaricando il Playtest gratuito del gioco, gli utenti si ritrovano invece con un malware sul proprio dispositivo, senza accorgersene: gli infostealer infatti vengono eseguiti in background e non impattano sulle performance del gioco.

Al momento non è chiaro come l’attaccante sia riuscito a caricare i file malevoli nel gioco, ma è probabile che ci sia di mezzo un insider malevolo. Bleeping Computer ha contattato sia Valve che il team dietro Chemia, ma non ha avuto riscontri in merito alla questione.

**Su Steam il gioco è ancora disponibile per il download**, ma non è chiaro se si tratti di una versione aggiornata e senza infostealer. Fino a che non verranno pubblicate comunicazioni ufficiali sullo stato dell’eseguibile, il download del gioco è ovviamente sconsigliato.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chemia](https://www.securityinfo.it/tag/chemia/), [EncryptHub](https://www.securityinfo.it/tag/encrypthub/), [Fickle Stealer](https://www.securityinfo.it/tag/fickle-stealer/), [HijackLoader](https://www.securityinfo.it/tag/hijackloader/), [infostealer](https://www.securityinfo.it/tag/infostealer/), [Steam](https://www.securityinfo.it/tag/steam/), [Vidar](https://www.securityinfo.it/tag/vidar/)

[CERT-AGID 19 – 25 luglio: il Fascicolo Sanitario Elettronico come leva](https://www.securityinfo.it/2025/07/28/cert-agid-19-25-luglio-il-fascicolo-sanitario-elettronico-come-leva/)
[Generative AI cinesi: i rischi dell’adozione incontrollata nelle aziende](https://www.securityinfo.it/2025/07/25/generative-ai-cinesi-i-rischi-delladozione-incontrollata-nelle-aziende/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![Shuckworm prende di mira le missioni in Ucraina con device rimovibili](https://www.securityinfo.it/wp-content/uploads/2025/04/15944-120x85.jpg)](https://www.securityinfo.it/2025/04/11/shuckworm-prende-di-mira-le-missioni-in-ucraina-con-device-rimovibili/ "Shuckworm prende di mira le missioni in Ucraina con device rimovibili")

  [Shuckworm prende di mira le missioni in...](https://www.securityinfo.it/2025/04/11/shuckworm-prende-di-mira-le-missioni-in-ucraina-con-device-rimovibili/ "Permanent link to Shuckworm prende di mira le missioni in Ucraina con device rimovibili")

  Apr 11, 2025  [0](https://www.securityinfo.it/2025/04/11/shuckworm-prende-di-mira-le-missioni-in-ucraina-con-device-rimovibili/#respond)
* [![ClickFix: torna la campagna di phishing che colpisce il settore turistico](https://www.securityinfo.it/wp-content/uploads/2025/03/83765...