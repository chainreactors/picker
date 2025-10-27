---
title: Messaggi segreti a prova di spia
url: https://hackerjournal.it/11339/messaggi-segreti-a-prova-di-spia/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-14
fetch_date: 2025-10-04T06:33:05.661818
---

# Messaggi segreti a prova di spia

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

#### Messaggi segreti a prova di spia

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

### [Articoli](https://hackerjournal.it/category/tech/)

# Messaggi segreti a prova di spia

Grazie alla steganografia potrete tutelare al massimo le vostre comunicazioni private e farle passare sotto il naso di chiunque

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

13 Febbraio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

* Share
* Tweet

Si chiama steganografia (dal greco per “scrittura nascosta”) quella tecnica che permette di occultare un messaggio in forma di file di testo all’interno di un altro file del tutto insospettabile come una innocente immagine JPG. Così facendo, solo chi è a conoscenza della presenza del messaggio potrà trovarlo e leggerlo. Ci sono diverse applicazioni e metodi per nascondere un file all’interno di un altro. Uno dei più semplici è quello di comprimere in un file .zip il documento da nascondere e di metterlo nella cartella in cui si trova l’immagine all’interno della quale andrà inserito. Dopodiché, aperto il Terminale ed entrati nella cartella con i due file, dovrete eseguire una riga di comando con la sintassi:

**$ cat [nomefile].jpg [nomefile].zip > [nuovofile].jpg**

Per recuperare il file nascosto, basterà poi eseguire la riga di comando:

**$ unzip [nuovofile].jpg**

Se volete anche proteggere il file con una password, allora è necessario usare uno strumento come Steghide che si installa da Terminale eseguendo semplicemente:

**$ sudo apt install steghide**

La sintassi per nascondere un file TXT in un JPG, ricordando che i due elementi devono trovarsi nella stessa cartella, è la seguente:

**$ steghide embed -ef [nomefile].txt -cf [nomefile].jpg**

A questo punto lo strumento vi chiederà di stabilire la password a protezione del documento. Per estrarre il file nascosto dovrete invece eseguire:

**$ steghide extract -sf [nomefile].jpg**

e poi digitare la password.

### **Strumenti con interfaccia grafica**

**Fino a questo momento sono stati presi in considerazione solo strumenti che si utilizzano da riga di comando, ma ne esistono anche con una più comoda interfaccia grafica, come Stegosuite**. Tuttavia, come nei casi visti in precedenza, si tratta di un’applicazione minimalista. Volendo avere a disposizione qualcosa di più complesso, capace di garantire un più alto livello di protezione ai vostri file nascosti, è consigliabile affidarsi a Steg. Oltre ad avere un’interfaccia grafica, ha anche il vantaggio di poter creare vari tipi di password con diversi livelli di complessità. Anche se è in inglese, l’interfaccia è piuttosto facile da usare e impiegherete poco tempo a destreggiarvi con essa, riuscendo a nascondere ed estrarre messaggi velocemente. Steg non va installato e, come vedrete nella guida, dovrete rendere eseguibile tramite riga di comando il file **AppImage** che serve ad avviare l’applicazione. Tuttavia, compiuta una volta questa operazione, potrete avviare Steg quando vorrete con un semplice doppio clic sul suo file eseguibile.

IN PRATICA

### **NASCONDETE UN FILE DI TESTO IN UN’IMMAGINE USANDO STEG**

**#1**
Con il vostro programma di navigazione collegatevi a questo indirizzo <https://www.fabionet.org/download>. Fate clic su **Steg for Linux 64 bit** e poi, nella sezione **Download Link**, su **Steg-1.1.0.0-Linux-x64.tgz**. Quindi aprite la cartella in cui l’avete scaricato.

![](https://hackerjournal.it/wp-content/uploads/2023/02/passo_1.png)

**#2**Fate un doppio clic sul file appena scaricato e, nella finestra che si apre, premete su **Estrai**. Come cartella di destinazione selezionate **Home** e fate di nuovo clic su **Estrai**, quindi chiudete tutte le finestre aperte e avviate una sessione del Terminale.

![](https://hackerjournal.it/wp-content/uploads/2023/02/passo_2.png)

**#3**Eseguite la riga cd Steg.1.1.0.0-Linux-x64, poi digitate **chmod a+x Steg\*.AppImage** e premete **INVIO** per rendere eseguibile il file di installazione, dopodiché lanciate la riga di comando **./Steg\*.AppImage**. Nella finestra **Accept Eula**, scorrete il contratto fino in fondo e fate clic su **Yes**.

![](https://hackerjournal.it/wp-content/uploads/2023/02/passo_3.png)

**#4**Fate clic su **OK** nella finestra di de[bug](https://hackerjournal.it/encyclopedia/bug/ "Un bug è un termine inglese che può essere tradotto in italiano come “baco”. In informatica viene usato per indicare un guasto che causa ...