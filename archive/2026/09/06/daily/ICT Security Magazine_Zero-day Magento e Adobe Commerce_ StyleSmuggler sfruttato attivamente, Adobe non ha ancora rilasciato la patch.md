---
title: Zero-day Magento e Adobe Commerce: StyleSmuggler sfruttato attivamente, Adobe non ha ancora rilasciato la patch
url: https://www.ictsecuritymagazine.com/notizie/zero-day-magento-stylesmuggler-adobe-commerce/
source: ICT Security Magazine
date: 2026-09-06
fetch_date: 2026-09-07T06:49:24.030454
---

# Zero-day Magento e Adobe Commerce: StyleSmuggler sfruttato attivamente, Adobe non ha ancora rilasciato la patch

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

![StyleSmuggler, zero-day Magento sfruttato: patch assente](https://www.ictsecuritymagazine.com/wp-content/uploads/Zero-day-StyleSmuggler-Magento-e-Adobe-Commerce-sotto-attacco-senza-patch-ufficiale.png)

# Zero-day Magento e Adobe Commerce: StyleSmuggler sfruttato attivamente, Adobe non ha ancora rilasciato la patch

A cura di:[Redazione](#molongui-disabled-link)  Ore 6 Settembre 20266 Settembre 2026

*Dal 4 settembre 2026 un attacco senza correzione ufficiale colpisce i negozi Magento Open Source aggiornati. Le mitigazioni disponibili sono di terze parti. Per gli e-commerce italiani si aprono due questioni giuridiche: la notifica al Garante e la responsabilità dell’agenzia.*

Dal 4 settembre 2026 gli e-commerce basati su Magento Open Source e Adobe Commerce sono esposti a un attacco attivo. Il produttore non ha ancora pubblicato una correzione. La vulnerabilità, chiamata **StyleSmuggler** dalla società olandese Sansec che l’ha scoperta, permette a un attaccante non autenticato di eseguire codice sul server del negozio e di installare una backdoor persistente.

Al 6 settembre Adobe non ha pubblicato avvisi, identificativi CVE, patch o soluzioni temporanee. L’[indice dei bollettini di sicurezza di Adobe Commerce](https://helpx.adobe.com/security/products/magento.html) si ferma all’aggiornamento dell’11 agosto ([APSB26-92](https://helpx.adobe.com/security/products/magento/apsb26-92.html)). Quel bollettino correggeva sette CVE, tra cui un’escalation di privilegi non autenticata con punteggio CVSS 9.1 (CVE-2026-71362), e dichiarava che Adobe non era a conoscenza di exploit in circolazione. Secondo Sansec, la prossima release di sicurezza è prevista per l’8 settembre, ma non è noto se coprirà questo difetto.

Questo articolo non ripercorre la cronaca. Si concentra sul vuoto tra la scoperta e la patch. Cosa può fare oggi un esercente italiano che tratta dati di pagamento? Quali limiti hanno le mitigazioni non ufficiali? Quali obblighi giuridici scattano quando la compromissione è probabile ma non accertata?

## Cosa è StyleSmuggler

La cronologia dell’[avviso di Sansec](https://sansec.io/research/stylesmuggler) fissa la prima esecuzione confermata dell’exploit alle 22:20 UTC del 4 settembre. Alle 22:40 Sansec ha individuato la campagna; alle 23:10 il suo scanner eComscan ha segnalato l’impianto su negozi non collegati tra loro. Nelle ore successive Sansec ha riprodotto l’intera catena su installazioni pulite di Magento Open Source 2.4.7, 2.4.8 e 2.4.9. Le regole di blocco del suo prodotto Shield sono entrate in funzione il 5 settembre alle 07:15 UTC. L’avviso è uscito lo stesso giorno, prima del completamento dell’analisi, perché i negozi venivano compromessi in quel momento.

L’attacco abusa del sistema di template di Magento, in particolare delle proprietà
`styles`
, per aggirare le protezioni esistenti. Si svolge in due fasi:

1. **Iniezione.** L’attaccante fa scrivere codice PHP in un file che Magento stesso genera. Sansec cita i rapporti di errore in
   `var/report/`
   . Disrex Group, società olandese di hosting e sviluppo Magento, ha gestito la risposta a due negozi compromessi. In entrambi i casi ha osservato l’avvelenamento di
   `var/log/system.log`
   : l’attaccante invia un codice negozio non valido e Magento lo registra così com’è. Secondo Disrex questa fase non è filtrabile a livello di server web, perché è indistinguibile da un’integrazione malfunzionante.
2. **Esecuzione.** L’attaccante provoca l’invio dell’email standard “Payment Transaction Failed Reminder”. Il codice iniettato viene eseguito mentre Magento prepara il messaggio. Nessuno deve aprire l’email; l’attacco riesce anche se la consegna fallisce. L’assenza di messaggi in casella non è quindi una prova di sicurezza.

La ricostruzione del meccanismo, pubblicata da Disrex in un [documento dedicato](https://github.com/disrex-group/stylesmuggler-mitigation/blob/main/HOW-IT-WORKS.md), è un’interpretazione indipendente. Secondo questa lettura, una direttiva
`{{block}}`
nel testo iniettato conduce, attraverso una catena di classi native di Magento, fino a codice pensato per il solo compilatore di dependency injection da riga di comando. Quel codice termina con un
`include`
su un percorso scelto dall’attaccante: il log avvelenato un istante prima. Disrex ha corretto una prima versione che identificava un punto di ingresso sbagliato. Sansec non ha confermato la ricostruzione né pubblicato la catena completa; Disrex non ha diffuso la richiesta assemblata. Per le stesse ragioni questo articolo non riporta dettagli riproducibili.

Una volta ottenuta l’esecuzione, un dropper PHP prova in ordine sei funzioni di avvio processo (
`shell_exec`
,
`exec`
,
`system`
,
`passthru`
,
`proc_open`
,
`popen`
) e usa la prima disponibile. Poi scarica e avvia l’impianto: un binario Rust statico e privo di simboli di circa 1,9 MB, per x86-64 e arm64. Il file viene installato in
`~/.local/share/.gvfsd/gvfsd-user`
, nella home dell’utente del sito e non nella cartella web. Il processo si maschera con il nome
`[kworker/u:8:0]`
, tipico di un thread del kernel Linux. Una voce cron lo riavvia ogni cinque minuti; è scritta direttamente nel file di spool, così i...