---
title: Qual è la causa dei disservizi di venerdì scorso? Ce la spiega CrowdStrike
url: https://www.securityinfo.it/2024/07/24/qual-e-la-causa-dei-disservizi-di-venerdi-scorso-ce-la-spiega-crowdstrike/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-25
fetch_date: 2025-10-06T17:45:16.551074
---

# Qual è la causa dei disservizi di venerdì scorso? Ce la spiega CrowdStrike

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

## Qual è la causa dei disservizi di venerdì scorso? Ce la rivela CrowdStrike

Lug 24, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Prodotto](https://www.securityinfo.it/category/approfondimenti/prodotto/), [RSS](https://www.securityinfo.it/category/rss/), [Software](https://www.securityinfo.it/category/approfondimenti/software/)
 [0](https://www.securityinfo.it/2024/07/24/qual-e-la-causa-dei-disservizi-di-venerdi-scorso-ce-la-spiega-crowdstrike/#respond)

---

Il 19 luglio 2024 è una data che rimarrà impressa per molto tempo nella nostra memoria: a partire dalle prime ore della mattinata, **milioni di dispositivi Windows hanno smesso di funzionare a causa di un [aggiornamento fallato](https://www.securityinfo.it/2024/07/19/un-aggiornamento-di-crowdstrike-ha-bloccato-i-sistemi-windows-di-tutto-il-mondo/) della piattaforma Falcon di CrowdStrike.**

Aeroporti, stazioni, emittenti radiofoniche e televisive ma anche servizi di emergenza si sono trovati all’improvviso con schermate blu di errore e dispositivi che non riuscivano più ad avviarsi correttamente. **Le macchine sono rimaste in un loop di boot provocando interruzioni di servizio per ore e ore**, tanto che numerose compagnie aeree hanno dovuto sospendere i voli in programma fino alla risoluzione del problema.

![CrowdStrike](https://www.securityinfo.it/wp-content/uploads/2024/07/cogwheels-284526_1920.jpg)

Pixabay

Oggi CrowdStrike ha rilasciato un **[report](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/)** in cui spiega cosa è accaduto e illustra agli utenti come risolvere la problematica nel caso in cui non l’avessero ancora fatto.

“*Venerdì 19 luglio alle 04:09 UTC (le 06:09 ora italiana*, n.d.r.*), come parte di regolari attività, CrowdStrike ha rilasciato un aggiornamento di configurazione per i sensori Windows per ottenere telemetria su potenziali nuove tecniche di attacco*” si legge nel report. “*Questi aggiornamenti sono parte dei meccanismi di protezione dinamica della piattaforma Falcon. **La nuova configurazione problematica di Rapid Response Content ha causato il crash dei sistemi Windows***“.

## Tutta colpa di un aggiornamento fallato

I dispositivi “vittime” dell’aggiornamento sono quelli che eseguono **versioni del sensore dalla 7.11 in su** che erano online tra le 06:09 (ora italiana) e le 07:27 di venerdì e che hanno ricevuto l’aggiornamento. L’update fallato è stato ripristinato alle 07:27 e tutti i dispositivi che hanno scaricato l’update dopo quell’orario non sono stati impattati dal problema.

Il problema era nel **Channel File 291**, un tipo di file che viene usato per aggiornare le configurazioni di Falcon che sfruttano la behavioral analysis per individuare e fermare le minacce. Nel dettaglio, il file conteneva un aggiornamento che migliorava il modo in cui Falcon valuta l’esecuzione delle “named pipe”, ovvero un comune meccanismo di comunicazione tra processi.

Nel file però era presente un errore di logica che non è stato individuato durante la validazione dell’update, e **il bug quindi è stato distribuito inavvertitamente a tutte le macchine online** nel lasso di tempo indicato da CrowdStrike.

Il contenuto del Channel File 291, una volta ricevuto dal sensor e caricato nel Content Interpreter, ha provocato una **out-of-bound memory read** che a sua volta ha causato un’eccezione non gestita; poiché Falcon è integrato col kernel Windows, l’eccezione ha portato poi al crash del sistema.

![](https://www.securityinfo.it/wp-content/uploads/2024/07/background-5035258_1920-1.jpg)

Pixabay

## CrowdStrike rassicura gli utenti

Il disservizio diffuso di venerdì scorso è stato indubbiamente uno dei più grandi ai quali abbiamo assistito finora, se non il più grande. L’aggiornamento ha creato molti problemi ad aziende di diversi settori e c’è voluto molto tempo per ritornare alla completa operatività.

“***Assicuriamo ai nostri clienti che CrowdStrike sta operando normalmente e che questo problema non riguarda i sistemi della piattaforma Falcon**. Se i vostri sistemi funzionano normalmente, non c’è alcun impatto sulla loro protezione se il sensore Falcon è installato. I servizi Falcon Complete e OverWatch non sono stati interrotti da questo incidente*” ha chiarito la compagnia.

Anche **George Kurtz**, fondatore e CEO di CrowdStrike, ha detto la sua in merito: “***Voglio scusarmi sinceramente con tutti voi per l’interruzione del servizio. Tutta CrowdStrike comprende la gravità e l’impatto della situazione.** Abbiamo rapidamente identificato il problema e implementato una soluzione, permettendoci di concentrarci diligentemente sul ripristino dei sistemi dei clienti come nostra massima priorità*” ha spiegato.

La compagnia ha promesso di **migliorare i test per la validazione degli aggiornamenti** e di **fornire ai propri clienti più controllo sugli update**, permettendogli di decidere quando installarli; fino a ora venivano installati automaticamente.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [aggiornamento](https://www.securityinfo.it/tag/aggiornamento/), [bug](https://www.securityinfo.it/tag/bug/), [CrowdStrike](https://www.securityinfo.it/tag/crowdstrike/), [disservizi](https://www.securityinfo.it/tag/disservizi/)

[Daggerfly sta usando una nuova versione di Macma, una backdoor per macOS](https://www.securityinfo.it/2024/07/25/daggerfly-sta-usando-una-nuova-versione-di-macma-una-backdoor-per-macos/)
[Cloud computing: per il Consorzio Italia Cloud bisogna ridurre la dipendenza da fornitori esteri](https://www.securityinfo.it/2024/07/24/cloud-computing-per-il-consorzio-italia-cloud-bisogna-ridurre-la-dipendenza-da-fornitori-esteri/)

---

![](https://secure.gravatar.com/av...