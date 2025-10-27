---
title: Quale crittografia per gli scenari digitali del futuro?
url: https://www.ictsecuritymagazine.com/articoli/quale-crittografia-per-gli-scenari-digitali-del-futuro/
source: ICT Security Magazine
date: 2023-03-15
fetch_date: 2025-10-04T09:38:39.991070
---

# Quale crittografia per gli scenari digitali del futuro?

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Fully-Homomorphic-Encryption-1.jpg)

# Quale crittografia per gli scenari digitali del futuro?

A cura di:[Luigi Perrone](#molongui-disabled-link)  Ore 14 Marzo 202314 Marzo 2023

Nel mondo digitale di oggi è oramai diventata consuetudine parlare di protezione dei dati in modo da garantire la riservatezza in qualunque stadio essi si trovino (at-rest, in-fly in-use), anche in caso di una loro esfiltrazione e divulgazione. Ma tutto questo può essere sufficiente per il futuro che ci aspetta?

Osservando con attenzione le attuali architetture di sicurezza per la protezione dei dati, notiamo come siano sempre presi in considerazione i due stadi più comuni in cui può trovarsi il dato, “at-rest” e “in-fly”, molto più raramente quando il dato è “in-use”. In presenza di ambienti cloud, ibridi o comunque aperti, dove il dato deve essere inevitabilmente trattato, ecco che si crea una grande vulnerabilità in quanto occorre decifrare il dato per poterlo elaborare, esponendolo così ad ogni tipo di attacco.

Applicando la tecnologia Fully Homomorphic Encryption (FHE) l’esposizione del dato “in-use” non costituisce più preoccupazione. Infatti FHE consente di operare con calcoli ed operazioni (come addizione e moltiplicazione e funzioni booleane) direttamente su dati crittografati. Il titolare del dato, potrà esporre tranquillamente le proprie informazioni sensibili, dopo averle cifrate con FHE, rendendole disponibili per qualsiasi tipo di elaborazione che verrà eseguita solo in modalità cifrata, quindi senza pericolo di violazione dei dati originali. La stessa elaborazione produrrà un risultato anch’esso cifrato, come se fosse stato prodotto con i dati non cifrati (fatto salvo una certa tolleranza di errore). Tale risultato cifrato potrà infine essere letto solo ed esclusivamente dal titolare che detiene la chiave privata con cui è possibile decifrare il dato.

### FHE utilizza diversi schemi crittografici

Entrando un po’ più nello specifico, FHE utilizza diversi schemi crittografici, come BGV, BFV, TFHE e CKKS. Questi schemi differiscono tra loro per il tipo di numeri con cui sono in grado di operare. Ad esempio, BGV, BFV e TFHE operano su numeri interi. Lo schema CKKS si utilizza invece con numeri reali o complessi (tipicamente nelle applicazioni di AI/ML utilizzate con le reti neurali). Questi schemi si basano essenzialmente su una tecnica chiamata Learning with Errors (LWE) che, come dice la parola stessa, introduce errori di tolleranza. In particolare LWE introduce un errore nel testo cifrato per fornire sicurezza. Questo errore continua a crescere man mano che si eseguono le operazioni sui dati crittografati finché a un certo punto non è più possibile continuare. Quindi, per continuare e preservare i risultati computazionali, diventa necessario usare il metodo di “bootstrap” utile per ridurre l’errore nel testo cifrato aggiunto intenzionalmente per proteggere lo schema. Ciò consente, in linea di principio, di continuare a eseguire tutti i calcoli, ma è anche vero che, tale operazione può diventare molto costosa e può degradare notevolmente le prestazioni. Poi abbiamo lo schema BGV dove l’errore nel testo cifrato è effettivamente nascosto all’utente, nel senso che quando l’utente esegue il decrypting del dato, non è in grado di rilevare l’errore. Mentre nello schema CKKS, l’errore viene crittografato nei dati stessi. In questo modo, quando l’utente decifra, non riceve il valore esatto, ma il valore sommato di qualche errore.

### Una crittografia quantum-resistant

Oggi la FHE è considerata una crittografia quantum-resistant. Pertanto non vi è alcun vantaggio nell’usare un processore quantistico per violare l’algoritmo di crittografia FHE poichè questo si basa proprio su presupposti di difficoltà computazionale con primitive che utilizzano i metodi/schemi omomorfici descritti in precedenza e che risultano sicuri e resistenti ai quanti. Lo schema originale di Craig Gentry, l’ideatore della FHE, è basato sui reticoli, un tipo di schema che è generalmente difficile da risolvere dai computer quantistici in quanto non suscettibile all’algoritmo di Shor. E’ per questo motivo che la FHE si candida ad essere una delle possibili soluzioni per la protezione del dato dai futuri attacchi digitali perpetrati tramite Quantum Computer.

### Requisiti hardware e software

Allo stato attuale FHE può essere facilmente sperimentata utilizzando il solo software in quanto non c’è alcuna dipendenza dall’hardware. Basta avere la disponibilità di un ambiente Docker per consentire agli sviluppatori di creare ed eseguire applicazioni distribuite. Nella maggior parte dei casi d’uso quasi tutti i moderni PC, laptop o dispositivi mobili dispongono di risorse sufficienti per eseguire attività FHE di test. Certo, se si tratta di applicazioni lato server con calcolo crittografato intenso, allora occorre esaminare bene il caso d’uso scoprendo che avere la disponibilità di sistemi ad alta capacità computazionale come i nuovi Mainframe faciliterebbe non poco. Possiamo dire però, che normalmente, per uno sviluppo un pò serio di prototipi significativi è bene avere a disposizione almeno 32 GB di RAM ed una CPU con almeno 4 core. Infatti le prestazioni di FHE scalano piuttosto b...