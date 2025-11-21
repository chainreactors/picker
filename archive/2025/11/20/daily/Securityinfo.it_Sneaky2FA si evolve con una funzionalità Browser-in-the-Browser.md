---
title: Sneaky2FA si evolve con una funzionalità Browser-in-the-Browser
url: https://www.securityinfo.it/2025/11/20/sneaky2fa-si-evolve-con-una-funzionalita-browser-in-the-browser/?utm_source=rss&utm_medium=rss&utm_campaign=sneaky2fa-si-evolve-con-una-funzionalita-browser-in-the-browser
source: Securityinfo.it
date: 2025-11-20
fetch_date: 2025-11-21T03:14:07.672158
---

# Sneaky2FA si evolve con una funzionalità Browser-in-the-Browser

Aggiornamenti recenti Novembre 20th, 2025 2:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Sneaky2FA si evolve con una funzionalità Browser-in-the-Browser](https://www.securityinfo.it/2025/11/20/sneaky2fa-si-evolve-con-una-funzionalita-browser-in-the-browser/)
* [DragonForce evolve in un “cartello” ransomware e diventa più aggressivo](https://www.securityinfo.it/2025/11/19/dragonforce-evolve-in-un-cartello-ransomware-e-diventa-piu-aggressivo/)
* [Rust riduce sensibilmente le vulnerabilità di memory safety in Android](https://www.securityinfo.it/2025/11/18/rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android/)
* [Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure](https://www.securityinfo.it/2025/11/18/impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure/)
* [Il protocollo di rete “Finger” rinasce in attacchi ClickFix](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/)

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

## Sneaky2FA si evolve con una funzionalità Browser-in-the-Browser

Nov 20, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2025/11/20/sneaky2fa-si-evolve-con-una-funzionalita-browser-in-the-browser/#respond)

---

I ricercatori di Push Security [hanno scoperto](https://pushsecurity.com/blog/analyzing-the-latest-sneaky2fa-phishing-page/) che gli autori di **Sneaky2FA**, un kit di Phishing-as-a-Service, hanno aggiunto al proprio toolkit una funzionalità di **Browser-in-the-Browser (BITB)**.

“*Di recente abbiamo scoperto un server Sneaky2FA che è un po’ diverso dal classico reverse-proxy Attacker-in-the-Middle, **con una finestra di un browser integrata che contiene l’effettiva pagina di phishing***” spiegano i ricercatori.

![Sneaky2FA](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_yj4dpuyj4dpuyj4d.png)

Sneaky2FA opera principalmente attraverso Telegram, dove i cybercriminali acquistano licenze per ottenere versioni offuscate del codice sorgente che poi distribuiscono autonomamente su server compromessi o domini usa e getta. Attivo da diversi anni, il gruppo ha incluso la nuova funzionalità solo all’inizio del 2025.

La tecnica BITB è stata coniata per la prima volta nel 2022 ed è nata per mascherare URL di phishing simulando una funzionalità di autenticazione in-browser; l’obiettivo è ingannare la vittima mostrandole una barra degli indirizzi falsa che però visualizza l’URL legittimo. **Le pagine BITB replicano infatti le finestre di pop-up con i form di login inserendole in un i-frame che punta a un server malevolo**; l’URL della finestra, però, appare come un link legittimo di login.

## Come funziona BITB in Sneaky2FA

Secondo quando riportato da Push Security, il flusso d’attacco inizia inviando un link alla vittima che punta a un dominio apparentemente legittimo. Quando l’utente atterra sulla pagina, gli viene richiesto di superare un controllo Cloudflare Turnstile o CAPTCHA; questo passaggio serve a **bloccare i crawler dei tool di sicurezza che analizzano la pagina.**

Superato il controllo, la pagina reindirizza a un sottodominio che simula un visualizzatore di documenti. All’utente viene richiesto a questo punto di effettuare l’accesso con l’account Microsoft per visualizzare il documento. Cliccando sul pulsante di login, non si apre una vera nuova finestra, ma **viene generato un pop-up interno alla pagina.**

In questa fase il toolkit si adatta all’OS su cui è in esecuzione: se la vittima usa Windows, il pop-up simula una finestra di Edge/Chrome su Windows; se usa un Mac, simula l’interfaccia di Safari su macOS. Al contempo, la finta barra degli indirizzi mostra l’URL legittimo di Microsoft. A questo punto, quando l’utente inserisce le credenziali e procede con l’MFA, **Sneaky2FA intercetta i dati e il token di sessione e li invia al server malevolo per procedere con il furto dell’account.**

![phishing](https://www.securityinfo.it/wp-content/uploads/2024/06/phishing-6573326_1920-1.png)

Pixabay

Il toolkit è particolarmente ostico da contrastare perché usa una serie di tecniche per evitare il rilevamento degli strumenti di sicurezza, come il **caricamento condizionale**che blocca l’esecuzione del toolkit nel caso l’indirizzo IP che sta visitando la pagina appartenga a vendor di sicurezza, VPN note o proxy, l’**offuscamento del codice**, **script anti-analisi**e **domini effimeri** (*burn and replace*).

È probabile che, vista la sua efficacia, l’uso della tecnica BITB non si fermi a Sneaky2FA, ma venga usata anche in altri kit di phishing. La tecnica, infatti, supera i controlli di sicurezza tradizionali come i gateway email, i filtri e le difese signature-based. È necessario quindi affidarsi a tool di analisi avanzati in grado di individuare i diversi tipi di toolkit in esecuzione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [account takeover](https://www.securityinfo.it/tag/account-takeover/), [browser-in-the-browser](https://www.securityinfo.it/tag/browser-in-the-browser/), [Phishing](https://www.securityinfo.it/tag/phishing/), [phishing-as-a-service](https://www.securityinfo.it/tag/phishing-as-a-service/), [Sneaky2FA](https://www.securityinfo.it/tag/sneaky2fa/), [toolkit phishing](https://www.securityinfo.it/tag/toolkit-phishing/)

[DragonForce evolve in un "cartello" ransomware e diventa più aggressivo](https://www.securityinfo.it/2025/11/19/dragonforce-evolve-in-un-cartello-ransomware-e-diventa-piu-aggressivo/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Il protocollo di rete “Finger” rinasce in attacchi ClickFix](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_3sw5nn3sw5nn3sw5-120x85.png)](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/ "Il protocollo di rete “Finger” rinasce in attacchi ClickFix")

  [Il protocollo di rete...](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/ "Permanent link to Il protocollo di rete “Finger” rinasce in attacchi ClickFix")

  Nov 17, 2025  [0](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/#respond)
* [![Crescono le truffe ai danni dei consumatori, preoccupano q...