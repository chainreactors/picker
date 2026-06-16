---
title: GreatXML e BitLocker: cosa sappiamo davvero sul presunto zero-day che aggira la cifratura di Windows
url: https://www.cybersecurity360.it/nuove-minacce/greatxml-e-bitlocker-cosa-sappiamo-davvero-sul-presunto-zero-day-che-aggira-la-cifratura-di-windows/
source: Over Security
date: 2026-06-15
fetch_date: 2026-06-16T07:16:41.524191
---

# GreatXML e BitLocker: cosa sappiamo davvero sul presunto zero-day che aggira la cifratura di Windows

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=www.cybersecurity360.it)
[I nostri servizi](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## GreatXML e BitLocker: cosa sappiamo davvero sul presunto zero-day che aggira la cifratura di Windows

* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [X](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

L'ANALISI TECNICA

# GreatXML e BitLocker: cosa sappiamo davvero sul presunto zero-day che aggira la cifratura di Windows

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

[Partecipa al dibattito](#comments)

Indirizzo copiato

---

GreatXML è stato presentato come un exploit zero-day capace di aggirare BitLocker sfruttando WinRE e Microsoft Defender Offline Scan. Le verifiche indipendenti, però, raccontano una storia meno lineare. Tra dubbi sul PoC e assenza di una CVE, il caso riapre il dibattito sulla sicurezza del recovery path di Windows

Pubblicato il 15 giu 2026

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)

---

[Vincenzo Calabrò](https://www.cybersecurity360.it/giornalista/vincenzo-calabro/)

Information Security & Digital Forensics Analyst and Trainer

---

---

![GreatXML e BitLocker](data:image/png;base64...)![GreatXML e BitLocker](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/06/GreatXML-e-BitLocker.jpg)

![AI Questions Icon](data:image/gif;base64...)![AI Questions Icon](https://chatbotdev.ai.nextwork360.it/icons/NW360.svg)

Chiedi all'AI

Riassumi questo articolo

Approfondisci con altre fonti

Punti chiave

* Il caso **GreatXML** segnala una falla nella trust chain del recovery path: possibile bypass di **BitLocker** sfruttando **WinRE** e **Microsoft Defender Offline Scan**; verifiche discordanti.
* Non è una rottura crittografica: **BitLocker** resta sicuro ma il problema è nella catena di fiducia (artefatti come **unattend.xml** e partizione **Recovery**); prerequisiti operativi incerti.
* Azioni raccomandate: non trarre conclusioni affrettate, rivedere configurazioni **TPM-only**, controllo accesso e abilitazione di **WinRE**, uso di **Microsoft Defender Offline Scan** e monitoraggio recovery.

Riassunto generato con AI

---

---

Il caso **GreatXML** evidenzia una **falla nella sicurezza degli endpoint**: la **fiducia riposta nel recovery path**. Il problema è legato al **bypass di BitLocker tramite WinRE e Microsoft Defender Offline Scan**, ma le verifiche indipendenti non sono del tutto concordi sulla sua riproducibilità.

Nel giro di poche ore, GreatXML è passato dalla timeline dei ricercatori ai siti di settore, con il tipico effetto amplificatore che accompagna ogni disclosure non coordinata.

Il punto critico è **ottenere l’accesso a un volume protetto da BitLocker senza la chiave di recupero**, sfruttando il comportamento di **Windows Recovery Environment (WinRE)** dopo l’uso di Microsoft Defender Offline Scan.

Per chi lavora nel settore della [sicurezza degli endpoint](https://www.cybersecurity360.it/soluzioni-aziendali/larchitettura-della-sicurezza-senza-gestione-degli-asset-non-ce-cyber-security/), il titolo era già di per sé un richiamo, perché toccava tre temi sensibili: full-disk encryption, trusted recovery environment e physical access. Per questo, serve un approccio rigoroso, il caso va trattato con metodo.

Quando un claim è molto impattante e non proviene da un advisory ufficiale, la prima difesa contro le semplificazioni consiste nel distinguere ciò che è documentato da Microsoft, ciò che è sostenuto dal ricercatore e ciò che è stato effettivamente verificato da terzi.

Indice degli argomenti

* [BitLocker non è stato violato: il problema è nella catena di fiducia](#BitLocker_non_e_stato_violato_il_problema_e_nella_catena_di_fiducia)
* [GreatXML funziona davvero? Le verifiche indipendenti non concordano](#GreatXML_funziona_davvero_Le_verifiche_indipendenti_non_concordano)
* [Perché il caso GreatXML riguarda tutti gli amministratori di endpoint](#Perche_il_caso_GreatXML_riguarda_tutti_gli_amministratori_di_endpoint)
* [Come ridurre il rischio in attesa di una posizione ufficiale di Microsoft](#Come_ridurre_il_rischio_in_attesa_di_una_posizione_ufficiale_di_Microsoft)
* [La vera lezione di GreatXML: la sicurezza non finisce con BitLocker](#La_vera_lezione_di_GreatXML_la_sicurezza_non_finisce_con_BitLocker)
* [Tra hype e realtà: cosa dovrebbero fare ora le organizzazioni](#Tra_hype_e_realta_cosa_dovrebbero_fare_ora_le_organizzazioni)
* [Riferimenti](#Riferimenti)

## BitLocker non è stato violato: il problema è nella catena di fiducia

Un punto fermo è che **BitL...