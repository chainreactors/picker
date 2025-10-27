---
title: WithSecure scopre una falla nella crittografia di Office 365
url: https://www.securityinfo.it/2022/10/22/withsecure-falla-crittografia-office-365/?utm_source=rss&utm_medium=rss&utm_campaign=withsecure-falla-crittografia-office-365
source: Over Security - Cybersecurity news aggregator
date: 2022-10-23
fetch_date: 2025-10-03T20:41:44.741505
---

# WithSecure scopre una falla nella crittografia di Office 365

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

## WithSecure scopre una falla nella crittografia di Office 365

Ott 22, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/10/22/withsecure-falla-crittografia-office-365/#respond)

---

**WithSecure**, conosciuta anche come F-Secure, un’azienda finlandese di software per la sicurezza informatica, **ha individuato una falla nella crittografia dei messaggi di Office 365.**

**OME (Office 365 Message Encryption) è il servizio di [crittografia](https://www.securityinfo.it/2022/08/05/crittografia-per-lera-dei-computer-quantistici/) per le email di Office**, inviate sia all’interno che all’esterno del proprio network. **La vulnerabilità è dovuta all’implementazione di Electronic Codebook (ECB)**, conosciuta per soffrire della perdita di informazioni strutturali dai messaggi.

**Un attaccante in grado di sfruttare la falla nella crittografia di Office 365 può accedere all’intero contenuto dei messaggi**. L’attaccante può agire anche offline: questo significa che potrebbe compromettere anche i messaggi precedenti.

La vulnerabilità di ECB sta nel fatto che ogni blocco di cifratura viene criptato individualmente e **i diversi blocchi di una stessa email vengono codificati sempre con la stessa chiave**; questo significa che ogni blocco che contiene la stessa sequenza di dati produce lo stesso blocco cifrato.

![Falla crittografia Office 365](https://www.securityinfo.it/wp-content/uploads/2022/10/cyber-ge496b026a_1280.jpg)

Essendo così semplice, questa tecnica rivela informazioni sulla struttura del messaggio cifrato. Un attaccante che ha un numero sufficiente di email OME p**uò individuare i pattern ripetuti e ricavare parte del o tutto il contenuto del messaggio.**

““Gli attaccanti che riescono a mettere le mani su più messaggi possono utilizzare le informazioni BCE trapelate per carpire il contenuto crittografato. Con un numero maggiore di email questo processo diventa più semplice e accurato, quindi **è un’operazione che gli attaccanti possono eseguire dopo essere riusciti ad accedere ad archivi di email rubati durante un data breach**, oppure introducendosi nell’account di posta elettronica di qualcuno, nel server di posta elettronica o ottenendo l’accesso ai backup” ha detto **Harry Sintonen**, il ricercatore di WithSecure che ha scoperto il problema.

WithSecure ha condiviso con Microsoft i risultati della sua ricerca, ma **l’azienda, pur comprendendo i rischi, ha deciso di non modificare l’implementazione.**

L’unica cosa che possono fare gli utenti, quindi, è **non utilizzare il metodo OME**, anche se questo non serve a proteggere le vecchie email scambiate con quel tipo di crittografia.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [email](https://www.securityinfo.it/tag/email/), [falla](https://www.securityinfo.it/tag/falla/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [microsot office](https://www.securityinfo.it/tag/microsot-office/), [sicurezza informatica](https://www.securityinfo.it/tag/sicurezza-informatica/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [WithSecure](https://www.securityinfo.it/tag/withsecure/)

[GitHub, migliaia di repository PoC sono falsi o malevoli](https://www.securityinfo.it/2022/10/24/github-poc-false-repository/)
[CISA individua nuove vulnerabilità per Advantech e Hitachi](https://www.securityinfo.it/2022/10/21/cisa-vulnerabilita-advantech-hitachi/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attacca...