---
title: Phishing ai clienti Telepass: non stai pagando una contravvenzione, ti stanno solo frodando
url: https://www.d3lab.net/phishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando/
source: D3Lab
date: 2026-07-31
fetch_date: 2026-08-01T05:13:26.193915
---

# Phishing ai clienti Telepass: non stai pagando una contravvenzione, ti stanno solo frodando

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

# Phishing ai clienti Telepass: non stai pagando una contravvenzione, ti stanno solo frodando

[Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/20260731_121833.jpg?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/20260731_121833.jpg?fit=1030%2C912&ssl=1 "Screenshot")

Negli ultimi anni si è assistito alla diversificazione dei servizi erogati da istituti bancari, compagnie telefoniche, gestori pagamenti che, nati svolgendo attività in uno specifico ramo di mercato (finanza, telefonia, ecc..), si sono successivamente proposti come erogatori di servizi a tutto tondo.

In tale scenario Telepass non ha fatto eccezione: nata come società dedicata al pagamento dei pedaggi autostradali è stata in breve in grado di offrire servizi diversi di supporto alla mobilità, dal pagamento delle soste, all’ingresso nelle ZTL, alle assicurazioni.

Questo ampliare i servizi verso l’utenza consumer, verso il cittadino, di contro offre ai criminali la possibilità di ingegnerizzare nuove frodi costruendo la loro struttura proprio sull’offerta differenziata ed ampliata dalle diverse società.

Nella giornata odierna il Team D3Lab, grazie al costante monitoraggio degli host facenti parte delle infrastrutture ICT delle organizzazioni criminali, ha individuato due siti di phishing a danno dei clienti Telepass in cui, differentemente da quanto avveniva in passato, non viene richiesto di regolarizzare un mancato pedaggio autostradale, ma di procedere al pagamento di una contravvenzione al Codice della Stada elevata nel comune di Milano.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/20260731_121945.jpg?resize=730%2C1030&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/20260731_122003.jpg?resize=790%2C1030&ssl=1)

*Pagine di phishing*

Il fine ultimo dei criminali è ovviamente quello di carpire i dati di carta di credito delle vittime, inseriti per ottemperare al pagamento, ed abusarne deliberatamente.

La modalità di identificazione del sito clone, derivante da monitoraggi proattivi e non dall’individuazione del vettore di attacco, non permette di sapere se la specifica frode sia diffusa dai criminali via email o sms. Quello che è certo è che la struttura di appoggio fa capo a domini creati ad hoc ***teleapass[.]cfd*** e ***teleapass[.]cyou***, facendo quindi uso delle tecnica del typosquattiing, inserendo un errore che nella fretta può passare inosservato, e dei TLD *cfd* riferito al mondo della moda (clothing, fashion, design) e *cyou* idelmente dedicato al pubblico giovanile.

I dati inseriti dalle vittime vengono istantanemente carpiti dai criminali attraverso WebSocket (WSS), in tal modo anche se l’utente dovesse avere un ripensamento e non cliccare il pulsante di invio del form, il successo per i criminali è garantito.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/Screenshot-2026-07-31-alle-14.56.12.jpg?resize=1030%2C193&ssl=1)

*Analisi traffico*

L’individuazione del pannello di controllo del kit, basato su Phoenix System, palesa l’origine cinese degli sviluppatori del codice.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/20260731_145719.jpg?resize=270%2C300&ssl=1)

*Login Admin panel*

Con il diversificarsi dei servizi lecitamente offerti dalle società è importante che i cittadini, a fronte di inusuali richieste di dati personali o pagamenti, adottino condotte prudenti, verificando il nome dominio dei siti raggiunti attraverso i link proposti in comunicazioni sospette e/o contattando il servizio clienti per chiedere spiegazioni e dettagli. Sebbene anche una verifica di questo tipo possa sembrare facile è bene evidenziare come il contatto non debbe mai avvenire attraverso numeri di telefono riportati dalle comunicazioni o pagina web sospette, questi potrebbero infatti essere stati appositamente inseriti dai criminali e far capo alla loro struttura di comunicazione.

IoC:

* domini fake:
  + teleapass[.]cfd;
  + teleapass[.]cyou;
* URL:
  + ht[tps:/]/teleapass[.]cyou/IT;
  + ht[tps:/]/teleapass[.]cfd/IT.

31 Luglio 2026/da [Denis D3Lab](https://www.d3lab.net/author/denis-f/)

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/phishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando/&t=Phishing%20ai%20clienti%20Telepass%3A%20non%20stai%20pagando%20una%20contravvenzione%2C%20ti%20stanno%20solo%20frodando)
* [Condividi su X](https://twitter.com/share?text=Phishing%20ai%20clienti%20Telepass%3A%20non%20stai%20pagando%20una%20contravvenzione%2C%20ti%20stanno%20solo%20frodando&url=https://wp.me/p7upL6-1Eo)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/phishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Fphishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando%2F&description=Phishing%20ai%20clienti%20Telepass%3A%20non%20stai%20pagando%20una%20contravvenzione%2C%20ti%20stanno%20solo%20frodando&media=https%3A%2F%2Fi0.wp.com%2Fwww.d3lab.net%2Fwp-content%2Fuploads%2F2026%2F07%2F20260731_121833.jpg%3Ffit%3D705%252C624%26ssl%3D1)
* [Condividi su LinkedIn](https://linkedin.com/shareArticle?mini=true&title=Phishing%20ai%20clienti%20Telepass%3A%20non%20stai%20pagando%20una%20contravvenzione%2C%20ti%20stanno%20solo%20frodando&url=https://www.d3lab.net/phishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando/)
* [Condividi su Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.d3lab.net%2Fphishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando%2F&name=Phishing%20ai%20clienti%20Telepass%3A%20non%20stai%20pagando%20una%20contravvenzione%2C%20ti%20stanno%20solo%20frodando&description=Negli%20ultimi%20anni%20si%20%C3%A8%20assistito%20alla%20diversificazione%20dei%20servizi%20erogati%20da%20istituti%20bancari%2C%20compagnie%20telefoniche%2C%20gestori%20pagamenti%20che%2C%20nati%20svolgendo%20attivit%C3%A0%20in%20uno%20specifico%20ramo%20di%20mercato%20%28finanza%2C%20telefonia%2C%20ecc..%29%2C%20si%20sono%20successivamente%20proposti%20come%20erogatori%20di%20servizi%20a%20tutto%20tondo.%20In%20tale%20scenario%20Telepass%20non%20ha%20fatto%20eccezione%3A%20nata%20come%20societ%C3%A0%20dedicata%20al%20%5B%E2%80%A6%5D)
* [Condividi su Vk](https://vk.com/share.php?url=https://www.d3lab.net/phishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando/)
* [Condividi su Reddit](https://reddit.com/submit?url=https://www.d3lab.net/phishing-ai-clienti-telepass-non-stai-pagando-una-contravvenzione-ti-stanno-solo-frodando/&title=Phishing%20ai%20clienti%20Telepass%3A%20non%20stai%20pagando%20una%20contravvenzione%2C%20ti%20stanno%20solo%20frodando)
* [Condividi attraverso Mail](/cdn-cgi/l/email-protection#aa95d9dfc8c0cfc9de97fac2c3d9c2c3c4cd8f989acbc38f989ac9c6c3cfc4dec38f989afecfc6cfdacbd9d98f99eb8f...