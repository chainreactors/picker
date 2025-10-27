---
title: Possibile zero-day su SonicWall: Akira colpisce le aziende
url: https://www.securityinfo.it/2025/08/05/possibile-zero-day-su-sonicwall-akira-colpisce-le-aziende/?utm_source=rss&utm_medium=rss&utm_campaign=possibile-zero-day-su-sonicwall-akira-colpisce-le-aziende
source: Securityinfo.it
date: 2025-08-06
fetch_date: 2025-10-07T00:49:14.168852
---

# Possibile zero-day su SonicWall: Akira colpisce le aziende

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

## Possibile zero-day su SonicWall: Akira colpisce le aziende

Ago 05, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/08/05/possibile-zero-day-su-sonicwall-akira-colpisce-le-aziende/#respond)

---

Il ransomware Akira torna a far parlare di sé, questa volta per una nuova serie di attacchi che **sembrano sfruttare una vulnerabilità ancora sconosciuta nei firewall SonicWall** di settima generazione. Secondo le indagini di Arctic Wolf, Huntress e altri team di risposta agli incidenti, gli aggressori sarebbero riusciti a violare **sistemi completamente aggiornati**, compromettendo anche dispositivi protetti da autenticazione multifattore.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/ChatGPT-Image-5-ago-2025-19_57_35-1024x683.png)

Le prime segnalazioni risalgono alla seconda metà di luglio 2025, ma attività simili erano già state osservate nei mesi precedenti. SonicWall ha confermato di essere al lavoro per analizzare quanto accaduto, senza escludere al momento l’ipotesi di uno **zero-day**.

### Accessi remoti anomali tramite VPN

Le intrusioni sono avvenute attraverso l’interfaccia SSL VPN dei firewall SonicWall Gen 7. Arctic Wolf ha registrato **accessi non autorizzati provenienti da infrastrutture VPS**, un comportamento coerente con l’attività di gruppi ransomware strutturati. In numerosi casi, gli attaccanti hanno ottenuto rapidamente l’accesso ai controller di dominio, passando alla fase di cifratura nel giro di poche ore.

Anche Huntress ha confermato l’osservazione di accessi malevoli **a partire dal 25 luglio**, seguiti da esecuzioni di payload tramite strumenti come AnyDesk, ScreenConnect o connessioni SSH. Tutti i sistemi colpiti utilizzavano firmware considerato aggiornato, in particolare la versione **7.2.0-7015 e precedenti**, e includevano anche dispositivi con MFA attivo.

### L’ipotesi di una vulnerabilità ancora non documentata

L’elemento più preoccupante emerso dalle analisi è che i sistemi compromessi non presentavano configurazioni deboli o password facili da indovinare. Al contrario, **molte delle aziende colpite avevano implementato MFA** e seguito le best practice di sicurezza raccomandate.

Secondo Arctic Wolf, questi segnali suggeriscono la possibile presenza di una vulnerabilità sfruttabile **senza credenziali valide**, in grado di aggirare le misure di protezione normalmente efficaci. I ricercatori sottolineano che la tempistica e il vettore d’accesso sono coerenti con un attacco mirato basato su una falla zero-day.

SonicWall, in una comunicazione ufficiale, **ha dichiarato di essere a conoscenza della campagna** in corso e di aver avviato un’indagine interna in collaborazione con i partner di sicurezza.

### Tecniche di post-sfruttamento e attacco lampo

Una volta ottenuto l’accesso iniziale, **gli operatori di Akira si muovono rapidamente** per consolidare la loro presenza e cifrare i dati. Le tecniche osservate comprendono l’eliminazione delle copie shadow, la disattivazione dei sistemi di protezione e l’utilizzo di credenziali di dominio per l’escalation dei privilegi.

In diversi casi è stato osservato l’utilizzo di strumenti legittimi già presenti negli ambienti target, secondo una logica di living-off-the-land. **La velocità dell’attacco suggerisce una preparazione accurata**, con playbook ben rodati e infrastrutture di comando e controllo già pronte.

### Mitigazioni consigliate e indicazioni operative

In attesa che venga confermata o smentita la presenza di una vulnerabilità zero-day, gli esperti raccomandano l’adozione immediata di misure difensive. Tra queste:

* Disattivazione dell’accesso VPN SSL per i dispositivi esposti su internet
* Limitazione dell’accesso remoto a indirizzi IP autorizzati
* Rimozione di account locali inutilizzati
* Monitoraggio dei log per individuare accessi anomali
* Segmentazione della rete e rafforzamento dei controlli di accesso

SonicWall ha inoltre invitato gli utenti a implementare funzionalità di sicurezza aggiuntive, come il **Geo-IP Filtering, la protezione Botnet e il logging avanzato**. Dove possibile, è consigliata l’adozione di sistemi di rilevamento comportamentale o servizi MDR.

Gli attacchi condotti dal gruppo Akira non sono nuovi **anche sul panorama italiano**. In passato, numerose aziende nazionali sono finite nel mirino del gruppo che opera compiendo la cifratura doppia dei dati e l’eventuale pubblicazione degli stessi su siti di leak.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Akira ransomware](https://www.securityinfo.it/tag/akira-ransomware/), [Arctic Wolf](https://www.securityinfo.it/tag/arctic-wolf/), [attacchi ransomware 2025](https://www.securityinfo.it/tag/attacchi-ransomware-2025/), [attacco informatico](https://www.securityinfo.it/tag/attacco-informatico/), [firewall Gen 7](https://www.securityinfo.it/tag/firewall-gen-7/), [Huntress Labs](https://www.securityinfo.it/tag/huntress-labs/), [sicurezza VPN](https://www.securityinfo.it/tag/sicurezza-vpn/), [SonicWall](https://www.securityinfo.it/tag/sonicwall/), [vulnerabilità SSL VPN](https://www.securityinfo.it/tag/vulnerabilita-ssl-vpn/), [zero-day SonicWall](https://www.securityinfo.it/tag/zero-day-sonicwall/)

[ReVault: vulnerabilità nei laptop Dell bypassano il login di Windows](https://www.securityinfo.it/2025/08/06/revault-vulnerabilita-nei-laptop-dell-bypassano-il-login-di-windows/)
[Cisco svela un nuovo tipo di jailbreak AI: i guardrail non bastano](https://www.securityinfo.it/2025/08/04/cisco-svela-un-nuovo-t...