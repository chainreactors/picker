---
title: Kaspersky: aumentano gli attacchi che usano SQL Server
url: https://www.securityinfo.it/2022/11/07/kaspersky-aumento-attacchi-sql-server/?utm_source=rss&utm_medium=rss&utm_campaign=kaspersky-aumento-attacchi-sql-server
source: Over Security - Cybersecurity news aggregator
date: 2022-11-08
fetch_date: 2025-10-03T21:57:57.933591
---

# Kaspersky: aumentano gli attacchi che usano SQL Server

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

## Kaspersky: aumentano gli attacchi che usano SQL Server

Nov 07, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2022/11/07/kaspersky-aumento-attacchi-sql-server/#respond)

---

L’ultimo report di **Kaspersky ha evidenziato che gli attacchi che sfruttano Microsoft SQL Server sono aumentati del 56%**. Lo scorso settembre si sono registrati più di 3000 attacchi; il trend è cominciato a salire già da inizio anno e ora ha superato di più del 50% il numero dello scorso anno.

Si tratta di attacchi conosciuti già da tempo che continuano a essere usati per ottenere l’accesso alla rete aziendale. **SQL Server è uno dei DBMS più usati dalle aziende**, ma i rischi a cui le espone sono ancora troppo sottovalutati.

Il team di Managed Detection and response di Kaspersky [ha illustrato un esempio di attacco a SQL Server](https://securelist.com/server-side-attacks-cc-in-public-clouds-mdr-cases/107826/) che modifica la configurazione del server per accedervi ed eseguire un malware.

![Kaspersky sql server](https://www.securityinfo.it/wp-content/uploads/2022/11/ed-hardie-1C5F88Af9ZU-unsplash.jpg)

https://unsplash.com/@impelling

È stato il processo sqlservr.exe ad esibire alcune attività sospette: a partire da questo si è in seguito risaliti all’intera catena di attacco. Nel dettaglio, **il processo compromesso cercava di creare un file con codice malevolo in assembly**. Il file in questione conteneva un trojan che cercava di eseguire script PowerShell per connettersi a degli indirizzi IP esterni; questi, in forma di file .png, eseguivano malware sul server.

Alcuni di questi indirizzi erano già presenti nella deny list di SQL Server e i restanti sono stati aggiunti dopo. Fortunatamente **l’attacco è stato individuato nelle prime fasi di esecuzione e le soluzioni di Kaspersky lo hanno bloccato in tempo**. Il tentativo di compromissione si è poi verificato su un altro host connesso alla rete; anche in questo caso l’attacco è stato sventato quasi subito.

**Spesso le reti aziendali non sono configurate correttamente e i server sono accessibili dalla rete esterna**: è fondamentale proteggere gli host e renderli irraggiungibili così da limitare i tentativi di compromissione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [cybersicurezza](https://www.securityinfo.it/tag/cybersicurezza/), [hacker](https://www.securityinfo.it/tag/hacker/), [malware](https://www.securityinfo.it/tag/malware/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [sicurezza informatica](https://www.securityinfo.it/tag/sicurezza-informatica/), [sql server](https://www.securityinfo.it/tag/sql-server/)

[La sicurezza informatica tra criminalità e guerra digitale](https://www.securityinfo.it/2022/11/07/la-sicurezza-informatica-tra-criminalita-e-guerra-digitale/)
[Fortinet rilascia patch per 6 vulnerabilità ad alto rischio](https://www.securityinfo.it/2022/11/04/fortinet-patch-vulnerabilita-alto-rischio/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/#respond)
* [![Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio](https://www.securityinfo.it/w...