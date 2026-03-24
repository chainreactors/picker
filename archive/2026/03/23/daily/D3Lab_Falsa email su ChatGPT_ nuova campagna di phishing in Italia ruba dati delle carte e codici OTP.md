---
title: Falsa email su ChatGPT: nuova campagna di phishing in Italia ruba dati delle carte e codici OTP
url: https://www.d3lab.net/falsa-email-su-chatgpt-nuova-campagna-di-phishing-in-italia-ruba-dati-delle-carte-e-codici-otp/
source: D3Lab
date: 2026-03-23
fetch_date: 2026-03-24T04:18:03.546022
---

# Falsa email su ChatGPT: nuova campagna di phishing in Italia ruba dati delle carte e codici OTP

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

# Falsa email su ChatGPT: nuova campagna di phishing in Italia ruba dati delle carte e codici OTP

[Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/ChatGPT_Phishing_01.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/ChatGPT_Phishing_01.png?fit=1030%2C701&ssl=1 "ChatGPT_Phishing_01")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/ChatGPT_Phishing_01.png?resize=1030%2C701&ssl=1)

I ricercatori di D3Lab hanno rilevato una nuova campagna di phishing che sfrutta il brand **ChatGPT**, servizio sviluppato da OpenAI, per sottrarre dati di carte di pagamento e codici di sicurezza agli utenti italiani.

Si tratta della **prima campagna in lingua italiana osservata da D3Lab** che utilizza questo pretesto, segnale di come i criminali stiano rapidamente adattando le proprie strategie all’evoluzione dei servizi digitali più diffusi.

## La falsa email: pagamento rifiutato della sottoscrizione

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/ChatGPT_Phishing_Mail.png?resize=960%2C1017&ssl=1)

La campagna viene veicolata tramite email in italiano che informano l’utente di un presunto rifiuto nel pagamento dell’abbonamento a ChatGPT.

Nel messaggio viene richiesto di aggiornare urgentemente i dati di pagamento per evitare l’interruzione del servizio. Un elemento indicativo della natura fraudolenta è la presenza del tag **“#email#”** non sostituito correttamente con il nominativo del destinatario, segnale tipico dell’utilizzo di template automatizzati nei kit di phishing.

Il pulsante presente nella comunicazione invita l’utente ad aggiornare i dati della carta, conducendolo verso una pagina malevola.

## Hosting su infrastrutture legittime e landing page realistica

Cliccando sul link, la vittima viene reindirizzata su uno spazio di hosting gratuito basato su sottodomini del dominio `nxcli[.]io`, utilizzato per ospitare la pagina di phishing.

La landing page simula in modo credibile la schermata di pagamento della sottoscrizione **ChatGPT Plus**, mostrando un importo coerente con il costo reale del servizio e riferimenti a sistemi di pagamento noti per aumentare il livello di fiducia dell’utente.

In questa fase vengono richiesti:

* numero della carta
* data di scadenza
* codice CVC
* nome dell’intestatario

Una volta inserite le informazioni, l’utente viene reindirizzato su una seconda pagina in cui viene richiesto il **codice OTP** necessario per autorizzare il pagamento.

## Frode in tempo reale: richiesta del codice OTP

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/ChatGPT_Phishing_02.png?resize=1030%2C701&ssl=1)

La richiesta del codice di sicurezza avviene mentre i criminali tentano immediatamente di eseguire pagamenti con i dati appena sottratti.

Questo schema rappresenta una forma di **frode in tempo reale**, particolarmente pericolosa perché riduce la possibilità per la vittima di accorgersi dell’attacco e bloccare la carta.

## I tentativi di addebito osservati tramite carta canary

Per analizzare il comportamento degli attori criminali, i ricercatori di D3Lab hanno utilizzato una carta di credito fittizia (canary), rilevando **dieci distinti tentativi di addebito nell’arco di un’ora**.

Di seguito il riepilogo delle transazioni osservate:

