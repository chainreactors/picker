---
title: Una vulnerabilità di UEFI Secure Boot permette l’esecuzione di codice durante il boot di sistema
url: https://www.securityinfo.it/2025/01/16/una-vulnerabilita-di-uefi-secure-boot-permette-lesecuzione-di-codice-durante-il-boot-di-sistema/?utm_source=rss&utm_medium=rss&utm_campaign=una-vulnerabilita-di-uefi-secure-boot-permette-lesecuzione-di-codice-durante-il-boot-di-sistema
source: Securityinfo.it
date: 2025-01-17
fetch_date: 2025-10-06T20:13:28.481469
---

# Una vulnerabilità di UEFI Secure Boot permette l’esecuzione di codice durante il boot di sistema

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

## Una vulnerabilità di UEFI Secure Boot permette l’esecuzione di codice durante il boot di sistema

Gen 16, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/01/16/una-vulnerabilita-di-uefi-secure-boot-permette-lesecuzione-di-codice-durante-il-boot-di-sistema/#respond)

---

I ricercatori di ESET [hanno scoperto](https://www.welivesecurity.com/en/eset-research/under-cloak-uefi-secure-boot-introducing-cve-2024-7344/) una nuova **vulnerabilità di Secure Boot dei sistemi UEFI** che consente ai cybercriminali di **eseguire codice arbitrario durante l’avvio del sistema.**

![vulnerabilità secure boot](https://www.securityinfo.it/wp-content/uploads/2025/01/pattern-3232784_1920-1.jpg)

Il bug, tracciato come CVE.2024-7344, è stato trovato in un’**applicazione UEFI** firmata da “Microsoft Corporation UEFI CA 2011”, un’autorità di certificazione dell’azienda di Redmond.

La vulnerabilità è causato da un loader PE custom che consente l’**esecuzione di qualsiasi binario UEFI**, anche quelli non firmati, durante l’avvio del sistema. Un attaccante può sfruttare questo bug per eseguire bootkit malevoli e alterare il corretto funzionamento del sistema operativo.

Normalmente il meccanismo di Secure Boot previene l’esecuzione di malware al caricamento del sistema garantendo che vengano caricati solo software riconosciuti. Questa funzionalità usa i certificati digitali per validare l’autenticità e l’integrità del codice che viene caricato, bloccando quello non legittimo. L’applicazione in questione però, a causa del bug, consente l’**esecuzione di codice senza controlli****di integrità.**

“*Il codice eseguito in questa fase iniziale di avvio può persistere sul sistema, potenzialmente caricando **estensioni kernel malevole che sopravvivono ai riavvii***” [avverte](https://kb.cert.org/vuls/id/529659) il CERT Coordination Center in un avviso.

![](https://www.securityinfo.it/wp-content/uploads/2024/10/security-6901712_1920.jpg)

La compagnia riporta che l’applicazione viene usata in diverse suite di ripristino del sistema di diversi provider. Nel dettaglio, i software colpiti sono: Howyar SysReturn, (versioni precedenti alla 10.2.023\_20240919); Greenware GreenGuard (versioni precedenti alla 10.2.023-20240927); Radix SmartRecovery (versioni precedenti alla 11.2.023-20240927); Sanfong EZ-back System (versioni precedenti alla 10.3.024-20241127); WASAY eRecoveryRX (versioni precedenti alla 8.4.022-20241127); CES NeoImpact (versioni precedenti alla 10.1.024-20241127); SignalComputer HDD King (versioni precedenti alla 10.3.021-20241127).

ESET ha individuato la vulnerabilità lo scorso luglio e ha immediatamente notificato la scoperta al CERT Coordination Center. Insieme all’associazione, ESET ha aiutato i provider a elaborare e validare le **patch risolutive.** Dopo la revoca di Microsoft delle applicazioni UEFI vulnerabili, oggi la compagnia ha reso nota la vulnerabilità.

“*Il numero di vulnerabilità UEFI scoperte negli ultimi anni e l’incapacità di correggerle o di revocare i binari vulnerabili entro un lasso di tempo ragionevole dimostrano che anche una funzione essenziale come **UEFI Secure Boot non dovrebbe essere considerata una barriera*** ***impenetrabile***” hanno commentato i ricercatori.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [bootkit](https://www.securityinfo.it/tag/bootkit/), [malware](https://www.securityinfo.it/tag/malware/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Secure Boot](https://www.securityinfo.it/tag/secure-boot/), [UEFI](https://www.securityinfo.it/tag/uefi/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Microsoft estende Administrator Protection agli utenti Insider](https://www.securityinfo.it/2025/01/17/microsoft-estende-administrator-protection-agli-utenti-insider/)
[Milioni di account Google "defunti" sono vulnerabili a un bug di OAuth](https://www.securityinfo.it/2025/01/15/milioni-di-account-google-defunti-sono-vulnerabili-a-un-bug-di-oauth/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo....