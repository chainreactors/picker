---
title: Phishing Interactive Brokers in italiano: oltre 6.000 email tentano di rubare le credenziali
url: https://www.d3lab.net/phishing-interactive-brokers-in-italiano-oltre-6-000-email-tentano-di-rubare-le-credenziali/
source: D3Lab
date: 2026-07-20
fetch_date: 2026-07-21T05:03:04.695100
---

# Phishing Interactive Brokers in italiano: oltre 6.000 email tentano di rubare le credenziali

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# Phishing Interactive Brokers in italiano: oltre 6.000 email tentano di rubare le credenziali

[Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/Phishing_IBKR_02.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/Phishing_IBKR_02.png?fit=1030%2C742&ssl=1 "Phishing_IBKR_02")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/Phishing_IBKR_01.png?resize=1030%2C742&ssl=1)

Nella giornata del **17 luglio**, il team antifrode di D3Lab ha individuato e analizzato una campagna di phishing in lingua italiana che sfrutta il nome e l’identità visiva di **Interactive Brokers**, nota piattaforma internazionale di intermediazione finanziaria.

La diffusione è risultata particolarmente rilevante: nel corso delle attività di monitoraggio sono state rilevate **oltre 6.000 email malevole** riconducibili alla stessa operazione fraudolenta.

Si tratta, per quanto osservato finora da D3Lab, della **prima campagna di phishing massiva in lingua italiana** rivolta agli utenti di Interactive Brokers.

È importante precisare che Interactive Brokers non è coinvolta nella diffusione dei messaggi: il brand viene utilizzato abusivamente dai criminali per rendere credibile la comunicazione e indurre i destinatari a consegnare le proprie credenziali.

## Una campagna distribuita attraverso numerosi domini

L’infrastruttura impiegata per distribuire la campagna appare articolata e progettata per ostacolare le attività di rilevamento e blocco.

Dall’analisi condotta da D3Lab sono emersi:

* **16 distinti domini** inseriti all’interno delle email;
* almeno **2 ulteriori domini di destinazione**, raggiunti attraverso meccanismi di reindirizzamento;
* numerosi indirizzi mittente generati utilizzando nomi e sottodomini differenti;
* implementazione di meccanismi di counter detection;
* controlli SPF non superati nei messaggi analizzati.

L’utilizzo di molteplici domini consente agli operatori della campagna di distribuire il traffico e sostituire rapidamente le risorse eventualmente oscurate.

## Dodici differenti oggetti per rendere credibili le email

Uno degli aspetti più interessanti della campagna è rappresentato dall’ampia varietà degli oggetti utilizzati.

Nel campione esaminato sono stati individuati **12 oggetti differenti**, tutti costruiti attorno a temi plausibili per un utente di una piattaforma di trading e investimento, abbinati ad email con specifici template grafici differenti.

Gli oggetti rilevati sono:

> [Protezione Dati] Verifica delle preferenze GDPR e autorizzazioni di accesso

> [Aggiornamento MiFID II] Verifica del profilo di adeguatezza dell’investitore

> [Interactive Brokers] Segnalazione di conformità: Aggiornamento del Codice Fiscale richiesto

> [Rendimento Liquidità] Ottimizzazione degli interessi sulla giacenza in EUR

> [Sicurezza Dispositivi] Registrazione del dispositivo affidabile e verifica 2FA

> [Gestione Valutaria] Configurazione del conto multivaluta e ottimizzazione del cambio EUR/USD

> [Interactive Brokers] Provvedimento di sicurezza: Accesso limitato per anomalie non risolte

> [Interactive Brokers] AVVISO IMPORTANTE: Sospensione funzioni per verifica KYC incompleta

> [Interactive Brokers] Notifica di limitazione conto: Adeguamento MiFID II obbligatorio

> [Interactive Brokers] Restrizione amministrativa: Scadenza del modulo fiscale W-8BEN

> [Informativa Fiscale] Quadro RW — Documentazione annuale per la dichiarazione dei redditi

> [Interactive Brokers] Notifica di revisione annuale: Conferma obbligatoria per riattivazione conto

Gli argomenti scelti non sono casuali. La campagna richiama obblighi normativi, verifiche fiscali, sicurezza dell’account, autenticazione a due fattori, gestione valutaria e rendimenti sulla liquidità.

La varietà dei messaggi permette di intercettare interessi e preoccupazioni differenti. Alcuni oggetti puntano sull’urgenza e sulla paura di perdere l’accesso al conto, mentre altri propongono un apparente vantaggio economico o una normale attività amministrativa.

Nel campione analizzato, gli oggetti più frequenti riguardavano la verifica delle preferenze GDPR, l’aggiornamento MiFID II, il codice fiscale e l’ottimizzazione degli interessi sulla liquidità.

## Il falso avviso di restrizione dell’account

Cliccando sul collegamento presente nell’email, la vittima viene indirizzata verso un sito web che riproduce l’identità visiva di Interactive Brokers.

La prima pagina mostra un falso messaggio intitolato: **“Account Sotto Restrizione”**

Il testo sostiene che sul conto sarebbero state rilevate attività sospette e che alcune funzionalità sarebbero state temporaneamente limitate.

Tra le possibili cause vengono citati:

* tentativi di accesso da una nuova posizione;
* attività di trading insolite;
* modifiche alle informazioni di sicurezza.

Il sito afferma inoltre che l’utente non potrebbe temporaneamente eseguire operazioni di trading, depositare o prelevare fondi oppure utilizzare alcune funzionalità del conto.

Per ripristinare l’accesso viene richiesto di avviare una presunta procedura di verifica dell’identità attraverso il pulsante **“Inizia”**.

## La falsa pagina di accesso

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/Phishing_IBKR_02.png?resize=1030%2C742&ssl=1)

Proseguendo, la vittima raggiunge una seconda pagina che imita il portale di autenticazione di Interactive Brokers.

Il modulo richiede l’inserimento di:

* nome utente;
* password.

Le credenziali digitate non vengono trasmesse al servizio legittimo, ma finiscono sotto il controllo degli autori della campagna.

L’obiettivo dell’attacco è quindi il **furto delle credenziali di accesso alla piattaforma di intermediazione finanziaria**.

Il possesso di queste informazioni potrebbe consentire ai criminali di tentare l’accesso al conto della vittima, raccogliere ulteriori dati personali oppure avviare successive attività di social engineering. La presenza, tra gli oggetti delle email, di riferimenti alla registrazione di dispositivi affidabili e alla verifica 2FA lascia inoltre ipotizzare la possibilità di ulteriori passaggi finalizzati ad acquisire i codici di autenticazione.

20 Luglio 2026/da [Andrea Draghetti](https://www.d3lab.net/author/andrea-d/)

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/phishing-interactive-brokers-in-italiano-oltre-6-000-email-tentano-di-rubare-le-credenziali/&t=Phishing%20Interactive%20Brokers%20in%20italiano%3A%20oltre%206.000%20email%20tentano%20di%20rubare%20le%20credenziali)
* [Condividi su X](https://twitter.com/share?text=Phishing%20Interactive%20Brokers%20in%20italiano%3A%20oltre%206.000%20email%20tentano%20di%20rubare%20le%20credenziali&url=https://wp.me/p7upL6-1DV)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/phishing-interactive-brokers-in-italiano-oltre-6-000-email-tentano-di-rubare-le-credenziali/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Fphishing-interactive-brokers-in-italiano...