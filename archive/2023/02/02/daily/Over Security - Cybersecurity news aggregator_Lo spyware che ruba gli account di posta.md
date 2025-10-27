---
title: Lo spyware che ruba gli account di posta
url: https://hackerjournal.it/11269/lo-spyware-che-ruba-gli-account-di-posta/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-02
fetch_date: 2025-10-04T05:30:49.247279
---

# Lo spyware che ruba gli account di posta

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

Connect with us

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnew-1.png)](https://hackerjournal.it/)
[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

## Hackerjournal.it

#### Lo spyware che ruba gli account di posta

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/coppadelmondo-400x240.png)

    Mondiali 2026: la truffa corre sul Web](https://hackerjournal.it/14527/mondiali-2026-la-truffa-corre-sul-web/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/massive_npm-400x240.png)

    Il virus che “ruba” il codice](https://hackerjournal.it/14522/il-virus-che-ruba-il-codice/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/stellarium-400x240.jpg)

    Il malware che spia chi visita siti porno](https://hackerjournal.it/14518/il-malware-che-spia-chi-visita-siti-porno/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/kaspesky_corso-400x240.png)

    Un corso online per difendere gli LLM](https://hackerjournal.it/14504/un-corso-online-per-difendere-gli-llm/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/truffa_iphone-400x240.png)

    Truffe online dell’iPhone 17](https://hackerjournal.it/14495/truffe-online-delliphone-17/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/deepin_home-400x240.png)

    Linux incontra il design](https://hackerjournal.it/14508/linux-incontra-il-design/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/concetto-di-gestione-delle-relazioni-con-i-clienti-400x240.jpg)

    L’arte di ascoltare le reti](https://hackerjournal.it/14474/larte-di-ascoltare-le-reti/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/04/attacchi-cibenetici-400x240.jpg)

    Attacchi ai servizi di rete](https://hackerjournal.it/14439/attacchi-ai-servizi-di-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/persona-che-scrive-su-un-primo-piano-del-computer-portatile-400x240.jpg)

    Enumerazione: la vera identità della rete](https://hackerjournal.it/14421/enumerazione-la-vera-identita-della-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/codice-binario-con-globo-sul-computer-portatile-400x240.jpg)

    I migliori tool per la scansione di rete](https://hackerjournal.it/14410/i-migliori-tool-per-la-scansione-di-rete/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

### [News](https://hackerjournal.it/category/news/)

# Lo spyware che ruba gli account di posta

Identificato da alcuni ricercatori di DSCO CyTec, è stato soprannominato StrelaStealer. Lo spyware prende di mira gli account Outlook e Thunderbird

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

1 Febbraio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2023/01/StreaStealer.jpg)

* Share
* Tweet

Mentre la maggior parte dei [malware](https://hackerjournal.it/encyclopedia/malware/) simili si concentrano sul browser, StrelaStealer – celato dietro un falso file ISO o in un documento HTML – è in grado di accedere direttamente alle credenziali della posta elettronica, impossessandosi dell’archivio dove queste sono salvate. **Diffuso tramite allegati di posta elettronica, il file contiene in realtà due file: un LNK e un HTML**. Quest’ultimo, noto come “poliglotta”, perché può essere trattato in modo diverso a seconda dell’applicazione che lo apre, contiene la destinazione che appare dopo l’esecuzione dell’LNK, tramite rundll32.exe. A questo punto parte il payload principale del [malware](https://hackerjournal.it/encyclopedia/malware/ "Malware o “software malevolo” è un termine generico che descrive un programma/codice dannoso che mette a rischio un sistema."). Si apre il browser nel tentativo di fare credere all’utente che non ci sia nulla di strano. Ma non è così!
**La DLL StrelaStealer cerca la directory Thunderbird e raccoglie i file logins.json e key4.db** (i contenitori, in sostanza, delle informazioni necessarie per decrittografare le password memorizzate) e, allo stesso tempo, scansiona il registro di Windows a caccia dei dati sulle credenziali di Microsoft Outlook. Infine, **utilizza la funzione Windows CryptUnprotectData per decrittografare il tutto**. Terminato tutto ciò, invia i dati al server C2 dell’organizzazione criminale e il gioco è fatto.
**A questo [link](https://medium.com/%40DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc) i ricercatori di DSCO CyTec hanno riportato i dettagli sullo spyware individuato**.

Related Topics:[DSCO CyTec](https://hackerjournal.it/tag/dsco-cytec/)[Malware](https://hackerjournal.it/tag/malware/)[outlook](https://hackerjournal.it/tag/outlook/)[spyware](https://hackerjournal.it/tag/spyware/)[StrelaStealer](https://hackerjournal.it/tag/strelastealer/)[Thunderbird](https://hackerjournal.it/tag/thunderbird/)

[Up Next

App bancarie nel mirino del malware](https://hackerjournal.it/11275/app-bancarie-nel-mirino-del-malware/)

[Don't Miss

Arriva SuperTuxKart con nuove modalità](https://hackerjournal.it/11262/arriva-supertuxkart-con-nuove-modalita/)

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=60&d=mm&r=g)

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2017/12/hjnew-1.png)

[wpdevart\_facebook\_comment curent\_url="http://developers.facebook.com/docs/plugins/comments/" order\_type="social" title\_text="Facebook Comment" title\_text\_color="#000000" title\_text\_font\_size="22" title\_text\_font\_famely="monospace" title\_text\_position="left" width="100%" bg\_color="#d4d4d4" animation\_effect="random" count\_of\_comments="7" ]

### [News](https://hackerjournal.it/category/news/)

# Mondiali 2026: la truffa corre sul Web

Dai biglietti falsi ai domini contraffatti, i cybercriminali preparano la loro partita sfruttando l’entusiasmo dei tifosi. Ecco cosa sappiamo e come difendersi

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

2 Ottobre 2025

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2025/09/coppadelmondo.png)

La Coppa del Mondo FIFA 2026 si avvicina, ma la sfida non si gioca solo sui campi da calcio. Secondo un nuovo rapporto di [Check Point Research](https://www.checkpoint.com/), i criminali informatici stanno già approfittando dell’entusiasmo dei tifosi per lanciare una massiccia campagna di frodi digitali. Il quadro che emerge è preoccupante: migliaia di domini fasulli, [botnet](https://hackerjournal.it/encyclopedia/botnet/ "Una ...