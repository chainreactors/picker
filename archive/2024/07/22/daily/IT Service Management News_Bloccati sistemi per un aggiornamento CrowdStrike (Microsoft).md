---
title: Bloccati sistemi per un aggiornamento CrowdStrike (Microsoft)
url: http://blog.cesaregallotti.it/2024/07/bloccati-sistemi-per-un-aggiornamento.html
source: IT Service Management News
date: 2024-07-22
fetch_date: 2025-10-06T17:40:47.578523
---

# Bloccati sistemi per un aggiornamento CrowdStrike (Microsoft)

# [IT Service Management News](http://blog.cesaregallotti.it/)

Sicurezza delle informazioni, IT service management e qualità da Cesare Gallotti

## domenica 21 luglio 2024

### Bloccati sistemi per un aggiornamento CrowdStrike (Microsoft)

La notizia del mese è che un aggiornamento del software CrowdStrike aveva un bug che, nella notte del 18 luglio, ha bloccato i sistemi Windows, con impatti e interruzioni in tutto il mondo, anche nei servizi di trasporto e in strutture sanitarie.

Fornisco il link alla notizia, data in formato sinteticissimo e con link e commenti di esperti, dal SANS: <https://www.sans.org/newsletters/newsbites/xxvi-55/>.

Intanto trovo interessante sapere che CrowdStrike è uno strumento per la sicurezza degli endpoint: sicuramente utile perché permette di centralizzare tante operazioni, ma anche pericoloso, come tutti gli strumenti.

Le riflessioni da fare sono molte. Io mi limito a qualche titolo, anche perché sono in assenza di notizie approfondite:

