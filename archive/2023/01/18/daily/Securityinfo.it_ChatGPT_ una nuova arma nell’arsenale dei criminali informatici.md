---
title: ChatGPT: una nuova arma nell’arsenale dei criminali informatici
url: https://www.securityinfo.it/2023/01/17/chatgpt-una-nuova-arma-nellarsenale-dei-criminali-informatici/?utm_source=rss&utm_medium=rss&utm_campaign=chatgpt-una-nuova-arma-nellarsenale-dei-criminali-informatici
source: Securityinfo.it
date: 2023-01-18
fetch_date: 2025-10-04T04:11:35.980581
---

# ChatGPT: una nuova arma nell’arsenale dei criminali informatici

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## ChatGPT: una nuova arma nell’arsenale dei criminali informatici

Gen 17, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2023/01/17/chatgpt-una-nuova-arma-nellarsenale-dei-criminali-informatici/#respond)

---

Da quando lo scorso novembre [OpenAI](https://openai.com/) ha rilasciato ChatGPT, il nuovo strumento ha iniziato ad **attirare l’interesse degli utenti privati e delle aziende** per le sue molteplici possibilità di utilizzo.

ChatGPT ha però anche catturato l’attenzione dei criminali informatici, perché è diventato presto evidente che **le sue funzioni di generazione di codice possono aiutare gli attori delle minacce** meno qualificati a lanciare attacchi informatici senza grande sforzo.

[Check Point Research](https://research.checkpoint.com/) ha analizzato in profondità le capacità di questo tool, mostrando tre differenti casi in cui **criminali informatici utilizzano OpenAI per sviluppare strumenti dannosi**. Alcuni di questi criminali non hanno alcuna capacità di sviluppo.

Gli esperti dell’azienda prevedono che **gli attori delle minacce più sofisticati miglioreranno il modo in cui utilizzano** gli strumenti basati sull’intelligenza artificiale per creare attacchi sempre più evoluti.

## Creare un Infostealer

Il 29 dicembre 2022, un thread intitolato “ChatGPT – Benefits of Malware” è **apparso su un popolare forum**.

L’autore del thread ha rivelato che stava **utilizzando ChatGPT per ricreare malware e tecniche descritte in pubblicazioni di ricerca** e articoli sul malware.

![](https://www.securityinfo.it/wp-content/uploads/2023/01/Caso-1.png)

Fonte: Check Point Research

Come esempio ha condiviso il codice di un **Infostealer basato su Python che cerca tipi di file comuni**, li copia in una cartella casuale all’interno della cartella Temp, li comprime e li carica su un server FTP.

Inoltre, ha condiviso un frammento di codice Java che **scarica ed esegue PuTTY**, un client SSH e telnet molto comune, utilizzando Powershell.

Questo thread è stato pensato per **spiegare ai criminali informatici meno capaci come utilizzare ChatGPT** per scopi dannosi, con esempi reali che possono utilizzare immediatamente.

## Strumenti di crittografia

Il 21 dicembre 2022, un attore di minacce soprannominato USDoD ha pubblicato uno script Python, che ha sottolineato essere **il primo script che abbia mai creato**.

![](https://www.securityinfo.it/wp-content/uploads/2023/01/Caso-2.png)

Fonte: Check Point Research

L’analisi dello script ha rivelato che **esegue operazioni crittografiche** come generazione di chiavi, firma, cifratura e decifratura dei file utilizzando algoritmi come la crittografia a curva ellittica, curva ed25519, Blowfish, Twofish, RSA, certificati PEM e funzioni hash.

Lo script include anche due funzioni principali che possono essere utilizzate per **cifrare un singolo file o una directory** specifica.

Anche se lo script può essere utilizzato in modo del tutto legittimo, può facilmente essere **modificato per diventare un ransomware**.

USDoD è un membro conosciuto della comunità underground che **si dedica a varie attività illecite**, tra cui la vendita dell’accesso a società compromesse e database rubati.

## ChatGPT per attività fraudolente

L’ultimo esempio è stato pubblicato la notte di Capodanno del 2022 e ha dimostrato l’uso di ChatGPT per **creare script per market Dark Web**.

![](https://www.securityinfo.it/wp-content/uploads/2023/01/Caso-3.png)

Fonte: Check Point Research

Il criminale informatico ha mostrato quanto sia facile creare un market Dark Web utilizzando ChatGPT, fornendo una **piattaforma per il commercio automatizzato di beni illegali o rubati** come conti o carte di pagamento, malware o persino droghe e munizioni, con pagamenti in criptovalute.

Inoltre, gli attori delle minacce hanno aperto discussioni in ulteriori forum incentrati su come utilizzare ChatGPT per schemi fraudolenti, come la **generazione di arte casuale** con un’altra tecnologia OpenAI (DALL-E 2) e la vendita online utilizzando piattaforme legittime come Etsy.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chatgpt](https://www.securityinfo.it/tag/chatgpt/), [Check Point Research](https://www.securityinfo.it/tag/check-point-research/), [dall-e](https://www.securityinfo.it/tag/dall-e/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [openai](https://www.securityinfo.it/tag/openai/)

[Microsoft e ACN uniscono le forze per la sicurezza informatica in Italia](https://www.securityinfo.it/2023/01/18/microsoft-e-acn-uniscono-le-forze-per-la-sicurezza-informatica-in-italia/)
[GitHub code scanning facilita l'analisi delle vulnerabilità](https://www.securityinfo.it/2023/01/17/github-code-scanning/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_camyclcamyclcamy-120x85.png)](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt...