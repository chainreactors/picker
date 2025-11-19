---
title: Cloud forensics: acquisizione delle prove in ambienti multi-tenant e chain of custody nei cloud ibridi
url: https://www.ictsecuritymagazine.com/articoli/cloud-forensics/
source: ICT Security Magazine
date: 2025-11-18
fetch_date: 2025-11-19T03:14:45.859138
---

# Cloud forensics: acquisizione delle prove in ambienti multi-tenant e chain of custody nei cloud ibridi

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

![Illustrazione concettuale della cloud forensics](https://www.ictsecuritymagazine.com/wp-content/uploads/cloud-forensics.jpeg)

# Cloud forensics: acquisizione delle prove in ambienti multi-tenant e chain of custody nei cloud ibridi

A cura di:[Redazione](#molongui-disabled-link)  Ore 18 Novembre 202511 Novembre 2025

La migrazione massiva verso architetture cloud ha ridefinito completamente i paradigmi dell’informatica forense. Se per decenni [la digital forensics](https://www.ictsecuritymagazine.com/articoli/digital-forensics-si-evolve-la-legge-reati-informatici/) si è sviluppata intorno al concetto di acquisizione di dispositivi fisicamente delimitati – hard disk, server on-premise, dispositivi mobili – oggi ci troviamo di fronte a una realtà dove i confini tra evidenze digitali, infrastrutture e giurisdizioni sono diventati labili, quando non del tutto evanescenti.

Il **cloud computing**, nella sua essenza distribuita e virtualizzata, rappresenta molto più di una semplice evoluzione tecnologica: costituisce una rottura epistemologica rispetto ai fondamenti stessi dell’investigazione digitale. La questione non è più “dove si trova la prova”, ma piuttosto “come possiamo garantire l’integrità e l’ammissibilità di un’evidenza che non esiste in un luogo fisico determinabile e che condivide risorse computazionali con centinaia di altri soggetti giuridici?”.

## Multi-tenancy: quando la segregazione logica diventa questione forense

L’architettura **multi-tenant** – pietra angolare dell’efficienza economica del cloud – rappresenta il primo, fondamentale nodo problematico per l’investigatore digitale. In questi ambienti, molteplici entità giuridicamente distinte condividono non solo l’infrastruttura hardware sottostante, ma spesso anche layer applicativi, storage pool e risorse di rete virtualizzate. La segregazione logica sostituisce quella fisica, affidandosi a meccanismi di isolamento implementati via software: *hypervisor*, *container*, policy di accesso, crittografia a livello di tenant.

Dal punto di vista forense, questa condivisione introduce **rischi di contaminazione probatoria** senza precedenti nel mondo on-premise. L’acquisizione di un’immagine forense tradizionale – il *gold standard* della disciplina – diventa tecnicamente impossibile o giuridicamente inammissibile. Come si può procedere al sequestro di un intero *storage array* quando questo contiene simultaneamente dati di decine di organizzazioni, molte delle quali del tutto estranee all’indagine? La risposta ovvia – acquisire solo i dati del tenant sotto investigazione – apre però ulteriori interrogativi sulla completezza dell’evidenza e sulla possibilità di alterazioni.

Il rischio di *cross-contamination* non è meramente teorico. In ambienti virtualizzati, fenomeni di *data bleeding* attraverso cache condivise, *side-channel attacks*, o semplicemente errori di configurazione nelle politiche di isolamento, possono portare a fughe di dati tra tenant. Per l’investigatore, verificare l’assenza di tali contaminazioni richiede una comprensione profonda dell’architettura del cloud service provider, informazioni che raramente sono accessibili per ragioni di sicurezza e segreto industriale.

Come evidenziato nella letteratura specialistica su [cloud computing forensics](https://www.ictsecuritymagazine.com/pubblicazioni/cloud-computing-forensics-peculiarita-e-indicazioni-metodologiche/), le criticità dovute alla volatilità delle risorse virtualizzate e all’inaccessibilità delle risorse fisiche rappresentano ostacoli significativi per qualsiasi indagine digitale.

## La catena di custodia nel paradigma ibrido: continuità o fiction giuridica?

Se il multi-tenant complica l’acquisizione, gli **ambienti cloud ibridi** mettono in crisi il concetto stesso di *chain of custody*. La catena di custodia – principio cardine dell’ammissibilità probatoria – presuppone la capacità di documentare ogni passaggio della prova, dalla sua acquisizione fino alla sua presentazione in sede giudiziaria, garantendo che non vi siano state alterazioni, sostituzioni o manipolazioni.

In un ambiente ibrido, dove i dati migrano dinamicamente tra infrastrutture on-premise, cloud privati e cloud pubblici, spesso attraversando molteplici giurisdizioni nel corso di normali operazioni business, questa documentazione diventa straordinariamente complessa. Un file oggetto di indagine potrebbe essere stato creato in un data center aziendale in Italia, replicato automaticamente in un cloud storage AWS situato in Irlanda per ragioni di *business continuity*, processato da un servizio di analytics ospitato su Google Cloud in Belgio, e infine archiviato in forma compressa su Azure negli Stati Uniti, il tutto nell’arco di poche ore e senza alcun intervento umano.

Ciascun “salto” in questa catena rappresenta un **potenziale punto di rottura forense**. Come garantire che i *timestamp* siano affidabili quando attraversano *time zone* e sistemi con clock potenzialmente non sincronizzati? Come documentare le trasformazioni che il dato subisce – compressione, crittografia, de-duplicazione – mantenendo la possibilità di risalire alla forma originale? Come tracciare chi ha avuto accesso al dato quando i log sono anch’essi distribuiti tra sistemi diversi, gestiti da fornitori diver...