---
title: Prima campagna di phishing ai danni di Klarna rilevata in Italia
url: https://www.d3lab.net/prima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-24
fetch_date: 2025-11-25T03:13:07.183523
---

# Prima campagna di phishing ai danni di Klarna rilevata in Italia

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

# Prima campagna di phishing ai danni di Klarna rilevata in Italia

[Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Klarna_Phishing_Mail.png?resize=1015%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Klarna_Phishing_Mail.png?fit=1015%2C837&ssl=1 "Klarna_Phishing_Mail")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Klarna_Phishing_Mail.png?resize=1015%2C837&ssl=1)

Venerdì 21 novembre il team anti-frode D3Lab ha identificato la prima campagna di phishing in lingua italiana rivolta agli utenti **Klarna**. L’attacco viene veicolato tramite e-mail e riproduce una comunicazione che informa la vittima della sospensione di alcune funzionalità dell’account a causa di un presunto pagamento non più valido. Il messaggio invita l’utente a verificare la propria identità attraverso un accesso immediato al profilo.

## **La dinamica dell’attacco**

L’obiettivo della campagna è il completo furto dell’account Klarna. La procedura fraudolenta è strutturata in più fasi, tutte accurate nel riprodurre l’esperienza di accesso reale. La vittima viene dapprima invitata a inserire un recapito, come il numero di telefono o l’indirizzo e-mail. Successivamente viene richiesta la password e, come ultima fase, il codice OTP generato da Klarna e inviato alla vittima tramite SMS. Tale modalità lascia presupporre la presenza di un criminale operante in real time, che interagendo con la voittima ha quindi modo di usare con profitto il token OTP prima della sua scadenza.

I criminali intercettano il codice in tempo reale, sfruttando così l’autenticazione a due fattori per completare l’accesso al conto. Questo consente agli attori malevoli di assumere pieno controllo dell’account, con potenziali conseguenze economiche e ulteriori tentativi di frode.

## **Analisi delle pagine di phishing**

Le pagine utilizzate in questa campagna replicano con buona fedeltà l’interfaccia grafica del portale Klarna, presentando colori, layout e riferimenti testuali coerenti con la versione legittima.

### **Schermata di accesso fraudolenta**

Nella prima pagina viene richiesto di inserire un numero di telefono o un indirizzo e-mail. La struttura della schermata, con i riferimenti ai Termini di utilizzo e all’Informativa sulla privacy, è progettata per aumentare la credibilità della pagina e ridurre i sospetti dell’utente.

![Schermata del sito di phishing che imita la pagina di login di Klarna con campo per numero di telefono o email](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Klarna_Phishing_01.png?resize=1025%2C915&ssl=1)

### **Richiesta del codice OTP**

Dopo aver fornito il recapito, la vittima viene reindirizzata alla pagina dedicata alla verifica tramite SMS. La schermata comunica che il codice è stato inviato e che dovrebbe essere ricevuto entro venti secondi, simulando il comportamento del sistema di sicurezza di Klarna.

Il dominio presente nella barra del browser, `kil3kal[.]info`, è uno degli indicatori di compromissione individuati durante l’analisi.

![Schermata della pagina di phishing Klarna che richiede il codice SMS OTP inviato alla vittima](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/11/Klarna_Phishing_02.png?resize=1025%2C915&ssl=1)

## **Indicatori di compromissione**

Durante l’analisi sono stati identificati diversi IoC legati all’infrastruttura utilizzata per ospitare le pagine di phishing. Le URL si appoggiano a domini temporanei o compromessi, tipici delle campagne costruite tramite kit prefabbricati.

```
https://interac[.]es/components/klis[.]php
https://www[.]sma2ll[.]pro/jdk[.]php
https://kil3kal[.]info/klaro
https://kil3kal[.]info/klaro/index2[.]php
```

## **Conclusioni**

Questa rappresenta la prima campagna di phishing in lingua italiana rilevata da D3Lab ai danni di Klarna. L’accuratezza con cui è stato replicato il processo di autenticazione e la capacità di intercettare il codice OTP rendono particolarmente insidioso l’attacco, aumentando significativamente il rischio di compromissione dell’account delle vittime.

Il team di D3Lab mantiene attivo il monitoraggio del brand e continuerà a segnalare tempestivamente eventuali nuove evoluzioni o varianti operative.

24 Novembre 2025/da [Andrea Draghetti](https://www.d3lab.net/author/andrea-d/ "Articoli scritti da Andrea Draghetti")

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/prima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia/&t=Prima%20campagna%20di%20phishing%20ai%20danni%20di%20Klarna%20rilevata%20in%20Italia)
* [Condividi su X](https://twitter.com/share?text=Prima%20campagna%20di%20phishing%20ai%20danni%20di%20Klarna%20rilevata%20in%20Italia&url=https://wp.me/p7upL6-1we)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/prima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Fprima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia%2F&description=Prima%20campagna%20di%20phishing%20ai%20danni%20di%20Klarna%20rilevata%20in%20Italia&media=https%3A%2F%2Fi0.wp.com%2Fwww.d3lab.net%2Fwp-content%2Fuploads%2F2025%2F11%2FKlarna_Phishing_Mail.png%3Ffit%3D705%252C581%26ssl%3D1)
* [Condividi su LinkedIn](https://linkedin.com/shareArticle?mini=true&title=Prima%20campagna%20di%20phishing%20ai%20danni%20di%20Klarna%20rilevata%20in%20Italia&url=https://www.d3lab.net/prima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia/)
* [Condividi su Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.d3lab.net%2Fprima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia%2F&name=Prima%20campagna%20di%20phishing%20ai%20danni%20di%20Klarna%20rilevata%20in%20Italia&description=D3Lab%20ha%20rilevato%20la%20prima%20campagna%20di%20phishing%20in%20italiano%20ai%20danni%20di%20Klarna.%20L%E2%80%99attacco%2C%20diffuso%20tramite%20e-mail%2C%20mira%20al%20furto%20completo%20degli%20account%20delle%20vittime%20attraverso%20la%20richiesta%20di%20recapito%2C%20password%20e%20codice%20OTP.%20Nel%20corso%20dell%E2%80%99analisi%20sono%20emersi%20diversi%20IoC%20collegati%20all%E2%80%99infrastruttura%20utilizzata%20dai%20criminali.)
* [Condividi su Vk](https://vk.com/share.php?url=https://www.d3lab.net/prima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia/)
* [Condividi su Reddit](https://reddit.com/submit?url=https://www.d3lab.net/prima-campagna-di-phishing-ai-danni-di-klarna-rilevata-in-italia/&title=Prima%20campagna%20di%20phishing%20ai%20danni%20di%20Klarna%20rilevata%20in%20Italia)
* [Condividi attraverso Mail](/cdn-cgi/l/email-protection#2b14585e49414e485f167b5942464a0e191b484a465b4a4c454a0e191b4f420e191b5b4342584342454c0e191b4a420e191b4f4a4545420e191b4f420e191b60474a59454a0e191b5942474e5d4a5f4a0e191b42450e191b625f4a47424a0d081b18131049444f5216435f5f5b581104045c5c5c054f18474a4905454e5f045b5942464a06484a465b4a4c454a064f42065b4342584342454c064a42064f4a454542064f420640474a59454a065942474e5d4a5f4a06424506425f4a47424a04)

htt...