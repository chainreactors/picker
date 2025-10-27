---
title: Gli attacchi BEC sono sempre più veloci
url: https://www.securityinfo.it/2023/03/17/gli-attacchi-bec-sono-sempre-piu-veloci/?utm_source=rss&utm_medium=rss&utm_campaign=gli-attacchi-bec-sono-sempre-piu-veloci
source: Securityinfo.it
date: 2023-03-18
fetch_date: 2025-10-04T09:59:53.553854
---

# Gli attacchi BEC sono sempre più veloci

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

## Gli attacchi BEC sono sempre più veloci

Mar 17, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [RSS](https://www.securityinfo.it/category/rss/), [Social engineering](https://www.securityinfo.it/category/minacce-2/social-engineering/)
 [0](https://www.securityinfo.it/2023/03/17/gli-attacchi-bec-sono-sempre-piu-veloci/#respond)

---

Il team Security Intelligence di Microsoft ha recentemente proposto un’[analisi dettagliata](https://techcommunity.microsoft.com/t5/microsoft-365-defender-blog/xdr-attack-disruption-in-action-defending-against-a-recent-bec/ba-p/3749822) relativa a un attacco BEC (Business Email Compromise), sottolineando **l’estrema rapidità con cui agiscono gli attaccanti**.

Con la denominazione BEC si indica un metodo utilizzato dai criminali per **accedere a un account email di un’organizzazione**, impersonando una persona di fiducia e convincendo i dipendenti a trasferire denaro o fornire informazioni sensibili.

I criminali utilizzano abitualmente tattiche sofisticate come **il** **phishing e l’ingegneria sociale** per ottenere accesso all’account email della vittima e commettere frodi finanziarie senza essere rilevati.

L’attacco analizzato dal Security Intelligence Team di Microsoft è stato **eseguito nel giro di circa due ore**, dal momento in cui l’attaccante ha ottenuto accesso alle credenziali compromesse fino al dirottamento (hijacking) di un thread di posta elettronica.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/diagram.png)

Fonte: Microsoft Security Intelligence

## La rapidità è un fattore essenziale

Questa rapidità dell’attacco rende difficile per le vittime identificare i segnali di pericolo e adottare misure preventive. Nel caso in esame l’attaccante **ha utilizzato la tecnica “adversary-in-the-middle”** per rubare il cookie di sessione della vittima, e aggirare così la protezione MFA.

Una volta all’interno dell’organizzazione, l’attaccante ha sfruttato la tecnica del thread hijacking, **aggiungendo un messaggio fraudolento come continuazione di una comunicazione** esistente; in questo modo aumentano sensibilmente le probabilità che il destinatario lo consideri legittimo.

L’attaccante ha costruito domini contraffatti e nell’arco di cinque minuti ha **creato una regola di posta** in arrivo per indirizzare i messaggi di un partner commerciale a una cartella specifica.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/email-g11a9473d2_1920.jpg)

Un minuto dopo ha inviato un’e-mail al partner **chiedendo la modifica delle credenziali bancarie** per l’accredito dei bonifici e ha immediatamente eliminato il messaggio inviato per ridurre la probabilità di scoperta essere scoperto.

**L’intera operazione è durata solo 127 minuti**, dimostrando l’estrema efficienza dell’attaccante. L’analisi si chiude però con una nota positiva, perché Microsoft 365 Defender ha rilevato l’attacco e ha disattivato l’account dell’utente compromesso, causando il fallimento del tentativo di frode.

Microsoft ha rivelato che la sua soluzione di sicurezza ha interrotto 38 attacchi BEC rivolti a 27 organizzazioni tramite **l’analisi dei segnali XDR (eXtended Detection and Response)** su endpoint, identità, e-mail e applicazioni SaaS.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [adversary-in-the-middle](https://www.securityinfo.it/tag/adversary-in-the-middle/), [BEC](https://www.securityinfo.it/tag/bec/), [Business Email Compromise](https://www.securityinfo.it/tag/business-email-compromise/), [MFA](https://www.securityinfo.it/tag/mfa/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [thread hijacking](https://www.securityinfo.it/tag/thread-hijacking/), [XDR](https://www.securityinfo.it/tag/xdr/)

[I rischi del lavoro remoto preoccupano le aziende](https://www.securityinfo.it/2023/03/20/rischi-sicurezza-lavoro-remoto/)
[Le minacce più diffuse in EMEA secondo Akamai](https://www.securityinfo.it/2023/03/17/le-minacce-piu-diffuse-in-emea-secondo-akamai/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/wp-content/uploads/2025/10/Home-Odyssey-Cybersecurity-10-03-2025_04_08_PM-120x85.png)](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/ "Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia")

  [Clearskies: la suite di sicurezza...](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/ "Permanent link to Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/#respond)
* [![SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024](https://www.securityinfo.it/wp-content/uploads/2025/08/Firewall-8-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  [SonicWall: Akira non sfrutta uno...](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "Permanent link to SonicWall: Akira non sfrutta...