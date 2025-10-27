---
title: LinkedIn e profili falsi
url: https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-30
fetch_date: 2025-10-06T17:46:30.733804
---

# LinkedIn e profili falsi

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [LinkedIn e profili falsi](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/)

Published by

Rocco Sicilia

on

[29 luglio 2024](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/)

[![LinkedIn e profili falsi](https://roccosicilia.com/wp-content/uploads/2024/08/mentoring.png?w=896)](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/)

Sfrutto un recente evento che mi ha interessato per riprende un tema che avevo già trattato in passato da un altro punto di vista: l’utilizzo di account social falsi per ottenere un primo “engage” verso una vittima.

In ambito offensivo la tecnica è ampiamente utilizzata (anche nei team con cui ho lavorato e lavoro viene sfruttata) come estensione della più classica campagna di phishing via email e solitamente lo scopo è guadagnare la fiducia dell’interlocutore al fine di portarlo a compiere un’azione specifica. L’azione dipende dal tipo di attacco che il Red Teamer vuole simulare: potrebbe essere il classico invio di file malevoli come di link che portano a false form di login appositamente crete per raccogliere le credenziali del malcapitat\*.

---

*Nota: ho fatto un breve video update disponibile qui: <https://www.patreon.com/posts/update-sul-tema-109103625>*

---

In passato ero stato contattato da falsi profili LinkedIn che si presentavano come potenziali clienti: nel giro di pochi giorni più utenti con caratteristiche simili mi avevano chiesto il collegamento (che io solitamente accetto salvo specifiche valutazioni, ma questo è un altro tema e non riguardano l’argomento del post) e avevano immediatamente avviato una conversazione professionale. La conversazione virava subito sul tema info sec. e l’interlocutore mi chiedeva se ero disponibile ad attività si *illegal penetration testing*. Ne avevo parlato proprio su LinkedIn per raccontare queste strane conversazioni ed emerse che diverse figure nel mondo cyber italiano erano state contattate con la stessa modalità.

I profili in questione erano, in definitiva, anche poco credibili: giovani donne asiatiche (Cina) con profilo poco curato a livello di dettagli, un centinaio di collegamenti (tutti italiani), nessuna interazione come *post* o *commenti* ad altri post. Tutti elementi che mi avevano insospettito immediatamente e chi mi avevano contemporaneamente incuriosito.

Veniamo ai giorni nostri: luglio 2024. Tre nuovi contatti, uno dopo l’altro, di tre profili LinkedIn strutturalmente identici:

* donna asiatica, questa volta giapponese
* posizione di lavoro in Europa (Londra, Parigi, Madrid)
* profilo molto curato:
  + formazione e posizione lavorativa coerente
  + un migliaio di contatti
  + diverse interazione come commenti generici e repost

In questo caso la conversazione di quello che sembra essere un bot va sempre nella direzione di richiedere di poter parlare tramite un App più comoda, ad esempio Whatsapp. Ho provato a proporre Talegram ma in questo caso, ed in tutti e tre i test, la conversazione si interrompe e dopo poco il profilo rimuove il collegamento.

![](https://roccosicilia.com/wp-content/uploads/2024/07/image.png?w=1024)

Parte di una delle conversazioni.

La mia ipotesi è che questi profili siano dei bot a caccia di interazioni e di numeri di telefono da associare a profili reali. Se avessi un numero da sacrificare proverei ad accettare la conversazione via Whatsapp per vedere in next stage di quello che sembra il preludio di un attacco diretto ad una persona.

Interessante il fatto che il presunto attacker abbia utilizzato tre profili con la stessa dinamica quando è abbastanza ovvio che fallito il primo tentativo diventa poco probabile che la stessa richiesta venga accolta a distanza di poche ore da un altro profilo molto simile al precedente. Molto interessante anche il fatto che, questa volta, i profili erano particolarmente curati, ad una prima occhiata possono sembrare dei profili reali, in particolare la presenza di interazioni.

## Possibili impatti e prevenzione

Come accennavo molto dipende dal modello di attacco che il T.A. sta utilizzando ma non è difficile immaginare cosa potrebbe accadere. Una volta creata la relazione di fiducia e portata la conversazione su uno strumento diretto come Whatsapp, l’attacker potrebbe tentate di far eseguire nuove azioni alla vittima che, se ancora ignara del pericolo, potrebbe trovarsi ad essere il veicolo di un’azione offensiva sulla rete o verso altri membri dell’organizzazione.

Un elemento da considerare è l’incredibile longevità dei profili che ho incontrato, uno dei quali presentava contenuti (commenti nello specifico) datati 2022. Si potrebbe ipotizzare che una certa longevità sia necessaria per rendere il profilo verosimile, diventa quindi utile tracciare questi profili utilizzando una struttura dati standard come STIX al fine di comporre un archivio di IoC da utilizzare negli strumenti di detection o semplicemente per condividere l’informazione.

Come discusso nelle [recenti live dedicate al tema degli IoC](https://www.patreon.com/posts/study-session-12-108112540), anche questi dati vanno validati ed aggiornati nel tempo: questi profili possono sparire (anzi, lo darei per scontato) o essere modificati, non sono da escludere anche degli errori di valutazione da parte degli analisti. Un processo di validazione periodico è assolutamente indispensabile. Lo standard STIX prevede un *type* denominato ***identity*** che potrebbe essere usato proprio allo scopo. Lo standard non prevede in realtà questo specifico utilizzo ma osservando alcuni esempi in cui il *type* in questione è stato utilizzato, con le dovute relazioni, per registrare attività di phishing. Anche in questo caso siano di fronte alla stessa casistica con una differenza rispetto al mezzo: non una email ma un messaggio da un profilo social.

Approfitto del caso in corso per aprire le danze sul [progetto BitIoC](https://github.com/b1th0rn/BitIoC) ed utilizzare i primi dati per creare un primo set di IoC. Il prossimo venerdì è in programma un confronto sul canale [**Discord**](https://discord.gg/Ys5AAbsyyH) del progetto.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/?share=jetpack-whatsapp)

Mi piace Caricamento…

## Una replica a “LinkedIn e profili falsi”

1. ![Avatar Update #5 – Rocco Sicilia](https://roccosicilia.com/wp-content/uploads/2018/09/sheliak.jpg?w=40)

   [Update #5 – Rocco Sicilia](https://roccosicilia.com/2024/08/17/update-5/)

   [17 agosto 2024](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/comment-page-1/#comment-667)

   […] la campagna di phishing tramite LinkedIn ad opera di T.A. che utilizzano profili compromessi (ne parlavo qui), tema che vorrei portare nel progetto […]

   ["Mi piace"](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/?like_comment=667&_wpnonce=eeb0110f49)"Mi piace"

   [Rispondi](https://roccosicilia.com/2024/07/29/linkedin-e-profili-falsi/comment-page-1/?replytocom=667#respond)

### Lascia un commento [Cancel...