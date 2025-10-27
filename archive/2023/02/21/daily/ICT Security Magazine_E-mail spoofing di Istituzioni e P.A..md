---
title: E-mail spoofing di Istituzioni e P.A.
url: https://www.ictsecuritymagazine.com/articoli/e-mail-spoofing-di-istituzioni-e-p-a/
source: ICT Security Magazine
date: 2023-02-21
fetch_date: 2025-10-04T07:38:55.726449
---

# E-mail spoofing di Istituzioni e P.A.

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/email-spoofing.jpg)

# E-mail spoofing di Istituzioni e P.A.

A cura di:[Mirko Caruso](#molongui-disabled-link)  Ore 20 Febbraio 2023

### INTRODUZIONE AL FENOMENO

Sono passati quasi 30 anni dall’origine del termine phishing e dai primi attacchi documentati, tuttavia, la stretta correlazione tra la buona riuscita degli stessi attacchi ed il fattore umano, sommata a campagne sempre più mirate e “autorevoli” e ad una – non proprio estesa – conoscenza e adozione globale dei meccanismi di prevenzione; fanno si che la prima posizione (per numero di vittime) dell’Internet Crime Report 2020 dell’FBI venga occupata da eventi criminosi di tipologia Phishing, al sesto posto quelli di tipo spoofing seguiti da misrepresentation, business e-mail compromise e, fuori dalla “top ten” di sole sei posizioni, la tipologia Government Impersonation.

Il fenomeno dell’e-mail spoofing e, più nello specifico, sender spoofing (impersonificazione di un indirizzo mittente di un dato nome di dominio) e domain spoofing (impersonificazione di un intero nome di dominio) sono spesso e da sempre, alla base delle campagne phishing e spear phishing in quanto consentono di condizionare negativamente il comportamento, le azioni e la scelte del destinatario, trasmettendo un falso senso di autorevolezza e attendibilità, sfruttando quindi proprio il “fattore umano” per la buona riuscita della campagna stessa.

Anche ENISA, sulla falsariga dell’FBI, già con le pubblicazioni Threat Landscape 2020 e 2021, pone l’accento verso gli “E-Mail Related Threats” dove le campagne BEC (Business e-mail compromise) e Phishing la fanno da padrona, tanto da arrivare a suggerire azioni tecniche volte all’implementazione di specifici standard / protocolli: DMARC, SPF e DKIM. Al centro di questa analisi e proposta di strategia sono proprio gli standard DMARC e, parzialmente, Sender Policy Framework e la loro comprovata utilità nel contrasto, se adottati in un più strutturato processo di intelligence, e nella prevenzione (intesa come blocco) di attacchi a tipologia Spoofing, Misrepresentation e Government Impersonation.

### ANALISI DEL CONTESTO NAZIONALE: DAL 2009 AD OGGI

La Direttiva n.8/2009 a firma dell’allora Ministro per la Pubblica amministrazione Renato Brunetta delineava le disposizioni in materia di riconoscibilità, aggiornamento, usabilità, accessibilità e registrazione al dominio “.gov.it” dei siti web delle P.A. assegnando al nome di dominio “.gov.it” l’obiettivo di « aggregare i siti web delle pubbliche amministrazioni che già erogano servizi istituzionali con un adeguato ed omogeneo livello di qualità, sicurezza ed aggiornamento dei servizi » delegando all’ormai cessato CNIPA ora AgID, Agenzia per l’Italia digitale, la fornitura dell’assistenza tecnica necessaria per l’iscrizione al dominio .gov.it e la sua gestione operativa: AgID che risponde egregiamente al compito assegnatole implementando, ormai da anni, un portale per la registrazione e gestione dei nomi di dominio di terzo livello di .gov.it, portale che integra (già in fase di accreditamento della P.A. richiedente) la gestione dei record DNS – inclusi quelli di tipo TXT come DMARC e Sender Policy Framework oggetto della presente analisi – o la delega del dominio verso name server (e relativi pannelli di gestione DNS) terzi, esterni alla stessa AgID.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/email-spoofing-01-700x480.jpg)

Nel panorama Istituzionale odierno, con il Piano Triennale per l’informatica nella Pubblica Amministrazione 2019-2021 e con la precedente determina AgID 36/2018 si è assistito al cosiddetto “riordino” del dominio di secondo livello gov.it, avviato, de facto, con lo scopo di aggiornare e riorganizzare i criteri di assegnazione e allocazione dei sottodomini secondo le politiche vigenti nell’Unione Europea; tale determina prevede nello specifico l’assegnazione del dominio di terzo livello di .gov.it « alle sole amministrazioni centrali dello Stato indicate all’elenco delle amministrazioni pubbliche individuate ai sensi dell’articolo 1, comma 3, della legge 31 dicembre 2009, n. 196 e successive modificazioni e pubblicate annualmente in G.U. » e prevede inoltre:

* che le amministrazioni territoriali e scolastiche che attualmente lo utilizzano debbano abbandonarlo nei termini stabiliti dalla determina;
* che tutte le infrastrutture ICT utilizzate per l’implementazione di tali siti siano conformi alle Misure minime di sicurezza ICT emanate da AgID e le applicazioni siano immuni almeno per i Top 10 Risk di OWASP correnti (allora OWASP Top 10 : 2017).

In estrema sintesi è stata disposta, in tutta fretta, la sola migrazione dei domini di terzo livello appartenenti a istituzioni scolastiche dal dominio “.gov.it” verso il nuovo “.edu.it” (quest’ultimo assegnato al MIUR) mentre per gli enti territoriali interessati dalla determina AgID è stata disposta la migrazione verso il dominio “.it” indicante, dal 1987, l’estensione geografica ufficiale dell’Italia.

A fronte di una tale migrazione su larga scala, si è sprecata la possibilità di adottare una politica di conformità per adeguare le “identità web” delle P.A. rendendole conformi a standard antiphishing e antispoofing globalmente riconosciut...