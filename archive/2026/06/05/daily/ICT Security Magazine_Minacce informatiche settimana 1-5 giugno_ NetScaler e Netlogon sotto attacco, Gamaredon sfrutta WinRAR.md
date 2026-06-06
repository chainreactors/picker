---
title: Minacce informatiche settimana 1-5 giugno: NetScaler e Netlogon sotto attacco, Gamaredon sfrutta WinRAR
url: https://www.ictsecuritymagazine.com/notizie/minacce-informatiche-settimana/
source: ICT Security Magazine
date: 2026-06-05
fetch_date: 2026-06-06T05:51:27.915734
---

# Minacce informatiche settimana 1-5 giugno: NetScaler e Netlogon sotto attacco, Gamaredon sfrutta WinRAR

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
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Sala operativa di sicurezza informatica con schermi che mostrano grafici di rete e un avviso critico: Minacce informatiche della settimana 1-5 giugno 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/2026-06-05_1030_minacce-informatiche-settimana.jpg)

# Minacce informatiche settimana 1-5 giugno: NetScaler e Netlogon sotto attacco, Gamaredon sfrutta WinRAR

A cura di:[Redazione](#molongui-disabled-link)  Ore 5 Giugno 20265 Giugno 2026

Minacce informatiche settimana 1-5 giugno: il roundup di *threat intelligence* è dominato da due vulnerabilità critiche in sfruttamento attivo, entrambe su componenti che presidiano il cuore delle infrastrutture aziendali: gli appliance Citrix NetScaler esposti su internet (CVSS 9.3 nella metrica 4.0 di Citrix, 9.8 nella 3.1 di NVD) e i *domain controller* Windows (CVSS 9.8). Sullo sfondo, il catalogo KEV di CISA continua ad allungarsi e il gruppo russo Gamaredon affina il proprio arsenale contro l’Ucraina sfruttando una vulnerabilità di WinRAR. Di seguito i fatti verificati e le priorità di mitigazione per i team di sicurezza.

## Citrix NetScaler: sfruttamento su larga scala della CVE-2026-3055

La vulnerabilità più pesante della settimana è CVE-2026-3055, un *out-of-bounds read* che interessa NetScaler ADC e NetScaler Gateway quando configurati come SAML Identity Provider. Il difetto, corretto da Citrix il 23 marzo con il [bollettino CTX696300](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696300) insieme alla correlata CVE-2026-4368, consente a un attaccante remoto di inviare richieste SAML malformate che inducono l’appliance a includere contenuti di memoria non inizializzata nel cookie NSC\_TASS. L’impatto è di *information disclosure* sul modello del vecchio CitrixBleed (CVE-2023-4966): dalla memoria possono uscire token di sessione e credenziali, con conseguente dirottamento delle sessioni e accesso abusivo, senza necessità di eseguire codice sull’appliance.

Il punto critico è la tempistica: le prime tracce di sfruttamento risalgono almeno al 27 marzo, quattro giorni dopo la patch, secondo le osservazioni di CrowdSec; l’[allerta di Fortinet](https://community.fortinet.com/fortirecon-48/outbreak-alert-citrix-netscaler-memory-overread-vulnerability-227772), che ha pubblicato gli indicatori di compromissione della campagna in corso, conferma uno sfruttamento ormai su larga scala contro gli appliance esposti. Chi applica la patch oggi deve quindi assumere la possibile compromissione pregressa: oltre all’aggiornamento, vanno riviste le attività SAML anomale nei log, le sessioni avviate dall’IdP senza corrispondenza con utenti legittimi, le modifiche inattese a configurazioni e certificati di firma e gli account locali creati di recente.

## Netlogon: RCE pre-autenticazione sui domain controller

La seconda emergenza riguarda CVE-2026-41089, *stack buffer overflow* nel servizio Netlogon corretto da Microsoft nel Patch Tuesday del 12 maggio e inizialmente classificato nella fascia di sfruttamento meno probabile. La valutazione è invecchiata in fretta: come riportato da [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/), a fine maggio il Centre for Cybersecurity Belgium ha confermato lo sfruttamento attivo in attacchi reali. La falla consente a un attaccante non autenticato che raggiunga l’interfaccia RPC di Netlogon su un *domain controller* di eseguire codice con privilegi SYSTEM; risultano interessate le versioni di Windows Server dalla 2012 R2 alla 2025, mentre le release fuori supporto restano coperte solo da micropatch di terze parti o dai programmi di supporto esteso.

Per un bug pre-autenticazione sul controller di dominio la finestra di tolleranza è zero: la priorità è completare il patching di tutti i DC della foresta nella stessa finestra di manutenzione, perché un ambiente parzialmente aggiornato non è uno stato difendibile. In parallelo conviene restringere il traffico Netlogon a livello di rete tenendo conto dell’intera superficie RPC: il servizio è raggiungibile via SMB sulla porta TCP 445 ma anche tramite l’Endpoint Mapper sulla 135 e le porte dinamiche alte, quindi chiudere la sola 445 non basta. I controller, in ogni caso, non dovrebbero mai essere raggiungibili da segmenti non fidati. Sul fronte della prioritizzazione, il criterio è lo stesso richiesto dalla misura ACN sulla [gestione delle vulnerabilità](https://www.ictsecuritymagazine.com/articoli/id-ra-08-acn-vulnerabilita/): prima ciò che è esposto e sfruttato, poi il resto.

## Il catalogo KEV si allunga: cgroups, Android e Magento

Sul fronte delle vulnerabilità sfruttate certificate da CISA, l’agenzia statunitense ha aggiunto al catalogo Known Exploited Vulnerabilities, [con l’alert del 2 giugno](https://www.cisa.gov/news-events/alerts/2026/06/02/cisa-adds-two-known-exploited-vulnerabilities-catalog), due voci: CVE-2022-0492, vecchia falla di *privilege escalation* nei cgroups v1 del kernel Linux (meccanismo release\_agent) tornata d’attualità negli attacchi ai container come tecnica di evasione, e CVE-2025-48595, un *integer overflow* nel framework Android. Il 3 giugno si è aggiunta CVE-2026-45247, deserializzazione di dati non fi...