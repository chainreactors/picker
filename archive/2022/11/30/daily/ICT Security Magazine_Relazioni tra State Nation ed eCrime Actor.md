---
title: Relazioni tra State Nation ed eCrime Actor
url: https://www.ictsecuritymagazine.com/articoli/relazioni-tra-state-nation-ed-ecrime-actor/
source: ICT Security Magazine
date: 2022-11-30
fetch_date: 2025-10-04T00:08:23.951264
---

# Relazioni tra State Nation ed eCrime Actor

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

![Distinzione tra eCrime Actor e Nation State Threat Actor: sfide di attribution, false flag e convergenza tra cybercrime e spionaggio.](https://www.ictsecuritymagazine.com/wp-content/uploads/eCrime-Actors.jpg)

# Relazioni tra Nation State ed eCrime Actor

A cura di:[Francesco Schifilliti](#molongui-disabled-link)  Ore 29 Novembre 202223 Settembre 2025

Nel panorama della cyber threat intelligence, distinguere con precisione tra un eCrime Actor e un Nation State Threat Actor rappresenta una delle sfide più complesse per gli analisti. L’attribuzione di un attacco informatico, infatti, non è mai un processo lineare: richiede la valutazione di tattiche, tecniche, procedure (TTP) e, soprattutto, delle connessioni sempre più sfumate tra criminalità informatica organizzata e attività sponsorizzate da governi.

Negli ultimi anni, i confini tra cybercrime a scopo di lucro e operazioni di spionaggio statale si sono progressivamente assottigliati. Gruppi eCrime sfruttano strumenti e risorse tipici degli attori statali, mentre i Nation State Threat Actor utilizzano ransomware e altre tecniche criminali come copertura per operazioni di intelligence e sabotaggio. Questa convergenza rende l’analisi delle minacce ancora più complessa e strategicamente rilevante per imprese, istituzioni e governi.

In questo articolo verranno approfondite le principali categorie di threat actor, le difficoltà legate al processo di attribution e gli scenari in cui le linee di confine tra eCrime e Nation State diventano sempre più difficili da distinguere.

### Sinossi

Per gli analisti d’intelligence, l’identificazione degli avversari responsabili di un attacco informatico è sempre stata un’attività molto impegnativa. In questo articolo si vogliono sinteticamente affrontare gli aspetti di complessità connaturati alla fase di *attribution* e, soprattutto, i punti di connessioni sempre più frequenti tra i gruppi *Nation* *State* e quelli *eCrime.*

### Principale categorizzazione degli avversari (Threat Actor)

Al fine di rendere più chiara la trattazione dell’argomento di questo articolo, è fondamentale introdurre le principali categorie utilizzate. Per categorizzare i Threat Actor responsabili degli attacchi informatici. La categorizzazione utilizzata è quella impiegata anche nel *MISP Galaxy*:

**NATION STATES**: entità che lavorano per il governo o i militari di uno Stato o che operano sotto la loro direzione. Questi attori hanno in genere accesso a supporto, risorse, formazione e strumenti significativi e sono in grado di progettare ed eseguire campagne molto sofisticati ed efficaci.

* Obiettivo principale: spionaggio, furto o qualsiasi altra attività che favorisca gli interessi di un particolare gruppo nazionale
* Obiettivi tipici: Aziende ed organizzazioni governative

**eCRIME**: un’organizzazione (anche individuale) in grado di condurre un’attività criminale significativa e su larga scala a scopo di lucro. L’eCrime (o Criminalità Organizzata) è generalmente costituito da gruppi di grandi dimensioni e dotati di buone risorse che operano per trarre profitto da tutti i tipi di crimini informatici. Il furto di proprietà intellettuale, l’estorsione tramite ransomware e la distruzione fisica sono esempi comuni.

* Obiettivo principale: Guadagno economico
* Obiettivi tipici: Organizzazioni e aziende ricche di denaro e/o di dati

**HACKTIVIST**: sostenitori, altamente motivati e potenzialmente distruttivi, di cause sociali (ad esempio, commercio, lavoro, ambiente, ecc.) o di ambiti politici che tenta di annientare il modello di business di un’organizzazione o di danneggiarne l’immagine. Questa categoria comprende attori talvolta definiti anarchici, vandali informatici ed estremisti.

* Obiettivo principale: svelare segreti e distruggere servizi/organizzazioni percepiti come malvagi
* Obiettivi tipici: Non limitati a un tipo specifico di organizzazione o azienda

**INDIVIDUALS**: un individuo che tende a penetrare nelle reti per il brivido del rischio o come gesto di sfida. Gli hacker possono avere competenze avanzate o utilizzare semplici script di attacco scaricati da sorgenti pubbliche. Tra gli individuals ci sono anche insider non ostili che espongono involontariamente l’organizzazione a un danno. In questo contesto, il termine “insider” comprende qualsiasi persona, interna all’organizzazione, che goda di una fiducia estesa, come dipendenti regolari, appaltatori, consulenti e lavoratori temporanei.

* Obiettivo principale: Lavorare dall’interno di un’organizzazione per aggirare la sua struttura di cyber security
* Obiettivi tipici: : Non limitati a nessun tipo specifico di organizzazione

Tra gli avversari appena elencati, quelli di maggiore interesse sono i gruppi Nation States e eCrime. Mentre gli obiettivi dei gruppi eCrime sono sempre di natura utilitaristica, i gruppi Nation States possono essere contraddistinti anche sulla base del coinvolgimento degli Stati negli attacchi.

Lo spettro delle responsabilità di uno Stato è uno strumento che può aiutare gli analisti, con conoscenze limitate, ad assegnare la paternità di un particolare attacco (o di campagne di attacchi) con maggiore precisione e trasparenza. Lo spettro attribuisce dieci categorie, ciascuna contrassegnata da un diverso grado di responsabilità, a seco...