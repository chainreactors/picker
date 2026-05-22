---
title: Pipeline sotto assedio: come i threat actor nation-state stanno compromettendo la software supply chain
url: https://www.ictsecuritymagazine.com/articoli/software-supply-chain-attacchi/
source: ICT Security Magazine
date: 2026-05-21
fetch_date: 2026-05-22T06:08:36.373886
---

# Pipeline sotto assedio: come i threat actor nation-state stanno compromettendo la software supply chain

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Attacchi alla software supply chain di matrice nation-state i paradigmi 3CX, SolarWinds, Volt Typhoon e XZ Utils. Francesco Schifilliti, Cyber Crime Conference](https://www.ictsecuritymagazine.com/wp-content/uploads/Attacchi-alla-software-supply-chain-di-matrice-nation-state-i-paradigmi-3CX-SolarWinds-Volt-Typhoon-e-XZ-Utils.-Francesco-Schifilliti-Cyber-Crime-Conference-scaled.jpg)

# Pipeline sotto assedio: come i threat actor nation-state stanno compromettendo la software supply chain

A cura di:[Redazione](#molongui-disabled-link)  Ore 21 Maggio 202615 Maggio 2026

*Dall’intervento di Francesco Schifilliti, Cyber Investigation & Threat Intelligence Advisor, alla 1[4ª Cyber Crime Conference](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026) (Roma, 6-7 maggio 2026)*

Negli ultimi cinque anni gli attacchi alla supply chain software sono cresciuti di circa il 400%, secondo una stima che incrocia i dati di Sonatype ed ENISA, e nello stesso periodo si è aperta una forbice che è oggi il nodo centrale per chi difende: solo il 9% delle organizzazioni li considera una minaccia prioritaria, mentre il 31% li indica come la categoria di attacco effettivamente subìta.

Su questo scarto fra percezione e realtà operativa Francesco Schifilliti ha costruito l’intervento alla 14ª Cyber Crime Conference, dedicato alla compromissione della pipeline software da parte di attori nation-state. Una riflessione che intreccia teoria dell’attacco, casistica forense e letture difensive, organizzata attraverso quattro paradigmi operativi distinti: 3CX, SolarWinds, Volt Typhoon e XZ Utils.

## Cos’è un attacco alla supply chain: due vittime, una sola fiducia tradita

Un attacco alla supply chain si distingue da qualunque altro vettore per una caratteristica strutturale: non esiste una sola vittima, ne esistono almeno due. La prima è la vittima primaria, tipicamente il produttore del software (*vendor*), che subisce la compromissione iniziale e mantiene visibilità tecnica sull’evento. La seconda è la vittima secondaria, cioè l’organizzazione cliente che riceve il *payload* attraverso una relazione di fiducia legittima con il *vendor*, e che non ha alcuna visibilità sulle fasi *upstream* della catena. Una *remediation* che non consideri entrambe le classi di vittima è incompleta per definizione.

![Francesco Schifilliti, Cyber Crime Conference 2026: software supply chain security, software supply chain, supply chain attack, pipeline software, supply chain security](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_nkvKFiThMy-700x393.png)

*Francesco Schifilliti, Cyber Crime Conference 2026*

Il secondo elemento distintivo è che un attacco alla supply chain è sempre, in ultima analisi, un attacco al *trust*. Mentre tutti gli altri vettori lavorano su una debolezza tecnica, umana o di configurazione della vittima, qui l’attaccante ribalta la logica: utilizza le difese del bersaglio finale come vettore di compromissione. Il software è verificato, il certificato è valido, il canale di aggiornamento è quello ufficiale: il confine di fiducia viene attraversato prima ancora che la vittima possa accorgersene. Esempi affini di attacchi al *trust* fuori dal perimetro della supply chain sono il DNS poisoning, gli attacchi tramite vettori hardware e le tecniche Golden SAML.

#### Percezione contro realtà: il bias del 9%

Il dato che meglio fotografa la situazione è quello della survey Kaspersky richiamata in apertura. Interrogate sulla classificazione delle minacce per livello di pericolosità, solo il 9% delle organizzazioni globali colloca gli attacchi alla supply chain in cima alla lista; eppure, quando si guarda alla frequenza realmente sperimentata, la stessa categoria raggiunge il 31% delle compromissioni rilevate.

La spiegazione, ha osservato Schifilliti, sta in un bias cognitivo elementare: si tende a sovrastimare ciò che si conosce e a sottostimare ciò che non si conosce a fondo. La conseguenza operativa è grave: l’81% delle organizzazioni che oggi non considera prioritaria questa minaccia, qualora fosse stata compromessa negli ultimi mesi, con ogni probabilità non se ne sarebbe accorta e non avrebbe attivato alcuna contromisura.

#### La timeline 2015-2025 e il posizionamento Gartner

Il decennio 2015-2025 ha disegnato una traiettoria nitida. A partire dal 2017 il numero di campagne supply chain documentate è cresciuto in modo marcato, e la quota attribuibile a gruppi nation-state ha assunto un peso strutturale rispetto a quella *crime* o non attribuita. Le campagne pienamente documentate nel periodo superano la trentina, e il conto esclude il sommerso non attribuito o non disclosurato pubblicamente.

![Francesco Schifilliti, Cyber Crime Conference 2026: software supply chain security, software supply chain, supply chain attack, pipeline software, supply chain security](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_imrgSfJrUE-700x393.png)

*Francesco Schifilliti, Cyber Crime Conference 2026*

Il posizionamento proposto da Gartner nel Threatscape 2025 è altrettanto eloquente: gli attacchi alla supply chain sono collocati al centro della matrice, nella categoria *Threat Advantage*. Si tratta di minacce per le quali esiste già una letteratura tecnica mat...