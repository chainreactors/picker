---
title: Salt Typhoon: nove mesi nascosti nei sistemi della Guardia Nazionale USA
url: https://www.securityinfo.it/2025/07/18/salt-typhoon-nove-mesi-nascosti-nei-sistemi-della-guardia-nazionale-usa/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-19
fetch_date: 2025-10-06T23:53:19.846131
---

# Salt Typhoon: nove mesi nascosti nei sistemi della Guardia Nazionale USA

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

## Salt Typhoon: nove mesi nascosti nei sistemi della Guardia Nazionale USA

Lug 18, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/07/18/salt-typhoon-nove-mesi-nascosti-nei-sistemi-della-guardia-nazionale-usa/#respond)

---

Un gruppo APT legato al governo cinese **ha mantenuto accesso non rilevato per nove mesi all’interno della rete informatica della Guardia Nazionale di uno Stato americano**, sottraendo dati sensibili e credenziali di amministratori. A rivelarlo è un documento interno del Dipartimento della Sicurezza Nazionale (DHS), trapelato nei giorni scorsi e confermato da fonti ufficiali.

Secondo quanto riportato da NBC, l’attacco è stato condotto da **Salt Typhoon**, nome in codice attribuito a un gruppo APT sponsorizzato dallo Stato cinese, ritenuto affiliato al Ministero per la Sicurezza dello Stato (MSS) di Pechino. Il gruppo è salito alla ribalta negli ultimi anni per una serie di **attacchi mirati contro provider di telecomunicazioni e infrastrutture critiche negli Stati Uniti** e a livello globale. Tra gli obiettivi figurano AT&T, Verizon, Lumen, Windstream, Viasat e altri operatori del settore.

![](https://www.securityinfo.it/wp-content/uploads/2025/07/SchemaReteInterna18-lug-2025CG-1024x683.png)

**Una compromissione a lungo termine**

Secondo il memorandum riservato, **Salt Typhoon è rimasto attivo nella rete della Guardia Nazionale tra marzo e dicembre 2024**, esfiltrando **diagrammi di rete, file di configurazione, credenziali amministrative e dati personali** dei militari. Una delle implicazioni più gravi è che i dati trafugati contenevano informazioni sulle interconnessioni tra le Guardie Nazionali di diversi Stati e territori statunitensi. Queste informazioni potrebbero servire per facilitare **successive compromissioni a catena** all’interno dell’apparato di sicurezza nazionale.

Non si tratta di un caso isolato. Il DHS afferma che **Salt Typhoon ha già utilizzato in passato file di configurazione sottratti per infiltrarsi in altre agenzie governative** e infrastrutture critiche. Tra gennaio e marzo 2024, il gruppo avrebbe esfiltrato dati da almeno due enti statali, utilizzandoli successivamente per colpire dispositivi vulnerabili all’interno di altri segmenti governativi.

I file di configurazione rubati contengono dettagli cruciali per chiunque voglia compromettere una rete: indirizzi IP, profili di sicurezza, credenziali di accesso e configurazioni di firewall e VPN. Sono veri e propri blueprint digitali che permettono di navigare all’interno di reti teoricamente isolate o protette.

**Le vulnerabilità sfruttate e gli indicatori d’attacco**

Il documento del DHS non chiarisce il vettore iniziale dell’attacco, ma attribuisce a Salt Typhoon una predilezione per **vecchie vulnerabilità nei dispositivi di rete, in particolare nei router Cisco**. Tra le CVE citate nel report figurano:

* **CVE-2018-0171**: esecuzione di codice remoto via TCP in Cisco IOS/IOS XE Smart Install.
* **CVE-2023-20198 e CVE-2023-20273**: due falle sfruttabili in combinazione su IOS XE per ottenere accesso remoto non autenticato e privilegi root.
* **CVE-2024-3400**: vulnerabilità di command injection in PAN-OS GlobalProtect di Palo Alto Networks.

In attacchi precedenti, Salt Typhoon ha utilizzato malware sviluppati ad hoc come **JumblePath** e **GhostSpider**, con l’obiettivo di **monitorare i flussi di comunicazione di campagne politiche e parlamentari statunitensi**, sfruttando la compromissione di ambienti telecom non aggiornati.

**Allerta massima per le agenzie governative**

Il DHS raccomanda a tutte le agenzie federali e statali di verificare l’aggiornamento dei dispositivi di rete, **disabilitare i servizi non essenziali, segmentare il traffico SMB, implementare la firma SMB e rafforzare i controlli sugli accessi**.

Un portavoce della Guardia Nazionale ha confermato l’incidente ma ha precisato che non si sono verificate interruzioni nelle missioni federali o statali. Tuttavia, la portata dell’attacco e la possibilità che Salt Typhoon abbia creato dei punti d’accesso latenti in altre reti sollevano **preoccupazioni a lungo termine per la sicurezza nazionale**.

Interpellata da NBC, l’ambasciata cinese a Washington non ha negato l’attacco ma ha affermato che **le accuse mancano di prove conclusive e affidabili** che colleghino il gruppo al governo cinese.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT cinesi](https://www.securityinfo.it/tag/apt-cinesi/), [attacco hacker Guardia Nazionale](https://www.securityinfo.it/tag/attacco-hacker-guardia-nazionale/), [DHS cybersecurity](https://www.securityinfo.it/tag/dhs-cybersecurity/), [MSS Cina](https://www.securityinfo.it/tag/mss-cina/), [Salt Typhoon](https://www.securityinfo.it/tag/salt-typhoon/), [sicurezza reti USA](https://www.securityinfo.it/tag/sicurezza-reti-usa/), [vulnerabilità Cisco](https://www.securityinfo.it/tag/vulnerabilita-cisco/)

[LameHug, un nuovo malware che sfrutta un LLM per eseguire comandi](https://www.securityinfo.it/2025/07/18/lamehug-un-nuovo-malware-che-sfrutta-un-llm-per-eseguire-comandi/)
[Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![Static Tund...