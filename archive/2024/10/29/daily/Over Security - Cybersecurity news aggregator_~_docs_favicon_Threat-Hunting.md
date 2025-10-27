---
title: ~/docs/favicon_Threat-Hunting
url: https://blog.lobsec.com/2024/01/favicon-threat-hunting/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-29
fetch_date: 2025-10-06T18:53:31.261673
---

# ~/docs/favicon_Threat-Hunting

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)

# ~/docs/favicon\_Threat-Hunting

2024-01-18 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

## Premessa

Gli HTTP favicon sono spesso utilizzati da bug bounty hunter e red teamer per individuare servizi fraudolenti.

Sebbene l’utilizzo di favicon hash sia comune nella comunità “red”, un numero significativo di blue teamer non li utilizza affatto e questo è un peccato in quanto, tra le loro altre funzioni, possono fornirci un modo semplice per identificare gli indirizzi che ospitano siti di phishing. Dopotutto questo è stato il motivo per cui le ricerche degli hash dei favicon sono state introdotte in Shodan.

Ad esempio, si può mostrare come rilevare dei siti che ospitano pagine di phishing, cercando di impersonarsi come portali di accesso per Office 365 e altri servizi Microsoft. Ovviamente lo stesso principio funziona per qualsiasi altro servizio.

Si potrebbe quindi calcolare gli hash utilizzati da sistemi specifici di un’azienda che si sta cercando di proteggere (ad esempio favicon da un sito Web aziendale) e utilizzare periodicamente queste ricerche su Shodan e/o altri servizi per implementare un meccanismo di rilevamento/protezione del marchio per il phishing.

## Nella pratica

Con uno script in python è possibile calcolare il MurmurHash di una qualsiasi risorsa, nel nostro esempio andremo a calcolarlo prendendo come fonte i byte restituiti dalla richiesta alla risorsa remota https://c.s-microsoft.com/favicon.ico

```
import requests
import mmh3
import base64

response = requests.get('https://c.s-microsoft.com/favicon.ico')
favicon = base64.encodebytes(response.content)
hash = mmh3.hash(favicon)

print(hash)
```

Lanciando lo script si ha questo risultato

![](https://blog.lobsec.com/wp-content/uploads/2024/01/mmh.png)

Img. 1 – MurmurHash del favicon su https://c.s-microsoft.com/favicon.ico

Andando ad eseguire una ricerca su Shodan possiamo vedere un cospicuo numero di risultati tra siti legittimi e siti illegittimi.

![](https://blog.lobsec.com/wp-content/uploads/2024/01/shodan1-1024x380.png)

Img. 2 – Ricerca su Shodan

Con una ricerca più approfondita si possono andare a filtrare meglio i risultati, ad esempio utilizzando questa stringa andremo ad estendere la nostra ricerca per cercare solo indirizzi di pagine web che assomigliano a portali di accesso (http.html:”Sign in”) e che non sono ospitate su infrastrutture Microsoft (-org:”Microsoft Corporation” -org:”Microsoft Azure “) ma eseguono un server Web Apache (prodotto:”Apache httpd”).

```
http.favicon.hash:-2057558656 -org:"Microsoft Corporation" -org:"Microsoft Azure" product:"Apache httpd" http.html:"Sign in"
```

Come si può vedere dal risultato, gli host trovati sono nettamente inferiori e – presumibilmente – molti dei quali illegali

![](https://blog.lobsec.com/wp-content/uploads/2024/01/shodan2-1024x425.png)

Img. 3 – Ricerca su Shodan con filtri

Come volevasi dimostrare, prendendo il primo della lista, il risultato è il seguente

![](https://blog.lobsec.com/wp-content/uploads/2024/01/web1.png)

Img. 4 – Il sito di phishing

EOF

Categorie [analysis](https://blog.lobsec.com/category/analysis/), [blue team](https://blog.lobsec.com/category/blue-team/), [tips](https://blog.lobsec.com/category/tips/) Tag [favicon](https://blog.lobsec.com/tag/favicon/), [favicon.ico](https://blog.lobsec.com/tag/favicon-ico/), [hunting](https://blog.lobsec.com/tag/hunting/), [shodan](https://blog.lobsec.com/tag/shodan/), [threat hunting](https://blog.lobsec.com/tag/threat-hunting/)

[~/docs/User-Agent\_Hunting](https://blog.lobsec.com/2024/01/docs-user-agent_hunting/)

[Fortinet CVE-2024-21762](https://blog.lobsec.com/2024/02/fortinet-cve-2024-21762/)

## 1 commento su “~/docs/favicon\_Threat-Hunting”

1. [diegobetto](https://diegobetto.com)

   [2024-01-18 alle 14:37](https://blog.lobsec.com/2024/01/favicon-threat-hunting/#comment-20)

   Interessante utilizzo della favicon!

   [Rispondi](#comment-20)

### Lascia un commento [Annulla risposta](/2024/01/favicon-threat-hunting/#respond)

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