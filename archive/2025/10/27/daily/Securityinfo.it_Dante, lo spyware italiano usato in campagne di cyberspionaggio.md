---
title: Dante, lo spyware italiano usato in campagne di cyberspionaggio
url: https://www.securityinfo.it/2025/10/27/dante-lo-spyware-italiano-usato-in-attacchi-di-cyberspionaggio/?utm_source=rss&utm_medium=rss&utm_campaign=dante-lo-spyware-italiano-usato-in-attacchi-di-cyberspionaggio
source: Securityinfo.it
date: 2025-10-27
fetch_date: 2025-10-28T03:08:25.152463
---

# Dante, lo spyware italiano usato in campagne di cyberspionaggio

Aggiornamenti recenti Ottobre 27th, 2025 12:07 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Dante, lo spyware italiano usato in campagne di cyberspionaggio](https://www.securityinfo.it/2025/10/27/dante-lo-spyware-italiano-usato-in-attacchi-di-cyberspionaggio/)
* [CERT-AGID 18–24 ottobre: phishing a tema PagoPA e Fascicolo Sanitario](https://www.securityinfo.it/2025/10/27/cert-agid-18-24-ottobre-phishing-pagopa-fascicolo-sanitario/)
* [Il Pwn2Own Irlanda si è concluso con oltre 1 milione di dollari di vincite](https://www.securityinfo.it/2025/10/24/il-pwn2own-irlanda-si-e-concluso-con-oltre-1-milione-di-dollari-di-vincite/)
* [Lazarus ha colpito alcune compagnie europee del settore della difesa](https://www.securityinfo.it/2025/10/23/lazarus-ha-colpito-alcune-compagnie-europee-del-settore-della-difesa/)
* [Arriva “Zyxel Commercialisti Italia”, iniziativa per educare i professionisti alla cybersecurity](https://www.securityinfo.it/2025/10/22/arriva-zyxel-commercialisti-italia-iniziativa-per-educare-i-professionisti-alla-cybersecurity/)

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

## Dante, lo spyware italiano usato in campagne di cyberspionaggio

Ott 27, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Campagne malware](https://www.securityinfo.it/category/approfondimenti/campagne-malware/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/10/27/dante-lo-spyware-italiano-usato-in-attacchi-di-cyberspionaggio/#respond)

---

**Dante**, un sofisticato e finora sconosciuto**spyware italiano** sviluppato da Memento Labs (ex Hacking Team), è stato utilizzato in diversi attacchi legati a **Operation ForumTroll**, una campagna di spionaggio contro obiettivi russi e bielorussi attribuita al gruppo ForumTroll APT. A scoprirlo è stato il team di ricercatori di [Kaspersky](https://securelist.com/forumtroll-apt-hacking-team-dante-spyware/117851/) guidato da Boris Larin, Principal Security Researcher di Kaspersky.

Nelle email gli attaccanti invitavano le vittime (dipendenti di, tra le altre realtà, università ed enti governativi) a partecipare a eventi professionali cliccando su un link personalizzato. La caratteristica più allarmante di questi attacchi stava nella semplicità con cui avveniva l’infezione: bastava che l’utente aprisse il link per aprire una pagina malevola che distribuiva il malware.

“*A marzo 2025, Kaspersky ha individuato una serie di **infezioni che avvenivano non appena un utente cliccava su link personalizzati di phishing inviati via email.** Non servivano altre azioni per dare inizio all’infezione; visitare il sito web malevolo usando Chrome o un altro browser basato su Chromium era sufficiente*” ha affermato Larin.

![Dante](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t0msmt0msmt0msmt.png)

La campagna ha sfruttato la CVE-2025-2783, una **vulnerabilità di Chrome** presente nella logica di gestione degli *pseudo-handle*di Windows che permette di aggirare la protezione sandbox del browser, scoperta da Kaspersky e risolta da Google.

Superato questo livello di protezione, ForumTroll APT è riuscito a stabilire la persistenza sui dispositivi delle vittime, eseguire il loader e caricare **LeetAgent**, un malware usato per il cyberspionaggio. Lo spyware si connette a uno dei server C2 del gruppo, quello specificato nella configurazione in uso, ed è in grado di riceve ed eseguire comandi per, tra gli altri, ottenere la lista dei task che sta eseguendo, scrivere e leggere file, iniettare shellcode e soprattutto effettuare keylogging ed esfiltrare file. Di default, lo spyware cerca e raccoglie file con estensioni \*.doc, \*.xls, \*.ppt, \*.rtf, \*.pdf, \*.docx, \*.xlsx, \*.pptx.

## Dante: la firma italiana dietro un nuovo cluster di attacchi

Oltre alle catene di infezione con LeetAgent scoperte in Operation ForumTroll, i ricercatori hanno identificato **un altro cluster di attacchi che usava uno spyware molto più sofisticato**. Anche in questo caso il malware era stato usato almeno dal 2022 e la catena di infezione cominciava sempre con email di phishing con link malevoli.

“*Gli attaccanti dietro questa attività hanno usato path di sistema simili e la stessa tecnica di persistenza del cluster di LeetAgent*” ha spiegato Larin. “*Questo ci ha fatto sospettare che i due cluster potessero essere legati e siamo riusciti a confermare questa connessione diretta quando abbiamo scoperto gli attacchi dove LeetAgent eseguiva questo spyware molto più sofisticato*“.

Analisi aggiuntive hanno portato all’identificazione di **Dante, uno spyware commerciale sviluppato da Memento Labs.**Noto precedentemente come Hacking Team, è uno dei vendor storici più noti, fondato nel 2003. Il gruppo è conosciuto soprattutto per aver sviluppato Remote Control System (RCS), uno spyware utilizzato da diversi governi.

Dopo essere stata acquisita da InTheCyber Group nel 2019 ed essere stata rinominata “Memento Labs”, nel 2023 la compagnia ha annunciato Dante, un nuovo tool di sorveglianza di cui non si conosceva molto, almeno finora.

![](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_n76bnsn76bnsn76b.png)

Dall’analisi di Kaspersky è emerso che lo spyware utilizza **VMProtect**, una tecnica di anti-analisi complessa che offusca il flusso di controllo e le funzioni importate. Dante usa inoltre una tecnica di **anti-hooking** per eludere il monitoraggio che risolve dinamicamente le API e crea degli *stub* per le chiamate di sistema.

In aggiunta, per non essere individuato, lo spyware controlla il log degli eventi di Windows per verificare se ci sono in uso macchine virtuali o strumenti di analisi contro il malware, controllando di fatto se l’ambiente è sicuro per continuare l’esecuzione.

Dopo aver effettuato e superato tutti i controlli, Dante decripta la propria configurazione e l’orchestratore, il modulo centrale del malware che si occupa di comunicare col server C2, gestire gli altri moduli e la configurazione, eseguire **controlli di protezione** e, in caso di necessità, come per esempio quando non riceve dei comandi per un certo numero di giorni, **auto-cancellarsi.**

Al momento il team di Kaspersky non è riuscito a individuare e analizzare altri moduli dello spyware perché sembra che non ci siano altre infezioni in corso.

Il segretissimo Dante, che Memento Labs è riuscita a tenere nascosto fino a ora, è stato alla fine scoperto e analizzato, almeno per quanto riguarda il modulo princi...