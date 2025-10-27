---
title: Furto di ricette elettroniche: come i criminali rivendono farmaci con le tue prescrizioni
url: https://www.ictsecuritymagazine.com/notizie/ricette-elettroniche/
source: ICT Security Magazine
date: 2025-08-13
fetch_date: 2025-10-07T00:49:30.161785
---

# Furto di ricette elettroniche: come i criminali rivendono farmaci con le tue prescrizioni

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

![Furto di ricette elettroniche: come i criminali rivendono farmaci con le tue prescrizioni](https://www.ictsecuritymagazine.com/wp-content/uploads/freepik__the-style-is-candid-image-photography-with-natural__43710.jpeg)

# Furto di ricette elettroniche: come i criminali rivendono farmaci con le tue prescrizioni

A cura di:[Redazione](#molongui-disabled-link)  Ore 12 Agosto 202517 Luglio 2025

La sanità digitale in Italia sta progressivamente eliminando il supporto cartaceo delle prescrizioni. La **dematerializzazione delle ricette elettroniche** è divenuta obbligatoria (art. 54 Legge di Bilancio 2025), integrandosi nel Sistema Tessera Sanitaria.

Questa rivoluzione normativa mira a migliorare il monitoraggio prescrittivo e l’integrazione nel Fascicolo Sanitario Elettronico, ma allo stesso tempo espone nuove vulnerabilità informatiche. I dati sanitari – diagnosi, terapie, prescrizioni – sono considerati particolarmente sensibili e vengono scambiati nel mercato nero a cifre rilevanti (un singolo record sanitario può valere circa 1.000 dollari). Di conseguenza, i **cybercriminali** mirano sempre più spesso a violare i sistemi di gestione delle ricette per accedere illegittimamente alle prescrizioni elettroniche e ai dati sanitari ad esse associati. Questo articolo analizza le tecniche d’attacco più comuni, il successivo impiego delle ricette trafugate, le implicazioni legali e di salute pubblica, e le contromisure di cybersecurity raccomandate.

## Modalità di accesso fraudolento alle ricette elettroniche

Le ricette elettroniche sono emesse e gestite tramite sistemi informatici gestionali medici e farmaceutici connessi in rete. I criminali utilizzano diverse tecniche per inserirsi in questi sistemi:

* **Phishing e ingegneria sociale**: vengono inviate e-mail o messaggi fasulli a medici, farmacisti o pazienti per carpire credenziali di accesso o informazioni sensibili. Ad esempio, il “credential stuffing” ha già colpito il settore farmaceutico: bot informatici hanno sottratto dati di login dai siti delle farmacie, ottenendo così prescrizioni di farmaci controllati da rivendere nel dark web.
* **Malware e Ransomware**: file allegati malevoli o link compromessi possono infettare i dispositivi dei professionisti sanitari, cifrando dati (ransomware) o rubando credenziali (malware keylogger). Un attacco di tipo *ransomware* all’ospedale può bloccare l’intero gestionale dei pazienti (come già avvenuto in diversi casi italiani).
* **Vulnerabilità dei software gestionali**: molti studi medici e farmacie usano pacchetti gestionali o sistemi legacy non sempre aggiornati. L’assenza di patch di sicurezza apre la porta a exploit mirati. La scarsa segmentazione delle reti interne rende facile il movimento laterale dopo un’intrusione. Spesso i server dei database (p. es. MongoDB, SQL) non sono sufficientemente protetti, esponendoli a furti di interi archivi.
* **Accesso abusivo a database sanitari centrali**: in un contesto europeo, sono stati segnalati data breach che hanno compromesso milioni di cartelle cliniche e prescrizioni. Ad esempio, l’attacco al sistema sanitario di Singapore ha esposto i dati personali di 1,5 milioni di pazienti e 160 mila prescrizioni. Un’eventuale violazione del sistema centrale italiano (Sistema TS) darebbe ai criminali accesso a migliaia di ricette elettroniche.

In sintesi, i medici e i farmacisti devono gestire con attenzione autenticazioni e aggiornamenti software: password forti e cambiate regolarmente, sistemi operativi e antivirus sempre aggiornati, e autenticazione a più fattori per l’accesso alle piattaforme prescrittive. Il fattore umano rimane spesso il punto debole: oltre il 90% degli incidenti sanitari è attribuibile a errori o disattenzioni del personale. Una adeguata formazione del personale sanitario è dunque fondamentale per prevenire **phishing** e [social engineering.](https://www.ictsecuritymagazine.com/articoli/il-social-engineering/)

## Uso illecito e mercificazione delle ricette elettroniche rubate

Una volta trafugata una ricetta elettronica valida, il criminale può procurarsi gratuitamente i farmaci prescritti e poi rivenderli sul mercato nero. Le ricette rubate o contraffatte alimentano due principali filiere illecite:

#### Acquisto illegale di farmaci

I farmaci ottenuti mediante ricette rubate sono consegnati a complici o intermediari che li vendono clandestinamente. Questi prodotti, spesso psicofarmaci o antidolorifici, entrano nella *filiera dell’abuso*: giovani senza prescrizione medica acquistano Xanax, Rivotril e simili per uso ricreativo. In qualche caso le ricette sono pure “confezionate” in anticipo: indagini di polizia hanno trovato ricette elettroniche contraffatte pronte all’uso, acquistate sul dark web e verosimili agli occhi dei software delle farmacie.

#### Vendita sul Dark Web

I criminali possono mettere all’asta online (sui mercati darknet) farmaci ottenuti con ricette rubate, utilizzando canali anonimi. Il Dark Web consente anonimato e l’uso di **criptovalute** (es. bitcoin) per i pagamenti. Studi indicano che i due terzi delle transazioni criminali nel darknet riguardano farmaci illegali. Il fenomeno è spesso collegato alla ‘cibernarco’: documenti comprati clandestinamente che permettono di reperire farmaci di spaccio. Second...