---
title: Albiriox, il RAT bancario che si finge UniCredit su Telegram
url: https://www.ictsecuritymagazine.com/notizie/albiriox-rat-bancario-italia/
source: ICT Security Magazine
date: 2026-07-16
fetch_date: 2026-07-17T05:00:18.416532
---

# Albiriox, il RAT bancario che si finge UniCredit su Telegram

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

![Albiriox, il RAT bancario che si finge UniCredit su Telegram](https://www.ictsecuritymagazine.com/wp-content/uploads/Albiriox-il-RAT-bancario-che-si-finge-UniCredit-su-Telegram.png)

# Albiriox, il RAT bancario che si finge UniCredit su Telegram

A cura di:[Redazione](#molongui-disabled-link)  Ore 16 Luglio 202616 Luglio 2026

Una finta promozione, la promessa di 100 dollari e un *bot* Telegram: è la trappola con cui, in una campagna a tema italiano documentata dalla società italiana D3Lab, viene distribuito Albiriox, un *banking trojan* Android costruito per la frode *on-device*. Il marchio abusato è quello di UniCredit, ma conviene chiarirlo subito per non generare equivoci: la banca e i suoi clienti sono le vittime dell’operazione, non la fonte di una compromissione. La catena descritta non coinvolge alcun sistema dell’istituto; ad essere sfruttata è la sua identità, usata come esca.

## La catena di infezione

Secondo l’[analisi di D3Lab](https://www.d3lab.net/fake-banking-rewards-telegram-delivery-and-albiriox-anatomy-of-an-android-malware-campaign/), l’allarme è partito da un servizio di *brand monitoring* che ha intercettato un dominio appena registrato,
`unicredit-tme[.]shop`
, creato l’8 luglio 2026. La pagina promette una ricompensa e invita a scaricare un’app, ma invece di rimandare a uno *store* ufficiale porta a un *bot* Telegram (
`@UniCreditit_bot`
) che guida la vittima nell’installazione. L’incentivo è esplicito: 100 dollari per chi installa l’applicazione e altri 50 per chi invita un amico, un meccanismo *referral* che trasforma il raggiro in un moltiplicatore di diffusione.

La campagna non risulta appoggiarsi a Google Play né ad altri store ufficiali: l’utente viene convinto a installare l’APK manualmente, presumibilmente dopo aver abilitato le sorgenti sconosciute. Il dettaglio tecnico più rilevante è che il file scaricato è un *dropper* autocontenuto: il *payload* di secondo stadio non viene prelevato dalla rete a runtime, ma è già incorporato nell’APK, spezzato in più *asset* con estensioni fuorvianti, ricomposto in locale, decifrato in AES-CBC e decompresso con GZIP. Così la catena di consegna deve solo convincere la vittima a installare il primo file: il resto avviene sul dispositivo, senza un secondo *download* che potrebbe fallire o essere intercettato dai controlli di rete.

## Che cosa fa Albiriox una volta a bordo

Il secondo stadio si registra come servizio di *Accessibility* e da lì controlla il telefono. Le capacità osservate sono quelle di un *banking trojan* moderno: *overlay* per catturare credenziali (con schermate configurabili per *PIN*, *pattern*, coppie utente/password), intercettazione degli SMS e degli *OTP*, controllo remoto in stile VNC con manipolazione dello schermo, fino alla modalità *black screen* che nasconde all’utente ciò che l’operatore sta facendo.

L’operatore non si limita a rubare le password: agisce direttamente dentro le sessioni bancarie legittime, aggirando i passaggi di autenticazione. La comunicazione con il server avviene su un protocollo TCP grezzo con messaggi JSON, verso
`179[.]43[.]159[.]210`
sulle porte
`5555`
e
`5552`
; nel codice compare persino un marcatore di campagna con il paese bersaglio scritto in cirillico,
`Италия`
, indizio dell’ecosistema in cui il *builder* è stato configurato.

L’attribuzione ad Albiriox, spiega D3Lab, poggia sul confronto manuale con un campione noto, sulle somiglianze di protocollo e sul materiale Telegram del progetto: il *sample* italiano appare una *build* personalizzata e offuscata. Vale la cautela d’obbligo sui nomi: si tratta di una *build* riconducibile alla famiglia, le cui funzionalità D3Lab allinea alla versione 1.5 annunciata dagli sviluppatori a gennaio 2026.

## Perché conta per il mercato italiano

Albiriox non nasce oggi. La [ricerca di Cleafy](https://www.cleafy.com/cleafy-labs/albiriox-rat-mobile-malware-targeting-global-finance-and-crypto-wallets), che per prima ne ha descritto la famiglia, lo inquadra come offerta *Malware-as-a-Service* commercializzata su forum di lingua russa, con una fase beta a settembre 2025 e la commercializzazione dall’ottobre successivo, a canoni mensili nell’ordine delle centinaia di dollari; la lista *hardcoded* dei bersagli superava le 400 applicazioni bancarie, di pagamento e *crypto*, come [riportato dalla stampa specializzata](https://thehackernews.com/2025/12/new-albiriox-maas-malware-targets-400.html). La novità della campagna italiana non è quindi il malware in sé, ma la sua localizzazione: un pacchetto pronto all’uso viene calato su un marchio bancario nazionale e distribuito con un *funnel* social semplice ed economico.

Il segnale non è isolato: nella sintesi settimanale del 4-10 luglio il [CERT-AGID](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-4-10-luglio/) ha rilevato campagne italiane a tema *banking* veicolate via SMS con link al download di APK malevoli, tra cui Albiriox insieme a RedWing e RedHook. Vettori diversi, stessa famiglia: nella stessa settimana Albiriox arriva agli utenti italiani per almeno due strade distinte.

Per il settore finanziario italiano contano soprattutto due...