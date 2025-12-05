---
title: Machine Learning e cybersecurity: potenzialità e limiti nell’individuazione delle minacce
url: https://www.ictsecuritymagazine.com/articoli/machine-learning-minacce/
source: ICT Security Magazine
date: 2025-12-04
fetch_date: 2025-12-05T03:19:02.883513
---

# Machine Learning e cybersecurity: potenzialità e limiti nell’individuazione delle minacce

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
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

![Il Professor Giorgio Giacinto al 23° Forum ICT Security parla di machine learning per individuare componenti malevoli nelle applicazioni Android](https://www.ictsecuritymagazine.com/wp-content/uploads/Untitled-design-5.png)

# Machine Learning e cybersecurity: potenzialità e limiti nell’individuazione delle minacce

A cura di:[Giorgio Giacinto](#molongui-disabled-link)  Ore 4 Dicembre 20253 Dicembre 2025

*Intervento di Giorgio Giacinto al 23° Forum ICT Security – “Il Machine Learning aiuta a individuare i componenti malevoli di una minaccia?”*

Il *machine learning* rappresenta oggi uno strumento imprescindibile nella lotta contro le minacce informatiche, ma la sua efficacia dipende da una progettazione accurata e dalla consapevolezza dei suoi limiti intrinseci. È questo il messaggio centrale emerso dall’intervento del Professor Giorgio Giacinto, ordinario di Ingegneria Informatica presso l’Università di Cagliari, durante il [23° Forum ICT Security](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025#evento) tenutosi a Roma il 19 e 20 novembre 2025.

Lo *speaker* ha aperto la sua relazione contestualizzando il tema all’interno del panorama della ricerca italiana in cybersicurezza, citando il progetto SERICS (*Security and Rights in the Cyberspace*), un partenariato esteso finanziato dal PNRR che ha coinvolto l’intero sistema universitario nazionale. L’iniziativa, nata in seno al Cybersecurity National Lab del CINI, ha dato vita a 27 progetti di ricerca, cui si aggiungono altri 54 finanziati attraverso bandi a cascata, con l’assunzione di 134 nuovi ricercatori e un investimento complessivo di 113 milioni di euro.

## Dall’interpretazione dei sensi umani alla cybersecurity

L’esperto ha ricordato come l’intelligenza artificiale abbia mosso i primi passi nell’interpretazione dei sensi umani: immagini, video, suoni. La sfida attuale consiste nel trasferire questa conoscenza, maturata in un contesto “umano”, verso un mondo completamente artificiale come quello informatico. I fattori chiave di questo sviluppo sono stati molteplici: modelli sempre più sofisticati capaci di simulare alcuni aspetti specifici del ragionamento umano, l’accumulo di enormi quantità di dati, le tecnologie IoT e la crescente disponibilità di risorse computazionali.

Applicando queste tecniche alla cybersecurity, il relatore ha evidenziato come gli attacchi stiano diventando sempre più sofisticati per diverse ragioni: sono realizzati con componenti diverse, ciascuna delle quali presa singolarmente non appare malevola; vengono eseguiti in più fasi; assomigliano sempre più ad attività legittime; sfruttano vulnerabilità del software non immediatamente emergenti. Ha citato come esempio recente le vulnerabilità scoperte in applicazioni come WhatsApp, dove un eseguibile malevolo era stato nascosto all’interno di un’immagine contenuta in un file zip.

## L’analisi delle applicazioni Android: un caso di studio illuminante

Particolarmente interessante è stato l’approfondimento sulle tecniche di analisi del *malware* per applicazioni Android. L’approccio adottato dal gruppo di ricerca dell’Università di Cagliari non si è limitato a far apprendere al sistema l’applicazione nella sua interezza, ma ha proceduto scomponendola in componenti elementari: da un lato il codice, dall’altro le risorse associate, come le immagini potenzialmente utilizzate per nascondere contenuti malevoli.

Un esperimento particolarmente significativo ha riguardato la rappresentazione semplificata delle applicazioni attraverso la sequenza delle chiamate a funzioni critiche, ovvero quelle che il sistema Android stesso definisce come sensibili (accesso alla rete, al Bluetooth, alla localizzazione). L’obiettivo non era tanto dimostrare se un’applicazione fosse malevola o meno, quanto verificare la possibilità di spiegare all’esperto umano quali componenti rendessero sospetta un’applicazione.

![machine learning](https://www.ictsecuritymagazine.com/wp-content/uploads/Capacita-di-rilevazione-nelle-Applicazioni-Android.png)

Capacità di rilevazione nelle Applicazioni Android

I risultati hanno messo in luce un fenomeno cruciale: nel 2018 si è verificato un crollo significativo nelle prestazioni del sistema di rilevamento. La causa? Android aveva modificato in modo sostanziale il paradigma di programmazione delle applicazioni, rendendo obsoleto l’addestramento precedente del modello. Questo episodio dimostra plasticamente come i sistemi di *machine learning* dipendano strettamente dai dati storici su cui sono stati addestrati.

![machine learning](https://www.ictsecuritymagazine.com/wp-content/uploads/Individuazione-componenti-malevole-nelle-Applicazioni-Android.png)

Individuazione componenti malevole nelle Applicazioni Android

L’aspetto più innovativo di questo approccio risiede nella capacità di fornire spiegazioni. Analizzando uno *spyware*, il sistema è stato in grado di indicare quali funzioni — legate ad esempio alla localizzazione GPS e alle connessioni WiFi — contribuissero maggiormente alla classificazione come malevolo. Confrontando questo risultato con l’analisi di un’applicazione legittima, dove tutte le caratteristiche puntavano verso la classificazione benigna, emerge il valore di questi strumenti per il professionista della sicurezza: non solo un verdetto, ma una spiegazione delle ragioni che lo sostengono.

## I Large Language Model entrano in gioco

L’intervento ha poi esplorato le frontiere più recenti...