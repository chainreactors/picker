---
title: Falla vecchia di 16 anni minaccia milioni di router Wi-Fi
url: http://www.zeusnews.it/n.php?c=32626
source: Instapaper: Unread
date: 2026-10-21
fetch_date: 2026-10-22T06:46:41.320503
---

# Falla vecchia di 16 anni minaccia milioni di router Wi-Fi

![](https://b.scorecardresearch.com/p?c1=2&c2=13879765&cv=2.0&cj=1)

[![Zeus News](/pic/logo.gif)](/)

[Salta il menu](#contenuto)

* [Home](http://www.zeusnews.it)
* [Editoriale](index.php3?ar=sezioni&numero=949)
* [Recensioni](index.php3?ar=sezioni&numero=912)
* [Focus](index.php3?ar=sezioni&numero=913)
* [Sicurezza](index.php3?ar=sezioni&numero=901)
* [Trucchi](index.php3?ar=sezioni&numero=906)
* [Maipiusenza](index.php3?ar=sezioni&numero=903)
* [Segnalazioni](index.php3?ar=sezioni&numero=905)
* [Sondaggi](index.php3?ar=sezioni&numero=902)
* [Antibufala](index.php3?ar=sezioni&numero=904)
* [Download](index.php3?ar=sezioni&numero=916)
* [News](index.php3?ar=sezioni&numero=907)
* [Flash](index.php3?ar=sezioni&numero=914)
* [Pag2](index.php3?ar=sezioni&numero=915)

[![Newsletter](pic/pulsanti/newsletter.png "Newsletter")](http://newsletter.zeusnews.it/index.php?p=subscribe&id=5)
[![RSS](pic/pulsanti/rss.png "Feed RSS")](http://feeds.feedburner.com/ZeusNews)
[![Facebook](pic/pulsanti/facebook.png "Zeus News su Facebook")](http://www.facebook.com/ZeusNews)
[![Forum Olimpo Informatico](pic/pulsanti/forum.png "Forum Olimpo Informatico")](http://forum.zeusnews.com/index.php?c=1)
[![Contatti](pic/pulsanti/contatti.png "Contatti")](http://www.zeusnews.it/index.php3?ar=staff)
[![Accadde oggi](pic/pulsanti/calendar3.png "Accadde oggi")](http://www.zeusnews.it/index.php3?ar=accaddeoggi)
[![Ricerca](pic/pulsanti/ricerca.png "Cerca in Zeus News")](http://www.zeusnews.it/index.php3?ar=ricerca)

[Newsletter](http://newsletter.zeusnews.it/index.php?p=subscribe&id=5)
[Feed RSS](http://feeds.feedburner.com/ZeusNews)
[Facebook](http://www.facebook.com/ZeusNews)
[Forum](http://forum.zeusnews.com/index.php?c=1)
[Contatti](http://www.zeusnews.it/index.php3?ar=staff)
[Accadde oggi](http://www.zeusnews.it/index.php3?ar=accaddeoggi)
[Cerca](http://www.zeusnews.it/index.php3?ar=ricerca)

# Falla vecchia di 16 anni minaccia milioni di router Wi-Fi

Colpiti soprattutto i router Broadcom. Rischio sottrazione di dati sensibili ed esecuzione remota di codice senza conoscere la chiave del Wi-Fi.

[Tweet](https://twitter.com/share)

[*ZEUS News* - [www.zeusnews.it](https://www.zeusnews.it/) - 21-10-2026] Commenti

![wifi router broadcom falla 16 anni](https://www.zeusnews.it/img/6/2/6/2/3/0/032626-620-wifi-router-broadcom-falla-16-anni.jpg)

Foto di [Dreamlike Street](https://unsplash.com/it/%40dreamlikestreet).

Milioni di [router Wi-Fi](util/extlink/cerca_amazon.php?q=router Wi-Fi "Cerca router Wi-Fi su Amazon") in tutto il mondo potrebbero essere vulnerabili a un attacco che non richiede né la password della rete né il completamento della procedura di associazione WPS. A portare alla luce il problema è una [ricerca](/link/48343 "https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/") che descrive una falla presente da almeno 16 anni in componenti software sviluppati da Broadcom, capace in alcuni casi di consentire l'esecuzione remota di codice e il controllo del dispositivo direttamente via radio. La vulnerabilità è stata documentata dal ricercatore Quentin Kaiser durante una presentazione tenuta alla conferenza Hexacon di Parigi. Per identificare il problema ha utilizzato il nome *WPSplinter*, una denominazione scelta dopo il rifiuto di Broadcom di assegnare un identificativo CVE ufficiale alla falla.

Secondo l'analisi tecnica pubblicata dal ricercatore, il difetto risiede nell'implementazione proprietaria di WPS integrata nel kit di sviluppo software di [Broadcom](util/extlink/cerca_amazon.php?q=Broadcom "Cerca Broadcom su Amazon"). Il componente vulnerabile gestisce in modo errato particolari messaggi del protocollo Wi-Fi e può essere indotto a divulgare contenuti della memoria o a eseguire codice arbitrario inviato dall'attaccante. Uno degli aspetti più rilevanti è che l'attacco non richiede la conoscenza della chiave della rete wireless. Secondo la documentazione pubblicata, è sufficiente trovarsi all'interno della copertura radio del dispositivo bersaglio. Inoltre, il problema non è collegato alla storica debolezza del PIN WPS emersa anni fa, ma riguarda direttamente il codice sviluppato da Broadcom per la gestione del protocollo.

La ricerca descrive due differenti categorie di impatto. La prima consente la divulgazione di informazioni sensibili memorizzate nel router. La seconda permette invece l'esecuzione remota di codice senza autenticazione preventiva. Nelle dimostrazioni pubblicate, Quentin Kaiser ha mostrato come sia possibile estrarre la [chiave](util/extlink/cerca_amazon.php?q=chiave "Cerca chiave su Amazon") Wi-Fi memorizzata nel dispositivo e, in altri casi, ottenere una shell remota direttamente attraverso frame Wi-Fi, senza necessità di connessioni Internet o infrastrutture esterne. I test sono stati condotti su dispositivi distribuiti da diversi fornitori di connettività in Belgio. Il ricercatore ha dichiarato di aver verificato la presenza della vulnerabilità su apparati utilizzati da tre dei quattro principali operatori del Paese, arrivando a stimare circa 1,5 milioni di dispositivi vulnerabili soltanto nel mercato belga.

L'impatto effettivo potrebbe però essere molto più ampio. La documentazione tecnica individua router e punti di accesso basati sugli stessi componenti software distribuiti da numerosi produttori internazionali, tra cui [Cisco](util/extlink/cerca_amazon.php?q=Cisco "Cerca Cisco su Amazon"), [TP-Link](util/extlink/cerca_amazon.php?q=TP-Link "Cerca TP-Link su Amazon"), [Netgear](util/extlink/cerca_amazon.php?q=Netgear "Cerca Netgear su Amazon"), [Zyxel](util/extlink/cerca_amazon.php?q=Zyxel "Cerca Zyxel su Amazon"), [Nokia](util/extlink/cerca_amazon.php?q=Nokia "Cerca Nokia su Amazon"), [ZTE](util/extlink/cerca_amazon.php?q=ZTE "Cerca ZTE su Amazon") e altri. L'elenco pubblicato dal ricercatore è esplicitamente definito incompleto e potrebbe comprendere migliaia di modelli differenti.

Per approfondire:

[![](/img/9/6/4/2/3/0/032469-620-ue-obbligo-segnalazione-falle.jpg)](/zn/32469)

[UE, la segnalazione delle vulnerabilità nei prodotti adesso è obbligat...](/zn/32469 "UE, la segnalazione delle vulnerabilità nei prodotti adesso è obbligatoria")

[![](/img/1/9/3/2/3/0/032391-620-comcast-wifi-rilevatore-movimento.png)](/zn/32391)

[Comcast trasforma i router Wi-Fi in sensori di movimento](/zn/32391 "Comcast trasforma i router Wi-Fi in sensori di movimento")

[![](/img/3/9/1/2/3/0/032193-620-openai-chip-jalapeno-nvidia.jpg)](/zn/32193)

[Jalapeño, il primo chip di OpenAI: più efficienza e meno costi operati...](/zn/32193 "Jalapeño, il primo chip di OpenAI: più efficienza e meno costi operativi")

[![](/img/4/7/9/1/3/0/031974-620-tplink-router-attacco-russo.png)](/zn/31974)

[Router TP-Link compromessi in tutto il mondo: così gli hacker russi sottrag...](/zn/31974 "Router TP-Link compromessi in tutto il mondo: così gli hacker russi sottraggono le credenziali")

Il codice vulnerabile sarebbe presente nel kit di sviluppo di Broadcom almeno dal 2010. Una correzione parziale sarebbe stata distribuita in modo silenzioso nel 2018, seguita dall'introduzione di una nuova generazione di strumenti software che sostituiva il componente vulnerabile. Tuttavia, molte aziende produttrici non avrebbero adottato tali modifiche, lasciando il codice originale nei dispositivi ancora oggi in circolazione. La vicenda è resa ancora più complessa dalla gestione della divulgazione. Quentin Kaiser sostiene che Broadcom fosse a conoscenza del problema almeno dal 2018 e che abbia rifiutato sia l'assegnazione di un identificativo CVE sia una comunicazione pubblica più ampia. Secondo il ricercatore, l'assenza di un identificativo ufficiale avrebbe contribuito a limitare la diffusione degli avvisi lungo la filiera composta da produttori di [router](util/extlink/cerca_amazon.php?q=router "Cerca router su Amazon") e operatori di telecomunicazioni.

Da parte propria, Broadcom avrebbe risposto affermando di aver sostituito il codice vulnerabile già nel 2018 e di c...