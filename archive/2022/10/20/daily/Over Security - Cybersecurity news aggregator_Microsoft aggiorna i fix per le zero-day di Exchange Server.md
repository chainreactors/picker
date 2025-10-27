---
title: Microsoft aggiorna i fix per le zero-day di Exchange Server
url: https://www.securityinfo.it/2022/10/08/microsoft-fix-zero-day-exchange-server/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-fix-zero-day-exchange-server
source: Over Security - Cybersecurity news aggregator
date: 2022-10-20
fetch_date: 2025-10-03T20:24:24.076007
---

# Microsoft aggiorna i fix per le zero-day di Exchange Server

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

## Microsoft aggiorna i fix per le zero-day di Exchange Server

Ott 08, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/10/08/microsoft-fix-zero-day-exchange-server/#respond)

---

**Microsoft** ha aggiornato i **fix per le vulnerabilità zero-day di Exchange Server**. Le due falle di sicurezza erano state individuate il 30 settembre e l’azienda aveva subito rilasciato dei fix, che però **si sono rivelati insufficienti.** Microsoft è quindi corsa ai ripari e li ha aggiornati nei giorni seguenti.

Le vulnerabilità erano due, identificate come **CVE-2022-41040** e **CVE-2022-41082**. La loro particolarità sta nel fatto che, **sfruttata la prima, è possibile innescare la seconda**. La prima vulnerabilità permette di **aumentare i privilegi di un utente fino a renderlo admin**; la seconda invece permette di **eseguire codice remoto sui server** di Exchange di Microsoft.

Microsoft ha rilasciato delle patch per risolvere il problema il prima possibile, ma ha anche confermato che **almeno 10 organizzazioni in tutto il mondo hanno subito attacchi** che hanno sfruttato queste vulnerabilità. Per un attaccante è sufficiente ottenere i dati di autenticazione di un utente e poi aumentare i propri privilegi di sistema.

![Microsoft Exchange Server](https://www.securityinfo.it/wp-content/uploads/2022/10/log-in-g7bde84c97_1280.png)

Per mitigare la minaccia Microsoft ha invitato gli amministratori delle reti Exchange a seguire **due procedure**, illustrandole sul [blog di Security Response Center](https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/).

La prima cosa da fare è **aggiungere una regola di riscrittura URL per bloccare il pattern di attacco**. Per fare ciò è sufficiente aprire l’IIS Manager, accedere alla feature *URL Rewrite*e aggiungere una nuova regola di tipo “Request Blocking”. A questo punto bisogna inserire la stringa “**.\*autodiscover\.json.\*Powershell.\***” e indicare “Abort Request” come azione da intraprendere.

La seconda cosa da fare è **disabilitare l’accesso ai server remoti** **tramite PowerShell** per tutti gli utenti non amministratori. Di default, infatti, qualsiasi tipologia di utente ha i permessi per accedere a una shell remota.

Oltre a queste indicazioni Microsoft consiglia di attivare la **protezione Cloud-Delivered** di Defender e quella di rete, **eseguire EDR in modalità*****block***e usare la funzionalità ***device discovery*** per individuare dispositivi non gestiti nella propria rete.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [fix](https://www.securityinfo.it/tag/fix/), [hacker](https://www.securityinfo.it/tag/hacker/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Microsoft Exchange Server](https://www.securityinfo.it/tag/microsoft-exchange-server/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[L'esercito U.S.A. monitora il traffico internet globale con Augury](https://www.securityinfo.it/2022/10/09/augury-esercito-americano-dati-navigazione/)
[Backdoor Maggie trovata in centinaia di server Microsoft SQL](https://www.securityinfo.it/2022/10/07/backdoor-maggie-trovata-in-centinaia-di-server-microsoft-sql/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabil...