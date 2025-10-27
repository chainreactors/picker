---
title: Un serio bug in Outlook mette a rischio i sistemi Windows
url: https://www.securityinfo.it/2023/03/21/un-serio-bug-in-outlook-mette-a-rischio-i-sistemi-windows/?utm_source=rss&utm_medium=rss&utm_campaign=un-serio-bug-in-outlook-mette-a-rischio-i-sistemi-windows
source: Over Security - Cybersecurity news aggregator
date: 2023-03-22
fetch_date: 2025-10-04T10:17:10.262925
---

# Un serio bug in Outlook mette a rischio i sistemi Windows

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

## Un serio bug in Outlook mette a rischio i sistemi Windows

Mar 21, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Apt](https://www.securityinfo.it/category/minacce-2/apt/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/03/21/un-serio-bug-in-outlook-mette-a-rischio-i-sistemi-windows/#respond)

---

Microsoft ha recentemente corretto **una vulnerabilità in Microsoft Outlook**, identificata come [CVE-2023-23397](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23397), che potrebbe consentire a un attaccante di eseguire un’escalation dei privilegi.

È stata valutata con un livello di gravità 9.8 e coinvolge tutte le versioni di Microsoft Outlook per Windows (sono quindi esclusi i client mobile e la versione macOS) connesse a un server Exchange. La vulnerabilità consente agli aggressori di rubare gli hash di autenticazione NTLM **inviando note o attività di Outlook**.

Questi elementi attivano automaticamente l’exploit quando vengono elaborati dal client, il che potrebbe portare alla compromissione anche senza che l’e-mail venga visualizzata nel riquadro di anteprima. Questo significa che il bersaglio non deve neppure aprire il messaggio per essere compromesso.

Gli attaccanti possono costruire email per far sì che il client della vittima si connetta a un indirizzo UNC esterno, comunicando il l’hash NTLMv2; questa informazione può poi essere utilizzata in altri servizi, consentendo agli attaccanti di **autenticarsi al posto della vittima**.

Nei giorni immediatamente successivi alla divulgazione del problema sono stati **pubblicati diversi exploit proof-of-concept**, che certamente saranno serviti come spunto alla criminalità informatica per realizzare attacchi; il bug è infatti particolarmente pericoloso, perché non è richiesta nessuna azione da parte dell’utente.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/MaliciousEmail_CVE-2023-23397.jpg)

Fonte: MDSec

Secondo Microsoft, un attaccante legato alla Russia ha sfruttato questa vulnerabilità per colpire diverse organizzazioni europee nei settori governativo, dei trasporti, dell’energia e militare.

Si ritiene che **il gruppo dietro gli attacchi sia APT28**, che è stato collegato alla Direzione principale dello Stato Maggiore delle Forze Armate della Federazione Russa (GRU).

Secondo le indiscrezioni emerse, **fino a 15 organizzazioni potrebbero essere state colpite utilizzando questa vulnerabilit**à quando era ancora zero-day, con attacchi registrati da aprile fino a dicembre dello scorso anno.

Dopo aver ottenuto l’accesso, gli attaccanti utilizzano spesso i framework open source Impacket e PowerShell Empire per estendere il controllo e raggiungere i sistemi più preziosi presenti in rete.

## Come proteggersi

Naturalmente, la strada maestra per risolvere la vulnerabilità rimane l’applicazione immediata degli aggiornamenti forniti da Microsoft; se però questa soluzione non è immediatamente percorribile, una mitigazione arriva da Daniel Hofmann, CEO of Hornetsecurity, che consiglia di **bloccare il traffico TCP in uscita verso Internet attraverso la porta 445/SMB**.

“Questa azione **impedisce la trasmissione di messaggi di autenticazione** NTLM a condivisioni file remote, contribuendo a risolvere CVE-2023-23397″, ha spiegato Hofmann.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/1530897904667.jpg)

Daniel Hofmann, CEO of Hornetsecurity

Le aziende devono inoltre **aggiungere gli utenti al gruppo “Utenti protetti” in Active Directory** per impedire l’uso di NTLM come meccanismo di autenticazione.

Inoltre, Microsoft ha reso disponibile **[uno script](https://microsoft.github.io/CSS-Exchange/Security/CVE-2023-23397/) per identificare e modificare (o eliminare) i messaggi** Exchange che contengono percorsi UNC nelle proprietà, e consiglia agli amministratori di eseguirlo per verificare che l’organizzazione è stata compromessa tramite questa vulnerabilità.

## La vulnerabilità dell’anno?

Molti ricercatori e dirigenti di aziende specializzate nella sicurezza IT hanno commentato **i rischi e la portata di questa vulnerabilità**, che è già stata battezzata come il bug dell’anno.

Le motivazioni per considerarla almeno come un serio contendente sono molteplici: innanzi tutto, ha un impatto potenziale su **aziende e singoli utenti di ogni genere**, è laboriosa da risolvere (bisogna applicare gli aggiornamenti a ogni singolo client installato) e non è influenzata neppure dalla cautela degli utenti.

La superficie di attacco è enorme: **la base di utenti di Outlook desktop è infatti molto vasta**, e la vulnerabilità è molto facile da sfruttare, anche grazie alla disponibilità di diversi proof of concept.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT28](https://www.securityinfo.it/tag/apt28/), [Exchange](https://www.securityinfo.it/tag/exchange/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Microsoft Outlook](https://www.securityinfo.it/tag/microsoft-outlook/), [NTLM](https://www.securityinfo.it/tag/ntlm/), [Outlook](https://www.securityinfo.it/tag/outlook/), [UNC](https://www.securityinfo.it/tag/unc/), [Windows](https://www.securityinfo.it/tag/windows/)

[Il ransomware mette nel mirino le infrastrutture critiche](https://www.securityinfo.it/2023/03/21/il-ransomware-mette-nel-mirino-le-infrastrutture-critiche/)
[Rilasciata Kali Purple, la distro Kali Linux per la defensive security](https://www.securityinfo.it/2023/03/21/kali-purple-linux-distro-defensive-security/)

---

![](https://...