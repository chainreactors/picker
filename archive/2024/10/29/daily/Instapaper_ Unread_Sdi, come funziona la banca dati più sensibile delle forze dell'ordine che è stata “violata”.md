---
title: Sdi, come funziona la banca dati più sensibile delle forze dell'ordine che è stata “violata”
url: https://www.wired.it/article/sdi-sistema-indagine-ministero-interno-database/
source: Instapaper: Unread
date: 2024-10-29
fetch_date: 2025-10-06T18:56:01.549070
---

# Sdi, come funziona la banca dati più sensibile delle forze dell'ordine che è stata “violata”

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

Sdi, come funziona la banca dati più sensibile delle forze dell'ordine che è stata “violata”

* [Scienza](/scienza/)
* [Economia](/economia/)
* [Cultura](/cultura/)
* [Gadget](/gadget/)
* [Security](/security/)
* [Diritti](/diritti/)
* [Idee](/idee/)
* [Video](/video/)
* [Podcast](/podcast-wired/)
* [Wired Consiglia](/wired-consiglia/)

More*Chevron*

[Cerca

Cerca](/search/)

* [Scienza](/scienza/)
* [Economia](/economia/)
* [Cultura](/cultura/)
* [Gadget](/gadget/)
* [Security](/security/)
* [Diritti](/diritti/)
* [Idee](/idee/)
* [Video](/video/)
* [Podcast](/podcast-wired/)
* [Wired Consiglia](/wired-consiglia/)

[Riccardo Piccolo](/contributor/riccardo-piccolo/)

L'indagine

28.10.2024

# Sdi, come funziona la banca dati più sensibile delle forze dell'ordine che è stata “violata”

Il Sistema di indagine contiene tutte le denunce, i precedenti penali e le informazioni investigative raccolte dalle forze dell'ordine. La Procura di Milano indaga su una serie di infiltrazioni non autorizzate

