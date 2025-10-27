---
title: MadLicense
url: https://blog.lobsec.com/2024/08/madlicense/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-29
fetch_date: 2025-10-06T18:53:42.748255
---

# MadLicense

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)

# MadLicense

2024-08-09 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

## Informazioni generali

La vulnerabilità “MadLicense” è una RCE (remote code execution) pre-auth che consente agli aggressori di eseguire codice arbitrario su sistemi vulnerabili senza richiedere l’interazione dell’utente.

A differenza di molte vulnerabilità RCE che richiedono una qualche forma di interazione da parte dell’utente, la vulnerabilità CVE-2024-38077 può essere sfruttata senza alcuna azione da parte dell’utente.

Ciò è particolarmente preoccupante dato l’uso diffuso del servizio licenze Desktop remoto che viene spesso distribuito su server con Servizi Desktop remoto abilitati. Il servizio gestisce ed emette licenze per l’accesso al desktop remoto rendendolo un componente fondamentale in molti ambienti aziendali.

Al momento della scrittura di questo articolo non è presente una patch, pertanto si consiglia di disabilitare il servizio. I prodotti Microsoft soggetti a questa vulnerabilità vanno dalla versione 2000 alla 2025.

Link di interesse: [MRSC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38077?utm_campaign=WIIT%20Security%20Advisory&utm_medium=email&_hsenc=p2ANqtz-905ao1s54hRgIE15xDoF32w9M7-AuszQtXP6NLyDTLCUJ-N-WrnpY_KcJ6Er3GSOnpbkHNBpLmqui-hW-8H1oyI_8YP2IWLlKdCQH-mbOVjjxtb3M&_hsmi=319422323&utm_content=319422323&utm_source=hs_email).

## Exploit

La vulnerabilità MadLicense consiste in un buffer overflow dell’heap di memoria nella procedura `CDataCoding::DecodeData`. Manipolando l’input gli attaccanti possono innescare un buffer overflow, portando all’esecuzione di codice arbitrario nel contesto del servizio RDL.

I ricercatori ([Lewis Lee](https://twitter.com/lewislee53), [Chunyang Han](https://twitter.com/ver0759) and [Zhiniang Peng](https://twitter.com/edwardzpeng)) hanno dimostrato con successo un exploit POC (proof-of-concept) su Windows Server 2025, ottenendo una percentuale di successo vicina al 100%. L’exploit aggira efficacemente tutte le mitigazioni contemporanee, comprendendo la mitigazione LFH recentemente introdotta in Windows Server 2025.

## POC

A quanto pare sembra essere presente su GitHub una [POC](https://github.com/CloudCrowSec001/CVE-2024-38077-POC/blob/main/README.md): tuttavia è bene far presente che si tratta di pseudocode con il quale non si può neanche triggerare il bug.

La patch di aggiornamento sarà rilasciata con il prossimo mese.

EOF

Categorie [red team](https://blog.lobsec.com/category/red-team/) Tag [CVE-2024-38077](https://blog.lobsec.com/tag/cve-2024-38077/), [licese server](https://blog.lobsec.com/tag/licese-server/), [madlicense](https://blog.lobsec.com/tag/madlicense/), [rce](https://blog.lobsec.com/tag/rce/), [rdp](https://blog.lobsec.com/tag/rdp/)

[~/docs/audit.d](https://blog.lobsec.com/2024/04/configurare-auditd/)

[~/docs/ips-ids.security](https://blog.lobsec.com/2024/08/docs-ips-ids-security/)

### Lascia un commento [Annulla risposta](/2024/08/madlicense/#respond)

Commento

Nome
Email
Sito web

[ ]  Salva il mio nome, email e sito web in questo browser per la prossima volta che commento.

Δ

* [Analisi di un dropper HTML/JS per Internet Explorer basato su ActiveX e regsvr32](https://blog.lobsec.com/2025/08/analisi-di-un-dropper-html-js-per-internet-explorer-basato-su-activex-e-regsvr32/)
* [Kekpi trojan dissection](https://blog.lobsec.com/2025/03/kekpi-malware-dissection/)
* [NIS2: il caos di cui non avevamo (forse) bisogno](https://blog.lobsec.com/2024/12/nis2-il-caos-di-cui-non-avevamo-forse-bisogno/)
* [~/news/blocklist.news](https://blog.lobsec.com/2024/10/blocklist-ioc-updated/)
* [~/tips/fortigate\_malware.feed](https://blog.lobsec.com/2024/10/fortigate-malware-feed/)
* [/usr/bin/touch nuova\_era](https://blog.lobsec.com/2024/10/lobsec-nuova-era/)

© 2025 Lobsec • Creato con [GeneratePress](https://generatepress.com)

Manage Consent

To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions.

Functional

[ ]
Functional
Sempre attivo

The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.

Preferences

[ ]
Preferences

The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.

Statistics

[ ]
Statistics

The technical storage or access that is used exclusively for statistical purposes.
The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.

Marketing

[ ]
Marketing

The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.

Gestisci opzioni
Gestisci servizi
Gestisci {vendor\_count} fornitori
[Per saperne di più su questi scopi](https://cookiedatabase.org/tcf/purposes/)

Accept
Deny
View preferences
Save preferences
View preferences

{title}
{title}
{title}

Manage consent