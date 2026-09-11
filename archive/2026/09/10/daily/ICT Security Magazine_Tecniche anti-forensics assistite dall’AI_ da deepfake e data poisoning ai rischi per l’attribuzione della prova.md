---
title: Tecniche anti-forensics assistite dall’AI: da deepfake e data poisoning ai rischi per l’attribuzione della prova
url: https://www.ictsecuritymagazine.com/articoli/tecniche-anti-forensics/
source: ICT Security Magazine
date: 2026-09-10
fetch_date: 2026-09-11T06:53:07.573401
---

# Tecniche anti-forensics assistite dall’AI: da deepfake e data poisoning ai rischi per l’attribuzione della prova

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

![tecniche anti-forensics: AI e manipolazione di prove digitali, tra data poisoning, deepfake e log alterati.](https://www.ictsecuritymagazine.com/wp-content/uploads/tecniche-anti-forensics.png)

# Tecniche anti-forensics assistite dall’AI: da deepfake e data poisoning ai rischi per l’attribuzione della prova

A cura di:[Cosimo De Pinto](#molongui-disabled-link)  Ore 10 Settembre 202613 Luglio 2026

L’evoluzione dell’intelligenza artificiale sta ridefinendo in modo profondo non solo le capacità di analisi dei dati, ma anche le modalità con cui le informazioni possono essere alterate, simulate o rese indistinguibili dall’autentico. In questo scenario emergono le tecniche anti-forensics assistite dall’AI, che spaziano dal data poisoning alla manipolazione della firma fotografica PRNU, fino ai deepfake e agli evasion attacks, mettendo in crisi la stabilità epistemologica della prova digitale.

Il contributo, che fa parte di una serie dedicata all’impatto dell’intelligenza artificiale sui sistemi probatori e sulle dinamiche del processo penale contemporaneo, analizza le principali categorie di attacchi e manipolazioni, mostrando come l’AI possa essere utilizzata sia per alterare i dati in ingresso ai modelli sia per falsificare log, immagini, contenuti multimediali e output algoritmici. L’obiettivo è evidenziare le implicazioni forensi di queste tecniche e la necessità di approcci probatori fondati su catene di verifica multiple e indipendenti.

## Tecniche anti-forensics assistite dall’AI

*Data poisoning, PRNU manipulation, deepfake ed evasion attacks: l’arsenale operativo dell’anti-forensics assistita dall’AI.*

### Data shaping e data poisoning

Il modellamento del dato (data shaping) consiste nell’alterare il dato prima che venga analizzato, senza renderlo necessariamente sospetto all’occhio umano o agli strumenti tradizionali. [L’avvelenamento del dataset (data poisoning)](https://www.ictsecuritymagazine.com/notizie/adversarial-machine-learning-il-report-del-nist/) colpisce invece i dati di addestramento, aggiornamento o affinamento del modello (fine-tuning), inducendo il sistema ad apprendere correlazioni errate o comportamenti distorti.

Goldblum et al. hanno sistematizzato questa categoria di attacchi in uno studio pubblicato su IEEE Transactions on Pattern Analysis and Machine Intelligence, distinguendo tra avvelenamento della disponibilità, volto a degradare le prestazioni generali, e avvelenamento per inserimento di backdoor, che induce comportamenti malevoli specifici attivabili da un innesco (trigger) predefinito.

Il caso Microsoft Tay (2016), benché non forense in senso stretto, rimane il riferimento emblematico: il chatbot fu ritirato dopo circa sedici ore perché un attacco coordinato sfruttava la sua capacità di apprendimento online per contaminarlo con contenuti offensivi e ideologicamente connotati. Il caso (documentato in un episodio reale) dimostra che un sistema AI può essere compromesso non perché difettoso nella propria architettura, ma perché esposto deliberatamente a un ambiente informativo ostile.

In ambito forense il parallelo è diretto: un modello linguistico impiegato per riassumere, classificare o correlare chat, messaggi di posta elettronica o documenti sequestrati potrebbe incontrare un corpus previamente manipolato con testi orientati, istruzioni ambigue o dati semanticamente falsificati. A ciò si aggiunge [il rischio dell’iniezione di prompt indiretta](https://www.ictsecuritymagazine.com/articoli/ai-digital-forensics-prova/) (indirect prompt injection, IPI): un documento apparentemente innocuo, processato da un sistema AI nell’ambito di un’analisi forense, può contenere istruzioni nascoste capaci di alterare le conclusioni del modello senza lasciare tracce evidenti nei log applicativi ordinari. Per questo la letteratura sulla forensic readiness dei sistemi LLM insiste sull’invocation logging: registrazione strutturata dell’inferenza, con timestamp, identificatori di sessione, prompt completo, contesto utilizzato, parametri rilevanti e output generato.

**Implicazione forense: ogni dato in ingresso a un sistema AI deve essere conservato nella forma grezza originale, autenticato con firma crittografica, sottoposto a controllo delle versioni e mantenuto separato dal dato trasformato. L’output del sistema AI non è mai valutabile in modo autonomo senza conoscere il dataset di partenza, il prompt esatto, il contesto operativo e l’intera catena delle trasformazioni subite dal dato.**

### Costruzione artificiosa dei log: fabbricare una realtà tecnicamente plausibile

Il log crafting consiste nella creazione o manipolazione di registrazioni di sistema formalmente coerenti: sintassi corretta, timestamp credibili, sequenze compatibili, messaggi verosimili. Il rischio specifico è che un sistema AI, addestrato al riconoscimento di pattern statistici, accetti come autentica una sequenza artificiale non perché difettoso, ma perché quella sequenza è stata confezionata per soddisfare esattamente i criteri di validità che il sistema impara a riconoscere.

Il caso Stuxnet rimane il riferimento storico più documentato di manipolazione sistematica della percezione dello stato di un s...