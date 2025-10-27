---
title: Cresce il Phishing ai danni di Binance: analisi di una campagna ben congegnata
url: https://www.d3lab.net/cresce-il-phishing-ai-danni-di-binance-analisi-di-una-campagna-ben-congegnata/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-07
fetch_date: 2025-10-06T22:29:06.451875
---

# Cresce il Phishing ai danni di Binance: analisi di una campagna ben congegnata

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

# Cresce il Phishing ai danni di Binance: analisi di una campagna ben congegnata

[Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_Phishing_01.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_Phishing_01.png?fit=1030%2C783&ssl=1 "Binance_Phishing_01")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_Phishing_01.png?resize=1030%2C783&ssl=1)

In questi primi mesi del 2025 il team di Threat Intelligence di D3Lab ha osservato un aumento preoccupante delle campagne di phishing rivolte agli utenti italiani di **Binance**, la nota piattaforma internazionale per lo scambio di criptovalute. Questo fenomeno non solo si distingue per l’alto volume di attacchi, ma anche per il grado di sofisticazione raggiunto: SMS, email, telefonate e ora anche Telegram vengono sfruttati per colpire le vittime in maniera mirata. In questo articolo analizziamo tecnicamente una delle campagne più attive di quest’anno, con l’obiettivo di informare e proteggere gli utenti.

## Il contesto normativo usato come esca

I truffatori sfruttano un contesto plausibile: l’obbligo di dichiarare le criptovalute nella dichiarazione dei redditi. Nel messaggio viene citata una presunta **dichiarazione SOW**, presentata come necessaria per adempiere agli obblighi normativi anti-riciclaggio (AML), di contrasto al finanziamento del terrorismo (CTF) e fiscali. Gli utenti italiani sono effettivamente obbligati a dichiarare nella propria dichiarazione dei redditi il patrimonio in criptovalute, così come quello in moneta FIAT. Tuttavia, Binance **non richiede mai** l’invio di tali informazioni tramite moduli esterni o link ricevuti via SMS o email.

La terminologia scelta (SOW, AML, imposta di bollo) è credibile e induce l’utente medio a non dubitare della legittimità della richiesta.

## Modalità dell’attacco

La campagna in corso si articola in più fasi e sfrutta diverse tecniche:

#### a. **Smishing**

Gli utenti ricevono SMS con shorturl o domini fake creati Ad Hoc, talvolta dallo stesso mittente che in passato inviava codici 2FA legittimi di Binance grazie alla tecnica di spoofing.

#### b. **Phishing**

Le landing page riproducono fedelmente l’interfaccia di Binance e invitano l’utente a inserire:

* email e numero di telefono
* tipo di cliente (privato o azienda)
* paese di residenza
* valore degli asset crypto
* **screenshot** dell’account Binance (come prova di saldo)

#### c. **Vishing**

A distanza di 24-48 ore, le vittime vengono **contattate telefonicamente** da falsi operatori con accento italiano. Il tono è rassicurante, il linguaggio professionale. Viene chiesto all’utente di accedere a un sito per “validare” la posizione fiscale e in alcuni casi viene richiesto di importare un wallet.

#### d. **Telegram**

Per la prima volta abbiamo rilevato l’invito esplicito a contattare un falso supporto su Telegram. Una modalità pericolosa che consente ai criminali di agire in tempo reale, manipolando la vittima direttamente.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_Smishing_01.webp?resize=464%2C1030&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_Smishing_02.webp?resize=464%2C1030&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_Smishing_03.jpg?resize=475%2C1030&ssl=1)

## Analisi tecnica della campagna

Le campagne analizzate da D3Lab evidenziano un buon livello di organizzazione da parte dei criminali. In particolare:

1. Sfruttano un’infrastruttura di **Command and Control (C2)** per raccogliere le credenziali e le informazioni sensibili inserite dalle vittime.
2. Le credenziali, o parte di esse, vengono **trasmesse anche tramite Telegram** a utenti specifici, a scopo di esfiltrazione o notifica in tempo reale.
3. È stato individuato l’utilizzo di **mailer PHP dedicati** per l’invio automatizzato di email fraudolente, costruite ad hoc per simulare comunicazioni ufficiali Binance.

Questi elementi confermano la natura strutturata e professionale della campagna.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_C2.png?resize=765%2C633&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Binance_Mailer.png?resize=959%2C896&ssl=1)

## Statistiche e trend rilevati da D3Lab

Nel grafico sottostante emerge chiaramente la crescita esponenziale delle campagne di phishing in lingua italiana ai danni di Binance:

**Phishing Binance su base annua (Italia):**

* 2022: 6 casi
* 2023: 29 casi
* 2024: 40 casi
* 2025 (gen-maggio): 168 casi

Questo trend suggerisce una **strategia criminale consolidata**, orientata in modo specifico all’Italia, probabilmente in relazione al crescente interesse per le criptovalute e al nuovo regime fiscale italiano.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/05/Segnalazioni-di-Phishing-ai-danni-di-Binance-Italia.png?resize=1030%2C614&ssl=1)

## Come difendersi

* Binance **non chiede mai via SMS o telefono** l’invio di dati personali o l’accesso a link esterni.
* **Non inviare mai screenshot** dei propri wallet.
* Se ricevi messaggi sospetti, verifica l’indirizzo del dominio: i siti ufficiali terminano con *binance.com*
* **Telegram non è un canale di supporto ufficiale** per Binance.
* In caso di dubbio, accedi solo da app o sito ufficiale, evitando qualsiasi interazione tramite link ricevuti.

## Conclusione

Questa campagna rappresenta una delle forme più insidiose e ben organizzate di phishing mai rilevate contro Binance in Italia. La combinazione di social engineering, falsi obblighi normativi e comunicazioni multi-canale (SMS, email, telefonate, Telegram) rende l’attacco estremamente pericoloso.

6 Maggio 2025/da [Andrea Draghetti](https://www.d3lab.net/author/andrea-d/ "Articoli scritti da Andrea Draghetti")

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/cresce-il-phishing-ai-danni-di-binance-analisi-di-una-campagna-ben-congegnata/&t=Cresce%20il%20Phishing%20ai%20danni%20di%20Binance%3A%20analisi%20di%20una%20campagna%20ben%20congegnata)
* [Condividi su X](https://twitter.com/share?text=Cresce%20il%20Phishing%20ai%20danni%20di%20Binance%3A%20analisi%20di%20una%20campagna%20ben%20congegnata&url=https://wp.me/p7upL6-1uK)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/cresce-il-phishing-ai-danni-di-binance-analisi-di-una-campagna-ben-congegnata/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Fcresce-il-phishing-ai-danni-di-binance-analisi-di-una-campagna-ben-congegnata%2F&description=Cresce%20il%20Phishing%20ai%20danni%20di%20Binance%3A%20analisi%20di%20una%20campagna%20ben%20congegnata&media=https%3A%2F%2Fi0.wp.com%2Fwww.d3lab.net%2Fwp-content%2Fuploads%2F2025%2F05%2FBinance_Phishing_01.png%3Ffit%3D705%252C536%26ssl%3D1)
* [Condividi su LinkedIn](https://linkedin.com/shareArticle?mini=true&title=Cresce%20il%20Phishing%20ai%20danni%20di%20Binance%3A%20analisi%20di%20una%20campagna%20ben%20congegnata&ur...