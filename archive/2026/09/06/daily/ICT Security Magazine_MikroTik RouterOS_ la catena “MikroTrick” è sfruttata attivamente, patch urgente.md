---
title: MikroTik RouterOS: la catena “MikroTrick” è sfruttata attivamente, patch urgente
url: https://www.ictsecuritymagazine.com/notizie/mikrotik-mikrotrick/
source: ICT Security Magazine
date: 2026-09-06
fetch_date: 2026-09-07T06:49:25.222945
---

# MikroTik RouterOS: la catena “MikroTrick” è sfruttata attivamente, patch urgente

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

![CERT Polska conferma attacchi a MikroTik RouterOS con SSH esposto: sei CVE, due critiche, account "ops" come IoC. Patch 7.24.2, 7.23.5 e 6.49.21, azioni.](https://www.ictsecuritymagazine.com/wp-content/uploads/MikroTik-RouterOS-la-catena-MikroTrick-e-sfruttata-attivamente-aggiornamento-immediato-raccomandato.png)

# MikroTik RouterOS: la catena “MikroTrick” è sfruttata attivamente, patch urgente

A cura di:[Redazione](#molongui-disabled-link)  Ore 6 Settembre 20266 Settembre 2026

Bastano un servizio SSH esposto su Internet e nessuna credenziale. Con questi soli requisiti, almeno dal 2 settembre, alcuni attaccanti prendono il controllo completo di dispositivi MikroTik RouterOS e lasciano come firma un account amministrativo chiamato
`ops`
. Lo ha confermato il 5 settembre 2026 [CERT Polska](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/), il team che ha scoperto le vulnerabilità e ha chiamato la catena “MikroTrick”. MikroTik ha pubblicato le versioni corrette su tutti i canali e raccomanda di aggiornare subito.

## Cosa è successo

Il team polacco ha individuato sei vulnerabilità in RouterOS, due delle quali critiche, e ne ha coordinato la divulgazione. Combinandone due, un attaccante ottiene privilegi amministrativi completi senza autenticarsi, purché il dispositivo esponga SSH su rete pubblica. Le falle riguardano il server e il client SSH, il servizio bandwidth-test, la gestione dei certificati X.509 e l’interfaccia WebFig.

Secondo i record [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67276), sono interessate tutte le release RouterOS 6.x precedenti alla 6.49.21, le 7.x precedenti alla 7.23.4 e la 7.24 precedente alla 7.24.2. I punteggi che seguono sono i CVSS 4.0 assegnati da CERT Polska, ente assegnatario delle CVE; NVD non ha ancora pubblicato una propria valutazione.

Le tre vulnerabilità principali sono:

* **[CVE-2026-67276](https://nvd.nist.gov/vuln/detail/CVE-2026-67276)** (CVSS 9.2): elusione dell’autenticazione SSH. RouterOS non confrontava per intero la chiave pubblica RSA associata a un utente. Chi conosceva il nome utente e il modulo pubblico della chiave poteva costruire una chiave diversa e autenticarsi senza la chiave privata, con i privilegi dell’account bersaglio.
* **[CVE-2026-86060](https://nvd.nist.gov/vuln/detail/CVE-2026-86060)** (CVSS 9.2): elevazione dei privilegi di sessione tramite un nome utente costruito ad arte. Il meccanismo di login SSH gestiva male i nomi utente che iniziano con un carattere non ammesso; l’attaccante poteva così modificare la maschera dei permessi e ottenere una sessione con pieni diritti amministrativi.
* **CVE-2026-67277** (CVSS 8.8): il servizio bandwidth-test permetteva a una connessione non autenticata di raggiungere uno stato riservato agli utenti autenticati. Insieme a due ulteriori difetti (esposizione di dati non inizializzati e integer underflow nella verifica delle dimensioni), consentiva di leggere memoria del kernel o di provocare un riavvio remoto del sistema.

L’elenco completo delle sei CVE è disponibile su una [pagina dedicata](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve) di CERT Polska. Il team spiega di aver anticipato la pubblicazione per una ragione precisa: i pacchetti corretti erano già pubblici e il confronto tra le versioni aveva permesso alla comunità di ricostruire alcune correzioni. Non ha diffuso codice di exploit né dettagli utili ad automatizzare gli attacchi.

## Gli attacchi osservati e gli indicatori di compromissione

CERT Polska dichiara di aver ricevuto conferma che la catena MikroTrick viene usata per assumere il controllo di dispositivi con SSH esposto e che le patch bloccano gli attacchi osservati. Gli attacchi riusciti, compresa la creazione dell’account
`ops`
, provengono dall’indirizzo IP 82.192.72.4 e risalgono almeno al 2 settembre. Un secondo indirizzo, 103.102.31.18, è stato usato in tentativi di sfruttamento della stessa catena.

Nei log di RouterOS l’attacco lascia due tracce riconoscibili: un accesso fallito per l’utente
`-2`
via SSH, seguito dalla creazione di un nuovo utente da parte di
`ssh:-2@<ip>`
. La presenza di uno qualsiasi di questi elementi va indagata subito. La loro assenza, avverte il team, non esclude un’attività non autorizzata.

## La risposta del vendor

Il [bollettino di sicurezza MikroTik](https://mikrotik.com/supportsec/september-2026-vulnerability/), datato 3 settembre 2026, definisce l’aggiornamento importante e afferma che la maggior parte delle configurazioni non è a rischio. Conferma che la correzione è inclusa in RouterOS 7.25beta3, 7.24.2, 7.23.4 e 6.49.21. Il 4 settembre è uscita anche la [7.23.5](https://mikrotik.com/download/routeros) per il ramo long-term: non aggiunge correzioni di sicurezza, ma risolve una regressione del DHCP IPv6 introdotta dalla 7.23.4, ed è quindi la versione a cui puntare. Il vendor non ha ancora pubblicato dettagli tecnici, per dare tempo agli amministratori di aggiornare. Per gli utenti domestici, scrive, il rischio non è immediato, ma consiglia comunque a tutti di aggiornare. CERT Polska riferisce inoltre che MikroTik, per la prima volta, ha inviato una notifica push agli utenti...