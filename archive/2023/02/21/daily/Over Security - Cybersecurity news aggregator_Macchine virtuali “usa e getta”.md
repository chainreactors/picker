---
title: Macchine virtuali “usa e getta”
url: https://hackerjournal.it/11376/macchine-virtuali-usa-e-getta/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-21
fetch_date: 2025-10-04T07:38:41.403616
---

# Macchine virtuali “usa e getta”

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

#### Macchine virtuali “usa e getta”

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

# Macchine virtuali “usa e getta”

Imparate a padroneggiare Multipass, il sistema di virtualizzazione che funziona su qualsiasi piattaforma desktop

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

20 Febbraio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2023/02/multipass_1.png)

* Share
* Tweet

Agli sviluppatori piace poter avviare rapidamente delle [macchine virtuali](https://hackerjournal.it/10682/hyperjacking-macchine-virtuali-vmware-sotto-attacco/) per i test ma quando scrivono codice su piattaforme diverse diventa un po’ più complesso farlo usando differenti stack di virtualizzazione. **Ubuntu fornisce però una soluzione per creare VM veloci e “usa e getta” su computer basati su processori Intel che è anche supportata dai nuovi dispositivi con chip Apple M1, seppure con alcune limitazioni. Si chiama Multipass** ed è un front-end per avviare macchine virtuali, ma può supportare molti back-end diversi, tra cui Virtual Box, LXD, KVM e altri. **L’installazione di Multipass in Linux richiede che sia presente Snap**:

**$ sudo snap install multipass**

**$ sudo snap info multipass**

Trovate le istruzioni per l’installazione in Windows e macOS all’indirizzo <https://multipass.run>. Multipass è disponibile sia a riga di comando sia con un’interfaccia grafica rudimentale. **Qui utilizzeremo la versione a riga di comando perché offre una maggiore flessibilità**. Al termine dell’installazione dello strumento, è consigliabile riavviare il sistema.

### **Primi passi con Multipass**

Per iniziare a usare Multipass, aprite una finestra del terminale e usate il seguente comando:

**$ multipass launch**

Scaricherà e creerà una nuova macchina virtuale con un nome generato dinamicamente. **La prima volta, la creazione di una VM potrebbe richiedere qualche istante, perché bisogna scaricare l’immagine di base di Ubuntu**. Per impostazione predefinita, il tool utilizzerà l’ultima immagine di Ubuntu server disponibile per l’uso in Multipass sulla piattaforma su cui è in esecuzione. Questa prima macchina virtuale è speciale ed è contrassegnata come istanza primaria. **Di default (in Linux) l’istanza primaria monta anche la cartella Home dell’utente. Nella macchina virtuale viene visualizzata come una cartella denominata Home all’interno della directory Home esistente**, quindi potete accedere ai file come se facessero parte del normale filesystem. Le macchine virtuali aggiuntive richiedono un ulteriore comando:

**$ multipass mount $HOME**

**lfexample4 /home/home**

È possibile avere più mount su una stessa macchina virtuale e non è necessario esportare i mount in una variabile. Si possono sostituire le variabili con dei percorsi: per esempio, **$HOME** potrebbe essere **Downloads** per esporre alla VM solo la cartella degli scaricamenti. Lo smontaggio si effettua utilizzando il comando **unmount : multipass umount lfexample4 / home/home**. Si può accedere alla macchina virtuale primaria anche tramite una console grafica, aprendo il menu a tendina e selezionando open [shell](https://hackerjournal.it/encyclopedia/shell/ "Un termine Unix per l'interfaccia utente interattiva con un sistema operativo. La shell è il livello di programmazione che comprende ed esegue i comandi immessi da un utente. In alcuni sistemi, la shell è chiamata interprete di comandi. "). Altri modi per ottenere una [shell](https://hackerjournal.it/encyclopedia/shell/ "Un termine Unix per l'interfaccia utente interattiva con un sistema operativo. La shell è il livello di programmazione che comprende ed esegue i comandi immessi da un utente. In alcuni sistemi, la shell è chiamata interprete di comandi. ") nella VM includono il comando **Multipass [shell](https://hackerjournal.it/encyclopedia/shell/ "Un termine Unix per l'interfaccia utente interattiva con un sistema operativo. La shell è il livello di programmazione che comprende ed esegue i comandi immessi da un utente. In alcuni sistemi, la shell è chiamata interprete di comandi. ")** che si può usare per eseguire una [shell](https://hackerjournal.it/encyclopedia/shell/ "Un termine Unix per l'interfaccia utente interattiva con un sistema operativo. La shell è il livello di programmazione che comprende ed esegue i comandi immessi da un ute...