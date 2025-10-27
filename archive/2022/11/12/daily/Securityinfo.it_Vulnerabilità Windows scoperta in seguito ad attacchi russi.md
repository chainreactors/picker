---
title: Vulnerabilità Windows scoperta in seguito ad attacchi russi
url: https://www.securityinfo.it/2022/11/11/vulnerabilita-windows-cyberspionaggio-russo/?utm_source=rss&utm_medium=rss&utm_campaign=vulnerabilita-windows-cyberspionaggio-russo
source: Securityinfo.it
date: 2022-11-12
fetch_date: 2025-10-03T22:35:52.878793
---

# Vulnerabilità Windows scoperta in seguito ad attacchi russi

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

## Vulnerabilità Windows scoperta in seguito ad attacchi russi

Nov 11, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/11/11/vulnerabilita-windows-cyberspionaggio-russo/#respond)

---

È stata individuata **un’importante vulnerabilità di Windows in seguito ad attacchi di cyberspionaggio da parte di hacker russi**. La falla riguarda la funzionalità “credential roaming” che gestisce i certificati per ciascun utente.

La vulnerabilità è stata **scoperta durante l’analisi delle query LDAP eseguite da APT29**, un gruppo russo di cyberspionaggio finanziato dal servizio di intelligence russo. Le query erano dirette al sistema di Active Directory di Windows per sottrarre credenziali.

![Vulnerabilità Windows](https://www.securityinfo.it/wp-content/uploads/2022/11/cyber-security-3374252_1280.jpg)

Uno degli attributi specificato nelle query era msPKI-CredentialRoamingTokens, relativo alla memorizzazione dei token criptati per le credenziali utente. La vulnerabilità, valutata di gravità 7.3 su 10, **permetteva agli attaccanti di eseguire codice da remoto sulle macchine senza i privilegi necessari.**

La funzionalità è usata per sincronizzare le informazioni di login tra diversi device e usare così un solo certificato per utente, senza doverlo duplicare ogni volta. Il credential roaming usa la libreria dimsjob.dll per ottenere i dati da msPKI-AccountCredentials e sincronizzare le informazioni.

Durante questo processo i ricercatori di Mandiant hanno individuato una vulnerabilità legata alla sanificazione del path che indica la posizione delle credenziali: **un attaccante che ha accesso all’attributo delle credenziali dell’account può inserire un token malevolo che contiene codice per creare file eseguibili e lanciarli.**

![Vulnerabilità windows](https://www.securityinfo.it/wp-content/uploads/2022/11/office-4857268_1280.jpg)

Aggiornando gli attributi, il credential roaming innesca la sincronizzazione delle informazioni su ogni computer in cui la vittima effettuerà il login da quel momento in poi. **Ad ogni login verrà quindi eseguito il codice malevolo inserito dalla query LDAP creata ad hoc**.

Lo scorso settembre **Windows ha rilasciato una patch per la vulnerabilità**; occorre quindi aggiornare i sistemi che utilizzano il credential roaming. Prima di questo è necessario però seguire un processo di pulizia della funzionalità: per prima cosa bisogna disabilitare la group policy per il credential roaming; in seguito si dovranno cancellare le credenziali dall’Active Directory. È fondamentale eseguire i passi in quest’ordine.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Active Directory](https://www.securityinfo.it/tag/active-directory/), [credential roaming](https://www.securityinfo.it/tag/credential-roaming/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [cybersicurezza](https://www.securityinfo.it/tag/cybersicurezza/), [cyberspionaggio](https://www.securityinfo.it/tag/cyberspionaggio/), [falla](https://www.securityinfo.it/tag/falla/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Windows](https://www.securityinfo.it/tag/windows/)

[Tre vulnerabilità scoperte nel server Web OpenLiteSpeed](https://www.securityinfo.it/2022/11/14/tre-vulnerabilita-scoperte-nel-server-web-openlitespeed/)
[La sicurezza nelle Pmi non è al passo con il lavoro ibrido](https://www.securityinfo.it/2022/11/11/la-sicurezza-nelle-pmi-non-e-al-passo-con-il-lavoro-ibrido/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità criti...