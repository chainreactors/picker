---
title: Zero-day nelle VPN Check Point: CISA impone la patch in tre giorni mentre Qilin sfrutta la falla
url: https://www.ictsecuritymagazine.com/notizie/zero-day-check-point-vpn-qilin/
source: ICT Security Magazine
date: 2026-06-10
fetch_date: 2026-06-11T06:36:47.443038
---

# Zero-day nelle VPN Check Point: CISA impone la patch in tre giorni mentre Qilin sfrutta la falla

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

![Zero-day nelle VPN Check Point](https://www.ictsecuritymagazine.com/wp-content/uploads/Zero-day-nelle-VPN-Check-Point.png)

# Zero-day nelle VPN Check Point: CISA impone la patch in tre giorni mentre Qilin sfrutta la falla

A cura di:[Redazione](#molongui-disabled-link)  Ore 10 Giugno 202610 Giugno 2026

Una vulnerabilità critica di *authentication bypass* nei prodotti di accesso remoto Check Point, già usata in attacchi reali, ha spinto la *Cybersecurity and Infrastructure Security Agency* statunitense a emettere un ordine vincolante con scadenza ravvicinata. Il caso, tracciato come CVE-2026-50751, unisce tre elementi che la redazione segue da vicino: un perimetro VPN esposto, un attore ransomware di primo piano e una risposta regolatoria d’emergenza.

## Cosa è successo

Lunedì 8 giugno 2026 Check Point ha pubblicato l’advisory per CVE-2026-50751, una falla di tipo *improper authentication* (CWE-287) con punteggio CVSS pari a 9,3. Il difetto consente a un attaccante non autenticato di stabilire una sessione VPN senza credenziali valide, aggirando i controlli. Sono interessati i gateway *Remote Access VPN*, *Mobile Access* e *Spark Firewall* configurati con il protocollo di scambio chiavi IKEv1 deprecato, quando accettano client legacy e non richiedono un certificato macchina per la connessione.

Secondo il vendor lo sfruttamento è attivo: le prime tracce risalgono al 7 maggio 2026, con un’impennata nel primo fine settimana di giugno. La campagna resta, al momento, circoscritta ad alcune decine di organizzazioni nel mondo. Gli indicatori raccolti, hash condivisi tra i casi, uso del software open source *Rclone* per l’esfiltrazione, comunicazioni via protocollo *Tox* e infrastruttura VPS dedicata, hanno permesso a Check Point di collegare almeno un incidente a un affiliato del ransomware Qilin, attribuzione espressa con confidenza media; più ferma è invece la constatazione dell’attività ransomware seguita alla compromissione. Qilin resta uno degli ecosistemi *ransomware as a service* più attivi del 2026.

Durante l’indagine è emersa una seconda vulnerabilità correlata, CVE-2026-50752 (CVSS 7,4), nello stesso percorso di codice IKEv1: potrebbe abilitare un attacco *man in the middle* contro i tunnel site-to-site in configurazioni specifiche. Per quest’ultima non risultano sfruttamenti.

## L’intervento di CISA

L’8 giugno 2026 CISA ha aggiunto CVE-2026-50751 al catalogo *Known Exploited Vulnerabilities* e ha imposto alle agenzie federali civili di applicare la patch o isolare i sistemi entro l’11 giugno 2026, una finestra di appena tre giorni. La *binding operational directive* vincola formalmente solo il governo statunitense, ma l’agenzia ha esteso la raccomandazione a tutti i team di sicurezza, settore privato incluso.

## Perché conta

Il caso è significativo oltre il singolo incidente. Un *authentication bypass* su un concentratore VPN annulla la prima linea di difesa perimetrale e apre la strada a movimenti laterali e a una [catena ransomware](https://www.ictsecuritymagazine.com/?s=ransomware) completa; non a caso il più recente *Data Breach Investigations Report* colloca per la prima volta lo sfruttamento delle vulnerabilità come primo vettore di accesso iniziale, al 31 per cento dei casi, in crescita di oltre la metà su base annua e trainato proprio dagli *zero-day* contro VPN ed *edge device*. La configurazione IKEv1 vulnerabile, inoltre, è frequente in installazioni datate e poco presidiate, proprio quelle più difficili da mappare in tempo utile. Per i responsabili sicurezza la priorità immediata è duplice: verificare se i gateway accettano IKEv1 con client legacy senza certificato macchina, e applicare gli aggiornamenti senza attendere la scadenza federale. La combinazione tra finestra di sfruttamento aperta da inizio maggio e coinvolgimento di un affiliato Qilin rende il rischio concreto anche per chi non rientra nel perimetro della direttiva.

## Il contesto italiano

[Qilin non è un nome astratto per l’Italia](https://www.acn.gov.it/portale/w/qilin-campagne-di-sfruttamento-sistematico-e-diffusione-del-ransomware-sul-territorio-nazionale). Lo scorso marzo 2026 un attacco ransomware attribuito allo stesso ecosistema ha colpito Netalia, *cloud provider* genovese che gestisce i pagamenti digitali per il Comune di Genova, bloccando il sistema di riscossione delle sanzioni della polizia locale e costringendo l’amministrazione a prorogare le scadenze con riduzione del 30 per cento. Il precedente mostra come un singolo fornitore compromesso possa propagare il disservizio a un intero servizio pubblico; un [gateway VPN](https://www.ictsecuritymagazine.com/?s=vpn) bucato come quello descritto da CVE-2026-50751 offre allo stesso attore una via d’ingresso ancora più diretta verso reti aziendali e della Pubblica Amministrazione.

Condividi sui Social Network:

Tag articolo:  [#authentication bypass](https://www.ictsecuritymagazine.com/tag/authentication-bypass/ "authentication bypass")[#Check Point](https://www.ictsecuritymagazine.com/tag/check-point/ "Check Point")[#CISA](https://www.ictsecuritymagazine.com/tag/cisa/ "CISA")[#CVE-2026-50751](https://www.ictsecuritymagazine.com/tag/cve-2026-50751...