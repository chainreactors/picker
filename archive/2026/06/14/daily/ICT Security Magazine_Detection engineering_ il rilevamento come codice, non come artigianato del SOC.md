---
title: Detection engineering: il rilevamento come codice, non come artigianato del SOC
url: https://www.ictsecuritymagazine.com/notizie/detection-engineering/
source: ICT Security Magazine
date: 2026-06-14
fetch_date: 2026-06-15T07:10:05.118808
---

# Detection engineering: il rilevamento come codice, non come artigianato del SOC

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

![Detection engineering](https://www.ictsecuritymagazine.com/wp-content/uploads/Detection-engineering-2.png)

# Detection engineering: il rilevamento come codice, non come artigianato del SOC

A cura di:[Redazione](#molongui-disabled-link)  Ore 14 Giugno 20269 Giugno 2026

La *detection engineering* nasce per colmare uno squilibrio che il report *M-Trends 2026* di Mandiant misura con precisione: nelle intrusioni analizzate l’accesso iniziale passa da chi lo ottiene a chi lo sfrutta in una mediana di ventidue secondi, e lo sfruttamento di vulnerabilità resta il primo modo per entrare, per il sesto anno consecutivo, con il 32 per cento dei casi. L’attaccante è veloce e industrializzato: ottiene l’accesso, lo cede, lo monetizza lungo una catena di operatori specializzati che si scambiano il lavoro in tempi che il difensore fatica anche solo a immaginare.

Il difensore, troppo spesso, lavora con un metodo che appartiene a un’altra epoca. Il problema, quasi sempre, non è la mancanza di strumenti. È il modo in cui le regole di rilevamento vengono prodotte: una alla volta, spesso in reazione all’ultimo incidente, scritte da chi capita di turno, senza versionamento, senza test, senza una misura di ciò che coprono davvero. La *detection engineering* parte da una premessa scomoda per molti reparti di sicurezza: una regola di rilevamento è software, e va trattata come software. Non come un appunto da incollare nel SIEM.

## Dal SOC reattivo al rilevamento progettato

Per anni il lavoro di rilevamento è stato un’attività di reazione. Arriva un *alert* da un prodotto, l’analista lo gestisce, e quando un attacco sfugge si aggiunge una regola che lo avrebbe intercettato. Il risultato è un magazzino di regole stratificate, di cui nessuno conosce con precisione l’origine, la logica o il tasso di errore. Funziona finché il volume resta gestibile. Smette di funzionare quando le regole diventano migliaia e i falsi positivi seppelliscono i veri.

La *detection engineering* ribalta l’ordine delle operazioni. Non parte dallo strumento ma dal comportamento dell’avversario, e tratta ogni rilevamento come un artefatto che ha un autore, una motivazione documentata, dei test e un ciclo di vita. È la differenza tra accumulare regole e progettare un sistema di rilevamento. Questa logica non sostituisce il [Security Operations Center](https://www.ictsecuritymagazine.com/articoli/security-operations-center/), ma ne cambia il baricentro: meno tempo speso a smistare allarmi, più tempo speso a costruire e mantenere la capacità di rilevare ciò che conta.

Il punto di partenza è una domanda che il SOC tradizionale si pone di rado: cosa stiamo cercando di rilevare, e perché proprio quello. Non “quali regole abbiamo”, ma “quali comportamenti avversari vogliamo intercettare, e quanto bene li copriamo”.

#### Il bersaglio giusto: la piramide del dolore

La risposta a quella domanda ha una base concettuale precisa, formulata da David Bianco nel 2013 a partire dalla lettura del report APT1 di Mandiant. La sua piramide del dolore ordina gli indicatori in base a quanto costa all’attaccante cambiarli una volta scoperti. Alla base ci sono gli *hash* dei file, banali da modificare: bloccarli infastidisce l’avversario per pochi minuti. Salendo si incontrano indirizzi IP, nomi di dominio, artefatti di rete. In cima ci sono le tattiche, le tecniche e le procedure, cioè il modo in cui un attaccante opera. Costringerlo a cambiare quelle significa imporgli un costo reale, perché tocca riprogettare l’attacco, non semplicemente rigenerare un indicatore.

La conseguenza operativa è netta. Una regola che insegue *hash* e indirizzi IP invecchia nel giro di ore. Una regola che descrive un comportamento, per esempio l’uso anomalo di uno strumento di amministrazione legittimo per muoversi lateralmente, resta valida a lungo e fa male all’avversario. Per questo la *detection engineering* matura ancora la propria logica sulle tecniche, e usa come vocabolario condiviso il [framework MITRE ATT&CK](https://attack.mitre.org/).

La versione 19, rilasciata il 28 aprile 2026, descrive per il dominio *Enterprise* quindici tattiche, oltre duecento tecniche e centinaia di sotto-tecniche, e viene aggiornata due volte l’anno: proprio in questa release la tattica Defense Evasion è stata divisa in due, Stealth e Defense Impairment, un cambiamento che obbliga chi mantiene rilevamenti a rimappare la propria copertura. Mappare ogni rilevamento a una tecnica di ATT&CK non è un esercizio formale: è il modo per sapere, in concreto, cosa si copre e cosa resta scoperto.

## Detection engineering e detection-as-code: il ciclo di vita di una regola

Qui la *detection engineering* prende la forma che le dà il nome di disciplina ingegneristica. L’approccio *detection-as-code* applica alle regole le stesse pratiche con cui si sviluppa software di produzione. Ogni rilevamento vive in un repository sotto controllo di versione. Ogni modifica passa da una *pull request* e da una revisione tra pari. Ogni regola viene testata contro dati di riferimento in una pipeline di integrazione continua prima di arrivare in produzione, e può essere ritirata con un *rollback* se si comporta male.

Il for...