| Data | Ora (UTC) | Merchant | Paese | Importo |
| --- | --- | --- | --- | --- |
| 23/03/2026 | 08:05 | SIFTFR | FR | 4066.70 MAD |
| 23/03/2026 | 08:15 | GOOGLE \*WALLET TEMP | GBR | 0 EUR |
| 23/03/2026 | 08:17 | SIFTFR | FR | 4066.70 MAD |
| 23/03/2026 | 08:20 | Ditur.es | DK | 945 EUR |
| 23/03/2026 | 08:28 | Ditur.es | DK | 945 EUR |
| 23/03/2026 | 08:34 | Ditur.es | DK | 945 EUR |
| 23/03/2026 | 08:38 | GLOBALTELEHOST CORP. | CAN | -49 USD |
| 23/03/2026 | 09:23 | Ditur.es | DK | 945 EUR |
| 23/03/2026 | 09:25 | Ditur.es | DK | 945 EUR |
| 23/03/2026 | 10:01 | Ditur.es | DK | 1059 EUR |

Tra le attività rilevate figura anche un tentativo di **aggiungere la carta al wallet digitale**, indicatore della volontà di tokenizzare il metodo di pagamento per utilizzarlo successivamente.

## Possibili collegamenti con circuiti fraudolenti internazionali

La presenza di tentativi di addebito in **Dirham marocchini (MAD)** è coerente con pattern osservati in precedenti campagne di phishing attribuite a gruppi criminali attivi nell’area nord-africana.

Sebbene non sia possibile attribuire con certezza la campagna a specifici attori, questi indicatori evidenziano come le operazioni fraudolente siano spesso gestite tramite infrastrutture e merchant internazionali.

## Conclusioni

Le campagne di phishing che sfruttano il brand ChatGPT dimostrano come i criminali informatici adattino rapidamente le proprie strategie ai servizi digitali più utilizzati dagli utenti.

In questo caso, la combinazione tra raccolta dei dati della carta, richiesta del codice OTP e tentativi immediati di eseguire pagamenti fraudolenti rende l’attacco particolarmente pericoloso.

Per questo motivo è fondamentale mantenere sempre alta l’attenzione quando si ricevono comunicazioni relative a pagamenti o abbonamenti online.

## IoC (Indicator of Compromise)

La campagna di phishing viene veicola attraverso i seguenti IoC:

* 5a172d1fdf[.]nxcli[.]io

23 Marzo 2026/da [Andrea Draghetti](https://www.d3lab.net/author/andrea-d/ "Articoli scritti da Andrea Draghetti")

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/falsa-email-su-chatgpt-nuova-campagna-di-phishing-in-italia-ruba-dati-delle-carte-e-codici-otp/&t=Falsa%20email%20su%20ChatGPT%3A%20nuova%20campagna%20di%20phishing%20in%20Italia%20ruba%20dati%20delle%20carte%20e%20codici%20OTP)
* [Condividi su X](https://twitter.com/share?text=Falsa%20email%20su%20ChatGPT%3A%20nuova%20campagna%20di%20phishing%20in%20Italia%20ruba%20dati%20delle%20carte%20e%20codici%20OTP&url=https://wp.me/p7upL6-1zz)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/falsa-email-su-chatgpt-nuova-campagna-di-phishing-in-italia-ruba-dati-delle-carte-e-codici-otp/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Ffalsa-email-su-chatgpt-nuova-campagna-di-phishing-in-italia-ruba-dati-delle-carte-e-codici-otp%2F&description=Falsa%20email%20su%20ChatGPT%3A%20nuova%20campagna%20di%20phishing%20in%20Italia%20ruba%20dati%20delle%20carte%20e%20codici%20OTP&media=https%3A%2F%2Fi0.wp.com%2Fwww.d3lab.net%2Fwp-content%2Fuploads%2F2026%2F03%2FChatGPT_Phishing_01.png%3Ffit%3D705%252C480%26ssl%3D1)
* [Condividi su LinkedIn](https://linkedin.com/shareArticle?mini=true&title=Falsa%20email%20su%20ChatGPT%3A%20nuova%20campagna%20di%20phishing%20in%20Italia%20ruba%20dati%20delle%20carte%20e%20codici%20OTP&url=https://www.d3lab.net/falsa-email-su-chatgpt-nuova-campagna-di-phishing-in-italia-ruba-dati-delle-carte-e-codici-otp/)
* [Condividi su Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.d3lab.net%2Ffalsa-email-su-chatgpt-nuova-campagna-di-phishing-in-italia-ruba-dati-delle-carte-e-codici-otp%2F&name=Fals...