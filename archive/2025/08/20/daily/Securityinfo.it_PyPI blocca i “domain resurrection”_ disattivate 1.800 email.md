---
title: PyPI blocca i “domain resurrection”: disattivate 1.800 email
url: https://www.securityinfo.it/2025/08/19/pypi-blocca-i-domain-resurrection-disattivate-1-800-email/?utm_source=rss&utm_medium=rss&utm_campaign=pypi-blocca-i-domain-resurrection-disattivate-1-800-email
source: Securityinfo.it
date: 2025-08-20
fetch_date: 2025-10-07T00:48:47.054686
---

# PyPI blocca i “domain resurrection”: disattivate 1.800 email

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## PyPI blocca i “domain resurrection”: disattivate 1.800 email

Ago 19, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Scenario](https://www.securityinfo.it/category/news/scenario-news/)
 [0](https://www.securityinfo.it/2025/08/19/pypi-blocca-i-domain-resurrection-disattivate-1-800-email/#respond)

---

Il team di sicurezza della Python Software Foundation, guidato da Mike Fiedler **PyPI,** ha [introdotto un controllo automatico](https://blog.pypi.org/posts/2025-08-18-preventing-domain-resurrections/) sui **domini email scaduti** per impedire il *domain resurrection*, una tecnica con cui gli attaccanti ricomprano un dominio lasciato scadere e lo usano per **prendere il controllo degli account** tramite il reset della password. Dall’inizio di giugno 2025 sono state **invalidate oltre 1.800 caselle** legate a domini in fase di scadenza, così da ridurre un vettore d’attacco subdolo che può portare attacchi molto difficili da identificare.![](https://www.securityinfo.it/wp-content/uploads/2025/08/Deademail19-ago-2025CG-1024x683.png)

## I domini scaduti sono un problema

Gli account PyPI, come molti quelli di molte altre piattaforme, sono legati a indirizzi email; gli indirizzi, a loro volta, dipendono da un **nome di dominio** che può scadere se non rinnovato. Quando ciò accade, **chiunque** può ricomprare quel dominio, configurare la posta e ricevere i link di recupero password per i progetti associati. Su pacchetti **abbandonati ma ancora molto usati** a valle, il rischio si amplifica: un takeover silenzioso può sostituire versioni legittime con **release malevole**, con impatti a catena su CI/CD e ambienti di produzione. Questo scenario non è puramente speculativo, purtroppo: nel 2022 il pacchetto **ctx** su PyPI fu compromesso proprio sfruttando un dominio scaduto del maintainer a cui seguì la pubblicazione di versioni trojanizzate.

## Come funziona il nuovo controllo di PyPI

Per individuare tempestivamente i casi a rischio, PyPI **interroga periodicamente lo stato dei domini** associati agli account, facendo leva sullo **Status API di Domainr** (un servizio Fastly) per capire in quale fase del ciclo di vita si trovano. Quando un dominio entra in **redemption** o in altre fasi indicative della perdita di controllo da parte del legittimo titolare, PyPI **marca l’indirizzo email come “non verificato”** e **non invia** reset password a quell’indirizzo. Dopo un primo controllo massivo ad aprile 2025, il monitoraggio prosegue in modo ricorrente; il team indica una **finestra operativa di 30 giorni** per allineare le verifiche al tipico ciclo “grazia–redemption–pending delete” dei registrar.

## Cosa cambia per gli utenti e per gli attaccanti

La misura **non è un’arma risolutiva**, ma alza significativamente l’asticella. Per un attore ostile, **acquistare un dominio scaduto** non basta più per pilotare la procedura di recupero credenziali: l’email collegata all’account viene disattivata come fattore di prova e l’operazione si interrompe. Il beneficio si estende anche ai progetti poco attivi, dove il maintainer potrebbe non accorgersi per tempo dell’avvenuta scadenza o di un takeover del dominio. Dall’inizio di giugno a oggi, la **revoca della verifica a più di 1.800 indirizzi** conferma che il fenomeno è molto ampio.

Il team PyPI ribadisce alcuni accorgimenti per i maintainer. **Abilitare la 2FA** rimane essenziale e, se l’account usa **un solo indirizzo su dominio personalizzato**, conviene aggiungerne **un secondo su un grande provider** come Gmail o Outlook, così da avere un canale alternativo che non è soggetto a scadenza di dominio. La raccomandazione si intreccia con i processi di **account recovery**: riutilizzare lo stesso indirizzo anche su altri servizi di verifica può facilitare prove di identità incrociate, ma solo se gli altri account sono a loro volta protetti da 2FA.

## Un tassello in più nella difesa della filiera open source

Negli ultimi anni i **software supply-chain attack** hanno spesso fatto leva sugli anelli deboli degli **ecosistemi di pacchetti**, e l’**account takeover** dei maintainer è tra i metodi a **maggior impatto con basso sforzo**. Bloccare i reset password verso indirizzi su **domini scaduti** riduce la superficie d’attacco senza penalizzare gli utenti legittimi, e si affianca ad altre misure introdotte da PyPI, come l’**obbligo di 2FA per gli account attivi** dalla data di riferimento definita dal progetto. L’episodio di **ctx** ha mostrato come un singolo maintainer compromesso possa generare danni su larga scala; l’automazione annunciata questa settimana mira a **intercettare il problema prima che il dominio cambi davvero mano**.

## Prospettive

Il controllo dei domini non copre tutti i casi, ad esempio **trasferimenti legittimi** senza scadenza o scenari in cui l’attaccante compromette direttamente la **2FA** dell’utente. Resta quindi cruciale mantenere **igiene delle identità**, rotazione delle **token di pubblicazione**, segregazione delle **chiavi CI/CD** e monitoraggio delle **release**. Ma l’iniziativa di PyPI è un segnale importante: **prevenire è meglio che ripulire** dopo una compromissione, soprattutto quando l’attacco può propagarsi lungo tutta la filiera di sviluppo.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [2FA](https://www.securityinfo.it/tag/2fa/), [account takeover](https://www.securityinfo.it/tag/account-takeover/), [ato](https://www.securityinfo.it/tag/ato/), [autenticazione a due fattori](https://www.securityinfo.it/tag/autenticazione-a-due-fattori/), [best practice maintainer](https://www.securityinfo.it/tag/bes...