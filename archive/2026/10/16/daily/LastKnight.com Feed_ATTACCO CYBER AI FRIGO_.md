---
title: ATTACCO CYBER AI FRIGO?
url: https://mgpf.it/2026/10/16/attacco-cyber-frigo.html
source: LastKnight.com Feed
date: 2026-10-16
fetch_date: 2026-10-17T06:37:53.557957
---

# ATTACCO CYBER AI FRIGO?

[![Matteo Flora](https://mgpf.it/wp-content/uploads/2022/07/MatteoFlora.thinks-1.png)](https://mgpf.it/)

* [CHI SONO](https://matteoflora.com/)
* [English](https://en.mgpf.it/)

# ATTACCO CYBER AI FRIGO?

In [hacking](https://mgpf.it/category/hacking), [security](https://mgpf.it/category/security)

15 ore ago

16 min

A

![](https://mgpf.it/wp-content/uploads/2026/10/frigo_small-1024x512.jpg)

Nella notte fra domenica 11 e lunedì 12 ottobre 2026, in circa **150 Intermarché** sparsi per la Francia, i banchi frigo hanno smesso di raffreddare e si sono messi a scaldare, arrivando a **50 gradi per sei ore**, come il gruppo Les Mousquetaires ha raccontato a [Reuters](https://www.internazionale.it/ultime-notizie-reuters/2026/10/12/hackers-heat-french-supermarket-fridges-sparking-fires-and-food-losses) *(mamma, me lo ricordavo diverso il bollitore!)*; la mattina dopo i direttori hanno trovato carne, formaggi e yogurt da buttare, e la stessa scena si è ripetuta, secondo le catene, in 80 Carrefour, in circa il 5% dei Monoprix e in un numero ancora imprecisato di Coopérative U e Leclerc *(i totali ballano fra 250 e 500 negozi a seconda di chi conta, e infatti ve li do sempre con il nome di chi li ha contati…)*. Thierry Cotillard, presidente di Intermarché, intervistato dall’emittente BFMTV e ripreso dall’[Agence France-Presse](https://www.lavenir.net/actu/monde/2026/10/13/cyberattaque-des-frigos-de-supermarches-en-france-des-millions-deuros-de-pertes-des-frigos-a-50c-des-produits-jetes-videos-SDZ772RZVRCH7O47347UPSQGQM/), ha parlato di **decine di milioni di euro di merce persa in una sola mattinata**, aggiungendo il dettaglio che a me pare il più eloquente di tutto il caso: **le assicurazioni non coprono questo tipo di incidente**.

Non è stato un ransomware, perché nessuno ha chiesto soldi e al 14 ottobre 2026 nessuno ha rivendicato niente, e non è stato nemmeno un furto di dati, che è la forma a cui ci hanno abituato vent’anni di titoli sugli attacchi informatici. Qualcuno è entrato nei sistemi che regolano la refrigerazione, in gran parte centraline del fabbricante danese **Danfoss**, e ha ordinato ai banchi di **andare in sbrinamento tutti insieme**, cioè ha fatto partire una funzione normalissima, quella che scalda le serpentine per sciogliere il ghiaccio, nel momento sbagliato e per il tempo sbagliato: tenuta accesa per ore, invece che per i pochi minuti previsti, scalda il banco intero. Il danno è fisico, si conta in chili di cibo e in euro, e passa per un oggetto che nessun cliente ha mai guardato in vita sua: **la centralina che comanda i frigoriferi**, appesa al muro di un retro, con la sua lucina verde accesa.

Se vi state chiedendo perché ve ne parlo qui e non su una rivista di cronaca francese, la risposta sta in un nome e in due date. Il nome è **Dixell**, un altro fabbricante di controllori per la refrigerazione, diverso da Danfoss, nato ad Alpago, in provincia di Belluno, che oggi si chiama [Copeland Controls](https://www.expoclima.net/en/aziende/1262/copeland-controls-srl/profilo) e ha sempre sede lì: il 13 ottobre 2026 i suoi sistemi di supervisione *xweb* sono entrati nell’elenco degli apparecchi colpiti, aggiornato dalle autorità francesi. La prima data è il **20 maggio 2025**, il giorno in cui l’agenzia americana per la sicurezza informatica pubblicava un avviso sulle vulnerabilità di quegli stessi controllori Danfoss, con la raccomandazione esplicita di non lasciarli raggiungibili da Internet. La seconda è il **31 ottobre 2026**, il termine entro cui le aziende italiane già iscritte nell’elenco della NIS2, la direttiva europea sulla sicurezza delle reti, devono avere in piedi le misure di sicurezza di base. Fra la prima e la seconda ci stanno diciassette mesi in cui, a giudicare dai risultati, **una parte del settore si è dimenticata di staccare quelle centraline da Internet**, che in molti casi vuol dire, alla lettera, staccare un cavo di rete *(in altri è molto più difficile, specialmente se hanno una sim a bordo)*.

### Quello che sappiamo, e quello che ancora non sappiamo

La fonte più solida è l’[allerta del CERT-FR](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/), la squadra di risposta agli incidenti dell’agenzia francese per la cybersicurezza (l’ANSSI), pubblicata il 12 ottobre 2026 e aggiornata il giorno dopo. Parla di **numerose compromissioni di controllori remoti per impianti di refrigerazione**, indica le serie Danfoss AK-SM e AK-SC e, nell’aggiornamento, i sistemi xweb di Copeland e Dixell, e soprattutto scrive una frase che andrebbe appesa in ogni ufficio acquisti: *“esporre un’interfaccia di gestione su Internet è contrario alle buone pratiche” (grazie al…)*. Le raccomandazioni sono quelle che chiunque si occupi di sicurezza ripete da vent’anni, cioè togliere gli apparecchi da Internet, rientrarci solo attraverso una rete privata protetta (la famosa VPN), controllare le fasce di sbrinamento, cambiare le password di fabbrica, e c’è un avvertimento che pesa più di tutto il resto: un apparecchio **fuori supporto**, che non riceve più correzioni, lasciato esposto ha una probabilità *“molto forte”* di essere compromesso, e rimetterlo alle impostazioni di fabbrica non basta, perché resta vulnerabile e verrà bucato di nuovo.

Danfoss, dal canto suo, ha spiegato a [Cooling Post](https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/) che la maggior parte delle unità colpite sono **prodotti vecchi**, come l’AK-SM800, a fine vita dal 2021, e l’AK-SC355, ritirato nel 2016, oppure modelli attuali con il software non aggiornato. Che sposta solo ad un altro problema: avete ancora un sistema in manutenzione o no? Il resto del quadro è ancora in movimento, e conviene dirlo onesti: la procura di Parigi ha aperto un’inchiesta con l’ufficio di polizia giudiziaria francese per i reati informatici; una fonte vicina al primo ministro Sébastien Lecornu ha detto a Reuters che l’ANSSI avrebbe individuato una vulnerabilità nel software danese, mentre l’allerta pubblica non ne indica nessuna; un analista della società Sekoia, sempre a Reuters, sostiene che siano stati colpiti anche Spagna, Portogallo, Polonia, Germania e Belgio, ma per ora è una voce sola *(e io le voci sole le tratto come i funghi raccolti da un amico: probabilmente buoni, ma prima li fa vedere a qualcuno)*. **Nessuna attribuzione, nessuna rivendicazione, nessuna richiesta di riscatto**: chi sia stato e perché, al momento, non lo sa nessuno, e diffido di chi ve lo racconta con sicurezza.

### Diciassette mesi di avvisi, letti da chi?

La parte che non è in movimento, invece, è la cronologia, e vale la pena metterla in fila con un minimo di ordine… Il **20 maggio 2025** la CISA, l’agenzia statunitense per la sicurezza informatica e delle infrastrutture, pubblica l’[avviso ICSA-25-140-03](https://www.cisa.gov/news-events/ics-advisories/icsa-25-140-03) sui controllori Danfoss della serie **AK-SM 8xxA**: il difetto più grave è che la password di servizio veniva generata a partire dalla data e dall’ora del dispositivo, per cui chi conosce il metodo può calcolarsi da solo la chiave del giorno e **saltare del tutto il login** *(per i nerd, un “code of the day” che fa tanto anni Novanta, con un punteggio di gravità di 8,2 su 10)*. Danfoss corregge il difetto della password con la versione R4.2, il 26 agosto 2025 l’avviso viene aggiornato con altre due vulnerabilità, una delle quali permette di eseguire comandi sul dispositivo, e la raccomandazione della CISA è scritta in chiaro: **ridurre l’esposizione in rete, fare in modo che questi apparecchi non siano accessibili da Internet**, metterli dietro un firewall e usare una VPN per l’accesso remoto.

Il **9 agosto 2026** i ricercatori di Claroty Team82, gli stessi che avevano segnalato il problema alla CISA, pubblicano il racconto completo con un titolo che oggi suona come una profezia, [*“Congela il controllore, scongela il cibo”*](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food...