* non so perché CrowdStrike ha dovuto apportare l'aggiornamento, ma ho sempre il sospetto che, tra correzioni e nuove funzionalità da fare velocemente e a costi ridotti, quasi tutti i produttori di software rischiano di essere causa di incidenti più o meno significativi;
* chissà se CrowdStrike aveva fatto dei test al prodotto; visto l'impatto, un test in ambiente di prova avrebbe dovuto evidenziare il problema; però sappiamo che i test si fanno poco e male per il problema di cui sopra;
* dall'analisi tecnica (che, grazie a Pietro Calorio degli Idraulici della privacy, trovo su <https://www.linkedin.com/posts/daniele-zecca-74b64925_memoria-computer-0x9c-activity-7220358324712574976-YWX7>) sembra che uno strumento di controllo della qualità e della sicurezza (statica) del codice avrebbe dovuto segnalare il problema; quindi o non è stato usato uno strumento di controllo o la segnalazione è stata ignorata e le cause sono sempre quelle sopra indicate;
* chissà se i conduttori delle infrastrutture critiche che poi si sono bloccate avevano fatto dei test prima di distribuire l'aggiornamento su tutti i sistemi; anche loro, lo sappiamo, soffrono del solito problema per cui gli investimenti nell'informatica non sono proporzionali alla sua importanza (e questo e altri incidenti dimostrano che siamo ben lontani dall'avere manager con la giusta sensibilità);
* se ci sono dei sistemi critici che potrebbero bloccare tutta un'infrastruttura, vanno posti in reti dedicate e separate, come si consiglia in ambito OT e come andrebbe fatto in tutti gli ambiti critici; ma anche questo richiede investimenti (e, purtroppo, temo che NIS2, DORA e compagnia non impongano questa misura, anche perché oggi in pochi sanno valutarla correttamente).

Niccolò Castoldi mi ha segnalato la dichiarazione del CEO di CrowdStrike (<https://www.wired.com/story/microsoft-windows-outage-crowdstrike-global-it-probems/>) che dice: "Questo non è un incidente di sicurezza o un ciber attacco". Qui si vede un uso del termine "incidente di sicurezza" come sinonimo di "attacco di malintenzionati" molto diffuso. In realtà, lo sappiamo, si è trattato di un errore (causa) che ha provocato un incidente di sicurezza delle informazioni (effetto almeno sulla disponibilità).

E ancora una volta colgo l'occasione per ricordare che chi si occupa di sicurezza delle informazioni non si occupa "solo" di attacchi, ma anche di errori, che sono spesso molto più numerosi e provocano danni molto più estesi (credo che tanti gruppi di criminali se lo possono solo sognare un attacco di così grande impatto).

Pubblicato da

[Cesare Gallotti](https://www.blogger.com/profile/02941990619036529409 "author profile")

alle
[12:08:00](http://blog.cesaregallotti.it/2024/07/bloccati-sistemi-per-un-aggiornamento.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/3090080509035095684/5638753695764985089 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3090080509035095684&postID=5638753695764985089&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5638753695764985089&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5638753695764985089&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5638753695764985089&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5638753695764985089&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5638753695764985089&target=pinterest "Condividi su Pinterest")

Etichette:
[Minacce e attacchi](http://blog.cesaregallotti.it/search/label/Minacce%20e%20attacchi)

#### Nessun commento:

#### Posta un commento

[Post più recente](http://blog.cesaregallotti.it/2024/07/edpb-approva-criteri-europrise.html "Post più recente")

[Post più vecchio](http://blog.cesaregallotti.it/2024/07/legge-90-del-2024-sulla-cybersicurezza_18.html "Post più vecchio")
[Home page](http://blog.cesaregallotti.it/)

Iscriviti a:
[Commenti sul post (Atom)](http://blog.cesaregallotti.it/feeds/5638753695764985089/comments/default)

* [Home cesaregallotti.it](http://www.cesaregallotti.it/index.html)
* [Servizi](http://www.cesaregallotti.it/Servizi.html)
* [Competenze](http://www.cesaregallotti.it/Competenze.html)
* [Pubblicazioni](http://www.cesaregallotti.it/Pubblicazioni.html)
* [Risorse on-line](http://www.cesaregallotti.it/Risorse_on_line.html)
* [Normativa](http://www.cesaregallotti.it/Normativa.html)
* [Newsletter](http://www.cesaregallotti.it/Newsletter.html)
* [Blog](http://blog.cesaregallotti.it/)
* [Contatti](http://www.cesaregallotti.it/Contatti.html)

[![Creative Commons Licence](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/deed.en_GB)
IT Service Management News  by [Cesare Gallotti](www.cesaregallotti.it) is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/deed.en_GB).

Link, articoli e altre notizie su <http://www.cesaregallotti.it/>.

E' possibile iscriversi alla newsletter seguendo le istruzioni nella [specifica pagina web](http://www.cesaregallotti.it/Newsletter.html).

Cookie: questo blog è gestito da Blogger (Google) e questa è la sua informativa: <http://bit.ly/1IvDrsv>. Io ho usato solo funzionalità standard proposte da Blogger.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjnXZjqeW7yaRPjHFzb-FvJEsIspEKWyZR2ptNll05499Mc8RtXWgJ20F2AI1bZKHUFYB1phy6uH1IM3nPPyH8uPC1Gj0s4b-U4T1Qf5iWS--nEOdcuXAW5wVECyUZWz1Hn8pmowXhrBnxMTfkpcq7leN6uwR5wQIUE1hEx-8i9_hTcOxee64VJ5Q8OCw=s378)](http://blog.cesaregallotti.it/p/blog-page.html)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhAoL5kwmZ6bVwW69Ofgn-cweipB9S9geYJ27nn_O7z23bLMfXprsGOKQmE2VVeRqUjWqSojM_BYLLxQLmvi67gev-X5IyxUMiqMmYfZiG2fdQ2PSrNrzLI_lxc_7myPAYVWAvzD8Nsvm0uT793dGGpAX3db4brnQMQtZ7TvuAWBzc_DGNEM_bd0Rz9Pw=s378)](https://blog.cesaregallotti.it/p/blog-page_20.html)

## Iscriviti a questo Blog

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Post

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fblog.cesaregallotti.it%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fblog.cesaregallotti.it%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](http://blog.cesaregallotti.it/feeds/posts/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.c...