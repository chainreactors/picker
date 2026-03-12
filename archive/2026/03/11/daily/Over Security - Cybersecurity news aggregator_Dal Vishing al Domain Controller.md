---
title: Dal Vishing al Domain Controller
url: https://www.certego.net/blog/dal-vishing-al-domain-controller-kill-chain-di-un-attacco-iniziato-via-microsoft-teams/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-11
fetch_date: 2026-03-12T04:08:29.183812
---

# Dal Vishing al Domain Controller

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/dal-vishing-al-domain-controller-kill-chain-di-un-attacco-iniziato-via-microsoft-teams/)

[Are you under attack?](/have-you-been-breached/)

March 11, 2026

## Dal Vishing al Domain Controller

#### Kill Chain completa di un attacco iniziato via Microsoft Teams

![](data:image/svg+xml;charset=utf-8...)

![image](/static/089ef73672f47aff44a7c3d876c981a8/bd885/Certego%20visging%20microsoft%20teams%20kill%20chain.png)![image](/static/089ef73672f47aff44a7c3d876c981a8/bd885/Certego%20visging%20microsoft%20teams%20kill%20chain.png)

**Nelle ultime settimane il nostro SecOps Team ha rilevato un incremento significativo di campagne di Vishing veicolate tramite Microsoft Teams**, in linea con quanto avevamo giÃ  evidenziato [in questo documento](https://www.certego.net/docs/Certego_Vishing_via_Microsoft_Teams.pdf).

Non si tratta di semplice phishing adattato a un nuovo canale di comunicazione. Parliamo di attacchi strutturati, costruiti combinando:

* ingegneria sociale
* abuso di configurazioni cloud permissive
* utilizzo di strumenti legittimi per lâaccesso remoto
* escalation progressiva verso i sistemi core

Lâobiettivo finale osservato Ã¨ chiaro: **ottenere il controllo delle macchine aziendali, fino al Domain Controller**, con il rischio concreto di compromissione dellâintera infrastruttura.

# Kill Chain dellâattacco tipico (MITRE ATT&CK mapping)

## 1. Initial Access â Valid Accounts & Phishing (T1078 / T1566)

Lâattacco inizia con una chiamata improvvisa su Teams.

Gli attaccanti si presentano come personale IT e sfruttano una configurazione spesso lasciata invariata: **Teams consente di default chiamate da utenti esterni**.

Questa fase combina:

* Phishing via servizio di comunicazione (T1566)
* Tentativi di raccolta credenziali â Valid Accounts (T1078)

La leva dominante Ã¨ lâurgenza: un presunto aggiornamento critico di sicurezza Windows che richiede un intervento immediato.

## 2. Execution â Remote Services & User Execution (T1021 / T1204)

Una volta ottenuta la fiducia dellâutente, lâattaccante guida lâinterazione verso lâazione concreta: **condivisione di credenziali, installazione di strumenti di accesso remoto o utilizzo di tool di Remote Support giÃ  presenti sullâhost**.

Qui osserviamo tipicamente:

* User Execution (T1204)
* Remote Services (T1021)
* In alcuni casi Command and Scripting Interpreter (T1059)

Non viene necessariamente distribuito malware custom. Lâattacco si basa su **Living-off-the-Land techniques (LOLBins)**, sfruttando strumenti legittimi giÃ  disponibili nellâambiente. Questo riduce drasticamente gli indicatori tradizionali di compromissione.

[![Gallery 1](/static/40a290cef9282b0c9d4b3a5670e59b84/71c1d/Certego%20qualys%20vulnerability.png)](https://www.certego.net/blog/continuous-vulnerability-detection-qualys-vmdr-ora-nativo-in-panoptikon/)

## 3. Privilege Escalation & Credential Access (T1068 / T1003)

Dopo lâaccesso iniziale, lâobiettivo diventa lâespansione del controllo.

Si osservano:

* raccolta di credenziali
* reset password sospetti
* modifiche agli account

Le tecniche associate possono includere:

* Credential Dumping (T1003)
* Exploitation for Privilege Escalation (T1068)
* Account Manipulation (T1098)

Il fine Ã¨ **ottenere privilegi amministrativi sufficienti per muoversi lateralmente allâinterno dellâinfrastruttura**.

## 4. Lateral Movement & Impact (T1486)

Una volta acquisiti privilegi adeguati, lâattacco entra nella fase piÃ¹ critica: accesso ai sistemi core, **movimento verso Active Directory e tentativo di controllo del Domain Controller**.

In questa fase possono essere attivate:

* Remote Services (T1021)
* Distribuzione di payload ransomware (T1486)
* Persistenza su identitÃ  privilegiate

A questo punto lâ**incidente** non Ã¨ piÃ¹ limitato a un singolo endpoint: **diventa infrastrutturale**.

# PerchÃ© questo attacco elude molte difese

Questo tipo di compromissione Ã¨ particolarmente insidiosa perchÃ©:

1. Utilizza un canale legittimo (Teams)
2. Sfrutta configurazioni di default
3. Impiega strumenti amministrativi leciti
4. Non richiede exploit zero-day

Ã un attacco **identity-driven**. Ed Ã¨ proprio questa caratteristica a renderlo difficile da intercettare con controlli tradizionali basati su firme o IOC statici.

# MDR: cosa deve essere monitorato

Un MDR orientato alla detection engineering deve essere in grado di correlare eventi cloud, endpoint e identity in unâunica vista coerente.

### 1. Eventi anomali su Teams

Segnali rilevanti includono:

* chiamate provenienti da tenant sconosciuti
* tenant di prova o domini onmicrosoft.com
* pattern di contatto verso utenti non tecnici

**Questa visibilitÃ  richiede lâintegrazione dei log Microsoft 365 nel SIEM e la capacitÃ  di analizzare i comportamenti nel tempo**.

### 2. Uso anomalo di strumenti di Remote Support

Gli attaccanti sfruttano tool giÃ  presenti sugli host, riducendo lâimpatto delle soluzioni anti-malware tradizionali.

* Un approccio detection-first efficace prevede:
* alert su esecuzione di tool di remote access fuori baseline
* correlazione tra chiamata Teams e avvio di una sessione remota
* monitoraggio dei privilegi temporanei concessi

Il valore non Ã¨ nel singolo alert, ma nella concatenazione logica degli eventi.

### 3. Identity & Account Monitoring

Tra gli eventi da correlare:

* reset password non pianificati
* modifiche agli account
* cambi di configurazione sugli host

Ancora una volta, Ã¨ la sequenza temporale a fare la differenza: singoli eventi possono sembrare legittimi; la loro combinazione racconta invece una storia diversa.

## Hardening: misure concrete - Revisione delle chiamate esterne su Teams

PoichÃ© Teams consente chiamate da utenti esterni di default, Ã¨ fondamentale intervenire con:

* whitelist di tenant autorizzati
* policy restrittive per utenti non IT

## Blocco dei domini onmicrosoft.com

Gli attaccanti utilizzano frequentemente tenant di prova. Se non necessari, bloccare domini che terminano con onmicrosoft.com riduce significativamente la superficie di attacco.

[![Gallery 1](/static/6435807a8cbc14655ff201e21e910106/71c1d/Certego%20ioc%20intelligence%20mdr.png)](https://www.certego.net/blog/indicatori-di-compromissione-mdr/)

# Detection-first vs Prevention-only

Questo caso dimostra un punto chiave: la prevenzione, da sola, non Ã¨ sufficiente.

Il controllo deve essere continuo e la correlazione cross-layer Ã¨ determinante. Un servizio
MDR focalizzato su:

* telemetria estesa
* detection engineering
* risposta 24/7

puÃ² intercettare la kill chain nelle fasi iniziali, prima che il Domain Controller venga compromesso.

Il Vishing via Teams rappresenta lâevoluzione naturale delle tecniche di social engineering negli ambienti cloud collaborativi.

Non Ã¨ solo la sofisticazione della tecnica di attacco a fare la differenza, ma la capacitÃ  dellâorganizzazione di:
rilevare comportamenti anomali
correlare segnali deboli
interrompere lâescalation prima che diventi sistemica

Dal Vishing al Domain Controller, la distanza puÃ² essere pocaâ¦ **la differenza sta nella capacitÃ  di detection*...