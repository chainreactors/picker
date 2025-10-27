---
title: Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio
url: https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-22
fetch_date: 2025-10-07T00:49:38.582998
---

# Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio

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

## Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio

Ago 21, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/#respond)

---

Un gruppo di cyber spionaggio legato ai servizi segreti russi sta sfruttando una falla di sicurezza risalente a sette anni fa nei software Cisco IOS e IOS XE. L’allarme arriva da Cisco Talos che ha osservato attività riconducibili a **Static Tundra**, un gruppo collegato all’FSB e operativo da oltre un decennio impegnato nella raccolta di intelligence a lungo termine.

Secondo i ricercatori, il gruppo prende di mira settori sensibili **come telecomunicazioni, università e manifatturiero**, con attacchi documentati in Nord America, Europa, Asia e Africa. Negli ultimi anni le attività si sono concentrate soprattutto contro l’Ucraina e i suoi alleati, in parallelo al conflitto avviato nel 2022.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/StaticTundra_21-ago-2025CG-1024x683.png)

## Una vulnerabilità critica mai scomparsa

Il punto d’ingresso sfruttato dagli attaccanti è la **CVE-2018-0171**, una vulnerabilità critica (CVSS 9.8) nel protocollo Smart Install che può consentire a un aggressore remoto e non autenticato di provocare denial of service o eseguire codice arbitrario. Nonostante la patch sia disponibile dal 2018, molti dispositivi vulnerabili restano esposti, in particolare quelli obsoleti o non più supportati.

Lo stesso difetto era stato **già sfruttato in passato** da altri gruppi di hacker di stato: tra questi il gruppo cinese Salt Typhoon, che nel 2024 lo aveva utilizzato contro provider statunitensi.

Il **Federal Bureau of Investigation (FBI)** conferma in una nota che le operazioni di Static Tundra hanno coinvolto migliaia di apparati di rete negli Stati Uniti e a livello globale. Gli attaccanti avrebbero sfruttato anche **SNMP** e altri protocolli deboli per raccogliere file di configurazione, manipolare le impostazioni dei dispositivi e creare accessi non autorizzati.

Una volta stabilita la testa di ponte, i criminali conducono attività di ricognizione interna e installano tool personalizzati come **SYNful Knock**, un impianto malevolo sui router che modifica il firmware per mantenere persistenza e può essere aggiornato nel tempo. In alcuni casi, hanno utilizzato SNMP per scaricare file da server esterni e modificarne la configurazione oppure alterato i parametri **TACACS+** per eludere i sistemi di logging.

Le operazioni mirano anche a intercettare traffico sensibile: gli attaccanti creano tunnel GRE per **dirottare pacchetti verso infrastrutture controllate dal gruppo**, oppure raccolgono dati NetFlow ed esfiltrano le informazioni tramite connessioni TFTP o FTP.

## Target, finalità strategiche e contromisure

Static Tundra si concentra soprattutto su **apparati non aggiornati o a fine vita**, sfruttandoli come trampolino per spingersi più a fondo nelle reti delle vittime. L’obiettivo è ottenere informazioni di valore strategico e garantire un accesso a lungo termine, adattando le proprie operazioni agli interessi geopolitici russi del momento.

Cisco sottolinea che lo scopo della campagna è la **raccolta massiva di configurazioni e dati di rete** che possono essere sfruttati in tempi successivi in base alle priorità governative di Mosca.

L’azienda ha aggiornato il bollettino relativo alla CVE-2018-0171, ribadendo che la falla è tuttora sfruttata attivamente. La raccomandazione è di **applicare senza ritardi le patch disponibili** o, laddove non sia possibile aggiornare, **disabilitare la funzione Smart Install**.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi rete](https://www.securityinfo.it/tag/attacchi-rete/), [Cisco IOS](https://www.securityinfo.it/tag/cisco-ios/), [Cisco IOS XE](https://www.securityinfo.it/tag/cisco-ios-xe/), [Cisco Talos](https://www.securityinfo.it/tag/cisco-talos/), [CVE-2018-0171](https://www.securityinfo.it/tag/cve-2018-0171/), [cyber spionaggio Russia](https://www.securityinfo.it/tag/cyber-spionaggio-russia/), [FBI advisory](https://www.securityinfo.it/tag/fbi-advisory/), [FSB](https://www.securityinfo.it/tag/fsb/), [router compromessi](https://www.securityinfo.it/tag/router-compromessi/), [sicurezza informatica](https://www.securityinfo.it/tag/sicurezza-informatica/), [Smart Install](https://www.securityinfo.it/tag/smart-install/), [spionaggio informatico](https://www.securityinfo.it/tag/spionaggio-informatico/), [Static Tundra](https://www.securityinfo.it/tag/static-tundra/), [SYNful Knock](https://www.securityinfo.it/tag/synful-knock/), [vulnerabilità Cisco](https://www.securityinfo.it/tag/vulnerabilita-cisco/)

[Prompt injection nelle immagini: l’image scaling trasforma un JPEG in un esfiltratore](https://www.securityinfo.it/2025/08/22/prompt-injection-nelle-immagini-limage-scaling-trasforma-un-jpeg-in-un-esfiltratore/)
[Lenovo, il chatbot AI “Lena” era troppo loquace](https://www.securityinfo.it/2025/08/20/lenovo-il-chatbot-ai-lena-era-troppo-loquace/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/wp-content/uploads/2025/10/Microsoft-Sentinel_3ott-2025CG-120x85.png)](https://www.securityinfo.it/...