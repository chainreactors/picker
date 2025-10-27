---
title: SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali
url: https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/?utm_source=rss&utm_medium=rss&utm_campaign=sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali
source: Securityinfo.it
date: 2025-09-20
fetch_date: 2025-10-02T20:26:15.758473
---

# SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali

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

## SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali

Set 19, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Gestione dati](https://www.securityinfo.it/category/news/gestione-dati-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/#respond)

---

**SonicWall** [ha confermato](https://www.sonicwall.com/support/knowledge-base/mysonicwall-cloud-backup-file-incident/250915160910330) di essere stata **vittima di un breach** che ha colpito il servizio di backup cloud dei firewall. La compagnia sta ora chiedendo ai propri clienti di **resettare urgentemente le credenziali** dei servizi.

Nel dettaglio, gli attaccanti son riusciti ad **accedere ai file di backup delle configurazioni dei firewall** memorizzati e gestiti su MySonicWall.com. Secondo l’analisi della [compagnia](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/), sono stati sottratti file relativi a meno del 5% dei propri clienti. “*Nonostante le credenziali memorizzate nei file siano criptate, i file includono anche informazioni che semplificano potenziali exploit legati ai fireall*” ha sottolineato SonicWall.

La compagnia ha affermato che non si è trattato di un attacco ransomware, ma di una serie di **attacchi bruteforce mirati.** Al momento non ci sono indicazioni sui possibili autori degli attacchi.

![SonicWall](https://www.securityinfo.it/wp-content/uploads/2025/09/cyber-security-3411499_1920.jpg)

Per verificare se i propri file di configurazione sono stati compromessi, è necessario effettuare il login al proprio account MySonicWall e verificare lo stato dei backup cloud. Se non ci sono backup per i firewall, allora non si è a rischio; in caso contrario, occorre verificare se il numero seriale del firewall (indicato sempre nella sezione dei backup) è presente nella sezione “Issue List” della piattaforma.

Nel caso in cui il numero di serie non sia presente nella lista, è comunque importante **seguire gli aggiornamenti della compagnia** per rilasci di eventuali informazioni e guide aggiuntive

In caso positivo, è fondamentale resettare immediatamente le password seguendo la [guida](https://www.sonicwall.com/support/knowledge-base/essential-credential-reset/250909151701590) fornita dalla compagnia. I clienti sono caldamente invitati, tra le altre cose, a resettare e aggiornare le password e il binding TOTP per tutti gli utenti locali, aggiornare i secret condivisi e resettare le password di tutti gli account email usati per l’automazione dei log.

SonicWall invita inoltre i propri clienti a importare i nuovi file di configurazione disponibili che includono password randomiche per tutti gli utenti, reset del binding TOTP per l’autenticazione e chiavi IPSec VPN randomiche.

Attualmente non ci sono informazioni su possibili leak dei file, ma è essenziale agire il prima possibile per anticipare eventuali incidenti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backup](https://www.securityinfo.it/tag/backup/), [data breach](https://www.securityinfo.it/tag/data-breach/), [firewall](https://www.securityinfo.it/tag/firewall/), [MySonicWall](https://www.securityinfo.it/tag/mysonicwall/), [reset password](https://www.securityinfo.it/tag/reset-password/), [SonicWall](https://www.securityinfo.it/tag/sonicwall/)

[CERT-AGID 13-19 settembre: il phishing punta alle criptovalute](https://www.securityinfo.it/2025/09/22/cert-agid-13-19-settembre-phishing-criptovalute/)
[Cohesity Identity Resilience: da Cohesity e Semperis una soluzione per proteggere le infrastrutture di identità aziendali](https://www.securityinfo.it/2025/09/18/cohesity-identity-resilience-da-cohesity-e-semperis-una-soluzione-per-proteggere-le-infrastrutture-di-identita-aziendali/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_eubydneubydneuby-120x85.png)](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon")

  [Il 60% dei firewall non supera i...](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Permanent link to Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon")

  Ott 01, 2025  [0](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/#respond)
* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www....