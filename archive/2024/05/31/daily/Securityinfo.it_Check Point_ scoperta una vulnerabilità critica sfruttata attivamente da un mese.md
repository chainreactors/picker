---
title: Check Point: scoperta una vulnerabilità critica sfruttata attivamente da un mese
url: https://www.securityinfo.it/2024/05/30/check-point-scoperta-una-vulnerabilita-critica-sfruttata-attivamente-da-un-mese/?utm_source=rss&utm_medium=rss&utm_campaign=check-point-scoperta-una-vulnerabilita-critica-sfruttata-attivamente-da-un-mese
source: Securityinfo.it
date: 2024-05-31
fetch_date: 2025-10-06T16:52:29.757209
---

# Check Point: scoperta una vulnerabilità critica sfruttata attivamente da un mese

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

## Check Point: scoperta una vulnerabilità critica sfruttata attivamente da un mese

Mag 30, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/05/30/check-point-scoperta-una-vulnerabilita-critica-sfruttata-attivamente-da-un-mese/#respond)

---

I ricercatori di mnemonic [hanno scoperto](https://www.mnemonic.io/resources/blog/advisory-check-point-remote-access-vpn-vulnerability-cve-2024-24919/) una **vulnerabilità critica in Check Point Security Gateways**. Il bug colpisce Security Gateways con l’accesso VPN remoto abilitato e alle istanze in cui è attivo Mobile Secure Workspace con Capsule.

Il bug, tracciato come CVE-2024-24919, consente a un attaccante di **enumerare ed estrarre gli hash delle password per tutti gli account locali**, incluso quello usato per connettersi ad Active Directory. Al momento non è chiaro lo scopo dell’attacco, ma è probabile che gli attaccanti vogliano spostarsi lateralmente nella rete e potenzialmente violare account esterni.

Sfruttando la vulnerabilità gli attaccanti potrebbero **divulgare informazioni sensibili** e accedere a servizi VPN che prevedono la password come unico metodo di autenticazione.

I ricercatori parlano di “tentativi” di sfruttamento, lasciando intendere che finora non ci sono stati attacchi andati a buon fine. La situazione è comunque preoccupante, anche perché la vulnerabilità non richiede alcuna interazione utente né privilegi elevati per essere sfruttata.

![](https://www.securityinfo.it/wp-content/uploads/2024/04/cyber-security-1923446_1920.png)

Pixabay

Check Point [ha rivelato](https://blog.checkpoint.com/security/enhance-your-vpn-security-posture) che gli attacchi **sembrano aver colpito solo pochi clienti**, anche se non ha rivelato quanti siano con esattezza. [La compagnia](https://www.securityinfo.it/2024/05/28/check-point-software-potenzia-la-sicurezza-delle-api-con-api-discovery/) ha spiegato di aver individuato i tentativi di sfruttamento solo a partire dal 24 maggio, mentre secondo mnemonic **i tentativi di exploit sarebbero cominciati almeno dal 30 aprile.**

Il bug non è legato a versioni specifiche di software. Check Point ha già rilasciato il fix per la vulnerabilità e invita i suoi utenti ad **applicare il prima possibile la patch**, oltre che a implementare l’autenticazione multi-fattore per account di servizio e amministrativi.

Oltre ad aggiornare le soluzioni Check Point, il team di mnemonic consiglia di **ruotare le password** e gli account per le connessioni LDAP dal gateway ad Active Directory e **controllare i log per individuare qualsiasi segno di compromissione o login sospetto.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Check Point](https://www.securityinfo.it/tag/check-point/), [hash password](https://www.securityinfo.it/tag/hash-password/), [mnemonic](https://www.securityinfo.it/tag/mnemonic/), [VPN](https://www.securityinfo.it/tag/vpn/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[Gli U.S.A. hanno smantellato la botnet 911 S5](https://www.securityinfo.it/2024/05/30/gli-u-s-a-hanno-smantellato-la-botnet-911-s5/)
[Risk hunting, una metodologia proattiva per migliorare la cybersecurity](https://www.securityinfo.it/2024/05/29/risk-hunting-una-metodologia-proattiva-per-migliorare-la-cybersecurity/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una v...