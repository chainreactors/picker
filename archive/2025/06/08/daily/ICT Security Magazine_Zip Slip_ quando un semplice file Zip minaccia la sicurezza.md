---
title: Zip Slip: quando un semplice file Zip minaccia la sicurezza
url: https://www.ictsecuritymagazine.com/articoli/zip-slip-vulnerability/
source: ICT Security Magazine
date: 2025-06-08
fetch_date: 2025-10-06T22:53:33.350691
---

# Zip Slip: quando un semplice file Zip minaccia la sicurezza

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

![Zip Slip: quando un semplice file Zip minaccia la sicurezza informatica](https://www.ictsecuritymagazine.com/wp-content/uploads/zip-slip-vulnerabilita.jpeg)

# Zip Slip: quando un semplice file Zip minaccia la sicurezza

A cura di:[Redazione](#molongui-disabled-link)  Ore 7 Giugno 202530 Maggio 2025

La vulnerabilità Zip Slip, una minaccia tanto sottile quanto devastante che ha colpito giganti tecnologici come Oracle, Amazon, Google, LinkedIn e Twitter.

## Un nemico silenzioso nel mondo digitale

Pensate a quante volte al giorno scaricate, aprite o condividete file ZIP. Documenti di lavoro, foto delle vacanze, software, backup: gli archivi compressi sono diventati parte integrante della nostra vita digitale. Ma cosa succederebbe se vi dicessi che dietro quella innocua icona di una cartella compressa si può nascondere una delle minacce informatiche più subdole e devastanti degli ultimi anni?

La storia che sto per raccontarvi inizia nel 2018, quando un gruppo di ricercatori della società di cybersecurity Snyk ha fatto una scoperta che ha letteralmente scosso il mondo della tecnologia. Hanno identificato una vulnerabilità così semplice nel suo funzionamento, eppure così devastante nelle sue conseguenze, da aver colpito migliaia di progetti software utilizzati quotidianamente da miliardi di persone in tutto il mondo.

Questa vulnerabilità ha un nome che suona quasi innocuo: Zip Slip. Ma non lasciatevi ingannare dalla semplicità del nome. Zip Slip ha la capacità di trasformare un normale file ZIP in uno strumento che può permettere a un attaccante di prendere completamente il controllo del vostro computer, rubare i vostri dati più sensibili o utilizzare il vostro sistema come trampolino di lancio per attacchi ancora più devastanti.

#### Il meccanismo dell’inganno: come funziona Zip Slip

Per capire come funziona Zip Slip, dobbiamo prima comprendere cosa succede normalmente quando il vostro computer apre un file ZIP. Immaginate il vostro sistema operativo come una grande biblioteca con scaffali ben organizzati. Quando decomprimete un archivio, è come se steste prendendo una scatola di libri e li steste sistemando sullo scaffale giusto.

Normalmente, se la scatola contiene un libro chiamato “Ricette della Nonna”, questo finirà nella sezione cucina della vostra biblioteca digitale.

Ma cosa succederebbe se qualcuno riuscisse a etichettare quel libro in modo ingannevole? Invece di chiamarlo semplicemente “Ricette della Nonna”, lo etichettasse come “../../Sistema/Password/Ricette della Nonna”? Il vostro bibliotecario digitale, seguendo ciecamente l’etichetta, non metterebbe il libro nella sezione cucina, ma seguirebbe il percorso indicato: uscirebbe dalla sezione attuale, risalirebbe di due livelli nella gerarchia della biblioteca, entrerebbe nella sezione Sistema e poi in quella Password, sistemando il libro (che in realtà contiene codice malevolo) in un luogo dove non dovrebbe mai trovarsi.

Questo è esattamente ciò che accade con Zip Slip. Gli attaccanti creano archivi ZIP che contengono file con nomi speciali, che includono quelle che tecnicamente vengono chiamate “sequenze di attraversamento delle directory”. Questi nomi di file contengono simboli come “../” che dicono al sistema operativo: “non mettere questo file dove dovrebbe andare normalmente, ma seguimi mentre navigo fuori dalla cartella sicura verso zone molto più sensibili del sistema”.

Una volta che un file malevolo è riuscito a “scappare” dalla sua opportuna destinazione e a finire in una posizione critica del sistema – come le cartelle che contengono le password degli utenti, i programmi che si avviano automaticamente all’accensione del computer, o i file di configurazione dei servizi più importanti – l’attaccante ha essenzialmente vinto la partita.

#### La grande rivelazione del 2018: un terremoto nel mondo della tecnologia

Quando i ricercatori di Snyk hanno reso pubblica la loro scoperta il 5 giugno 2018, l’industria tecnologica si è trovata di fronte a una verità sconcertante. Non si trattava di una vulnerabilità che colpiva un singolo software o una specifica azienda. Era un problema sistemico che attraversava praticamente tutto l’ecosistema software moderno.

L’elenco delle aziende e dei progetti colpiti leggeva come un “chi è chi” della tecnologia mondiale. Oracle, il gigante dei *database enterprise* utilizzati da migliaia di aziende in tutto il mondo, doveva fare i conti con software vulnerabile. Amazon, con la sua vasta infrastruttura cloud che supporta una parte significativa di Internet, aveva componenti a rischio. Google, dalle cui applicazioni dipendono miliardi di utenti quotidianamente, aveva prodotti che necessitavano di correzioni urgenti.

Ma non erano solo i colossi tecnologici a essere colpiti. LinkedIn, dove professionisti di tutto il mondo condividono informazioni sensibili sulla loro carriera, aveva vulnerabilità da correggere. Twitter, la piattaforma dove si svolgono dibattiti globali e si condividono notizie in tempo reale, doveva mettere in sicurezza i suoi sistemi. Anche Alibaba, il gigante dell’e-commerce che gestisce transazioni per miliardi di dollari, si è trovata a dover affrontare il problema.

Quello che rendeva la situazione ancora più preoccupante era la diversità dei contesti colpiti. Non ...