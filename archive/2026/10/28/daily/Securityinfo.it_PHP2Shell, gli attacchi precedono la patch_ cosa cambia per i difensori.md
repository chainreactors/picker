---
title: PHP2Shell, gli attacchi precedono la patch: cosa cambia per i difensori
url: https://www.securityinfo.it/2026/10/28/php2shell-gli-attacchi-precedono-la-patch-cosa-cambia-per-i-difensori/?utm_source=rss&utm_medium=rss&utm_campaign=php2shell-gli-attacchi-precedono-la-patch-cosa-cambia-per-i-difensori
source: Securityinfo.it
date: 2026-10-28
fetch_date: 2026-10-29T07:52:31.700603
---

# PHP2Shell, gli attacchi precedono la patch: cosa cambia per i difensori

Aggiornamenti recenti Ottobre 28th, 2026 11:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [PHP2Shell, gli attacchi precedono la patch: cosa cambia per i difensori](https://www.securityinfo.it/2026/10/28/php2shell-gli-attacchi-precedono-la-patch-cosa-cambia-per-i-difensori/)
* [PHP2Shell,milioni di siti Web a rischio e la disclosure diventa un caso](https://www.securityinfo.it/2026/10/23/php2shellrischio-milioni-di-siti-web-a-rischio-e-la-disclosure-diventa-un-caso/)
* [Midnight Mimosa, ancora malware Android installato prima dell’acquisto](https://www.securityinfo.it/2026/10/09/midnight-mimosa-ancora-malware-android-installato-prima-dellacquisto/)
* [Bitdefender crea una VPN per gli agenti AI](https://www.securityinfo.it/2026/09/21/bitdefender-crea-una-vpn-per-gli-agenti-ai/)
* [No Hat 2026, a Bergamo l’hacking incontra AI, cyber-spionaggio e droni](https://www.securityinfo.it/2026/09/11/no-hat-2026-a-bergamo-lhacking-incontra-ai-cyber-spionaggio-e-droni/)

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

## PHP2Shell, gli attacchi precedono la patch: cosa cambia per i difensori

Ott 28, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/10/28/php2shell-gli-attacchi-precedono-la-patch-cosa-cambia-per-i-difensori/#respond)

---

**Il caso analizzato da Sekoia mostra perché aggiornare i sistemi deve accompagnarsi alla ricerca di compromissioni precedenti. Tra dipendenze nascoste e ricerca delle vulnerabilità accelerata dall’AI, i team di sicurezza devono prepararsi a intervenire anche prima che esista una correzione.**

Il rilascio burrascoso delle informazioni sulle vulnerabilità PHP2Shell ha concentrato l’attenzione di tutti sulla delicatezza della fase che precede un annuncio importante, ma **non bisogna trascurare le buone pratiche anche dopo che la patch è stata rilasciata**. Un’[analisi di David Greenwood per Sekoia](https://www.sekoia.com/blog/php2shell-was-exploited-before-the-patch-expect-more-of-it) mostra che il primo tentativo di sfruttamento di PHP2Shell rilevato da Amazon risale al 17 ottobre, quattro giorni prima del rilascio delle patch e questo ci ricorda che la verifica delle attività sospette deve coprire anche il periodo precedente.

Ricordiamo che **PHP2Shell comprende due vulnerabilità del motore PHP, CVE-2026-109618 e CVE-2026-109619**, che possono consentire l’esecuzione di codice da remoto senza autenticazione. La prima riguarda la gestione dell’esaurimento della memoria, la seconda uno stato interno che può sopravvivere alla liberazione della memoria cui fa riferimento. In determinate configurazioni l’attacco può avvenire prima dell’esecuzione del codice applicativo. **Le correzioni sono state pubblicate il 21 ottobre** nelle versioni PHP 8.5.12, 8.4.27, 8.3.36 e 8.2.35.

![](https://www.securityinfo.it/wp-content/uploads/2026/10/Tracce-dattacco-prima-della-patch-1-1024x576.png)

**Gli attacchi rilevati hanno colpito degli honeypot**

Nel suo report, Amazon ha documentato tentativi contro i propri honeypot precisando che non era chiaro se quei payload avrebbero avuto successo su sistemi reali, ma non è questo il punto.  Secondo Sekoia, **lo sfruttamento prima della divulgazione è destinato a diventare sempre più frequente per il software esposto su Internet**. Apparati perimetrali, piattaforme di trasferimento file e runtime web offrono agli attaccanti un incentivo evidente: **una sola falla può aprire l’accesso a un numero elevato di installazioni**. La disponibilità della patch, quindi, non può più essere considerata il punto di partenza dell’esposizione al rischio.

Un secondo problema riguarda le dipendenze. La prossima emergenza, che in realtà sarebbe la riproposizione di qualcosa di già visto in passato, potrebbe nascere **in una libreria incorporata in prodotti che l’organizzazione non sa nemmeno di usare** indirettamente. Sapere quali applicazioni sono installate diventa insufficiente se manca il collegamento con i componenti che includono. Inoltre, aggiornamenti distribuiti senza un avviso di sicurezza possono rendere meno immediata l’identificazione del rischio attraverso gli scanner.

**L’intelligenza artificiale può amplificare questa dinamica.**

Nell’interpretazione di Sekoia, la pubblicazione di una classe di vulnerabilità offre ai ricercatori e agli attaccanti un modello da cercare in altro codice. **Una scoperta importante potrebbe così generare una famiglia di problemi correlati**, distribuiti fra prodotti e runtime differenti. Anche il vantaggio oggi disponibile ai team con accesso ai modelli più avanzati potrebbe ridursi con il miglioramento dei modelli aperti. A questo si aggiunge la fragilità degli embarghi: una dimostrazione pubblicata in anticipo o una correzione distribuita prima del previsto possono anticipare la circolazione delle informazioni.

**Cosa devono fare i difensori?**

Per i difensori, la prima conseguenza pratica è **affiancare alla correzione un’indagine retrospettiva**. Nel caso di PHP2Shell, la ricerca deve partire almeno dal 17 ottobre, anziché limitarsi ai giorni successivi alla pubblicazione delle patch. Applicarla elimina la vulnerabilità, ma non rimuove eventuali accessi o meccanismi di persistenza già introdotti.

**La seconda priorità è migliorare l’inventario**, collegando applicazioni, runtime e librerie incorporate. Sul piano operativo, questo significa poter rispondere rapidamente a una domanda concreta: quali servizi dipendono dal componente appena segnalato, chi li gestisce e quali sono raggiungibili dall’esterno?

Sekoia, inollre, raccomanda di proteggere le interfacce di amministrazione con controlli di accesso e di rimuovere dalla rete pubblica i servizi che non devono essere raggiungibili. In pratica, sottolinea l’importanza di regole che dovrebbero essere già la norma nella maggior parte delle aziende, ma spesso si perdono di vista.

Occorre poi **decidere in anticipo come agire quando la patch non esiste**. Disabilitare un modulo, applicare una regola al web application firewall o sospendere un servizio sono opzioni da valutare prima dell’emergenza, individuando anche chi può autorizzarle fuori dall’orario di lavoro. Per PHP2Shell, le mitigazioni di configurazione non sostituiscono l’aggiornamento completo.

Infine, **la rilevazione deve seguire ciò che accade dopo lo sfruttamento**: un processo web che avvia una shell, file inattesi nella directory del sito o connessioni i...