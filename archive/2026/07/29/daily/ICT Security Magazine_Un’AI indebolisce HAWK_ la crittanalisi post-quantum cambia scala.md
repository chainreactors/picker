---
title: Un’AI indebolisce HAWK: la crittanalisi post-quantum cambia scala
url: https://www.ictsecuritymagazine.com/notizie/claude-crittanalisi-hawk-post-quantum/
source: ICT Security Magazine
date: 2026-07-29
fetch_date: 2026-07-30T04:52:23.055307
---

# Un’AI indebolisce HAWK: la crittanalisi post-quantum cambia scala

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

![AI indebolisce HAWK la crittanalisi degli standard post-quantum](https://www.ictsecuritymagazine.com/wp-content/uploads/AI-indebolisce-HAWK-la-crittanalisi-degli-standard-post-quantum.png)

# Un’AI indebolisce HAWK: la crittanalisi post-quantum cambia scala

A cura di:[Redazione](#molongui-disabled-link)  Ore 29 Luglio 202629 Luglio 2026

*Anthropic ha annunciato di aver usato un proprio modello per ricavare un attacco che riduce la robustezza effettiva delle chiavi di HAWK, uno dei candidati alla firma digitale post-quantum in gara al NIST, e per accelerare di 200-800 volte il miglior attacco noto su una versione ridotta di AES. Nessuno dei due risultati tocca sistemi in produzione, ma sposta un problema di governance: la revisione degli algoritmi crittografici sta per diventare più veloce di quanto le comunità umane sappiano verificare.*

Il 28 luglio Anthropic ha pubblicato, tramite il proprio Frontier Red Team, due risultati di crittanalisi ottenuti con il modello Claude Mythos Preview, un modello ad accesso ristretto e non disponibile pubblicamente. Il primo è un attacco di *key recovery* migliorato contro
`HAWK`
, uno schema di firma digitale progettato per resistere ai computer quantistici; il secondo è un’ottimizzazione del miglior attacco noto su
`AES-128`
ridotto a sette round. La ricostruzione qui proposta si basa sul [comunicato di ricerca](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) e sui due paper tecnici rilasciati insieme a un repository con codice dimostrativo.

## Cosa è stato trovato su HAWK

`HAWK`
è l’unico schema basato su reticoli tra i nove candidati ammessi al terzo round del processo NIST per [firme digitali aggiuntive](https://csrc.nist.gov/projects/pqc-dig-sig/round-3-additional-signatures) (selezione del maggio 2026, NIST IR 8610), il bando aperto nel 2022 per diversificare gli algoritmi post-quantum. I set di parametri ufficiali sono due,
`HAWK-512`
(livello di sicurezza NIST 1) e
`HAWK-1024`
(livello 5);
`HAWK-256`
non è invece una configurazione in uso, ma un parametro-sfida che i progettisti forniscono come bersaglio crittanalitico. È un punto da tenere fermo, perché l’attacco di recupero chiave dimostrato riguarda proprio
`HAWK-256`
, non i set in uso.

La sicurezza di
`HAWK`
poggia sulla difficoltà del *Lattice Isomorphism Problem*: un attaccante dovrebbe recuperare una trasformazione nascosta tra due reticoli. Un [lavoro precedente](https://eprint.iacr.org/2025/928) di Daniël van Gent e Ludo Pulles aveva dimostrato che l’esistenza di un particolare automorfismo (una simmetria che preserva il reticolo) avrebbe ridotto il recupero della chiave alla ricerca di un vettore corto in un reticolo di dimensione circa dimezzata, senza però stabilire se quell’automorfismo fosse davvero accessibile nel reticolo usato da
`HAWK`
. Secondo Anthropic, il modello ha individuato l’automorfismo mancante, costruendo un’enumerazione più rapida della chiave.

L’effetto è quantificabile: per
`HAWK-256`
il costo atteso di un recupero completo della chiave scende da circa
`2^64`
a
`2^38`
operazioni. Anthropic descrive il risultato come un dimezzamento della *keysize* effettiva, cioè della dimensione del reticolo su cui l’attaccante deve lavorare; da qui la conseguenza operativa, cioè che per mantenere il livello di sicurezza dichiarato le chiavi andrebbero raddoppiate, e questo erode molti dei vantaggi che rendevano lo schema interessante. Per i parametri più grandi il conto resta proibitivo: le stime di *gate count* riportate nel [paper su HAWK](https://www.anthropic.com/document/hawk_key_recovery.pdf) (Tabella 1) scendono da
`2^150`
a
`2^108`
per
`HAWK-512`
e da
`2^288`
a non più di
`2^182`
per
`HAWK-1024`
, valori che restano impraticabili. Va precisato che l’attacco è esponenziale, non è una rottura in tempo polinomiale, ed è specifico di
`HAWK`
: non si estende agli altri candidati NIST né alla crittografia su reticoli in generale.

Un precedente aiuta a inquadrare la portata, ma va maneggiato con misura: durante la standardizzazione post-quantum lo schema SIKE, ritenuto solido, fu completamente compromesso in circa un’ora su un portatile. La differenza è sostanziale, perché SIKE venne rotto in tempo pratico, mentre l’attacco a
`HAWK`
resta esponenziale e non ne consente la violazione effettiva; l’analogia riguarda il momento, non l’esito, cioè una debolezza emersa a valle di anni di revisione. Trovare falle tardive è, in questo senso, il processo che funziona.

Il risultato è arrivato dentro una cornice di *responsible disclosure* che per una rivista di sicurezza conta quanto il dato tecnico: Anthropic dichiara di aver condiviso l’attacco con gli autori di
`HAWK`
a giugno, di aver coordinato la divulgazione con la mailing list pubblica del NIST lo stesso giorno del rilascio e di aver distribuito copie anticipate a partner governativi e industriali, oltre a consultare accademici per la validazione. Non è quindi un lancio unilaterale.

## AES ridotto: più veloce, ancora impraticabile

Il secondo risultato riguarda
`AES-128`
, tra i cifrari simmetrici più studiati al mondo, ma nella variante ridotta a sette dei dieci round previsti. Studiare cifrari a ...