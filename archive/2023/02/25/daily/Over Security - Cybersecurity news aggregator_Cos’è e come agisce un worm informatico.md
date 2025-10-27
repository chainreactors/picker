---
title: Cos’è e come agisce un worm informatico
url: https://hackerjournal.it/11391/cose-e-come-agisce-un-worm-informatico/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-25
fetch_date: 2025-10-04T08:06:18.549357
---

# Cos’è e come agisce un worm informatico

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

#### Cos’è e come agisce un worm informatico

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

# Cos’è e come agisce un worm informatico

Si tratta di un malware automatico che si replica rapidamente per diffondersi in altri computer.

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

24 Febbraio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2023/02/37692-scaled.jpg)

* Share
* Tweet

In una rete locale, per espandersi più rapidamente, un worm si basa sulle falle nella sicurezza del primo computer di destinazione. **Una volta entrato in questo primo computer, che diventa l’host, inizia a scansionare e infettare altre macchine nella LAN**. Quando il worm ha acquisito il controllo di questi nuovi computer, continua a eseguire la scansione delle reti collegate per cercare di infettare altri computer e usarli di nuovo come host. Questo comportamento continua in maniera automatica, diffondendo la minaccia in modo esponenziale. **In realtà, i worm informatici usano metodi ricorsivi per copiare se stessi anche senza host: in questo modo riescono a distribuirsi in base alla legge matematica della crescita esponenziale, controllando e infettando sempre più computer in breve tempo**.
**Per chi si occupa di computer forensic, un worm per essere definito tale deve avere quattro caratteristiche**: **essere un software autonomo** e indipendente; **deve essere tecnicamente complesso** (non bastano poche righe di codice che copiano dei bit su alcuni settori del disco); **deve contenere anche un [exploit](https://hackerjournal.it/8446/pwnkit-nuovo-exploit-mette-a-rischio-le-distribuzioni-linux/) per un attacco** (è il payload); infine deve essere altamente contagioso, cioè **diffondersi velocemente tramite canali diversi**: email, cartelle condivise, pagine Web infettate.

*\*illustrazione articolo progettata da* [rawpixel / Freepik](https://img.freepik.com/free-vector/illustration-virus-detection_53876-37692.jpg?w=740&t=st=1676842771~exp=1676843371~hmac=ce7c0f8cab4cf30307a66c2562de03075fc35ca3d50c51add531de6f8aa9f628)

Related Topics:[Malware](https://hackerjournal.it/tag/malware/)[Virus](https://hackerjournal.it/tag/virus/)[worm](https://hackerjournal.it/tag/worm/)

[Up Next

Rilasciata la distro Parrot Security 5.2](https://hackerjournal.it/11402/rilasciata-la-distro-parrot-security-5-2/)

[Don't Miss

Pluton, l’arma finale di Microsoft](https://hackerjournal.it/11387/pluton-larma-finale-di-microsoft/)

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

La Coppa del Mondo FIFA 2026 si avvicina, ma la sfida non si gioca solo sui campi da calcio. Secondo un nuovo rapporto di [Check Point Research](https://www.checkpoint.com/), i criminali informatici stanno già approfittando dell’entusiasmo dei tifosi per lanciare una massiccia campagna di frodi digitali. Il quadro che emerge è preoccupante: migliaia di domini fasulli, [botnet](https://hackerjournal.it/encyclopedia/botnet/ "Una botnet è una rete di droni zombie sotto il controllo di un hacker. Quando i black hat lanciano un attacco Distributed Denial of Service, ad esempio, utilizzeranno una botnet sotto il loro controllo. Molto spesso, gli utenti dei sistemi hackerati non sanno nemmeno di esser...