---
title: GIT-SHELL: p-o-c v0.1
url: https://roccosicilia.com/2023/01/13/git-shell-p-o-c-v0-1/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-14
fetch_date: 2025-10-04T03:54:50.457479
---

# GIT-SHELL: p-o-c v0.1

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [GIT-SHELL: p-o-c v0.1](https://roccosicilia.com/2023/01/13/git-shell-p-o-c-v0-1/)

Published by

Rocco Sicilia

on

[13 gennaio 2023](https://roccosicilia.com/2023/01/13/git-shell-p-o-c-v0-1/)

[![GIT-SHELL: p-o-c v0.1](https://roccosicilia.com/wp-content/uploads/2023/01/image-22.png?w=950)](https://roccosicilia.com/2023/01/13/git-shell-p-o-c-v0-1/)

Tempo fa mi ero imbattuto in un post su medium in cui si discuteva dell’utilizzo di git per gestire una reverse shell. Non è un tema nuovo, ho visto diverse presentazioni in vari eventi in cui sono state mostrate le potenzialità della tecnica che trovo interessante per diversi fattori tra cui:

* la possibilità di utilizzare come “base” una piattaforma considerata affidabile come un servizio di versioning in cloud
* la possibilità di utilizzare comodamente SSH o HTTPS come protocollo di comunicazione
* la versatilità dello strumento in se (git)

Ho rispolverato l’argomento in questi giorni (attività in corso con il red team) ed ho approfittato per costruire un piccolo prototipo che sfrutti le funzionalità di git con qualche accorgimento in più. Di seguito il funzionamento del mio proof of concept ed il codice utilizzato in questa primissima versione dimostrativa.

## Come funziona

Il processo è molto semplice, partiamo dal contesto. Si tratta a tutti gli effetti di una reverse shell, siamo quindi in una fase di post-exploitation in cui abbiamo ottenuto un accesso ad un sistema o abbiamo modo di interagire. E’ inoltre necessario, almeno in questa versione del tool, che git sia presente sul sistema target salvo poterlo installare senza destare sospetti.

Sfruttando una qualsiasi funzionalità che consenta ti eseguire ad intervalli uno script facciamo in modo di eseguire il seguente processo:

* creiamo/aggiorniamo la repo locale del progetto
* verifichiamo il contenuto dell’ultimo commit message
* se contiene una stringa che corrisponde ad un comando bash, eseguiamo il comando sul sistema
* ridirigiamo l’output del comando in un file di testo che fa parte della repo (es: output.txt)
* eseguiamo il commit delle modifiche ed aggiorniamo la repo remota

L’unica differenza di sostanza con altre git-shell sta nel fatto che i comandi vengono solitamente posizionati encoded in un file che fa parte dalla repo. In questa versione ho utilizzato il campo dedicato ai messaggi delle commit per inviate i comandi alla shell mentre per ricevere gli output ho mantenuto il metodo classico.

Come risultato finale per dialogare con il sistema basta eseguire una commit sulla repo ed aspettare l’aggiornamento del file “output.txt” con la risposta.

## Demo

Una piccola dimostrazione pratica per vedere gli step e le modalità di lavoro della versione 0.1 che rilascio solo a fini dimostrativi per ambienti unix-like. Seguiranno probabilmente integrazione per altri ambienti.

Per prima cosa è ovviamente necessario clonare la repo sulla macchina target:

```
$ git clone https://github.com/roccosicilia/sToolz
```

Il progetto è una collezione di piccoli tools, in questa occasione ci interessa solo il contenuto della directory RedTeam/C2demo/ dove troverete diversi file tra cui:

* il file git-demo.sh con lo script da tenere in esecuzione sulla macchina target
* il file git-output.txt dove verranno scritti gli output dei comandi alla shell

Nota sugli altri file: fanno parte di altre versioni della p-o-c ancora in sviluppo, la metodologia è la stessa ma i canali utilizzati sono differenti.

Usando una tecnica a vostro piacimento è necessario far girare periodicamente lo script git-demo.sh:

![](https://roccosicilia.com/wp-content/uploads/2023/01/image-16.png?w=666)

Lo script si occupa semplicemente di aggiornare la repo locale e verificare l’ultimo messaggio di commit: se il messaggio è NOP lo script non esegue azioni e procede con la prossima iterazione, in caso contrario legge il contenuto dell’ultimo commit e lo utilizza come comando da inviare al sistema locale. L’output del comando viene così inviato al file git-output.txt su cui si esegue la commit e la push verso la repo remota.

A questo punto è sufficiente eseguire una qualsiasi modifica ad uno dei file della repo (es: README) mettendo nel messaggio il comando da eseguire.

![](https://roccosicilia.com/wp-content/uploads/2023/01/image-12.png?w=1024)

l’esempio più idiota che mi è venuto in mente

L’output del comando verrà quindi salvato all’interno del file git-output.txt e sincronizzato con la repository del progetto su GitHub o su altri repo Git di vostro gradimento.

## Utilizzo in un contesto reale

Ripercorriamo assieme gli step usando solo la cli sia lato “attacker” (a sinistra) che lato target (a destra), tenendo in considerazione che questa versione dimostrativa non è dotata di una interfaccia utente che possa agevolare qualche comando.

![](https://roccosicilia.com/wp-content/uploads/2023/01/image-18.png?w=950)

In arancione sono evidenziali i due file che compongono la versione 0.1 della git-shell, mentre nel riquadro azzurro il comando che avvia il loop sulla macchina target. Non essendoci stati change sulla repo remota lo script in loop restituisce il messaggio che indica che non ci sono azioni da eseguire (NOP).

![](https://roccosicilia.com/wp-content/uploads/2023/01/image-19.png?w=948)

Mentre sul sistema target è in esecuzione lo script, sul sistema locale modifichiamo uno dei file della repo (in questo caso il README.md. Come previsto con un *git status* possiamo visualizzare la modifica in accesa di commit.

![](https://roccosicilia.com/wp-content/uploads/2023/01/image-21.png?w=946)

commit

Una volta modificato il file possiamo eseguirne l’add e poi il commit (nell’esempio stiamo ancora usando la mia repository di test). Nell’esecuzione del commit, sottolineato in verde, vi è un comando specifico: per evitare problemi nell’utilizzo della stringa da utilizzare come comando sul sistema target si è adottata una forma che consenta di evitare gli spazi come carattere separatore.

Ora è sufficiente eseguire la push delle modifiche sulla repo ed attendere che il sistema remoto aggiorni la propria repository. In caso l’aggiornamento vada a buon fine dovremmo poter osservare la sincronizzazione delle repo:

![](https://roccosicilia.com/wp-content/uploads/2023/01/image-22.png?w=950)

A questo punto lo script avrà eseguito il comando passato tramite messaggio (df -kh) e scritto l’output sul file git-output.txt. Per accedere al contenuto sarà sufficiente aggiornare la repo sulla macchina locale leggere il contenuto del file:

![](https://roccosicilia.com/wp-content/uploads/2023/01/image-24.png?w=939)

l’output del comando “df -kh”

## Qualche riflessione

Come sicuramente in molti avranno avuto modo di sperimentare l’utilizzo dei blasonati tools di Penetration Testing viene spesso limitato dal fatto che i sistemi di sicurezza ne conoscono bene il comportamento e sono spesso in grado di bloccare specifiche azioni. L’esigenza di creare componenti “originali” per le suite più note o piccoli strumenti from scratch credo si manifesterà sempre più frequentemente.

Le reverse shell sono strumenti potenti e se ben pensate sono difficili da individuare. L’esempio presentato in questo breve post difficilmente potrebbe essere rilevato se non grazie a sistemi di controllo in grado di correlare l’azione in se (dei comandi git e del traffico https) ad un comportamento anomalo come l’intervallo regolare degli update o il fatto che la rete target non ha familiarità con gli host di atterraggio delle sessioni. Tecnica ancor più insidiosa se la si veicol...