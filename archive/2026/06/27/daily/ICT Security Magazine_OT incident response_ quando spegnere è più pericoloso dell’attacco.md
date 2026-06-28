---
title: OT incident response: quando spegnere è più pericoloso dell’attacco
url: https://www.ictsecuritymagazine.com/industrial-cyber-security/ot-incident-response/
source: ICT Security Magazine
date: 2026-06-27
fetch_date: 2026-06-28T06:14:17.078506
---

# OT incident response: quando spegnere è più pericoloso dell’attacco

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

![OT incident response](https://www.ictsecuritymagazine.com/wp-content/uploads/OT-incident-response.png)

# OT incident response: quando spegnere è più pericoloso dell’attacco

A cura di:[Redazione](#molongui-disabled-link)  Ore 27 Giugno 20269 Giugno 2026

OT incident response è la risposta agli incidenti nei sistemi industriali, ed è uno dei pochi ambiti in cui le competenze della sicurezza informatica, applicate senza adattamento, possono fare più male dell’attacco che vorrebbero fermare. In informatica il riflesso, di fronte a una compromissione, è quasi automatico: isolare il sistema, staccarlo dalla rete, terminare il processo, e nei casi peggiori reinstallare tutto da zero. Sono mosse rapide e quasi sempre prive di conseguenze fisiche. Nel mondo della tecnologia operativa quelle stesse mosse possono provocare un arresto di emergenza, una perdita di produzione, il danneggiamento di un macchinario, o mettere a rischio l’incolumità di chi lavora nell’impianto.

Il punto di partenza, quindi, è un’inversione dell’obiettivo. In informatica il fine della risposta è fermare l’attaccante, e si accetta che farlo costi un disservizio temporaneo. Nell’OT il fine è mantenere il processo fisico in uno stato sicuro mentre si gestisce l’incidente, e fermare l’attaccante diventa un obiettivo secondario, da perseguire solo con azioni che non compromettano la sicurezza e la continuità dell’impianto. Chi affronta un incidente industriale con la testa dell’informatico, e stacca la spina come farebbe con un server, rischia di trasformare un problema di sicurezza in un problema di sicurezza fisica.

## Contenere non vuol dire spegnere

La distinzione più importante riguarda proprio il contenimento. In informatica contenere significa spesso isolare brutalmente: scollegare, spegnere, mettere in quarantena. Nell’OT questa equivalenza salta, perché ogni decisione di isolamento ha una ricaduta sul processo che governa. Scollegare un controllore può togliere la visibilità o il controllo su una parte di impianto nel momento meno opportuno, e la disconnessione fisica improvvisa è raramente la scelta giusta. La regola, qui, è privilegiare la segmentazione logica e graduale rispetto allo strappo, e soprattutto valutare ogni mossa di contenimento contro le sue conseguenze materiali prima di eseguirla.

È quello che gli specialisti definiscono spesso il ciclo delle conseguenze: per ogni azione di risposta, la domanda non è solo se ferma l’attaccante, ma cosa succede al processo se la si compie. Spegnere quel sistema interrompe una catena di sicurezza? Isolare quella zona lascia un impianto senza supervisione? La risposta a queste domande non la conosce chi viene dalla sicurezza informatica: la conosce l’ingegnere di processo, ed è per questo che nell’[incident response](https://www.ictsecuritymagazine.com/articoli/incident-response/) industriale la decisione non può restare nelle mani dei soli esperti di sicurezza.

## Sicuro non è la stessa cosa di protetto

Dietro tutto questo c’è una differenza concettuale che vale la pena rendere esplicita, perché in italiano due parole diverse si confondono in una. Esiste uno stato sicuro, lo *safe state*, che è la condizione in cui il processo fisico resta sotto controllo e non può produrre danni; ed esiste uno stato protetto, il *secure state*, che è la condizione in cui l’attaccante è stato escluso e il sistema informatico è messo in sicurezza. Nell’informatica i due tendono a coincidere: rendere sicuro un sistema vuol dire proteggerlo. Nell’OT possono entrare in conflitto diretto, perché l’azione che mette in sicurezza informatica un impianto, isolandolo o spegnendolo, può portarlo fuori dal suo stato fisico sicuro.

Quando i due obiettivi confliggono, l’OT sceglie il primo: la sicurezza fisica viene prima della pulizia informatica. È anche per questo che il recupero, in ambito industriale, è lento e si misura spesso in giorni o settimane, non in ore. Non si reinstalla un controllore come si reimmagina un portatile, non si manda offline un processo produttivo per ricostruirlo con calma, e ogni ripristino va validato per essere certi che il processo torni davvero nel suo stato corretto, e non solo apparentemente.

## OT incident response si pianifica al contrario

Da questa realtà discende un’indicazione pratica controintuitiva, al centro dei [cinque controlli critici](https://www.sans.org/white-papers/five-ics-cybersecurity-critical-controls) per la sicurezza ICS proposti dagli istruttori SANS Tim Conway e Robert M. Lee a partire dall’analisi degli attacchi industriali realmente avvenuti. Il primo di quei controlli è proprio il piano di risposta agli incidenti specifico per l’OT, e l’osservazione più interessante, come ha notato Lee, è che conviene partire da lì, dal piano di incident response industriale, e ricavare a ritroso il resto della strategia di sicurezza. Un piano OT non è la versione adattata di un piano informatico: nasce con priorità diverse, ordina le azioni in base all’impatto operativo e punta a tenere il sistema in funzione durante l’attacco, riducendo insieme l’effetto dell’aggressione e il colpo al processo controllato.

Un piano del genere coinvolge figure che l...