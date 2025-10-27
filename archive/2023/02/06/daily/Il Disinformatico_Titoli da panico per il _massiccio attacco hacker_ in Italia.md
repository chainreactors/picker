---
title: Titoli da panico per il "massiccio attacco hacker" in Italia
url: http://attivissimo.blogspot.com/2023/02/titoli-da-panico-per-il-massiccio.html
source: Il Disinformatico
date: 2023-02-06
fetch_date: 2025-10-04T05:48:07.213132
---

# Titoli da panico per il "massiccio attacco hacker" in Italia

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2023/02/05

### Titoli da panico per il "massiccio attacco hacker" in Italia: i dati concreti

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR1XXBkfC4k0Rc7v0BkzhpQWaeLzli-xxV_XY4AP29_O3hh74vRZvBex35vSUL7N0lLnK6uxWNau3DgVq0TkmSmoQxHEM2wbQcyRN18Gv1jEZ9wS9XNRQtLT5aJLM51jyB-fn4FxxZc5SSNx3pde13P4M0R7_RuHJU1eOiOEeWLtf5byrbt_A/s320/Screenshot%202023-02-05%20at%2018.42.05.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR1XXBkfC4k0Rc7v0BkzhpQWaeLzli-xxV_XY4AP29_O3hh74vRZvBex35vSUL7N0lLnK6uxWNau3DgVq0TkmSmoQxHEM2wbQcyRN18Gv1jEZ9wS9XNRQtLT5aJLM51jyB-fn4FxxZc5SSNx3pde13P4M0R7_RuHJU1eOiOEeWLtf5byrbt_A/s1336/Screenshot%202023-02-05%20at%2018.42.05.png)

*Ultimo aggiornamento: 2023/02/09 22:20.*

