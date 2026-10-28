---
title: Phishing PagoPA: nuove campagne a tema multe diffuse tramite PEC compromesse
url: https://cert-agid.gov.it/news/phishing-pagopa-nuove-campagne-a-tema-multe-diffuse-tramite-pec-compromesse/
source: Over Security
date: 2026-10-27
fetch_date: 2026-10-28T07:49:33.231261
---

# Phishing PagoPA: nuove campagne a tema multe diffuse tramite PEC compromesse

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
* Phishing PagoPA: nuove campagne a tema multe diffuse tramite PEC compromesse

# Phishing PagoPA: nuove campagne a tema multe diffuse tramite PEC compromesse

27/10/2026

 [multe](https://cert-agid.gov.it/tag/multe/)
[PagoPA](https://cert-agid.gov.it/tag/pagopa/)
[PEC](https://cert-agid.gov.it/tag/pec/)

Nell’ultima settimana il CERT-AGID ha osservato diverse campagne di phishing che utilizzano caselle di posta elettronica certificata **(PEC) compromesse** per distribuire false richieste di pagamento a nome di **PagoPA**.

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/email-fake-pagopa-1024x595.png)

*PEC di phishing PagoPA a tema multe*

Negli ultimi due casi analizzati, il messaggio viene inviato da una PEC compromessa a un indirizzo di posta elettronica ordinaria (PEO), inserendo in copia circa **340 indirizzi PEC**. In entrambi i casi, i collegamenti presenti nei messaggi conducevano a pagine fraudolente ospitate su infrastrutture riconducibili a un provider di hosting russo.

La comunicazione si presenta come un provvedimento amministrativo relativo a una presunta violazione del Codice della Strada. Il testo, caratterizzato da un linguaggio particolarmente formale e da numerosi riferimenti normativi, richiede il pagamento di **198 euro entro una scadenza ravvicinata**, minacciando un aumento dell’importo a 268 euro in caso di ritardo.

Il messaggio presenta un pulsante denominato “**Accesso al portale istituzionale**” che conduce a un sito fraudolento, ospitato su un dominio con estensione `.ru`, che riproduce loghi e grafica di PagoPA.

## Un falso portale con controllo della navigazione

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/home-fake-pagopa-1024x764.png)

*Falsa pagina PagoPA per il pagamento della multa*

Il sito invita la vittima a inserire i propri dati personali, tra cui nome, cognome, codice fiscale, data di nascita, indirizzo email e numero di telefono, per procedere al pagamento della presunta sanzione.

Da ulteriori analisi sono emersi elementi di particolare interessante: **la presenza di un sistema che consente agli attaccanti di controllare da remoto il percorso di navigazione della vittima**.

La pagina comunica con un pannello di gestione sul server ogni mezzo secondo, verificando la presenza di istruzioni per indirizzare l’utente verso ulteriori schermate. Tra queste figurano pagine potenzialmente dedicate alla **raccolta dei dati delle carte di pagamento** e dei **codici di verifica bancaria.**

```
setInterval(function(){
    $.post("../panel/classes/processor.php",
        {redirectionListener:1},
        function(data){
            redirect = data;
            if(redirect == 0){
                return false;
            } else {
                clearRedirections();
                window.location = targets[redirect];
            }
        });
}, 500);
```

Questo meccanismo potrebbe consentire ai criminali di guidare la vittima attraverso le diverse fasi della frode, adattando le richieste alle informazioni necessarie per completarla.

## Oltre 1.800 campagne di phishing a tema multe per PagoPA e SEND

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/campaigns-multe-1024x272.png)

*Andamento delle campagne a tema multe dal 21/04/205 al 27/10/2026*

Il fenomeno delle false multe non è nuovo. **Dal 21 aprile 2025 a oggi, il CERT-AGID ha censito 1.874 campagne di phishing**, a tema multe, che sfruttano i nomi di PagoPA e SEND, individuando e distribuendo alle PA accreditate al [Flusso IoC del CERT-AGID](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) **14.279 indicatori di compromissione (IoC)**.

Le campagne che sfruttano nomi e loghi di PagoPA risultano quasi il doppio rispetto a quelle che impersonano SEND, confermando il persistente interesse dei criminali per i servizi digitali della Pubblica Amministrazione.

L’utilizzo di caselle PEC compromesse rappresenta un ulteriore elemento di attenzione, poiché può indurre i destinatari a considerare attendibili comunicazioni che, in realtà, sono state predisposte per sottrarre dati personali e bancari.

Il CERT-AGID ricorda che **la provenienza di un messaggio da una casella PEC non garantisce la legittimità del contenuto** e raccomanda di verificare eventuali richieste di pagamento direttamente attraverso i canali ufficiali degli enti interessati, senza utilizzare i collegamenti presenti nelle comunicazioni sospette.

## Azioni di contrasto

Il CERT-AGID ha avviato le attività di contrasto con il supporto dei Gestori PEC. Gli Indicatori di Compromissione relativi alla campagna sono stati condivisi attraverso il **[Feed IoC del CERT-AGID](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)** con le strutture accreditate, al fine di consentire l’individuazione e il blocco tempestivo delle infrastrutture e degli artefatti coinvolti.

Si raccomanda di prestare attenzione alle **PEC inattese che fanno riferimento a fatture, pagamenti o solleciti**, anche quando il mittente appare legittimo.

Nel dubbio, le comunicazioni sospette possono essere inoltrate al CERT-AGID per le opportune verifiche.

Taggato
[multe](https://cert...