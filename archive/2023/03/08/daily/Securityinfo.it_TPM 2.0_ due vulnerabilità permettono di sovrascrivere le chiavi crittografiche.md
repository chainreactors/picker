---
title: TPM 2.0: due vulnerabilità permettono di sovrascrivere le chiavi crittografiche
url: https://www.securityinfo.it/2023/03/07/tpm-vulnerabilita-chiavi-crittografiche/?utm_source=rss&utm_medium=rss&utm_campaign=tpm-vulnerabilita-chiavi-crittografiche
source: Securityinfo.it
date: 2023-03-08
fetch_date: 2025-10-04T08:56:25.881171
---

# TPM 2.0: due vulnerabilità permettono di sovrascrivere le chiavi crittografiche

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

## TPM 2.0: due vulnerabilità permettono di sovrascrivere le chiavi crittografiche

Mar 07, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/03/07/tpm-vulnerabilita-chiavi-crittografiche/#respond)

---

I ricercatori di Quarkslab [hanno individuato **due vulnerabilità**](https://trustedcomputinggroup.org/wp-content/uploads/TCGVRT0007-Advisory-FINAL.pdf) **buffer overflow nel Trusted Platform Module (TPM) 2.0.** Identificate come CVE-2023-1018 e CVE-2023-1017, rispettivamente una out-of-bounds read e out-of-bounds write, le due falle permettono a un attaccante di accedere a dati sensibili e **sovrascrivere dati protetti come le chiavi crittografiche.**

Il TPM è infatti un modulo hardware-based **usato per creare e memorizzare le [chiavi crittografiche](https://www.securityinfo.it/2023/02/02/sicurezza-quantum-computing-crittografia/)** e confermare che sistema operativo e firmware del dispositivo siano attendibili e non siano stati manomessi. Il modulo **è utilizzato ampiamente dai sistemi Windows**: se prima era opzionale per alcune feature di sicurezza, è diventato obbligatorio per eseguire Windows 11 sui dispositivi.

![tpm vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2023/03/hacked-system-dark-background-3d-illustration.jpg)

Kerfin7 – Freepik

[Come riportato dal CERT Coordination Center](https://kb.cert.org/vuls/id/782720) della Carnegie Mellon University, **le due vulnerabilità riguardano il modo in cui TPM processa alcuni dei parametri presenti nei comandi del modulo**; in particolare, le falle colpiscono la funzione *CryptParameterDecryption*, che non esegue i controlli necessari sulla lunghezza dell’input.

Un attaccante con accesso al dispositivo può inviare comandi creati appositamente per sfruttare le vulnerabilità e **sovrascrivere i dati del modulo per ottenere privilegi di amministratore.**

Le vulnerabilità colpiscono le versioni 1.16, 1.38 e 1.59 di TPM. Trusted Computing Group, società sviluppatrice del modulo Windows, [ha consigliato](https://trustedcomputinggroup.org/resource/errata-for-tpm-library-specification-2-0//) agli amministratori dei sistemi ad **aggiornare TPM rispettivamente alle versioni 1.6 o maggiori, 1.13 o maggiori, e 1.4 o maggiori**.

Come specifica CERT, in alcuni casi **potrebbe essere necessario aggiornare il firmware dei chip TPM** tramite il vendor del sistema operativo o il produttore stesso del dispositivo.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [crittografia](https://www.securityinfo.it/tag/crittografia/), [Out-of-bounds read](https://www.securityinfo.it/tag/out-of-bounds-read/), [out-of-bounds write](https://www.securityinfo.it/tag/out-of-bounds-write/), [tpm 2.0](https://www.securityinfo.it/tag/tpm-2-0/), [trusted platform module](https://www.securityinfo.it/tag/trusted-platform-module/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Windows](https://www.securityinfo.it/tag/windows/)

[Le nuove tecniche d'attacco superano l'autenticazione multifattore](https://www.securityinfo.it/2023/03/08/autenticazione-multifattore-attacchi/)
[GitHub lancia Secret Scanning contro la divulgazione di credenziali](https://www.securityinfo.it/2023/03/06/github-lancia-secret-scanning-contro-la-divulgazione-di-credenziali/)

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
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-...