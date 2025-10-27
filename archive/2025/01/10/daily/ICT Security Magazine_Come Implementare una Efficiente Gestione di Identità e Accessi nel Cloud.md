---
title: Come Implementare una Efficiente Gestione di Identità e Accessi nel Cloud
url: https://www.ictsecuritymagazine.com/notizie/gestione-di-identita-e-accessi/
source: ICT Security Magazine
date: 2025-01-10
fetch_date: 2025-10-06T20:11:49.883575
---

# Come Implementare una Efficiente Gestione di Identità e Accessi nel Cloud

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

![Gestione di Identità e Accessi nel Cloud - Carla Roncato, WatchGuard Technologies](https://www.ictsecuritymagazine.com/wp-content/uploads/gestione-di-accessi-e-identita-nel-cloud.jpg)

# Come Implementare una Efficiente Gestione di Identità e Accessi nel Cloud

A cura di:[Carla Roncato](#molongui-disabled-link)  Ore 9 Gennaio 2025

L’adozione di una moderna gestione di identità e accessi (IAM) nel Cloud è un elemento centrale in ogni roadmap di sicurezza e strategia di protezione delle informazioni basata sull’approccio zero trust. Vi sono numerose ragioni convincenti per cui le organizzazioni dovrebbero migrare verso sistemi di identità basati sul Cloud: questi sistemi offrono funzionalità come gestione unificata, governance degli accessi, single sign-on (SSO), elevata disponibilità e resilienza. Includono anche progressi nella sicurezza dell’identità, come l’autenticazione multifattore (MFA), il monitoraggio delle credenziali nel dark web e il rilevamento e la risposta alle minacce legate all’identità (ITDR).

## L’Evoluzione nella Gestione di Identità e Accessi

#### **Identity Fabric: un nuovo paradigma per la sicurezza**

Con la crescente adozione di IAM basati sul Cloud, sta emergendo un concetto chiave che sta ridefinendo l’approccio delle organizzazioni alla sicurezza: l’**identity fabric**. Questo approccio olistico consente una sicurezza basata sull’identità, superando i silos e gli strumenti disparati per offrire una visione unificata e coerente della gestione delle identità e degli accessi.

Le organizzazioni che passano dalle infrastrutture IAM tradizionali a un identity fabric sperimenteranno numerosi vantaggi, tra cui riduzione della complessità, maggiore compatibilità, automazione migliorata, orchestrazione più rapida, analisi dei rischi quasi in tempo reale e convenienza economica. Questo approccio, combinato con i principi dello zero trust e il controllo degli accessi basato su policy attraverso la rete, gli endpoint e l’identità, assicura un’applicazione coerente e una valutazione continua della sicurezza.

##### **Credenziali: il tallone d’Achille della sicurezza**

È ben noto che gli attacchi basati sulle credenziali sono la principale causa di violazioni dei dati ogni anno. Sebbene l’[autenticazione multifattore (MFA)](https://www.ictsecuritymagazine.com/articoli/lautenticazione-che-si-evolve-dalla-password-ai-token-u2f/) possa contrastare significativamente i tentativi di acquisizione di account verificando ogni richiesta di accesso degli utenti, il fattore di autenticazione primario, solitamente una password, rimane vulnerabile a usi impropri, furti e vendita. Il monitoraggio delle credenziali sul dark web si concentra sulla raccolta continua di informazioni sulle minacce da fonti in cui le credenziali vengono comunemente raccolte e vendute. Essere informati sulla potenziale esposizione delle proprie credenziali consente a utenti e aziende di gestire meglio i rischi associati a tali violazioni.

### **ITDR: L’evoluzione della risposta alle minacce**

Un’area emergente nel continuum di rilevamento e risposta avanzata alle minacce (XDR) è il rilevamento e risposta alle minacce legate all’identità (ITDR). Questa disciplina si concentra sulla protezione delle identità e delle infrastrutture di identità contro le varie tecniche utilizzate dagli attaccanti. L’ITDR comprende capacità progettate per rilevare, indagare e rispondere in modo proattivo alle minacce e anomalie legate all’identità, oltre che alle vulnerabilità presenti nelle infrastrutture di identità locali.

Rimuovere gli attori malevoli è complesso: una volta ottenuto l’accesso, possono causare danni significativi acquisendo privilegi, muovendosi lateralmente e applicando tecniche di esfiltrazione dei dati. Per questo motivo, raccomandiamo innanzitutto un approccio zero trust, in cui nessuna entità è considerata affidabile per impostazione predefinita, si applica il principio del minimo privilegio e il controllo degli accessi è basato su policy. Inoltre, promuoviamo l’implementazione dell’ITDR, in cui tutte le identità, i dispositivi e le infrastrutture di identità sono monitorati attraverso la raccolta continua di eventi, correlazione dei segnali, punteggio del rischio e azioni di risposta, allineate con la matrice ATT&CK di MITRE, un framework ampiamente utilizzato per descrivere i comportamenti degli attaccanti.

## **Il futuro della sicurezza delle identità**

Man mano che le organizzazioni migrano verso il cloud, la sicurezza delle identità è diventata una componente cruciale di qualsiasi strategia di cybersecurity. Adottare un identity fabric e tecnologie avanzate come ITDR e MFA non solo rafforza la protezione degli asset digitali, ma prepara anche le imprese ad affrontare un panorama di minacce sempre più sofisticato.

Combinando una moderna gestione delle identità con i principi dello zero trust, le organizzazioni possono garantire che le proprie infrastrutture di identità siano resilienti, automatizzate e capaci di rilevare e rispondere a eventuali minacce emergenti.

L’approccio di [WatchGuard](https://www.watchguard.com/it) in questo ambito riflette una visione chiara e convincente per il futuro della cybersecurity. L’architettura della piattaforma di sicurezza unificata di WatchGuard crea un “te...