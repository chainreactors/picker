---
title: Torna Shalai Ulud: centinaia di pacchetti compromessi
url: https://www.securityinfo.it/2025/11/25/torna-shalai-ulud-centinaia-di-pacchetti-compromessi/?utm_source=rss&utm_medium=rss&utm_campaign=torna-shalai-ulud-centinaia-di-pacchetti-compromessi
source: Securityinfo.it
date: 2025-11-25
fetch_date: 2025-11-26T03:17:09.130016
---

# Torna Shalai Ulud: centinaia di pacchetti compromessi

Aggiornamenti recenti Novembre 25th, 2025 6:31 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Torna Shalai Ulud: centinaia di pacchetti compromessi](https://www.securityinfo.it/2025/11/25/torna-shalai-ulud-centinaia-di-pacchetti-compromessi/)
* [DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”](https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/)
* [CERT-AGID 15–21 novembre: attacchi a università, banche e PEC](https://www.securityinfo.it/2025/11/24/cert-agid-15-21-novembre-attacchi-universita-banche-pec/)
* [Come Firemon supporta i propri partner nel processo di migrazione da Skybox](https://www.securityinfo.it/2025/11/21/come-firemon-supporta-i-propri-partner-nel-processo-di-migrazione-da-skybox/)
* [Sneaky2FA si evolve con una funzionalità Browser-in-the-Browser](https://www.securityinfo.it/2025/11/20/sneaky2fa-si-evolve-con-una-funzionalita-browser-in-the-browser/)

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

## Torna Shalai Ulud: centinaia di pacchetti compromessi

Nov 25, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/11/25/torna-shalai-ulud-centinaia-di-pacchetti-compromessi/#respond)

---

I ricercatori di Wiz Threat Research e Aikido [hanno segnalato](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack) il ritorno di una massiccia campagna di attacchi supply-chain soprannominata **“Shalai Ulud 2.0”**, un’operazione su vasta scala che ha colpito ecosistemi open-source come NPM e PyPI.

Come [spiega](https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains) il team di Aikido, si tratta di una seconda ondata di attacchi (la prima era avvenuta a metà settembre). “*Shai-Hulud, che prende il nome dai giganteschi vermi delle sabbie di Dune come parte del gusto dell’autore dell’attacco per la teatralità, è un **worm NPMautoreplicante creato per diffondersi rapidamente attraverso gli ambienti di sviluppo compromessi**. Una volta infettato un sistema, cerca segreti esposti come chiavi API e token utilizzando TruffleHog e pubblica tutto ciò che trova in un repository GitHub pubblico. Quindi tenta di inviare nuove copie di se stesso a NPM, aiutandolo a propagarsi nell’ecosistema, mentre esfiltra i dati all’attaccante*” spiegano i ricercatori.

![Shalai Ulud](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_e2m231e2m231e2m2.png)

L’obiettivo degli attaccanti è appunto quello di infiltrarsi negli ambienti di sviluppo e nelle pipeline CI/CD per infettare i pacchetti usati dagli sviluppatori ed eseguire furti di credenziali, criptomining e ottenere accesso persistente ai sistemi.

I pacchetti infetti vengono distribuiti sfruttando account maintainer che pubblicano **versioni compromesse di pacchetti legittimi.** Gli attaccanti creano pacchetti con nomi molti simili a quelli di librerie note, cambiando solo una lettera o aggiungendo un trattino; spesso prendono di mira strumenti interni di grandi aziende, sperando che gli sviluppatori digitino male il nome durante l’installazione.

Per far sembrare legittimi i pacchetti malevoli, gli attaccanti collegano i metadati del pacchetto (su NPM o PyPI) ai repository GitHub di progetti reali; in questo modo, il pacchetto malevolo appare sul registry pubblico mostrando migliaia di “stelle” e statistiche di utilizzo che in realtà appartengono a un altro progetto legittimo.

In questa seconda ondata di attacchi, i ricercatori hanno individuato **tecniche avanzate di offuscamento multilivello.** Spesso il payload finale non è incluso nel pacchetto stesso, ma viene scaricato dinamicamente da un server remoto solo dopo l’installazione, rendendo più difficile il rilevamento statico da parte degli antivirus tradizionali.

Dopo l’installazione del pacchetto, il payload malevolo si differenzia in due moduli che eseguono differenti workflow. In primo luogo, viene installata una **backdoor** sulla macchina infetta che consente agli attaccanti di eseguire comandi da remoto. Un altro modulo si occupa di **esfiltrare i *secret* di GitHub** e di caricarli come artefatti.

Il malware è anche in grado di cercare ed esfiltrare credenziali da file di configurazione locali, variabili d’ambiente, metadati dei servizi cloud, token di autenticazione per esfiltrare i secret AWS, Google Cloud ed Azure; inoltre, il malware tenta di assumere ruoli con privilegi elevati per manipolare le policy IAM per effettuare un’ulteriore escalation dei privilegi.

![](https://www.securityinfo.it/wp-content/uploads/2025/11/blockchain-3750157_1920.jpg)

Secondo quanto riportato da Wiz, attualmente l’impatto delle compromissioni si attesta a 775 token di accesso a GitHub, 373 credenziali AWS, 300 credenziali GCP e 115 credenziali Azure. In totale, ci sono **più di 25.000 repository infetti per più di 350 utenti unici**.

Shalai Ulud, soprattutto nella sua nuova versione, è particolarmente preoccupante perché usa tecniche di attacco e di offuscamento particolarmente sofisticato. La campagna è **altamente automatizzata** e le operazioni in corso possono generare e pubblicare **centinaia di pacchetti al giorno**.

Per proteggersi da Shalai Ulud, la prima cosa da fare è **rimuovere i pacchetti compromessi** e installare versioni legittime; in seguito, è necessario **ruotare tutte le credenziali**, revocando e rigenerando i token NPM, i PAT GitHub, le chiavi SSH e le credenziali per i servizi cloud.

I ricercatori consigliano inoltre di cercare e segnalare repository creati di recente con “Shai-Hulud” nella descrizione, controllare la presenza di workflow non autorizzati o commit sospetti e monitorare le nuove pubblicazioni NPM della propria organizzazione. In generale è inoltre buona norma limitare o disabilitare gli script del ciclo di vita (come `postinstall`, `preinstall`) nei processi di CI/CD, limitare gli accessi di rete in uscita dai sistemi di build ai domini fidati e usare token di automazione a breve scadenza e con permessi limitati.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi supply chain](https://www.securityinfo.it/tag/attacchi-supply-chain/), [librerie software](https://www.securityinfo.it/tag/librerie-software/), [npm](https://www.securityinfo.it/tag/npm/), [pacchetti software](https://www.securityinfo.it/tag/pacchetti-software/), [Shalai Ulud](https://www.securityinfo.it/tag/shalai-ulud/), [Worm](https://www.securityinfo.it/tag/worm/)

[DeepSeek R1 produce codice vulnerabile con prompt "politicamente sensibili"](https://www.security...