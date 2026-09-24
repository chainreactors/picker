---
title: IA e dati degli studenti: la catena che il fornitore non copre
url: https://www.ictsecuritymagazine.com/articoli/ia-a-scuola-dati-studenti/
source: ICT Security Magazine
date: 2026-09-23
fetch_date: 2026-09-24T07:08:10.652959
---

# IA e dati degli studenti: la catena che il fornitore non copre

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

![Dati degli studenti tra scuola, sistemi di intelligenza artificiale e infrastrutture digitali, con rischi di conservazione e privacy](https://www.ictsecuritymagazine.com/wp-content/uploads/IA-a-scuola-e-dati-degli-studenti-privacy-ZDR-e-rischi.png)

# IA e dati degli studenti: la catena che il fornitore non copre

A cura di:[Francesco Silvaggio](#molongui-disabled-link)  Ore 23 Settembre 2026

L’uso dell’intelligenza artificiale nelle scuole apre questioni che vanno oltre le policy del fornitore. *No-training*, conservazione e *Zero Data Retention* indicano condizioni diverse, mentre log, cache, backup e servizi collegati possono continuare a conservare dati sensibili. L’articolo analizza responsabilità, controlli e obblighi alla luce del GDPR e delle verifiche del Garante.

## IA nelle scuole: il piano ispettivo del Garante

Con la [deliberazione n. 797 del 30 dicembre 2025](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10214259) il Garante per la protezione dei dati personali ha fissato le priorità ispettive per il periodo gennaio-luglio 2026. Il provvedimento prevede almeno quaranta accertamenti, condotti anche tramite la Guardia di Finanza. Fra le aree indicate compaiono le verifiche sull’utilizzo di strumenti di intelligenza artificiale in ambito scolastico.

L’oggetto di quelle verifiche non è un’astrazione. Con la ripresa delle attività didattiche le scuole producono piani educativi individualizzati, piani didattici personalizzati, verbali del Gruppo di lavoro operativo per l’inclusione, relazioni e profili di funzionamento. Questi documenti contengono dati sulla salute, informazioni sulla disabilità e valutazioni riferite a minori.

## Perché il caso interessa chi fa sicurezza fuori dalla scuola

Lo schema si ripete ovunque. Un professionista incolla un documento riservato in un assistente conversazionale per riscriverlo meglio e più in fretta. Cambia il documento, non il problema: un contratto, una cartella clinica, un fascicolo disciplinare. La scuola è il caso limite, perché somma minori, dati sanitari e un titolare pubblico con risorse tecniche limitate. Le domande da porre al fornitore, però, sono le stesse in ogni settore.

#### Pseudonimizzazione: perché togliere il nome non basta

[Cancellare nome e cognome produce pseudonimizzazione](https://www.ictsecuritymagazine.com/articoli/gdpr-conservazione-e-pseudonimizzazione/), non anonimizzazione. Classe, territorio, diagnosi, date e composizione familiare, combinate fra loro, possono ricondurre al singolo alunno.

Sul piano giuridico la questione è stata precisata dalla Corte di giustizia dell’Unione europea con la [sentenza del 4 settembre 2025, causa C-413/23 P](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:62023CJ0413), GEPD contro Comitato di risoluzione unico (ECLI:EU:C:2025:645). La Corte ha respinto la tesi secondo cui i dati pseudonimizzati sarebbero dati personali in ogni caso e per chiunque. La pseudonimizzazione non entra nella definizione di dato personale: è una misura tecnica e organizzativa che riduce il rischio di correlazione. Per il destinatario, i dati possono perdere carattere personale, ma solo se le misure gli impediscono davvero di risalire all’interessato, anche incrociando altri elementi in suo possesso.

Due passaggi della stessa sentenza contano più del resto per il nostro caso.

Il primo riguarda chi ha eseguito la pseudonimizzazione. Chi conserva le informazioni aggiuntive continua a trattare dati personali, qualunque mascheratura applichi. La scuola conserva sempre quelle informazioni. Per la scuola, quindi, il documento resta un dato personale anche dopo la pulizia del testo.

Il secondo riguarda le opinioni. La Corte afferma che i punti di vista personali, in quanto espressione del pensiero di chi li formula, sono necessariamente connessi a quella persona. Il principio richiama la sentenza Nowak del 20 dicembre 2017, causa C-434/16, sulle correzioni apposte da un esaminatore. Un verbale del GLO o la parte descrittiva di un piano educativo contengono giudizi: sono dati personali dell’alunno e anche di chi li ha scritti.

La conseguenza operativa è netta. La domanda giusta non è se il fornitore riesca a identificare l’alunno. La domanda è se la scuola abbia adempiuto ai propri obblighi verso gli interessati prima di inviare il documento a chiunque.

#### Tre nozioni che vengono confuse: No-training, conservazione e Zero Data Retention

**No-training** significa che, alle condizioni applicabili, contenuti in ingresso e in uscita non alimentano l’addestramento dei modelli. Non dice nulla sulla conservazione.

**Conservazione** riguarda se, dove e per quanto tempo il contenuto resta memorizzato. I cicli cambiano fra conversazioni, file caricati, cache, funzioni con memoria, controlli antiabuso e servizi collegati.

**Zero Data Retention** significa che, nel perimetro approvato e per le funzioni compatibili, il fornitore non conserva il contenuto dopo l’elaborazione. È una condizione contrattuale perimetrata, non un marchio di qualità applicabile all’intero servizio.

La distinzione non è teorica, e per le scuole è già stata tradotta in una prescrizione. Nel [parere n. 454 del...