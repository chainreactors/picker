---
title: Zero-day febbraio 2026: la crisi della patch management che ha rotto il modello patch-and-pray
url: https://www.ictsecuritymagazine.com/notizie/zero-day-2026-patch-management/
source: ICT Security Magazine
date: 2026-02-18
fetch_date: 2026-02-19T04:22:00.570202
---

# Zero-day febbraio 2026: la crisi della patch management che ha rotto il modello patch-and-pray

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![Zero-day febbraio 2026 la crisi della patch management che ha rotto il modello patch-and-pray](https://www.ictsecuritymagazine.com/wp-content/uploads/Zero-day-febbraio-2026-la-crisi-della-patch-management-che-ha-rotto-il-modello-patch-and-pray.jpeg)

# Zero-day febbraio 2026: la crisi della patch management che ha rotto il modello patch-and-pray

A cura di:[Redazione](#molongui-disabled-link)  Ore 18 Febbraio 202617 Febbraio 2026

*Zero-day*, febbraio 2026, crisi della *patch management*: non è uno slogan allarmistico. È la sintesi di sette giorni – dall’11 al 17 febbraio 2026 – in cui l’ecosistema della sicurezza informatica ha ricevuto simultaneamente più colpi critici di quanti qualsiasi team operativo possa ragionevolmente assorbire. Non uno alla volta, con il tempo di respirare tra un’emergenza e l’altra. Tutti insieme, in una settimana che ha reso evidente ciò che molti sospettavano da tempo: il modello reattivo della [*patch management*](https://www.ictsecuritymagazine.com/articoli/strategia-di-patching-per-la-sicurezza-nazionale/) non è più sostenibile.

In sette giorni si sono concentrati: due CVE critiche in Ivanti EPMM con sistemi giudiziari europei compromessi; una vulnerabilità CVSS 9.9 in BeyondTrust sfruttata entro 24 ore dalla pubblicazione del *proof-of-concept*; il *Patch Tuesday* di Microsoft con 59 vulnerabilità e sei *zero-day* attivamente sfruttati; uno *zero-day* Apple descritto come parte di un attacco “estremamente sofisticato”; 30 estensioni Chrome malevole che hanno colpito oltre 260.000 utenti; una nuova variante ClickFix basata su DNS; e campagne attive di *supply chain poisoning* su npm e PyPI collegate a Lazarus Group.

Nessun SOC al mondo è dimensionato per gestire tutto questo contemporaneamente. Ed è esattamente questo il punto.

## Il catalogo dell’impossibile: cosa è successo tra l’11 e il 17 febbraio

Per comprendere la portata della crisi è necessario ricostruire la sequenza degli eventi con la precisione di una *timeline* forense. Non perché l’elenco sia fine a sé stesso, ma perché la densità temporale è il dato che trasforma una serie di incidenti individuali in un problema sistemico.

#### Ivanti EPMM: il *vendor* che non smette di essere vulnerabile

Il 29 gennaio 2026, Ivanti ha divulgato due vulnerabilità critiche nel suo Endpoint Manager Mobile – CVE-2026-1281 e CVE-2026-1340, entrambe con *score* CVSS 9.8 – che consentivano l’esecuzione di codice remoto senza autenticazione. Nelle settimane successive la situazione è degenerata rapidamente: il [governo olandese ha confermato al Parlamento](https://thehackernews.com/2026/02/dutch-authorities-confirm-ivanti-zero.html) che la *Dutch Data Protection Authority* e il Consiglio della Magistratura erano stati compromessi. La [Commissione Europea ha ammesso un attacco](https://www.bleepingcomputer.com/news/security/european-commission-discloses-breach-that-exposed-staff-data/) alla propria infrastruttura di gestione dei dispositivi mobili. La finlandese [Valtori ha rivelato l’esposizione di dati](https://www.helsinkitimes.fi/finland/finland-news/domestic/28492-state-data-breach-exposes-details-of-up-to-50-000-officials.html) relativi a fino a 50.000 dipendenti governativi.

L’[analisi di GreyNoise](https://thehackernews.com/2026/02/83-of-ivanti-epmm-exploits-linked-to.html) ha rivelato un dato particolarmente allarmante: l’83% dell’attività di sfruttamento proveniva da un singolo indirizzo IP ospitato su infrastruttura *bulletproof* di PROSPERO OOO (AS200593), registrato a San Pietroburgo. In nove giorni (1-9 febbraio) i sensori GreyNoise hanno registrato 417 sessioni di *exploitation*, con un picco di 269 in un singolo giorno – l’8 febbraio – pari a tredici volte la media giornaliera della settimana precedente.

Il dettaglio più inquietante non è lo sfruttamento in sé, ma la natura dell’attività post-compromissione. [Defused Cyber](https://www.helpnetsecurity.com/2026/02/11/ivanti-epmm-sleeper-webshell/) ha identificato una campagna che installava *web shell* “dormienti” – *class loader* Java in memoria al percorso
`/mifs/403.jsp`
– attivabili solo con un parametro specifico. Nessuna attività malevola osservata dopo l’impianto. Il *pattern* è quello dell’*initial access broker*: compromettere, catalogare, rivendere l’accesso. Il che significa che le conseguenze reali di questa campagna potrebbero manifestarsi settimane o mesi dopo.

Il problema Ivanti, tuttavia, non è la singola vulnerabilità. È il *pattern*. Ivanti EPMM (precedentemente MobileIron Core) è stato colpito da vulnerabilità critiche di esecuzione remota a luglio 2023 (CVE-2023-35078, sfruttata contro il governo norvegese), a maggio 2025 (CVE-2025-4427 e CVE-2025-4428, catena di *authentication bypass* + RCE sfruttata da attori *state-nexus* cinesi) e ora a gennaio 2026. A luglio 2025 la campagna “ToolShell” – attribuita ad APT27 e APT31 e diretta primariamente contro *server* SharePoint *on-premise* – ha visto gli stessi attaccanti sfruttare anche vulnerabilità note in Ivanti EPMM come vettore complementare, come documentato da Check Point Research.

Stesso prodotto, stesso tipo di falla (*code injection*, RCE non autenticata), stesso risultato: governi europei compromessi. Come ha osservato [*Dark Reading*]...