---
title: Spyware, come una cybergang russa sfrutta gli strumenti di Nso group
url: https://www.wired.it/article/spyware-apt29-nso-group-intellexa/
source: Instapaper: Unread
date: 2024-09-02
fetch_date: 2025-10-06T18:26:43.526016
---

# Spyware, come una cybergang russa sfrutta gli strumenti di Nso group

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

Come una cybergang russa sfrutta gli strumenti delle aziende di spyware

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

[Lily Hay Newman](/contributor/lily-hay-newman/)

[Security](/security/)

30.08.2024

# Come una cybergang russa sfrutta gli strumenti delle aziende di spyware

Google ha scoperto che i criminali informatici di Apt29 sono riusciti a violare una serie di siti web in modo da utilizzare sofisticati exploit molto simili a quelli creati da Nso e Intellexa

![Image may contain Electronics and Hardware](https://media-assets.wired.it/photos/66d18eafbd696ca9c760c542/16:9/w_2560%2Cc_limit/GettyImages-1392424007.jpg)

Photograph: Just\_Super/ Getty Images

Negli ultimi anni, i produttori di **spyware** commerciali d'élite come Intellexa e [Nso group](https://www.wired.it/article/pegasus-spyware-nso-commissione-parlamento-trasparenza/) hanno sviluppato una serie di potenti strumenti che sfruttano [vulnerabilità zero-day](https://www.wired.it/article/cybersecurity-attacchi-zero-day/) rare e non ancora corrette nei software per compromettere i dispositivi delle vittime. E sempre più spesso i governi di tutto il mondo diventano i [principali](https://www.wired.it/article/nso-pegasus-el-salvador/) [clienti](https://www.wired.it/article/pegasus-spyware-nso-nagorno-karabakh/) di queste aziende, utilizzando i loro prodotti per violare gli smartphone di leader dell'opposizione, giornalisti, attivisti, avvocati e altri ancora. Giovedì tuttavia il Threat analysis group di Google (Tag, l'unità del gigante che si occupa di minacce informatiche) [ha pubblicato un'analisi](https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/) che rivela come una serie di **recenti campagne apparentemente condotte dalla famigerata cybergang russa Apt29 Cozy Bear** ha sfruttato **exploit molto simili a quelli sviluppati da Intellexa e Nso Group** per attività di **spionaggio ancora in corso**.

## L'analisi di Google

Tra il novembre 2023 e il luglio 2024, gli aggressori hanno compromesso i siti web del **governo della Mongolia**, sfruttando poi l'accesso per sferrare **[attacchi di tipo *watering hole*](https://www.wired.com/story/what-is-a-watering-hole-attack-hacking/)**, violando i dispositivi vulnerabili che caricavano un sito compromesso. I criminali informatici hanno configurato la loro infrastruttura dannosa in modo da sfruttare **exploit "*identici o sorprendentemente simili a quelli precedentemente utilizzati dai fornitori di servizi di sorveglianza commerciale Intellexa e Nso group*"**, riporta il Tag. I ricercatori dicono di "*ritenere con moderata fiducia*" che le campagne siano state condotte da Apt29.

Questi strumenti simili a spyware hanno sfruttato **vulnerabilità di iOs e Android**, che però in gran parte erano già state corrette. Anche se in origine erano stati distribuiti dalle aziende di spyware come exploit zero-day, ovvero di cui non era nota l'esistenza, i cybercriminali russi li hanno utilizzati per colpire i dispositivi che non erano stati aggiornati con le correzioni.

"*Sebbene non sia certo come i sospetti aggressori di Apt29 abbiano acquisito questi exploit, la nostra ricerca sottolinea la misura in cui gli exploit sviluppati originariamente dall'industria della sorveglianza commerciale siano arrivati ad attori pericolosi* – scrivono i ricercatori del Tag. –*. Gli attacchi watering hole rimangono una minaccia che permette di usare exploit sofisticati per colpire coloro che visitano regolarmente siti, anche su dispositivi mobili. Possono rappresentare ancora una via efficace per* [... ] ***colpire in massa una popolazione che potrebbe ancora utilizzare browser senza patch***". È possibile che i criminali informatici abbiano acquistato e adattato gli exploit spyware oppure che li abbiano rubati o acquisiti tramite un leak. Ma non si può escludere nemmeno che si siano ispirati agli strumenti commerciali e che li abbiano poi modificati esaminando i dispositivi infetti delle vittime.

"***Nso non vende i suoi prodotti alla Russia*** – ha dichiarato a *Wired US* Gil Lainer, vicepresidente dell'azienda per le comunicazioni globali –*. Le nostre tecnologie sono vendute esclusivamente ad agenzie di intelligence e forze dell'ordine alleate di Stati Uniti e Israele. I nostri sistemi e le nostre tecnologie sono estremamente sicuri e vengono continuamente monitorati per rilevare e neutralizzare le minacce esterne*".

## La strategia dei cybercrminali

Tuttavia, tra il novembre 2023 e il febbraio 2024 gli aggressori hanno utilizzato un exploit per iOs e Safari **tecnicamente identico a un prodotto di Intellexa**, presentato per la prima volta un paio di mesi prima. Nel luglio 2024, poi, i cybercriminali hanno impiegato anche un **exploit per Chrome adattato da uno strumento di Nso group** apparso per la prima volta nel maggio 2024. Quest'ultimo è stato utilizzato in combinazione con un exploit che presentava forti somiglianze con un altro lanciato da Intellexa nel settembre 2021.

Quando gli aggressori sfruttano vulnerabilità per cui è già stata distribuita una patch, si parla di **n-day exploitation**, dal momento che la falla esiste ancora e può essere sfruttata nei dispositivi non aggiornati. La cybergang russa ha costruito le sue campagne – compresa la distribuzione di malware e l'attività sui dispositivi compromessi – in modo diverso da come farebbe un classico cliente di spyware commerciali, un aspetto che indica un **livello di fluidità e di competenza tecnica caratteristico di un gruppo di cybercriminali affermato e ben finanziato da uno stato**.

"*In ogni versione delle campagne di watering hole, gli aggressori hanno utilizzato exploit identici o sorprendentemente simili a quelli di* [fornitori di prodotti di sorveglianza commerciali] *Intellexa e Nso group* – ha scritto il Tag –*. Non sappiamo come gli aggressori abbiano acquisito questi exploit. **Ciò che è chiaro è che gli attori di Apt stanno utilizzando exploit n-day che sono stati originariamente utilizzati come zero-day*****" da questo tipo di aziende**.

*Questo articolo è apparso originariamente [su Wired US](https://www.wired.com/story/russia-cozy-bear-watering-hole-attacks/).*

## Le storie da non perdere di Wired

* È iniziato a Rovereto il Wired Next Fest Trentino. Incontri, eventi, workshop e attività per parlare di innovazione, tecnologie e delle “energie” che ci servono fino al 5 ottobre. Per partecipare ai talk e interviste, [iscriviti sul sito dedicato o segui la diretta live!](https://eventi.wired.it/nextfest25-trentino/)
* ⛵️ Come seguire la missione della [Global Sumud Flotilla](https://www.wired.it/topic/global-sumud-flotilla), la flotta umanitaria diretta a Gaza
* 🔌 È in edicola il nuovo numero di *Wired* che parla di energia. [Abbonati!](https://abbonatiqui.it/rivista/wired)
* ❗️Il caso di Alberto Trentini, il cooperante in carcere in Venezuela da novembre 2024: [le notizie per non spegnere l'attenzione](https://www.wired.it/topic/alberto-trentini/) e chiederne l'immediata liberazione
* 🇺🇦 Le condizioni per un accordo tra Ucraina e Russia e [gli sviluppi del conflitto](https://www.wired.it/topic/ucraina/)
* 🇮🇱 🇵🇸 L'escalation [in Medio Oriente](https://www.wired.it/topic/israele/): cosa sta succedendo in [Israele](https://www.wired.it/topic/israele/) e la [crisi umanitaria a Gaza...