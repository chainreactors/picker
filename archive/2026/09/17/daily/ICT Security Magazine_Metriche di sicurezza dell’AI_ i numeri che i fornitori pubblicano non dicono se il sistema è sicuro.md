---
title: Metriche di sicurezza dell’AI: i numeri che i fornitori pubblicano non dicono se il sistema è sicuro
url: https://www.ictsecuritymagazine.com/articoli/metriche-di-sicurezza-dell-ai/
source: ICT Security Magazine
date: 2026-09-17
fetch_date: 2026-09-18T06:53:36.412365
---

# Metriche di sicurezza dell’AI: i numeri che i fornitori pubblicano non dicono se il sistema è sicuro

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

![Metriche di sicurezza dell'AI: Una rappresentazione simbolica del divario tra metriche dichiarate e sicurezza reale: in superficie, grafici ordinati e indicatori apparentemente positivi circondano il nucleo dell’AI; sotto, la struttura è invece fragile, danneggiata e piena di criticità nascoste.](https://www.ictsecuritymagazine.com/wp-content/uploads/Metriche-di-sicurezza-dellAI-i-numeri-che-i-fornitori-pubblicano-non-dicono-se-il-sistema-e-sicuro.png)

# Metriche di sicurezza dell’AI: i numeri che i fornitori pubblicano non dicono se il sistema è sicuro

A cura di:[Redazione](#molongui-disabled-link)  Ore 17 Settembre 202617 Settembre 2026

Metriche di sicurezza dell’AI come “il nostro sistema intercetta il 95% degli attacchi” circolano ormai in ogni presentazione commerciale. Quattro lavori usciti fra maggio e settembre 2026 mostrano che quel tipo di cifra, presa da sola, non permette di concludere nulla sulla sicurezza del sistema in esercizio.

Non si tratta di numeri falsi. Rispondono però a una domanda diversa da quella che interessa a chi firma un contratto, redige una valutazione d’impatto o misura la [vulnerabilità da prompt injection](https://www.ictsecuritymagazine.com/articoli/prompt-injection/) di un prodotto.

## Che cosa misurano davvero le metriche di sicurezza dell’AI

### Il punteggio è locale, la domanda è di sistema

Un tasso di rifiuto, un tasso di successo degli attacchi o un punteggio di violazione descrivono come si è comportato un controllo sulle richieste su cui è stato provato. Sono numeri statistici, non verdetti binari, per la ragione che rende l’[AI red teaming](https://www.ictsecuritymagazine.com/cyber-security/ai-red-teaming/) diverso da un penetration test. Chi installa quel controllo ha però un’altra domanda: quanto aiuto su compiti dannosi il servizio continua a dare a un attaccante che si adatta o che entra da un’altra parte.

La distinzione è al centro di un [lavoro sui safeguard](https://arxiv.org/abs/2609.00519) di Pingyu Wu, Weiming Zhang e Nenghai Yu, depositato il 1 settembre 2026. La risposta degli autori è che un punteggio locale migliore non costituisce, di per sé, un’affermazione più forte sul sistema dispiegato.

### L’asimmetria delle prove

Il punto metodologico è che le due direzioni non si dimostrano allo stesso modo. Un solo attacco che ottiene aiuto dannoso dal servizio in produzione basta a stabilire che quell’aiuto è ancora disponibile. Dimostrare che ne resti poco non discende dai numeri del controllo, perché richiede prove su che cosa il sistema circostante continua a permettere dopo che il controllo ha svolto la propria funzione locale.

Gli autori rilevano che quel tipo di prova compare solo in una piccola minoranza delle affermazioni esaminate. È un’asimmetria che conviene tenere presente quando un fornitore presenta un miglioramento di punteggio come un miglioramento di sicurezza. Vale anche per i [nuovi framework di valutazione](https://www.ictsecuritymagazine.com/articoli/difesa-dallai-offensiva/) che stanno emergendo sul lato difensivo.

## Tre modi in cui un punteggio aggregato inganna

### Il monitor che passa dal 95% all’11%

Il primo caso riguarda i sistemi che sorvegliano la catena di ragionamento di un agente, cioè i passaggi intermedi che il modello produce prima di agire. Shikhar Shiromani e Leo Richter, in uno [studio sui monitor](https://arxiv.org/abs/2608.00583) del 1 agosto 2026, costruiscono un attacco che riscrive soltanto il ragionamento e lascia invariate le azioni.

Sul sottoinsieme in cui il monitoraggio del ragionamento è l’unico segnale disponibile, il tasso di intercettazione scende da circa il 95% a meno dell’11%. L’accuratezza aggregata resta alta perché è dominata dagli attacchi già visibili dalle sole azioni. Gli autori la chiamano una falsa media. L’attacco si trasferisce fra famiglie di monitor e modelli di agente diversi e si riproduce con agenti in esecuzione. Contro un monitor calibrato, però, l’evasione si concentra nell’agente più capace.

### Il detector che scambia il benigno per attacco

Il secondo caso riguarda il lato opposto della soglia di decisione, quello dei falsi positivi, che raramente viene misurato. Yusuf Khalid Shire e Sang-Chul Kim, in [PIDS-Bench](https://arxiv.org/abs/2609.15017) del 14 settembre 2026, valutano sette rilevatori lungo più assi. Non sono tutti rilevatori dedicati: accanto a baseline addestrate e a classificatori esterni di prompt injection ci sono comparatori di sicurezza generale. Gli assi comprendono prompt benigni che imitano la struttura di un’iniezione senza intento malevolo, attacchi offuscati e cambi di dominio.

Un rilevatore che supera un F1 di 0,98 sull’insieme di collaudo classifica male circa un terzo di un insieme benigno di provenienza esterna, ristretto a contenuti attinenti alla sicurezza. L’F1 è l’indice sintetico che i fornitori citano più spesso, e combina in un solo numero quante minacce vengono colte e quanti allarmi sono infondati. Su quella distribuzione di stress nessun rilevatore interno raggiunge un punto operativo accettabile. Il criterio è un F1 non inferiore a 0,95, insieme a un tasso di falsi positivi sui benigni difficili non superiore a...