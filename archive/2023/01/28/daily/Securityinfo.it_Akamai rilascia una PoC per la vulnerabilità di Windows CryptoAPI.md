---
title: Akamai rilascia una PoC per la vulnerabilità di Windows CryptoAPI
url: https://www.securityinfo.it/2023/01/27/akamai-windows-cryptoapi-poc/?utm_source=rss&utm_medium=rss&utm_campaign=akamai-windows-cryptoapi-poc
source: Securityinfo.it
date: 2023-01-28
fetch_date: 2025-10-04T05:06:30.186509
---

# Akamai rilascia una PoC per la vulnerabilità di Windows CryptoAPI

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

## Akamai rilascia una PoC per la vulnerabilità di Windows CryptoAPI

Gen 27, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/01/27/akamai-windows-cryptoapi-poc/#respond)

---

**I ricercatori di Akamai hanno pubblicato una Proof of Concept relativa a una vulnerabilità di Windows CryptoAPI**, interfaccia per la crittografia delle applicazioni Windows-based. La vulnerabilità, identificata come CVE-2022-34689, è considerata di livello alto, con un punteggio di 7.5 del CVSS score.

**La vulnerabilità permette a un attaccante di manipolare lo standard X.509 per eseguire un attacco di spoofing**, quindi falsificando la propria identità, per eseguire azioni di autenticazione su connessioni, codice e allegati; lo standard in esame, infatti, definisce il formato dei certificati a chiave pubblica e delle autorità di certificazione.

![Windows CryptoAPI](https://www.securityinfo.it/wp-content/uploads/2023/01/cyber-security-6848265_1280.jpg)

La falla non è nuova: era stata patchata da Microsoft lo scorso agosto, anche se l’annuncio pubblico era avvenuto soltanto qualche mese dopo, a ottobre. In questi giorni Akamai ha rilasciato una Proof of Concept per illustrare le fasi dell’attacco e le conseguenze a cui porta.

## La vulnerabilità di Windows CryptoAPI

**Alla base del bug c’è MD5, una funzione di hash nota per soffrire di collisioni,** e di conseguenza considerata debole e deprecata dagli esperti di sicurezza; tuttavia, la funzione è ancora usata in gran parte delle applicazioni moderne.

Come indicato dai [ricercatori Akamai](https://www.securityinfo.it/2022/12/02/akamai-attacchi-web-app-api/), **l’attacco si svolge in due fasi: nella prima gli attaccanti modificano un certificato legittimo per fornirlo alla vittima; in seguito, creano un nuovo certificato il cui hash MD5 collide con quello del certificato legittimo**. A questo punto gli attaccanti possono usare il loro nuovo certificato per fingersi quello originale, ottenendo libero accesso alle risorse della vittima e compromettendo le comunicazioni.

![Windows CryptoAPI](https://www.securityinfo.it/wp-content/uploads/2023/01/password-security-4993196_1280.png)

**Microsoft ha affermato che al momento non ci sono evidenze di attacchi che hanno sfruttato la vulnerabilità.** Le ultime versioni dei prodotti che usano CryptoAPI non soffrono della falla, ma **la quasi totalità delle istanze sul web è vulnerabile: secondo i ricercatori, meno dell’1% dei dispositivi visibili sul web è aggiornato.** Akamai consiglia di aggiornare tutti i server e gli endpoint con le ultime patch di sicurezza rilasciate dall’azienda.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Akamai](https://www.securityinfo.it/tag/akamai/), [certificato digitale](https://www.securityinfo.it/tag/certificato-digitale/), [crittografia](https://www.securityinfo.it/tag/crittografia/), [CryptoAPI](https://www.securityinfo.it/tag/cryptoapi/), [MD5](https://www.securityinfo.it/tag/md5/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [proof-of-concept](https://www.securityinfo.it/tag/proof-of-concept/), [Windows](https://www.securityinfo.it/tag/windows/), [x.509](https://www.securityinfo.it/tag/x-509/)

[La minaccia cyber: cosa aspettarsi nel 2023 secondo Trend Micro](https://www.securityinfo.it/2023/01/27/la-minaccia-cyber-cosa-aspettarsi-nel-2023-secondo-trend-micro/)
[I malware più interessanti del 2022 per Palo Alto Networks](https://www.securityinfo.it/2023/01/26/i-malware-piu-interessanti-del-2022-per-palo-alto-networks/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  Set 09, 2025  [0](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/#respond)
* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74-120x85.png)](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  [Secret Blizzard attacca le ambasciate...](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Permanent link to Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/#respond)
* [![Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-120x85.png)](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-trad...