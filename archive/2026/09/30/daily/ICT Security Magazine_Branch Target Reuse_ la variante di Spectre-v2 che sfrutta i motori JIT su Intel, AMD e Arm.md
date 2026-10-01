---
title: Branch Target Reuse: la variante di Spectre-v2 che sfrutta i motori JIT su Intel, AMD e Arm
url: https://www.ictsecuritymagazine.com/notizie/spectre-v2-branch-target-reuse-motori-jit/
source: ICT Security Magazine
date: 2026-09-30
fetch_date: 2026-10-01T07:59:23.129987
---

# Branch Target Reuse: la variante di Spectre-v2 che sfrutta i motori JIT su Intel, AMD e Arm

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

![fantasma e freccie che portano all hardware: Branch Target Reuse, variante di Spectre-v2, sfrutta predizioni di salto obsolete nei motori JIT: exploit sul kernel Linux, patch e azioni per i CISO.](https://www.ictsecuritymagazine.com/wp-content/uploads/Branch-Target-Reuse-la-variante-di-Spectre-v2.png)

# Branch Target Reuse: la variante di Spectre-v2 che sfrutta i motori JIT su Intel, AMD e Arm

A cura di:[Redazione](#molongui-disabled-link)  Ore 30 Settembre 202630 Settembre 2026

Ricercatori di VUSec (Vrije Universiteit Amsterdam) e della Scuola Superiore Sant’Anna di Pisa hanno reso pubblica Branch Target Reuse, una variante di Spectre-v2 che sfrutta predizioni di salto obsolete nei motori JIT. Sul kernel Linux l’attacco ha estratto l’hash della password di root da una CPU Intel moderna, aggirando le mitigazioni attive prima della correzione specifica introdotta a luglio. Quelle correzioni sono ora disponibili e già riportate sui kernel stabili. AMD sostiene che bastino le indicazioni già esistenti per Spectre-v2.

Le vulnerabilità microarchitetturali tornano nell’agenda dei responsabili della sicurezza. L’embargo su Branch Target Reuse (BTR) è caduto il 29 settembre 2026 nel primo pomeriggio negli Stati Uniti, la sera in Italia. L’attacco è descritto sulla [pagina di progetto del gruppo VUSec](https://www.vusec.net/projects/btr/) e nel paper *Branch Target Reuse: Practical Spectre-v2 Attacks in JIT Engines via Stale Branch Prediction Entries*, accettato alla ACM Conference on Computer and Communications Security (CCS) 2026 e in programma a novembre. Il [paper](https://download.vusec.net/papers/btr_ccs26.pdf) e il [codice](https://github.com/vusec/btr) sono pubblici.

Gli autori sono Sander Wiebing, Yuhui Zhu, Alessandro Biondi e Cristiano Giuffrida. Appartengono al gruppo Systems and Network Security (VUSec) della Vrije Universiteit Amsterdam e alla Scuola Superiore Sant’Anna di Pisa. La vulnerabilità si colloca nella famiglia aperta nel 2018 da [Meltdown e Spectre](https://www.ictsecuritymagazine.com/articoli/lhardware-e-la-sicurezza-it-parte-3-meltdown-e-spectre/).

Tra i finanziatori figurano:

* AWS, con il progetto Themis;
* l’ente olandese per la ricerca NWO, con il progetto INTERSECT e il Dutch Prize for ICT research;
* il programma Horizon Europe, con il progetto RESCALE (grant n. 101120962);
* il progetto SERICS (PE00000014) del PNRR, programma MUR.

## Branch Target Reuse, perché è una notizia importante

Dal 2018 si riteneva che il codice automodificante, con cui i motori JIT generano istruzioni al volo, rendesse impraticabili attacchi di questo tipo. Giuffrida ha spiegato a [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-spectre-v2-attack-variant-leaks-linux-root-password-hash-in-minutes/) che BTR dimostra il contrario: gli attacchi di esecuzione transiente basati sul codice automodificante sono praticabili in ambienti reali e permettono di esfiltrare l’hash della password di root.

### Da violazioni spaziali a violazioni temporali: il primo esempio di attacco Spectre-v2 pratico *in-place*

A [The Hacker News](https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html) Giuffrida ha descritto BTR come il primo esempio di attacco Spectre-v2 pratico *in-place*, che usa lo stesso salto indiretto sia per addestrare il predittore sia per l’attacco. Secondo il ricercatore, gli attacchi tradizionali sfruttano violazioni spaziali, cioè dirottano un salto verso una destinazione diversa, e questo si riteneva difficile da ottenere su un solo salto. In BTR il salto e la destinazione restano gli stessi: cambia il significato della destinazione, cioè il codice che vi si trova. È una violazione temporale.

### Non un ritorno dopo una pausa

BTR non arriva dopo un lungo silenzio. Come ricorda The Hacker News, circa due mesi prima i ricercatori del MIT CSAIL Daniël Trujillo e Mengjia Yan avevano divulgato Interrupt Injection, tecnica che aggira le difese Spectre-v2 e legge memoria arbitraria del kernel su sistemi Linux con CPU Intel e AMD. Il filone degli [attacchi side channel e alla cache](https://www.ictsecuritymagazine.com/articoli/lhardware-e-la-sicurezza-it-parte-2-attacchi-side-channel-row-hammer-ed-attacchi-alla-cache/) resta attivo.

## Il meccanismo: predizioni che sopravvivono al codice

BTR non attacca il codice: attacca ciò che la CPU ricorda del codice. I motori just in time (JIT) generano ed eliminano di continuo codice nativo e riusano le stesse regioni della cache del codice. Le CPU moderne ripristinano la coerenza del codice dopo ogni modifica. Non invalidano però necessariamente le voci del predittore dei salti indiretti (Branch Target Buffer, BTB).

Quando la cache del codice viene ripopolata, una voce obsoleta può ancora puntare al vecchio punto di ingresso. La CPU vi salta in modo speculativo, ma a quell’indirizzo ora c’è codice nuovo, letto da una posizione non prevista. In questo modo l’attaccante può aggirare le protezioni software. Può anche eseguire sequenze di istruzioni disallineate (gadget) che ha predisposto nel nuovo codice.

### La primitiva speculative execute-after-free

I ricercatori chiamano il risultato primitiva *specu...