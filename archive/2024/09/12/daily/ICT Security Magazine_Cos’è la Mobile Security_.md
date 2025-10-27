---
title: Cos’è la Mobile Security?
url: https://www.ictsecuritymagazine.com/articoli/cose-la-mobile-security/
source: ICT Security Magazine
date: 2024-09-12
fetch_date: 2025-10-06T18:31:34.694785
---

# Cos’è la Mobile Security?

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![](https://www.ictsecuritymagazine.com/wp-content/uploads/mobile-security-1.jpg)

# Cos’è la Mobile Security?

A cura di:[Alessio Merlo](#molongui-disabled-link)  Ore 11 Settembre 202416 Ottobre 2024

La *mobile security* è una branca della *cybersecurity* che si occupa specificamente degli aspetti di sicurezza legata ai dispositivi mobili (smartphone, tablet, watch, smart tv…), alla loro interazione con i servizi esterni e alla protezione dell’utente e dei suoi dati personali.

In questo articolo, primo di una serie dedicata alla sicurezza mobile, verranno esplorate le principali sfide e soluzioni per proteggere i dispositivi mobili e le applicazioni. Analizzeremo i concetti fondamentali della sicurezza mobile, con un focus su minacce comuni, vulnerabilità delle applicazioni e le migliori pratiche per mitigare i rischi. Nel prossimo articolo ci concentreremo sulla [sicurezza del sistema operativo Android,](https://www.ictsecuritymagazine.com/articoli/sicurezza-del-sistema-operativo-android/) esaminando le sue caratteristiche, le principali vulnerabilità e le strategie per rafforzarne la protezione.

### Nozioni preliminari di Mobile Security

Per capire gli obiettivi della *mobile security* occorre introdurre il concetto di *threat model*, legato ai dispositivi mobili. Un *threat model* serve a fare assunzioni sulle **capacità di un attaccante** in un dato ecosistema, ed è il primo passo per capire e studiare problemi di *cybersecurity* in ogni sua declinazione.

Ricordiamo che nello scenario descritto nella Figura 1 gli utenti cercano e installano app per aumentare le funzionalità del proprio dispositivo. Dal punto di vista della sicurezza, le app possono essere o vulnerabili o *malware*. Nella prima categoria rientrano app benevole ma che, fisiologicamente, presentano dei problemi di sicurezza, definite **vulnerabilità**. In dettaglio, una vulnerabilità è un *bug* dell’app che ha un impatto sulla sicurezza del sistema o dell’utente. In un’assunzione realistica ogni app, come ogni software, presenta necessariamente qualche vulnerabilità. L’insieme di vulnerabilità di un software prende il nome di **superficie di attacco**.

I *malware* sono invece app malevole sviluppate dall’attaccante al fine di sfruttare vulnerabilità; il primo obiettivo è spingere l’utente ad installarle e/o eseguirle sul proprio dispositivo. Per questo motivo, i malware tendono a camuffarsi da app innocue, o si nascondono dentro app già esistenti tramite un processo, tipico del solo mondo mobile, che si chiama *repackaging* (cfr. Sezione 4.3.2).

![Mobile Security Threat model ](https://www.ictsecuritymagazine.com/wp-content/uploads/2-1-521x700.png)

Figura 2: Threat model del Confused Deputy e delle Colluded Apps

In questo scenario, il *threat model* di riferimento è rappresentato in Figura 2, dove si assume che l’attaccante sia in grado di trovare vulnerabilità esistenti in una qualsiasi app o versione del sistema operativo Android. Inoltre, l’attaccante può produrre un *malware* e distribuirlo sugli *app store* ufficiali e non, nonché tramite canali terzi (e.g., caricandolo su un sito o inviandolo via e-mail), per sfruttare le vulnerabilità scoperte. Infine, si assume che il *malware* riesca a eseguirsi sullo smartphone, tramite interazione con l’utente o sfruttando le caratteristiche di Android.

Una volta eseguito, lo stesso cerca di attaccare l’app vulnerabile o Android, sfruttando i canali di comunicazione messi a disposizione del sistema operativo. Infine, si assume che ogni app benevola non sia a conoscenza di alcuna propria vulnerabilità.

Tale *threat model* prende il nome di *confused deputy*, nome che sottolinea l’impossibilità dell’app di distinguere se le sue interazioni avvengano con un’altra app lecita o con un *malware* che sfrutti qualche sua vulnerabilità.

Una variante del *confused deputy* è quella delle *colluded apps* dove il *malware*, per ridurre le probabilità di essere identificato, divide il codice malevolo su più app maliziose ma all’apparenza innocue. Tuttavia, l’interazione tra queste app permette di perpetrare l’attacco.

### Valutare il peso di una vulnerabilità: il concetto di rischio

La valutazione della pericolosità di una vulnerabilità si esprime in termini di **rischio**. Il rischio associato ad una vulnerabilità è il prodotto tra due metriche, ovvero la **probabilità** e l’**impatto** (**Rischio = Probabilità x Impatto**). La probabilità indica la facilità con cui un attaccante potrebbe sfruttare con successo la vulnerabilità. Facendo un paragone con il mondo reale, la probabilità indica quanto sia facile per un ladro violare la serratura di una casa ed entrarvi.

L’impatto si riferisce alle conseguenze di un attacco riuscito che sfrutta la vulnerabilità. Ad esempio, se l’attaccante, sfruttando la vulnerabilità, riesce ad impossessarsi di numeri di carte di credito, l’impatto sarà alto. Secondo il paragone precedente, l’impatto valuta quanto il ladro riesce a rubare una volta penetrato in casa.

![Mobile Security: Valore di Rischio associato alla Zygote Vulnerability (2011)](https://www.ictsecuritymagazine.com/wp-content/uploads/3-1.png)

Figura 3: Valore di Rischio associato alla Zygote Vulnerability (2011)

A titolo di esempio, la Figura 3 indica il valore di rischio di u...