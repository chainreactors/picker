---
title: Vulnerabilità nei prodotti Zyxel, ProjectSend e CyberPanel
url: https://www.securityinfo.it/2024/12/09/vulnerabilita-nei-prodotti-di-zyxel-projectsend-e-cyberpanel/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-10
fetch_date: 2025-10-06T19:41:55.481907
---

# Vulnerabilità nei prodotti Zyxel, ProjectSend e CyberPanel

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

## Vulnerabilità nei prodotti Zyxel, ProjectSend e CyberPanel

Dic 09, 2024  [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/ "Articoli scritti da Valentina Caruso")
 [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/12/09/vulnerabilita-nei-prodotti-di-zyxel-projectsend-e-cyberpanel/#respond)

---

La Cybersecurity and Infrastructure Security Agency (CISA) degli Stati Uniti ha recentemente aggiunto al proprio catalogo delle **Known Exploited Vulnerabilities (KEV)** una serie di vulnerabilità nei prodotti di aziende come Zyxel, North Grid Proself, ProjectSend e CyberPanel. Una decisione che arriva in seguito a **segnalazioni di sfruttamento attivo di queste falle** per scopi malevoli.

## Le vulnerabilità sotto i riflettori

Tra le criticità segnalate figura una vulnerabilità classificata come **CVE-2024-51378**, che **ha ottenuto un punteggio CVSS di 10.0**, il massimo della gravità. Il calcolo del punteggio base del CVSS (Common Vulnerability Scoring System) si basa su tre categorie: Exploitability, Impact e Scope.

![vulnerabilità nei prodotti](https://www.securityinfo.it/wp-content/uploads/2024/12/vulnerabilita-nei-prodotti.jpg)

La falla CVE-2024-51378 è **legata a permessi predefiniti errati.** Consentono di **bypassare l’autenticazione ed eseguire comandi arbitrari**, sfruttando metacaratteri della shell. Un’altra vulnerabilità, **CVE-2024-11680**, presenta invece un problema di autenticazione insufficiente, permettendo agli hacker di **creare da remoto nuovi account o incorporare script dannosi**. Anche CVE-2024-11667 va monitorata. Questo perché dà agli hacker la possibilità di scaricare o caricare file tramite URL appositamente modificati. CVE-2023-45727, invece, apre la porta a potenziali attacchi XML External Entity (XXE), che colpiscono le applicazioni per analizzare l’input XML.

CISA ha invitato le agenzie della **Federal Civilian Executive Branch (FCEB)** a risolvere queste vulnerabilità entro il 25 dicembre 2024, per garantire la sicurezza delle reti e prevenire possibili compromissioni.

## Il coinvolgimento di alcuni noti gruppi di hacker

Tra le nuove falle inserite nel catalogo di CISA, CVE-2023-45727 è stata collegata a un gruppo di cyber spionaggio cinese noto come **Earth Kasha**, identificato anche con il nome di **MirrorFace** dagli esperti di Trend Micro. Questa vulnerabilità è perfetta per condurre attacchi mirati. Le vulnerabilità CVE-2024-11680, CVE-2024-51378 e CVE-2024-11667, invece, sono state associate a campagne ransomware come **PSAUX** e **Helldown**.

## Nuove segnalazioni sui router I-O DATA

Parallelamente, il JPCERT/CC, il primo CSIRT (Computer Security Incident Response Team) istituito in Giappone, ha segnalato attività malevole contro i router I-O DATA UD-LT1 e UD-LT1/EX. Tra le vulnerabilità individuate, **una consente ai criminali dotati di accesso come ospite di leggere file sensibili contenenti credenziali**. Un’altra può essere invece sfruttata da utenti autenticati con privilegi amministrativi per eseguire comandi arbitrari. Infine, un’ulteriore criticità permette di **disabilitare il firewall**, alterare la configurazione del router ed eseguire comandi non autorizzati.

## Misure di mitigazione in attesa delle patch

Per una delle falle critiche nei router, la società giapponese I-O DATA ha già rilasciato una patch con il firmware Ver2.1.9. **Gli aggiornamenti per le altre vulnerabilità nei prodotti**, invece, **sono previsti per il 18 dicembre 2024**. Nel frattempo, si raccomanda agli utenti di disattivare la gestione remota, di modificare le password di default per gli account ospite e di usare credenziali amministrative più robuste.

## Monitoraggio costante

I più recenti sviluppi di [CISA](https://www.cisa.gov/) e [JPCERT](https://www.jpcert.or.jp/english/) sulle vulnerabilità nei prodotti mettono in evidenza l’importanza di adottare un approccio proattivo alla cybersecurity, **aggiornando regolarmente i sistemi** e monitorando in modo continuo le possibili falle. **Il panorama delle minacce è in costante evoluzione**. Una corretta gestione dei rischi è fondamentale per proteggere infrastrutture critiche e dati sensibili.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

[Privacy web: Google si conferma lo strumento di tracciamento più usato](https://www.securityinfo.it/2024/12/09/privacy-web-google-si-conferma-lo-strumento-di-tracciamento-piu-usato/)
[CERT-AGID 30 novembre – 6 dicembre: il phishing colpisce Intesa Sanpaolo](https://www.securityinfo.it/2024/12/09/cert-agid-30-novembre-6-dicembre-il-phishing-colpisce-intesa-sanpaolo/)

---

![](https://secure.gravatar.com/avatar/0a083e115b9328218407201798ab82c0?s=90&d=mm&r=g)

##### [Valentina Caruso](https://www.securityinfo.it/author/valentina-caruso/)

##### Articoli correlati

* [![Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/wp-content/uploads/2019/01/Morten-Lehn-120x85.jpg)](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  [Transparency Center Initiative di...](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/ "Permanent link to Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia")

  Gen 18, 2019  [0](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/#respond)
* [![CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/wp-content/uploads/2025/10/CERT-AGID-cover-120x85.png)]...