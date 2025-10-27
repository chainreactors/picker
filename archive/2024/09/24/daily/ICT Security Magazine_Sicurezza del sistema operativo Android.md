---
title: Sicurezza del sistema operativo Android
url: https://www.ictsecuritymagazine.com/articoli/sicurezza-del-sistema-operativo-android/
source: ICT Security Magazine
date: 2024-09-24
fetch_date: 2025-10-06T18:30:25.322748
---

# Sicurezza del sistema operativo Android

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Sicurezza-del-sistema-operativo-Android.jpg)

# Sicurezza del sistema operativo Android

A cura di:[Alessio Merlo](#molongui-disabled-link)  Ore 23 Settembre 202415 Ottobre 2024

L’architettura del sistema operativo Android, rappresentata in Figura 6[[1]](#_ftn1), ha caratteristiche uniche. Costruita con la filosofia di essere un ambiente completamente *open*, che ogni soggetto potesse modificare a suo piacimento, Android è formato da un insieme di componenti eterogenei, in buona parte *“off-the-shelf”* – ovvero liberamente disponibili sul mercato – e integrati.

Introdurremo brevemente le caratteristiche utili a capire il funzionamento di Android attraverso queste componenti, in modo da poter poi ragionare sulle principali problematiche di sicurezza.

![funzionamento di Android e principali problematiche di sicurezza.](https://www.ictsecuritymagazine.com/wp-content/uploads/6-1.png)

Figura 6: Architettura di Android 13

Il *kernel* di Android (in rosso nell’immagine) è un *kernel* Linux generico, multi-utente, in uso su desktop e server. Una simile scelta permette ai produttori di comporre l’hardware dello *smartphone* che intendono commercializzare con molti gradi di libertà, in quanto è estremamente probabile che, per ogni componente hardware assemblato, sia disponibile il corrispondente *driver* Linux. La definizione di un *kernel* nuovo, *ad hoc* per Android, avrebbe magari potuto essere più performante, specie sui primi dispositivi con poca disponibilità hardware; tuttavia, avrebbe limitato le possibilità dei produttori di *smartphone*, che avrebbero dovuto attendere lo sviluppo del corrispondente *driver* per poter aggiungere uno specifico componente alla propria architettura, con il rischio di una riduzione della diffusione di Android.

L’*Hardware Abstraction Layer* (HAL – in azzurro) è un insieme di moduli di libreria, ognuno specifico per una componente hardware. Lo scopo di tutti gli HAL è semplificare la comunicazione tra i servizi dei livelli superiori del sistema operativo e l’hardware: ad esempio, questo permette ai livelli più alti del sistema operativo (in particolare al *Java API Framework*) di ignorare le specificità dei *driver* sottostanti per poter comunicare con i componenti hardware corrispondenti, nonché di utilizzare un set di istruzioni standard eseguite su astrazioni indipendenti dall’attuale componentistica dello *smartphone*. È compito poi delle funzioni di libreria dell’HAL tradurre i comandi nei corrispondenti sui *driver* specifici del *kernel*.

Android si basa su un insieme di librerie native (in viola), ovvero scritte in C/C++, che sono state inserite a supporto delle funzionalità, anche in questo caso, del Java API Framework e delle app. Tali librerie, ampiamente disponibili *“off-the-shelf”*, sono state inserite con la filosofia di riutilizzare quanto già disponibile, senza doverlo riscrivere. Rientrano in questo gruppo, tra le altre, le librerie per il *rendering* 2D e 3D (usate estensivamente dai videogiochi) e le librerie con i font e i codec audio/video supportati dallo *smartphone*.

L’*Android Runtime* (in giallo) è l’ambiente di esecuzione delle app. ART è una macchina virtuale in grado di eseguire il codice delle app, compilandolo nell’architettura nativa dello *smartphone* durante l’installazione. Per l’esecuzione, si basa su un insieme di librerie Java chiamate *Core Libraries* che corrispondono a un sottoinsieme dell’SDK di Java, più un insieme di classi specifiche di Android.

Il *Java API Framework* (in verde) implementa un insieme di servizi fondamentali che supportano l’esecuzione delle app, fornendo l’accesso ai servizi dei livelli sottostanti del sistema operativo, nonché la comunicazione tra app tramite uno specifico *driver* del *kernel* chiamato Binder. Ogni servizio è specifico per un certo tipo di attività: gestire l’installazione delle app, il loro ciclo di vita quando in esecuzione, la posizione, le telefonate e le notifiche, nonché il *rendering* delle schermate delle app. Questo componente del sistema operativo è stato completamente implementato da zero.

Infine, le app (in blu) occupano il livello gerarchico più alto e sfruttano tutti i servizi sottostanti per la loro esecuzione.

## Aspetti e problemi di sicurezza di Android

Da un punto di vista della sicurezza, il sistema operativo ha una doppia valenza. Da una parte, come ogni pezzo di software, contiene delle vulnerabilità ed è soggetto al *threat model* del *confused deputy* che abbiamo presentato precedentemente. In questo caso, come per le app, l’attacco può provenire da app malevole installate dall’utente; tuttavia alcuni attacchi possono essere eseguiti anche dall’esterno tramite le connessioni di rete (Wi-Fi, 5G, Bluetooth, NPC), anche se in letteratura questi attacchi sono molto specifici, limitati e appartenenti soprattutto alle prime versioni del sistema operativo.

D’altra parte, Android è anche la componente che deve essere modificata in prima battuta per “hardenizzare” il canale di comunicazione tra app, per ridurre, come discusso, la probabilità che un *malware* installato possa attaccare con successo un’app vulnerabile o lo stesso sistema operativo. Come si può intuire la parte di *hardening* richi...