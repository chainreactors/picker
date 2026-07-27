---
title: Memory safety: la classe di vulnerabilità che i governi vogliono estinguere
url: https://www.ictsecuritymagazine.com/articoli/memory-safety-linguaggi-sicuri/
source: ICT Security Magazine
date: 2026-07-26
fetch_date: 2026-07-27T05:42:38.180129
---

# Memory safety: la classe di vulnerabilità che i governi vogliono estinguere

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

![Memory safety](https://www.ictsecuritymagazine.com/wp-content/uploads/Memory-safety.png)

# Memory safety: la classe di vulnerabilità che i governi vogliono estinguere

A cura di:[Redazione](#molongui-disabled-link)  Ore 26 Luglio 202617 Luglio 2026

La memory safety è uno dei problemi di sicurezza più antichi del software, e nel 2026 è tornata in cima all’agenda con la spinta delle agenzie governative. Si tratta dell’assenza di una intera famiglia di difetti, quelli che nascono quando un programma gestisce a mano la memoria e sbaglia: un *buffer overflow* che scrive oltre i confini di un’area, un *use-after-free* che accede a memoria già liberata, una lettura fuori dai limiti. Non sono bug esotici, sono i mattoni con cui si costruiscono da decenni gli *exploit* più gravi, e continuano a esserlo. Secondo la [guida di CISA e agenzie alleate](https://www.cisa.gov/case-memory-safe-roadmaps) del dicembre 2023, due terzi delle vulnerabilità segnalate nei linguaggi non *memory-safe* restano legate proprio alla gestione della memoria.

Il punto di svolta non è tecnico ma di prospettiva. Per anni questi difetti sono stati trattati come errori da correggere uno per uno; oggi l’idea che si sta affermando è che siano una classe da eliminare alla radice, scegliendo strumenti che non li rendano possibili. È lo spostamento dal “programmare con più attenzione” al “programmare in un linguaggio che non lascia commettere quell’errore”, e ha smesso di essere una preferenza accademica per diventare una richiesta esplicita di chi regola il mercato.

## Che cos’è la memory safety, e perché C e C++ non ce l’hanno

Un linguaggio è *memory-safe* quando impedisce, per costruzione, gli accessi scorretti alla memoria: non si può leggere oltre la fine di un array, usare un puntatore a memoria già liberata o dimenticare di controllare un limite, perché il linguaggio non lo consente o lo verifica al posto dello sviluppatore. Rientrano in questa categoria linguaggi molto diversi tra loro, da Java e C# a Go, Swift, Python e Rust, che ci arrivano per strade differenti: alcuni con un *garbage collector* che gestisce la memoria automaticamente, Rust con un sistema di proprietà verificato dal compilatore che ottiene lo stesso risultato senza rinunciare al controllo di basso livello.

C e C++, i linguaggi su cui poggia gran parte del software di sistema, non offrono questa garanzia: lasciano allo sviluppatore la gestione manuale della memoria, e con essa la possibilità di sbagliare. La conseguenza è quantificata da chi ha più codice al mondo. Microsoft ha stimato nel 2019 che circa il 70% delle proprie vulnerabilità con CVE derivasse ogni anno da problemi di memory safety, e in Chrome, su un’analisi di 912 bug di gravità alta o critica segnalati dal 2015 in poi, Google ne ha ricondotto alla stessa classe circa il 70%. Non è una questione di programmatori distratti: è che una classe di errori, su basi di codice enormi, si ripresenta comunque, a prescindere dalla bravura di chi scrive.

## Da problema tecnico a richiesta delle autorità

La novità è che la memory safety è entrata nei documenti delle autorità. La stessa guida di CISA, NSA, FBI e delle agenzie di Australia, Canada, Regno Unito e Nuova Zelanda chiede ai produttori di software di pubblicare una *roadmap* memory-safe, cioè un piano concreto per ridurre nel tempo la dipendenza dai linguaggi non sicuri. Con il documento [Product Security Bad Practices](https://www.ic3.gov/CSA/2025/250117.pdf), arrivato alla versione 2.0 nel gennaio 2025, il tono si è fatto più netto: sviluppare nuove linee di prodotto in linguaggi non *memory-safe*, per il software che sostiene funzioni critiche, viene indicato come una cattiva pratica, e ai produttori si chiede di pubblicare la propria roadmap entro la fine del 2025, scadenza ormai alle spalle, con l’eccezione dei prodotti la cui fine del supporto è prevista prima del 2030. Lo stesso documento precisa di non imporre alcun obbligo: non è una legge, ma una guida; sposta però le attese, e con esse la responsabilità di chi continua a ignorare il problema.

L’orientamento è confermato e dettagliato dal documento congiunto [NSA e CISA sui linguaggi memory-safe](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF) del giugno 2025. In Europa la spinta è meno esplicita ma va nella stessa direzione, per la via del [security by design](https://www.ictsecuritymagazine.com/articoli/security-by-design/): il Cyber Resilience Act, i cui requisiti essenziali di cybersicurezza si applicheranno dall’11 dicembre 2027, imporrà sicurezza fin dalla progettazione e gestione delle vulnerabilità per i prodotti con elementi digitali, mentre l’obbligo di segnalare le vulnerabilità attivamente sfruttate scatta già dall’11 settembre 2026. Il regolamento non nomina i linguaggi memory-safe, e il collegamento resta quindi inferenziale, ma un difetto di memoria evitabile alla radice è proprio il tipo di rischio che quell’obbligo mira a comprimere. La memory safety, insomma, sta migrando dal terreno delle buone pratiche a quello delle aspettative di mercato e, in prospettiva, degli obb...