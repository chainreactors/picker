---
title: wp2shell, la RCE pre-autenticazione che rimette in discussione il WordPress Core
url: https://www.ictsecuritymagazine.com/notizie/wordpress-core-wp2shell-rce/
source: ICT Security Magazine
date: 2026-07-18
fetch_date: 2026-07-19T05:02:31.473648
---

# wp2shell, la RCE pre-autenticazione che rimette in discussione il WordPress Core

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

![wp2shell la RCE pre autenticazione che rimette in discussione il WordPress Core](https://www.ictsecuritymagazine.com/wp-content/uploads/wp2shell-la-RCE-pre-autenticazione-che-rimette-in-discussione-il-WordPress-Core.png)

# wp2shell, la RCE pre-autenticazione che rimette in discussione il WordPress Core

A cura di:[Redazione](#molongui-disabled-link)  Ore 18 Luglio 202618 Luglio 2026

Una vulnerabilità critica nel cuore di WordPress consente a un attaccante anonimo di eseguire codice da remoto su un’installazione standard, senza credenziali, senza plugin e senza interazione della vittima. La falla, battezzata *wp2shell* dai ricercatori di [Searchlight Cyber](https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core/) (divisione Assetnote) che l’hanno scoperta, colpisce il *core* della piattaforma che, secondo la stessa società, sostiene oltre 500 milioni di siti nel mondo. WordPress ha rilasciato le correzioni il 17 luglio 2026 e ha attivato gli aggiornamenti forzati; una scala di esposizione di questa portata impone una verifica immediata a chiunque gestisca un sito pubblico, dalla PA alle testate ai siti aziendali.

Nota di trasparenza sulla freschezza: la prima pubblicazione risale alla sera del 17 luglio 2026 (advisory Searchlight alle 19:10 UTC, *release* WordPress e *GitHub Security Advisory* in pari data), quindi appena fuori dalla finestra stretta delle sei ore ma nettamente all’interno delle ultime 24. È la storia dominante del ciclo e il rischio è in evoluzione: nelle prime ore del 18 luglio è comparso un primo *proof-of-concept* pubblico (vedi sotto), motivo in più per selezionarla segnalando in chiaro i *timestamp*.

## Cosa è, tecnicamente

*wp2shell* non è un singolo bug ma una catena. Il *remote code execution* pre-autenticazione è tracciato come
`CVE-2026-63030`
e nasce da una *route confusion* sull’*endpoint*
`/wp-json/batch/v1`
delle REST API: la logica che smista le richieste *batch* può essere indotta a raggiungere percorsi non previsti. A valle si innesta una *SQL injection*,
`CVE-2026-60137`
, nel parametro
`author__not_in`
di
`WP_Query`
, la classe che costruisce quasi ogni query verso il database. La combinazione dei due difetti porta dall’accesso anonimo all’esecuzione di codice.

Attenzione al disallineamento nei riferimenti: diversi *tracker* etichettano l’intera catena come la sola
`CVE-2026-63030`
, che è però l’identificativo della sola *route confusion*. I due *Security Advisory* ufficiali mappano con precisione difetti e scopritori: la *route confusion* nella *batch API* (
`CVE-2026-63030`
,
`GHSA-ff9f-jf42-662q`
, gravità *Critical*) è stata trovata da Adam Kues di Assetnote e Searchlight Cyber; la *SQL injection* nel parametro
`author__not_in`
di
`WP_Query`
(
`CVE-2026-60137`
,
`GHSA-fpp7-x2x2-2mjf`
, gravità *Moderate*) è stata segnalata in team da TF1T, dtro e haongo. Non esiste un terzo difetto: la RCE nasce dalla combinazione dei due e la seconda metà della catena non è opera di Searchlight, ma del secondo gruppo. Chi mappa l’esposizione tenga conto di entrambi gli identificativi.

Un elemento operativo utile arriva da Cloudflare, citata nell’analisi di [Rapid7](https://www.rapid7.com/blog/post/etr-cve-2026-63030-wp2shell-a-critical-remote-code-execution-vulnerability-in-wordpress-core/): il percorso vulnerabile risulta raggiungibile quando non è attiva una *persistent object cache*, condizione che riguarda molte installazioni predefinite ma non tutte.

## Versioni colpite e correzioni

Il *GitHub Security Advisory*
`GHSA-ff9f-jf42-662q`
circoscrive la RCE
`CVE-2026-63030`
alle versioni
`6.9.0`
–
`6.9.4`
e
`7.0.0`
–
`7.0.1`
; le release precedenti alla
`6.9`
non sono esposte alla *route confusion*. La *SQL injection*
`CVE-2026-60137`
risale invece al ramo
`6.8`
e copre
`6.8.0`
–
`6.8.5`
,
`6.9.0`
–
`6.9.4`
e
`7.0.0`
–
`7.0.1`
. Le correzioni sono in [WordPress 7.0.2](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/), nella *backport*
`6.9.5`
, nella
`6.8.6`
e nella
`7.1 Beta 2`
. Qui sta la ragione per cui il ramo
`6.8`
riceve solo una patch parziale: la
`6.8.6`
chiude la sola *SQL injection*, classificata *Moderate*, mentre la catena RCE *Critical* non lo tocca, non essendo presente su quel ramo la *route confusion*. WordPress.org ha forzato l’aggiornamento automatico sulle installazioni interessate; resta da verificare manualmente ogni sito esposto, perché *hosting* con *auto-update* disabilitato o *deploy* sotto controllo di versione possono restare scoperti.

Sul punteggio conviene essere precisi: l’advisory GitHub classifica la gravità come *Critical* sul piano qualitativo, mentre il CVSS numerico finora assegnato è 7.5, come segnala Rapid7. La divergenza tra etichetta e punteggio riflette metriche e contesti diversi; per la prioritizzazione pesa più la superficie (esecuzione di codice senza autenticazione su una piattaforma ubiqua) del numero isolato.

## Sfruttamento e mitigazioni

La sera del 17 luglio, alla pubblicazione degli advisory, non circolava alcun *proof-of-concept* pubblico: Searchlight aveva volutamente omesso i dettagli tecnici per dare tempo alle patch, rilasciando solo un servizio di verifica dell...