![Poliziotti nel centro di comando della Questura di Milano](https://media-assets.wired.it/photos/671f54e8c96a23a0d03e8819/16:9/w_2560%2Cc_limit/1210654879)

Poliziotti nel centro di comando della Questura di MilanoGianmarco Maraviglia/Bloomberg via Getty Images

[Secondo quanto emerge da un'inchiesta della Procura di Milano](https://www.wired.it/article/dati-parlamentari-italiani-dark-web/) un gruppo di **informatici è riuscito a violare il Sistema di indagine (Sdi) del ministero dell'Interno**, la **banca dati più sensibile delle forze dell'ordine italiane,** attraverso un sofisticato virus informatico e con la complicità di persone infiltrate nel team di manutenzione. La banda faceva [riferimento alla **società Equalize srl**](https://www.wired.it/article/equalize-societa-dossier-pazzali-gallo), il cui amministratore delegato è l'ex poliziotto Carmine Gallo. Come rivelato nelle intercettazioni pubblicate dal *Corriere della Sera*, **il sistema utilizzat**o permetteva di "***scaricare i dati direttamente dalla banca dati del ministero dell'Interno*"** grazie a un [malware](https://www.wired.it/article/windows-antivirus-serve-ancora/) di tipo Rat (Remote Access Trojan) inserito nei server del Viminale.

**Risultano indagati** nell'inchiesta, coordinata dal pubblico ministero Francesco De Tommasi, con l'aggiunto Alessandra Dolci e il procuratore Marcello Viola, [**Enrico Pazzali,** presidente di Fondazione Fiera Milano](https://www.wired.it/article/enrico-pazzali-equalize-inchiesta-procura-milano), consigliere dell’Università Bocconi e principale socio di Equalize, ora sotto sequestro; **Gallo**, [socio di minoranza dell'azienda](https://www.wired.it/article/carmine-gallo-poliziotto-reggiani-sgrena-equalize-banche-dati), **Nunzio Samuele Calamucci**, socio di un’agenzia di investigazioni e esperto informatico.

## Anatomia dello Sdi

[Lo Sdi è molto più di una semplice banca dati](https://www.wired.it/article/beyond-piattaforma-dossier-equalize-come-funziona-dati). Secondo la documentazione tecnica del Viminale, si tratta di **un sistema informativo complesso che si articola in 13 aree applicative principali**, dalla gestione delle armi al controllo degli stranieri, dalle informative di polizia al monitoraggio delle gare d'appalto. Il cuore del sistema è costituito dall'area **"Informative"**, che gestisce tutte le **denunce dei cittadini** e le attività delle forze dell'ordine. Qui confluisce "*qualsiasi comunicazione originata dalle **denunce effettuate alle Forze di polizia da parte del cittadino*****"**, che possono riguardare sia persone (scomparse, sequestrate, ritrovate) sia oggetti (veicoli rubati, documenti smarriti).

[Un'altra componente cruciale della banca dati](https://www.wired.it/article/agenzia-per-la-cybersicurezza-nazionale-equalize-inchiesta-calamucci-milano/) è il **"Sistema utente investigativo"** (Sisute), un sofisticato motore di ricerca interno che permette agli investigatori di consultare e collegare tra loro informazioni provenienti da diverse fonti. Attraverso questo strumento, un agente può per esempio **verificare se una persona fermata per un controllo ha precedenti penal**i, vedere se un'auto è rubata o controllare se un cittadino straniero ha un **permesso di soggiorno valido**. Il sistema può anche interfacciarsi con database esterni come quello dell'Aci per le auto, della Motorizzazione per le patenti e del Sistema Schengen per i ricercati in Europa.

Le dimensioni del sistema violato sono impressionanti. Si tratta di uno dei più **grandi sistemi informatici della [pubblica amministrazione italiana](https://www.wired.it/article/it-wallet-documenti-app-io-obbligatorio-tempi-uso-valore-legale/)**, con una complessità paragonabile a quella dei maggiori istituti bancari. La sua struttura comprende centinaia di database interconnessi che gestiscono ogni aspetto dell'attività investigativa e di sicurezza nazionale.

Nell'area "Macro" sono mappate **tutte le connessioni della criminalità organizzata, le reti terroristiche e i gruppi eversivi**, con i loro collegamenti, le gerarchie e le attività sul territorio. Un patrimonio di intelligence che, finito nelle mani sbagliate, potrebbe compromettere anni di indagini. Come rivela il *Corriere della Sera*, gli indagati avevano persino accesso al sistema FastSDI-StatDel, **che analizza i trend criminali e aiuta a prevedere possibili minacce alla sicurezza**. Non solo dati storici, ma anche le preziose "copie forensi" dei cellulari sequestrati, che contengono le prove digitali delle indagini in corso.

![article image](https://media-assets.wired.it/photos/615da627b217d49ff6a16db3/master/w_775%2Cc_limit/wired_placeholder_dummy.png)

[WiredLeaks, come mandarci una segnalazione anonima](/internet/web/2021/02/15/wiredleaks-come-fare-segnalazioni-anonime/)

Conosci altri casi di database sensibili accessibili anche a chi non è autorizzato? Inviaci una segnalazione anonima

## Come è stato violato il sistema?

Sulla carta, la [sicurezza](https://www.wired.it/article/nazioni-unite-un-women-sicurezza-informatica-database/) dovrebbe essere garantita da un sistema di protezione a più livelli. **Gli agenti possono accedere solo da computer specificamente autorizzati**, collegati a una rete interna protetta. Ogni ricerca deve essere motivata e viene registrata nel sistema, creando una sorta di "registro delle consultazioni" che permette di identificare eventuali abusi.

[Ma è proprio qui che la banda è riuscita a inserirsi.](https://www.wired.it/article/equalize-aziende-clienti-dossier-erg-barilla) Come rivela *Il Messaggero*, stando a quanto emerge dalle indagini, il gruppo avrebbe infiltrato due team chiave: **"i ragazzi di Bologna"**, che si sarebbero occupati dello sviluppo del software, e **"i ragazzi di Colchester"** nel Regno Unito, responsabili della progettazione del sistema. Non solo: secondo la ricostruzione dell'indagine, gli informatici sarebbero riusciti ad avere accesso anche ai **"server fisici di Torino"**, dove sono effettivamente conservati i dati. Un'infiltrazione che, secondo le intercettazioni riportate dal *Corriere della Sera*, avrebbe garantito al gruppo un vantaggio di oltre quattro anni rispetto a qualsiasi tentativo di individuazione. Una penetrazione a tutti i livelli che ha permesso loro di aggirare ogni sistema di sicurezza e di **scaricare enormi quantità di dati sensibili senza essere individuati.**

## Le storie da non perdere di Wired

* È iniziato a Rovereto il Wired Next Fest Trentino. Incontri, eventi, workshop e attività per parlare di innovazione, tecnologie e delle “energie” che ci servono fino al 5 ottobre. Per partecipare ai talk e interviste, [iscriviti sul sito dedicato o segui la diretta live!](https://eventi.wired.it/nextfest25-trentino/)
* ⛵️ Come seguire la missione della [Global Sumud Flotilla](https://www.wired...