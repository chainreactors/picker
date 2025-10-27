---
title: Il 12% dei siti di ecommerce espone backup privati
url: https://www.securityinfo.it/2023/02/10/il-12-dei-siti-di-ecommerce-espone-backup-privati/?utm_source=rss&utm_medium=rss&utm_campaign=il-12-dei-siti-di-ecommerce-espone-backup-privati
source: Over Security - Cybersecurity news aggregator
date: 2023-02-11
fetch_date: 2025-10-04T06:22:25.388981
---

# Il 12% dei siti di ecommerce espone backup privati

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

## Il 12% dei siti di ecommerce espone backup privati

Feb 10, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2023/02/10/il-12-dei-siti-di-ecommerce-espone-backup-privati/#respond)

---

[Sansec](https://sansec.io/) ha pubblicato una nuova analisi in cui ha mostrato come **un negozio online su nove esponga involontariamente backup** privati: un errore che potrebbe avere conseguenze molto gravi, perché i backup contengono password e altre informazioni sensibili.

Proprio attraverso questi file, i criminali informatici sono già riusciti in varie occasioni a **prendere il controllo dei siti, intercettare i pagamenti o semplicemente estorcere denaro** ai proprietari.

Sansec ha preso in esame oltre 2000 negozi online di varie dimensioni, e in 250 casi i ricercatori hanno trovato archivi (come file Zip, Sql e Tar) **nella cartella Web pubblica senza restrizioni di accesso**. Questi backup contengono password di database, Url privati per l’accesso a pagine di amministrazione, chiavi API e dati completi dei clienti.

## Una facile preda

La scoperta di backup pubblici non protetti può essere **molto semplice per un utente malintenzionato** abbastanza competente, che può impostate attacchi automatizzati per testare migliaia di possibili denominazioni e percorsi per i backup.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/s3.us-west-2.amazonaws.com_65b85a71-0b7e-4ea7-9881-8bda7c24f7a5.png)

Sansec ha trovato centinaia di siti che espongono file di backup (Fonte: Sansec)

Questi attacchi possono **continuare indefinitamente fino a quando non viene trovato un risultato** valido; se un utente malintenzionato riuscisse a scaricare un backup privato, potrebbe essere in grado di ottenere informazioni molto preziose sensibili, come password di database, Url di amministratore segreto e dati dei clienti.

La ricerca di Sansec ha **rilevato diversi pattern di attacco già in azione**, provenienti da molti Ip di origine; questo suggerisce che vulnerabilità di questo genere siano ben note alla criminalità informatica e qualcuno le stia già sfruttando.

Proprio per questo è fondamentale che le organizzazioni adottino **misure per proteggere i propri backup** e prevenire eventuali perdite di dati o accessi non autorizzati.

È quindi essenziale verificare se le impostazioni del proprio store prevedono che i backup siano salvati all’interno di cartelle accessibili via Web. Per tutti i file eventualmente trovati, bisogna poi **verificare se i permessi assegnati loro li rendono effettivamente scaricabili** tramite una richiesta via browser.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/s3.us-west-2.amazonaws.com_b6a32c2d-dc58-4b3b-8191-b27b4792667a.png)

Un attacco brute force cerca di individuare backup accessibili da remoto (Fonte: Sansec)

## Correre ai ripari

Se i backup sono esposti da tempo, bisogna inoltre **analizzare la configurazione del sito alla ricerca di eventuali segni di compromissione**: Sansec suggerisce di controllare i file di registro del server Web per verificare se il backup è stato scaricato, controllare se sono stati aggiunti eventuali account amministratore.

Bisogna poi **modificare tutte le password**, in particolare quelle degli account amministratore, gli accessi Ssh/Ftp e le password del database, e attivare se disponibile l’autenticazione a due fattori per tutti gli utenti.

È anche importante verificare che **il sito non esponga nessun pannello di amministrazione** remoto, come phpMyAdmin o Adminer. Sansec suggerisce anche di utilizzare il suo scanner di sicurezza backend [eComscan](https://sansec.io), sviluppato proprio per accelerare questo tipo di indagini.

Per evitare problemi analoghi in futuro, Sansec suggerisce l’utilizzo di un **file system in sola lettura** che non consenta la creazione di file ad hoc; questa tecnologia è presente nella piattaforma Adobe Commerce, ma se si usa un altro provider potrebbe invece non essere disponibile.

È comunque consigliabile utilizzare altre soluzioni di backup, che non prevedano la creazione di file accessibile da remoto; inoltre, si può **configurare il server Web per limitare l’accesso** ad alcune tipologie di file, come per esempio Zip, Gz, Tgz, Tar E Sql.

Restrizioni di accesso possono essere **aggiunte al file htaccess** (per il server Apache) o **alla configurazione** **principale di Nginx**.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backup](https://www.securityinfo.it/tag/backup/), [configurazione](https://www.securityinfo.it/tag/configurazione/), [ecommerce](https://www.securityinfo.it/tag/ecommerce/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Web Server](https://www.securityinfo.it/tag/web-server/)

[Backup immutabili e “sigillati” per contrastare il malware](https://www.securityinfo.it/2023/02/13/backup-immutabili-e-sigillati-per-contrastare-il-malware/)
[ESET Threat Report T3 2022: l'impatto della guerra in Ucraina](https://www.securityinfo.it/2023/02/10/eset-threat-report-t3-2022-limpatto-della-guerra-in-ucraina/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated...