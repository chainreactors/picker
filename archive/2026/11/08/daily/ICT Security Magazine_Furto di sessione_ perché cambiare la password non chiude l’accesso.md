---
title: Furto di sessione: perché cambiare la password non chiude l’accesso
url: https://www.ictsecuritymagazine.com/articoli/furto-di-sessione/
source: ICT Security Magazine
date: 2026-11-08
fetch_date: 2026-11-09T08:53:23.479976
---

# Furto di sessione: perché cambiare la password non chiude l’accesso

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.351 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

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

[Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

# Furto di sessione: perché cambiare la password non chiude l’accesso

Il furto di sessione consegna all’attaccante un accesso già autenticato. Come avviene, perché cambiare la password non basta e quali controlli legano cookie e token al dispositivo.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il8 Novembre 20264 Novembre 2026  Condividi

![Furto di sessione: perché cambiare la password non chiude l'accesso: Due biglietti identici in pixel art: uno attraversa un arco di pietra luminoso, l'altro è trattenuto da un cavo al portatile](https://www.ictsecuritymagazine.com/wp-content/uploads/furto-di-sessione-cookie-token.webp)

In sintesi

* Il furto di sessione copia cookie o token già emessi e permette di entrare senza password e senza secondo fattore.
* Per chiudere l'accesso non basta la password: Microsoft indica di revocare le sessioni, e i token di accesso già emessi durano in genere un'ora.
* DPoP, TLS reciproco e DBSC legano token o cookie a una chiave non esportabile, ma non fermano il malware attivo sul dispositivo.

Il furto di sessione permette di entrare in un account senza password e senza secondo fattore. L’attaccante non indovina le credenziali. Copia la prova che l’accesso è già avvenuto e la presenta al servizio al posto dell’utente.

Dopo l’autenticazione il servizio consegna al browser un cookie di sessione, oppure all’applicazione un token di accesso. Chi presenta quell’oggetto viene trattato come l’utente autenticato, finché il servizio non lo dichiara scaduto. L’articolo tratta solo questo oggetto. La [catena completa dell’account takeover](/notizie/account-takeover/) e il [rilevamento con l’ITDR](/digital-id-security/itdr-identity-threat-detection-response/) sono già trattati dalla testata.

## Che cosa si ruba con il furto di sessione

Il [NIST](https://pages.nist.gov/800-63-4/sp800-63b/session/) spiega nella linea guida [SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final), pubblicata il 31 luglio 2025, che la continuità di una sessione autenticata si basa sul possesso di un segreto. Il servizio lo emette al momento dell’autenticazione. Tra gli esempi il NIST cita il cookie di una sessione nel browser.

[Google](https://blog.google/security/protecting-cookies-with-device-bound-session-credentials/) scrive nel post del 9 aprile 2026 che i cookie hanno spesso una vita lunga. Chi li sottrae può quindi accedere agli account senza conoscere la password. Secondo Google, gli attori malevoli spesso raggruppano, scambiano o vendono questi accessi.

### Il cookie di sessione

[MITRE ATT&CK](https://attack.mitre.org/techniques/T1539/) classifica il furto del cookie come tecnica T1539 (versione 1.5, modificata il 12 maggio 2026). Secondo MITRE, i cookie si trovano su disco, nella memoria dei processi del browser e nel traffico di rete. MITRE scrive che possono aggirare alcuni protocolli di autenticazione a più fattori.

Il riuso del cookie rubato è la tecnica [T1550.004](https://attack.mitre.org/techniques/T1550/004/), che in gergo si chiama pass-the-cookie. Il nome compare nel titolo di uno scritto del ricercatore Johann Rehberger (dicembre 2018), che MITRE cita nella scheda T1539. MITRE riporta due casi. Nella campagna SolarWinds, il gruppo APT29 ha usato cookie rubati per accedere a risorse cloud e un cookie duo-sid falsificato per aggirare l’autenticazione a più fattori su un account di posta. Il gruppo Star Blizzard ha aggirato lo stesso controllo sugli account di posta delle vittime con cookie rubati tramite EvilGinx.

### Token di accesso e refresh token

Nei servizi che usano OAuth 2.0 il cookie lascia il posto ai token. Il token di accesso autorizza le richieste verso un’API. Il refresh token serve a ottenerne di nuovi senza ripetere l’accesso. [Microsoft](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access) indica che Entra ID emette token di accesso che durano un’ora per impostazione predefinita.

L’[RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html), la guida di sicurezza su OAuth 2.0 pubblicata dall’IETF a gennaio 2025, raccomanda di vincolare i token di accesso a chi li ha ricevuti. Per i client pubblici prescrive di vincolare i refresh token oppure di ruotarli a ogni uso.

### Perché il secondo fattore non interviene

Il secondo fattore verifica l’utente al momento dell’accesso, mentre il cookie rubato nasce dopo. [Microsoft](https://www.microsoft.com/en-us/security/blog/2022/07/12/from-cookie-theft-to-bec-attackers-use-aitm-phishing-sites-as-entry-point-to-further-financial-fraud/) lo documenta nell’analisi del 12 luglio 2022 su una campagna di phishing con intermediario (in inglese *adversary-in-the-middle*, AiTM). Secondo Microsoft, l’attaccante si autentica a nome dell’utente a prescindere dal metodo di accesso. In più casi i cookie contenevano già la dichiarazione dell’autenticazione a più fattori avvenuta.

## Come avviene il furto di sessione

Le fonti consultate descrivono tre strade: il malware sul dispositivo, il proxy di phishing e le fughe dai sistemi di supporto.

### Infostealer sul dispositivo

L’[ACN](https://www.acn.gov.it/portale/documents/20119/551838/ACN_Infosteale...