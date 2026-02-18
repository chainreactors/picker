---
title: Come Pensa la Macchina
url: https://pinperepette.github.io/signal.pirate/articoli/come-pensa-la-macchina.html
source: Instapaper: Unread
date: 2026-02-17
fetch_date: 2026-02-18T04:16:28.105891
---

# Come Pensa la Macchina

[SIGNALPIRATE](../index.html)

* [Home](../index.html)
* [Articoli](../index.html#articoli)
* [GitHub](https://github.com/pinperepette)

2026-02-16 | Pinperepette

# Come Pensa la Macchina

Un LLM smontato pezzo per pezzo. Tokenizzazione, embeddings, attention, hallucinations. Ollama in locale, zero fuffa.

Transformer
Embeddings
Attention
Ollama

## // L'Apicoltrice e il Pappagallo

Sezione 01. L'antefatto

La iena usa ChatGPT sull'iPad. Non per lavoro. Per le api, per le galline, per capire perché la Nera non fa un uovo da ottobre, per sapere se la regina nuova è buona. Le cose che le interessano. Lo usa come userebbe un'enciclopedia, con la differenza che l'enciclopedia non si contraddiceva da sola.

L'altra sera stava chiedendo qualcosa sulle api. Il modello le ha risposto, e da qualche parte nella risposta si è contraddetto. Non so cosa esattamente, perché quando la iena ha iniziato a spiegarmi il problema io ero già in modalità automatica: annuisco a 0.3 Hz, lo sguardo fisso che simula attenzione, il cervello su un altro thread. La stessa frequenza di campionamento della cena di San Valentino. Funziona da 26 anni, non vedo motivo di cambiarla.

Quello che ho sentito, filtrato dal mio passa-basso cognitivo, è stato più o meno: "...si è contraddetto... ha scritto una cosa e poi il contrario... bla bla bla... l'intelligenza artificiale non serve a niente... bla bla bla... non capisco come fai ad avere tutto questo lavoro con una roba così stupida... bla bla bla... non sostituirà mai nessuno... bla bla bla..."

Annuisco. 0.3 Hz. "Hai ragione." Non ho la minima idea di cosa abbia detto ChatGPT di sbagliato sulle api. Ma la iena ha ragione su una cosa, anche se non nel senso che intende lei: c'è un problema enorme con come la gente parla di intelligenza artificiale.

Perché ci penso, quella sera, dopo che la iena si è addormentata. E mi rendo conto che ho letto decine di articoli su come funzionano gli LLM. Centinaia forse. E il 99,9999% erano cagate. "L'AI capisce il contesto." "I neuroni si attivano come nel cervello." "Il modello ragiona." Metafore colorate, infografiche carine con le frecce, zero formule, zero codice, zero esperimenti. Gente che spiega cose che non capisce, usando parole che non significano quello che pensano. Una catena di pappagalli che scrivono articoli sui pappagalli.

Allora lo scrivo io. Smonto la macchina pezzo per pezzo. Ho [Ollama](https://ollama.com) sul Mac con una decina di modelli. Scelgo il più piccolo: `llama3.1:8b`, 8 miliardi di parametri, 4.9 gigabyte su disco. Il più facile da maneggiare senza sbatti, e tanto l'architettura è identica per tutti: che siano 8 miliardi o 405 miliardi, il meccanismo è lo stesso. Cambiano le dimensioni delle matrici, non come funziona la macchina. Lo apro dal terminale, guardo i byte, e seguo il percorso completo: dal testo che entra al testo che esce. Ogni passaggio, ogni formula, ogni decisione matematica. Niente metafore del cervello. Niente fuffa. Se vuoi capire come funziona una cosa, la smonti. Non leggi chi ne scrive.

0B

Parametri

0 GB

Dimensione su disco

0

Transformer layer

0K

Vocabolario token

## // 4 Giga di Coscienza

Sezione 02. Dentro il file

![La scrivania di notte: terminale aperto, Ollama che gira, la iena dorme](../immagini/desktop.jpg)

La scrivania. La iena dorme. Il terminale è aperto. Si smonta.

La iena dorme. Io apro il terminale. Il modello è un file. Un singolo file da 4.920.738.944 byte, seduto nella cartella `~/.ollama/models/blobs/`. Tutto quello che "sa" Llama 3.1 8B, tutto quello che ha "imparato" da terabyte di testo, è compresso in quei byte. Niente magia, niente coscienza. Numeri.

I primi byte li leggo con `xxd`:

00000000: 4747 5546 0300 0000 2401 0000 0000 0000 GGUF....$.......
00000010: 1d00 0000 0000 0000 1400 0000 0000 0000 ................
00000020: 6765 6e65 7261 6c2e 6172 6368 6974 6563 general.architec
00000030: 7475 7265 0800 0000 0500 0000 0000 0000 ture............
00000040: 6c6c 616d 61 0c00 0000 0000 0000 67656e llama........gen

`GGUF`: i primi quattro byte. Il magic number del formato. Come `%PDF` all'inizio di un PDF, o `PK` in uno ZIP. Dice al software che tipo di file è. Dopo il magic: la versione (3), il numero di tensori (292) e il numero di metadati (29).

Lo apro dal terminale con `xxd`, lo stesso approccio che userei per qualsiasi binario. Non è codice eseguibile, è un formato dati, ma il principio è lo stesso: vuoi capire una cosa, guardi i byte. L'header si legge in chiaro: architettura, numero di layer, dimensione dei vettori, tipo di quantizzazione. Tutto scritto nei primi kilobyte.

![Hex dump del file GGUF di Llama 3.1 8B con header e metadati](../immagini/aether-gguf.png)

xxd: il file GGUF di Llama 3.1 8B aperto dal terminale. 4.9 GB di matrici quantizzate. Il magic "GGUF" si legge nei primi 4 byte.

GGUF sta per **GPT-Generated Unified Format**. È il formato inventato da Georgi Gerganov per `llama.cpp`, il progetto che ha reso possibile far girare LLM su hardware consumer. Un singolo file, autodescrittivo, che contiene tutto: metadati, vocabolario, pesi. Nessuna dipendenza esterna.

| Campo | Valore | Significato |
| --- | --- | --- |
| `magic` | GGUF | Identificativo formato |
| `version` | 3 | Versione del formato GGUF |
| `tensor_count` | 292 | Matrici di pesi nel modello |
| `general.name` | Meta Llama 3.1 8B Instruct | Modello e variante |
| `general.file_type` | Q4\_K\_M | Quantizzazione a 4 bit (medium) |
| `llama.block_count` | 32 | Numero di layer del transformer |
| `llama.embedding_length` | 4096 | Dimensione dei vettori interni |
| `llama.attention.head_count` | 32 | Teste di attenzione per layer |
| `llama.attention.head_count_kv` | 8 | Teste KV (Grouped-Query Attention) |
| `llama.vocab_size` | 128.256 | Token nel vocabolario |
| `llama.context_length` | 131.072 | Finestra di contesto (128K token) |

I numeri originali del modello sono in **float16** (16 bit per parametro). 8 miliardi di parametri × 2 byte = 16 GB. Non ci stanno nella RAM della maggior parte delle macchine consumer. La soluzione: **quantizzazione**. Q4\_K\_M significa che ogni peso è stato compresso da 16 bit a circa 4.5 bit, con un algoritmo che preserva la precisione dove conta di più (i pesi con magnitudine maggiore). Il risultato: 4.9 GB invece di 16 GB. Corre sul mio Mac con 96 GB di RAM. Perde un po' di qualità, ma non troppa.

$$\text{Dimensione} = \frac{N\_{\text{params}} \times b\_{\text{quant}}}{8} \approx \frac{8 \times 10^9 \times 4.5}{8} \approx 4.5 \text{ GB}$$

Il rapporto: parametri × bit per parametro / 8 = byte su disco

292 tensori. Ogni tensore è una matrice di numeri: pesi delle connessioni, bias, parametri di normalizzazione. Organizzati in 32 layer identici, ognuno con le stesse matrici: `attention.wq`, `attention.wk`, `attention.wv`, `attention.wo`, `feed_forward.w1`, `feed_forward.w2`, `feed_forward.w3`, `attention_norm`, `ffn_norm`. Più il layer di embedding iniziale e quello finale.

![Script Python che calcola le dimensioni dei tensori di Llama 3.1 8B e output con il conteggio parametri](../immagini/tensori.png)

Le ossa del modello: 292 tensori, ~8 miliardi di parametri. Ogni layer ha le stesse 9 matrici, ripetute 32 volte.

**Cosa c'è nel file:** nessuna "conoscenza" in senso umano. Nessun database di fatti. Nessun motore di ricerca interno. Solo 292 matrici di numeri che, moltiplicate nel giusto ordine, trasformano una sequenza di token in ingresso in una distribuzione di probabilità sul token successivo. Tutto il "sapere" del modello è codificato nelle relazioni statistiche tra questi numeri. È per questo che può scrivere che la regina "esce dall'alveare per fondare una nuova colonia" e che le operaie "si addormentano" in inverno nello stesso paragrafo: non ha un concetto di "ape", ha pattern statistici sul testo.

## // Il Mondo a Pezzi

Sezione 03. Tokenizzazione

Il modello non vede lettere. Non vede parole. Vede **token**: pezzi di testo, a volte parole intere, a volte frammenti, a volte s...