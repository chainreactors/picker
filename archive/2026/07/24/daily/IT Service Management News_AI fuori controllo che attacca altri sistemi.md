---
title: AI fuori controllo che attacca altri sistemi
url: http://blog.cesaregallotti.it/2026/07/ai-fuori-controllo-che-attacca-altri.html
source: IT Service Management News
date: 2026-07-24
fetch_date: 2026-07-25T05:00:39.531646
---

# AI fuori controllo che attacca altri sistemi

# [IT Service Management News](http://blog.cesaregallotti.it/)

Sicurezza delle informazioni, IT service management e qualità da Cesare Gallotti

## venerdì 24 luglio 2026

### AI fuori controllo che attacca altri sistemi

La notizia è del 22 luglio e si è diffusa molto velocemente (a me l'ha segnalata Claudio Modenesi, che ringrazio). Un test interno di OpenAI è sfociato in una compromissione reale dell’infrastruttura di un'azienda che produce applicazioni basate su sistemi di IA: <https://www.ansa.it/amp/canale_tecnologia/notizie/cybersecurity/2026/07/22/openai-i-nostri-modelli-ia-fuori-controllo-hanno-hackerato-altra-piattaforma_b024ad4e-1e77-4420-afea-efe8294343e7.html>

Rimando all'articolo "L’AI sfugge dal laboratorio e attacca: cosa insegna il caso OpenAI-Hugging Face" per un'analisi più approfondita e qualche commento interessante: <https://www.agendadigitale.eu/sicurezza/lai-sfugge-dal-laboratorio-e-attacca-cosa-insegna-il-caso-openai-hugging-face/>.

Savino Menna mi ha segnalato l'articolo di analisi "The Emperor’s New Exploit": [https://medium.com/@lfloridi/the-emperors-new-exploit-2b062f124c06](https://medium.com/%40lfloridi/the-emperors-new-exploit-2b062f124c06).

Roberto Piazzolla mi ha anche segnalato una spiegazione più approfondita dell'accaduto direttamente dal blog di OpenAI: <https://openai.com/index/hugging-face-model-evaluation-security-incident/>.

Io sono un profano di intelligenza artificiale e da qui in poi copio il commento di Roberto.

In pratica OpenAI stava facendo un test su un suo nuovo modello. Questo modello "voleva" conoscere il punteggio ottenuto, in modo da poterlo migliorare, e il sistema che ha trovato è stato:

* prima scardinare la sandbox di OpenAI, ottenendo l'accesso a Internet (partendo dallo sfruttamento di uno zero day);
* poi hackerare Hugging Face, che è il repository di tutti i test (anche di quelli interni delle aziende AI).

La prima ad accorgersene è stata Hugging Face, che non sapeva esattamente da dove venisse l'attacco, e si è difesa usando una AI cinese (GLM 5.2) perché modelli di frontiera americani non permettevano loro di usare un livello così sofisticato di cybersecurity senza alzare il cartello di "Stop!".

L'articolo "The Emperor’s New Exploit" dice che il problema non è nuovo nuovo e infatti c'è anche un filmato su You Tube del 2020 dal titolo "OpenAI Plays Hide and Seek…and Breaks The Game!". In esso due AI di OpenAI (che all'epoca faceva solo esperimenti con le intelligenze artificiali dentro ai videogame) giocano a nascondino in un ambiente controllato e trovano strategie sempre più inusuali, fino a scoprire che c'è un bug nell'ambiente di test che permette loro di attraversare i muri. La questione del reward hacking è conosciuta nel mondo della security AI da ben prima di 6 anni fa.

Il problema quindi non è che questa AI ci "abbia provato", ma che OpenAI, pur conoscendo i rischi, non abbia usato un ambiente di test a prova di hacking.

Pubblicato da

[Cesare Gallotti](https://www.blogger.com/profile/02941990619036529409 "author profile")

alle
[12:00:00](http://blog.cesaregallotti.it/2026/07/ai-fuori-controllo-che-attacca-altri.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/3090080509035095684/5209088888507832042 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3090080509035095684&postID=5209088888507832042&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5209088888507832042&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5209088888507832042&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5209088888507832042&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5209088888507832042&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5209088888507832042&target=pinterest "Condividi su Pinterest")

#### Nessun commento:

#### Posta un commento

[Post più vecchio](http://blog.cesaregallotti.it/2026/07/slittamento-delle-scadenze-dellai-act.html "Post più vecchio")
[Home page](http://blog.cesaregallotti.it/)

Iscriviti a:
[Commenti sul post (Atom)](http://blog.cesaregallotti.it/feeds/5209088888507832042/comments/default)

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

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjtA6P9GF1vc37l-JgNuPVc6Zxc39HghAiXpuAb7gOU-DyIsXVJHs0u2t-0AEBqHtTxScfazg_yt6Lkgp0OX_3Dy8qEuJw5bb5idkz3Xd16DyJi-iVB6Y8yJRo-j_hp_Y-19jZEvQXSI8LZEZz23HfeXVBXF9aTD3N7WneVk0r_3bcAymj8Q7pGd_kxEePt=s378)](http://blog.cesaregallotti.it/p/blog-page.html)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjdcGL6Kz5OasXxPPNY4U2pIGza6emK_DajDM67MB_XOYwDcCRYF8iZAOCwxvgnQv5P566eq7IHLF1bMrbVK5ATwo7D6zGkMyKR_f7_xGapVPxB7_bfXMhS9TxUe17hItfVFEJgU4c_4oDMZJ0pjn_CbdOkJJsteDeJH0RQyg1NXaM-vIdLfDFQj8qeLWEF=s356)](https://blog.cesaregallotti.it/p/blog-page_20.html)

## Iscriviti a questo Blog

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Post

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fblog.cesaregallotti.it%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fblog.cesaregallotti.it%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](http://blog.cesaregallotti.it/feeds/posts/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Post

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Commenti

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fblog.cesaregallotti.it%2Ffeeds%2F5209088888507832042%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fblog.cesaregallotti.it%2Ffeeds%2F5209088888507832042%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](http://blog.cesaregallotti.it/feeds/5209088888507832042/comments/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Comme...