---
title: Aspetti tecnici della raccolta e analisi dei dati: OSINT, ADINT e Digital Forensics
url: https://www.ictsecuritymagazine.com/articoli/analisi-dei-dati/
source: ICT Security Magazine
date: 2025-11-14
fetch_date: 2025-11-15T03:09:18.216919
---

# Aspetti tecnici della raccolta e analisi dei dati: OSINT, ADINT e Digital Forensics

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

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![analisi dei dati, OSINT e digital forensics con grafici e simboli tecnologici](https://www.ictsecuritymagazine.com/wp-content/uploads/analisi-dei-dati-osint-adint.jpeg)

# Aspetti tecnici della raccolta e analisi dei dati: OSINT, ADINT e Digital Forensics

A cura di:[Sergiu Deaconu](#molongui-disabled-link)  Ore 14 Novembre 20254 Novembre 2025

L’analisi dei dati rappresenta oggi il fulcro delle moderne strategie di intelligence digitale. Questo articolo fa parte di una serie di approfondimenti dedicati all’Open Source Intelligence (OSINT) e all’Advertising Intelligence (ADINT), esplorando le loro applicazioni innovative e gli impatti significativi in ambito industriale, civile e dell’intelligence europea.

Il presente contenuto esamina in dettaglio l’approccio OSINT, analizzando come l’utilizzo di fonti pubblicamente accessibili – dai social media agli archivi web – possa fornire informazioni cruciali per la sicurezza digitale. Viene inoltre presentato l’innovativo approccio ADINT, che sfrutta i dati del tracking pubblicitario per scopi investigativi, aprendo nuove frontiere nell’intelligence moderna.

## L’approccio OSINT

#### Fonti pubbliche e social media

L’OSINT (Open Source Intelligence) si basa sull’analisi di dati provenienti da fonti pubblicamente accessibili. Come evidenziato da Yadav et al. (2023), l’utilizzo crescente di Internet e del World Wide Web ha portato ad una crescita esponenziale delle informazioni disponibili, con particolare rilevanza per i professionisti della cybersecurity. Le fonti OSINT includono principalmente archivi web, database pubblici, indirizzi e-mail e social network come Facebook, X, LinkedIn.

La rilevanza dell’OSINT è cresciuta significativamente negli ultimi anni, portando ad un dibattito sulle modalità di raccolta dei dati tra il settore militare, governativo e commerciale. Le sfide principali riguardano l’acquisizione di dati rilevanti, il loro sfruttamento e la loro successiva condivisione per soddisfare specifici requisiti di intelligence (Nouh et al., 2019).

I dati raccolti da piattaforme come X e Facebook includono immagini, video, post testuali e metadati, che possono essere analizzati per identificare pattern comportamentali o geolocalizzazioni. Ad esempio, l’uso di hashtag specifici su X (all’epoca Twitter) ha permesso agli analisti OSINT di seguire il movimento di manifestanti durante eventi come le proteste di Hong Kong del 2019 (Clarke & Knake, 2020). Tuttavia, l’analisi dei social media presenta sfide significative. Ad esempio, la grande quantità di dati disponibili può causare la cosiddetta *“information overload”*[[1]](#_ftn1), mentre la presenza di *fake news* e *bot* richiede un’attenta verifica delle fonti. Strumenti come “Hoaxy”[[2]](#_ftn2) e “Botometer”[[3]](#_ftn3) sono stati sviluppati per affrontare queste problematiche, migliorando la capacità degli analisti di distinguere tra contenuti autentici e manipolati.

Hoaxy è uno strumento progettato per tracciare la diffusione di contenuti online, come notizie false o informazioni manipolate, attraverso i social network. Funziona analizzando le condivisioni e le interazioni relative a specifici articoli o argomenti, mostrando visivamente come si propagano nei social network (come ad esempio X). Questo strumento consente agli analisti di identificare i nodi principali, analizzare i percorsi di propagazione e infine di rilevare potenziali segnali di manipolazione (un esempio può essere quello di un’alta frequenza di condivisione in tempi molto brevi, che potrebbe indicare l’utilizzo di *bot*).

Botometer invece è uno strumento che valuta la probabilità che un account su X (ex Twitter) sia controllato da un *bot* anziché da un essere umano. Utilizza algoritmi di apprendimento automatico per analizzare diversi aspetti dell’attività di un account, tra cui i metadati, le caratteristiche linguistiche, la connettività e infine l’attività temporale. Inoltre, questo strumento assegna un punteggio che indica la probabilità che un account sia automatizzato e ciò è particolarmente utile per rilevare campagne di manipolazione che utilizzano reti di *bot* per amplificare contenuti specifici o distorcere il dibattito pubblico.

#### Tecniche di aggregazione

Le tecniche di aggregazione sono fondamentali per gestire l’enorme volume di dati disponibili attraverso l’OSINT. Come descritto da Vasilaras et al. (2024), l’efficacia degli strumenti OSINT dipende fortemente dalla loro capacità di automatizzare la raccolta e l’analisi dei dati e con l’aiuto di software specializzati è possibile estrarre informazioni da diverse fonti, inclusi metadati delle immagini (i sopracitati EXIF), dati di geolocalizzazione e informazioni sui dispositivi. Un aspetto cruciale evidenziato dalla ricerca è l’importanza della validazione delle fonti e della verifica dell’autenticità delle informazioni raccolte, e per questo motivo gli strumenti OSINT moderni integrano sempre più spesso funzionalità di machine learning e di IA per migliorare l’accuratezza dell’analisi e ridurre i falsi positivi.

Un esempio interessante di utilizzo di tecniche di aggregazione è stato descritto da Kaplan (2021), il quale ha mostrato come l’analisi incrociata di dati provenienti da social media e registri pubblici possa rivelare connessio...