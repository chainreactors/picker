---
title: NGINX Rift, rischio RCE per una falla rimasta nascosta 18 anni
url: https://www.securityinfo.it/2026/05/14/nginx-rift-rischio-rce-per-una-falla-rimasta-nascosta-18-anni/?utm_source=rss&utm_medium=rss&utm_campaign=nginx-rift-rischio-rce-per-una-falla-rimasta-nascosta-18-anni
source: Securityinfo.it
date: 2026-05-14
fetch_date: 2026-05-15T05:53:19.938425
---

# NGINX Rift, rischio RCE per una falla rimasta nascosta 18 anni

Aggiornamenti recenti Maggio 14th, 2026 3:40 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [NGINX Rift, rischio RCE per una falla rimasta nascosta 18 anni](https://www.securityinfo.it/2026/05/14/nginx-rift-rischio-rce-per-una-falla-rimasta-nascosta-18-anni/)
* [Falso repository OpenAI su Hugging Face distribuisce malware](https://www.securityinfo.it/2026/05/11/falso-repository-openai-su-hugging-face-distribuisce-malware/)
* [Ecco il GitHub per fare di Claude un operatore OSINT avanzato](https://www.securityinfo.it/2026/05/08/ecco-il-github-per-fare-di-claude-un-operatore-osint-avanzato/)
* [Un dipendente su otto considera accettabile vendere le credenziali](https://www.securityinfo.it/2026/05/07/un-dipendente-su-otto-considera-accettabile-vendere-le-credenziali/)
* [Quasar Linux RAT: malware che punta alla supply chain software](https://www.securityinfo.it/2026/05/06/quasar-linux-rat-malware-che-punta-alla-supply-chain-software/)

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

## NGINX Rift, rischio RCE per una falla rimasta nascosta 18 anni

Mag 14, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/05/14/nginx-rift-rischio-rce-per-una-falla-rimasta-nascosta-18-anni/#respond)

---

Una vulnerabilità critica rimasta nascosta per quasi due decenni sta scuotendo il mondo della sicurezza applicativa. I [ricercatori di depthfirst](https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability?utm_source=chatgpt.com) hanno infatti identificato una falla nel modulo di rewrite di NGINX che potrebbe consentire a un attaccante remoto non autenticato di causare crash dei processi oppure, in determinate condizioni, ottenere esecuzione di codice remoto (RCE).  La vulnerabilità, tracciata come CVE-2026-42945 e soprannominata “NGINX Rift”, ha ricevuto **un punteggio CVSS di 9.2 ed è particolarmente significativa** non solo per la gravità tecnica, ma anche perché sarebbe stata introdotta nel codice nel lontano 2008, restando invisibile per circa 18 anni.

![](https://www.securityinfo.it/wp-content/uploads/2026/05/BugNGIX-1024x683.png)

Secondo quanto riportato dagli advisory pubblicati da F5 e dagli stessi ricercatori, il problema interessa **il modulo ngx\_http\_rewrite\_module, utilizzato comunemente per manipolare URL e richieste HTTP** all’interno delle configurazioni NGINX.

### **Il problema nasce dalle direttive di rewrite**

La falla si manifesta in configurazioni specifiche in cui vengono utilizzate direttive come rewrite, if o set insieme a capture regex non nominate, ad esempio $1 o $2, e stringhe contenenti il carattere ?. In queste circostanze, richieste HTTP opportunamente costruite possono provocare un **heap buffer overflow nel processo worker di NGINX**. Nella maggior parte dei casi l’effetto immediato sarebbe un denial of service, con il crash del worker e il suo successivo riavvio automatico. Tuttavia, i ricercatori hanno dimostrato che in ambienti dove la protezione ASLR (Address Space Layout Randomization) è disabilitata, è possibile arrivare anche all’esecuzione arbitraria di codice. Il team di depthfirst ha dichiarato di aver sviluppato **una proof-of-concept funzionante per l’RCE** e di aver condiviso il materiale con NGINX durante il processo di responsible disclosure.

### **Milioni di sistemi potenzialmente esposti**

La rilevanza della vulnerabilità deriva anche dalla **diffusione globale di NGINX, uno dei web server più utilizzati al mondo**, ampiamente presente in ambienti enterprise, cloud, CDN, reverse proxy e infrastrutture Kubernetes. Secondo le informazioni diffuse dagli advisory, sarebbero vulnerabili tutte le versioni comprese tra NGINX 0.6.27 e 1.30.0. Le patch sono state introdotte nelle versioni 1.31.0 e 1.30.1.

Anche se al momento **non risultano exploit attivi pubblicamente documentati**, diversi osservatori ritengono probabile una rapida weaponization della falla, soprattutto considerando la semplicità con cui è possibile innescare il crash dei processi worker.

### **Non solo CVE-2026-42945: emergono altre vulnerabilità**

L’analisi di depthfirst ha portato all’identificazione di **ulteriori problemi di sicurezza** all’interno dell’ecosistema NGINX. Tra questi figurano vulnerabilità di excessive memory allocation, use-after-free e out-of-bounds read che interessano moduli SCGI, uWSGI, SSL e charset. Alcune di queste falle potrebbero consentire lettura di memoria, disclosure di informazioni sensibili oppure ulteriori crash dei worker process. Sebbene abbiano punteggi inferiori rispetto a CVE-2026-42945, contribuiscono a delineare un quadro delicato per amministratori di sistema e team DevSecOps.

### **Il ruolo crescente dell’AI nella scoperta delle vulnerabilità**

Uno degli aspetti più interessanti del caso riguarda il metodo con cui le falle sono state individuate. Depthfirst ha spiegato di aver **utilizzato un sistema automatizzato basato su analisi avanzata del codice sorgente** capace di individuare vulnerabilità di memory corruption all’interno di NGINX.

Il tema è particolarmente rilevante perché mostra come strumenti automatizzati e **tecniche AI-assisted** stiano diventando sempre più efficaci nell’individuazione di bug storici annidati in software critici. Parallelamente, questo scenario potrebbe accelerare anche la capacità offensiva degli attaccanti, riducendo drasticamente i tempi necessari per identificare superfici vulnerabili all’interno di grandi codebase legacy.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [CVE-2026-42945](https://www.securityinfo.it/tag/cve-2026-42945/), [cybersecurity web server](https://www.securityinfo.it/tag/cybersecurity-web-server/), [exploit NGINX rewrite module](https://www.securityinfo.it/tag/exploit-nginx-rewrite-module/), [F5 NGINX patch](https://www.securityinfo.it/tag/f5-nginx-patch/), [heap buffer overflow NGINX](https://www.securityinfo.it/tag/heap-buffer-overflow-nginx/), [NGINX RCE](https://www.securityinfo.it/tag/nginx-rce/), [NGINX Rift](https://www.securityinfo.it/tag/nginx-rift/), [sicurezza web server](https://www.securityinfo.it/tag/sicurezza-web-server/), [vulnerabilità Linux server](https://www.securityinfo.it/tag/vulnerabilita-linux-server/), [vulnerabilità NGINX](https://www.securityinfo.it/tag/vulnerabilita-nginx/)

[Falso repository OpenAI su Hugging Face distribuisce malware](https://www.securityinfo.it/2026/05/11/falso-repository-openai-su-hugging-face-distribuisce-malware/)

---

![](https://secure.gravatar.com/avatar/93ad3a1bbb47d1f5755e4f5086cb3f22?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/autho...