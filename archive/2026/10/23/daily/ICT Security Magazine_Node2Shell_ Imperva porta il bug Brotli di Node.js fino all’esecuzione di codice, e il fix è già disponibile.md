---
title: Node2Shell: Imperva porta il bug Brotli di Node.js fino all’esecuzione di codice, e il fix è già disponibile
url: https://www.ictsecuritymagazine.com/notizie/node2shell-brotli-node-js-cve-2026-111497/
source: ICT Security Magazine
date: 2026-10-23
fetch_date: 2026-10-24T06:47:58.268558
---

# Node2Shell: Imperva porta il bug Brotli di Node.js fino all’esecuzione di codice, e il fix è già disponibile

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security.webp)](https://www.ictsecuritymagazine.com/)

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

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security.webp)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026-1440.webp)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Node2Shell Nucleo cyber_ attacco e difesa](https://www.ictsecuritymagazine.com/wp-content/uploads/Node2Shell-Nucleo-cyber_-attacco-e-difesa.webp)

# Node2Shell: Imperva porta il bug Brotli di Node.js fino all’esecuzione di codice, e il fix è già disponibile

A cura di:[Redazione](#molongui-disabled-link)  Ore 23 Ottobre 202623 Ottobre 2026

Una vulnerabilità che il progetto Node.js aveva classificato *high* il 21 ottobre ha ora una dimostrazione pubblica di esecuzione di codice. Il team Red Team di Imperva ha battezzato Node2Shell la loro analisi di [CVE-2026-111497](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases), una scrittura fuori dai limiti nel decoder Brotli incluso in Node.js, e ha mostrato che dati Brotli costruiti ad arte, contenuti in una risposta o nel corpo di una richiesta, portano ad eseguire codice su un’immagine ufficiale.

## Che cosa è stato dimostrato

Una prima proof of concept pubblica, uscita il 22 ottobre, otteneva esecuzione di codice solo su una build di test deliberatamente indebolita; su una build standard il suo autore riferiva un crash e una lettura limitata della memoria del processo, senza esecuzione di codice (così la [ripresa THN del 22/10](https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html)). Node2Shell sposta il quadro: l’esecuzione avviene su un’immagine ufficiale.

Il [post di Imperva](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/) descrive l’esecuzione di codice sull’immagine ufficiale Node.js 24.22.0 per Linux arm64, senza debugger né binari strumentati. Il difetto sta nella gestione delle transizioni tra tipi di blocco: l’input di test raggiunge una transizione che la struttura stessa del flusso rende impossibile; il decoder vulnerabile la tratta come richiesta di ulteriori dati e prosegue in uno stato non valido. Un’esecuzione con *sanitizer* ha mostrato la scrittura oltre il buffer previsto. La correzione a monte (commit nel repository Google Brotli) fa restituire al decoder un errore di formato, e la 24.22.1 rifiuta gli stessi input.

Imperva precisa che l’esecuzione ha richiesto più tentativi nel suo ambiente. Non pubblica dati su affidabilità dell’exploit, né sull’ASLR; l’architettura testata è una sola (arm64), e le linee 22.x e 26.x non sono state provate. Un limite da tenere presente per chi deve stimare il rischio reale.

## Dove arrivano dati Brotli non attendibili

I punti di ingresso verificati dai ricercatori sono due: la funzione
`fetch()`
integrata, quando consuma una risposta compressa con Brotli, e i *body parser* di Express 5 (intervalli 5.0.0 a 5.3.0 e body-parser 2.0.0 a 2.3.0, provati con
`express.json()`
e
`express.raw()`
), che decodificano il corpo delle richieste. Un semplice server
`http`
di Node non decodifica da solo; il decoder è raggiungibile anche direttamente dal modulo
`node:zlib`
. Ne discende che l’esposizione riguarda soprattutto API che accettano corpi compressi e servizi che interrogano endpoint esterni, dunque anche i *backend* di piattaforme agentiche che fanno molte chiamate in uscita.

## Versioni, gravità, mitigazioni

Secondo l’advisory Node.js sono interessate le linee 26.x, 24.x e 22.x; i rilasci correttivi sono 22.23.4, 24.22.1 e 26.12.1. La gravità è indicata come *high*; né Node.js né Imperva riportano un punteggio CVSS, e conviene non attribuirne uno finché NVD non lo pubblica. Le versioni a fine vita (20.x e precedenti) non ricevono correzioni.

Non esiste un *workaround* interno a Node.js: Imperva suggerisce di limitare il traffico Brotli non attendibile sui percorsi esposti e ha aggiunto regole WAF; per le immagini container serve la ricostruzione con la versione corretta. Al 22 ottobre non risultavano sfruttamenti in the wild, secondo [The Hacker News](https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html). Vercel ha attivato regole WAF il 21 ottobre per le richieste in ingresso, ma [dichiara](https://vercel.com/kb/bulletin/node-js-security-advisory) che non coprono le risposte Brotli scaricate dall’applicazione da altri server (il percorso
`fetch()`
) e non sostituiscono la patch; per queste serve il runtime aggiornato.

La correzione è un commit a monte del progetto Brotli, apparso nei sorgenti a febbraio 2026 e rilasciato come correzione di sicurezza solo il 21 ottobre nelle versioni Brotli 1.2.1, 1.1.1 e 1.0.10 (dato THN): altri software che incorporano Brotli potrebbero richiedere lo stesso aggiornamento. Lo stesso rilascio Node.js blocca anche otto chiavi di CA intermedie di eMudhra segnalate come compromesse.

Due incongruenze tra le fonti: Imperva attribuisce la segnalazione a Matteo Collina e la correzione ad Antoine du Hamel, mentre l’advisory Node.js indica come segnalatori Khai Tran e Sylvie Mayer di OpenAI Codex Security e come autori del fix gli utenti mcollina e aduh95; qui si segue l’advisory del progetto. Lo stesso rilascio corregge altre CVE *high* (resolver DNS, due bypass nella verifica dei nomi host TLS), e l’aggiornamento va quindi pianificato per l’insieme, non solo per Brotli.

## Esposizione italiana

Nessun atto italiano (ACN, CSIRT Italia, CERT-AGID) risulta pubblicato sul ...