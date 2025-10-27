---
title: Email Security: Cyber Kill Chain come modello di Difesa
url: https://www.ictsecuritymagazine.com/articoli/email-security-cyber-kill-chain-come-modello-di-difesa/
source: ICT Security Magazine
date: 2024-07-13
fetch_date: 2025-10-06T17:49:49.783436
---

# Email Security: Cyber Kill Chain come modello di Difesa

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

![Modello Cyber Kill Chain: 7 fasi di attacchi informatici - reconnaissance, weaponization, delivery, exploitation, installation, command and control, actions on objectives. Strategie di difesa cyber, prevenzione APT, mitigazione malware, e contromisure per sicurezza aziendale.](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Kill-Chain.jpg)

# Email Security: Cyber Kill Chain come modello di Difesa

A cura di:[Fabrizio Giorgione](#molongui-disabled-link)  Ore 12 Luglio 202426 Luglio 2024

Per comprendere come difendersi da potenziali attacchi malevoli è necessario studiare come questi avvengano. Per fare ciò, esistono diversi modelli, tra questi uno dei più noti ed utilizzati è quello della “**Cyber Kill Chain**” ideato da Lockheed Martin nel 2011.

![Cyber Kill Chain: modello di sicurezza informatica per analisi attacchi hacker. Fasi: OSINT, exploit, social engineering, malware, APT. Strategie di cyber defense: firewall, IDS/IPS, SIEM, SOC. Prevenzione minacce e protezione dati aziendali.](https://www.ictsecuritymagazine.com/wp-content/uploads/004.png)

Figura 2. Cyber Kill Chain

Indice degli argomenti

* [Cyber Kill Chain: Un Modello Essenziale per la Sicurezza Informatica e la Difesa Cibernetica](#cyber-kill-chain-un-modello-essenziale-per-la-sicurezza-informatica-e-la-difesa-cibernetica)
* [Mitigazione dei Rischi e Interruzione della Catena d'Attacco: Strategie di Difesa Cibernetica](#mitigazione-dei-rischi-e-interruzione-della-catena-dattacco-strategie-di-difesa-cibernetica)

## Cyber Kill Chain: Un Modello Essenziale per la Sicurezza Informatica e la Difesa Cibernetica

Questo modello descrive in sette fasi, si veda la figura 2, come un attaccante può compromettere un determinato target e di contro anche come identificare e prevenire potenziali attività malevole:

1. **Reconnaissance**: consiste nella raccolta di informazioni tramite tecniche di social engineering e/o OSINT per identificare e selezionare l’obiettivo. Questa fase può avvenire in due modalità:

* + **Passiva**: analisi e raccolta di informazioni tramite l’uso di siti web, annunci, Google, Shodan e simili.
  + **Attiva**: tramite l’uso di tool per effettuare scansioni dirette sul target (verifica delle porte aperte con i relativi servizi esposti e molto altro). Tra i tool più noti va sicuramente citato Nmap.

L’obiettivo di questa fase è trovare delle vulnerabilità che, potenzialmente, consentiranno agli attaccanti di entrare nella rete. Di contro la cyber defense dovrà occuparsi di mitigare e ridurre la superficie d’attacco utilizzabile dagli attaccanti.

2. **Weaponization**: trovata una vulnerabilità, gli attaccanti creano o cercano un exploit che consenta di sfruttarla. In questa fase vengono anche individuati possibili malware a supporto dell’attacco. Spesso per guadagnare l’accesso ad un sistema, vengono sfruttati anche gli zero day o vulnerabilità note ma non ancora “patchate” dagli amministratori del sistema.
3. **Delivery:** consiste nella trasmissione dell’exploit individuato all’obiettivo, di seguito alcuni esempi di come potrà essere consegnato:

* + Compromissione di un servizio esposto;
  + Invio di una mail malevola all’indirizzo della vittima;
  + Campagne di Social Engineering;
  + Chiavetta USB lasciata nei pressi dell’azienda, ad esempio nel parcheggio;
  + Compromissione di siti web terzi, abitualmente visitati dai dipendenti dell’azienda target (tramite l’uso, ad esempio, di attacchi di cross-site scripting (XSS)).

In questa fase, nella cyber defense, è fondamentale adottare un sistema di monitoraggio che consenta di individuare potenziali attività malevole e quindi strutturare un perimetro difensivo che comprenda almeno: firewall perimetrali, IDS/IPS, secure mail gateway, SIEM e un security operation center (SOC) per la gestione dei molteplici alert che verranno generati.

4. **Exploitation:** consiste nello sfruttamento di una o più vulnerabilità da parte dei malware introdotti nel sistema sotto attacco. Tendenzialmente si fa uso anche di tecniche di obfuscation per rendere queste azioni totalmente invisibili ai sistemi difensivi precedentemente elencati.
5. **Installation:** ottenuto l’accesso al sistema gli attaccanti cercheranno di mantenerlo tentando di installare ulteriori malware e backdoors che gli consentiranno successivamente di propagarsi nella rete e di accedere, tramite movimenti laterali, ad utenze con maggior privilegio.
6. **Command and Control (C2 o C&C)**: in questa fase si tenta di stabilire una comunicazione stabile e duratura con l’obiettivo di utilizzare la macchina infetta. In questa fase un APT consentirà ad esempio di:
   * Esfiltrare informazioni sensibili;
   * Infettare altre macchine;
   * Effettuare “**privilege escalation**” su macchine amministrative;

In queste ultime due fasi, il monitoraggio delle attività sospette lato cyber defense è fondamentale. È molto importante in questo caso, ad esempio, avere sistemi come **[UEBA](https://ieeexplore.ieee.org/document/8855782) (User and entity behavior analytics)** e regole di **GPO (Group Policy Objects)** che consentano di individuare comportamenti anomali e accessi non autorizzati.

7. **Actions on objectives:** in quest’ultima fase avverrà il vero e proprio attacco al sistema; Questo varierà in base al ...