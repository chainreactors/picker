---
title: Okta rileva un importante aumento di attacchi di credential stuffing
url: https://www.securityinfo.it/2024/04/30/okta-rileva-un-importante-aumento-di-attacchi-di-credential-stuffing/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-01
fetch_date: 2025-10-06T17:20:07.891437
---

# Okta rileva un importante aumento di attacchi di credential stuffing

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

## Okta rileva un importante aumento di attacchi di credential stuffing

Apr 30, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/04/30/okta-rileva-un-importante-aumento-di-attacchi-di-credential-stuffing/#respond)

---

Nell’ultimo mese **Okta** [ha osservato](https://sec.okta.com/blockanonymizers) un preoccupante **aumento nella frequenza e nella scala di attacchi di credential stuffing** diretti ai propri servizi.

La notizia arriva dopo che Cisco Talos [aveva rilevato](https://www.securityinfo.it/2024/04/18/in-aumento-gli-attacchi-brute-force-a-vpn-e-servizi-ssh/) un **aumento degli attacchi brute force su larga scala nel periodo 18 marzo – 16 aprile** contro numerosi modelli di dispositivi VPN; in seguito, Okta ha scoperto un importante incremento di attività di credential stuffing dal 19 al 26 aprile.

Gli attaccanti sono riusciti a effettuare il login ai servizi sfruttando username e password ottenuti da precedenti breach che hanno coinvolto altre entità e da campagne phishing e malware.

I ricercatori della compagnia hanno spiegato che gli attacchi sono stati facilitati anche dall’**usodiffusione di servizi proxy residenziali** e dalla disponibilità di tool di scripting (Il post sul blog di Okta è stato modificato dopo l’uscita del nostro pezzo rimuovendo i nomi dei servizi citati originariamente); inoltre, gli attaccanti hanno sfruttato servizi di anonimizzazione come TOR per effettuare il routing delle richieste.

![](https://www.securityinfo.it/wp-content/uploads/2024/04/hacking-3112539_1920-1.png)

Pixabay

La compagnia ha rivelato che gli attacchi sono stati particolarmente efficaci contro le organizzazioni che eseguivano **Okta Classic Engine** e con **ThreatInsight configurato in modalità Audit-only** e non con le consigliate Log o Enforce. In tutti questi casi le compagnie avevano anche delle policy di autenticazione che consentivano le richieste da proxy anonimizzati; al contrario, le organizzazioni che usano Okta Identity Engine e ThreatInsight in modalità Log o Enforce non hanno sofferto breach di dati.

Per proteggersi da questi attacchi, Okta consiglia alle organizzazioni di **bloccare le richieste provenienti da servizi anonimizzati**, impostare ThreatInsight nelle modalità consigliate, utilizzare Identity Engine e implementare Dynamic Zones per specificare indirizzi IP da bloccare.

I ricercatori ricordano inoltre di **preferire l’approccio passwordless per l’autenticazione** o, se non è possibile, implementare l’autenticazione multifattore e imporre agli utenti di utilizzare password robuste; inoltre, è indispensabile monitorare il traffico e **bloccare richieste e IP sospetti.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [brute-force](https://www.securityinfo.it/tag/brute-force/), [credential stuffing](https://www.securityinfo.it/tag/credential-stuffing/), [MFA](https://www.securityinfo.it/tag/mfa/), [Okta](https://www.securityinfo.it/tag/okta/), [proxy residenziali](https://www.securityinfo.it/tag/proxy-residenziali/), [Tor](https://www.securityinfo.it/tag/tor/)

[Microsoft "rompe" la VPN con l'ultimo update per Windows](https://www.securityinfo.it/2024/05/02/microsoft-rompe-la-vpn-con-lultimo-update-per-windows/)
[I siti di phishing legati a USPS ricevono più richieste del dominio legittimo](https://www.securityinfo.it/2024/04/29/i-siti-di-phishing-legati-a-usps-ricevono-piu-richieste-del-dominio-legittimo/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  [Ondata di attacchi brute-force contro...](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Permanent link to Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  Ago 12, 2025  [0](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/#respond)
* [![SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024](https://www.securityinfo.it/wp-content/uploads/2025/08/Firewall-8-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  [SonicWall: Akira non sfrutta uno...](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "Permanent link to SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  Ago 08, 2025  [0](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/#respond)
* [![PoisonSeed è riuscito ad aggirare la protezione FIDO](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_ud7ej8ud7ej8ud7e-120x85.png)](https://www.securityinfo.it/2025/07/21/poisonseed-e-riuscito-ad-aggirare-la-protezione-fido/ "PoisonSeed è riuscito ad aggirare la protezione FIDO")

  [PoisonSeed è riuscito ad aggirare la...](https://www.securityinfo.it/2025/07/21/poisonseed-e-riuscito-ad-aggirare-la-prot...