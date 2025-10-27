---
title: Caratteri Unicode speciali possono essere usati per iniettare comandi nei chatbot
url: https://www.securityinfo.it/2024/10/22/caratteri-unicode-speciali-possono-essere-usati-per-iniettare-comandi-nei-chatbot/?utm_source=rss&utm_medium=rss&utm_campaign=caratteri-unicode-speciali-possono-essere-usati-per-iniettare-comandi-nei-chatbot
source: Securityinfo.it
date: 2024-10-23
fetch_date: 2025-10-06T18:53:26.745113
---

# Caratteri Unicode speciali possono essere usati per iniettare comandi nei chatbot

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

## Caratteri Unicode speciali possono essere usati per iniettare comandi nei chatbot

Ott 22, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/22/caratteri-unicode-speciali-possono-essere-usati-per-iniettare-comandi-nei-chatbot/#respond)

---

Una delle problematiche più discusse degli assistenti di IA riguarda la possibilità di **iniettare dei comandi malevoli** per aprire un canale di comunicazione col tool e ottenere i dati condivisi dagli utenti. Nonostante le precauzioni prese per ridurre l’efficacia delle tecniche dietro questi attacchi, esistono ancora dei modi per inviare comandi ai chatbot senza farsi notare, per esempio tramite i **caratteri Unicode.**

![Unicode chatbot](https://www.securityinfo.it/wp-content/uploads/2024/10/chatbot-6626193_1920.png)

Come [spiega](https://arstechnica.com/security/2024/10/ai-chatbots-can-read-and-write-invisible-text-creating-an-ideal-covert-channel/) Dan Goodin di Ars Technica, gli attaccanti possono **usare caratteri speciali invisibili all’utente ma interpretabili dai chatbot** per iniettare comandi malevoli e prendere il controllo del tool. Poiché questo testo invisibile può essere combinato con quello normale, gli utenti potrebbero copiare e incollare i prompt senza accorgersi della presenza di caratteri speciali.

A illustrare il funzionamento di questa tecnica è stato **Johann Rehberger**, un ricercatore di sicurezza che ha pubblicato **due POC dove ha colpito Microsoft 365 Copilot.**

Nelle POC condivise, l’utente chiede a Copilot di riassumere un’email ricevuta da un mittente non conosciuto. Nell’email ci sono delle istruzioni che chiedono al chatbot di cercare tra le email ricevute in precedenza dall’utente cifre di vendita o password OTP e includerle in un URL che punta al suo server web. L’uso di caratteri nascosti permetteva a Rehberger di **nascondere i dati sensibili raccolti in una stringa invisibile alla fine dell’URL**, il quale compariva normale all’utente.

![](https://www.securityinfo.it/wp-content/uploads/2024/10/hidden-unicode-found-2048x1108-1.jpg)

Seguendo le istruzioni incluse nell’email, le quali istruivano il chabot ad appendere i dati sensibili all’URL codificati con tag Unicode, rendendoli così invisibili. **“*L’URL del browser codifica i caratteri Unicode, poi viene inviato tutto e il server web riceverà il testo codificato nell’URL e lo decodificherà nei caratteri corretti*“.**

## I caratteri invisibili

Le POC di Rehberger derivano da una serie di scoperte fatte da **Riley Goodside**, ricercatore esperto di sicurezza degli LLM. Tra le migliaia di **caratteri dello standard Unicode**, ce ne sono **128 invisibili**, simili ai caratteri ASCII, che venivano usati inizialmente per indicare la lingua dei testi (per esempio “en” per l’inglese o “jp” per il giapponese). Questo range di caratteri viene indicato come **“Tags”.**

Questo utilizzo è stato quasi subito abbandonato e in seguito si è pensato di usare questi caratteri per indicare i Paesi di fianco alle emoji delle bandiere; anche questa opzione è stata scartata e i caratteri sono rimasti inutilizzati.

Goodside ha scoperto che proprio questi 128 caratteri, invisibili nella maggior parte delle interfacce utente, **possono essere compresi dagli LLM e quindi usati per iniettare comandi al chatbot senza che l’utente se ne accorga**. Il ricercatore, già esperto di tecniche di manipolazione dei chatbot tramite testo invisibile, ha sfruttato la sua conoscenza del blocco di caratteri invisibili per dimostrare attacchi di prompt injection contro i chatbot,

## I chatbot vulnerabili alla tecnica dei caratteri Unicode

Secondo quanto riportato da Goodin, attualmente **i servizi più colpiti** dalla tecnica del testo invisibile sono la **web app di Claud**e e **l’API di Claud**e. In entrambi i casi, **i Tag Unicode vengono interpretati  e scritti come testo ASCII**. Fino a poche settimane fa, anche OpenAI API Access e Azure OpenAI API leggevano e scrivevano i Tag e li interpretavano come ASCII; OpenAPI non ha spiegato se questa modifica è legata alla diffusione dei risultati delle POC.

Dopo essere stata contattata in merito alle POC, **anche Microsoft ha modificato il comportamento del suo chatbot**: se a inizio ottobre Copilot Consumer App riusciva ancora a leggere e scrivere i caratteri Unicode nascosti, ora non è più in grado di farlo. Microsoft 365 Copilot invece riesce ancora a leggerli.

Infine, **Gemini può leggere e scrivere i caratteri nascosti ma non li interpreta sempre come testo ASCII**; per questo motivo, gli attaccanti non possono fare completamente affidamento sul chatbot per iniettare comandi.

“***L’onnipresente standard Unicode supporta un framework leggero la cui unica funzione è quella di nascondere dati attraverso la steganografia**, l’antica pratica di rappresentare le informazioni all’interno di un messaggio o di un oggetto fisico*” sottolinea Goodin.

![](https://www.securityinfo.it/wp-content/uploads/2024/10/security-6901712_1920.jpg)

La possibilità di leggere e scrivere i caratteri Unicode pone in serio pericolo gli utenti dei chatbot e **apre a diverse tipologie di attacco**. Il consiglio da parte dei provider di LLM di controllare attentamente l’output di questi tool per evitare leak ...