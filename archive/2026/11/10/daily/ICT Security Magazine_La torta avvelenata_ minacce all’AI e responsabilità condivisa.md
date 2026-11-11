---
title: La torta avvelenata: minacce all’AI e responsabilità condivisa
url: https://www.ictsecuritymagazine.com/articoli/torta-avvelenata-minacce-ai-responsabilita-condivisa/
source: ICT Security Magazine
date: 2026-11-10
fetch_date: 2026-11-11T08:35:28.291130
---

# La torta avvelenata: minacce all’AI e responsabilità condivisa

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.354 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

  Minacce e attacchi

  + [Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)

  Rischio, norme e privacy

  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)

  Tecnologie

  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)

  Scenari

  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)

  Ultimi in **Cyber Security**

  [Tutti gli articoli di Cyber Security →](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Approfondimenti](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* [Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Eventi ↗](https://eventi.ictsecuritymagazine.com/)

[Newsletter](/newsletter/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca

Attiva/disattiva menu

[Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)Contenuto sponsorizzato

# La torta avvelenata: minacce all’AI e responsabilità condivisa

Cinque strati, dall’energia alle applicazioni, per localizzare le minacce all’AI. Incrociati con API, GPU a noleggio e on-prem, mostrano come si ripartisce la responsabilità condivisa.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il10 Novembre 202610 Novembre 2026  Condividi

![La torta avvelenata: minacce all’AI e responsabilità condivisa: Fetta di torta a cinque strati tecnologici con uno strato che brilla di rosso, su sfondo blu notte e circuiti luminosi](https://www.ictsecuritymagazine.com/wp-content/uploads/torta-avvelenata-minacce-ai-responsabilita-condivisa-4.webp)

In sintesi

* Le minacce all’AI non stanno solo nel prompt: l’autore le colloca in cinque strati, dall’energia alle applicazioni.
* Incrociando gli strati con API, GPU a noleggio e on-prem, la matrice mostra cosa presidiare, cosa governare con i fornitori e cosa è condiviso.
* L’autore propone tre passi: censire i servizi AI, assegnare le responsabilità per strato e definire con una matrice RACI le celle condivise.

*Un modello a strati per le minacce all’AI e la gestione della responsabilità condivisa*

Gran parte dei framework di sicurezza per l’AI si concentra sul livello applicativo: prompt, agenti e output dei modelli. Eppure l’AI moderna poggia su uno stack fisico e industriale fatto di energia, silicio, infrastruttura e modelli, ciascuno con le proprie caratteristiche e vulnerabilità.

Questo articolo sostiene due tesi. La prima è che la “torta a cinque strati” (energia, chip, infrastruttura, modelli, applicazioni) è uno schema pratico per localizzare le minacce all’AI, perché dà a ogni rischio un indirizzo e rende visibile come i guasti in basso nello stack si propaghino verso l’alto.

La seconda è che lo stesso schema, incrociato con i tre modi più comuni di usare l’AI (API, GPU a noleggio, on-prem), mostra quali rischi un’organizzazione deve presidiare direttamente, quali può solo governare attraverso i fornitori e dove la responsabilità è condivisa.

Per ogni strato descriviamo il contesto di mercato ed individuiamo minacce prioritarie (motivate anche attraverso incidenti documentati). Leggiamo poi la matrice di responsabilità che ne risulta alla luce della normativa europea (AI Act, NIS2 e DORA) e chiudiamo con tre passi pratici.

## Introduzione

Nel panorama della analisi sulla sicurezza dell’AI, la vasta maggioranza dei framework si concentra sul livello applicativo e, in misura minore, sul modello. Ciò trova giustificazione se si considera che il meccanismo di fruizione dei modelli di frontiera è essenzialmente legato all’uso di GUI o API o similari; tutto ciò che sta sotto l’applicazione è un problema del provider.

Due forze stanno ora spingendo a far girare modelli propri su infrastrutture noleggiate o di proprietà, specialmente in area europea.

**La prima è il costo:** il prezzo per token continua a scendere, ma gli agenti consumano molti più token per task. Gartner per esempio prevede che il costo di inferenza per workflow agentico aumenterà di oltre cinque volte entro il 2028 [[1]](https://www.ictsecuritymagazine.com/articoli/torta-avvelenata-minacce-ai-responsabilita-condivisa/#ref-1).

**La seconda è la sovranità:** GDPR, DORA e NIS2 rendono verificabili la localizzazione dei dati e il controllo sui fornitori, e per un modello che tratta dati dei clienti è molto più semplice dimostrare dove si trovano i dati, e chi può raggiungerli, su un’infrastruttura che si controlla direttamente.

Questi driver spingono per una strategia di consumo dei servizi AI dove il vecchio modello verrà affiancato dagli approcci “on-prem” o “GPU rented” per la gestione dei dati sensibili e più strategici per l’organizzazione.

Tali considerazioni sollevano due domande, alle quali il presente articolo tenta di dare risposta: dove si trovano davvero le minacce all’AI lungo l’intero stack? E, per un dato modo di usare l’AI, chi ha la responsabilità di mitigare i rischi derivanti da tali minacce?

## Un modello a strati del rischio AI

Il CEO di NVIDIA, Jensen Huang, ha descritto l’industria dell’AI come una torta a cinque strati. L’intenzione originale della metafora era indirizzato a sottolineare la rilevanza industriale dell’evoluzione dell’intelligenza artificiale, e come essa non si limiti al puro livello applicativo.

Riteniamo che tale visualizzazione sia utile anche per discutere di sicurezza e rischio AI; pertanto la adotteremo come schema analitico, con gli strati numerati dal basso:

![Tabella dei cinque strati dello stack AI, da Energia (strato 0) ad Applicazioni (strato 4), con ambito ed esposizione caratteristica di ciascuno](https://www.ictsecuritymagazine.com/wp-content/uploads/torta-avvelenata-tabella-cinque-strati-700x396.webp)

Lo schema dà un indirizzo a ogni minaccia, obbligando il threat model a considerare strati che altrimenti ignorerebbe, e rende esplicito che dipendenza ed impatti vanno dal basso verso l’alto.

Per ogni strato descriviamo brevemente il contesto e selezioniamo tre minacce che siano specifiche dell’AI, o da essa amplificate, e su cui un’organ...