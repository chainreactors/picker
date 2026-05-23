---
title: Giochiamo insieme #1
url: https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/
source: Over Security
date: 2026-05-22
fetch_date: 2026-05-23T05:42:30.047022
---

# Giochiamo insieme #1

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Giochiamo insieme #1](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/)

Published by

Rocco Sicilia

on

[22 Maggio 2026](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/)

[![Giochiamo insieme #1](https://roccosicilia.com/wp-content/uploads/2025/01/cybersecurity-test-serie.png)](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/)

### Premessa

Ho pensato di proporre, su LinkedIn, delle piccole challenge dedicate alla sicurezza offensiva: semplici scenari di attacco che prendo dal mondo vero (cose che a tutti i PenTester sono successe).

Ho decisi di proporre questo “gioco” su LinkedIn perché i contenuti della piattaforma stanno letteralmente *[andando a ramengo](https://www.treccani.it/vocabolario/ramengo/)*, per usare un’espressione popolare. Come ho recentemente raccontato sono molto legalo all’espressione scritta, altrimenti non avrei un blog, e LinkedIn per un periodo è stata un’eccellente piattaforma per discutere e confrontarsi. Purtroppo la situazione è molto cambiata ma non voglio restare passivo e nel mio piccolo continuerò a proporre contenuti. Ora veniamo al tema del post.

### Introduzione allo scenario

[![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/05/image-3.png?resize=1000%2C744&ssl=1)](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7462779608250286080/)

Post originale

**Se vuoi provare a rogionare sullo scenario in autonomia fallo prima di proseguire nella lettura.**

Si tratta di una situazione molto classica di cui anche nei corsi di Penetration Testing si trovano diverse varianti. Non è raro che sui sistemi server e client di una rete siano attive operazioni pianificate o script eseguiti tramite determinate policies. Quando si tratta di operazioni di manutenzione può capitare che l’utente con cui queste operazioni vengano eseguite sia privilegiano, forse non sempre SYSTEM (si spera) ma spesso è un utente con dei privilegi più alti rispetto ai “normali” utenti della rete.

Se lo script che viene eseguito sulla macchina è in qualche misura accessibile e/o modificabile ci troviamo nella situazione di poter eseguire comandi privilegiato sull’host su cui quello script è attivo. Questa ipotesi va ovviamente verificata e poi sfruttata considerando che l’accesso al sistema non è diretto ma è veicolato dallo strumento che abbiamo utilizzato per prendere possesso della sessione dell’utente sulla macchina target. Quindi se l’attaccante ha accesso diretto al sistema (manu sulla tastiera con una sessione locale) si possono fare delle cose, se l’attaccante opera da remoto grazie ad un primo accesso non privilegiato (reverse shell è C2) si possono comunque eseguire diverse azioni nei limiti della shell che, nel mondo MS Windows, sarà un prompt di DOS o Powershell.

In questo post analizziamo la seconda opzione, statisticamente più probabile rispetto alla prima, e ragioniamo sulle azioni che un’attaccante potrebbe intraprendere con un’accesso tramite una reverse shell classica.

### Verifica delle ipotesi

Come detto per prima cosa dobbiamo accertarci del livello di accesso alla risorsa: per poter valutare una modifica dobbiamo verificare che path e file siano accessibili in lettura e scrittura. Considerando che, in relazione alla nostra ipotesi di partenza, stiamo lavorando da una *reverse shell* dobbiamo poterlo fare con dei comandi da CLI.

![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/05/image-4.png?resize=1024%2C306&ssl=1)

L’utility *icacls* è quella da manuale in queste situazioni e può essere usata anche per una risorsa remota come un file condiviso tramite network share. In questo caso quello che ci interessa è che l’utente che abbiamo compromesso (*rocco* nell’esempio del mio LAB) a accesso ***(I)(F)*** al file dove “F” sta per “Full Control”: possiamo sicuramente modificare il file in oggetto.

Aggiungiamoci un po’ di elementi dal mondo vero: non possiamo semplicemente sostituire il file in quanto andremmo a compromettere una procedura implementata quasi certamente dal team IT del target e “disattivarla” potrebbe generare sospetti o allarmi sul sistema di monitoraggio.

### Abuso del livello di accesso alla risorsa

Arriviamo al punto: possiamo modificare lo script ed assicurarci l’esecuzione di comandi powershell con i privilegi di SYSTEM e ovviamente le possibili strade sono tante. Riprendendo alcuni dei commenti nel post una delle opzioni è sicuramente aprirsi una comoda e nuove reverse shell con privilegi elevati e da quella indubbiamente comoda posizione possiamo fare diverse cose.

Restando sulla challenge e considerando che dobbiamo sicuramente fare i conti con i sistemi di detection a mio avviso la prima preoccupazione è relativa alle possibilità di compromissione o disturbo dei sistemi di difesa e lo farei prima di aprire una nuova *reverse shell*.

![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/05/image-5.png?resize=900%2C221&ssl=1)

Al netto delle nostre valutazioni su come procedere nell’attività, lo script lo dobbiamo modificare senza comprometterne il funzionamento e la cosa più logica, solitamente, è aggiungere in coda le operazioni che vogliamo eseguire tramite l’automatismo.

```
PS C:\Users\sheliak\Coding\Temp> Add-Content .\test.ps1 @'
>> Write-Host "Elemento aggiunto"
>> Get-Date
>> '@
```

Va però tenuto in considerazione che probabilmente dovremo utilizzare comandi eseguibili in una unica riga:

```
Add-Content .\test.ps1 "Write-Host `"Elemento aggiunto`"`r`nGet-Date"
```

Operare attraverso una *reverse shell* o attraverso un C2 non consente sempre di emulare tutte le funzionalità di una vera shell e visto che il rischio è perdere la sessione è sempre necessario fare attenzione ai comandi che si decide di impartire.

### Prossimi step?

Come accennato una volta che abbiamo capito come utilizzare lo script i prossimi step dipenderanno dalla strategia che si vorrà adottare e lo approfittiamo nelle prossime challenge se questo metodo di condivisione vi piace e lo trovate utile.

Secondo la mia esperienza è opportuno valutare come ridurre la capacità di detection del sistema prima di fare ulteriore rumore anche considerando che tutto quello che faremo eseguire allo script verrà associato ad una procedura che probabilmente gira da tempo, cosa che ci permette di restare molto ben nascosti. Se dovessi riuscire in questa prima azione molto probabilmente eseguirei una escalation dei privilegi locale modificando l’utente di dominio in modo da farlo diventare Local Administrator. Non è la scelta più silenziosa ma è quella che potrebbe restituire una maggiore efficienza nei prossimi step.

---

Se questi contenuti ti piacciono seguimi anche su [YouTure](https://youtube.com/%40roccosicilia) ed inscriviti al mio [Substack](https://roccosicilia.substack.com/subscribe):

[![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/05/image.png?resize=1600%2C404&ssl=1)](https://roccosicilia.substack.com/subscribe)

### Condividi:

* Invia un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Condividi su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/?share=linkedin)
* [Condividi su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/?share=telegram)
* [Condividi su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/?share=jetpack-whatsapp)

### Mi piace:

Mi piace Caricamento in corso…

### Rispondi[Annulla risposta](/2026/05/22/giochi...