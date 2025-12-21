---
title: Come estrarre i dati da una copia forense XRY per elaborarli con altri software di analisi
url: https://andrealazzarotto.com/2025/12/19/come-estrarre-i-dati-da-una-copia-forense-xry-per-elaborarli-con-altri-software-di-analisi/
source: Instapaper: Unread
date: 2025-12-20
fetch_date: 2025-12-21T03:27:07.459971
---

# Come estrarre i dati da una copia forense XRY per elaborarli con altri software di analisi

[Vai al contenuto](#content)

[Andrea Lazzarotto](https://andrealazzarotto.com/)

Informatica forense, sviluppo software e consulenza

[ ]

Menu +
×
esteso
chiuso

* [Home](https://andrealazzarotto.com/)
* [Chi sono](https://andrealazzarotto.com/about/)
* [Informatica forense](https://andrealazzarotto.com/informatica-forense/)
* [Servizi](https://andrealazzarotto.com/servizi/)
* [Blog](https://andrealazzarotto.com/blog/)
* [Contatti](https://andrealazzarotto.com/contatti/)

* [Facebook](https://www.facebook.com/AndreaLazzarottoSoftware/)
* [Twitter](https://twitter.com/TheLazza/)
* [Mastodon](https://mastodon.social/%40lazza)
* [LinkedIn](https://www.linkedin.com/in/andrealazzarotto/)
* [GitHub](https://github.com/Lazza/)
* [YouTube](https://www.youtube.com/c/AndreaLazzarotto)

# Come estrarre i dati da una copia forense XRY per elaborarli con altri software di analisi

Pubblicato da[Lazza](https://andrealazzarotto.com/author/lazza/)[19 Dicembre 202519 Dicembre 2025](https://andrealazzarotto.com/2025/12/19/come-estrarre-i-dati-da-una-copia-forense-xry-per-elaborarli-con-altri-software-di-analisi/)Pubblicato in: [Digital forensics](https://andrealazzarotto.com/category/digital-forensics/)Tag:[android](https://andrealazzarotto.com/tag/android/), [ios](https://andrealazzarotto.com/tag/ios/), [smartphone](https://andrealazzarotto.com/tag/smartphone/)

![](https://andrealazzarotto.com/wp-content/uploads/2025/12/conversione-xry-zip-1568x882.jpg)

XRY è un formato di file utilizzato per le copie forensi dall’omonimo software di acquisizione di dati da smartphone, nonché dalla suite di analisi XAMN. Entrambi i programmi sono sviluppati da MSAB, una multinazionale svedese che opera nel settore dell’informatica forense, per la quale [sono stato relatore in alcuni workshop](https://andrealazzarotto.com/2025/04/16/intervento-sulla-web-forensics-al-convegno-msab-di-milano-2025/).

Il formato XRY presenta alcuni vantaggi in termini di integrità dei dati, in quanto consiste in un *container* sicuro che racchiude i dati acquisiti da XRY e il risultato delle analisi effettuate con XAMN. Ma il fatto di essere un formato proprietario, con caratteristiche anti-manomissione, lo rende poco interoperabile con i software di altre aziende o i programmi di analisi open-source.

Una domanda ricorrente nelle comunità dedicate alla *digital forensics* riguarda proprio la necessità di convertire un’acquisizione forense in formato XRY affinché possa essere importata in altre suite di analisi.

Normalmente la risposta “classica”, che talvolta proponevo anch’io, era di utilizzare la propria licenza di XRY o XAMN per esportare i dati in formato ZIP.

Ciò non è sempre possibile, e può capitare di ricevere un file in formato XRY generato da un altro consulente. **La cosa interessante è che esiste una soluzione semplice e gratuita,** recentemente condivisa dall’utente DFxb all’interno del [Digital Forensics Discord Server](https://github.com/Digital-Forensics-Discord-Server), una comunità internazionale per i professionisti del settore.

Questa procedura può tornare utile a molti, perciò ritengo interessante condividerla qui con un articolo in lingua italiana per i colleghi che dovessero averne bisogno, ma anche come appunti per il futuro.

## Aprire la copia con XAMN Viewer

Se volete replicare le istruzioni descritte in questo articolo, dovete utilizzare un’immagine forense in formato XRY. Ho sperimentato la procedura con quella create da Josh Hickman e pubblicata [su Digital Corpora](https://digitalcorpora.org/corpora/cell-phones/android-13-image/https%3A//digitalcorpora.org/corpora/cell-phones/android-13-image/), di cui vi lascio il link:

[Android\_13\_MSAB.xry](https://digitalcorpora.s3.amazonaws.com/corpora/mobile/android_13/Android_13_MSAB.xry)

Avete inoltre bisogno di [XAMN Viewer](https://www.msab.com/download-xamn-viewer/), il visualizzatore gratuito messo a disposizione da MSAB per il sistema operativo Windows.

[XAMN Viewer per Windows](https://www.msab.com/xamn-viewer-launcher/)

Dopo aver avviato il programma (che non richiede installazione), è sufficiente cliccare su **Open** per caricare il file XRY di interesse. Una volta terminato il processo, vedrete alcune informazioni di base sui dati contenuti:

![Schermata che mostra la copia forense aperta con XAMN Viewer, si notano alcune informazioni di base come il numero di chiamate, messaggi e contatti](https://andrealazzarotto.com/wp-content/uploads/2025/12/xamn-viewer-home-1024x654.jpg)

Schermata iniziale di XAMN Viewer

## Esportare il file system

A questo punto è necessario identificare l’elenco dei file da esportare. Per prima cosa, selezionate **View all artifacts.** Nella schermata che si apre, identificate la modalità di visualizzazione indicata da **List** (in alto) e poi scegliete **File Tree.**

![Schermata che mostra le diverse modalità per visualizzare i dati con XAMN Viewer: List, Column, Gallery, File Tree e Chat.](https://andrealazzarotto.com/wp-content/uploads/2025/12/xamn-viewer-list.png)

Menù per cambiare la modalità di visualizzazione

Comparirà una elenco di file, che inizia dal nodo radice (per esempio *Tar Android\_13\_MSAB.xry*). Fate click con il tasto destro su questo elemento e scegliete l’opzione **Export all files.**

![Schermata che mostra l'albero delle directory contenute nel dispositivo. Sul nodo radice è stato attivato il menù contestuale, che mostra la voce "Export all files".](https://andrealazzarotto.com/wp-content/uploads/2025/12/xamn-viewer-esportazione-1024x341.png)

Opzione per avviare l’esportazione di tutti i file

XAMN Viewer salverà i dati nel percorso da voi scelto, generando una struttura di cartelle nella quale dovrete identificare quelle chiamata `Volumes`. All’interno di essa troverete la struttura dei file corrispondente al contenuto del dispositivo.

Alla fine del processo verrà mostrato anche **un file di log che indica eventuali cambi di nome** effettuati dal programma su alcuni file. Assicuratevi di leggerlo con attenzione.

## Creare un archivio ZIP

Nel mio esempio, c’era un’unica directory chiamata `data`. Ad ogni modo, se desiderate creare un archivio ZIP, dovete selezionare tutte le directory e aggiungerle a un archivio compresso. Questo rappresenta una *estrazione file system* che può essere importata in molti programmi di analisi.

È importante **verificare che la struttura dell’archivio ZIP sia corretta.** Quando lo aprite con un programma di gestione archivi, dovete vedere le directory corrispondenti al dispositivo. Se trovate una cartella `Volumes` come nodo radice, significa che l’archivio non è stato creato nel modo giusto.

Non vi resta altro che sbizzarrirvi a usare lo strumento che preferite per analizzare l’archivio ZIP. Io ho provato [ALEAPP](https://github.com/abrignoni/ALEAPP), un ottimo programma open-source che ha fatto un eccellente lavoro nell’interpretare i dati del dispositivo.

![Schermata che mostra una sezione di report generata con ALEAPP. Nello specifico si vede una pagina con alcuni messaggi di WhatsApp.](https://andrealazzarotto.com/wp-content/uploads/2025/12/aleapp-dati-xry-1024x576.jpg)

Report generato con ALEAPP

Per concludere, vi lascio i link alle guide sull’importazione degli archivi ZIP per alcuni dei principali software di analisi forense:

* MOBILedit Forensic: [Data from Folder/ZIP & Import file system](https://forensic.manuals.mobiledit.com/MM/data-from-folder-zip)
* Cellebrite PA: [Load Any Full File System Extraction Into Physical Analyzer](https://cellebrite.com/en/how-to-load-any-full-file-system-extraction-into-physical-analyzer-from-a-different-tool/)
* Magnet Axiom: [Loading Full File System Extractions in Magnet AXIOM](https://www.magnetforensics.com/blog/loading-graykey-images-into-magnet-axiom/)

### Condividi:

Share on Email[Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fandrealazzarotto.com%2F2025%2F12%2F19%2Fcome-estrarre-i-dati-da-una-copia-forense-xry-per-elaborarli-con-alt...