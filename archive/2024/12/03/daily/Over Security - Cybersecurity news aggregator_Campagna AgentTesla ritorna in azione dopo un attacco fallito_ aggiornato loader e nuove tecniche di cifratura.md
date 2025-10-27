---
title: Campagna AgentTesla ritorna in azione dopo un attacco fallito: aggiornato loader e nuove tecniche di cifratura
url: https://cert-agid.gov.it/news/campagna-agenttesla-ritorna-in-azione-dopo-un-attacco-fallito-aggiornato-loader-e-nuove-tecniche-di-cifratura/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-03
fetch_date: 2025-10-06T19:42:20.353227
---

# Campagna AgentTesla ritorna in azione dopo un attacco fallito: aggiornato loader e nuove tecniche di cifratura

* [Vai al contenuto](#main)
* [Vai alla navigazione del sito](#menu "accedi al menu")

[![Logo CERT-AGID](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)](https://cert-agid.gov.it/)

# [CERT-AGID Computer Emergency Response Team AGID](https://cert-agid.gov.it/)

[Agenzia per
l'Italia Digitale](https://www.agid.gov.it)

[![Logo AgID - Agenzia per l'Italia Digitale](/wp-content/themes/cert-agid/assets/images/logo-agid.svg)](https://www.agid.gov.it)

Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

cerca nel sito

[Menu](#menu "accedi al menu")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>

## Menu di navigazione

* Documentazione
  + [Documenti AGID](https://cert-agid.gov.it/documenti-agid/)
  + [Pillole informative](https://cert-agid.gov.it/pillole-informative/)
  + [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)
* [Chi siamo](https://cert-agid.gov.it/chi-siamo/)
* [Contatti](https://cert-agid.gov.it/contatti/)
* [Strumenti](https://cert-agid.gov.it/strumenti/)
  + [hashr](https://cert-agid.gov.it/hashr/)
  + [Verifica HTTPS e CMS](https://cert-agid.gov.it/verifica-https-cms/)
  + [Statistiche sulle campagne italiane di malware e phishing](https://cert-agid.gov.it/statistiche/)
* [Glossario](https://cert-agid.gov.it/glossario/)
  + [0day](https://cert-agid.gov.it/glossario/0day/)
  + [Botnet](https://cert-agid.gov.it/glossario/botnet/)
  + [Data breach](https://cert-agid.gov.it/glossario/data-breach/)
  + [DDOS-DOS](https://cert-agid.gov.it/glossario/ddos-dos/)
  + [Deep-Dark web](https://cert-agid.gov.it/glossario/deep-dark-web/)
  + [Defacing](https://cert-agid.gov.it/glossario/defacing/)
  + [Exploit](https://cert-agid.gov.it/glossario/exploit/)
  + [MITM](https://cert-agid.gov.it/glossario/mitm/)
  + [OSINT-CLOSINT](https://cert-agid.gov.it/glossario/osint-closint/)
  + [Phishing](https://cert-agid.gov.it/glossario/phishing/)
  + [Privilege escalation](https://cert-agid.gov.it/glossario/privilege-escalation/)
  + [Spam](https://cert-agid.gov.it/glossario/spam/)
  + [Spoofing](https://cert-agid.gov.it/glossario/spoofing/)
  + [SQLi-SQL Injection](https://cert-agid.gov.it/glossario/sqli-sql-injection/)
  + [XSS](https://cert-agid.gov.it/glossario/xss/)
* Link utili
  + [Agenzia per l’Italia Digitale](https://www.agid.gov.it/)
  + [CSIRT Italia](https://csirt.gov.it)
  + [CERT-GARR](https://www.cert.garr.it/)
  + [CNAIPIC](https://www.commissariatodips.it/profilo/cnaipic/index.html)
  + [CERT-DIFESA](https://www.difesa.it/smd/cor/cert-difesa/25338.html)

* [Home](https://cert-agid.gov.it/)
* [Notizie](https://cert-agid.gov.it/category/news/)
* [Malware](https://cert-agid.gov.it/category/news/malware/)
* Campagna AgentTesla ritorna in azione dopo un attacco fallito: aggiornato loader e nuove tecniche di cifratura

# Campagna AgentTesla ritorna in azione dopo un attacco fallito: aggiornato loader e nuove tecniche di cifratura

02/12/2024

 [AgentTesla](https://cert-agid.gov.it/tag/agenttesla/)

Le operazioni finalizzate alla diffusione di malware non sempre vengono condotte con la necessaria attenzione. Il CERT-AGID ha già [registrato](https://cert-agid.gov.it/news/malware/anche-i-criminali-sbagliano-il-fattore-errore-umano-nelle-campagne-malware/) in [passato](https://cert-agid.gov.it/news/nuova-campagna-sload-in-atto-su-caselle-pec/) e-mail contenenti malware il cui meccanismo di attivazione si è rivelato difettoso. Questi messaggi presentano allegati pericolosi che, sebbene vengano aperti, non riescono a compromettere i dispositivi delle vittime.

In alcuni casi, questo può essere attribuito a distrazioni da parte degli autori. In altre circostanze, i malfattori non riescono a integrare correttamente i vari strumenti acquistati come MaaS (Malware as a Service), commettendo errori nel collegamento dei diversi componenti, come dimostrato dagli eventi verificatisi di recente.

Nei primi giorni della scorsa settimana, infatti, il CERT-AGID ha rilevato una campagna malevola veicolata massivamente tramite email, in cui l’allegato non riusciva ad attivare la catena di compromissione a causa dell’assenza di un elemento indispensabile: una stringa `"FjDyD6U"` utilizzata come delimitatore per estrarre i byte corretti necessari alla generazione di un nuovo file eseguibile.

In effetti, sebbene [varie sandbox online](https://www.virustotal.com/gui/file/4d386bc8914a74c9d6a1127feb52aa9dd4a5a1ba818a6b05c2f65c383e300271/community) lo identifichino come malevolo, il malware non genera alcun traffico di rete e nessuna sandbox è riuscita a determinare il nome della famiglia di appartenenza.

Nel fine settimana, gli autori della campagna hanno rivisto la loro strategia, ripetendo l’attacco con un malware che questa volta funzionava correttamente.

## Analisi del binario

Il campione analizzato è un file `.NET` che include codice opportunamente cifrato con **AES**. La chiave e l’IV necessari per la decifratura vengono estratti dai byte in sequenza, separati dal delimitatore X8mnGBm come possiamo osservare dalla funzione `smethod_0`.

![](https://cert-agid.gov.it/wp-content/uploads/2024/12/0_code.png)

Questa volta il delimitatore era presente, il che ha reso relativamente semplice l’estrazione delle informazioni necessarie: chiave, IV e codice da decifrare.

![](https://cert-agid.gov.it/wp-content/uploads/2024/12/byte_.png)
![](https://cert-agid.gov.it/wp-content/uploads/2024/12/byte_2.png)
![](https://cert-agid.gov.it/wp-content/uploads/2024/12/byte_3.png)

Utilizzando Cyberchef, è stato possibile decifrare agevolmente le stringhe e ottenere l’eseguibile che il loader carica direttamente in memoria, senza lasciare alcuna traccia sul disco.

![](https://cert-agid.gov.it/wp-content/uploads/2024/12/results2-1024x469.png)

![](https://cert-agid.gov.it/wp-content/uploads/2024/12/results-1024x462.png)

Il binario ottenuto è un malware già noto: si tratta di **[AgentTesla](https://tria.ge/241201-zqnv2s1qav/behavioral1)**, che da oltre due anni si posiziona tra i dieci infostealer più diffusi in Italia.

**AgentTesla** cambia loader con una certa frequenza e, sebbene solitamente utilizzi codice memorizzato nelle risorse, questa volta è stato osservato un nuovo metodo che impiega tecniche di cifratura avanzate per caricare il payload direttamente in memoria, rendendo più difficile la sua rilevazione e analisi.

## Indicatori di Compromissione

Gli IoC relativi a questa campagna sono stati già condivisi con le organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/12/agenttesla_01-12-2024.json)

Taggato
[AgentTesla](https://cert-agid.gov.it/tag/agenttesla/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 23 – 29 novembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-23-29-novembre/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 30 novembre – 6 dicembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-30-novembre-6-dicembre/)

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)
CERT-AGID

cerca nel sito

* [Contatti](https://cert-agid.gov.it/contatti/)
* [Privacy](https://cert-agid.gov.it/privacy/)
* [Note legali](https://cert-agid.gov.it/note-legali/)

#### Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>