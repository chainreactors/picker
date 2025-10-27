---
title: Circola una nuova versione di Qilin, ancora più potente
url: https://www.securityinfo.it/2024/10/30/circola-una-nuova-versione-di-qilin-ancora-piu-potente/?utm_source=rss&utm_medium=rss&utm_campaign=circola-una-nuova-versione-di-qilin-ancora-piu-potente
source: Securityinfo.it
date: 2024-10-31
fetch_date: 2025-10-06T18:57:30.376739
---

# Circola una nuova versione di Qilin, ancora più potente

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

## Circola una nuova versione di Qilin, ancora più potente

Ott 30, 2024  [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/ "Articoli scritti da Valentina Caruso")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/10/30/circola-una-nuova-versione-di-qilin-ancora-piu-potente/#respond)

---

Una nuova versione di Qilin attacca mietendo vittime grazie a una crittografia più potente e a una **capacità migliorata di interrompere i tradizionali meccanismi di recupero dat****i**. Non solo: questa versione evoluta del ransomware Qilin riesce a ingannare i principali strumenti di sicurezza in circolazione in modo più efficiente rispetto al passato.

A raccontare le caratteristiche di questo Qilin.B è [Halcyon](https://www.halcyon.ai/). I suoi ricercatori specializzati in cyber sicurezza hanno messo in guardia le aziende e **condiviso alcuni consigli per rilevare più velocemente la minaccia**.

## Nuova minaccia, funzionamento noto

Qilin.B prende di mira sia le directory locali sia le cartelle di rete e **genera delle richieste di riscatto per ogni directory elaborata**, incluso l’ID della vittima. **Non parliamo di un ransomware rivoluzionario**, ma un suo attacco può avere una portata molto pesante e di vasta portata, soprattutto se combinato ad altre tipologie di attacchi.

![nuova versione di Qilin](https://www.securityinfo.it/wp-content/uploads/2024/10/nuova-versione-di-Qilin.jpeg)

## Quando la nuova versione di Qilin entra in azione

Al momento dell’esecuzione, il nuovo malware Qilin.B **aggiunge una chiave di esecuzione automatica nel Registro di sistema di Windows** per assicurarsi di agire indisturbato. Quindi, **fa terminare una serie di processi**, così da disabilitare gli strumenti di sicurezza ostili e **ottimizzare le operazioni di crittografia fraudolente**. Tra i processi che vengono bloccati ci sono Veeam (backup e ripristino), SQL database services (gestione dei dati aziendali), Sophos (software antivirus e di sicurezza), Acronis Agent (servizio di backup e ripristino) e molti altri ancora.

## Sistema di crittografia più potente

La nuova versione di Qilin può contare su uno schema di crittografia più performante rispetto al passato. Qilin.B, infatti, **sfrutta AES-256-CTR con funzionalità AESNI per le CPU che lo supportano**, velocizzando la crittografia. Inoltre, usa anche RSA-4096 con schema OAEP padding per la protezione della chiave di crittografia, **rendendo quasi impossibile la decifratura senza la chiave privata**.

Le copie shadow di Windows esistenti vengono cancellate per impedire un facile ripristino del sistema e **i registri eventi di Windows vengono anch’essi eliminati,** ostacolando in via preventiva un’eventuale analisi forense.

## Come e dove colpisce

La scorsa estate, Sophos ha rivelato che **la nuova versione Qilin distribuisce un info-stealer personalizzato negli attacchi**, per raccogliere credenziali archiviate nel browser Google Chrome. L’obiettivo è estendere la minaccia e introdursi in un secondo momento nelle reti violate o **attaccare intere Reti**. Qilin.B è stato già usato in attacchi molto dannosi diretti, per esempio, contro l’azienda automotive Yanfeng e alcuni importanti ospedali di Londra.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco ransomware](https://www.securityinfo.it/tag/attacco-ransomware/), [crittografia](https://www.securityinfo.it/tag/crittografia/), [Windows](https://www.securityinfo.it/tag/windows/)

[Malware mobile in aumento: trovate oltre 200 applicazioni dannose sul Google Play Store](https://www.securityinfo.it/2024/10/31/malware-mobile-in-aumento-trovate-oltre-200-applicazioni-dannose-sul-google-play-store/)
[Spectre è ancora presente nei nuovi processori Intel e AMD](https://www.securityinfo.it/2024/10/30/spectre-e-ancora-presente-nei-nuovi-processori-intel-e-amd/)

---

![](https://secure.gravatar.com/avatar/0a083e115b9328218407201798ab82c0?s=90&d=mm&r=g)

##### [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/)

##### Articoli correlati

* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  Set 09, 2025  [0](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/#respond)
* [![Fog ransomware, un ransomware anomalo a una finanziaria asiatica](https://www.securityinfo.it/wp-content/uploads/2025/06/Ransomware16-giu-2025CG-120x85.png)](https://www.securityinfo.it/2025/06/17/fog-ransomware-un-ransomware-anomalo-a-una-finanziaria-asiatica/ "Fog ransomware, un ransomware anomalo a una finanziaria asiatica")

  [Fog ransomware, un ransomware anomalo a...](https://www.securityinfo.it/2025/06/17/fog-ransomware-un-ransomware-anomalo-a-una-finanziaria-asiatica/ "Permanent link to Fog ransomware, un ransomware anomalo a una finanziaria asiatica")

  Giu 17, 2025  [0](https://www.securityinfo.it/2025/06/17/fog-ransomware-un-ransomware-anomalo-a-una-finanziaria-asiatica/#respond)
* [![Scoperto un RAT per Windows che corrompe gli header DOS e PE per l’elusione](https://www.securityinfo.it/wp-content/uploads/2025/05/banner-5185767_1920-120x85.jp...