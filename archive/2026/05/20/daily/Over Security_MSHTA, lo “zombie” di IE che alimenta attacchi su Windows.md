---
title: MSHTA, lo “zombie” di IE che alimenta attacchi su Windows
url: https://www.securityinfo.it/2026/05/19/mshta-lo-zombie-di-internet-explorer-che-alimenta-attacchi-su-windows/
source: Over Security
date: 2026-05-20
fetch_date: 2026-05-21T06:04:09.949602
---

# MSHTA, lo “zombie” di IE che alimenta attacchi su Windows

Aggiornamenti recenti Maggio 20th, 2026 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Attacco ai router Huawei dietro blackout telecom del Lussemburgo](https://www.securityinfo.it/2026/05/20/attacco-ai-router-huawei-dietro-blackout-telecom-del-lussemburgo/)
* [MSHTA, lo “zombie” di IE che alimenta attacchi su Windows](https://www.securityinfo.it/2026/05/19/mshta-lo-zombie-di-internet-explorer-che-alimenta-attacchi-su-windows/)
* [NGINX Rift, rischio RCE per una falla rimasta nascosta 18 anni](https://www.securityinfo.it/2026/05/14/nginx-rift-rischio-rce-per-una-falla-rimasta-nascosta-18-anni/)
* [Falso repository OpenAI su Hugging Face distribuisce malware](https://www.securityinfo.it/2026/05/11/falso-repository-openai-su-hugging-face-distribuisce-malware/)
* [Ecco il GitHub per fare di Claude un operatore OSINT avanzato](https://www.securityinfo.it/2026/05/08/ecco-il-github-per-fare-di-claude-un-operatore-osint-avanzato/)

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

## MSHTA, lo “zombie” di IE che alimenta attacchi su Windows

Mag 19, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/05/19/mshta-lo-zombie-di-internet-explorer-che-alimenta-attacchi-su-windows/#respond)

---

Nonostante Internet Explorer sia ormai ufficialmente morto da tempo, uno dei suoi componenti storici continua a rappresentare un serio problema di sicurezza per gli ambienti Windows moderni. Si tratta di **MSHTA.exe**, il Microsoft HTML Application Host, una utility legacy ancora inclusa di default nel sistema operativo e **oggi sempre più sfruttata dai cybercriminali** per distribuire malware, loader e infostealer.

![](https://www.securityinfo.it/wp-content/uploads/2026/05/ZombieIE-1024x683.png)

Secondo una nuova ricerca pubblicata da [Bitdefender Labs](https://www.bitdefender.com/en-us/blog/labs/microsofts-mshta-legacy-malware-windows?utm_source=chatgpt.com), negli ultimi mesi si è registrato un forte aumento delle catene di attacco che utilizzano **mshta.exe** come componente centrale delle operazioni malevole. Il fenomeno riguarda **sia campagne cybercriminali opportunistiche sia minacce più sofisticate** basate su tecniche LOLBIN, cioè “Living-off-the-Land Binary”.

Il problema è particolarmente delicato perché MSHTA è **un binario firmato da Microsoft e considerato legittimo** dal sistema operativo. Questo consente agli attaccanti di utilizzare uno strumento trusted di Windows per eseguire codice malevolo riducendo la probabilità di essere intercettati dalle difese tradizionali.

**Cos’è MSHTA e perché esiste ancora in Windows**

MSHTA **nasce alla fine degli anni ’90 insieme a Internet Explorer 5** come componente dedicato all’esecuzione delle cosiddette HTML Application (HTA), applicazioni sviluppate con HTML, VBScript e JavaScript. L’obiettivo originario era **permettere la creazione di piccoli strumenti amministrativi o applicazioni desktop leggere** basate su tecnologie web. Nonostante la progressiva scomparsa di Internet Explorer, Microsoft ha continuato a mantenere MSHTA in Windows per ragioni di **backward compatibility**, soprattutto nei contesti enterprise dove alcuni ambienti legacy continuano ancora a dipendere da script e applicazioni HTA.

Secondo Bitdefender, una parte limitata dell’utilizzo di MSHTA è ancora legittima. **Alcuni amministratori lo impiegano** per script di login, notifiche di aggiornamento o piccoli tool interni. Tuttavia, la componente malevola sta crescendo molto più rapidamente rispetto agli utilizzi leciti. Ma c’è un problema: MSHTA consente di **eseguire script direttamente in memoria**, scaricare contenuti remoti ed eludere diversi controlli di sicurezza sfruttando un processo firmato Microsoft.

**Come gli attaccanti usano MSHTA nelle campagne malware**

Secondo i ricercatori di Bitdefender, MSHTA viene oggi utilizzato soprattutto come **stadio intermedio** nelle moderne catene di infezione. Gli attaccanti convincono la vittima ad aprire file HTA o eseguire comandi apparentemente innocui tramite phishing, siti fake, campagne ClickFix o falsi aggiornamenti software. Una volta avviato, **mshta.exe può recuperare script remoti e lanciare codice PowerShell o VBScript** direttamente in memoria senza scrivere necessariamente payload evidenti sul disco.

Questo approccio permette di distribuire malware come **Lumma Stealer**, Amatera e altri infostealer moderni mantenendo un profilo operativo relativamente basso. Bitdefender segnala inoltre che molti dei domini contattati dalle campagne osservate utilizzano tecniche di **typosquatting**, simulando URL apparentemente legittimi per aumentare la credibilità dell’infrastruttura malevola. Il vantaggio per gli attaccanti è duplice. Da un lato utilizzano un binario di sistema trusted; dall’altro **eseguono gran parte dell’attività malevola direttamente in memoria**, riducendo la visibilità per antivirus e strumenti EDR meno evoluti.

**Il ritorno dei LOLBIN e la crisi delle difese tradizionali**

Il caso MSHTA conferma un trend ormai consolidato nel panorama della cybersecurity: il ritorno massiccio delle tecniche **LOLBIN**. Invece di introdurre malware custom facilmente identificabili, molti gruppi criminali preferiscono sfruttare componenti già presenti nel sistema operativo per mascherare le proprie attività. **Windows offre numerosi strumenti di questo tipo** — PowerShell, rundll32, regsvr32, certutil, wmic — e MSHTA continua a essere uno dei più efficaci.

Questo approccio complica enormemente il lavoro dei team SOC perché il comportamento osservato appare inizialmente legittimo. **Bloccare completamente mshta.exe può inoltre creare problemi operativi** in alcune aziende che utilizzano ancora applicazioni legacy. Secondo diversi analisti, il problema deriva anche dall’enorme eredità storica di Windows. La necessità di mantenere compatibilità con software sviluppati decenni fa continua infatti a lasciare disponibili componenti che oggi rappresentano superfici di attacco estremamente appetibili.

**Perché MSHTA è ancora così efficace contro le aziende**

Uno degli aspetti più interessanti evidenziati dal report riguarda la persistenza operativa di questo strumento nonostante le tecnologie moderne di sicurezza. Molte organizzazioni si concentrano infatti sulla rilevazione del malware finale, ma **monitorano molto meno attentamente i processi trusted** del sistema operativo.

MSHTA permette inoltre di **concatenare facilmente più tecnologie offensive**. Un semplice file HTA può scaricare script PowerShell, avviare payload in memoria, contattare server remoti e stabilire persistenza senza utilizzare eseguibili trad...