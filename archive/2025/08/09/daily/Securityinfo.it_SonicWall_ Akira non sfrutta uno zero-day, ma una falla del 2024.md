---
title: SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024
url: https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/?utm_source=rss&utm_medium=rss&utm_campaign=sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024
source: Securityinfo.it
date: 2025-08-09
fetch_date: 2025-10-07T00:49:41.770185
---

# SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024

Ago 08, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/#respond)

---

SonicWall ha smentito l’ipotesi che i recenti attacchi ransomware **Akira** contro firewall Gen 7 con **SSLVPN** attivo siano dovuti a una nuova vulnerabilità. Secondo l’azienda, i cybercriminali stanno invece sfruttando la **CVE-2024-40766**, una falla di **controllo degli accessi** in SonicOS corretta nell’agosto 2024, ma che aveva bisogno di una procedura più estesa del solito per esser corretta.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/Firewall-8-ago-2025CG-1024x683.png)

In un aggiornamento pubblicato questa settimana sul bollettino di sicurezza, SonicWall afferma di avere un alto grado di certezza sul fatto che le attività osservate non siano legate a uno zero-day, ma alla falla già documentata nella precedente advisory SNWLID-2024-0015. La **CVE-2024-40766** consente a un attaccante di ottenere accesso non autorizzato agli endpoint vulnerabili, dirottare sessioni attive o entrare nella rete tramite VPN, aggirando i controlli di protezione.

La vulnerabilità era stata ampiamente sfruttata dopo la sua divulgazione, con operatori ransomware come **Akira** e **Fog** che l’avevano utilizzata per penetrare nelle reti aziendali. Lo scorso venerdì, **Arctic Wolf Labs** aveva ipotizzato l’esistenza di un nuovo zero-day nei firewall Gen 7, basandosi su pattern di attacco compatibili con le campagne Akira. Questo aveva spinto SonicWall a consigliare ai clienti di disattivare temporaneamente i servizi SSLVPN e limitare la connettività ai soli indirizzi IP fidati.

Le indagini interne condotte su 40 incidenti hanno però portato a una conclusione diversa: in molti casi, la vulnerabilità è stata sfruttata perché, durante la migrazione da firewall **Gen 6** a **Gen 7**, le **password locali degli utenti** sono state mantenute inalterate, contrariamente alle indicazioni contenute nella prima advisory. SonicWall ricorda che il reset delle credenziali era un passaggio **critico** per mitigare la falla.

L’azienda raccomanda ora di aggiornare il firmware alla versione **7.3.0 o successiva**, che introduce protezioni più robuste contro attacchi brute-force e l’autenticazione multifattoriale (**MFA**), e di reimpostare tutte le password locali, soprattutto quelle utilizzate per l’accesso SSLVPN.

Non tutti, però, sembrano convinti. Su Reddit, diversi clienti hanno espresso dubbi sull’accuratezza del resoconto di SonicWall, riportando violazioni su account creati solo dopo la migrazione e lamentando che il vendor abbia rifiutato di analizzare i loro log. Resta da vedere quanto le violazioni connesse a questi post siano davvero correlati al resto della campagna di Akira e quanti siano invece relativi a eventi diversi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Akira ransomware](https://www.securityinfo.it/tag/akira-ransomware/), [Arctic Wolf Labs](https://www.securityinfo.it/tag/arctic-wolf-labs/), [attacco informatico](https://www.securityinfo.it/tag/attacco-informatico/), [brute force protection](https://www.securityinfo.it/tag/brute-force-protection/), [CVE-2024-40766](https://www.securityinfo.it/tag/cve-2024-40766/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [MFA](https://www.securityinfo.it/tag/mfa/), [migrazione Gen 6 a Gen 7](https://www.securityinfo.it/tag/migrazione-gen-6-a-gen-7/), [password locali](https://www.securityinfo.it/tag/password-locali/), [sicurezza IT](https://www.securityinfo.it/tag/sicurezza-it/), [SonicOS](https://www.securityinfo.it/tag/sonicos/), [SonicWall](https://www.securityinfo.it/tag/sonicwall/), [SSLVPN](https://www.securityinfo.it/tag/sslvpn/), [violazione dati](https://www.securityinfo.it/tag/violazione-dati/), [vulnerabilità firewall](https://www.securityinfo.it/tag/vulnerabilita-firewall/)

[CERT-AGID 2 – 8 agosto: rubati documenti d’identità a clienti di hotel italiani](https://www.securityinfo.it/2025/08/11/cert-agid-2-8-agosto-rubati-documenti-didentita-a-clienti-di-hotel-italiani/)
[Anche Google vittima della campagna di ShinyHunters](https://www.securityinfo.it/2025/08/07/anche-google-vittima-della-campagna-di-shinyhunters/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali](https://www.securityinfo.it/wp-content/uploads/2025/09/cyber-security-3411499_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/ "SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali")

  [SonicWall vittima di un breach, la...](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/ "Permanent link to SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali")

  Set 19, 2025  [0](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/#respond)
* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it...