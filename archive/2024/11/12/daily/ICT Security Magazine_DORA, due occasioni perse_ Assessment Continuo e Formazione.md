---
title: DORA, due occasioni perse: Assessment Continuo e Formazione
url: https://www.ictsecuritymagazine.com/articoli/assessment-formazione-dora/
source: ICT Security Magazine
date: 2024-11-12
fetch_date: 2025-10-06T19:21:20.600512
---

# DORA, due occasioni perse: Assessment Continuo e Formazione

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

![Regolamento DORA 7layers](https://www.ictsecuritymagazine.com/wp-content/uploads/regolamento-dora.jpg)

# DORA, due occasioni perse: Assessment Continuo e Formazione

A cura di:[Fabrizio Baiardi](#molongui-disabled-link)  Ore 11 Novembre 2024

Due premesse sono necessarie. La prima è che sono stato membro di un gruppo di lavoro di AIEA, associazione italiana degli EDP auditor, su DORA. Ovviamente tutto quanto discusso in questo articolo sono le mie opinioni personali e non quelle del gruppo di lavoro o della associazione. La seconda premessa è che non ho né mai avrò una mentalità legale in grado di analizzare le leggi ed i regolamenti e le loro nascoste relazioni, rinvii o contraddizioni.

Quello che mi interessa è capire il contesto e l’analisi del contesto che ha portato a definire una legge. Ciò mi rende costituzionalmente incapace di risolvere il problema di come sia possibile rispettare formalmente una norma mentre in realtà la si viola. So bene che il problema è molto importante nel mondo reale ed anche in quello accademico, ma purtroppo nel seguito non troverete una soluzione.

Detto questo, i due principali punti del regolamento DORA che voglio evidenziare sono la frequenza dei Threat Lead Penetration Test, TLPT, in pratica un penetration test dove si emula una specifica minaccia, e quello del team che questo TLPT deve eseguire. Accennerò ad altri problemi sulla notifica di incidenti. Di seguito discuterò questi punti dopo aver descritto brevemente lo scenario attuale delle intrusioni nei sistemi informatici che è la causa principale delle mie obiezioni.

## Intrusioni: lo scenario attuale

Riassumo brevemente lo scenario attuale delle intrusioni informatiche e quello dell’ecosistema criminale che le genera per individuare alcune caratteristiche generali delle attuali minacce, cioè degli attuali attaccanti

### Le intrusioni accelerano

Quasi tutte le analisi concordano nell’evidenziare che le intrusioni stanno diventando più veloci e più stealth, ovvero più difficili da individuare. Queste tendenze sono favorite da un lato da un ecosistema criminale dove i potenziali attaccanti trovano in vendita, grazie agli initial access broker, i fornitori di accessi iniziali alla infrastruttura informatica di una organizzazione.

Utilizzando questo accesso un attaccante può iniziare la sua intrusione dall’interno del sistema target riducendo cosi sensibilmente il tempo necessario per una intrusione. Il gran numero di access broker è provato dal crescente numero di annunci pubblicitari esistenti sui mercati nel dark web dove ogni broker elogia le proprie offerte indicando, ad esempio, il fatturato delle aziende che possiedono le infrastrutture di cui si vende un accesso.

Gli stessi mercati offrono malware, ad esempio per intrusioni ransomware in cambio di una percentuale dei ricavi. La forte competizione tra fornitori, come nel caso degli initial access broker porterà, come in tutti i mercati, ad una riduzione dei prezzi che aumenterà la redditività delle intrusioni, basta pensare che esistono accessi che costano meno di 10 *.*

L’offerta dei mercati nel dark web permette anche a criminali non particolarmente esperti di creare intrusioni acquistando gli strumenti necessari invece di svilupparli. Ciò aumenta sia il numero di attaccanti che di intrusioni e quindi anche la probabilità di essere attaccati. L’aumento degli attaccanti è dovuto anche alla diffusione di piattaforme offensive in grado di eseguire automaticamente alcuni o tutti i passi di una intrusione La condivisione di malware e piattaforme d’attacco tramite i mercati sul dark web permette ad un gruppo criminale di modificare velocemente le proprie strategie e le proprie tecniche di attacco se e quando i difensori applicano contromisure efficaci.

### Vivi dei frutti della tua terra

Un’altra ragione dell’accelerazione delle intrusioni è la diffusione di strategie quali la *living of the land* o, in breve, LOTL. Questa strategia prevede che l’attaccante utilizzi al massimo strumenti già esistenti nel sistema da attaccare, la terra che lo alimenta, risparmiando il tempo per sviluppare o personalizzare i propri strumenti.

Quindi l’attaccante non userà una propria shell ma quella di amministrazione, non userà dei propri strumenti per eliminare strumenti di difesa ma, come avvenuto, manipolerà quelli di end point protection per far si che considerino malware gli strumenti di difesa e li eliminino. In intrusioni LOTL, gli attaccanti creano inizialmente una proprio accesso permanente a risorse periferiche di un sistema, ad esempio il router di frontiera che connette il sistema ad internet oppure le VPN appliances, i firewalls o i routers, fase detta anche living on the edge.

Successivamente, usano l’accesso permanente per capire quali sono gli strumenti utilizzati nel sistema target e come usarli a loro favore. La strategia LOTL è molto popolare tra APT ed attaccanti state sponsored, quelli più interessati agli impatti di tipo sistemico che la direttiva DORA vorrebbe prevenire. LOTL è stata inizialmente utilizzata da alcuni attaccanti state sponsored da paesi dell’estremo oriente ma, per la sua efficacia, si è diffusa rapidamente ad altri attaccanti stati sponsored ma di paesi dell’europa orientale.

Ad esempio, un recente rapporto Ma...