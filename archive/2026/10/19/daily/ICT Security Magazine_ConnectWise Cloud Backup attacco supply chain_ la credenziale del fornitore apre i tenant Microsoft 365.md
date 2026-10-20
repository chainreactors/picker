---
title: ConnectWise Cloud Backup attacco supply chain: la credenziale del fornitore apre i tenant Microsoft 365
url: https://www.ictsecuritymagazine.com/notizie/connectwise-cloud-backup-attacco-supply-chain/
source: ICT Security Magazine
date: 2026-10-19
fetch_date: 2026-10-20T06:53:43.903272
---

# ConnectWise Cloud Backup attacco supply chain: la credenziale del fornitore apre i tenant Microsoft 365

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![ConnectWise Cloud Backup attacco supply chain la credenziale del fornitore apre i tenant Microsoft 365Chiave Fornitore e Volte Cloud Aperte.png](https://www.ictsecuritymagazine.com/wp-content/uploads/ConnectWise-Cloud-Backup-attacco-supply-chain-la-credenziale-del-fornitore-apre-i-tenant-Microsoft-365Chiave-Fornitore-e-Volte-Cloud-Aperte.png)

# ConnectWise Cloud Backup attacco supply chain: la credenziale del fornitore apre i tenant Microsoft 365

A cura di:[Redazione](#molongui-disabled-link)  Ore 19 Ottobre 2026

*ConnectWise Cloud Backup attacco supply chain: il servizio resta sospeso, e la revoca della credenziale non basta a chiudere l’incidente nei tenant dei clienti.*

ConnectWise Cloud Backup, attacco supply chain: dal 15 ottobre 2026 una credenziale applicativa del fornitore ha permesso di ottenere token Microsoft Graph nei tenant di clienti e partner. Il servizio, ex SkyKick e usato da molti MSP per il backup di Microsoft 365, è sospeso. Al 19 ottobre le fonti consultate non indicano una data di ripristino. Questo articolo separa ciò che i fornitori hanno confermato, ciò che i ricercatori hanno osservato e ciò che resta aperto. Poi traduce l’incidente in azioni per gli amministratori e per gli MSP italiani.

## ConnectWise Cloud Backup attacco supply chain: la cronologia verificata

### Che cosa ha dichiarato ConnectWise

Le dichiarazioni sono tratte dagli avvisi del [Trust Center di ConnectWise](https://www.connectwise.com/company/trust/advisories), nel testo fornito dalla redazione fino all’aggiornamento del 19 ottobre alle 01:15, e dalla [pagina di stato](https://status.connectwise.com/), che riporta gli stessi aggiornamenti con orari che differiscono di pochi minuti. Gli orari che seguono sono quelli del Trust Center. Sono dichiarazioni di parte e vanno lette come tali.

* 15 ottobre: ConnectWise indica questa data come quella della scoperta e dell’avvio delle indagini interne ed esterne.
* 16 ottobre, 17:47: l’azienda parla di tentativi di accesso non autorizzato associati all’ambiente Cloud Backup. Pubblica come indicatori l’indirizzo 144.172.64.128 e gli user agent Python-urllib/3.12 e python-requests/2.31.
* 17 ottobre, 05:01: l’azienda dichiara di aver identificato accessi non autorizzati a identità applicative dell’ambiente Cloud Backup e spegne l’accesso dell’applicazione.
* 17 ottobre, 07:00: ConnectWise disabilita sette identità applicative. Revoca i certificati delle connessioni coinvolte e rende non più valide le credenziali condivise di Cloud Backup.
* 17 ottobre, 17:00: l’azienda dichiara di aver coinvolto una società esterna di risposta agli incidenti e di non aver osservato attività riuscite dell’attaccante negli ambienti che monitora.
* 18 ottobre, 01:00: ConnectWise mette offline anche SaaS Security e Cloud Management, per precauzione. Precisa che la disattivazione delle connessioni non annulla le modifiche già fatte in un tenant. I token già emessi possono restare utilizzabili fino alla scadenza. Credenziali e permessi creati tramite altre identità richiedono una revisione separata.
* 18 ottobre, 18:45: l’azienda aggiunge due indirizzi alla lista degli indicatori, 144.172.64.99 e 144.172.64.60, segnalati da monitoraggi di terze parti.
* 19 ottobre, 01:15: i tre servizi restano sospesi, senza un orario di ripristino confermato. Il prossimo aggiornamento è annunciato entro le 13:00.

Sugli archivi, ConnectWise dichiara che restano cifrati e isolati e che non ha evidenze di accesso. Aggiunge però di non avere visibilità sugli ambienti dei clienti. Per questo non può stabilire, con la sola indagine interna, se un singolo tenant Microsoft 365 sia stato toccato. Alla richiesta di iTnews ha ribadito che gli archivi esistenti non sono interessati e torneranno accessibili alla ripresa del servizio ([iTnews](https://www.itnews.com.au/news/stolen-connectwise-skykick-credential-exposed-microsoft-365-tenants-629721), aggiornamento del 19 ottobre). Sull’attribuzione, secondo [The Register](https://www.theregister.com/security/2026/10/19/connectwise-turns-off-its-saas-y-backup-security-and-management-services-to-probe-security-snafu/5303758), l’azienda dichiara di non poter parlare.

### Che cosa hanno osservato Huntress, Todyl e Microsoft

Queste sono osservazioni di società di sicurezza, ricavate dai log dei tenant che monitorano.

[Huntress](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access) ricostruisce quattro momenti:

* 13 e 14 ottobre: password spraying da 144.172.64.128 contro quattro tenant di studi legali. Due account sono stati bloccati; Huntress non ha visto accessi utente riusciti da quell’indirizzo.
* 15 ottobre, dalle 01:58: in circa 50 tenant monitorati, i service principal delle app ConnectWise Cloud Management (Exchange Online, Teams, Graph) si assegnano ruoli di directory, soprattutto Exchange Administrator. L’user agent è kiota-dotnet, quello delle app del fornitore. Huntress lo considera indice di automazione del fornitore, ma non l’ha confermato con ConnectWise.
* 15 ottobre, dalle 03:44: in un tenant, l’app ConnectWise Cloud Management per Microsoft Teams si assegna il ruolo di Global Administrator. Poi uno script Python aggiun...