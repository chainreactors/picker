---
title: VenomSoftX: l’estensione Chromium che sottrae password e criptovalute
url: https://www.securityinfo.it/2022/11/23/venomsoftx-estensione-chromium-criptovalute/?utm_source=rss&utm_medium=rss&utm_campaign=venomsoftx-estensione-chromium-criptovalute
source: Over Security - Cybersecurity news aggregator
date: 2022-11-24
fetch_date: 2025-10-03T23:40:18.089070
---

# VenomSoftX: l’estensione Chromium che sottrae password e criptovalute

Aggiornamenti recenti Ottobre 3rd, 2025 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)

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

## VenomSoftX: l’estensione Chromium che sottrae password e criptovalute

Nov 23, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Trojan](https://www.securityinfo.it/category/minacce-2/trojan/)
 [0](https://www.securityinfo.it/2022/11/23/venomsoftx-estensione-chromium-criptovalute/#respond)

---

Sono emersi nuovi dettagli su **VenomSoftX, un’estensione malevola dei browser Chromium in grado di ottenere password, criptovalute e contenuti copiati** mentre gli utenti navigano sul web. I primi a individuarla, nel 2020, sono stati i due ricercatori di sicurezza Cerberus e Colin Cowie. Oggi Avast ha pubblicato alcuni dettagli in più sul funzionamento della minaccia.

![VenomSoftX](https://www.securityinfo.it/wp-content/uploads/2022/11/pexels-caio-67112.jpg)

L’estensione **viene installata da ViperSoftX, un malware per Windows**, che agisce come un Remote Access Trojan basato su Javascript. Essa è in grado di accedere a ogni pagina visitata dall’utente, sottrarre credenziali e contenuti copiati dall’utente ed eseguire attacchi man-in-the-browser per **attuare il *cryptocurrency swapping***. Si tratta di una pratica che consiste nello scambiare due criptovalute per modificarne il valore e poi, in molti casi, sottrarle al proprietario.

Lo stesso **ViperSoftX è in grado di ottenere il nome del computer e lo username utente**, oltre a informazioni sul sistema operativo e su eventuali antivirus installati e attivi. **L’estensione, attiva dal 2019, finora ha rubato circa 130.000 dollari in criptovalute**.

**VenomSoftX si installa sui [browser basati su Chromium](https://www.securityinfo.it/2022/11/10/cloud9-prende-il-controllo-di-chrome-e-derivati/)** (Chrome, Brave, Edge, Opera) fingendosi un’estensione lecita; i ricercatori hanno individuato il malware dietro nomi come Google Sheets 2.1 o Update Manager. **L’estensione si inserisce nelle chiamate alle API del server di criptovalute per direzionare la richiesta verso l’attaccante, inviando a lui i soldi**, oppure modificando il body della risposta dal server.

![VenomSoftX](https://www.securityinfo.it/wp-content/uploads/2022/11/pexels-worldspectrum-844124.jpg)

Dal momento che le transazioni sulle blockchain sono irreversibili, quando l’utente si accorge di operazioni sospette sul suo portafoglio è ormai troppo tardi per annullare i pagamenti e bloccare gli attaccanti. **VenomSoftX può anche modificare l’HTML di una pagina web per mostrare all’utente il proprio portafoglio durante le operazioni di manipolazione del suo contenuto.** Oltre a ciò, per il dominio “Blockchain.info”, l’estensione cerca di rubare username e password dell’utente.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chromium](https://www.securityinfo.it/tag/chromium/), [criptovalute](https://www.securityinfo.it/tag/criptovalute/), [cryptocurrency](https://www.securityinfo.it/tag/cryptocurrency/), [cybersicurezza](https://www.securityinfo.it/tag/cybersicurezza/), [Hacking](https://www.securityinfo.it/tag/hacking/), [VenomSoftX](https://www.securityinfo.it/tag/venomsoftx/), [ViperSoftX](https://www.securityinfo.it/tag/vipersoftx/)

[Black Basta ora attacca le aziende statunitensi con Qakbot](https://www.securityinfo.it/2022/11/24/black-basta-ora-attacca-le-aziende-statunitensi-con-qakbot/)
[Il settore dei trasporti nel mirino dello smishing](https://www.securityinfo.it/2022/11/23/il-settore-dei-trasporti-nel-mirino-dello-smishing/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![TeamItaly, presentata la nuova squadra di giovani cyber defender](https://www.securityinfo.it/wp-content/uploads/2025/09/conferenza_stampa_gruppo_TeamItaly_Marco_Cervellini_CNA_e_Paolo_Prinetto_CINI-scaled-120x85.jpg)](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/ "TeamItaly, presentata la nuova squadra di giovani cyber defender")

  [TeamItaly, presentata la nuova squadra...](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/ "Permanent link to TeamItaly, presentata la nuova squadra di giovani cyber defender")

  Set 15, 2025  [0](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/#respond)
* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  [Cina contro Nvidia: dubbi sulla...](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Permanent link to Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  Ago 13, 2025  [0](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/#respond)
* [![Un cartello messicano ha spiato l’FBI hackerando i suoi dispositivi](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_iqghiqiqghiqiqgh-120x85.png)](https://www.securityinfo.it/2025/07/04/un-cartello-messicano-ha-spiato-l-fbi-hackerando-i-suoi-dispositivi/ "Un cartello messicano ha spiato l’FBI hackerando i suoi dispositivi")

  [Un cartello messicano ha spiato...](https:/...