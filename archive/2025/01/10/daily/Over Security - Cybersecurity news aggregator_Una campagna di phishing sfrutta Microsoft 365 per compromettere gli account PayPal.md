---
title: Una campagna di phishing sfrutta Microsoft 365 per compromettere gli account PayPal
url: https://www.securityinfo.it/2025/01/09/una-campagna-di-phishing-sfrutta-microsoft-365-per-compromettere-gli-account-paypal/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-10
fetch_date: 2025-10-06T20:11:40.095688
---

# Una campagna di phishing sfrutta Microsoft 365 per compromettere gli account PayPal

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## Una campagna di phishing sfrutta Microsoft 365 per compromettere gli account PayPal

Gen 09, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/01/09/una-campagna-di-phishing-sfrutta-microsoft-365-per-compromettere-gli-account-paypal/#respond)

---

Di recente è emersa una nuova campagna di phishing che **sfrutta una feature legittima di Microsoft 365 per prendere il controllo degli account PayPal delle vittime.** A lanciare l’allarme è **Carl Windsor, CISO di Fortinet Labs**, che è stato coinvolto in un tentativo di attacco.

In un [post](https://www.fortinet.com/blog/threat-research/phish-free-paypal-phishing) sul blog della compagnia, Windsor ha spiegato di aver ricevuto una mail di richiesta di pagamento da PayPal sul proprio indirizzo email Fortinet, anche se con indirizzo mail di destinazione diverso da quello effettivo. Pur essendo chiaramente phishing visto che il CISO non utilizza la mail professionale per il servizio, Windsor ha deciso di analizzare il messaggio, scoprendo un pattern interessante.

**Sia il mittente che il link interno per il pagamento apparivano autentici**, caratteristica sufficiente a convincere molti utenti della legittimità della richiesta. Cliccando sul link nella mail, si atterra su una pagina di PayPal con la richiesta di un pagamento. **“*Un utente in panico potrebbe essere tentato di loggarsi con il proprio account, ma potrebbe essere molto pericoloso*“** ha specificato Windsor. “*Collega il tuo indirizzo PayPal con l’indirizzo a cui era inviata la mail – non con quella dove è stata ricevuta*“.

![](https://www.securityinfo.it/wp-content/uploads/2024/02/phishing-6573326_1920-1.png)

Pixabay

L’attaccante ha registrato un dominio di test di Microsoft 365, gratuito per tre mesi, e poi ha creato una l**ista di distribuzione con le email delle vittim**e. Da PayPal, l’attaccante ha semplicemente inviato una richiesta di pagamento agli indirizzi specificati.

A questo punto entra in gioco la **funzionalità SRS (Sender Rewrite Scheme) di Microsoft 365** che riscrive il mittente dell’email per facilitare l’inoltro, evitando gli errori causati da SPF. In questo caso, il meccanismo ha permesso all’attaccante di **inviare messaggi di phishing PayPal superando i controlli di sicurezza.**

Una volta che l’utente fa il login su PayPal per verificare il pagamento, **l’account dell’attaccante viene collegato a quello della vittima**; in questo modo, il cybercriminale riesce a prendere il controllo del profilo target.

“***La bellezza di questo attacco è che non usa metodi di phishing tradizionali.** L’email, gli URL  e tutto il resto sono perfettamente legittimi*” spiega Windsor. L’unico modo davvero efficace per proteggersi è mantenersi aggiornati sui metodi di phishing usati dagli attaccanti e verificare sempre la legittimità della richiesta e l’identità del mittente, mettendo in dubbio anche ciò che a primo impatto potrebbe sembrare legittimo.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Fortinet Labs](https://www.securityinfo.it/tag/fortinet-labs/), [Microsoft 36](https://www.securityinfo.it/tag/microsoft-36/), [Microsoft 365 SRS](https://www.securityinfo.it/tag/microsoft-365-srs/), [PayPal](https://www.securityinfo.it/tag/paypal/), [Phishing](https://www.securityinfo.it/tag/phishing/), [scam](https://www.securityinfo.it/tag/scam/)

[CERT-AGID 4 – 10 gennaio: Vidar protagonista con una campagna malspam](https://www.securityinfo.it/2025/01/13/cert-agid-4-10-gennaio-vidar-protagonista-con-una-campagna-malspam/)
[Gli Stati Uniti cambiano opinione sulla crittografia e sulle backdoor](https://www.securityinfo.it/2025/01/08/gli-stati-uniti-cambiano-opinione-sulla-crittografia-e-sulle-backdoor/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![Criminali abusano dei servizi di link wrapping per aggirare i controlli](https://www.securityinfo.it/wp-content/uploads/2025/08/MatrioskaMalware1-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/ "Criminali abusano dei servizi di link wrapping per aggirare i controlli")

  [Criminali abusano dei servizi di link...](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/ "Permanent link to Criminali abusano dei servizi di link wrapping per aggirare i controlli")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/criminali-abusano...