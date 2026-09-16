---
title: DDRop, un interposer da 159 dollari rimette in discussione le garanzie del confidential computing
url: https://www.ictsecuritymagazine.com/notizie/ddrop-confidential-computing-intel/
source: ICT Security Magazine
date: 2026-09-15
fetch_date: 2026-09-16T07:06:02.073560
---

# DDRop, un interposer da 159 dollari rimette in discussione le garanzie del confidential computing

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

![DDRop, l'attacco hardware che incrina le garanzie del confidential computing su Intel TDX e AMD SEV-SNP](https://www.ictsecuritymagazine.com/wp-content/uploads/DDRop-lattacco-hardware-che-incrina-le-garanzie-del-confidential-computing-su-Intel-2.png)

# DDRop, un interposer da 159 dollari rimette in discussione le garanzie del confidential computing

A cura di:[Redazione](#molongui-disabled-link)  Ore 15 Settembre 202615 Settembre 2026

Un circuito stampato che costa meno di duecento dollari, inserito per pochi minuti fra processore e memoria, basta a far leggere alla CPU dati vecchi come se fossero attuali. DDRop sfrutta questo difetto. La ricerca è stata divulgata il 14 settembre 2026 da nove ricercatori di KU Leuven, ETH Zurigo, Durham University e Google. Intel e AMD hanno riconosciuto i risultati, ma hanno risposto che gli attacchi fisici alla memoria restano fuori dal proprio modello di minaccia.

Quella risposta pesa più di quanto sembri. Il [confidential computing](https://www.ictsecuritymagazine.com/articoli/confidential-computing/) viene venduto come la tecnologia che protegge i dati anche dal fornitore di infrastruttura. Se gli scenari esclusi dal modello di minaccia sono gli stessi che una valutazione sui trasferimenti di dati deve esaminare, il problema smette di essere solo tecnico.

## Che cosa è stato pubblicato

Lo studio si intitola [«DDRop: Active Memory Interposer Attacks on Confidential VMs by Dropping DDR5 Writes»](https://ddropattack.eu/ddrop.pdf) e sarà presentato alla conferenza ACM CCS 2026, in programma all’Aia dal 15 al 19 novembre. Gli autori hanno pubblicato il sito divulgativo [ddropattack.eu](https://ddropattack.eu/). Hanno inoltre rilasciato a sorgente aperto schemi, disegni della scheda, firmware del microcontrollore e codice degli attacchi sul [repository GitHub del progetto](https://github.com/ddropattack/ddrop).

Gli attacchi funzionano su tre tecnologie: Intel TDX, Intel Scalable SGX e AMD SEV-SNP. La cronaca internazionale ha dato risalto alle prime due. La terza risulta colpita allo stesso modo, come indicano sia l’abstract sia la tabella riassuntiva dello studio.

## Il difetto: la cifratura protegge il contenuto, non l’attualità

Le tre tecnologie cifrano la memoria per proteggere i carichi di lavoro dall’ipervisore e dall’operatore del centro dati. Per reggere quantità di memoria grandi, però, rinunciano a una garanzia: la freschezza crittografica.

Freschezza significa poter stabilire se il valore letto da un indirizzo sia davvero l’ultimo che vi è stato scritto. Senza quella garanzia il processore può confermare che la memoria è cifrata, non che è attuale. Un dato vecchio si decifra perfettamente.

Da qui nasce l’attacco. Se una scrittura non arriva al modulo di memoria, al suo posto resta il contenuto precedente. Se quel contenuto è stato collocato dall’attaccante, il motore di cifratura lo decifra senza rilevare alcuna anomalia.

Le due piattaforme colpite usano schemi diversi ma condividono il limite. Intel TDX cifra con AES in modalità XTS e chiavi assegnate per dominio. AMD SEV-SNP usa AES in modalità XEX con chiavi per ospite e, scrivono i ricercatori, non prevede né integrità crittografica né freschezza.

TDX offre in via opzionale una modalità di integrità crittografica, che aggiunge a ogni linea di cache un codice di autenticazione da 28 bit. Intel lo descrive come derivato da SHA-3 e avverte che il suo inserimento riduce la copertura dei bit di correzione d’errore. Neppure quella modalità, però, introduce la freschezza.

## Come funziona l’interposer

Un interposer è una scheda che si frappone fisicamente fra il processore e il modulo di memoria, e che può osservare o alterare i segnali che li collegano. Quelli già noti per DDR5 erano ingombranti: richiedevano analizzatori logici e imponevano di abbassare la frequenza del bus, un intervento che un controllo all’avvio potrebbe individuare.

L’interposer di DDRop è invece una scheda compatta di interruttori analogici. Lavora alla frequenza nativa della memoria e si installa in pochi minuti.

Il meccanismo sfrutta il controllo di parità del bus comandi. I moduli di memoria usati nei server montano un componente che verifica la parità di ogni comando in arrivo. Quando trova un errore scarta il comando e lo segnala alla CPU su una linea di allerta, che ne provoca il reinvio.

L’interposer forza l’errore di parità e allo stesso tempo scollega la linea di allerta. Il modulo scarta la scrittura, il processore non riceve alcuna segnalazione, e la scrittura sparisce senza lasciare traccia.

La distinta base pubblicata dagli autori indica 159 dollari per un singolo sistema, calcolati su una produzione di dieci unità e al netto di ricerca, sviluppo e montaggio. Lo studio dichiara un costo complessivo inferiore a 200 dollari. Per confronto, gli stessi autori ricordano che un attacco passivo del 2020 richiedeva strumentazione da circa 170.000 dollari.

## Che cosa ottiene l’attaccante su Intel TDX

Su TDX l’attacco colpisce le tabelle delle pagine sicure. Sono la struttura con cui il modulo TDX traduce gli indirizzi di una macchina virtuale protetta, e il modulo le gestisce in via esclusiva proprio per i...