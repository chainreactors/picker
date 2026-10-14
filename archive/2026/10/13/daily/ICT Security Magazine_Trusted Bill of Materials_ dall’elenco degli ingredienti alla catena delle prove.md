---
title: Trusted Bill of Materials: dall’elenco degli ingredienti alla catena delle prove
url: https://www.ictsecuritymagazine.com/articoli/trusted-bill-of-materials/
source: ICT Security Magazine
date: 2026-10-13
fetch_date: 2026-10-14T06:53:15.975053
---

# Trusted Bill of Materials: dall’elenco degli ingredienti alla catena delle prove

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

![Trusted Bill of Materials dall'elenco degli ingredienti alla catena delle prove_Catena di verifica digitale protetta, Horizon Europe RESCALE](https://www.ictsecuritymagazine.com/wp-content/uploads/Trusted-Bill-of-Materials-dallelenco-degli-ingredienti-alla-catena-delle-prove_Catena-di-verifica-digitale-protetta.png)

# Trusted Bill of Materials: dall’elenco degli ingredienti alla catena delle prove

A cura di:[Alessandro Visintin](#molongui-disabled-link)  Ore 13 Ottobre 202613 Ottobre 2026

*Un SBOM dice quali componenti ci sono dentro un prodotto, non se siano stati verificati. Il progetto Horizon Europe RESCALE ha lavorato su un artefatto che prova entrambe le cose: il Trusted Bill of Materials.*

## Il deficit di fiducia nelle supply chain digitali

Da SolarWinds a Log4j, lo schema è sempre lo stesso: una singola dipendenza compromessa, annidata in profondità in un grafo di dipendenze transitive, si propaga a migliaia di sistemi a valle. Il software moderno viene assemblato a partire da centinaia di librerie open source, immagini firmware e componenti hardware forniti da terzi, ciascuno con un profilo di rischio opaco. La postura di sicurezza di un’organizzazione è solida solo quanto l’anello meno visibile della sua catena di fornitura, come mostrano le campagne che negli ultimi anni hanno preso di mira i registri pubblici [npm e PyPI](https://www.ictsecuritymagazine.com/articoli/supply-chain-software/).

Eppure l’[SBOM](https://www.ictsecuritymagazine.com/articoli/sbom/), di per sé, non è sufficiente rispetto ai requisiti di assurance che stanno entrando nei testi normativi. Elenca cosa c’è all’interno di un prodotto software, ma non dice se quei componenti siano stati testati, se le prove siano verificabili o se restino sicuri man mano che emergono nuove vulnerabilità. Questo scarto genera un deficit di fiducia: le organizzazioni possono risultare conformi agli obblighi di trasparenza senza disporre di prove crittograficamente verificabili della solidità della propria supply chain.

Il progetto RESCALE (Revolutionised Enhanced Supply Chain Automation with Limited Threats Exposure) affronta proprio questo deficit, trasformando trasparenza e assurance in un unico artefatto continuamente validato: il Trusted Bill of Materials (TBOM). Si tratta di un’azione di ricerca e innovazione finanziata dal programma Horizon Europe, con un costo complessivo di 4.998.250 euro, avviata il 1° ottobre 2023 e [conclusa il 30 settembre 2026](https://cordis.europa.eu/project/id/101120962), coordinata dall’Athena Research Center di Atene con un consorzio misto di enti di ricerca e partner industriali.

> **Nota della redazione** Il Trusted Bill of Materials descritto in questo articolo è un concetto sviluppato in ambito di ricerca dal progetto RESCALE, concluso il 30 settembre 2026. Non costituisce uno standard né uno strumento di conformità formalmente riconosciuto dalle autorità: gli obblighi in materia di distinta base del software restano quelli fissati dal Cyber Resilience Act e dalla direttiva NIS2. Le valutazioni sull’efficacia della piattaforma sono del consorzio di progetto e non sono state verificate in modo indipendente dalla redazione.

## Il quadro normativo: CRA, NIS2 e il cambio di rotta statunitense

I regolatori hanno reagito con urgenza. Il [Cyber Resilience Act](https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=CELEX%3A32024R2847) (Regolamento UE 2024/2847), adottato nel 2024, obbliga i produttori di prodotti con elementi digitali a redigere e tenere aggiornata una distinta base del software in formato leggibile da dispositivo automatico, che copra almeno le dipendenze di primo livello del prodotto. La distinta non va pubblicata: va messa a disposizione delle autorità di vigilanza del mercato solo a seguito di una richiesta motivata.

I produttori devono inoltre garantire la gestione delle vulnerabilità per un periodo di assistenza di almeno cinque anni, o pari alla durata di utilizzo prevista se inferiore, come stabilito dall’articolo 13, paragrafo 8. Le obbligazioni principali del regolamento decorrono dall’11 dicembre 2027. L’obbligo di segnalazione è invece già operativo: dall’11 settembre 2026 i fabbricanti devono notificare le vulnerabilità sfruttate attivamente e gli incidenti gravi, con un preallarme entro 24 ore e una notifica completa entro 72, attraverso la [Single Reporting Platform gestita da ENISA](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting).

La direttiva NIS2 richiede ai soggetti essenziali e importanti di adottare misure di [gestione del rischio legate ai fornitori](https://www.ictsecuritymagazine.com/notizie/third-party-risk-management/). In Italia il recepimento è avvenuto con il D.Lgs. 138/2024, che estende tali obblighi a una platea più ampia di operatori nazionali. Parallelamente, l’applicazione del CRA inciderà sui produttori italiani di dispositivi embedded e IoT, spingendoli ad adottare processi rigorosi di tracciabilità dei componenti.

Negli Stati Uniti la direzione è opposta. L’Executive Order 14028 del 2021 aveva introdotto requisiti SBOM per gli acquisti federali, ma l’EO 14306 e il memorandum OMB M-26-05 ne hanno smantellato l’impianto att...