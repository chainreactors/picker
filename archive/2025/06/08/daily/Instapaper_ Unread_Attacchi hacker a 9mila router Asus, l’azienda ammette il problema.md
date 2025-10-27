---
title: Attacchi hacker a 9mila router Asus, l’azienda ammette il problema
url: https://www.wired.it/article/router-asus-attacco-hacker-contromisure-soluzioni/
source: Instapaper: Unread
date: 2025-06-08
fetch_date: 2025-10-06T22:53:38.427680
---

# Attacchi hacker a 9mila router Asus, l’azienda ammette il problema

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

Attacchi hacker a 9mila router Asus, l’azienda ammette il problema

* [Scienza](/scienza/)
* [Economia](/economia/)
* [Cultura](/cultura/)
* [Gadget](/gadget/)
* [Security](/security/)
* [Diritti](/diritti/)
* [Idee](/idee/)
* [Video](/video/)
* [Podcast](/podcast-wired/)
* [Wired Consiglia](/wired-consiglia/)

More*Chevron*

[Cerca

Cerca](/search/)

* [Scienza](/scienza/)
* [Economia](/economia/)
* [Cultura](/cultura/)
* [Gadget](/gadget/)
* [Security](/security/)
* [Diritti](/diritti/)
* [Idee](/idee/)
* [Video](/video/)
* [Podcast](/podcast-wired/)
* [Wired Consiglia](/wired-consiglia/)

[Marco Schiaffino](/contributor/marco-schiaffino/)

[Security](/security/)

05.06.2025

# Attacchi hacker a 9mila router Asus, l’azienda ammette il problema

Sfruttata una vulnerabilità vecchia di 2 anni per compromettere i dispositivi dell’azienda taiwanese. Ecco come funziona l’attacco e cosa bisogna fare per eliminare la *backdoor* installata dai cyber criminali

