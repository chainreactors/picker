---
title: Plugin WordPress di Awesome Motive avvelenati via CDN: la fiducia nello script di terze parti diventa la porta d’ingresso
url: https://www.ictsecuritymagazine.com/notizie/awesome-motive-pushengage-optinmonster-supply-chain-cdn/
source: ICT Security Magazine
date: 2026-06-16
fetch_date: 2026-06-17T07:04:01.676455
---

# Plugin WordPress di Awesome Motive avvelenati via CDN: la fiducia nello script di terze parti diventa la porta d’ingresso

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

![Plugin WordPress di Awesome Motive avvelenati via CDN](https://www.ictsecuritymagazine.com/wp-content/uploads/Plugin-WordPress-di-Awesome-Motive-avvelenati-via-CDN.png)

# Plugin WordPress di Awesome Motive avvelenati via CDN: la fiducia nello script di terze parti diventa la porta d’ingresso

A cura di:[Redazione](#molongui-disabled-link)  Ore 16 Giugno 202616 Giugno 2026

Un attaccante ha manomesso i file JavaScript serviti da tre plugin WordPress molto diffusi, **PushEngage**, **OptinMonster** e **TrustPulse**, tutti dello stesso editore (Awesome Motive), trasformandoli in un canale per impiantare backdoor nei siti che li caricavano. La società di sicurezza [Sansec](https://sansec.io/research/optinmonster-supply-chain-attack) ha divulgato la campagna il 13 giugno 2026; PushEngage ha pubblicato il proprio avviso di incidente il giorno dopo. Per la linea editoriale di ICT Security Magazine la notizia conta non come singolo incidente, ma come ennesima dimostrazione che la superficie d’attacco si è spostata sulla [supply chain](https://www.ictsecuritymagazine.com/tag/supply-chain-security/) del software: a cedere non è una vulnerabilità del sito, ma la fiducia riposta in uno script di terze parti distribuito via *CDN*. Lo schema è quello che Sansec accosta esplicitamente al caso Polyfill del 2024: manomettere un singolo file a monte per raggiungere migliaia di siti a valle.

## Come ha funzionato l’attacco

Lo script avvelenato non faceva nulla su una normale visita. Si attivava solo quando un amministratore WordPress autenticato caricava la pagina, e a quel punto sfruttava la sessione dell’amministratore per agire con pieni privilegi. La sequenza, ricostruita da Sansec su tutti e tre i plugin e confermata da [PushEngage](https://www.pushengage.com/security-incident-tampered-script-served-via-pushengage/) sul proprio, è lineare: creazione di un nuovo account amministratore controllato dall’attaccante (nomi tipo developer\_api1 o dev\_xxxxxx), installazione di un plugin che non compare nella *dashboard*, apertura di una *web shell* (un canale di comando remoto raggiungibile da chi conosce l’URL, senza autenticazione) ed esfiltrazione delle nuove credenziali verso il dominio tidio[.]cc, un falso costruito per somigliare al legittimo tidio.com. Quel dominio era stato registrato il 28 aprile, settimane prima: segno di un’operazione pianificata, non di un colpo improvvisato.

È qui il punto che i difensori devono interiorizzare: poiché la backdoor è progettata per restare fuori dalle schermate di amministrazione, la *dashboard* di WordPress non può dire se il sito è stato colpito. Il plugin nascosto si presenta con cartelle dal nome rassicurante, content-delivery-helper (“Content Delivery Helper”) o database-optimizer (“Database Optimizer”), e l’unico controllo affidabile è lato server, sul filesystem e nei log.

## La portata, da non confondere con il danno

Sansec stima che i tre plugin raggiungano oltre 1,2 milioni di siti, in larga parte attribuibili a OptinMonster, che da solo supera il milione di installazioni attive; il [plugin WordPress](https://wordpress.org/plugins/pushengage/) di PushEngage ne conta oltre 9.000. È un numero di diffusione, non di compromissione: misura i siti che eseguono i plugin, non quelli effettivamente violati. La finestra di esposizione, peraltro, è stata diseguale e in controtendenza rispetto alla diffusione: secondo Sansec il codice malevolo è rimasto in OptinMonster e TrustPulse per circa venticinque minuti il 12 giugno (dalle 22:17 alle 22:42 UTC), mentre per PushEngage è durata diverse ore il 12 giugno, con lo script ancora servito da alcuni nodi *edge* della *CDN* fino al 14 giugno (ultima rilevazione verificata il 13 giugno alle 19:02 UTC). I due plugin con più siti hanno avuto la finestra più stretta; PushEngage, la più ampia. La ricostruzione resta in aggiornamento: alla data della divulgazione sia Sansec sia PushEngage indicavano la *timeline* come ancora in verifica, e Sansec segnalava il server di comando tuttora attivo nel generare nuovi *payload*.

## Il punto d’ingresso conteso

Sull’origine della violazione le due ricostruzioni divergono, e vale la pena riportarlo con onestà. PushEngage sostiene che l’attaccante sia entrato nel server del suo sito di *marketing*, separato dai sistemi che gestiscono il prodotto e i dati dei clienti, sfruttando una falla nota in UpdraftPlus, un plugin di backup. Ciò che contava non era il server, ma una chiave che vi risiedeva: una *API key* della *CDN*. Con quella chiave l’attaccante non ha dovuto violare i sistemi principali; gli è bastato modificare i file che la *CDN* già distribuiva ai siti dei clienti. Sansec, però, non considera chiuso il punto d’ingresso: indica come più probabile un server di Awesome Motive, possibile l’account *CDN*, improbabile il provider BunnyNet. Va precisato che l’analisi pubblica di Sansec non avalla la tesi di UpdraftPlus, che proviene dalla sola PushEngage e riguarda il suo ambiente. UpdraftPlus ha effettivamente una vulnerabilità distinta di *authentication bypass*, [CVE-2026-10795](https://nvd.nist.gov/vuln/detail/CVE-2026-10795), valutata 8,1 da Wordfence, ora corretta e già oggetto ...