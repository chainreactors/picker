---
title: IEC 62443: la sicurezza industriale non è l’informatica trapiantata in fabbrica
url: https://www.ictsecuritymagazine.com/industrial-cyber-security/iec-62443-sicurezza-ot/
source: ICT Security Magazine
date: 2026-06-25
fetch_date: 2026-06-26T06:09:36.539516
---

# IEC 62443: la sicurezza industriale non è l’informatica trapiantata in fabbrica

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/IEC-62443.png)

# IEC 62443: la sicurezza industriale non è l’informatica trapiantata in fabbrica

A cura di:[Redazione](#molongui-disabled-link)  Ore 25 Giugno 20269 Giugno 2026

IEC 62443 è lo standard internazionale per la sicurezza dei sistemi di automazione e controllo industriale, e nasce da una constatazione che chi viene dall’informatica tende a sottovalutare: la tecnologia operativa, l’OT che governa turbine, linee di produzione, impianti idrici e reti elettriche, non è informatica con qualche peculiarità in più. È un mondo diverso, con priorità diverse, in cui le abitudini consolidate della sicurezza informatica non solo non bastano, ma a volte fanno danni. Applicare un aggiornamento che riavvia un server, in un ufficio, è routine; farlo su un controllore che regola un processo fisico può fermare la produzione o, nei casi peggiori, mettere a rischio l’incolumità delle persone.

Il punto di partenza dello standard è proprio questo ribaltamento delle priorità. Nella sicurezza informatica tradizionale la riservatezza viene prima di tutto: si protegge anzitutto il dato dallo sguardo altrui. Nell’OT l’ordine si capovolge, e al primo posto stanno la disponibilità e la sicurezza fisica, perché un impianto che si ferma o un processo che esce di controllo hanno conseguenze immediate e materiali. IEC 62443 ne prende atto, e lo fa nel modo più concreto: tratta la disponibilità come un requisito fondamentale a sé stante e deriva i propri controlli dalle esigenze dell’OT, non dalle consuetudini dell’ufficio. È questo a renderlo il riferimento per chi deve mettere in sicurezza la fabbrica senza romperla.

## Perché l’OT non è l’informatica

La distanza tra i due mondi è fatta di vincoli concreti. I sistemi industriali hanno cicli di vita lunghissimi: macchinari e controllori installati dieci o vent’anni fa sono ancora in produzione, spesso basati su software che non riceve più aggiornamenti e che non si può sostituire senza fermare l’impianto. Molti non sono stati progettati per la sicurezza, parlano protocolli nati per reti chiuse e fidate, e non prevedono nulla che somigli a un’autenticazione robusta. La possibilità di applicare patch è limitata, perché ogni intervento va programmato dentro finestre di fermo rare e costose, e a volte non è proprio praticabile.

In questo contesto, copiare i controlli dell’informatica sull’OT fallisce in due modi: o non si applicano, perché i sistemi non li supportano, o si applicano e interferiscono con il processo, violando proprio quella disponibilità che è la priorità numero uno. IEC 62443 prende atto di questi limiti invece di ignorarli. Non chiede di rendere l’OT identico all’IT, ma offre un metodo per proteggerlo alle sue condizioni, accettando che un sistema non sempre si possa aggiornare e che la continuità del processo non sia negoziabile.

## Zone e condotti: segmentare il mondo fisico

Il primo strumento dello standard è una logica di segmentazione pensata per l’industria. L’ambiente viene diviso in zone, gruppi di sistemi e componenti che condividono gli stessi requisiti di sicurezza per funzione e criticità, e le comunicazioni tra una zona e l’altra passano per condotti, canali controllati in cui si decide cosa può transitare. È la traduzione industriale del principio per cui una violazione in un punto non deve propagarsi al resto: se un’area meno critica viene compromessa, i condotti impediscono all’attaccante di raggiungere facilmente la sala di controllo o i sistemi che governano il processo.

Questa [segmentazione](https://www.ictsecuritymagazine.com/articoli/network-segmentation/) ha un valore particolare al confine tra l’informatica e l’OT, il punto dove le due reti si incontrano e dove storicamente sono passati molti attacchi: trattare quel confine come un condotto sorvegliato, e non come un passaggio aperto, è una delle mosse più efficaci. La convergenza tra IT e OT, spinta dalla digitalizzazione degli impianti, ha reso questo principio ancora più urgente, perché ha collegato sistemi un tempo isolati a reti raggiungibili dall’esterno.

## IEC 62443 misura la sicurezza per livelli, non per assoluti

Il secondo contributo dello standard è un modo pragmatico di stabilire quanta sicurezza serve, zona per zona. Invece di pretendere il massimo ovunque, cosa impossibile e controproducente in ambienti così vincolati, IEC 62443 definisce quattro livelli di sicurezza crescenti, dal primo, che protegge dagli errori involontari, fino al quarto, che difende da avversari sofisticati, molto motivati e dotati di risorse ingenti. A ogni zona si assegna un livello obiettivo in base al rischio e alle conseguenze di un suo cedimento, si verifica quale livello i componenti sono effettivamente in grado di garantire, e si misura quello davvero raggiunto: la distanza tra obiettivo e realtà diventa il programma di lavoro.

A dare struttura a questa misura ci sono i sette requisiti fondamentali su cui lo standard articola la sicurezza, una sorta di griglia delle dimensioni da presidiare.

### I sette requisiti fondamentali

Sono il controllo dell’identificazione e dell’autenticazione, il controllo dell’uso, l’in...