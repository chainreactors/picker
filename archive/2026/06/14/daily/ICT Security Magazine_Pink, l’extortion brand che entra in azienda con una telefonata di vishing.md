---
title: Pink, l’extortion brand che entra in azienda con una telefonata di vishing
url: https://www.ictsecuritymagazine.com/notizie/pink-estorsione-vishing-bypass-mfa/
source: ICT Security Magazine
date: 2026-06-14
fetch_date: 2026-06-15T07:10:01.919393
---

# Pink, l’extortion brand che entra in azienda con una telefonata di vishing

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

![Pink basta una telefonata per entrare in azienda, senza un solo exploit](https://www.ictsecuritymagazine.com/wp-content/uploads/Pink-basta-una-telefonata-per-entrare-in-azienda-senza-un-solo-exploit.png)

# Pink, l’extortion brand che entra in azienda con una telefonata di vishing

A cura di:[Redazione](#molongui-disabled-link)  Ore 14 Giugno 202614 Giugno 2026

Le aziende investono in *patch management*, *firewall* e rilevamento delle intrusioni, ma il gruppo di estorsione Pink non bussa a nessuna di quelle porte: chiama al telefono. Secondo l’analisi di [Unit 42](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-06-03-Pink-Extortion-Brand-Activity.txt) (Palo Alto Networks), che traccia il cluster come CL-CRI-1147 e lo qualifica come *extortion brand*, l’accesso iniziale ai sistemi aziendali arriva tramite *vishing*, cioè phishing vocale, senza *malware* sofisticati, senza cifratura dei dati e senza vulnerabilità *zero-day*. Una conversazione ben costruita, ed è la vittima stessa a consegnare le chiavi, aggirando di fatto l’intero perimetro tecnologico.

## Come funziona la catena di attacco

Lo schema è lineare e per questo efficace. L’aggressore chiama la vittima con [false telefonate](https://www.theregister.com/cyber-crime/2026/06/04/pink-is-the-latest-goon-squad-to-use-fake-helpdesk-calls-to-steal-creds/) fingendosi un addetto IT interno e la convince a inserire le proprie credenziali su una pagina di *phishing* controllata. La pagina cattura non solo username e password, ma anche il secondo fattore: con il furto della sessione, Pink supera l’autenticazione a più fattori senza doverla forzare.

Una volta dentro, l’attore individua ed esfiltra rapidamente i dati: tra le piattaforme prese di mira figurano *SharePoint* e *OneDrive*. L’account compromesso viene poi usato per recapitare l’email di estorsione e messaggi minatori direttamente nelle chat interne di *Microsoft Teams*, portando la pressione dentro gli strumenti di lavoro quotidiani.

Nel modello osservato da Unit 42 non compare alcun *payload* di cifratura: [il ricatto](https://gbhackers.com/pink-hacking-group-targets-enterprises/) si fonda sui dati sottratti, non sul blocco dei sistemi, in linea con lo spostamento di molti attori finanziariamente motivati dal *ransomware* classico all’estorsione mirata. I domini di *phishing* identificati richiamano, non a caso, il lessico della sicurezza moderna: passkeyadd[.]com, passkeydeploy[.]com e deploypasskey[.]com, ospitati tramite l’infrastruttura di DDoS-Guard. Pink riutilizza i domini di secondo livello per colpire più organizzazioni e riserva i domini di terzo livello a bersagli specifici, segno di una pianificazione mirata.

## Estorsione a tempo e identità sfuggente

La componente di pressione psicologica è strutturata. In un caso esaminato da Unit 42, dopo trattative rimaste a lungo senza risposta, il 1 giugno 2026 l’aggressore ha ricontattato la vittima da un account di posta gratuito, fornendo un nuovo identificativo qTox e il link al sito Pink Leak, con un ultimatum di 72 ore per rispondere. Il sito di *data leak* del gruppo, secondo quanto riportato dallo stesso, è stato attivato il 31 maggio 2026, e nel giro di pochi giorni sono comparse le prime presunte vittime.

Sull’attribuzione resta cautela. Google Threat Intelligence, che collega l’attività al codice UNC6671, ritiene che Pink possa non essere un gruppo del tutto nuovo, ma il *rebranding* di un team esistente: dopo la chiusura del marchio BlackFile nel maggio 2026 sarebbe nato Redact, poi forse riemerso come Pink. Unit 42 collega inoltre il gruppo alla galassia criminale Com, che ricorre a *social engineering*, furto di account ed estorsione, con tattiche affini a quelle di Bling Libra (noto anche come *ShinyHunters*).

## Perché conta per le aziende

Il dato strategico è che Pink non sfrutta una falla tecnica, ma la fiducia organizzativa. Nessun *patch management*, per quanto rapido, intercetta una telefonata che convince un dipendente a digitare la password su una pagina falsa. Per i responsabili della sicurezza la lezione è operativa: verificare con procedure fuori banda ogni contatto che si presenti come supporto IT, in particolare le richieste urgenti di aggiornare l’[autenticazione a più fattori](https://www.ictsecuritymagazine.com/articoli/sicurezza-informatica/) o di confermare un accesso; rafforzare la formazione contro il [vishing](https://www.ictsecuritymagazine.com/articoli/social-engineering/); adottare fattori resistenti al *phishing*, come le *passkey* legate al dispositivo, proprio ciò che i domini malevoli imitano per ingannare; monitorare comportamenti anomali su SharePoint, OneDrive e Teams. La superficie di attacco, ancora una volta, è umana.

Condividi sui Social Network:

Tag articolo:  [#estorsione](https://www.ictsecuritymagazine.com/tag/estorsione/ "estorsione")[#identità](https://www.ictsecuritymagazine.com/tag/identita/ "identità")[#MFA](https://www.ictsecuritymagazine.com/tag/mfa/ "MFA")[#ransomware](https://www.ictsecuritymagazine.com/tag/ransomware/ "ransomware")[#ShinyHunters](https://www.ictsecuritymagazine.com/tag/shinyhunters/ "ShinyHunters")[#social engineeri...