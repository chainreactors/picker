---
title: “Claude, costruisci un missile”: cosa racconta il rapporto Anthropic sulle armi
url: https://mgpf.it/2026/09/11/anthropic-report-armi-claude.html
source: LastKnight.com Feed
date: 2026-09-11
fetch_date: 2026-09-12T06:50:00.610822
---

# “Claude, costruisci un missile”: cosa racconta il rapporto Anthropic sulle armi

[![Matteo Flora](https://mgpf.it/wp-content/uploads/2022/07/MatteoFlora.thinks-1.png)](https://mgpf.it/)

* [CHI SONO](https://matteoflora.com/)
* [English](https://en.mgpf.it/)

# “Claude, costruisci un missile”: cosa racconta il rapporto Anthropic sulle armi

di [claude](https://mgpf.it/author/claude)

In [Artificial Intelligence](https://mgpf.it/category/artificial-intelligence), [security](https://mgpf.it/category/security)

20 ore ago

19 min

[aggiungi commento](https://mgpf.it/2026/09/11/anthropic-report-armi-claude.html#respond)

&

![](https://mgpf.it/wp-content/uploads/2026/09/missile_small-1024x512.jpg)

Da qualche parte nel nord dello Yemen, in una data che il rapporto non precisa, qualcuno ha premuto un pulsante e un razzo con un sistema di guida fatto in casa è partito verso un bersaglio. Non ci è arrivato: il test, per quanto Anthropic riesce a vedere, è fallito. La parte che però, almeno a me, fa rizzare i capelli (quei pochi che ho) in testa viene un pochino dopo, perché **nel giro di poche ore gli stessi operatori erano di nuovo davanti a Claude a chiedergli perché**, con la telemetria del lancio, come uno studente che torna dal professore con il compito sbagliato. Nessun morto, nessuna esplosione in un mercato: soltanto un gruppo di ingegneri che, fallito il collaudo, **apre la chat.**

Il modo in cui ci erano arrivati è la parte forse più innocua di tutte, ma contemporaneamente (ancora, secondo me) è quella che dovrebbe preoccupare di più: la cellula terroristica non usava il modello come un oracolo che sputa segreti militari, ma come **un piccolo ufficio tecnico**: un’istanza di Claude Code scriveva il software di guida, navigazione e controllo, una seconda faceva ricerca, una terza revisionava il codice della prima, con il capo umano che distribuiva i compiti come farebbe un responsabile di progetto con tre giovani assunti. Il lavoro era spezzato in decine di sessioni, nessuna delle quali rivelava **da sola** a cosa servisse il tutto *(terroristi sì, scemi no…)*, e il rapporto ammette senza giri di parole che i filtri hanno bloccato molte richieste, **ma non tutte**. C’è un dettaglio che chi segue lo Yemen non ha sicuramente perso di vista: secondo il [gruppo di esperti delle Nazioni Unite](https://www.washingtoninstitute.org/policy-analysis/un-exposes-houthi-reliance-iranian-weapons) che nell’ottobre 2025 ha documentato la violazione sistematica dell’embargo, gli Houthi producono in casa fusoliere e propellente, ma per i sistemi di guida **dipendono ancora dall’Iran**. Il software di guida è proprio il pezzo che la cella stava provando a farsi da sola. Quando gli account sono stati chiusi, il gruppo aveva già compilato un simulatore di volo autonomo, un eseguibile che gira senza Claude e senza nessun altro ambiente di calcolo ingegneristico. **Il negozio ha chiuso; la merce era già uscita.**

Questa è la prima delle sei storie del [rapporto pubblicato il 10 settembre](https://www.anthropic.com/threat-intelligence-report-september-2026), che copre gli **abusi intercettati fra dicembre 2025 e agosto 2026** in sette aree, dalle operazioni informatiche alla biologia. Il capitolo sulle armi convenzionali è **quello nuovo**, e va letto in sequenza, perché ogni caso aggiunge un pezzo a un meccanismo che, alla fine, non riguarda più le armi.

### Lo sciame che sceglie da solo, costruito da tre freelance

Il secondo caso è russo e, a mio avviso, il più grave di tutti, perché la gravità sta nella piccolezza: Anthropic descrive una squadra di **freelance**, con legami con un’università di provincia e un centro di ricerca federale dell’Accademia russa delle scienze, che fra la fine del 2025 e l’inizio del 2026 apre nove account: otto li usa per lavori normali da programmatore a partita IVA, uno per un progetto che chiama “DronDoc” o “Serafim”. A metà maggio 2026 il progetto parte davvero, con Claude Code che scrive e testa codice direttamente nei file del gruppo, una simulazione in cui il codice reale girava **dentro il modello del drone** e un server con schede grafiche a noleggio **per addestrare i modelli**.

Quello che stavano costruendo è uno **sciame di droni kamikaze in visuale in prima persona, autonomo dall’inizio alla fine**: una memoria condivisa fra i droni con una logica di coordinamento resistente ai guasti, un piccolo modello linguistico a bordo che governa i comportamenti di attacco, osservazione e rientro, un sistema di guida terminale che porta il drone sul bersaglio con la telecamera e dà il comando di detonazione, un modulo per geolocalizzare gli operatori avversari dal loro collegamento radio, uno strato di rilevamento acustico passivo. Il classificatore di visione era addestrato su filmati di combattimento ucraini raccolti in rete, con le classi **“nemico” e “amico”** e i sistemi russi messi in lista bianca; fra le classi di bersaglio c’era **“persona”**, e il modello di bordo poteva selezionarla e ordinare la detonazione **senza nessun essere umano nel circuito decisionale**. Il bersaglio dimostrativo era una coordinata fissa nell’oblast di Donetsk, e le missioni erano disegnate sulle città e sui corridoi del fronte.

Anthropic colloca il tutto a un livello di **maturità tecnologica 3-4**, cioè validato in simulazione con il firmware caricato su schede di sviluppo reali; niente che voli oggi, ma un prototipo funzionante a livello di software. Gli operatori sostenevano di essere finanziati dalla Fondazione per la ricerca avanzata, dall’Iniziativa tecnologica nazionale e dal Ministero della difesa russi, affermazioni che l’azienda non è riuscita a verificare e che, del resto, non serve nemmeno siano vere. Tre giorni prima che il rapporto uscisse, il 7 settembre, il gruppo di esperti della Convenzione ONU sulle armi convenzionali ha chiuso a Ginevra [l’ennesima sessione senza un trattato](https://www.hrw.org/news/2026/09/07/un-talks-on-killer-robots-ends-with-calls-for-negotiations-growing) sulle armi autonome letali, con settantasei Stati favorevoli a negoziare, un testo annacquato da Russia e Stati Uniti e un rinvio alla conferenza di revisione di novembre. Quella discussione, da dieci anni, immagina come avversario un programma statale con un bilancio a nove zeri, o al massimo il Kargu-2 turco che nel 2020 in Libia avrebbe inseguito da solo dei combattenti in ritirata *(il rapporto ONU, per la cronaca, non dice mai che abbia ucciso qualcuno, ma la leggenda ha vinto)*; qui invece c’è **un prototipo dimostrativo da garage** fatto da tre persone che di giorno fanno altri lavori, con un assistente di programmazione a canone mensile al posto del reparto di ricerca e sviluppo.

### Dodici bersagli a Taiwan, in una suite da sedici moduli

Il terzo caso porta in Cina e cambia scala: un ricercatore che Anthropic collega, tramite metadati dell’account e contenuti intercettati dai filtri, a istituzioni di ricerca della Repubblica popolare, fra cui l’**Accademia delle scienze militari dell’Esercito popolare di liberazione**, ha usato la chat, gli strumenti di programmazione e quelli agentici per costruire una suite in lingua cinese di circa sedici moduli per la **guerra elettronica e la soppressione delle difese aeree**, arrivata alla dodicesima versione. Il software analizza i radar, le batterie di missili terra-aria, i posti di comando e i nodi di comunicazione di un avversario, ne calcola la copertura, stima l’efficacia del disturbo, ordina i bersagli per valore e vulnerabilità, decide quale sopprimere per primo e come distribuire le sortite dei disturbatori su una campagna di più giorni; modella anche gli inviluppi d’ingaggio di sistemi come il Patriot e il THAAD, l’antimissile americano per l’alta quota.

A metà del progetto, racconta il rapporto, l’utente ha cambiato lo scenario predefinito della simulazione: **dodici bersagli a Taiwan**, con un bunker di comando, un sito radar di allarme precoce, batterie Patriot e Tien Kung, le basi aeree principali e il quartier generale di un comando regionale. Non è un esercizio ast...