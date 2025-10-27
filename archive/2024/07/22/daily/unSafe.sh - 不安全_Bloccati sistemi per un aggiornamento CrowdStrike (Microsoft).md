---
title: Bloccati sistemi per un aggiornamento CrowdStrike (Microsoft)
url: https://buaq.net/go-251668.html
source: unSafe.sh - 不安全
date: 2024-07-22
fetch_date: 2025-10-06T17:39:34.434333
---

# Bloccati sistemi per un aggiornamento CrowdStrike (Microsoft)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Bloccati sistemi per un aggiornamento CrowdStrike (Microsoft)

La notizia del mese è che un aggiornamento del software CrowdStrike aveva un bug che, nella notte de
*2024-7-21 18:8:0
Author: [blog.cesaregallotti.it(查看原文)](/jump-251668.htm)
阅读量:30
收藏*

---

La notizia del mese è che un aggiornamento del software CrowdStrike aveva un bug che, nella notte del 18 luglio, ha bloccato i sistemi Windows, con impatti e interruzioni in tutto il mondo, anche nei servizi di trasporto e in strutture sanitarie.

Fornisco il link alla notizia, data in formato sinteticissimo e con link e commenti di esperti, dal SANS: <https://www.sans.org/newsletters/newsbites/xxvi-55/>.

Intanto trovo interessante sapere che CrowdStrike è uno strumento per la sicurezza degli endpoint: sicuramente utile perché permette di centralizzare tante operazioni, ma anche pericoloso, come tutti gli strumenti.

Le riflessioni da fare sono molte. Io mi limito a qualche titolo, anche perché sono in assenza di notizie approfondite:

- non so perché CrowdStrike ha dovuto apportare l'aggiornamento, ma ho sempre il sospetto che, tra correzioni e nuove funzionalità da fare velocemente e a costi ridotti, quasi tutti i produttori di software rischiano di essere causa di incidenti più o meno significativi;

- chissà se CrowdStrike aveva fatto dei test al prodotto; visto l'impatto, un test in ambiente di prova avrebbe dovuto evidenziare il problema; però sappiamo che i test si fanno poco e male per il problema di cui sopra;

- dall'analisi tecnica (che, grazie a Pietro Calorio degli Idraulici della privacy, trovo su <https://www.linkedin.com/posts/daniele-zecca-74b64925_memoria-computer-0x9c-activity-7220358324712574976-YWX7>) sembra che uno strumento di controllo della qualità e della sicurezza (statica) del codice avrebbe dovuto segnalare il problema; quindi o non è stato usato uno strumento di controllo o la segnalazione è stata ignorata e le cause sono sempre quelle sopra indicate;

- chissà se i conduttori delle infrastrutture critiche che poi si sono bloccate avevano fatto dei test prima di distribuire l'aggiornamento su tutti i sistemi; anche loro, lo sappiamo, soffrono del solito problema per cui gli investimenti nell'informatica non sono proporzionali alla sua importanza (e questo e altri incidenti dimostrano che siamo ben lontani dall'avere manager con la giusta sensibilità);

- se ci sono dei sistemi critici che potrebbero bloccare tutta un'infrastruttura, vanno posti in reti dedicate e separate, come si consiglia in ambito OT e come andrebbe fatto in tutti gli ambiti critici; ma anche questo richiede investimenti (e, purtroppo, temo che NIS2, DORA e compagnia non impongano questa misura, anche perché oggi in pochi sanno valutarla correttamente).

Niccolò Castoldi mi ha segnalato la dichiarazione del CEO di CrowdStrike (<https://www.wired.com/story/microsoft-windows-outage-crowdstrike-global-it-probems/>) che dice: "Questo non è un incidente di sicurezza o un ciber attacco". Qui si vede un uso del termine "incidente di sicurezza" come sinonimo di "attacco di malintenzionati" molto diffuso. In realtà, lo sappiamo, si è trattato di un errore (causa) che ha provocato un incidente di sicurezza delle informazioni (effetto almeno sulla disponibilità).

E ancora una volta colgo l'occasione per ricordare che chi si occupa di sicurezza delle informazioni non si occupa "solo" di attacchi, ma anche di errori, che sono spesso molto più numerosi e provocano danni molto più estesi (credo che tanti gruppi di criminali se lo possono solo sognare un attacco di così grande impatto).

文章来源: http://blog.cesaregallotti.it/2024/07/bloccati-sistemi-per-un-aggiornamento.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)