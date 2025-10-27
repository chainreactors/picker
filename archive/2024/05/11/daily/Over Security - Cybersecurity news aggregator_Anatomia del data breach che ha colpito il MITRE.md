---
title: Anatomia del data breach che ha colpito il MITRE
url: https://www.securityinfo.it/2024/05/10/anatomia-del-data-breach-che-ha-colpito-il-mitre/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-11
fetch_date: 2025-10-06T17:18:47.198849
---

# Anatomia del data breach che ha colpito il MITRE

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

## Anatomia del data breach che ha colpito il MITRE

Mag 10, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2024/05/10/anatomia-del-data-breach-che-ha-colpito-il-mitre/#respond)

---

A partire dallo scorso gennaio e fino a metà marzo, **MITRE è stata vittima di un attacco** che ha sfruttato due **vulnerabilità zero-day di Ivanti Connect Secure** e ha permesso agli attaccanti di accedere al **NERVE**, una rete di ricerca e sviluppo dell’organizzazione, ed esfiltrare informazioni.

L’organizzazione [aveva reso noto l’attacco a fine aprile](https://www.securityinfo.it/2024/04/22/mitre-colpita-da-un-breach-a-opera-di-gruppo-nation-state/), spiegando di essere **riuscita a segmentare la rete** per evitare che gli attaccanti riuscissero a muoversi ulteriormente all’interno del network. Il gruppo, sfruttando il session hijacking e una **serie di backdoor e web shell sofisticate**, è riuscito a mantenere la persistenza e ottenere le credenziali di diversi account.

In un recente articolo MITRE [ha dettagliato](https://medium.com/mitre-engenuity/technical-deep-dive-understanding-the-anatomy-of-a-cyber-intrusion-080bddc679f3) le attività malevole spiegando che la prima intrusione, avvenuta il 31 dicembre 2023, è iniziata con **ROOTROT**, una web shell che ha sfruttato le vulnerabilità Ivanti per accedere al NERVE senza autorizzazione, eludendo l’autenticazione multi-fattore.

In seguito, dopo aver profilato l’ambiente NERVE, gli attaccanti sono riusciti a **loggarsi a diversi account tramite RDP**, sfruttando le credenziali per accedere ai preferiti e ai file condivisi dagli utenti. “Questa attività di scoperta, culminata con l’esfiltrazione di documenti, **mirava a mappare la topologia della rete e a identificare obiettivi di alto valore per un futuro sfruttamento**” ha affermato **Lex Crumpton**, principal cybersecurity engineer dell’organizzazione.

![](https://www.securityinfo.it/wp-content/uploads/2024/01/matrix-1799651_1920-1.jpg)

Pixabay

Il gruppo ha poi manipolato le macchine virtuali e stabilito il controllo sull’infrastruttura sfruttando credenziali di amministratore compromesso. Dopo l’accesso alle macchine virtuali, gli attaccanti hanno eseguito una serie di payload come la backdoor **BRICKSTORM** e una web shell chiamata **BEEFLUSH**: l’obiettivo era **ottenere accesso persistente alla rete** e riuscire ad eseguire comandi per raccogliere informazioni e comunicare col server C2.

Nel corso dell’analisi i ricercatori di sicurezza del MITRE hanno individuato anche **WIREFIRE** e **BUSHWALK**, altre due web shell che servivano a nascondere le comunicazioni e facilitare quindi il furto di dati.

Da febbraio e fino a metà marzo il gruppo è riuscito a mantenere la persistenza sui sistemi e ha cercato di muoversi al di fuori della rete NERVE per ottenere nuove risorse, ma senza successo.

L’organizzazione è riuscita a eliminare ogni traccia del gruppo, ma ha sottolineato l’**importanza di rafforzare la propria sicurezza per scongiurare attacchi futuri.** “Sebbene i nostri sforzi iniziali di risposta abbiano contribuito a mitigare l’impatto immediato dell’attacco informatico, riconosciamo la **necessità di una continua vigilanza e adattamento**” ha affermato Crumpton.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [data breach](https://www.securityinfo.it/tag/data-breach/), [mitre](https://www.securityinfo.it/tag/mitre/), [movimento laterale](https://www.securityinfo.it/tag/movimento-laterale/), [NERVE](https://www.securityinfo.it/tag/nerve/), [Web Shell](https://www.securityinfo.it/tag/web-shell/)

[Microsoft annuncia il Zero Trust DNS per garantire connessioni più sicure](https://www.securityinfo.it/2024/05/10/microsoft-annuncia-il-zero-trust-dns/)
[Scoperta una campagna che sfrutta un bug di LiteSpeed Cache di Wordpress](https://www.securityinfo.it/2024/05/09/scoperta-una-campagna-che-sfrutta-un-bug-di-litespeed-cache-di-wordpress/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali](https://www.securityinfo.it/wp-content/uploads/2025/09/cyber-security-3411499_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/ "SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali")

  [SonicWall vittima di un breach, la...](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-d...