---
title: Così ci siamo dimenticati delle falle nel silicio
url: https://www.guerredirete.it/cosi-ci-siamo-dimenticati-delle-falle-nel-silicio
source: Over Security
date: 2026-11-17
fetch_date: 2026-11-18T09:23:25.032066
---

# Così ci siamo dimenticati delle falle nel silicio

[![Guerre di Rete](/assets/brand/guerredirete_orizzontale.png)](/)

Sezioni

[Cyber](/articoli/categorie/cyber)
[Diritti e sorveglianza](/articoli/categorie/diritti-e-sorveglianza)
[Economia e politica](/articoli/categorie/economia-e-politica)
[Intelligenza Artificiale](/articoli/categorie/intelligenza-artificiale)
[Internet](/articoli/categorie/internet)
[Editoriale](/articoli/categorie/editoriale)

[Chi siamo](/chi-siamo)
[Il progetto](/il-progetto)
[La newsletter](https://guerredirete.substack.com)
[Speciali](/speciali)
[Sostienici](/sostienici)

Sezioni

[Cyber](/articoli/categorie/cyber)
[Diritti e sorveglianza](/articoli/categorie/diritti-e-sorveglianza)
[Economia e politica](/articoli/categorie/economia-e-politica)
[Intelligenza Artificiale](/articoli/categorie/intelligenza-artificiale)
[Internet](/articoli/categorie/internet)
[Editoriale](/articoli/categorie/editoriale)

[Chi siamo](/chi-siamo)
[Il progetto](/il-progetto)
[La newsletter](https://guerredirete.substack.com)
[Speciali](/speciali)

[Sostienici](/sostienici)

![Guerre di Rete](/assets/brand/guerredirete_orizzontale.png)

## Cerca nel sito

Cerca articoli

Cerca

Inserisci un titolo o un argomento per iniziare.

![Così ci siamo dimenticati delle falle nel silicio](/)

[Economia e politica](/articoli/categorie/economia-e-politica)

# Così ci siamo dimenticati delle falle nel silicio

[N. A.](/autore/n-a) · 14 marzo 2022

Stiamo assistendo alla crescita silenziosa di vulnerabilità e attacchi a chip, memorie, periferiche. Dopo anni di interesse rivolto solo alle prestazioni e frammentazione della supply chain, ecco chi sta lavorando per inserire la sicurezza fin dalla progettazione.

![Credits: foto di Umberto](/img/asset/YXNzZXRzL2FydGljb2xpLWlubGluZS9jb3NpLWNpLXNpYW1vLWRpbWVudGljYXRpLWRlbGxlLWZhbGxlLW5lbC1zaWxpY2lvLWlubGluZS0xLmpwZw/cosi-ci-siamo-dimenticati-delle-falle-nel-silicio-inline-1.jpg?w=1200&s=fb8d5cfa9c783c2e4b77e0b795e7c45a)

Credits: foto di Umberto

Quando lo scorso 9 novembre Intel ha [reso pubblica](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00562.html) l’esistenza di\*\* **tre nuove falle di sicurezza che affliggono una lunga lista dei suoi processori**, **la notizia è passata pressoché sotto silenzio. L’eco dell’annuncio fatto sul sito ufficiale di Santa Clara non si è spinto oltre l’esiguo perimetro informativo delimitato da [portali tech](https://www.bleepingcomputer.com/news/security/high-severity-bios-flaws-affect-numerous-intel-processors/) e di cybersicurezza. Eppure, le falle scoperte dai ricercatori di Sentinel One e Positive Technologies per conto di Intel non sono da prendere sottogamba. Al contrario, secondo il sistema di classificazione gestito da Mitre Corporation noto come “Common Vulnerabilities and Exposures”, o, più semplicemente, CVE – un database pubblico nato alla fine degli anni ‘90 per tenere traccia dei bug del software, estesosi poi progressivamente anche alle vulnerabilità hardware –** **il loro impatto è da considerarsi di tipo alto:** \*\*su una scala da uno a dieci, [alla falla meno seria](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00528.html) viene attribuito un valore di 7,1, mentre [le due più gravi](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00562.html) arrivano fino ad 8,2.

Un malintenzionato determinato a sfruttarle – per poterlo fare è però necessario avere accesso fisico alla macchina che monta il processore difettoso – può condurre una “Escalation of Privileges” (EoP), ovvero un\*\* **attacco attraverso cui garantirsi in maniera illecita i privilegi di amministratore di un sistema** **e prenderne il controllo. E con ‘sistema’ non si intendono solo server e portatili – per esempio un laptop rubato da cui estrarre le chiavi di cifratura in modo da avere accesso alle informazioni che esso custodisce – ma anche un’automobile: infatti, una delle CPU** \*\*(acronimo di Central Processing Unit, un altro modo di dire processore) affette dalle falle di sicurezza in questione è stata progettata appositamente per il settore [automotive](https://newsroom.intel.com/press-kits/intel-atom-processor-e3900-series/#gs.sea8d8) ed è il cervello di diversi modelli di autovetture attualmente in circolazione.

**L’insicurezza hardware è un tema che resta trascurato**, e non perché non sia rilevante, anzi. È semmai un elemento integrante dell’infrastruttura tecnologica usata quotidianamente da miliardi di persone. Ma come dice il filosofo francese Benjamin Constant, ci si abitua alle infrastrutture tecniche e alle loro caratteristiche (insicurezza inclusa), così come ci si abitua alle leggi naturali della fisica.

# **Una, cento, mille falle**

Quando si parla di insicurezza hardware si fa spesso riferimento solo alle falle più note al grande pubblico: [Rowhammer](https://en.wikipedia.org/wiki/Row_hammer), [Meltdown](https://en.wikipedia.org/wiki/Meltdown_%28security_vulnerability%29) e [Spectre](https://en.wikipedia.org/wiki/Spectre_%28security_vulnerability%29). Queste vulnerabilità interessano differenti componenti dei computer – Rowhammer la memoria RAM, Meltdown e Spectre il processore – ma hanno tutte origine in dei difetti di progettazione che permettono ad un attaccante di usare in modo improprio le normali funzionalità di un chip e provocare così dei problemi di sicurezza inaspettati.

Parlare di queste tre falle al singolare sarebbe un errore. La comunità di sicurezza informatica ha continuato a studiarle anche dopo che la loro esistenza era stata resa pubblica e per ognuna ha individuato numerose varianti. Quelle di Spectre sono venute a galla con cadenza quasi mensile nei due anni successivi alla sua scoperta e l’ultima ad essere stata resa nota risale al [maggio del 2021](https://www.cs.virginia.edu/venkat/papers/isca2021a.pdf). Nel 2019 invece, un gruppo di ricercatori ha annunciato di aver messo a punto un nuovo attacco alla memoria RAM (ribattezzato “[RamBleed](https://rambleed.com/)”) basato su Rowhammer, nonostante fossero passati più di cinque anni da quando [un gruppo di ricercatori della Carnegie Mellon](https://users.ece.cmu.edu/~yoonguk/papers/kim-isca14.pdf) ne aveva annunciato l’esistenza al mondo.

![Rambleed, Spectre e Meltdown](/img/asset/YXNzZXRzL2FydGljb2xpLWlubGluZS9jb3NpLWNpLXNpYW1vLWRpbWVudGljYXRpLWRlbGxlLWZhbGxlLW5lbC1zaWxpY2lvLWlubGluZS0yLnBuZw/cosi-ci-siamo-dimenticati-delle-falle-nel-silicio-inline-2.png?w=1200&s=52bcb5e25d6206091ebf5477b2ef72c7)

Rambleed, Spectre e Meltdown

# Memorie,\*\* processori, ma anche periferiche\*\*

Esistono poi attacchi che utilizzano in maniera combinata Rowhammer e Spectre: [SpecHammer](https://www.computer.org/csdl/proceedings-article/sp/2022/131600b362/1A4Q4ffpqlW) permette di eludere qualsiasi forma di contromisura fino ad oggi elaborata per mitigare l’impatto di queste due falle, mentre [Spoiler](https://arxiv.org/pdf/1903.00446.pdf) utilizza i difetti presenti nei processori Intel per rendere più semplici gli attacchi alla RAM. Basta così? Magari, perché purtroppo non sono solo i transistor di cui sono fatti i processori ed i banchi di memoria ad essere inaffidabili. Alla lista vanno aggiunti anche [Bluetooth](https://www.armis.com/research/blueborne/), [USB](https://web.archive.org/web/20161019034729/https%3A//srlabs.de/wp-content/uploads/2014/07/SRLabs-BadUSB-BlackHat-v1.pdf), interfacce [Thunderbolt](https://fahrplan.events.ccc.de/congress/2014/Fahrplan/events/6128.html), [wireless](https://www.krackattacks.com/), [chip di sicurezza](https://crocs.fi.muni.cz/_media/public/papers/nemec_roca_ccs17_preprint.pdf): praticamente qualsiasi altra periferica di cui sono fatti i nostri computer\*\* \*\*– e quindi i nostri telefoni, elettrodomestici, orologi, consolle da gioco, contatori del gas, sistemi di controllo industriali e veicoli di trasporto, aeroplani inclusi – è nota per essere o essere stata affetta da una vulnerabilità più o meno grave.

# **La silenziosa crescita delle falle ha...