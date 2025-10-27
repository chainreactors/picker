---
title: Podcast RSI - Dati personali pubblicati per errore su Internet: tre casi concreti
url: http://attivissimo.blogspot.com/2023/02/podcast-rsi-dati-personali-pubblicati.html
source: Il Disinformatico
date: 2023-02-04
fetch_date: 2025-10-04T05:43:01.370171
---

# Podcast RSI - Dati personali pubblicati per errore su Internet: tre casi concreti

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2023/02/03

### Podcast RSI - Dati personali pubblicati per errore su Internet: tre casi concreti

[![logo del Disinformatico](https://blogger.googleusercontent.com/img/a/AVvXsEgLKyKCnDBWHOWzQyRyIaCUDkpP2fHygIFp5X6KdZBQ_3U4KET1t5s_QY8Bkpdjvp9gYs1s1KbGjT0QUAlu4eIW2PFXmu1Jy-ub_qWnBRiwPLS9uokARrkjYylWMgYeiqi-YzDI7nMCzDMWdQUHhlirE6MtOAFKpr_ocZmCL4EczL0avELuFYg)](https://blogger.googleusercontent.com/img/a/AVvXsEgLKyKCnDBWHOWzQyRyIaCUDkpP2fHygIFp5X6KdZBQ_3U4KET1t5s_QY8Bkpdjvp9gYs1s1KbGjT0QUAlu4eIW2PFXmu1Jy-ub_qWnBRiwPLS9uokARrkjYylWMgYeiqi-YzDI7nMCzDMWdQUHhlirE6MtOAFKpr_ocZmCL4EczL0avELuFYg)

È disponibile subito il podcast di oggi de *Il Disinformatico* della
Radiotelevisione Svizzera, scritto, montato e condotto dal sottoscritto: lo
trovate presso
[www.rsi.ch/ildisinformatico](http://www.rsi.ch/ildisinformatico)
([link diretto](https://rsi-aod-dd.akamaized.net/ww/15989971.mp3?ts=1675369383&fname=Il_Disinformatico_Dati_personali_pubblicati_per_errore_su_Internet_tre_casi_concreti.mp3)) e qui sotto.

Le puntate del *Disinformatico* sono ascoltabili anche tramite
[feed RSS](https://www.rsi.ch/rete-tre/programmi/intrattenimento/il-disinformatico/?f=podcast-xml&type=itunes),
[iTunes](https://podcasts.apple.com/ch/podcast/il-disinformatico/id203842628),
[Google Podcasts](https://podcasts.google.com/feed/aHR0cHM6Ly93d3cucnNpLmNoL3JldGUtdHJlL3Byb2dyYW1taS9pbnRyYXR0ZW5pbWVudG8vaWwtZGlzaW5mb3JtYXRpY28vP2Y9cG9kY2FzdC14bWw)
e
[Spotify](https://open.spotify.com/show/20uK3XvVxdNxFHreEepr8k).

Buon ascolto, e se vi interessano il testo e i link alle
fonti di questa puntata, sono qui sotto.

---

*[CLIP: La richiesta di “password” da* Eyes Wide Shut *di Stanley Kubrick]*

Ci sono tanti modi per scoprire le password e i dati personali di qualcuno.
Spesso i criminali informatici vengono immaginati e rappresentati come maghi
della tastiera che sanno scovare e rubare qualunque dato digitale usando
tecniche di penetrazione sofisticatissime, ma altrettanto spesso queste
tecniche non sono affatto necessarie, perché i dati sono stati messi
maldestramente a disposizione del primo che passa e sono accessibili via
Internet a chiunque abbia una minima capacità informatica. La colpa, insomma,
non è del titolare dei dati, ma di chi è tenuto a custodire i dati degli
altri.

Sono Paolo Attivissimo, e in questa puntata del *Disinformatico*, il
podcast della Radiotelevisione Svizzera dedicato alle notizie e alle storie
strane dell’informatica, vi racconto tre episodi recentissimi di dati
personali trovati a spasso su Internet, le tecniche usate per trovarli, e le
trappole usate dai criminali informatici per sfruttare quei dati, partendo da
informazioni banali come un’ordinazione di caffé. Due di queste storie hanno
un lieto fine: la terza, almeno per ora, ha un finale aperto.

*[SIGLA di apertura]*

### Assicurati poco rassicuranti

Pochi giorni fa mi è arrivata in via confidenziale la segnalazione di un sito
aperto a chiunque che contiene quello che sembra essere un elenco di dati
assicurativi di clienti italiani, probabilmente della zona di Chieti. Nomi,
cognomi, indirizzi, codici fiscali, dettagli delle polizze assicurative, e
altro ancora, tutto tranquillamente sfogliabile e leggibile con un normale
browser. Tutto quello che serve sapere per leggerli è l’indirizzo IP del sito.

Trovare questo indirizzo IP non è difficile. Esistono motori di ricerca
appositi, come Shodan, che in sostanza fanno la stessa cosa che fa Google,
ossia esplorano e catalogano tutta Internet, ma a differenza di Google, che
rastrella tutti i testi e tutte le immagini, questi motori di ricerca prendono
nota solo dei siti che hanno degli accessi non protetti. È sufficiente
sfogliare Shodan per trovare di tutto: telecamere di sorveglianza accessibili,
server leggibili e scrivibili da chiunque, e pagine Web come quella che mi è
stata segnalata. Esattamente come con Google, è sufficiente immettere le
parole chiave giuste, facilmente intuibili: nomi di marche famose di
telecamere o di apparati di controllo industriale oppure frasi descrittive
tipiche degli archivi di dati online. E a volte queste stesse parole chiave
sono usabili direttamente in Google, senza neppure dover ricorrere a motori di
ricerca specializzati.

Fra l’altro, la facilità con la quale questi dati assicurativi teoricamente
privati sono reperibili è dimostrata nella maniera più evidente da una riga
molto particolare dell’elenco dei clienti di questo servizio assicurativo. Al
posto del nome e cognome del cliente, in questa riga c’è una vistosa dicitura,
tutta in maiuscolo: *“BUONGIORNO QUESTO DATABASE È ACCESSIBILE A CHIUNQUE VIA
INTERNET”*.

Chiaramente qualcuno è già passato di qui, ha notato i dati personali
pubblicamente accessibili, e ha scelto un modo molto diretto per avvisare i
responsabili del sito.

La presenza di questo avviso, inoltre, segnala altrettanto chiaramente che i
dati non sono soltanto leggibili, ma sono anche scrivibili da chiunque via
Internet. Questo vuol dire che chiunque può alterarli o semplicemente
cancellarli. Un avviso del genere è l’equivalente informatico di trovare un
volantino di una società di installazione di antifurto *dentro casa,* sul
tavolo in cucina.

Non è una bella situazione, soprattutto per gli assicurati elencati, e così
sono andato a frugare pazientemente nei dati e nei documenti pubblicamente
accessibili, vi ho trovato l’indirizzo di mail di quella che sembra essere la
ditta responsabile e l’ho avvisata della situazione.

Nel giro di poche ore le pagine sono state disattivate, non so se per merito
dell’avviso lasciato nei dati stessi oppure della mia segnalazione via mail.
Quei dati sono ancora reperibili in Google, che ne conserva temporaneamente
memoria nella sua cache, ma perlomeno non sono più alterabili da qualunque
malintenzionato in vena di dispetti.

Mi è poi arrivato su Telegram un messaggio di qualcuno che sembra parlare a
nome della ditta coinvolta e dice che si trattava di “una versione alfa non in
produzione” che conteneva “dati totalmente fittizi anche se costruiti
coerentemente”. Non ho modo di verificare questa dichiarazione: posso solo
notare che erano “costruiti coerentemente” con un realismo e un dettaglio
davvero straordinari per essere dei dati fittizi, e posso solo sperare che la
versione definitiva sarà un po’ meno accessibile e disinvoltamente scrivibile
di questa, perché in ogni caso provare un database lasciandolo aperto a tutti
su Internet, in modo che possa essere riscritto, cancellato o devastato dal
primo vandalo che passa, non è comunque una buona prassi di sicurezza
informatica. E non è l’unica prassi del suo genere che viene disattesa, come
vi racconterò tra un attimo.

*Screenshot e dettagli:
<https://attivissimo.blogspot.com/2023/01/poi-la-gente-si-chiede-come-mai-i-dati.html>*

### Dati sanitari lombardi a spasso

Non si capisce se sia incoscienza, disinvoltura o ignoranza, ma è
impressionante la quantità di organizzazioni che mette su alla bell’e meglio
una pagina Web con i dati personali dei dipendenti, clienti o collaboratori
“*perché così è comodo e possiamo consultarli facilmente”*.

Vero, è comodo, ma altrettanto facilmente può consultarli anche chiunque
altro. A quanto pare non è ancora stata capita diffusamente la lezione
fondamentale che non basta non dire a nessuno dove si trovano i dati e così
nessuno li troverà: bisogna proteggerli *attivamente,* così come non
basta lasciare la chiave di casa sotto lo zerbino e sperare che nessuno la
trovi.

I motori di ricerca ...