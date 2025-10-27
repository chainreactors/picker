---
title: Lorenz: attacco ransomware a distanza di mesi
url: https://www.securityinfo.it/2023/01/12/lorenz-attacco-ransomware-a-distanza-di-mesi/?utm_source=rss&utm_medium=rss&utm_campaign=lorenz-attacco-ransomware-a-distanza-di-mesi
source: Over Security - Cybersecurity news aggregator
date: 2023-01-13
fetch_date: 2025-10-04T03:48:46.866128
---

# Lorenz: attacco ransomware a distanza di mesi

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## Lorenz: attacco ransomware a distanza di mesi

Gen 12, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [News](https://www.securityinfo.it/category/news/), [Ransomware](https://www.securityinfo.it/category/minacce-2/ransomware/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/01/12/lorenz-attacco-ransomware-a-distanza-di-mesi/#respond)

---

I ricercatori di sicurezza di S-RM hanno scoperto una modalità di comportamento piuttosto estremo, che denota molta **pazienza, pianificazione e fiducia** nei propri mezzi.

I criminali informatici hanno infatti sfruttato alcune vulnerabilità per collocare backdoor quando c’era l’occasione, per poi **tornare e colpire molto tempo dopo**, quando la vittima aveva applicato gli aggiornamenti di sicurezza che nel frattempo erano stati prodotti e distribuito.

Nello specifico, il caso è un attacco ransomware portato dal gruppo Lorenz che è stato completato mesi dopo che i criminali avevano ottenuto l’accesso alla rete della vittima utilizzando un **exploit per un bug critico in un sistema di telefonia**.

## La semina della backdoor

I ricercatori della società di consulenza [S-RM](https://insights.s-rminform.com/lorenz-cyber-intelligence-briefing-special) hanno stabilito che i criminali avevano **violato la rete delle vittime cinque mesi prima** di iniziare a rubare dati e crittografare i sistemi.

![](https://www.securityinfo.it/wp-content/uploads/2023/01/thomas-peham-WCFQfysyi3g-unsplash-scaled.jpg)

La vulnerabilità utilizzata dagli attaccanti era un bug critico nell’infrastruttura di telefonia Mitel ([CVE-2022-29499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29499)) che consente l’esecuzione di codice remoto. La **patch per questa vulnerabilità è stata rilasciata a luglio** ma i criminali avevano già installato una backdoor una settimana prima.

La **backdoor era costituita da una singola riga di codice** PHP che ascoltava le richieste HTTP POST con due parametri: “id”, che fungeva da credenziale per l’accesso al sistema, e “img” che includeva i comandi da eseguire.

Gli hacker hanno nascosto la backdoor in una directory legittima sul sistema, con una denominazione apparentemente inoffensiva (“twitter\_icon\_”) e l’hanno **lasciata dormire per cinque mesi**. Quando erano pronti, hanno utilizzato la backdoor per distribuire il ransomware Lorenz nel giro di 48 ore.

## Verificare le intrusioni

Secondo i ricercatori di S-RM, il lungo intervallo di lunga inattività potrebbe essere dovuto al fatto che il **gruppo ransomware abbia acquistato l’accesso alla rete da un broker** o che abbia un ramo dedicato all’acquisizione dell’accesso iniziale.

Per questo motivo, i ricercatori sottolineano che aggiornare i software all’ultima versione al momento giusto è un passo importante nella difesa della rete, ma nel caso di vulnerabilità critiche, **le aziende dovrebbero anche tenere sotto controllo il loro ambiente per evidenziare tentativi di exploit** e possibili intrusioni.

La revisione dei registri, la ricerca di accessi o comportamenti non autorizzati e il monitoraggio della rete alla ricerca di traffico inatteso potrebbero infatti **rivelare un’intrusione capace di sopravvivere agli aggiornamenti** di sicurezza.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco](https://www.securityinfo.it/tag/attacco/), [lorenz](https://www.securityinfo.it/tag/lorenz/), [mitel](https://www.securityinfo.it/tag/mitel/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [S-RM](https://www.securityinfo.it/tag/s-rm/)

[Cybersecurity: le figure che possono sopperire alla carenza di talenti](https://www.securityinfo.it/2023/01/13/transizione-team-cybersecurity/)
[Guilty Gear Strive colpito dagli hacker: una vulnerabilità causa il crash del sistema](https://www.securityinfo.it/2023/01/12/guilty-gear-strive-hacker-vulnerabilita/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respo...