---
title: Scoperta una variante Linux del ransomware Play che colpisce gli ambienti ESXi
url: https://www.securityinfo.it/2024/07/22/scoperta-una-variante-linux-del-ransomware-play-che-colpisce-gli-ambienti-esxi/?utm_source=rss&utm_medium=rss&utm_campaign=scoperta-una-variante-linux-del-ransomware-play-che-colpisce-gli-ambienti-esxi
source: Securityinfo.it
date: 2024-07-23
fetch_date: 2025-10-06T17:45:57.441683
---

# Scoperta una variante Linux del ransomware Play che colpisce gli ambienti ESXi

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

## Scoperta una variante Linux del ransomware Play che colpisce gli ambienti ESXi

Lug 22, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/07/22/scoperta-una-variante-linux-del-ransomware-play-che-colpisce-gli-ambienti-esxi/#respond)

---

I ricercatori di Trend Micro [hanno scoperto](https://www.trendmicro.com/en_us/research/24/g/new-play-ransomware-linux-variant-targets-esxi-shows-ties-with-p.html) una v**ariante Linux del ransomware Play** che cifra i file solo quando si trova in un ambiente ESXi VMware. Il gruppo è attivo dal 2022, ma è la prima volta che esegue campagne attaccando i sistemi Linux.

Finora il ransomware ha colpito per lo più organizzazioni negli Stati Uniti, in particolare quelle del settore manifatturiero e dei servizi professionali. La variante Linux indica che il gruppo sta cercando di **espandersi per colpire nuove vittime**e aumentare i propri guadagni.

I ricercatori spiegano che **il gruppo ottiene l’accesso iniziale ai sistemi tramite tecniche di phishing**, sottraendo credenziali valide di utenti aziendali. In seguito, dopo aver stabilito la comunicazione, esegue una serie di tool per individuare altre macchine da infettare (Netscan), per il movimento laterale (PsExec), per la gestione dei comandi inviati dal server C2 (Coroxy backdoor) e per l’esfiltrazione dei dati (WinRAR e WinSCP).

La variante ESXi esegue una serie di comandi relativi a questo ambiente per capire se si trova effettivamente in un ambiente VMware; in caso positivo, prosegue con il flusso di infezione, altrimenti termina il processo e cancella tutti i file creati.

![ransomware](https://www.securityinfo.it/wp-content/uploads/2024/02/ransomware-3998798_1920.jpg)

Pixabay

Tra i file cifrati ci sono anche quelli relativi alla VM, come le informazioni sui dischi, le configurazioni e i metadati. La maggior parte dei file cifrati contiene **informazioni critiche sulle applicazioni e sull’utente della macchina.** Dopo aver concluso il processo di cifratura, la variante Linux del ransomware appende l’estensione “.play” ai file risultanti e crea una nota per il riscatto nella directory di root contenente i link ai siti Tor del gruppo.

Secondo l’analisi dei ricercatori, l’**URL da cui gli attaccanti scaricano il payload del ransomware è collegato a Prolific Puma**, un altro gruppo di cybercriminali. Prolific Puma è noto per generare nomi di dominio tramite un algoritmo apposito e utilizzarli per offrire un servizio di link-shortening per gli altri attaccanti, i quali lo usano poi per eludere i controlli durante le campagne di phishing e malware.

Per proteggere efficacemente gli ambienti ESXi (e non solo) dai ransomware, i ricercatori ricordano di **applicare regolarmente le patch** e installare gli ultimi aggiornamenti disponibili, segmentare la rete e implementare m**eccanismi robusti per il controllo degli accessi**. Per minimizzare la superficie di attacco è inoltre fondamentale **disabilitare tutti i servizi e i protocolli non utilizzati.** Infine, è opportuno pianificare ed eseguire **backup regolari** e risolvere le potenziali configurazioni errate degli ambienti di lavoro.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [ESXi](https://www.securityinfo.it/tag/esxi/), [Linux](https://www.securityinfo.it/tag/linux/), [PLAY](https://www.securityinfo.it/tag/play/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [Trend Micro](https://www.securityinfo.it/tag/trend-micro/), [VMware](https://www.securityinfo.it/tag/vmware/)

[Il numero di vittime dei data breach è aumentato del 1.000%](https://www.securityinfo.it/2024/07/23/il-numero-di-vittime-dei-data-breach-e-aumentato-del-1-000/)
[Le istituzioni finanziarie lavorano per rafforzare le proprie misure di sicurezza](https://www.securityinfo.it/2024/07/22/le-istituzioni-finanziarie-lavorano-per-rafforzare-le-proprie-misure-di-sicurezza/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report ...