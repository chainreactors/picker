---
title: Il rilevamento del GPS spoofing nei droni
url: https://www.ictsecuritymagazine.com/articoli/gps-spoofing-nei-droni/
source: ICT Security Magazine
date: 2024-11-19
fetch_date: 2025-10-06T19:20:48.925972
---

# Il rilevamento del GPS spoofing nei droni

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
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![GPS spoofing nei droni](https://www.ictsecuritymagazine.com/wp-content/uploads/GPS-spoofing-nei-droni.jpg)

# Il rilevamento del GPS spoofing nei droni

A cura di:[Fabrizio D'Amore](#molongui-disabled-link)  Ore 18 Novembre 202425 Novembre 2024

Il controllo di un UAV (*Unmanned Aerial Vehicle*[[1]](#_ftn1), cioè velivolo senza pilota umano a bordo) rappresenta una sfida tecnologica apparentemente gestibile e alla portata di un pubblico sempre più esteso; se non fosse soggetto ad attacchi di *GPS spoofing*, che hanno il potere di alterare la percezione dell’UAV in merito al posizionamento corrente.

Si capisce che l’effetto di tale pratica può essere spiacevole, fino a divenire devastante nei casi di velivoli ad uso militare. In questo articolo ci occuperemo di alcune possibilità di rilevare lo *spoofing*, in maniera che si possano prendere misure di contrasto, almeno per evitare effetti drastici conseguenti a queste tipologie di attacchi.

## UAV e droni

I termini “UAV” e “droni” oggi sono usati praticamente come sinonimi.[[2]](#_ftn2)

In realtà, mentre “UAV” è usato soprattutto in ambienti militari, “drone” viene utilizzato nell’ambito di applicazioni civili come la fotografia, l’esplorazione, l’agricoltura, la manutenzione di opere stradali e ferroviarie o le attività ricreative; e si tratta, in genere, di velivoli a pilotaggio remoto.

Il termine più tecnico (“UAV”) descrive invece l’assenza di un pilota umano a bordo. Si usano, in effetti, vari acronimi: *Unmanned Aircraft System* (UAS) sta ad indicare un intero sistema, composto non solo dal velivolo ma anche da una stazione di controllo e da un collegamento per la comunicazione tra questa e il velivolo. La statunitense FAA (Federal Aviation Administration, agenzia federale del Dipartimento dei Trasporti, che si occupa dell’aviazione civile) ha introdotto il termine UA per indicare un aeromobile senza pilota. Le regole della FAA richiedono che in un UAS ci sia un pilota in comando remoto (RPIC), o un osservatore visivo, che sia in grado di vedere il velivolo in ogni momento mentre l’aereo è in volo.

Spesso si usa la sigla “RPAV” (*Remotely Piloted Aerial Vehicle*), in italiano SAPR (Sistema Aeromobile a Pilotaggio Remoto[[3]](#_ftn3),[[4]](#_ftn4), ambito regolato dall’ENAC[[5]](#_ftn5) ma divenuto obsoleto dopo l’emissione del regolamento UAS-IT[[6]](#_ftn6)). A rendere più confuso lo scenario ci sono i termini UAVS e RPAS, ove la lettera S descrive il sistema, come già detto per gli UAS.

Precisiamo che gli UAV possono essere a guida completamente autonoma (se fanno uso di sensori e di una logica autonoma) o semi-autonoma (il velivolo funziona utilizzando sensori, un sistema di controllo a terra e una programmazione software specifica). Merita una menzione a parte la sottocategoria FPV (*First-Person View*) in cui il pilota remoto vede ciò che è visibile dal drone.[[7]](#_ftn7) Naturalmente è un caso speciale di UAS.

È ancora dubbio se un velivolo a pilotaggio remoto possa essere chiamato UAV o meno: in letteratura ci sono indicazioni contrastanti al riguardo[[8]](#_ftn8),[[9]](#_ftn9).

Esistono numerose altre sigle[[10]](#_ftn10) ma non si tratta di una questione rilevante ai fini della presente analisi. La letteratura sul tema è piuttosto ricca.[[11]](#_ftn11)

![GPS spoofing nei droni. GPS spoofing](https://www.ictsecuritymagazine.com/wp-content/uploads/image1-1-700x700.jpg)

Figura 1. Drone usato per l’ispezione di uno scomodo viadotto autostradale.

## Navigazione satellitare

Da parecchi anni è disponibile la navigazione satellitare, che supporta la localizzazione nel tempo e nello spazio di molti operatori; negli ultimi anni, grazie alla diffusione di smartphone e tablet, è utilizzata anche dal grande pubblico.

Tecnicamente si tratta di satelliti orbitanti che forniscono informazioni per il geoposizionamento; se la copertura è globale si parla di GNSS (*Global Navigation Satellite Systems*), mentre se è regionale si usa RNSS (*Regional Navigation Satellite Systems*).

I sistemi globali sono attualmente quattro: GPS (statunitense), GLONASS (russo), BDS (cinese) e Galileo (europeo). Il funzionamento del GNSS si basa su alcuni principi fisici che qui non discuteremo[[12]](#_ftn12), limitandoci a osservare come il più diffuso sia sicuramente il GPS. In tutti i casi è prevista la messa a punto di un dispositivo di ricezione che riceve segnali dai satelliti per determinare la posizione. Da qui, due conseguenze pratiche: non c’è ricezione di segnale satellitare in un ambiente *indoor*[[13]](#_ftn13); la diffusa convinzione per cui un ricevitore è anche in grado di comunicare la posizione è errata, occorrendo, oltre al ricevitore, un trasmettitore.

Di seguito faremo riferimento al GPS, il più noto fra i GNSS; tuttavia, quanto discusso vale, in linea di principio, per tutti gli altri sistemi di navigazione satellitare.

## Lo Spoofing e i suoi effetti

![GPS spoofing: Illustrazione del GPS spoofing](https://www.ictsecuritymagazine.com/wp-content/uploads/image3-1-700x700.jpg)

Figura 2. Illustrazione suggestiva del GPS spoofing

Il termine *spoofing* è usato in numerosi scenari differenti: tutti hanno in comune l’idea di un attaccante che falsifica l’identità per ottenere un vantaggio illegittimo. Può avvenire nell’email, nel...