---
title: Oltre il CVSS: come prioritizzare le vulnerabilità con EPSS, CISA KEV e contesto dell’asset
url: https://www.ictsecuritymagazine.com/notizie/prioritizzare-le-vulnerabilita/
source: ICT Security Magazine
date: 2026-11-03
fetch_date: 2026-11-04T08:19:09.616363
---

# Oltre il CVSS: come prioritizzare le vulnerabilità con EPSS, CISA KEV e contesto dell’asset

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.342 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

  Minacce e attacchi

  + [Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)

  Rischio, norme e privacy

  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)

  Tecnologie

  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)

  Scenari

  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)

  Ultimi in **Cyber Security**

  [Tutti gli articoli di Cyber Security →](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Approfondimenti](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* [Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Eventi ↗](https://eventi.ictsecuritymagazine.com/)

[Newsletter](/newsletter/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca

Attiva/disattiva menu

[Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)Contenuto sponsorizzato

# Oltre il CVSS: come prioritizzare le vulnerabilità con EPSS, CISA KEV e contesto dell’asset

Come prioritizzare le vulnerabilità combinando CVSS, EPSS, catalogo KEV e contesto dell’asset, per costruire una coda di intervento realistica e difendibile anche in ottica NIS2.

A cura di:[Francesco Pandiscia](https://www.ictsecuritymagazine.com/author/francesco-pandiscia/)  Ore Pubblicato il3 Novembre 20263 Novembre 2026  Condividi

![Poster blu cobalto con quattro barre in ordine di urgenza: la prima, gialla, è evidenziata da un cerchio bianco](https://www.ictsecuritymagazine.com/wp-content/uploads/prioritizzare-vulnerabilita-poster-blu-cobalto-barre.webp)

In sintesi

* Il CVSS misura la gravità tecnica, non il rischio: ordinare la correzione solo per punteggio produce code che nessun team riesce a smaltire.
* EPSS stima la probabilità di sfruttamento, il catalogo KEV documenta quella già avvenuta e il contesto dell’asset dice quanto conta il sistema colpito.
* Combinando i tre segnali si ottiene una coda in quattro livelli, ricalcolata a ogni ciclo e con le decisioni tracciate, utile anche per la NIS2.

Chi gestisce un programma di *vulnerability management* e deve prioritizzare le vulnerabilità conosce bene la scena: la scansione si chiude con migliaia di risultati, centinaia dei quali classificati come “critical” o “high”. Il volume non è un’impressione: nel 2026, al 2 novembre, le nuove CVE pubblicate sono in media circa 270 al giorno. A quel ritmo, l’idea di correggere tutto ciò che supera una certa soglia CVSS smette di essere una strategia e diventa una lista di arretrati.

Il tema è tornato al centro del dibattito con la [BOD 26-04 di CISA](/notizie/cisa-bod-26-04-vulnerability-management-risk-based/), emessa il 10 giugno 2026. Con questa direttiva l’agenzia statunitense ha chiesto alle amministrazioni federali di abbandonare il *patching* guidato dalla sola severità per un modello basato sul rischio reale, con scadenze pienamente applicabili dal 7 dicembre 2026. La direttiva vincola solo le agenzie federali, ma la domanda che pone riguarda qualsiasi organizzazione: su quali informazioni si decide che cosa correggere per primo?

La risposta proposta qui è operativa: tre segnali, ciascuno con una funzione precisa, e un modo per combinarli in una coda di intervento che il team IT possa davvero seguire.

## Prioritizzazione delle vulnerabilità: perché il CVSS da solo non basta

Il *Common Vulnerability Scoring System* misura la [gravità tecnica di una vulnerabilità](/articoli/valutazione-contestuale-della-criticita-di-una-vulnerabilita/): quanto è facile sfruttarla in teoria e quali danni può causare. È un’informazione utile, ma risponde a una domanda diversa da quella che interessa a chi deve pianificare la *remediation*. Il punteggio base non dice se esiste un exploit in circolazione, se qualcuno lo sta già usando, né se il sistema vulnerabile è un server esposto su Internet o una macchina di laboratorio isolata.

La versione 4.0 dello standard ha dato più rilievo alle metriche di minaccia e di ambiente proprio per colmare questa distanza. Nella pratica, però, la maggior parte delle console e dei report continua a mostrare il solo punteggio base. Il risultato è una distribuzione schiacciata verso l’alto, in cui troppe vulnerabilità sembrano urgenti e quindi nessuna lo è davvero.

Per prioritizzare le vulnerabilità e uscire da questa trappola servono tre domande distinte: quanto è probabile che la vulnerabilità venga sfruttata, se è già sfruttata e quanto conta l’asset su cui si trova.

## EPSS: stimare la probabilità di sfruttamento

L’*Exploit Prediction Scoring System*, gestito da [FIRST](https://www.first.org/epss/), stima la probabilità che una vulnerabilità pubblica venga sfruttata nei trenta giorni successivi. Non sostituisce il CVSS: lo affianca, aggiungendo la dimensione che il punteggio di gravità non considera. Il modello, giunto alla versione 5 nel giugno 2026, ricalcola ogni giorno i punteggi. Questi sono liberamente consultabili tramite API o file CSV, quindi possono arricchire gli export di qualsiasi scanner senza costi di licenza.

Per usarlo bene occorre distinguere i due valori che restituisce. Il punteggio è una probabilità; il percentile indica la posizione rispetto a tutte le altre CVE. Nei dati di inizio novembre 2026, un EPSS pari a 0,10 corrisponde a circa il percentile 96. Significa una probabilità stimata di sfruttamento del 10% e un punteggio pari o superiore a quello del 96% circa delle vulnerabilità valutate. Confondere percentile e probabilità porta a sovrastimare il rischio di molte vulnerabilità che, in assoluto, hanno probabilità molto basse.

EPSS ha anche limiti che è bene dichiarare. È un modello statistico addestrato su dati di sfruttamento raccolti da terzi, quindi dipende dalla qualità e dalla disponibilità di quei dati. Si basa inoltre sugli identificativi CVE: non dice nulla sugli zero-day, sulle vulnerabilità prive di CVE e sui difetti di configurazione. Va trattato come un segnale di probabilità, non come un verdetto.

## Cataloghi KEV: quando lo sfruttamento è già documentato

Il catalogo [Known Exploited Vulnerabilities](https://www.c...