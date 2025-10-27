---
title: Email Forensics: Studio di email malevola e principali tool di analisi
url: https://www.ictsecuritymagazine.com/articoli/email-forensics-sicurezzamail/
source: ICT Security Magazine
date: 2024-09-28
fetch_date: 2025-10-06T18:28:59.110783
---

# Email Forensics: Studio di email malevola e principali tool di analisi

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/tools-studio-email-malevola.jpg)

# Email Forensics: Studio di email malevola e principali tool di analisi

A cura di:[Fabrizio Giorgione](#molongui-disabled-link)  Ore 27 Settembre 202427 Settembre 2024

Nell’era digitale, la sicurezza email è diventata una priorità imprescindibile per organizzazioni e individui. Questo articolo offre una guida all’*Email Forensics* utile ad analizzare e difendere le comunicazioni via email da minacce informatiche illustrando metodologie e strumenti all’avanguardia per individuare messaggi sospetti o dannosi.

Il testo si propone come risorsa fondamentale per chi desidera potenziare le proprie difese, fornendo best practice, indicatori chiave da monitorare e una panoramica degli strumenti più efficaci per l’analisi forense: dall’esame degli header alla verifica degli allegati, vengono trattati tutti gli aspetti critici per implementare una strategia di protezione completa.

In un contesto in cui le minacce veicolate via email diventano sempre più sofisticate, questa guida offre competenze essenziali per proteggere dati sensibili e infrastrutture IT. Per un’analisi più approfondita sull’intersezione tra sicurezza email e tecnologie emergenti, vi invitiamo a consultare il precedente articolo “[Email Security e Intelligenza Artificiale](https://www.ictsecuritymagazine.com/articoli/email-security-e-intelligenza-artificiale/)“, che esplora le ultime innovazioni nel settore.

## *Email Forensics*, come realizzare un’analisi approfondita

Quando si analizza un’email ci sono diversi fattori da tenere in considerazione:

* Verifica **dell’header from**, se quindi il sender è noto oppure sconosciuto facendo caso anche ad eventuali “errori” nel dominio e/o nel nome dell’indirizzo. Questo potrebbe essere un primo chiaro segnale di una mail potenzialmente malevola.
* Se il **contenuto della mail** cerca di far leva sulle nostre emozioni per ottenere delle informazioni
* **Analisi degli URL**: un primo sintomo di una mail malevola riguarda l’uso del protocollo “http” invece dell’uso di un protocollo più sicuro e protetto come “https”.
* **Analisi degli allegati**, utili per infettare una macchina e/o eseguire un malware, ad esempio, aprendo un file word/excel se come prima azione viene richiesto di “attivare le macro”. L’attivazione di macro di un file office è uno dei modelli d’attacco più utilizzati da molteplici malware, tra cui **Emotet** e da altri ransomware, per infettare le macchine destinatarie. Quest’operazione quindi in moltissimi casi è sintomo che l’allegato possa essere malevolo. Si invita quindi a non aprire e/o eseguire allegati provenienti da mittenti sconosciuti e in cui si chieda di “abilitare” le macro. Altri file da cui si consiglia di porre maggior attenzione sono gli eseguibili “.**exe**” e i file con estensione “.**bat**”.

Un’analisi più approfondita può essere effettuata tramite analizzando l’header. Quest’analisi consentirà di individuare molteplici **IoC** (**Indicator of compromise**) che aiuteranno a comprendere se effettivamente la mail risulta essere malevola. Tra le informazioni più rilevanti estraibili dall’header di un email ci sono:

* “Connections” come sender IP da cui è partita la mail e relativi hostname/relay attraversati;
* Envelope information (Sender e Recipient);
* Header From, to, subject e data;
* Return-Path;
* SPF, DKIM e DMARC e relative configurazioni;
* Message-ID, univoco per ogni mail;
* MIME- Version;
* X-Spam Status;

Per estrarre l’header di una mail è sufficiente seguire i seguenti passi:

* Aprire la mail tramite Outlook, Thunderbird o altro software simile
* File -> Info -> Properties -> Internet headers

![Figura 11. Header Information - Email Forensics](https://www.ictsecuritymagazine.com/wp-content/uploads/013.png)

![Figura 11. Header Information - Email Forensics: header analysis](https://www.ictsecuritymagazine.com/wp-content/uploads/014.png)

Figura 11. Header Information

**Nota**. Per effettuare una corretta analisi dell’header è fondamentale che la mail **NON** sia stata “forwadata” ma che la segnalazione ricevuta sia invece allegata nella mail. Ciò consentirà di non perdere tutte le informazioni relative alle connessioni e comunicazioni avvenute tra il sender sospetto e il recipient.

![Figura 12. Segnalazione di un’email sospetta - Email Forensics](https://www.ictsecuritymagazine.com/wp-content/uploads/015.png)

Figura 12. Segnalazione di un’email sospetta

Una volta selezionato il contenuto “**dell’internet headers**” sarà possibile procedere all’analisi di tutti i vari campi di interesse sin qui elencati. Tra i tool a supporto per analizzare un header si segnalano:

* **MxToolbox**: https://mxtoolbox.com/EmailHeaders.aspx
* **Google Admin Toolbox**: https://toolbox.googleapps.com/apps/messageheader/
* **Analyze mail header**: https://mailheader.org

MxToolbox fornisce una vasta gamma di informazioni relative a:

* **Blacklist** di un IP e/o dominio
* “**Delivery information**”: SPF, DKIM e DMARC
* “**Relay information**” con tutte le informazioni di interesse relative al flusso della mail (dal sender al recipient finale). Tramite quest’area sarà infatti possibile osservare se la mail ha attraversato qualche relay e/o hostname malevolo.

!...