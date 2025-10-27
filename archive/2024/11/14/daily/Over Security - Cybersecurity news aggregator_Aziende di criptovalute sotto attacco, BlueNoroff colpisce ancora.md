---
title: Aziende di criptovalute sotto attacco, BlueNoroff colpisce ancora
url: https://www.securityinfo.it/2024/11/12/aziende-di-criptovalute-sotto-attacco-bluenoroff-colpisce-ancora/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-14
fetch_date: 2025-10-06T19:28:59.810620
---

# Aziende di criptovalute sotto attacco, BlueNoroff colpisce ancora

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

## Aziende di criptovalute sotto attacco, BlueNoroff colpisce ancora

Nov 12, 2024  [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/ "Articoli scritti da Valentina Caruso")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/11/12/aziende-di-criptovalute-sotto-attacco-bluenoroff-colpisce-ancora/#respond)

---

Le aziende di criptovalute sono prese di mira da una campagna malware in grado di infettare i dispositivi macOS. Gli autori di questa minaccia sembrano essere legati alla Repubblica Popolare Democratica di Corea (DPRK). Secondo gli specialisti in cybersicurezza di [SentinelOne](https://it.sentinelone.com/), infatti, si tratterebbe di **BlueNoroff. Un gruppo nordcoreano specializzato in phishing** che prima del 2020 ha portato a termine un furto del valore di 3 miliardi di dollari in fondi. Negli anni, BlueNoroff è stato collegato alla **diffusione di alcune famiglie di malware tra cui figurano TodoSwift, RustDoor e ObjCShellz**.

## La campagna Hidden Risk

L’attuale campagna sembra essere **iniziata a luglio 2024** ed è stata soprannominata Hidden Risk. Il malware si nasconde in un’applicazione dannosa che si spaccia per un file pdf e **opera sfruttando attacchi multi-fase**.

Tutto parte da una mail che ha come oggetto proprio le criptovalute e adesca le sue vittime grazie a titoli sensazionalistici. L’esca, spesso, è rappresentata da false **opportunità di investimento o di lavoro nel mondo crypto**.

![aziende di criptovalute minacciate](https://www.securityinfo.it/wp-content/uploads/2024/11/aziende-di-criptovalute.jpeg)

## Alta ingegneria sociale

L’FBI ha sottolineato, in una comunicazione che risale allo scorso settembre, come questi attacchi siano **difficili da rilevare e ben congegnati**. Si rivolgono a dipendenti che lavorano nel settore delle criptovalute e della finanza o ad appassionati del tema. E sono altamente personalizzati.

Tra gli aspetti più pericolosi c’è quello del **coinvolgimento di lunga durata**: i cybercriminali inviano mail non sospette per lungo tempo, **conquistando la fiducia dei malcapitati**, e solo alla fine distribuiscono il malware.

## Le osservazioni di SentinelOne

In particolare, il singolo attacco Hidden Risk osservato analizzato da SentinelOne risale alla fine di ottobre 2024. **L’applicazione malevola ha scaricato un file PDF esca recuperato da Google Drive** ma allo stesso tempo ha anche recuperato un file eseguibile da un server remoto, **aprendo una backdoor**.

L’applicazione era scritta nel linguaggio di programmazione Swift, **firmata e autenticata da una ID sviluppatore Apple**. Tra le attività criminali di BlueNoroff c’è, infatti, anche quella del **dirottamento di account sviluppatori validi.** Vengono usati per diffondere in modo più efficace il malware.

La backdoor si distingue poi per la presenza di **un nuovo meccanismo di persistenza** pensato per sopravvivere ai reboot. Il meccanismo sfrutta **il file di configurazione zshenv**. Gli APT (Advanced Persistent Threat) riescono a mantenere l’accesso non autorizzato ai sistemi, senza essere rintracciati, anche per lungo tempo, continuando a spiare le vittime e rubare dati.

## La notifica di Apple non si attiva

Il meccanismo degli attacchi Hidden Risk alle aziende di criptovalute è in parte simile a quello che era stato usato da questo o da altri gruppi hacker per distribuire TodoSwift. Il sistema è particolarmente astuto perché **Apple ha introdotto, a partire macOS Ventura, delle notifiche di minaccia**. Gli utenti, cioè, vengono avvisati quando vengono installati nel sistema metodi persistenti e applicazioni sospette. L’abuso di zshenv però non allerta il sistema macOS e non comporta nessuna notifica.

![allerta security](https://www.securityinfo.it/wp-content/uploads/2024/11/allerta-security.jpg)

## Meno sofisticato ma comunque efficace

Negli ultimi 12 mesi, **i criminali informatici nordcoreani stanno sferrando attacchi contro una serie di aziende legate al mondo delle criptovalute** sfruttando approcci anche molto complessi che hanno previsto, ad esempio, di **avvicinarsi gradualmente alle vittime** usando i social network.

Hidden Risk da questo punto di vista **è una campagna meno sofisticata perché sfrutta in modo più tradizionale una serie di email**. Non per questo, però, si dimostra meno efficace.

Il furto di codici privati e informazioni relative ai portafogli digitali è una minaccia molto seria che coinvolge non solo le singole aziende del settore ma potenzialmente l’intero ecosistema delle criptovalute.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

[Report APT ESET: i gruppi filo-cinesi e iraniani intensificano le attività](https://www.securityinfo.it/2024/11/12/report-apt-eset-i-gruppi-filo-cinesi-e-iraniani-intensificano-le-attivita/)
[Proattivà nelle patch e visione unificata della sicurezza: l'approccio migliore per la sicurezza OT](https://www.securityinfo.it/2024/11/11/proattiva-nelle-patch-e-visione-unificata-della-sicurezza-lapproccio-migliore-per-la-sicurezza-ot/)

---

![](https://secure.gravatar.com/avatar/0a083e115b9328218407201798ab82c0?s=90&d=mm&r=g)

##### [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/)

##### Articoli correlati

* [![Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/wp-content/uploads/2019/01/Morten-Lehn-120x85.jpg)](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  [Transparency Center Initiative di...](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-l...