Scrive
[Rainews](https://www.rainews.it/articoli/2023/02/agenzia-per-la-cybersicurezza-e-in-corso-un-massiccio-attacco-hacker-014f5925-0bbf-4ad0-b569-c81d4325ae47.html):
*“Agenzia per la cybersicurezza: "E' in corso un massiccio attacco
hacker"*.

Come al solito, siccome in tante redazioni linkare le fonti è considerato un
abominio, non viene riportata l’indicazione più importante, ossia
l’informazione tecnica del CSIRT. È
[qui](https://www.csirt.gov.it/contenuti/rilevato-lo-sfruttamento-massivo-della-cve-202121974-in-vmware-esxi-al01-230204-csirt-ita). E dice una cosa che Rainews ha tralasciato di mettere in evidenza:
**la falla di VMware ESXi sfruttata per l’attacco è stata corretta dal vendor
due anni fa.**

No, dico, *due anni fa*. L’avviso del CSIRT lo dice chiaramente: “*vulnerabilità
[CVE-2021–21974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21974)
– già sanata dal vendor nel febbraio 2021”.*

Parliamoci chiaro: se non patchi un sistema da due anni e per di più lo esponi
direttamente a Internet, prendi una canna da pesca e smetti di fare danni,
perlamordiddio.

E per favore piantiamola con i titoli sensazionalisti: il titolo corretto,
qui, non è *“È in corso un massiccio attacco hacker”* ma
*“Imbecilli non aggiornano da 2 anni computer esposti a Internet, si beccano
quello che si meritano”*.

Gli anglofoni hanno un modo di dire perfettamente azzeccato per queste
occasioni: FAFO. *Fuck around, find out*. Ossia, grosso modo,
*“Fai una cretinata, scoprine le conseguenze”*.

---

Se vi interessano i dettagli tecnici, BleepingComputer ha pubblicato un ottimo
[articolo](https://www.bleepingcomputer.com/news/security/massive-esxiargs-ransomware-attack-targets-vmware-esxi-servers-worldwide/)
in proposito; Censys ha un
[elenco dei server colpiti](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.http.response.body%3A+%22How+to+Restore+Your+Files%22+and+services.http.response.html_title%3A%22How+to+Restore+Your+Files%22); e [qui ci sono istruzioni](https://enes.dev/) per proteggere i
server e per tentare il recupero dei file cifrati dal ransomware.

> Look at the world! look how many OLD ESXi servers are exposed :D
> <https://t.co/z2ykKB3sGB>
> [pic.twitter.com/Jeqr9veyRr](https://t.co/Jeqr9veyRr)
>
> — mRr3b00t (@UK\_Daniel\_Card)
> [February 5, 2023](https://twitter.com/UK_Daniel_Card/status/1622168646792486912?ref_src=twsrc%5Etfw)

Secondo Censys, in Italia i server colpiti (non quelli vulnerabili, ma quelli
che sono già stati infettati) sono almeno una
[ventina](https://search.censys.io/search?resource=hosts&virtual_hosts=EXCLUDE&q=%28%28services.http.response.body%3A+%22How+to+Restore+Your+Files%22+and+services.http.response.html_title%3A%22How+to+Restore+Your+Files%22%29+and+location.country%3D%60Italy%60%29+and+services.software.product%3D%60VMware+ESXi+Server%60); in Svizzera sono più o meno altrettanti.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8bTCmN6CaH1WSgPi0Wj3rHmOGFK6cG90FuXMgxbNnvEdj3NsCf17mLYGQVCZynqc0uIZNfbUD5S6LGPdeyyXpK15i4dJOWUh1EyEUxXWwV7sPuYJ9SGm9ad7aUzjRT7Dk9TmwUB3WVh3c2RvIaTYTQ_sIdctVaAUuYJilZudN0xIPpz22UL4/w614-h640/Screenshot%202023-02-06%20at%2009.37.27_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8bTCmN6CaH1WSgPi0Wj3rHmOGFK6cG90FuXMgxbNnvEdj3NsCf17mLYGQVCZynqc0uIZNfbUD5S6LGPdeyyXpK15i4dJOWUh1EyEUxXWwV7sPuYJ9SGm9ad7aUzjRT7Dk9TmwUB3WVh3c2RvIaTYTQ_sIdctVaAUuYJilZudN0xIPpz22UL4/s1286/Screenshot%202023-02-06%20at%2009.37.27_censored.jpg)

---

Ho parlato della vicenda a Teleticino ([video](https://www.ticinonews.ch/ticino/anche-la-svizzera-toccata-dallattacco-hacker-attivissimo-preoccupante-vedere-aziende-impreparate-373519)) e a Radio Radicale ([registrazione audio](https://www.youtube.com/watch?v=O4GE3u9dQZU)).

La [nota](https://www.agi.it/cronaca/news/2023-02-06/attacco-hacker-nessuna-istituzione-colpita-19974454/amp) del governo italiano è molto netta (evidenziazioni mie): *“L’aggressione informatica, emersa già dalla serata del 3 febbraio e
culminata ieri in modo così diffuso, era stata individuata da ACN* [Agenzia per la Cybersicurezza Nazionale] *come
ipoteticamente possibile fin dal febbraio 2021, e a tal fine **l’Agenzia
aveva allertato** tutti i soggetti sensibili affinché adottassero le
necessarie misure di protezione. **Taluni dei destinatari dell’avviso
hanno tenuto in debita considerazione l’avvertimento, altri no e
purtroppo oggi ne pagano le conseguenze.** Per fare una analogia con l’ambito sanitario, è accaduto come se a
febbraio 2021 un virus particolarmente aggressivo avesse iniziato a
circolare, le autorità sanitarie avessero sollecitato le persone fragili
a una opportuna prevenzione, e a distanza di tempo siano emersi i danni
alla salute per chi a quella prevenzione non abbia ottemperato".”*

Non avrei saputo dirlo meglio.

*---*

**2023/02/09 22:20.** Anche la CISA (Cybersecurity and Infrastructure Security Agency) statunitense ha [pubblicato](https://www.cisa.gov/uscert/ncas/current-activity/2023/02/07/cisa-releases-esxiargs-ransomware-recovery-script) uno script e delle istruzioni per il recupero dei dati in caso di attacco con questo ransomware.

Pubblicazione iniziale:
[5.2.23](https://attivissimo.blogspot.com/2023/02/titoli-da-panico-per-il-massiccio.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7421441/2646709487285285683 "Post per email")

Labels:
[attacchi informatici](https://attivissimo.blogspot.com/search/label/attacchi%20informatici),
[ransomware](https://attivissimo.blogspot.com/search/label/ransomware)

#### Nessun commento:

[Posta un commento](https://www.blogger.com/comment/fullpage/post/7421441/2646709487285285683)

[Post più recente](https://attivissimo.blogspot.com/2023/02/ansa-e-lastronomia-repubblica-e-il.html "Post più recente")

[Post più vecchio](https://attivissimo.blogspot.com/2023/02/2001-odissea-nello-spazio-con-le.html "Post più vecchio")
[Home page](https://attivissimo.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://attivissimo.blogspot.com/feeds/2646709487285285683/comments/default)

Choose a language
English
Afrikaans
العربية
Azərbaycan
Беларуская
Български
Català
Český
Cymraeg
Danske
Deutsch
Ελληνικά
Euskal
Español
Eesti
فارسی
Suomalainen
Français
Gaeilge
Galego
हिन्दी
Hrvatski
Kreyòl
Magyar
Հայերեն
Bahasa Indonesia
Íoslainnis
עברית
日本
ქართული
한국어
Latinum
Lietuvas
Latvijā
Македонски
Melayu
Malti
Nederlandse
Norske (Bokmål)
Polski
Português
Română
Русский
Slovenská jazyku
Slovenski jezik
Shqiptar
Српски језик
Svenska
Swahili
ไทย
Filipino
Türk
Українське
اردو
Việt
ייִדיש
中文 (简体字)
中文 (正體字)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQ-_-OkaZJx...