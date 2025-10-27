---
title: La Prototype Pollution
url: https://www.ictsecuritymagazine.com/articoli/la-prototype-pollution/
source: ICT Security Magazine
date: 2023-03-22
fetch_date: 2025-10-04T10:17:34.079044
---

# La Prototype Pollution

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![](https://www.ictsecuritymagazine.com/wp-content/uploads/javascript-prototype-pollution.jpg)

# La Prototype Pollution

A cura di:[Damiano Capo](#molongui-disabled-link)  Ore 21 Marzo 2023

Tra le innumerevoli vulnerabilità che affliggono i siti web, ve ne sono alcune che si manifestano di rado, tuttavia, non sono da sottovalutare, poiché possono arrecare danni incalcolabili agli applicativi. Una di queste è sicuramente la Prototype Pollution.

Prima di addentrarci nella trattazione della vulnerabilità vera e propria, è necessario comprendere alcuni concetti di JavaScript.

JavaScript utilizza un modello di ereditarietà prototipale diverso dal modello basato sulle classi adoperato dagli altri linguaggi.

### Che cos’è un oggetto in JavaScript?

Un oggetto JavaScript è essenzialmente un insieme di coppie chiave:valore, note come “proprietà”. Ad esempio, il seguente oggetto potrebbe rappresentare un utente:

```
const user = {
   username: "mario_rossi",
   userId: 123456789,
   isAdmin: false
}
```

È possibile accedere alle proprietà di un oggetto utilizzando i punti oppure le parentesi quadre, per fare riferimento alle rispettive chiavi:

```
user.username     // "mario_rossi"
user['userId']   // 123456789
```

Oltre ai dati, le proprietà possono contenere anche funzioni eseguibili. In questo caso, la funzione è nota come “metodo”.

```
const user = {
   username: "mario_rossi",
   userId: 123456789,
   exampleMethod: function(){
      // do something
   }
}
```

L’esempio precedente è un “letterale di oggetto”, il che significa che è stato creato usando la sintassi delle parentesi graffe per dichiarare esplicitamente le sue proprietà e i loro valori iniziali. Tuttavia, è importante capire che quasi tutto in JavaScript è un oggetto. In questo elaborato, il termine “oggetto” si riferisce a tutte le entità, non solo agli oggetti letterali.

### Che cos’è un prototype in JavaScript?

Ogni oggetto in JavaScript è collegato a un altro oggetto di qualche tipo, noto come prototype. Per impostazione predefinita, JavaScript assegna automaticamente ai nuovi oggetti uno dei suoi prototype incorporati.

Ad esempio, alle stringhe viene automaticamente assegnato il prototipo incorporato String.prototype. Di seguito sono riportati alcuni esempi di questi prototype globali:

```
let myObject = {};
Object.getPrototypeOf(myObject);   // Object.prototype
let myString = "";
Object.getPrototypeOf(myString);   // String.prototype
let myArray = [];
Object.getPrototypeOf(myArray);    // Array.prototype
let myNumber = 1;
Object.getPrototypeOf(myNumber);   // Number.prototype
```

Gli oggetti ereditano automaticamente tutte le proprietà del prototype assegnato, a meno che non abbiano già una proprietà propria con la stessa chiave. Ciò consente agli sviluppatori di creare nuovi oggetti che possono riutilizzare le proprietà e i metodi degli oggetti esistenti.

I prototype incorporati forniscono proprietà e metodi utili per lavorare con i tipi di dati di base.

Ad esempio, l’oggetto String.prototype ha un metodo toLowerCase(). Di conseguenza, tutte le stringhe hanno automaticamente un metodo pronto all’uso per convertirle in minuscolo. Questo evita agli sviluppatori di dover aggiungere manualmente questo comportamento a ogni nuova stringa creata.

### Come funziona l’ereditarietà degli oggetti in JavaScript?

Ogni volta che si fa riferimento a una proprietà di un oggetto, il motore JavaScript cerca innanzitutto di accedervi direttamente sull’oggetto stesso. Se l’oggetto non ha una proprietà corrispondente, il motore JavaScript la cerca invece nel prototype dell’oggetto. Dati i seguenti oggetti, ciò consente di fare riferimento a myObject.propertyA, ad esempio:

![](https://www.ictsecuritymagazine.com/wp-content/uploads/WINWORD_wc5JADxnr5.png)

È possibile utilizzare la console del browser per osservare questo comportamento in azione. Per prima cosa, è necessario creare un oggetto completamente vuoto:

```
let myObject = {};
```

Quindi, si digiti myObject seguito da un punto. Si noti che la console chiede di selezionare da un elenco di proprietà e metodi:

![](https://www.ictsecuritymagazine.com/wp-content/uploads/metodi-oggetto-javascript-700x355.png)

Anche se non ci sono proprietà o metodi definiti per l’oggetto stesso, ne ha ereditati alcuni dal built-in Object.prototype.

Si noti che il prototype di un oggetto non è altro che un altro oggetto, che dovrebbe avere anch’esso il suo prototype, e così via. Dal momento che praticamente tutto in JavaScript è un oggetto, questa catena riporta al livello superiore Object.prototype, il cui prototype è semplicemente null.

### ![](https://www.ictsecuritymagazine.com/wp-content/uploads/WINWORD_Pe1OSbRIMP-700x450.png)

È fondamentale che gli oggetti ereditino le proprietà non solo dal loro prototype immediato, ma anche da tutti gli oggetti che li precedono nella catena dei prototype. Nell’esempio precedente, ciò significa che l’oggetto nomeutente ha accesso alle proprietà e ai metodi di String.prototype e Object.prototype.

### Accedere al prototype di un oggetto usando \_\_proto\_\_

Ogni oggetto ha una proprietà speciale che può essere usata per accedere al suo prototype. Sebbene non abbia un nome formalmente standardizzato, \_\_proto\_\_ è lo standard de facto utilizzat...