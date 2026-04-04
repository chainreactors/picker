---
title: L’Attacco alla Supply Chain di Axios e il RAT Multipiattaforma di Sapphire Sleet
url: https://blog.lobsec.com/2026/04/analisi-tecnica-attacco-supply-chain-axios-rat/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-03
fetch_date: 2026-04-04T04:17:35.915241
---

# L’Attacco alla Supply Chain di Axios e il RAT Multipiattaforma di Sapphire Sleet

[Vai al contenuto](#content "Vai al contenuto")

[LobSec](https://blog.lobsec.com/)

Layered Offensive Barrier of Security

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)
* [GPG](https://blog.lobsec.com/gpg/)

# L’Attacco alla Supply Chain di Axios e il RAT Multipiattaforma di Sapphire Sleet

2026-04-03 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

Il 31 marzo 2026, l’ecosistema JavaScript ha subito uno degli attacchi alla supply chain più critici della storia recente. `axios`, una delle librerie HTTP client più utilizzate al mondo con circa 100 milioni di download settimanali, è stata compromessa. Un threat actor è riuscito a pubblicare due versioni malevole del pacchetto su npm, distribuendo un Remote Access Trojan (RAT) multipiattaforma progettato per colpire silenziosamente macchine di sviluppo e pipeline CI/CD.

L’attacco, attribuito dalla threat intelligence al gruppo state-sponsored nordcoreano **Sapphire Sleet** (legato al cluster UNC1069), evidenzia un’incredibile sofisticazione nei meccanismi di offuscamento, anti-forensics ed execution.

Ecco l’analisi tecnica approfondita dell’intera kill chain, dai vettori di compromissione iniziale fino alle meccaniche di esecuzione dei payload di Stage-2.

## Vettore di Infezione e Compromissione dell’Account

L’attacco è iniziato con la compromissione dell’account npm di uno dei primary maintainer del progetto (`jasonsaayman`). L’evidenza della compromissione è visibile dai metadati del registry npm:

* Nelle release legittime (es. `1.14.0`), la pubblicazione avveniva tramite **GitHub Actions OIDC** con attestazioni SLSA provenance.
* Nelle versioni compromesse (`1.14.1` taggata come `latest` e `0.30.4` taggata come `legacy`), il metodo di pubblicazione è degradato a un **Direct CLI publish**, e l’email dell’autore è stata modificata in `ifstap@proton[.]me`.

L’attaccante ha colpito in maniera chirurgica, introducendo una singola nuova dipendenza malevola nel `package.json` di Axios: `plain-crypto-js@^4.2.1`. Il codice sorgente di Axios è rimasto intatto, permettendo al pacchetto di mantenere il suo comportamento legittimo per non destare sospetti a runtime.

## Stage 1: Il Dropper “plain-crypto-js” e il postinstall Hook

Il cuore del delivery iniziale si basa sull’abuso dei lifecycle hook di npm. La dipendenza fake `plain-crypto-js` contiene il seguente blocco nel proprio manifest:

```
"scripts": {
  "postinstall": "node setup.js"
}
```

Questo innesca l’esecuzione silente senza alcuna interazione dell’utente durante un banale `npm install axios` o in un aggiornamento automatico generato da bot come Dependabot.

### Offuscamento a Doppio Strato

Il file `setup.js` non espone stringhe in chiaro. Al contrario, adotta uno schema di decodifica a runtime a due layer per mascherare URL del C2, identificatori di piattaforma e percorsi filesystem:

1. **Layer 1:** Inversione della stringa seguita da decodifica Base64.
2. **Layer 2:** Un cifrario XOR utilizzando la chiave hardcodata `OrDeR_7077`, con un indice dipendente dalla posizione basato sulla formula `(7 * i² % 10)`.

### Delivery Selettivo e Mascheramento di Rete

Una volta de-offuscato, il dropper identifica l’architettura tramite `os.platform()` e avvia la fase di fetching effettuando richieste HTTP POST verso l’infrastruttura C2 `hxxp://sfrclak[.]com:8000/6202033` (risolto sull’IP `142.11.206.73`, ospitato su una VPS Hostwinds).

Per eludere l’analisi del traffico egress, il dropper falsifica i body della POST facendoli apparire come telemetria o richieste legittime al registry npm:

* **macOS**: `packages.npm.org/product0`
* **Windows**: `packages.npm.org/product1`
* **Linux**: `packages.npm.org/product2`

### Tecniche Anti-Forensics Avanzate

Immediatamente dopo l’esecuzione, il dropper cancella le sue tracce:

1. **Self-deletion:** Esegue `fs.unlink(__filename)` per eliminare `setup.js`.
2. **Manifest Swapping:** Rinomina uno stub benigno (`package.md` preparato appositamente) in `package.json`, sovrascrivendo la dichiarazione del `postinstall`. Un analista o un tool EDR che ispeziona `node_modules/plain-crypto-js/` post-infezione non troverà alcuna traccia dell’hook malevolo.

## Stage 2: Il RAT Multipiattaforma

Nonostante l’OS target generi payload in tre linguaggi differenti (PowerShell, C++ nativo, Python), le indagini di Elastic Security e Microsoft evidenziano che si tratta di **tre implementazioni dello stesso framework RAT**. Condividono infatti il medesimo protocollo C2 (JSON Base64 su HTTP POST), la stessa cadenza di beaconing (60 secondi), e un set identico di comandi (`kill`, `runscript`, `peinject`, `rundir`).

Un indicatore di compromissione (IoC) estremamente caratteristico è lo spoofing anacronistico dello **User-Agent** hardcodato per tutte le varianti: `mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)` (Internet Explorer 8 su Windows XP). La presenza di questo User-Agent proveniente da sistemi macOS o Linux moderni rappresenta un alert di rilevamento critico.

### Variante macOS (C++ Mach-O)

**Delivery:** Il post-install utilizza un AppleScript (scritto in /tmp ed eseguito silente tramite `nohup osascript`) per scaricare l’eseguibile.

**Payload:** Il file Mach-O viene salvato in `/Library/Caches/com.apple.act.mond`, vengono concessi permessi `chmod 770` e viene lanciato in background tramite `/bin/zsh`.

**Attribuzione:** Reverse engineering del binario ha rivelato significative sovrapposizioni a livello di codice con **WAVESHAPER**, un noto backdoor C++ del cluster nordcoreano UNC1069.

### Variante Windows (PowerShell e VBScript)

**Delivery:** Viene droppato un file `.vbs` temporaneo che avvia una shell `cmd.exe` nascosta. Tramite `curl`, scarica la risposta del C2 in uno script PowerShell transitorio (`%TEMP%\6202033.ps1`).

**Mascheramento:** Il payload individua l’interprete PowerShell nel sistema e lo copia in `%PROGRAMDATA%\wt.exe` per confondersi con Windows Terminal, eseguendo il bypass delle policy di esecuzione (`-ep bypass -w hidden`).

**Persistenza e Capabilities:** È l’unica variante a mantenere persistenza tramite Registry Run key (`HKCU:\Software\Microsoft\Windows\CurrentVersion\Run\MicrosoftUpdate`). Il comando `peinject` del RAT su Windows utilizza il loading riflessivo `.NET` tramite `[System.Reflection.Assembly]::Load()` per eseguire assembly in memoria senza toccare il disco, pur non implementando hook per disabilitare AMSI.

### Variante Linux (Python)

**Delivery:** Una one-liner in shell usa `curl` per scaricare lo stage in `/tmp/ld.py`.

**Esecuzione:** Viene lanciato come processo detached tramite `nohup python3 /tmp/ld.py ... & > /dev/null 2>&1`. Anche in caso di `peinject`, la variante Linux scrive binari temporanei nascosti in directory `/tmp/` ed esegue chiamate a `subprocess.Popen()`.

## Ricognizione Iniziale (Reconnaissance)

All’avvio, ogni RAT genera un UID di 16 caratteri alfanumerici e invia un primo heartbeat (tipo `FirstInfo`) profilando intensamente il sistema. I dati raccolti includono:

* Variabili d’ambiente, Hostname e Username (tramite WMI, `getuid`/`getpwuid`, ecc.).
* System uptime e tempo di boot.
* Enumerazione completa dei processi.
* Snapshot dei contenuti di directory critiche (Documenti, Desktop, Profile).

## Mitigazione, Detection e Incident Response

Un attacco con una superficie esposta potenziale di milioni di host impone una risposta drastica, specialmente in ambienti Enterprise e CI/CD.

### Immediate Action Items

1. **Downgrade ed Eradicazione:** Le uniche versioni sicure adiacenti all’incidente sono `1.14.0` (o patch inferiori) e `0.30.3`. Rimuovere fisicamente `node_modules` e reinstallare usando versioni verificate.
2. **Rotazione dei Secret:** Essendo l’esecuzione avvenuta nel contesto dello sviluppatore o del runner CI/CD, **qualsiasi secret, token AWS/GCP, chiave SSH o variabile d’ambiente esposta deve considerarsi co...