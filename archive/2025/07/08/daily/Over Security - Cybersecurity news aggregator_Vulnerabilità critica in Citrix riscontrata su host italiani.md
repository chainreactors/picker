---
title: Vulnerabilità critica in Citrix riscontrata su host italiani
url: https://cert-agid.gov.it/news/vulnerabilita-critica-in-citrix-riscontrata-su-host-italiani/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-08
fetch_date: 2025-10-06T23:39:46.011274
---

# Vulnerabilità critica in Citrix riscontrata su host italiani

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
* Vulnerabilità critica in Citrix riscontrata su host italiani

# Vulnerabilità critica in Citrix riscontrata su host italiani

07/07/2025

 [CitrixBleed](https://cert-agid.gov.it/tag/citrixbleed/)
[CVE-2025-5777](https://cert-agid.gov.it/tag/cve-2025-5777/)

L’emergenza relativa alla vulnerabilità **CVE-2025-5777**, battezzata con nome “**CitrixBleed 2**” per la sua somiglianza con la nota [CVE-2023-4966](https://www.cisa.gov/guidance-addressing-citrix-netscaler-adc-and-gateway-vulnerability-cve-2023-4966-citrix-bleed), già sfruttata in passato per attacchi di ampia portata, non rappresenta una novità improvvisa. La vulnerabilità, riscontrata in Citrix NetScaler ADC e NetScaler Gateway, è stata [resa nota](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX693420&articleTitle=NetScaler_ADC_and_NetScaler_Gateway_Security_Bulletin_for_CVE_2025_5349_and_CVE_2025_5777) e corretta da Citrix a inizio giugno 2025, ma ha recentemente attirato maggiore attenzione a seguito del [rilascio di un Proof-of-Concept](https://labs.watchtowr.com/how-much-more-must-we-bleed-citrix-netscaler-memory-disclosure-citrixbleed-2-cve-2025-5777/) (PoC) pubblico e delle prime segnalazioni di sfruttamento attivo in-the-wild.

Il ritardo nell’applicazione delle patch da parte di molte organizzazioni, incluse numerose Pubbliche Amministrazioni, ha aumentato in modo significativo il rischio di attacchi, soprattutto ora che è disponibile un PoC funzionante e sono stati confermati [tentativi di sfruttamento](https://reliaquest.com/blog/threat-spotlight-citrix-bleed-2-vulnerability-in-netscaler-adc-gateway-devices/).

In data odierna il CERT-AGID ha avuto evidenza di **scansioni pubbliche** mirate a individuare host vulnerabili. Attualmente, su una lista di 18K host, risultano oltre **70 domini italiani potenzialmente vulnerabili** tra cui alcuni di Pubbliche Amministrazioni, istituti bancari, agenzie assicurative e organizzazioni private. Le Pubbliche Amministrazioni coinvolte sono state puntualmente informate dal CERT-AGID affinché possano intraprendere con urgenza le azioni di mitigazione necessarie.

## Modalità di sfruttamento

Il difetto nasce da una validazione insufficiente degli input, che permette a un attaccante remoto **non autenticato** di inviare richieste appositamente costruite che consentono di ottenere risposte contenenti parti di memoria non inizializzate o sensibili. Nello specifico, l’attacco può essere portato a termine con i seguenti step.

* L’attaccante invia una richiesta **HTTP POST manipolata** all’endpoint di login del Gateway.
* La richiesta include solo il parametro `login` senza valore né simbolo “=” (es. `login` al posto di `login=username`).
* Un difetto di inizializzazione nel backend fa sì che il server risponda con una struttura XML contenente il tag `<InitialValue>`, che può esporre dati di memoria non inizializzata.
* L’utilizzo del formato `<InitialValue>%.*s</InitialValue>` per stampare la variabile in questione fa sì che il contenuto venga restituito fino al primo byte nullo. Tuttavia, richieste ripetute possono rivelare segmenti di memoria aggiuntivi.

### Esempio di richiesta che sfrutta la vulnerabilità

```
POST /login HTTP/1.1
Host: [citrix-gateway-target]Content-Type: application/x-www-form-urlencodedContent-Length: 5login
```

## Impatti potenziali

Se sfruttata, la vulnerabilità consente ad attori **non autenticati** di:

* accedere a token di autenticazione direttamente dalla memoria del dispositivo;
* bypassare l’autenticazione a più fattori (MFA);
* dirottare sessioni utente attive;
* ottenere accesso non autorizzato a sistemi critici.

Le conseguenze possono includere violazioni di dati, attacchi ransomware o interruzioni operative.

## Azioni di mitigazione

* Applicare le patch per tutte le versioni supportate e/o aggiornare immediatamente le versioni EOL.
* Dopo l’aggiornamento, terminare tutte le sessioni attive per prevenire accessi non autorizzati tramite sessioni compromesse.
* Monitorare i log per attività sospette, in particolare accessi anomali o provenienti da IP non riconosciuti.

## Risorse utili

* **Supporto ufficiale Citrix:** <https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX693420>
* **PoC in Python per testare la vulnerabilità:** <https://github.com/edelucia/poc/blob/main/CitrixBleed2/CVE-2025-5777.py>

Taggato
[CitrixBleed](https://cert-agid.gov.it/tag/citrixbleed/)
[CVE-2025-5777](https://cert-agid.gov.it/tag/cve-2025-5777/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 28 giugno – 4 luglio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-28-giugno-4-luglio/)

[Prossima notizia: Il tema SPID sfruttato per una nuova campagna di phishing](https://cert-agid.gov.it/news/il-tema-spid-sfruttato-per-una-nuova-campagna-di-phishing/)

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)
CERT-AGID

cerca nel sito

* [Contatti](https://cert-agid.gov.it/contatti/)
* [Privacy](https://cert-agid.gov.it/privacy/)
* [Note legali](https://cert-...