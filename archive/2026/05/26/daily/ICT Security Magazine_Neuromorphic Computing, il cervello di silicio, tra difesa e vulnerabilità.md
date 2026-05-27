---
title: Neuromorphic Computing, il cervello di silicio, tra difesa e vulnerabilità
url: https://www.ictsecuritymagazine.com/articoli/neuromorphic-computing/
source: ICT Security Magazine
date: 2026-05-26
fetch_date: 2026-05-27T06:12:34.162992
---

# Neuromorphic Computing, il cervello di silicio, tra difesa e vulnerabilità

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Neuromorphic Computing](https://www.ictsecuritymagazine.com/wp-content/uploads/neuromorphic-computer.jpeg)

# Neuromorphic Computing, il cervello di silicio, tra difesa e vulnerabilità

A cura di:[Redazione](#molongui-disabled-link)  Ore 26 Maggio 202614 Maggio 2026

Quando i chip cominciano a pensare come neuroni, la cybersecurity deve fare i conti con regole del gioco completamente inedite.

## Un nuovo paradigma computazionale

Per decenni l’industria informatica ha costruito i propri fondamenti sull’architettura di Von Neumann: processore separato dalla memoria, ciclo *fetch-decode-execute*, flusso di dati lineare. Uno dei principali ostacoli alla riduzione di latenza e consumo energetico nell’inferenza AI è proprio il cosiddetto [collo di bottiglia di Von Neumann](https://research.ibm.com/blog/northpole-llm-inference-results): in quasi tutti i microprocessori moderni la memoria è fisicamente separata dal processore, e lo spostamento continuo dei dati tra le due unità limita la velocità e consuma elettricità.

Il *neuromorphic computing* rompe questa logica partendo da un’analogia biologica radicale. L’approccio mira a [progettare hardware e software](https://www.ibm.com/think/topics/neuromorphic-computing) che simulino le strutture e le funzioni neurali e sinaptiche del cervello umano per elaborare informazioni. Le sue origini risalgono agli anni Ottanta, quando Misha Mahowald e Carver Mead svilupparono i primi neuroni e sinapsi in silicio. Oggi, però, la maturazione tecnologica ha trasformato quello che era un esperimento accademico in un settore con ricadute concrete su sicurezza, difesa e intelligenza artificiale distribuita.

Il meccanismo fondamentale su cui si basano questi sistemi è la rete neurale a impulsi, o *Spiking Neural Network* (SNN). A differenza delle reti neurali artificiali convenzionali che elaborano valori continui, [le SNN operano con impulsi](https://www.onoff.gr/blog/en/future/neuromorphic-chips-think-like-brain/): un neurone artificiale accumula carica e, quando supera una soglia, genera uno *spike*. Se non richiesto, rimane inattivo, e inattivo significa consumo energetico pari a zero. I neuroni biologici trasmettono segnali solo in risposta a cambiamenti, con un processamento sparso, parallelo e adattivo, consumando circa 20 watt per capacità di riconoscimento dei *pattern* di livello straordinario.

## L’hardware: da Loihi a Hala Point, passando per TrueNorth

I protagonisti industriali di questo panorama sono essenzialmente due, Intel e IBM, con una platea crescente di attori specializzati.

[Il chip Loihi di Intel Labs](https://open-neuromorphic.org/neuromorphic-computing/hardware/loihi-intel/), annunciato formalmente nel 2017, integra 128 *core* neuromorfi, 3 processori x86 e oltre 33 MB di memoria SRAM *on-chip*, supportando reti neurali a impulsi asincroni fino a 130.000 neuroni compartimentali sintetici e 130 milioni di sinapsi, fabbricato su processo a 14 nm. La seconda generazione, Loihi 2, ha spinto ulteriormente le prestazioni: introdotto alla fine del 2021, conta circa un milione di neuroni per *chip* con programmabilità migliorata rispetto al predecessore.

Il confronto tra le generazioni è significativo: Loihi 2 supera il predecessore con una capacità di elaborazione fino a dieci volte superiore ed è accompagnato da *Lava*, un *framework open source* che supporta più metodi AI e hardware per lo sviluppo di applicazioni neuro-ispirate.

Il progetto più ambizioso di Intel si chiama Hala Point. **Hala Point, il più grande sistema neuromorfico di Intel ad oggi, contiene 1,15 miliardi di neuroni** e racchiude 1.152 processori Loihi 2 prodotti su [nodo di processo Intel 4](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai/) in uno *chassis* per *data center* da sei unità *rack* delle dimensioni di un forno a microonde. Il sistema supporta fino a 1,15 miliardi di neuroni e 128 miliardi di sinapsi distribuiti su 140.544 *core* di elaborazione neuromorfica, con un consumo massimo di 2.600 watt, e include oltre 2.300 processori x86 integrati per calcoli ausiliari.

Le prestazioni del sistema sono state misurate ufficialmente da Intel: i sistemi basati su Loihi possono eseguire inferenza AI e risolvere problemi di ottimizzazione usando **cento volte meno energia** a velocità fino a cinquanta volte superiori rispetto ad architetture CPU e GPU convenzionali, raggiungendo efficienze fino a 15 TOPS/W su *deep neural network* convenzionali senza necessità di raggruppare i dati in *batch*. Hala Point è stato inizialmente distribuito presso i Sandia National Laboratories per la ricerca in ambito AI e difesa.

Sul fronte IBM, il percorso evolutivo è stato differente. TrueNorth, introdotto nel 2014, è un processore di rete su *chip* con 4.096 *core*, ciascuno con 256 neuroni programmabili simulati, per un totale di poco più di un milione di neuroni. IBM dichiara un consumo di soli 70 milliwatt e una densità di potenza pari a un diecimillesimo di quella dei microprocessori convenzionali.

Nel 2023, con NorthPole, IBM ha compiuto un ulteriore salto qualitativo. [NorthPole è un’estensione di TrueNorth](https://research.ibm.com/blog/northpole-ibm-ai-chip), progettata per ...