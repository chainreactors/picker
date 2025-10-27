---
title: Un PDF interattivo pericoloso!
url: https://hackerjournal.it/11103/un-pdf-interattivo/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-08
fetch_date: 2025-10-04T03:19:53.337810
---

# Un PDF interattivo pericoloso!

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

Connect with us

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnew-1.png)](https://hackerjournal.it/)
[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

## Hackerjournal.it

#### Un PDF interattivo pericoloso!

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/coppadelmondo-400x240.png)

    Mondiali 2026: la truffa corre sul Web](https://hackerjournal.it/14527/mondiali-2026-la-truffa-corre-sul-web/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/massive_npm-400x240.png)

    Il virus che “ruba” il codice](https://hackerjournal.it/14522/il-virus-che-ruba-il-codice/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/stellarium-400x240.jpg)

    Il malware che spia chi visita siti porno](https://hackerjournal.it/14518/il-malware-che-spia-chi-visita-siti-porno/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/kaspesky_corso-400x240.png)

    Un corso online per difendere gli LLM](https://hackerjournal.it/14504/un-corso-online-per-difendere-gli-llm/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/truffa_iphone-400x240.png)

    Truffe online dell’iPhone 17](https://hackerjournal.it/14495/truffe-online-delliphone-17/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/deepin_home-400x240.png)

    Linux incontra il design](https://hackerjournal.it/14508/linux-incontra-il-design/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/concetto-di-gestione-delle-relazioni-con-i-clienti-400x240.jpg)

    L’arte di ascoltare le reti](https://hackerjournal.it/14474/larte-di-ascoltare-le-reti/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/04/attacchi-cibenetici-400x240.jpg)

    Attacchi ai servizi di rete](https://hackerjournal.it/14439/attacchi-ai-servizi-di-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/persona-che-scrive-su-un-primo-piano-del-computer-portatile-400x240.jpg)

    Enumerazione: la vera identità della rete](https://hackerjournal.it/14421/enumerazione-la-vera-identita-della-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/codice-binario-con-globo-sul-computer-portatile-400x240.jpg)

    I migliori tool per la scansione di rete](https://hackerjournal.it/14410/i-migliori-tool-per-la-scansione-di-rete/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

### [Articoli](https://hackerjournal.it/category/tech/)

# Un PDF interattivo pericoloso!

La funzionalità che consente di inserire JavaScript in un PDF, per automatizzare i form, è implementata con un bug in Adobe Reader, che può portare a una esecuzione remota di codice

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

7 Gennaio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2023/01/javascript-api.png)

* Share
* Tweet

Il **[bug](https://hackerjournal.it/encyclopedia/bug/)** a cui facciamo riferimento in questo articolo appartiene a uno dei programmi più diffusi sui PC (soprattutto quelli dotati di Windows) di tutto il mondo: **Adobe Reader**. Quando un utente scarica un PDF, c’è buona probabilità che lo apra automaticamente con questo programma. Per capire meglio come funziona, bisogna capire come funzionano i PDF. Il loro “progenitore”, il formato **PostScript**, è una sorta di linguaggio di programmazione vero e proprio, che contiene le istruzioni per la stampa. Queste istruzioni devono poi essere interpretate dalle stampanti (e dai programmi che visualizzano l’anteprima). Un po’ come un programma in **Python**. Invece, i PDF sono una sorta di versione già compilata, come un programma binario. Ciò non toglie che debbano essere “interpretati” per poterli visualizzare sullo schermo, ma con la differenza che l’interpretazione parte proprio da un binario. È più simile a una emulazione, come quando si usa una macchina virtuale per far girare un programma scritto per una architettura diversa da quella nativa del processore del proprio PC.

[![](https://hackerjournal.it/wp-content/uploads/2023/01/deassembly-1024x525.png)](https://hackerjournal.it/wp-content/uploads/2023/01/deassembly.png)

##### *[figura #1] – Il codice di Adobe Acrobat Reader non è pubblico, ma con un debugger è possibile vedere le porzioni in cui l’indirizzo di memoria viene liberato e nonostante questo il programma continua a usarlo (FONTE: <https://zscaler.com>)*

### Il cuore del problema

Nel corso degli anni il formato PDF è diventato uno standard indiscusso, ma gli utilizzi dell’informatica sono cambiati negli ultimi 30 anni, e da un po’ di tempo i PDF hanno iniziato a supportare i **form**, per consentire una semplice compilazione dei moduli. Non soltanto: hanno anche iniziato a supportare **JavaScript** (<https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/pdfs/acrobatsdk_jsapiref.pdf>) per automatizzare la gestione dei form stessi. Ed è qui che si annida il problema: se un PDF di per sé non contiene del codice da interpretare o eseguire, il codice JavaScript deve essere eseguito, e questo può dare spazio di manovra a qualche malintenzionato. Nel caso specifico, Adobe ha sviluppato alcune apposite **API** che permettono al codice JavaScript di accedere a determinate parti della pagina. Per esempio, la funzione **print** stampa un subset di pagine del documento PDF. Questa funzione ha una serie di parametri opzionali: **nStart** e **nEnd** indicano il numero di inizio e fine del range di pagine da stampare, **bShrinkToFit** indica se sia necessario ridimensionare le pagine per adattarle all’area di stampa, eccetera. In particolare, da Acrobat 6 in poi i vari parametri sono supportati per retrocompatibilità, ma è disponibile un nuovo elemento: **printParams**. Questo oggetto dovrebbe contenere tutte le impostazioni necessarie per la stampa e se è specificato tutti gli altri parametri vengono ignorati. Questa comodità prevista da Adobe, che in teoria facilita queste attività perché si può creare l’oggetto con le preferenze di stampa una volta sola e poi usarlo quando si vuole, ha in realtà un problema di implementazione. L’oggetto **printParams** viene infatti utilizzato senza prima verificare che contenga qualcosa di legittimo. Quindi per un malintenzionato è possibile creare un PDF che contenga questo codice:

*/OpenAction <<
/JS (
fthis = this;
try {
uAnwU19 = new Object(unescape(‘%EA7%DF’));
} catch(e) {};
try {
fthis.print({
bUI: true,
nStart: 1,
nEnd: 2,
bSilent: true,
bPrintAsImage: true,
bReverse: true,
bAnnotations: true,
printParams: uAnwU19
});
} catch(e) {};
fthis.resetForm();)
/S /JavaScript
>>*

L’interprete **JavaScript** di Adobe Reader eseguirà la funzione **print**, ignorando i vari parametri legittimi, e...