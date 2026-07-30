---
title: AI-BOM: l’AI Bill of Materials per sapere che cosa c’è dentro un modello
url: https://www.ictsecuritymagazine.com/articoli/ai-bom-ai-bill-of-materials/
source: ICT Security Magazine
date: 2026-07-29
fetch_date: 2026-07-30T04:52:24.463517
---

# AI-BOM: l’AI Bill of Materials per sapere che cosa c’è dentro un modello

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

![AI-BOM Artificial Intelligence Bill of Materials AI Bill of Materials](https://www.ictsecuritymagazine.com/wp-content/uploads/AI-BOM-Artificial-Intelligence-Bill-of-Materials-AI-Bill-of-Materials.png)

# AI-BOM: l’AI Bill of Materials per sapere che cosa c’è dentro un modello

A cura di:[Redazione](#molongui-disabled-link)  Ore 29 Luglio 202617 Luglio 2026

L’AI-BOM, sigla di AI Bill of Materials, porta al mondo dei modelli di intelligenza artificiale un’idea già rodata nel software: sapere di che cosa è fatto ciò che si usa. Come la distinta base di un prodotto industriale elenca i suoi componenti, e come il [Software Bill of Materials](https://www.ictsecuritymagazine.com/articoli/software-bill-of-materials/) elenca le librerie di cui un programma è composto, l’AI-BOM elenca gli ingredienti di un sistema di intelligenza artificiale: i modelli, i dataset con cui sono stati addestrati, i pesi, le configurazioni, le licenze e la provenienza. È l’inventario di una cosa che, fino a ieri, quasi nessuno inventariava, perché la si trattava come una scatola nera calata dall’alto.

La differenza rispetto al software tradizionale è che qui gli ingredienti sono molto più opachi e molto meno verificabili, e il bisogno di elencarli è cresciuto insieme alla loro diffusione: nel momento in cui le aziende scaricano modelli da repository pubblici e li innestano nei propri prodotti, ereditano rischi che non sanno di avere. L’AI-BOM è la prima mossa per riprenderne il controllo, ma è anche una mossa che risolve meno di quanto sembri, perché con i modelli la parte difficile comincia proprio dove finisce l’elenco.

## Che cos’è un AI-BOM

Un AI-BOM, o AI Bill of Materials, è l’inventario strutturato e leggibile dalle macchine dei componenti di un sistema di intelligenza artificiale. Non elenca soltanto il modello, ma la costellazione che lo circonda: i dataset di addestramento e la loro origine, i pesi e la loro versione, l’architettura e gli iperparametri, le licenze d’uso, le metriche dichiarate e i limiti noti, fino alle considerazioni etiche e ai rischi di distorsione. È l’estensione al mondo dell’AI della stessa logica di trasparenza che ha portato il software a dotarsi di distinte dei materiali, applicata però a oggetti fatti non di codice ma di dati e di numeri.

Gli standard esistono già, e non sono nuovi di zecca. [CycloneDX](https://cyclonedx.org/capabilities/mlbom/), progetto di punta di OWASP oggi sviluppato in seno al comitato tecnico TC54 di Ecma International, ha introdotto il bill of materials per il machine learning con la versione 1.5 del 2023 e lo ha portato dentro uno standard internazionale: la versione 1.7, di ottobre 2025, è stata ratificata come ECMA-424 di seconda edizione, che copre esplicitamente la descrizione dei modelli di machine learning, nella terminologia del progetto l’AI/ML-BOM. Sul fronte parallelo, lo standard [SPDX 3.0](https://www.ictsecuritymagazine.com/articoli/spdx-3-0/) del 2024 ha aggiunto profili dedicati all’intelligenza artificiale e ai dataset, pensati proprio per documentare un sistema di AI e i dati che lo alimentano. Come per l’SBOM, quindi, l’AI-BOM non è un formato proprietario ma una grammatica comune, con cui descrivere un modello, generarne l’inventario e scambiarlo lungo la filiera.

## Che cosa cambia quando il componente è un modello

Qui però la somiglianza con l’SBOM si ferma, ed è la parte che conta. In un software tradizionale le dipendenze sono librerie di cui, in linea di principio, si può leggere il codice: se un componente è vulnerabile, lo si identifica, lo si ispeziona, lo si aggiorna. Un modello è un’altra cosa. Il suo equivalente del codice sorgente è il dato con cui è stato addestrato, che quasi mai viaggia insieme al modello e spesso non è nemmeno pubblico; e ciò che si scarica, i pesi, è una distesa di miliardi di numeri che nessun essere umano può leggere, ispezionare riga per riga o “diffare” per capire che cosa è cambiato tra due versioni.

La conseguenza è che l’AI-BOM elenca ciò che si possiede, ma non può rivelare ciò che si nasconde nel modello. Una backdoor addestrata dentro i pesi, una distorsione ereditata da un dataset avvelenato, un comportamento indesiderato che emerge solo con certi input non compaiono in nessuna distinta: restano invisibili proprio perché il modello è opaco per costruzione. A questo si aggiunge un problema che il software conosce meno, quello del formato: molti modelli viaggiano in formati di serializzazione, come il pickle di Python, che all’atto del caricamento eseguono codice, trasformando il semplice “aprire un modello” in un potenziale punto di esecuzione. Un formato più sicuro esiste già, il safetensors nato in casa Hugging Face proprio per contenere solo i dati del modello e non codice eseguibile, ma l’ecosistema non lo ha ancora sostituito, e la piattaforma segnala i modelli in pickle come non sicuri senza però bloccarli. La provenienza, poi, non si deduce dal file: un modello scaricato da un repository pubblico non porta con sé la garanzia di essere quello che dichiara di essere. L’inventario è la premessa per porsi queste domande, non la risposta.

## La supply chain dei modelli e perché va inventari...