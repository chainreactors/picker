---
title: Di Codemotion e tanto altro
url: https://codiceinsicuro.it/blog/di-codemotion-e-tanto-altro/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-29
fetch_date: 2025-10-30T03:12:14.963843
---

# Di Codemotion e tanto altro

[![Codice Insicuro](https://codiceinsicuro.it/assets/images/logo.png)](https://codiceinsicuro.it/)

* [Blog](https://codiceinsicuro.it/index.html)
* [About](https://codiceinsicuro.it/about)
* [Chi sono](https://codiceinsicuro.it/chi-sono/)
* [Talks](https://codiceinsicuro.it/talks/)
* [Contatti](https://codiceinsicuro.it/contatti)

Share

##### Iscriviti alla mailing list

Basta la tua email

![Paolo Perego](https://www.gravatar.com/avatar/d05560cd673cf2f4114012616fd57c33?s=250&d=mm&r=x)

[Paolo Perego](https://codiceinsicuro.it)[Follow](https://twitter.com/thesp0nge)
Specialista di sicurezza applicativa e certificato OSCE e OSCP, amo spaccare e ricostruire il codice in maniera sicura. Sono cintura nera di taekwon-do, marito e papà. Ranger Caotico Neutrale, scrivo su @codiceinsicuro.

# Di Codemotion e tanto altro

![Di Codemotion e tanto altro](data:image/png;base64...)

1497
parole -  Lo leggerai in 8 minuti

---

Il mio autunno è iniziato con una grossa novità in famiglia. Grace, un cucciolo
di Beagle che ha portato un po’ di scompiglio nelle nostre vite.

![La mia cucciola Grace](http://localhost:4000/assets/images/grace.jpg)

Dicono tutti che un cucciolo impegni tanto quanto un neonato e che i Beagle
siano, tra le razze, quelle più impegnative. Ecco, verissimo in entrambi i casi.

Settembre e i ricordi dell’estate, se ne sono andati con quell’aria melanconica
descritta nel finale del film Sapore di Mare e parimenti, tutte le mie energie
sono state indirizzate a costruire una nuova routine con Grace. Aspetto molto
positivo: la mia media passi è stabilmente attorno ai 10.000 ai giorno. Non male
vero?

## Ma il codice open source è veramente più sicuro?

Se Settembre mi vede impegnato nella sottile, ma per me molto faticosa, arte di
organizzare il tempo, Ottobre mi ha visto su due palchi molto importanti:

* il [Codemotion di Milano](https://conferences.codemotion.com/milan2025/)
* l’[Hackersgen](https://event.hackersgen.com/), evento organizzato da
  Sorint.LAB per i ragazzi di alcune scuole superiori qui della zona tra le
  provincie di Milano e Bergamo.

Ho affrontato un tema abbastanza controverso, ovvero la non correlazione che
esiste tra un codice open source e il suo livello di sicurezza.

Le slide del talk sono disponibili
[qui](https://speakerdeck.com/thesp0nge/what-does-make-open-source-ecosystem-secure-one-audit-at-time-mean-version-2-dot-0).

Si lo so siamo tutti abituati a credere in massa che, essendo il codice alla
portata di tutti ed essendo la community quest’organismo positivo che mira alla
condivisione della conoscenza, beh allora anche il livello di sicurezza del
codice deve per forza essere alto.

Beep. Risposta sbagliata. O meglio, risposta teoricamente giusta. Il problema
sta tutto qui: il codice è sì lì, condiviso e libero di circolare, ma mancano
(statisticamente parlando) persone che fanno audit di sicurezza.

Da una parte abbiamo strumenti automatici come
[dependabot](https://github.com/dependabot) o similari, che ci permettono
trovare in automatico qualche *low hanging fruit* e che spesso ci vengono messi
a disposizione dalla piattaforma che ospita i sorgenti, dall’altra abbiamo
invece la mancanza di persone che analizzano il codice nel profondo, che
cerchino le vulnerabilità, che facciano pull request con le fix, che aprano bug,
insomma… che diano una mano.

Perché tutto questo? Non sono l’oracolo, posso solo dire che idea mi sono fatto:

1. fare audit del codice è un’attività lunga e complessa. Io per un audit di un
   pacchetto, diciamo di medie dimensioni, posso impiegare anche un mese di
   tempo.
2. fare audit del codice non è alla portata di tutti. Serve coniugare bene la
   mentalità dell’attaccante con l’amore e l’attitudine allo sviluppo software.
   In un mondo spesso polarizzato sulla divisione tra chi attacca e chi difende,
   tra chi *“fa l’hacker”* e chi *“è un builder e scrive codice”*, trovare
   persone che vadano oltre e sappiano fare da ponte tra i due mondi. Aneddoto
   curioso: una persona mi ha avvicinato a Codemotion, evento che di norma vede
   un buon 100% di sviluppatori e mi ha detto, forse per mettermi in difficoltà
   o forse per farmi capire che gli sto sul belin: “Paolo, ma cosa ci fai qui?
   Sei lontano dalla tua zona di comfort!!!”. Scrivo codice e mi occupo di
   sicurezza applicativa da 30 anni ma vabbé…
3. I maintainer non comunicano adeguatamente ai ricercatori di sicurezza, come
   interfacciarsi con loro. La
   [security policy](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)
   per i repository è qualcosa che Github o analoghi dovrebbero rendere
   obbligatori secondo me.

I talk sono stati molto belli, mi sono divertito molto a tenerli e a rispondere
alle domande della platea. Ho applicato lo stesso talk anche per l’evento
aziendale del prossimo anno, la [SUSECON 2026](https://www.suse.com/susecon/).
Vedremo cosa succederà.

## Le domande di Hackersgen ancora senza risposta

Durante il talk ad Hackersgen, putroppo, non c’è stato modo di rispondere a
tutte le domande. Per questo motivo, mi sono fatto dare l’elenco delle domande
arrivate e provo a rispondere qui: prometto, senza andare a cercare su Google.

### Codice “sporco” e Ai, ci sarà una futura crisi dovuta al codice impreciso?

In realtà non ho idea di cosa sia del codice “sporco”, forse si voleva dire
“malevolo”. In questo caso, no non credo ci sia una crisi in futuro.
Nell’apprendimento, il modello di AI potrà contare su tanto materiale valido,
per cui quello “sporco” potrebbe risultare trascurabile.

### Plugin di obsidian preferito?

Non uso Obsidian. Per le note sono molto analogico, uso un taccuino e una
stilografica nera. Mi piace la filosofia alla base del
[bullet journal](https://bulletjournal.com), quindi resto analogico su questa
parte.

Per le note invece tecniche, uso il mio fido editor [vim](https://www.vim.org) e
tanti file [Markdown](https://www.markdownguide.org/).

### Dalla mia esperienza personale, ho capito che un pentester esperto utilizza i suoi tool personali per pentesting. Tuttavia, come fa un professionista a creare tutti i tool che si hanno bisogno (come nmap, fuff, sqlmap, ecc.)?

Ecco, questa è una bella domanda. In realtà i tool base che un professionista
usa sono quelli che altre persone hanno creato e che magari lui può modificare o
combinare a suo piacimento. Sul “come fa” eventualmente a creare un tool,
sinceramente una volta individuato il problema che deve risolvere, il
professionista lo sviluppi :)

### Se potessi tornare indietro nel tempo per cambiare una sola piccola cosa (niente eventi enormi tipo “fermare una guerra”), cosa cambieresti?

Rispondo per quella che è la mia carriera. Tornerei nel luglio 2001 e quando il
professor Bruschi mi propose di rimanere in Ateneo come dottorando, me ne
fregherei che le società di consulenza pagavano di più e avrei accettato.

### Voglio sapere il gusto di gelato preferito

Caramello salato

### È ancora affidabile non dopo tutti gli attacchi ai pacchetti?

Qui penso volesse scrivere “npm”. Gli attacchi alla *supply chain* esistono ed
esisteranno sempre, quindi sì è ancora affidabile, ma, come dicevo nel talk, la
community deve fare la sua parte per evitare che codice malevolo ne infici la
qualità.

### Se il codice open source è più trasparente, perché non tutto il software critico del mondo è open?

Eh bella domanda. Credo che interessi militari e politici prendano il
sopravvento in ambienti critici per cui, difficile affidarsi ad un software che
comunque non ha un vendor alle spalle. Ricordiamo il detto: *nessuno è mai stato
licenziato per aver acquistato IBM*.

### É vero che non è revisionato, ma in un codice open source io ho il pieno controllo sulla gestione della sicurezza

E se non è revisionato, che tipo di controllo hai sulla gestione della
sicurezza?

### In zsh usi l’alias per nvim a vi?

```
|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ➜  ~ alias | grep vim gmtlvim='git merge...