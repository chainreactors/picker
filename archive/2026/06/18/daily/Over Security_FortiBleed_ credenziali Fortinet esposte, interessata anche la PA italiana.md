---
title: FortiBleed: credenziali Fortinet esposte, interessata anche la PA italiana
url: https://cert-agid.gov.it/news/fortibleed-credenziali-fortinet-esposte-interessata-anche-la-pa-italiana/
source: Over Security
date: 2026-06-18
fetch_date: 2026-06-19T07:08:58.483189
---

# FortiBleed: credenziali Fortinet esposte, interessata anche la PA italiana

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
* [Data breach](https://cert-agid.gov.it/category/news/data-breach/)
* FortiBleed: credenziali Fortinet esposte, interessata anche la PA italiana

# FortiBleed: credenziali Fortinet esposte, interessata anche la PA italiana

18/06/2026

 [dataleak](https://cert-agid.gov.it/tag/dataleak/)
[FortiBleed](https://cert-agid.gov.it/tag/fortibleed/)
[Fortigate](https://cert-agid.gov.it/tag/fortigate/)
[Fortinet](https://cert-agid.gov.it/tag/fortinet/)

![](https://cert-agid.gov.it/wp-content/uploads/2026/06/image-1-1024x614.png)

È recentemente emerso un dataset di credenziali compromesse di dispositivi **Fortinet**, denominato **FortiBleed**. Il dataset è stato originariamente scoperto dal ricercatore **[Bob Diachenko](https://www.linkedin.com/posts/vdyachenko_massive-fortinetfortigate-bruteforceactive-share-7471222470814072832-X4zm/)** su un server accessibile pubblicamente, contenente un archivio strutturato di credenziali riferite a interfacce SSL VPN e pannelli di amministrazione di apparati FortiGate distribuiti a livello globale.

Secondo le analisi disponibili, il dataset contiene credenziali riferite a **73.932 URL unici** di firewall e VPN Fortinet, su **21.632 domini distinti**, distribuiti in **194 Paesi**. I dati includono username, indirizzi email e password in chiaro, oltre a metadati descrittivi delle organizzazioni coinvolte.

I settori interessati sono numerosi: telecomunicazioni, servizi IT, finanza, sanità, istruzione, manifatturiero e pubblica amministrazione.

Il dato rilevante, per il contesto nazionale, è che sono emerse evidenze di coinvolgimento anche di enti della Pubblica Amministrazione italiana. Questo rende la minaccia concreta e richiede verifiche immediate da parte di tutte le amministrazioni che utilizzano apparati FortiGate, anche in assenza di una notifica diretta.

## Modalità operative osservate

Allo stato attuale delle informazioni disponibili, l’operazione non risulta legata a una vulnerabilità zero-day di FortiOS.

Le analisi indicano invece una combinazione di tecniche già note, ma applicate su larga scala: credential stuffing con credenziali provenienti da precedenti leak e log di infostealer, attacchi brute force contro interfacce SSL VPN e pannelli di management esposti su Internet, e cracking offline di hash di autenticazione tramite cluster GPU.

Sono stati documentati circa **1,16 miliardi di tentativi di autenticazione** contro circa **320.000 dispositivi FortiGate** esposti su Internet.

Una volta ottenuto l’accesso, i dispositivi compromessi possono essere utilizzati come punti di osservazione passivi per intercettare ulteriore traffico autenticato. Questo può alimentare un ciclo progressivo di compromissione, con il rischio di successivi movimenti laterali verso ambienti interni, inclusi domini Active Directory.

## Impatto sulla Pubblica Amministrazione italiana

Il CERT-AGID ha riscontrato evidenze di coinvolgimento di enti della Pubblica Amministrazione italiana. Le amministrazioni interessate sono state prontamente notificate attraverso i canali istituzionali.

Il punto centrale è che il rischio non riguarda solo gli enti già individuati. La presenza di credenziali valide o riutilizzate, l’esposizione pubblica delle interfacce SSL VPN e la mancanza di controlli forti sugli accessi remoti possono rendere vulnerabili molte altre amministrazioni.

Per questo motivo, la vicenda FortiBleed deve essere trattata come un segnale di allerta operativo. Ogni amministrazione che utilizza apparati FortiGate dovrebbe verificare subito la propria esposizione, controllare i log di autenticazione e rafforzare le misure di protezione degli accessi remoti.

## Raccomandazioni

Si raccomanda a tutte le amministrazioni che utilizzano apparati FortiGate di adottare almeno le seguenti misure:

1. **Abilitare la MFA su tutti gli accessi remoti**, incluse interfacce SSL VPN e interfacce di gestione. Questo riduce il rischio che credenziali già compromesse possano essere riutilizzate con successo.
2. **Rimuovere, ove possibile, l’accesso diretto da Internet alle interfacce di management**. In alternativa, limitarlo tramite ACL e local-in policy, consentendo l’accesso solo da indirizzi IP sorgente autorizzati.
3. **Forzare la rotazione delle credenziali** per gli account amministrativi e per gli utenti VPN, con particolare attenzione agli account privilegiati, condivisi o non più necessari.
4. **Analizzare i log di autenticazione** alla ricerca di accessi anomali per geografia, orario, ASN, indirizzo IP sorgente, user agent o pattern di tentativi ripetuti.
5. **Verificare la presenza di accessi riusciti sospetti**, non limitandosi ai soli tentativi falliti. Un singolo login valido da una sorgente anomala può essere più rilevante di molti errori di autenticazione.
6. **Controllare eventuali movimenti laterali verso la rete interna**, in particolare verso sistemi Active Directory, server critici, sistemi di posta, file server e console di amministrazione.
7. **Aggiornare FortiOS e verificare la configurazione degli apparati**, tenendo presente che in questo caso l’aggiornamento software, da solo, potrebbe non essere sufficiente se le credenz...