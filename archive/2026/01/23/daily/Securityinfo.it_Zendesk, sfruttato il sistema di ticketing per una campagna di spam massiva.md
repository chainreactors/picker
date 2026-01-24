---
title: Zendesk, sfruttato il sistema di ticketing per una campagna di spam massiva
url: https://www.securityinfo.it/2026/01/23/zendesk-sfruttato-il-sistema-di-ticketing-per-una-campagna-di-spam-massiva/?utm_source=rss&utm_medium=rss&utm_campaign=zendesk-sfruttato-il-sistema-di-ticketing-per-una-campagna-di-spam-massiva
source: Securityinfo.it
date: 2026-01-23
fetch_date: 2026-01-24T03:32:35.741725
---

# Zendesk, sfruttato il sistema di ticketing per una campagna di spam massiva

Aggiornamenti recenti Gennaio 23rd, 2026 9:41 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Zendesk, sfruttato il sistema di ticketing per una campagna di spam massiva](https://www.securityinfo.it/2026/01/23/zendesk-sfruttato-il-sistema-di-ticketing-per-una-campagna-di-spam-massiva/)
* [Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive](https://www.securityinfo.it/2026/01/21/sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive/)
* [StackWarp: scoperta una nuova vulnerabilità nei processori AMD](https://www.securityinfo.it/2026/01/20/stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd/)
* [CERT-AGID 10-16 gennaio: ancora phishing PagoPA e nuovi malware bancari](https://www.securityinfo.it/2026/01/19/cert-agid-10-16-gennaio-phishing-pagopa-malware-bancari/)
* [Il 64% delle app di terze parti accede a dati sensibili senza un motivo valido. La ricerca di Reflectiz](https://www.securityinfo.it/2026/01/16/il-64-delle-app-di-terze-parti-accede-a-dati-sensibili-senza-un-motivo-valido-la-ricerca-di-reflectiz/)

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

## Zendesk, sfruttato il sistema di ticketing per una campagna di spam massiva

Gen 23, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/01/23/zendesk-sfruttato-il-sistema-di-ticketing-per-una-campagna-di-spam-massiva/#respond)

---

**Zendesk**, nota piattaforma di ticketing, sta venendo **sfruttata per una campagna di phishing massiva** che sta colpendo utenti in tutto il mondo. A partire dal 18 gennaio, migliaia di utenti hanno infatti iniziato a [segnalare](https://x.com/nickoates_/status/2012761746503606379) di aver ricevuto centinaia di email sospette provenienti da mittenti apparentemente legittimi.

I messaggi arrivano da sistemi di supporto ufficiali di nomi quali Discord, Tinder, Riot Games e Dropbox. Come riporta [Bleeping Computer](https://www.bleepingcomputer.com/news/security/zendesk-ticket-systems-hijacked-in-massive-global-spam-wave/), gli attaccanti stanno sfruttando una **vulnerabilità nei processi di gestione dei ticket di Zendesk.**

La campagna sta abusando delle funzionalità di automazione di Zendesk: molte aziende configurano il proprio supporto clienti per consentire a chiunque, ovvero anche utenti non registrati, di inviare un ticket. Quando un utente invia una richiesta, il sistema genera automaticamente un’email di conferma ricevuta.

![Zendesk](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_67ku5j67ku5j67ku.png)

Gli attaccanti hanno automatizzato l’operazione usando liste con migliaia di indirizzi email e testi arbitrati da usare come oggetto della richiesta, aprendo ticket in maniera massiva. I server di Zendesk, agendo come un relay, hanno quindi cominciato a **inviare migliaia di email agli utenti.** Dal momento che queste email provengono da domini legittimi, riescono a bypassare quasi tutti i filtri antispam tradizionali.

Gli oggetti delle email sono spesso scritti con caratteri Unicode per catturare l’attenzione o eludere ulteriori controlli. Tra gli oggetti più comuni ci sono “FREE DISCORD NITRO!!” e “LEGAL NOTICE FROM ISRAEL”, oppure comunicazioni di presunti ordini di rimozione da parte della Cina o degli USA. Figurano anche richieste d’aiuto con tono disperato e conferme di acquisto fittizie. Anche se i messaggi appaiono allarmanti, gli esperti di sicurezza hanno notato che, al momento, **la maggior parte di essi non contiene link malevoli o tentativi di phishing diretti; è probabile quindi che la campagna sia finalizzata solo al *trolling*** o a testare la capacità di saturazione dei sistemi.

L’attacco ha colpito una vasta gamma di settori, dai videogiochi ai servizi governativi; tra le aziende colpite ci sono CD Projekt, Riot Games, Konami, Square Enix, Discord, Dropbox e i dipartimenti del Lavoro e delle Entrate del Tennessee e della Louisiana.

Alcune aziende hanno comunicato ai propri utenti di ignorare le email di questo tipo, rassicurandoli sul fatto che riceverle non implica la compromissione del loro account personale.

Lato Zendesk, un portavoce dell’azienda ha dichiarato a BleepingComputer di aver introdotto nuove misure di sicurezza, come l’implementazione di alcune restrizioni per bloccare più rapidamente i flussi di spam. **La compagnia aveva in realtà già avvertito i propri clienti nel dicembre precedente riguardo questo rischio**, consigliando di limitare la creazione di ticket ai soli utenti verificati.

In seguito all’attacco, Zendesk ha rinnovato alle aziende le raccomandazioni per ridurre il rischio di campagne simili: oltre a ribadire di [consentire l’invio di ticket solo a utenti con indirizzo email verificato](https://support.zendesk.com/hc/en-us/articles/4408883658906-Permitting-only-added-users-to-submit-tickets), è consigliato rimuovere specifici placeholder (come {{ticket.title}}{{ticket.requester.first\_name}}) per evitare che il testo inserito dall’utente nell’oggetto del ticket venga riportato automaticamente nell’email di conferma inviata dal sistema. Infine, occorre implementare CAPTCHA per rendere il sistema a prova di bot.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [campagna spam](https://www.securityinfo.it/tag/campagna-spam/), [email spam](https://www.securityinfo.it/tag/email-spam/), [spam](https://www.securityinfo.it/tag/spam/), [ticketing](https://www.securityinfo.it/tag/ticketing/), [trolling](https://www.securityinfo.it/tag/trolling/), [Zendesk](https://www.securityinfo.it/tag/zendesk/)

[Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive](https://www.securityinfo.it/2026/01/21/sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Centinaia di estensioni Chrome sfruttate in una campagna di spam](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_z82y4pz82y4pz82y-120x85.png)](https://www.securityinfo.it/2025/10/20/centinaia-di-estensioni-chrome-sfruttate-in-una-campagna-di-spam/ "Centinaia di estensioni Chrome sfruttate in una campagna di spam")

  [Centinaia di estensioni Chrome...](https://www.securityinfo.it/2025/10/20/centinaia-di-estensioni-chrome-sfruttate-in-una-campagna-di-spam/ "Permanent link to Centinaia di estensioni Chrome sfruttate in una campagna di spam")

  Ott 20, 2025  [0](https://www.securityinfo.it/20...