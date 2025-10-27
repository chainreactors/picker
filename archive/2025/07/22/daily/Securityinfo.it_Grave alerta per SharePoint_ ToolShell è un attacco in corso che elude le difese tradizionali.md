---
title: Grave alerta per SharePoint: ToolShell è un attacco in corso che elude le difese tradizionali
url: https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/?utm_source=rss&utm_medium=rss&utm_campaign=grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali
source: Securityinfo.it
date: 2025-07-22
fetch_date: 2025-10-06T23:54:08.876661
---

# Grave alerta per SharePoint: ToolShell è un attacco in corso che elude le difese tradizionali

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

## Grave alerta SharePoint: attacco in corso che elude le difese

Lug 21, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/#respond)

---

Una campagna di attacchi mirati sta sfruttando una vulnerabilità critica in Microsoft SharePoint Server per compromettere infrastrutture aziendali e istituzionali. Il bug, tracciato come **CVE-2025-53770**, consente l’esecuzione di codice remoto da parte di attaccanti non autenticati e rappresenta una grave minaccia per migliaia di ambienti esposti su Internet. A rendere ancora più grave la situazione è la conferma, da parte di Microsoft e di varie società di threat intelligence, che la vulnerabilità è attivamente sfruttata da almeno un gruppo ben organizzato e con capacità avanzate.

![](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-1024x683.png)

Secondo quanto emerso, l’exploit sfrutta una combinazione di richieste malevole inviate a una **specifica pagina di SharePoint** (`ToolPane.aspx`), manipolando i parametri HTTP per bypassare i meccanismi di controllo. La catena di attacco consente di caricare una web shell ASPX attraverso PowerShell, che viene poi **utilizzata per sottrarre le chiavi di crittografia ASP.NET**. In particolare, il furto delle chiavi MachineKey permette agli attaccanti di mantenere un accesso persistente al sistema anche dopo l’applicazione di patch, configurando **uno scenario di compromissione permanente** se non si interviene con misure di bonifica avanzate.

Le infezioni rilevate finora, secondo i dati raccolti da Eye Security e Unit 42 di Palo Alto Networks, **hanno coinvolto diverse decine di organizzazioni**, tra cui enti pubblici federali e statali statunitensi, ospedali, università e aziende dei settori telecomunicazioni, energia e finanza. Tuttavia, secondo una stima prudente, potrebbero essere oltre 8.000 le istanze di SharePoint vulnerabili ancora esposte, molte delle quali configurate per l’accesso pubblico via Internet. Le analisi forensi mostrano che **l’attività malevola è iniziata intorno al 18 luglio 2025**, e che l’exploit utilizzato è identico in tutti i casi, a conferma della matrice unitaria dell’attacco.

A differenza di SharePoint Online che non è affetto dalla vulnerabilità, le versioni on-premise risultano direttamente esposte. Microsoft ha rilasciato patch correttive per SharePoint 2019 e per la Subscription Edition, mentre un aggiornamento per SharePoint 2016 è atteso a breve. Tuttavia, la stessa Microsoft ha avvertito che la sola applicazione delle patch non è sufficiente a eliminare il rischio, se il sistema è già stato compromesso. Gli amministratori dovranno infatti anche procedere alla **rotazione delle chiavi MachineKey**, riavviare i servizi IIS e condurre un’analisi approfondita per individuare eventuali web shell o strumenti di accesso remoto occultati nei sistemi.

La gravità della situazione ha spinto anche la Cybersecurity and Infrastructure Security Agency (CISA) a inserire il CVE-2025-53770 nel proprio catalogo delle vulnerabilità attivamente sfruttate, invitando tutte le organizzazioni pubbliche e private a **disconnettere temporaneamente i server esposti a Internet**, in attesa dell’adozione di tutte le misure correttive. Tra le azioni consigliate figurano anche l’attivazione del modulo AMSI (Antimalware Scan Interface), l’abilitazione di Microsoft Defender Antivirus e l’impiego di soluzioni EDR per individuare attività anomale e persistenti.

Unit 42 ha inoltre lanciato un’allerta a tutti gli amministratori di sistema, sottolineando che **ogni server SharePoint esposto al pubblico dovrebbe essere considerato potenzialmente compromesso**, e che l’unico modo per scongiurare accessi non autorizzati è eseguire una bonifica completa del sistema, compresa l’analisi del traffico passato, la verifica dei log e il controllo dei file di sistema alla ricerca di codice iniettato.

Si consiglia di tenere alta l’attenzione al rilascio di patch in questi giorni per esser sicuri di aggiornare tempestivamente i sistemi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco zero-day](https://www.securityinfo.it/tag/attacco-zero-day/), [CVE-2025-53770](https://www.securityinfo.it/tag/cve-2025-53770/), [esecuzione remota codice](https://www.securityinfo.it/tag/esecuzione-remota-codice/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [patch SharePoint](https://www.securityinfo.it/tag/patch-sharepoint/), [persistente](https://www.securityinfo.it/tag/persistente/), [SharePoint vulnerability](https://www.securityinfo.it/tag/sharepoint-vulnerability/), [Threat Hunting](https://www.securityinfo.it/tag/threat-hunting/), [ToolShell](https://www.securityinfo.it/tag/toolshell/), [webshell](https://www.securityinfo.it/tag/webshell/)

[PoisonSeed è riuscito ad aggirare la protezione FIDO](https://www.securityinfo.it/2025/07/21/poisonseed-e-riuscito-ad-aggirare-la-protezione-fido/)
[CERT-AGID 12 – 18 luglio: i finti QR code di PagoPA](https://www.securityinfo.it/2025/07/21/cert-agid-12-18-luglio-i-finti-qr-code-di-pagopa/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli...