---
title: Black Basta ora attacca le aziende statunitensi con Qakbot
url: https://www.securityinfo.it/2022/11/24/black-basta-ora-attacca-le-aziende-statunitensi-con-qakbot/?utm_source=rss&utm_medium=rss&utm_campaign=black-basta-ora-attacca-le-aziende-statunitensi-con-qakbot
source: Securityinfo.it
date: 2022-11-25
fetch_date: 2025-10-03T23:45:36.815228
---

# Black Basta ora attacca le aziende statunitensi con Qakbot

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

## Black Basta ora attacca le aziende statunitensi con Qakbot

Nov 24, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/)
 [0](https://www.securityinfo.it/2022/11/24/black-basta-ora-attacca-le-aziende-statunitensi-con-qakbot/#respond)

---

Il [Cybereason](https://www.cybereason.com/) Global Soc ha emesso un [threat alert](https://www.cybereason.com/blog/threat-alert-aggressive-qakbot-campaign-and-the-black-basta-ransomware-group-targeting-u.s.-companies) dopo aver effettuato un’accurata indagine per studiare le infezioni **Qakbot** riscontrate presso i clienti.

Obbiettivo di questa campagna, probabilmente orchestrata dal gruppo Black Basta, sono **principalmente aziende statunitensi** che vengono colpite innanzi tutto utilizzando il trojan Qakbot, che crea un primo punto di accesso al computer.

Black Basta è un gruppo ransomware individuato per la prima volta nell’aprile 2022, autore di **attacchi ransomware** e attivo principalmente negli Stati Uniti, Canada, Regno Unito, Australia e Nuova Zelanda.

Questo gruppo utilizza tattiche di **doppia estorsione**: dopo aver rubato i dati alle vittime utilizzano queste informazioni per una vera e propria estorsione, minacciando di renderle pubbliche se non si paga un riscatto.

Qakbot è un **trojan** già noto utilizzato in genere per rubare le credenziali bancarie, ma in questo caso gli attaccanti sfruttano la backdoor integrata per iniettare un payload aggiuntivo, ossia un ransomware.

Inoltre, in molti casi gli attaccanti hanno anche **disabilitato i servizi Dns**, estromettendo il computer dalla rete e quindi rendendo più complesso il ripristino.

![](https://www.securityinfo.it/wp-content/uploads/2022/11/qakbot-1.png)

Lo schema dell’attacco tramite Qakbot (Fonte: Cybereason)

## Veloce e aggressivo

Tra le motivazioni che hanno spinto i ricercatori di Cybereason a redigere un bollettino di allerta, si segnalano **l’estrema rapidità** con cui l’attacco ha luogo: gli attaccanti riescono a ottenere i privilegi di amministratore di dominio in meno di due ore, e passano all’iniezione del malware nel giro di 12 ore.

Obbiettivo della campagna sono attualmente aziende statunitensi, colpite in maniera **massiccia e veloce**: nelle ultime due settimane, infatti, Cybereason ha individuato oltre 10 clienti interessati a questo attacco.

Gli analisti hanno rilevato l’attacco a partire **dallo scorso 14 novembre**, veicolato tramite un’email di phishing che conteneva collegamenti Url malevoli.

Gli attaccanti hanno anche sfruttato **Cobalt Strike** per ottenere l’accesso al controller del dominio, dopodiché l’attacco ha disabilitato i meccanismi di sicurezza e isolato le macchine dalla rete tramite la disabilitazione del Dns.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi](https://www.securityinfo.it/tag/attacchi/), [Black Basta](https://www.securityinfo.it/tag/black-basta/), [Cobalt Strike](https://www.securityinfo.it/tag/cobalt-strike/), [Cybereason](https://www.securityinfo.it/tag/cybereason/), [DNS](https://www.securityinfo.it/tag/dns/), [minacce](https://www.securityinfo.it/tag/minacce/), [Qakbot](https://www.securityinfo.it/tag/qakbot/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [Trojan](https://www.securityinfo.it/tag/trojan/)

[Firewall Sophos sfrutta Xstream per l'Edge Computing](https://www.securityinfo.it/2022/11/24/firewall-sophos-xstream-edge-computing/)
[VenomSoftX: l'estensione Chromium che sottrae password e criptovalute](https://www.securityinfo.it/2022/11/23/venomsoftx-estensione-chromium-criptovalute/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_eubydneubydneuby-120x85.png)](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità")

  [Ricerca FireMon: il 60% dei firewall...](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Permanent link to Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità")

  Ott 01, 2025  [0](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/#respond)
* [![Un attacco supply chain ha compromesso oltre 40 pacchetti NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h-120x85.png)](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  [Un attacco supply chain ha compromesso...](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Permanent link to Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  Set 16, 2025  [0](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/0...