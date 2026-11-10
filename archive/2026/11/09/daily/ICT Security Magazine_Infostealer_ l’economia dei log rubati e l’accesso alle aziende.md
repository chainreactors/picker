---
title: Infostealer: l’economia dei log rubati e l’accesso alle aziende
url: https://www.ictsecuritymagazine.com/articoli/infostealer-mercato-log-rubati/
source: ICT Security Magazine
date: 2026-11-09
fetch_date: 2026-11-10T09:03:20.995367
---

# Infostealer: l’economia dei log rubati e l’accesso alle aziende

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.353 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

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

[Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

# Infostealer: l’economia dei log rubati e l’accesso alle aziende

Come funziona il commercio dei log degli infostealer: abbonamenti, mercati e canali Telegram, prezzi, initial access broker e il ruolo dei dispositivi non gestiti, con i casi Snowflake e CSIRT Italia.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il9 Novembre 20265 Novembre 2026  Condividi

![Infostealer: l'economia dei log rubati e l'accesso alle aziende: Banco di mercato notturno con casse di chiavi e cartellini dei prezzi; un filo lo collega a un portatile su un tavolo di casa](https://www.ictsecuritymagazine.com/wp-content/uploads/infostealer-mercato-log-rubati.webp)

In sintesi

* L'ACN scrive che i log degli infostealer, con credenziali e dati del browser, sono per lo più venduti ad altri attori malevoli.
* Nel 2023 Flare ha rilevato su Russian Market il prezzo di 10 dollari per ogni log, mentre i broker rivendono gli accessi verificati a prezzi superiori.
* Verizon stima che il 46% dei sistemi infettati con possibili credenziali aziendali fosse non gestito, come i portatili dei collaboratori nel caso Snowflake.

Un [infostealer](https://www.acn.gov.it/portale/documents/20119/551838/ACN_Infostealer.pdf/85077a9f-4838-fcf0-6134-9a7db439654f?t=1770734970008) è un software malevolo che raccoglie informazioni da un sistema informatico e le trasferisce a un’infrastruttura controllata dall’attaccante. Le informazioni raccolte si chiamano stealer log, o più semplicemente log. L’ACN scrive che nella maggior parte dei casi vengono vendute ad altri attori malevoli.

Questo articolo segue quel passaggio: come si vendono i log, quanto costano e come arrivano dentro un’azienda. La testata ha già raccontato le operazioni contro diverse famiglie di infostealer, tra cui [Lumma Stealer](/articoli/lumma-stealer/) e [StealC](/notizie/operation-endgame-socgholish-amadey-stealc/).

## Che cosa contiene un log di un infostealer

Un log contiene di solito:

* credenziali di accesso, in particolare a servizi bancari, social network, posta elettronica, VPN e FTP;
* cronologia, cookie, configurazioni ed estensioni del browser;
* carte di credito, conti bancari e portafogli di criptovalute;
* dati di compilazione automatica, come nome, indirizzo e numero di telefono;
* informazioni su hardware e software del dispositivo, antivirus compresi.

Oltre alle credenziali, gli infostealer rubano token delle applicazioni e cookie di sessione. Con questi oggetti l’attaccante entra in un servizio come utente già autenticato. Secondo [Europol](https://www.europol.europa.eu/cms/sites/default/files/documents/Steal-deal-repeat-IOCTA_2025.pdf), nell’IOCTA 2025, i dati su dispositivo e browser servono a imitare l’impronta digitale della vittima.

Usare i log è un metodo efficace e poco costoso per ottenere accessi non autorizzati. Abbassa le barriere d’ingresso, perché dà un vettore di accesso anche a chi non sa compromettere un sistema da solo.

Le cifre sulle dimensioni del fenomeno hanno ambiti diversi. L’ACN riporta una stima per il 2023, ripresa da uno studio di Proton: circa 500 milioni di dispositivi compromessi e oltre 2 miliardi di log. KELA conta nel proprio archivio, per il 2025, circa 3,9 milioni di macchine infettate, da cui ha ricavato 347,5 milioni di credenziali compromesse.

## La filiera: chi fa che cosa

Il modello dominante è il malware-as-a-service. Sviluppatori e operatori affittano infostealer già pronti, con assistenza, aggiornamenti, infrastruttura di comando e controllo e strumenti per analizzare i log. L’abbonamento mensile si paga di norma in criptovalute e costa tra 50 e 250 dollari, con casi che superano le migliaia. La cifra viene da uno studio di Flashpoint del 2024, ripreso dall’ACN.

I passaggi della filiera sono tre, secondo [Flare](https://flare.io/learn/resources/stealer-logs-and-corporate-access). I fornitori vendono l’infostealer su canali Telegram illeciti. Altri attori lo diffondono con finto software craccato o con email di phishing. Poi vendono i log dei dispositivi infetti su mercati specializzati.

I vettori principali di diffusione sono il phishing, il drive-by compromise e il software contraffatto, che comprende versioni gratuite di programmi, videogiochi e strumenti di cracking. Europol cita anche la pubblicità sui motori di ricerca e la manipolazione dei risultati (SEO poisoning) per diffondere finti download. Segnala inoltre la crescita di ClickFix, che induce la vittima a eseguire un comando con finti errori o finti test CAPTCHA.

## Dove si vendono i log

I mercati sono di due tipi. Quelli centralizzati offrono un punto unico di accesso, con ricerca per fonte, provider di rete, data di raccolta e infostealer usato, e una valutazione della reputazione dei venditori. Sono più esposti alle forze dell’ordine.

Quelli decentralizzati si basano su piattaforme di messaggistica come Telegram, con canali privati a cui si accede con un abbonamento. L’ACN lo colloca di solito tra 100 e 500 dollari al mese. Questi mercati veicolano log di valore più alto, ma senza meccanismi di reputazione e con più truffe. Europol conferma lo spostamento verso canali con cifratura end-to-end, dove spesso serve ...