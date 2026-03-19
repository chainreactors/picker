---
title: Supply chain software, attacco npm PyPI: 454.000 pacchetti malevoli e il primo worm autoreplicante che ha cambiato tutto
url: https://www.ictsecuritymagazine.com/articoli/supply-chain-software/
source: ICT Security Magazine
date: 2026-03-18
fetch_date: 2026-03-19T04:20:56.077391
---

# Supply chain software, attacco npm PyPI: 454.000 pacchetti malevoli e il primo worm autoreplicante che ha cambiato tutto

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
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![Supply chain software](https://www.ictsecuritymagazine.com/wp-content/uploads/Supply-chain-software.jpeg)

# Supply chain software, attacco npm PyPI: 454.000 pacchetti malevoli e il primo worm autoreplicante che ha cambiato tutto

A cura di:[Redazione](#molongui-disabled-link)  Ore 18 Marzo 202618 Marzo 2026

Un attacco alla supply chain software attraverso npm e PyPI non è più un’ipotesi accademica: è il meccanismo operativo che nel 2025 ha permesso la distribuzione di oltre 454.000 nuovi pacchetti malevoli nei registri open-source globali. È una cifra che merita di essere ripetuta, perché racconta qualcosa di profondo sulla fragilità strutturale dell’ecosistema su cui poggia la quasi totalità del software moderno.

Ogni volta che uno sviluppatore esegue *npm install* o *pip install*, sta dichiarando fiducia implicita in un registro pubblico che non richiede validazione dell’identità del publisher, non verifica la corrispondenza tra nome del pacchetto e contenuto, e – aspetto decisivo – privilegia automaticamente la versione più recente di ogni dipendenza. In un ecosistema dove i download annuali hanno superato i [9,8 trilioni](https://www.globenewswire.com/news-release/2026/01/28/3227372/0/en/Sonatype-Research-Reveals-OSS-Malware-Grows-75-as-Yearly-Open-Source-Downloads-Surpass-9-8-Trillion.html) e i componenti open-source costituiscono l’80-90% delle applicazioni moderne, quella fiducia implicita è diventata l’arma più efficiente a disposizione degli attaccanti.

Il [*2026 State of the Software Supply Chain Report* di Sonatype](https://www.sonatype.com/state-of-the-software-supply-chain/introduction) – pubblicato il 28 gennaio 2026 e basato sull’analisi di oltre 1,233 milioni di pacchetti malevoli cumulativi – documenta un’evoluzione che non è più quantitativa ma qualitativa: il malware nella supply chain software ha adottato la stessa architettura modulare, la stessa logica di riuso e la stessa capacità di scala che rendono potente l’open-source legittimo. Non stiamo più parlando di script rudimentali nascosti in pacchetti oscuri. Stiamo parlando di campagne industrializzate, persistenti, spesso orchestrate da attori statali, che trattano npm e PyPI come canali di distribuzione a basso attrito verso macchine di sviluppo e pipeline CI/CD – ambienti che, per definizione, sono vicini ai dati sensibili e all’accesso di produzione.

Questo articolo analizza i tre eventi che, tra la fine del 2025 e l’inizio del 2026, hanno reso impossibile ignorare la portata del problema: la campagna Lazarus “Graphalgo”, l’attacco “XPACK ATTACK” e – soprattutto – il worm autoreplicante Shai-Hulud, che ha dimostrato che la propagazione autonoma nei registri open-source non è più teoria, ma realtà operativa.

## L’anatomia di Graphalgo: come Lazarus ha trasformato un colloquio di lavoro in un trojan multi-stadio

Il 12 febbraio 2026, [ReversingLabs ha pubblicato l’analisi dettagliata](https://www.reversinglabs.com/blog/fake-recruiter-campaign-crypto-devs) di una campagna denominata “Graphalgo” – dal nome del primo pacchetto malevolo pubblicato su npm – attribuita con grado di confidenza medio-alto al [Lazarus Group](https://www.sonatype.com/resources/whitepapers/how-lazarus-group-is-weaponizing-open-source) nordcoreano. La campagna era attiva dal maggio 2025 e rappresenta un salto qualitativo nelle operazioni di supply chain poisoning condotte da attori statali.

Il meccanismo è sofisticato nella sua semplicità psicologica. Gli attaccanti contattano sviluppatori JavaScript e Python attraverso LinkedIn, Facebook e Reddit, proponendo opportunità lavorative presso “Veltrix Capital” – una società fittizia presentata come operatore blockchain e crypto exchange, completa di domini registrati (veltrixcap[.]org, veltrixcapital[.]ai) e organizzazioni GitHub con repository apparentemente legittimi. Ai candidati viene chiesto di completare un “coding test” come parte del processo di selezione. I repository contengono dipendenze che puntano a pacchetti compromessi su npm e PyPI.

Qui sta il genio tattico: quando la vittima esegue o fa il debug del codice di test, il package manager installa automaticamente le dipendenze malevole. I pacchetti agiscono come loader di primo stadio, scaricando un Remote Access Trojan (RAT) dall’infrastruttura C2 controllata dagli attaccanti. Il RAT è in grado di eseguire comandi arbitrari, caricare e scaricare file, elencare i processi in esecuzione e – dettaglio rivelatore – verificare la presenza dell’estensione browser MetaMask, indicando un interesse specifico per il furto di asset crittografici. Sono state identificate tre varianti del RAT, scritte in JavaScript, Python e Visual Basic Script.

[ReversingLabs ha identificato](https://www.reversinglabs.com/blog/inside-graphalgo) complessivamente 192 pacchetti malevoli in due lotti distinti: quelli con “graph” nel nome (apparsi su npm dal 2 maggio 2025 e su PyPI dal giugno 2025, progettati per mimare librerie legittime come *graphlib* e *networkx*) e quelli con “big” nel nome (apparsi su npm dal 17 novembre 2025 e su PyPI dal 9 dicembre 2025, probabilmente collegati a una seconda campagna di facciata ancora non identificata).

L’esempio emblematico è il pacchetto npm *bigmathutils*: la prima versione, benign...