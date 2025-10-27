---
title: Vidar compare ancora in una nuova campagna malspam che sfrutta le caselle PEC
url: https://cert-agid.gov.it/news/vidar-compare-ancora-in-una-nuova-campagna-malspam-che-sfrutta-le-caselle-pec/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-18
fetch_date: 2025-10-06T18:27:29.191003
---

# Vidar compare ancora in una nuova campagna malspam che sfrutta le caselle PEC

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
* Vidar compare ancora in una nuova campagna malspam che sfrutta le caselle PEC

# Vidar compare ancora in una nuova campagna malspam che sfrutta le caselle PEC

17/09/2024

 [PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

Ieri questo CERT ha emesso [un avviso](https://cert-agid.gov.it/news/il-dominio-italiano-di-excite-riutilizzato-in-una-campagna-di-malspam-via-pec/) riguardante una campagna di malspam veicolata tramite caselle PEC, nella quale il link utilizzato verso il dominio italiano **Excite** non supportava alcun payload malevolo. A quanto pare, gli autori di questa campagna hanno in seguito apportato delle modifiche, riproponendo gli stessi contenuti ma utilizzando un dominio attivo che rilascia un file *JavaScript* che porta all’installazione del malware **Vidar**.

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/email_vidar-1.png)

Questa è la quarta ondata che utilizza Vidar (la quinta se includiamo quella errata di ieri) che il CERT-AGID ha registrato nel 2024, tutte concentrate da agosto a oggi.

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/vidar_sept_2024.png)

## Perché gli autori di malware prediligono compromettere le PEC in Italia?

Gli autori di malware ([sLoad](https://cert-agid.gov.it/tag/sload/) prima e [Vidar](https://cert-agid.gov.it/tag/vidar/) oggi) trovano nella compromissione delle caselle PEC un obiettivo allettante, grazie al loro valore legale e alla fiducia che queste ispirano. Compromettendo questi account si può in genere accedere a dati sensibili ed inviare comunicazioni fraudolente che sembrano autentiche aumentando così le possibilità di inganno e diffusione del malware. Questa falsa percezione di sicurezza, insieme al credo comune che la PEC sia immune da compromissioni, rende la Posta Elettronica Certificata un bersaglio privilegiato per attacchi informatici in Italia.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AgID verso i Gestori PEC e verso le strutture accreditate.

Si raccomanda di prestare la massima attenzione alle comunicazioni ricevute via PEC, in particolare quando contengono link ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/09/vidar_17-09-2024.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Il dominio italiano di Excite riutilizzato in una campagna di malspam via PEC](https://cert-agid.gov.it/news/il-dominio-italiano-di-excite-riutilizzato-in-una-campagna-di-malspam-via-pec/)

[Prossima notizia: In atto una campagna di phishing bancario a tema SPID](https://cert-agid.gov.it/news/in-atto-una-campagna-di-phishing-bancario-a-tema-spid/)

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