![Attacchi hacker a 9mila router Asus lazienda ammette il problema](https://media-assets.wired.it/photos/68407ec124b3da7453bb3a2b/16:9/w_2560%2Cc_limit/Asus.png)

Migliaia di **router Asus** sono stati violati e “reclutati” nella botnet AyySSHush. L’attacco è stato individuato dalla società GreyNoise nel marzo scorso, ma i dettagli dell’attacco sono stati resi pubblici solo qualche giorno fa. Ora l’azienda con sede a Taiwan conferma l’esistenza del problema. La vicenda, però, è piuttosto complicata. Secondo i ricercatori di sicurezza che hanno analizzato l’attacco, infatti, non è escluso che si tratti dell’azione di un gruppo di “[hacker di stato](https://www.wired.it/article/corea-nord-lancia-unita-hacking-ai/)”.

## La scoperta della campagna di attacchi

I ricercatori di GreyNoise hanno rilevato gli attacchi ai router Asus grazie a un sistema di analisi basato su intelligenza artificiale che ha individuato una serie di anomalie nel traffico di alcuni router Asus, in particolare verso i modelli RT-AC3100, RT-AC3200 e RT-AX55. Le comunicazioni in questione, apparentemente trascurabili, erano in realtà l’indizio di **un attacco di brute forcing**, cioè una tecnica che prevede continui tentativi di accesso con credenziali sempre diverse, nel tentativo di “indovinare” quelle giuste.

![I volumi di attacchi di brute forcing. Fonte GreyNoise](https://media-assets.wired.it/photos/68407dc0912b2c202b43b992/master/w_1600%2Cc_limit/brute.jpg)

I volumi di attacchi di brute forcing. Fonte: GreyNoise

In seguito, i cyber criminali autori dell’attacco hanno cominciato a usare delle tecniche più evolute per aggirare i sistemi di autenticazione, sfruttando poi una vecchia vulnerabilità ([CVE-2023-39780](https://nvd.nist.gov/vuln/detail/CVE-2023-39780)) che consente di **eseguire comandi all’interno del sistema operativo** del router.

Utilizzando questa tecnica – e altre vulnerabilità che i ricercatori di GreyNoise non descrivono nel dettaglio – i cyber criminali hanno installato una connessione remota SSH sulla porta TCP 53282. In altre parole: hanno creato **una *backdoor*** che consente loro di controllare a distanza il router.

## Cosa c’è dietro gli attacchi e come reagire

Il sospetto degli esperti di sicurezza è che gli attacchi mirino a creare una nuova botnet, cioè una rete di “dispositivi zombie” sotto il controllo dei cyber criminali che li hanno compromessi.

Di solito, le botnet di questo genere vengono utilizzate per portare attacchi DDoS attraverso il collegamento in massa a siti o server per intasarne la connessione. È ciò che è accaduto in più occasioni in Italia a opera del gruppo filorusso NoName057, che ha preso di mira [aziende e istituzioni](https://www.wired.it/article/caso-mattarella-hacker-filorussi-attacchi/) a più riprese. GreyNoise, per [non esclude](https://www.greynoise.io/blog/stealthy-backdoor-campaign-affecting-asus-routers) che l’attacco sia stato portato da un gruppo più sofisticato, che farebbe rientrare la vicenda nella categoria degli attacchi “state sponsored”.

![Le analisi del sistema di intelligenza artificiale che hanno permesso di individuare gli attacchi. Fonte GreyNoise](https://media-assets.wired.it/photos/68407df9091be6406d98bc7c/master/w_1600%2Cc_limit/timeline.jpg)

Le analisi del sistema di intelligenza artificiale che hanno permesso di individuare gli attacchi. Fonte: GreyNoise

Gli utilizzatori dei router interessati dagli attacchi, si legge in un comunicato ufficiale di Asus, non possono risolvere il problema limitandosi ad aggiornare il firmware dei dispositivi. Per eliminare la backdoor è necessario, invece, **eseguire un ripristino alle impostazioni di fabbrica**.

La tecnica utilizzata dai cyber criminali, infatti, sfrutta una vulnerabilità che consente di registrare le impostazioni come legittime e, in quanto tali, **verrebbero mantenute anche con l’aggiornamento**. Come ulteriori accorgimenti, Asus consiglia di verificare che la porta TCP 53282 non sia accessibile dall’esterno della rete locale e di **controllare il registro di sistema** per verificare se siano presenti ripetuti errori di accesso, indizio di un possibile tentativo di compromissione.

## Un problema mai risolto

Può sembrare sorprendente che un attacco basato su un bug del 2023 possa ancora mietere così tante vittime a distanza di due anni. In realtà, il problema della vulnerabilità dei dispositivi di rete (e più in generale degli smart device) è qualcosa che il mondo della sicurezza informatica conosce bene e che si trascina da molto tempo. In assenza di sistemi di aggiornamento automatico, infatti, **l’installazione delle patch che correggono le vulnerabilità deve essere effettuato manualmente** e molti utenti non considerano i rischi collegati al mancato aggiornamento.

Tutto questo dovrebbe cambiare a partire dal 2027, quando entrerà ufficialmente in vigore il [Cyber Resilience Act](https://www.wired.it/article/open-source-europa-cyber-resilience-act-cybersicurezza/). Il regolamento dell’Unione Europea prevede una serie di accorgimenti per migliorare la sicurezza “by design” dei dispositivi della Internet of Things. Tra questi, appunto, la previsione di **aggiornamenti software automatici** che impediscano problemi come quello che ha interessato i router di Asus.

## Le storie da non perdere di Wired

* ⚡️Rivivi le “energie” del Wired Next Fest Trentino 2025: [leggi le interviste e rivedi i video](https://www.wired.it/topic/wired-next-fest-trentino-2025/)
* ⛵️ Il destino della missione della [Global Sumud Flotilla](https://www.wired.it/topic/global-sumud-flotilla), la flotta umanitaria diretta a Gaza
* 🔌 È in edicola il nuovo numero di *Wired* che parla di energia. [Abbonati!](https://abbonatiqui.it/rivista/wired)
* ❗️Il caso di Alberto Trentini, il cooperante in carcere in Venezuela da novembre 2024: [le notizie per non spegnere l'attenzione](https://www.wired.it/topic/alberto-trentini/) e chiederne l'immediata liberazione
* 🇺🇦 Le condizioni per un accordo tra Ucraina e Russia e [gli sviluppi del conflitto](https://www.wired.it/topic/ucraina/)
* 🇮🇱 🇵🇸 L'escalation [in Medio Oriente](https://www.wired.it/topic/israele/): cosa sta succedendo in [Israele](https://www.wired.it/topic/israele/) e la [crisi umanitaria a Gaza](https://www.wired.it/topic/striscia-di-gaza/)
* 🎤 [Leggi e guarda le interviste](https://www.wired.it/the-big-interview) agli ospiti di The Big Interview, il nuovo evento di Wired. [Anche su Youtube](https://www.youtube.com/%40wireditalia)
* 🎥 Le interviste, le video-news, i nostri reportage: [le notizie “da guardare”](https://www.wired.it/video/) di Wired
* ✍️ Vuoi ricevere comodamente a casa il magazine di Wired? [Abbonati qui](https://abbonatiqui.it/rivista/wired)
* 💬 Wired ha aperto il canale Whatsapp: [iscriviti subito!](https://www.wired.it/article/whatsapp-canali-wired/)
* 🛡️ Contro la violenza online, il [progetto Wired ...