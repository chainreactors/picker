---
title: Detection e function hooking
url: https://roccosicilia.com/2026/03/09/detection-e-function-hooking/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-09
fetch_date: 2026-03-10T04:03:47.465460
---

# Detection e function hooking

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Detection e function hooking](https://roccosicilia.com/2026/03/09/detection-e-function-hooking/)

Published by

Rocco Sicilia

on

[9 marzo 2026](https://roccosicilia.com/2026/03/09/detection-e-function-hooking/)

[![Detection e function hooking](https://roccosicilia.com/wp-content/uploads/2025/08/cyber-defense-stile-manga-solo-personaggio-con-barba-e-occhiali.png?w=1024)](https://roccosicilia.com/2026/03/09/detection-e-function-hooking/)

L’introduzione fatta ai [concetti di detection](https://roccosicilia.com/2026/03/01/il-concetto-di-detection-e-il-punto-di-vista-offensivo/) mi serviva per iniziare a discutere del funzionamento degli EDR partendo da una base comune di comprensione dell’architettura. Come ho anticipato questi post hanno lo scopo di discutere anche le possibile tecniche di bypass delle logiche di detection con degli esempi pratici e mi baserò molto sul funzionamento di EDR e SIEM.

Un aspetto che ho citato in diverse occasioni è la capacità degli EDR di mettere a disposizione molta telemetria riguardo a ciò che avviene sugli host. Le informazioni vengono raccolte dai sensori attivi sugli endpoint attraverso diverse funzioni, una di queste è il function hooking: gli EDR moderni si “interpongono” tra i programmi e le chiamate di sistema al fine di intercettare le richieste alle funzioni base del sistema operativo (ho iper-semplificato, ma ora vado un po’ nel dettaglio).

Prendiamo una delle funzioni più monitorate dagli EDR: VirtualAlloc, usata per allocare memoria, operazione comunissima nei payload malevoli.

Un flusso normale (senza EDR) potrebbe essere:

![](https://roccosicilia.com/wp-content/uploads/2026/03/edr_nohooking.png?w=1024)

Il flusso con un EDR attivo potrebbe essere qualcosa di simile:

![](https://roccosicilia.com/wp-content/uploads/2026/03/edr_hooking.png?w=1024)

Quando l’EDR si installa esegue diverse modifiche sul sistema, ad esempio modifica – in memoria – primi byte delle funzioni sensibili in ntdll.dll (la libreria che fa da ponte verso il kernel) sostituendoli con un JMP verso il proprio codice. L’EDR esegue la sua analisi, e se tutto è ok chiama la funzione originale che ha salvato da parte prima di patchare.

Possiamo verificare questa caratteristica degli EDR analizzando il comportamento a runtime di un processo che esegue una *syscall* e la verifica la possiamo fare “in profondità” analizzando il comportamento del processo con un debugger.

#### Lab Test: syscall

Ma quanto utile è avere un lab e tutti gli strumenti per approfondire questi temi! Chi si occupa di ricerca pura sono certo che si diverte come un matto ad eseguire questi test 🙂 nel mio caso di tratta di momenti di studio e ricerca personale che cerco di condividervi e che potete replicare abbastanza facilmente (rif. al tema HomeLab).

Per prima cosa dobbiamo **analizzare il comportamento di un processo su un sistema che non ha un agent EDR installato**. Nel mio lab si tratta della macchina che simula un ambiente desktop Windows 11 che utilizzo anche per la compilazione in ambiente Microsoft.

Nel contesto di laboratorio i sistemi desktop vengono usati, solitamente, con utenti di dominio non privilegiati, ma per il test in questione non è rilevante. Va in ogni caso installato un debugger e per il lab in questione ho deciso di usare IDA Free (v9.3 al momento disponibile, richiede python) che conto di usare anche per altri test che ho in mente di fare. Ovviamente serve anche avere il necessario per compilare un piccolo programma in C, io uso Visual Studio Code sia sul mio laptop che sulla macchina Win11 in questione dove ho anche installato MSYS2 che trovo molto comodo. Voi fate come vi pare 🙂

C’è abbondante documentazione su IDA nel web ma se volete approfittare (come ho fatto il) per un approfondimento sul mondo del *reverse engineering* vi suggerisco un libro per iniziare che mi ha dato qualche base che mi torna ancora utile considerando che io non sono un reverse engineer: “The IDA PRO book” di cui comprai la seconda edizione.

Il codice per il programma di test che dovrà eseguire l’azione di creazione di un file è il seguente:

```
#include <stdio.h>

#include <windows.h>

int main()

{

// test output

printf("Programma di test per creazione di un file");

// crea un file TXT

HANDLE hFile = CreateFileA(

"C:\\\\Users\\\\Public\\\\test.txt",

GENERIC_WRITE,          // scrittura

0,                      // nessuna condivisione

NULL,                   // security attributes default

CREATE_ALWAYS,          // crea sempre, sovrascrive se esiste

FILE_ATTRIBUTE_NORMAL,  // file senza attributi speciali

NULL                    // nessun template

);

if (hFile == INVALID_HANDLE_VALUE) {

printf("Errore creazione file: %d\\n", GetLastError());

return 1;

}

// contenuto del file

const char* contenuto = "test scrittura";

DWORD bytesWritten;

WriteFile(

hFile,

contenuto,

(DWORD)strlen(contenuto),

&bytesWritten,

NULL

);

CloseHandle(hFile);

getchar();

return 0;

}
```

Compilando ed eseguendo questo programma otterremo la creazione di un file nel path “C:\Users\Public\test.txt” e se ne facciamo il debug potremo osservare la chiamata “pulita” alla *syscall* per la creazione del file: 𝑵𝒕𝑪𝒓𝒆𝒂𝒕𝒆𝑭𝒊𝒍𝒆.

Vi risparmio i singoli passaggi che troverete nel video di sintesi, faccio solo presente che per analizzare cosa avviene a livello di *syscall* bisogna eseguire il debug del programma ed andare a “scartabellare” in quello che succede quando vengono chiamate le funzioni di sistema. Ad un certo punto dell’esecuzione si arriva alla chiamata che ci interessa in quanto è una delle chiamate che, in presenza di EDR, verrebbero intercettate.

![](https://roccosicilia.com/wp-content/uploads/2026/03/ida_ntcreatefile_ori.png?w=1024)

Quello che si osserva nel comportamento a runtime è una chiamata alla syscall che utilizza il ***syscall number*** “55” che, per la versione di Windows che stiamo usando, corrispondere esattamente a *NtCreateFile*.

---

Piccolo approfondimento sulle *syscall* per capire questo passaggio.

Quando un’applicazione *userland* deve accedere a risorse gestite dal kernel, come il filesystem, la memoria o i socket di rete, non può farlo direttamente. Il processore lavora in due modalità distinte: user mode (ring 3), dove girano le applicazioni, e kernel mode (ring 0), dove opera il sistema operativo.

Questa separazione è un meccanismo di protezione fondamentale: un processo *userland* non può leggere o scrivere memoria del kernel, né invocare direttamente le sue funzioni. Questa netta separazione in Windows nasce con i sistemi operativi NT ed è stato ciò che ha iniziato a dare stabilità al sistema riducendo drasticamente i BSOD.

Il meccanismo che permette ai due domini di interagire è la *system call*: quando un’applicazione deve eseguire un’operazione privilegiata, carica in un registro dedicato (**eax** su architettura x64 come di vede anche nello screenshot) un numero intero che identifica univocamente l’operazione che si vuole eseguire, poi esegue l’istruzione *syscall*. Il processore salva il contesto corrente, eleva il privilegio a ring 0 e trasferisce il controllo al kernel che **legge il numero in eax per determinare quale operazione eseguire**.

Questo numero, il ***syscall number***, è la chiave del meccanismo. Microsoft non rilascia documentazione ufficiale pubblica sui *syscall number*, inoltre questo numero varia tra versioni del sistema operativo. *NtCreateFile*, ad esempio, ha *syscall number* 0x52 su Windows Ser...