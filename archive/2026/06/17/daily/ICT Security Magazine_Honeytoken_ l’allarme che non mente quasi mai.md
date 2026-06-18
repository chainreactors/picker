---
title: Honeytoken: l’allarme che non mente quasi mai
url: https://www.ictsecuritymagazine.com/cyber-security/honeytoken-cyber-deception/
source: ICT Security Magazine
date: 2026-06-17
fetch_date: 2026-06-18T06:51:54.874816
---

# Honeytoken: l’allarme che non mente quasi mai

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

![Honeytoken](https://www.ictsecuritymagazine.com/wp-content/uploads/Honeytoken.png)

# Honeytoken: l’allarme che non mente quasi mai

A cura di:[Redazione](#molongui-disabled-link)  Ore 17 Giugno 20269 Giugno 2026

Honeytoken è il nome di un’idea tanto semplice da sembrare un trucco: mettere in giro qualcosa di falso che nessuno, tranne un intruso, avrebbe motivo di toccare, e farsi avvisare quando qualcuno lo tocca. Una credenziale che non apre nulla, una chiave API che non serve a niente, un file dal nome invitante che nessun dipendente userebbe mai. Sono esche, e la loro forza sta in una proprietà che il resto della sicurezza si sogna: chi le attiva è quasi certamente un attaccante, perché un utente legittimo non ha alcuna ragione per avvicinarvisi.

È un capovolgimento rispetto al modo in cui di solito si cerca un intruso. Il rilevamento tradizionale prova a distinguere l’attività malevola da quella legittima dentro un flusso enorme di eventi reali, e paga questo sforzo con una marea di falsi positivi che esaurisce gli analisti. L’*honeytoken* fa l’opposto: non cerca l’ago nel pagliaio, pianta aghi che brillano solo se qualcuno li afferra. L’allarme che ne deriva non mente quasi mai, ed è esattamente ciò che manca nei centri operativi sommersi dal rumore.

## Capovolgere l’economia del rilevamento

Il problema cronico del rilevamento è il rapporto tra segnale e rumore. Un [Security Operations Center](https://www.ictsecuritymagazine.com/articoli/security-operations-center/) riceve ogni giorno migliaia di avvisi, la grande maggioranza dei quali innocui, e la fatica di separare i pochi veri dai molti falsi è la prima causa di affaticamento e di incidenti mancati. Ogni tecnica che aggiunge avvisi, per quanto sofisticata, peggiora questo rapporto se non porta con sé un modo per distinguere ciò che conta.

La *deception*, l’inganno difensivo, attacca il problema dal lato opposto. Invece di analizzare meglio ciò che accade, cambia il terreno: dissemina l’ambiente di oggetti che esistono solo per essere toccati da chi non dovrebbe. Un decoy non genera traffico, non viene usato da nessun processo legittimo, non compare in nessun flusso di lavoro reale. Per costruzione, qualunque interazione con esso è sospetta, e l’avviso che produce nasce già con una fedeltà altissima e un tasso di falsi positivi prossimo allo zero. Non è un controllo che si aggiunge al rumore, è un controllo che lo aggira.

## Cos’è un honeytoken, in concreto

Sotto il nome rientrano oggetti diversi, accomunati dall’essere falsi e sorvegliati. La forma più nota è la *canary token*, una semplice esca digitale, un documento, un collegamento, una voce di configurazione, che invia un segnale nel momento esatto in cui viene aperta o usata. Ci sono poi le credenziali esca: una chiave API legata a una policy di solo monitoraggio, che non concede alcun accesso reale ma registra e segnala ogni tentativo di utilizzo. Quando uno script automatico raccoglie le chiavi trovate in un ambiente e prova a usarle, quella falsa lo tradisce all’istante.

La collocazione è tutto. Un *honeytoken* funziona se si trova dove un attaccante guarderebbe ma un utente onesto no: tra le variabili di un sistema, in un archivio di credenziali, in una cartella dal nome allettante, in una voce di database. È il rovescio esatto del problema affrontato da chi cerca di non lasciare [credenziali sparse](https://www.ictsecuritymagazine.com/notizie/attacco-supply-chain-miasma/) in giro: qui il segreto si lascia in vista apposta, perché serva da trappola e non da chiave.

## Honeytoken e identità: cogliere ciò che l’EDR non vede

Il valore di questo approccio cresce proprio mentre gli attacchi cambiano natura. Secondo il CrowdStrike 2026 Global Threat Report, l’82 per cento dei rilevamenti nel 2025 è stato privo di *malware*, in netta crescita rispetto al 51 per cento del 2020: gli intrusi usano sempre più spesso credenziali legittime e strumenti di sistema, anziché codice malevolo riconoscibile. È il terreno dove la difesa basata sulle firme arranca, perché non c’è un file da identificare, solo un accesso che sembra autentico. Ed è il terreno ideale per le esche d’identità.

Un *honeytoken* d’identità è un account che sembra prezioso e non lo è: un’utenza di servizio dormiente, una credenziale da amministratore mai usata, una voce costruita per attirare chi, dopo essere entrato, cerca privilegi e percorsi. Tecniche di attacco all’identità come il furto di credenziali dal sistema operativo, il Kerberoasting o il Pass-the-Hash, catalogate nel [framework MITRE ATT&CK](https://attack.mitre.org/), si tradiscono nel momento in cui toccano l’esca. Una rete di account e *breadcrumb* falsi, disseminata sui sistemi e nelle directory aziendali, intercetta il [movimento laterale](https://www.ictsecuritymagazine.com/articoli/network-segmentation/) che gli strumenti di protezione degli endpoint spesso non vedono, perché quel movimento usa credenziali vere su canali leciti. L’intruso non sbaglia un comando: sbaglia bersaglio, e nel farlo si rivela.

## Dalla trappola al framework: MITRE Engage

Disseminare esche a caso non è una strategia. Perché la *deception* diventi disciplina serve u...