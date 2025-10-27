---
title: Scoperto EvilVideo, una vulnerabilità zero-day di Telegram per Android
url: https://www.securityinfo.it/2024/07/25/scoperto-evilvideo-una-vulnerabilita-zero-day-di-telegram-per-android/?utm_source=rss&utm_medium=rss&utm_campaign=scoperto-evilvideo-una-vulnerabilita-zero-day-di-telegram-per-android
source: Securityinfo.it
date: 2024-07-26
fetch_date: 2025-10-06T17:44:30.690031
---

# Scoperto EvilVideo, una vulnerabilità zero-day di Telegram per Android

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

## Scoperta EvilVideo, una vulnerabilità zero-day di Telegram per Android

Lug 25, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [Prodotto](https://www.securityinfo.it/category/news/prodotto-news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/07/25/scoperto-evilvideo-una-vulnerabilita-zero-day-di-telegram-per-android/#respond)

---

I ricercatori di ESET [hanno scoperto](https://www.welivesecurity.com/en/eset-research/cursed-tapes-exploiting-evilvideo-vulnerability-telegram-android/) **EvilVideo**, una vulnerabilità zero-day che colpisce le versioni di Telegram per Android. Sfruttando il bug, gli attaccanti possono **condividere payload malevoli su canali, gruppi e chat Telegram mascherandoli come file multimediali.**

La particolarità dell’exploit è che gli attaccanti possono **creare payload specifici sfruttando l’API di Telegram**; ciò gli consente di inviare il payload malevolo e farlo apparire come una preview multimediale, non come un file binario allegato. Nell’esempio condiviso dai ricercatori, il payload, una volta condiviso in chat, viene visualizzato come un breve video.

![EvilVideo exploit- Credits: ESET](https://www.securityinfo.it/wp-content/uploads/2024/07/figure-3-example-of-exploit.jpeg)

Credits: ESET

Di default, tutti i media ricevuti su Telegram vendono scaricati immediatamente, quindi gli utenti che hanno ancora abilitata questa opzione scaricheranno automaticamente il payload non appena aprono la chat.

Se la vittima cerca di aprire il video, Telegram mostra un messaggio di errore specificando che non riesce a leggerlo e propone all’utente di utilizzare un’applicazione esterna. Se poi l’utente procede, gli verrà chiesto di **installare un’applicazione (malevola) per visualizzare il video**; installando l’app, il malware distribuito dall’attaccante viene eseguito sul dispositivo colpito.

I ricercatori hanno confermato che l’exploit funziona solo su Android: nel caso di Telegram Web e del client Desktop, il file malevolo è stato scaricato non come .apk ma come file .mp4, il che ha bloccato l’esecuzione del malware.

Al momento non è chiaro chi sia l’attaccante o gli attaccanti dietro l’exploit di EvilVideo. Lo stesso cybercriminale (o gruppo) sta vendendo anche un **cryptor-as-a-service per Android** che viene presentato come “Fully Undetectable” (FUD), ovvero che non può essere individuato da antivirus e prodotti di sicurezza.

Il team di ESET ha scoperto l’exploit in vendita su un forum del dark web il 6 giugno scorso e ha segnalato la vulnerabilità a Telegram il 26 giugno; **l’11 luglio, la compagnia ha rilasciato un aggiornamento che risolve il bug** (versioni 10.14.5 e superiori). Il consiglio è di aggiornare il prima possibile l’applicazione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Android](https://www.securityinfo.it/tag/android/), [cryptor-as-a-service](https://www.securityinfo.it/tag/cryptor-as-a-service/), [EvilVideo](https://www.securityinfo.it/tag/evilvideo/), [exploit](https://www.securityinfo.it/tag/exploit/), [payload maleolo](https://www.securityinfo.it/tag/payload-maleolo/), [telegram](https://www.securityinfo.it/tag/telegram/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[EvolvedAim: infostealer nascosto nel cheat per Escape From Tarkov](https://www.securityinfo.it/2024/07/26/evolvedaim-infostealer-nascosto-nel-cheat-per-escape-from-tarkov/)
[Daggerfly sta usando una nuova versione di Macma, una backdoor per macOS](https://www.securityinfo.it/2024/07/25/daggerfly-sta-usando-una-nuova-versione-di-macma-una-backdoor-per-macos/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilit...