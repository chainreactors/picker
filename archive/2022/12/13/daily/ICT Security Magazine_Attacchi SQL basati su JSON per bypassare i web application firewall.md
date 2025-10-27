---
title: Attacchi SQL basati su JSON per bypassare i web application firewall
url: https://www.ictsecuritymagazine.com/notizie/attacchi-sql-basati-su-json-per-bypassare-i-web-application-firewall/
source: ICT Security Magazine
date: 2022-12-13
fetch_date: 2025-10-04T01:20:08.836250
---

# Attacchi SQL basati su JSON per bypassare i web application firewall

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/json-waf.jpg)

# Attacchi SQL basati su JSON per bypassare i web application firewall

A cura di:[Redazione](#molongui-disabled-link)  Ore 12 Dicembre 2022

* Team82 ha sviluppato un bypass generico per i Web Application Firewall (WAF) leader del settore.
* La tecnica di attacco prevede l’aggiunta della sintassi JSON ai payload SQL injection che un WAF non è in grado di analizzare.
* I principali fornitori di WAF non avevano il supporto JSON integrato sui propri prodotti, nonostante da un decennio fosse supportato dalla maggior parte dei motori di database.
* La maggior parte dei WAF rileverà facilmente gli attacchi SQLi, ma l’aggiunta della sintassi JSON a SQL ha nascosto ai WAF questi attacchi.
* Il bypass sviluppato da Team82 ha funzionato contro i WAF commercializzati da cinque fornitori leader: Palo Alto Networks, Amazon Web Services, Cloudflare, F5 e Imperva. Tutti e cinque hanno aggiornato i loro prodotti per supportare la sintassi JSON nel loro processo di ispezione SQL injection.
* Gli aggressori che utilizzano questa tecnica sarebbero in grado di aggirare la protezione del WAF e utilizzare ulteriori vulnerabilità per esfiltrare i dati.

I Web Application Firewall (WAF) sono stati progettati per salvaguardare le applicazioni e le API basate sul Web dal traffico HTTP dannoso proveniente dall’esterno, in particolare gli script cross-site e gli attacchi SQL injection, che rimangono una costante per i radar della sicurezza informatica. Anche se riconosciuta e relativamente semplice da risolvere, l’SQL injection è sempre presente nell’output delle scansioni automatiche del codice e viene regolarmente inserita negli elenchi delle principali vulnerabilità di settore, inclusa la OWASP Top 10. Così nei primi anni 2000, l’introduzione dei WAF è stata in gran parte dettata dalla volontà di contrastare questi errori di codifica.

I WAF sono ora una linea di difesa chiave per proteggere le informazioni organizzative archiviate in un database raggiungibile tramite un’applicazione web. Inoltre, vengono sempre più utilizzati per proteggere le piattaforme di gestione basate su cloud che supervisionano i dispositivi integrati connessi, come router e access point. In questo contesto, quindi, un utente malintenzionato in grado di aggirare le funzionalità di scansione e blocco del traffico dei WAF può avere una linea diretta con le informazioni aziendali sensibili e sui clienti. Per fortuna tali bypass sono ancora rari e una tantum mirati all’implementazione di un particolare fornitore.

Team82 ha sviluppato una tecnica di attacco che funge da primo bypass generico di più firewall per applicazioni Web venduti da fornitori leader del settore. Il bypass funziona su WAF di cinque fornitori leader: Palo Alto, F5, Amazon Web Services, Cloudflare e Imperva. Tutti i fornitori interessati dopo la divulgazione di Team82 hanno implementato correzioni che aggiungono il supporto per la sintassi JSON ai processi di ispezione SQL dei loro prodotti.

La tecnica utilizzata da Team82 si basa innanzitutto sulla comprensione del modo in cui i WAF identificano e contrassegnano la sintassi SQL come dannosa. In seguito, quindi, i ricercatori Claroty si sono focalizzati sull’individuazione della sintassi SQL che non viene riconosciuta dai WAF, rivelando così JSON. JSON è un formato standard per lo scambio di file e dati ed è comunemente utilizzato quando i dati vengono inviati da un server a un’applicazione web. Questo supporto è stato introdotto nei database SQL da quasi 10 anni e, oggi, i moderni motori di database supportano la sintassi JSON per impostazione predefinita, ricerche e modifiche di base, nonché una gamma di funzioni e operatori JSON. Mentre il supporto JSON è la norma tra i motori di database, lo stesso non si può dire per i WAF. I provider di questa tipologia di Firewall si sono rivelati lenti nell’aggiungere questo supporto ai propri prodotti, permettendo così di creare nuovi payload SQL injection, che includono JSON, in grado di aggirarne la sicurezza.

Gli aggressori che utilizzano questa nuova tecnica potrebbero accedere a un database back-end e utilizzare ulteriori vulnerabilità ed exploit per esfiltrare le informazioni tramite l’accesso diretto al server o tramite il cloud. Ciò è particolarmente importante per le piattaforme OT e IoT che sono passate a sistemi di gestione e monitoraggio basati su cloud e i WAF devono garantire una sicurezza aggiuntiva per il cloud. In caso contrario, i criminali in grado di aggirare queste protezioni avrebbero accesso indisturbato ai sistemi.

E’ disponibile il [report dell’intera analisi](https://www.ictsecuritymagazine.com/wp-content/uploads/Team82-Waf-EVASION-Report-Noam-Moshe.pdf) effettuata dai ricercatori di Team82 e presentata da **Noam Moshe, Vulnerability Researcher di Claroty, durante il Black Hat Europe 2022** tenutosi a Londra la scorsa settimana.

Condividi sui Social Network:

Tag articolo:  [#Attacchi SQL](https://www.ictsecuritymagazine.com/tag/attacchi-sql/ "Attacchi SQL")[#bypass WAF](https://www.ictsecuritymagazine.com/tag/bypass-waf/ "bypass WAF")[#Cyber Security](https://www.ictsecuritymagazine.com/tag/cyber-security/ "Cyber Security")[#Exploit](https://www.ictsecuritymagazine.com/tag/expl...