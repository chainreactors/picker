---
title: Vulnerabilità critica minaccia migliaia di Nas QNAP in Italia
url: https://www.securityinfo.it/2023/02/03/vulnerabilita-critica-minaccia-migliaia-di-nas-qnap-in-italia/?utm_source=rss&utm_medium=rss&utm_campaign=vulnerabilita-critica-minaccia-migliaia-di-nas-qnap-in-italia
source: Over Security - Cybersecurity news aggregator
date: 2023-02-04
fetch_date: 2025-10-04T05:41:57.020271
---

# Vulnerabilità critica minaccia migliaia di Nas QNAP in Italia

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

## Vulnerabilità critica minaccia migliaia di Nas QNAP in Italia

Feb 03, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Concept](https://www.securityinfo.it/category/minacce-2/concept/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [Ransomware](https://www.securityinfo.it/category/minacce-2/ransomware/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/02/03/vulnerabilita-critica-minaccia-migliaia-di-nas-qnap-in-italia/#respond)

---

Il produttore di sistemi di storage [QNAP](https://www.qnap.com/it-it) ha annunciato una **vulnerabilità critica che interessa decine di migliaia di dispositivi NAS** (Network-Attached Storage). La vulnerabilità SQL injection ([CVE-2022-27596](https://nvd.nist.gov/vuln/detail/CVE-2022-27596)) può essere sfruttata da attori remoti per iniettare codice dannoso in dispositivi QNAP esposti e non protetti.

La società ha valutato la vulnerabilità con un punteggio CVSS di [9,8 su 10](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) e ha dichiarato che **può essere facilmente sfruttata da attori malintenzionati** senza bisogno interazione dell’utente. QNAP raccomanda ai clienti di aggiornare il software del dispositivo alla versione più recente per prevenire eventuali attacchi.

I dispositivi interessati sono quelli che hanno installato i sistemi operativi QTS 5.0.1 e QuTS hero h5.0.1; per risolvere il problema **è sufficiente svolgere la consueta procedura di aggiornamento**, ma è opportuno forzare la verifica della presenza di nuove release del firmware per applicare le versioni più recenti.

QNAP non ha segnalato che la vulnerabilità sia effettivamente stata sfruttata in the wild, ma **consiglia ai clienti di aggiornare i prodotti il prima possibile**, perché i sistemi Nas sono tra i bersagli preferiti degli attacchi ransomware.

## L’analisi di Censys

Il giorno dopo il rilascio degli aggiornamenti di sicurezza da parte di Qnap, [Censys](https://censys.io/) ha pubblicato un [rapporto](https://censys.io/cve-2022-27596/) in cui stima l’impatto del problema e la situazione sul campo. Secondo l’analisi, **solo una piccola percentuale dei dispositivi QNAP NAS** online è stata patchata.

Di oltre 67.000 host individuati con sistemi basati QNAP, solo 557 hanno in esecuzione le versioni sicure di QuTS Hero o QTS, **lasciando più del 98% dei dispositivi vulnerabili**.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/image1-5.png)

Fonte: Censys

Dopo gli Stati Uniti, l’I**talia è il secondo Paese per numero di host individuati, e la prima per dispositivi vulnerabili**. Fortunatamente, il difetto per ora non è ancora sfruttato e non c’è codice exploit, quindi gli amministratori hanno ancora un po’ di tempo per intervenire sui dispositivi.

Tuttavia, dal momento che i NAS QNAP sono stati presi di mira da diverse minacce ransomware in passato**, i clienti devono installare immediatamente le patch** per prevenire futuri attacchi.

Mark Ellzey, ricercatore di Censys, ha commentato: “Se l’exploit viene pubblicato e armato, potrebbe significare problemi a migliaia di utenti QNAP. **Tutti devono aggiornare immediatamente i propri dispositivi** QNAP per essere al sicuro da future campagne ransomware”.

Oltre ad aggiornare il dispositivo NAS al più presto, è anche consigliabile **non renderlo accessibile da remoto** se non strettamente necessario. QNAP aveva consigliato ai clienti con dispositivi esposti verso Internet di disattivare la funzione Port Forwarding del router, disabilitare la funzione UPnP del QNAP NAS e i servizi più pericolosi, come Ssh o Telnet.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Censys](https://www.securityinfo.it/tag/censys/), [NAS](https://www.securityinfo.it/tag/nas/), [QNAP](https://www.securityinfo.it/tag/qnap/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [SQL Injection](https://www.securityinfo.it/tag/sql-injection/)

[Il ransomware ESXiArgs spaventa l’opinione pubblica](https://www.securityinfo.it/2023/02/06/il-ransomware-esxiargs-spaventa-lopinione-pubblica/)
[Ransomware, IAB e infostealer: le minacce da tenere d'occhio nel 2023](https://www.securityinfo.it/2023/02/03/ransomware-iab-infostealer-minacce-2023/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-...