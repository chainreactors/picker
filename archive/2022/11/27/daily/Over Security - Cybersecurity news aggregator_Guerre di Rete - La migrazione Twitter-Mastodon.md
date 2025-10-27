---
title: Guerre di Rete - La migrazione Twitter-Mastodon
url: https://guerredirete.substack.com/p/guerre-di-rete-la-migrazione-twitter
source: Over Security - Cybersecurity news aggregator
date: 2022-11-27
fetch_date: 2025-10-03T23:53:34.104511
---

# Guerre di Rete - La migrazione Twitter-Mastodon

[![Guerre di Rete](https://substackcdn.com/image/fetch/$s_!JKxa!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c3cbe9e-1c39-4535-99d8-940270e03588_1010x1010.png)](/)

# [Guerre di Rete](/)

IscrivitiAccedi

# Guerre di Rete - La migrazione Twitter-Mastodon

### Exploit Signal e cyberwarfare. Starlink e Ucraina. DDoSecrets e giornalismo.

[![Avatar di Carola Frediani](https://substackcdn.com/image/fetch/$s_!tOoV!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9403bb00-3959-45dc-afb5-ac7994d708b8_750x741.jpeg)](https://substack.com/%40guerredirete)

[Carola Frediani](https://substack.com/%40guerredirete)

nov 26, 2022

19

[1](https://guerredirete.substack.com/p/guerre-di-rete-la-migrazione-twitter/comments)

Condividi

[![](https://substackcdn.com/image/fetch/$s_!-4DK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6b9ac4c7-dba7-4a3d-a916-3b0ecc6d0fa8_1426x716.png)](https://substackcdn.com/image/fetch/%24s_%21-4DK%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/6b9ac4c7-dba7-4a3d-a916-3b0ecc6d0fa8_1426x716.png)

*Immagine da [https://queer.party/@cassolotl](https://queer.party/%40cassolotl)*

**Guerre di Rete - una newsletter di notizie cyber
a cura di Carola Frediani
N.146 - 26 novembre 2022**

*Specie per i nuovi, ricordo che questa newsletter (che oggi conta più di 11mila iscritti - ma molti più lettori, essendo pubblicata anche online - e oltre 500 sostenitori) è gratuita e del tutto indipendente, non ha mai accettato sponsor o pubblicità, e viene fatta nel mio tempo libero. Se vi piace potete contribuire inoltrandola a possibili interessati, o promuovendola sui social. Molti lettori sono diventati sostenitori facendo una [donazione.](https://www.paypal.com/donate/?hosted_button_id=V8WAZ44NT942C) La prima campagna per raccogliere fondi è andata molto bene, e [qua ci sono i dettagli](https://guerredirete.substack.com/p/guerre-di-rete-vaccini-e-green-pass) (qua la [lista degli oltre 500 donator](https://associazione.guerredirete.it/donatori-di-guerre-di-rete/)i).*

[Dona alla newsletter](https://www.paypal.com/donate/?hosted_button_id=V8WAZ44NT942C)

*In più, a marzo il progetto si è ingrandito con un sito indipendente e noprofit di informazione cyber, [GuerrediRete.it](https://www.guerredirete.it/). Qui spieghiamo il [progetto](https://www.guerredirete.it/il-progetto/). Qui [l’editoriale](https://www.guerredirete.it/perche-e-il-momento-di-fare-e-informare/) di lancio del sito.*

**In questo numero:
- La migrazione Twitter-Mastodon vista da dentro
- Exploit per Signal e Ucraina
- Ultime dalla cyberwarfare scaturita dalla guerra
- Il ruolo di Starlink (e di Musk ) nella guerra in Ucraina
- L’ascesa del sito di leak DDoSecrets e il rapporto col giornalismo
- Altro**

*“Pietà per gli storici di domani, che cercheranno di dare un senso a petabyte di subtweet”* - Ben Tarnoff, T[he New York Review](https://www.nybooks.com/online/2022/11/11/in-the-hothouse-twitter-musk/?lp_txn_id=1398990)

*“È un casino: riconosco le persone da Twitter ma non riesco a ricordare se ci odiamo o no”.*[Ashley Quite Frankly](https://mastodon.lol/%40ashleyalready/109390794552782990), Mastodon.lol, Mastodon, Fediverso.

**TWITTER-MASTODON
È l’ora di tornare a parlare di social network e di cosa vogliamo**Uno degli effetti collaterali del nuovo corso di Twitter è che si è iniziato a registrare un afflusso di persone verso altre piattaforme, in particolare verso Mastodon, un social network decentralizzato e open source. Avrete visto molte guide su cosa è e come funziona Mastodon per cui non mi dilungo (mi limito a suggerire in italiano la pagina di [spiegazioni di Mastodon.it](https://mastodon.it/), che consiglio di leggere prima di tuffarsi nel fediverso; quella di Wired Italia - [Gli utenti di Mastodon ci spiegano come muovere i primi passi](https://www.wired.it/article/mastodon-primi-passi-guida/) - e quella de Il Post - [Che cos’è e come funziona Mastodon](https://www.ilpost.it/2022/11/07/mastodon/)).

**Qui inizia una parte esplicativa per nuovi, se siete esperti di Mastodon saltate fino al titoletto: “Chi si sta muovendo su Mastodon”**Siccome Mastodon (e più in generale il [fediverso](https://mastodon.it/it/fediverso)) può sembrare piuttosto complesso a chi si affaccia all’inizio, e la somiglianza con Twitter spesso è fatta, per così dire, di “f[alsi amici](https://it.wikipedia.org/wiki/Falso_amico)” (esattamente come in linguistica, per cui un termine in un’altra lingua sembra indicare la stessa cosa ma non è così), il mio personale suggerimento è di capire quei 4 concetti base: istanza (il condominio dove volete abitare, cioè aprire il vostro profilo), i toot (i tweet o post, dato che hanno più caratteri dei tweet), i boost (rilanci di altri o retweet), le tre timeline che potete visualizzare (*Home*, composta da tutti quelli che seguite, anche se stanno su istanze/condominii diversi; *Locale*, quelli che stanno sulla stessa vostra istanza/server/condominio, anche se non li seguite; *Federazione*, tutti i post pubblici di utenti che le persone nella vostra istanza seguono o rilanciano - vedi immagine di apertura in alto); e infine l’ordine cronologico inverso delle timeline, invece che algoritmico come su Twitter o Facebook. Acquisito tutto ciò, aprite un profilo e buttatevi.

**La decisione più importante all’inizio è la scelta dell’istanza** o server o condominio (qui una [lista](https://joinmastodon.org/it), qui un [motore di ricerca](https://instances.social/list#lang=it&allowed=&prohibited=&min-users=&max-users=) che mostra anche il numero utenti delle istanze, e altre variabili) che si può basare su vari parametri, ma per farla semplice considerate: **interessi** espressi dall’istanza (alcune sono nate attorno a dei temi o delle regioni); **amici o tipo di utenti** che già stanno lì; e **regole** di moderazione e gestione che si è data (ricordo che tutti i server registrati sul sito Mastodon hanno sottoscritto un patto, il [Mastodon Server Covenant](https://joinmastodon.org/covenant), che prevede la moderazione attiva contro razzismo, sessismo, omofobia, transfobia). Vi consiglio di guardare sempre, nella home dell’istanza, la voce Scopri di più (esempio: <https://infosec.exchange/about>). Qua trovate le regole che si è data e i server o istanze che blocca o silenzia.

Ciò detto, **qualche consiglio utile in ordine sparso:**

1) **Iscrivetevi dal browser** prima, e dopo usate l’app (qui una [lista](https://joinmastodon.org/it/apps)), funziona meglio l’esperienza. Questo non l’ho verificato di persona ma l’ho visto segnalato più volte, [come qua](https://clivethompson.medium.com/come-join-me-on-mastodon-folks-bbb073ff05d2).

2) **Per cercare i vostri amici di Twitter** si possono usare alcune app: [Debirdifly](https://pruvisto.org/debirdify/) - [Twitodon](https://twitodon.com/) - [Fedfinder](https://fedifinder.glitch.me/) e molto funzionale [Movetodon](https://www.movetodon.org/) (disabilitatele dopo dalle Impostazioni di Mastodon, in Account >App Autorizzate). Oppure se non volete autorizzare app, digitate "Mastodon" nella casella di ricerca di Twitter e cambiate il filtro in "Persone che segui" per vedere quali dei vostri contatti hanno condiviso un indirizzo Mastodon (via [PatrickW](https://twitter.com/PatrickW/status/1593591859800145921))
BONUS: qua ci sono [liste di accademici](https://github.com/nathanlesage/academics-on-mastodon) su Mastodon, via [Ryan](https://mastodon.social/%40ryanschultz/109360156223130510).

2) **Per farvi trovare dagli amici di Twitter**: scrivete il vostro indirizzo Mastodon - nome utente più il server o istanza dove state - nel nome o nella bio.
...