---
title: Il ransomware StopCrypt evolve per eludere la sicurezza
url: https://www.securityinfo.it/2024/03/18/il-ransomware-stopcrypt-evolve-per-eludere-la-sicurezza/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-19
fetch_date: 2025-10-04T12:12:56.561026
---

# Il ransomware StopCrypt evolve per eludere la sicurezza

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

## Il ransomware StopCrypt evolve per eludere la sicurezza

Mar 18, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/03/18/il-ransomware-stopcrypt-evolve-per-eludere-la-sicurezza/#respond)

---

Il team di SonicWall Capture Labs ha scoperto di recente una **[nuova variante](https://blog.sonicwall.com/en-us/2024/03/new-multi-stage-stopcrypt-ransomware/) di StopCrypt** che usa un meccanismo di esecuzione in più fasi per eludere i controlli di sicurezza.

**StopCrypt**, scoperto per la prima volta nel 2018, è un ransomware che, a differenza di LockBit, BlackCat o altri malware più conosciuti, **colpisce i singoli utenti** chiedendo riscatti relativamente bassi, dai 400 ai 1000 dollari. Generalmente questo ransomware viene distribuito tramite **installer di falsi software gratuiti** che, oltre a StopCrypt, distribuiscono anche trojan per sottrarre password e altre informazioni.

La nuova versione del ransomware usa un **ciclo di infezione in più fasi per superare i controlli di sicurezza.** All’inizio dell’esecuzione, crea ed esegue un file .dll che non viene però usato nelle fasi successive; i ricercatori sostengono che sia un diversivo per eludere i controlli.

Entrato nel vivo dell’esecuzione, il ransomware **crea delle chiamate a API direttamente sullo stack** e alloca la memoria necessaria per avere permessi di lettura, scrittura ed esecuzione. Durante questa fase StopCrypt definisce una serie di funzioni per eseguire operazioni sul dispositivo, tra le quali anche catturare uno screenshot dei processi in esecuzione.

![ransomware](https://www.securityinfo.it/wp-content/uploads/2024/02/ransomware-3998798_1920.jpg)

Pixabay

La seconda fase del payload consiste nel ***process hollowing***, una tecnica di code injection che rimpiazza i processi legittimi in esecuzione con il payload del malware; ciò permette di “nascondere” il codice malevolo nei processi così che venga eseguito senza essere bloccato.

Nella fase finale, il ransomware **esegue una serie di API per controllare l’esecuzione dei processi e le operazioni sulla memoria**, oltre che per ottenere persistenza sul dispositivo. StopCrypt lancia il processo “icacls.exe” per accedere e modificare le Access Control List di Windows, negando l’accesso all’utente alla directory del ransomware. Infine, il ransomware crea un **task che esegue una copia del payload finale ogni cinque minuti**, poi procede alla cifratura dei file.

Nella nota di riscatto gli attaccanti chiedono **980 dollari per decifrare i file**, prezzo che scende a 490 dollari se il pagamento avviene entro 72 ore dall’attacco.

StopCrypto, del quale finora si è sempre parlato poco visti gli impatti contenuti, ha assunto una certa importanza nel mondo della cybersecurity dopo questa evoluzione: **il ransomware è diventato più difficile da individuare** e quindi contrastare con i normali strumenti di protezione.

Il consiglio è, come sempre, di **non scaricare mai software da siti terzi**, ma solo da fonti ufficiali e affidabili

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [controlli di sicurezza](https://www.securityinfo.it/tag/controlli-di-sicurezza/), [malware](https://www.securityinfo.it/tag/malware/), [multistage](https://www.securityinfo.it/tag/multistage/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [SonicWall](https://www.securityinfo.it/tag/sonicwall/), [StopCrypto](https://www.securityinfo.it/tag/stopcrypto/)

[Hacker sfruttano le eSIM per l'hijacking del numero di telefono](https://www.securityinfo.it/2024/03/18/esim-hijacking-numero-telefono/)
[Resi noti i dettagli di una vulnerabilità Kubernetes a rischio elevato](https://www.securityinfo.it/2024/03/15/resi-noti-i-dettagli-di-una-vulnerabilita-kubernetes-a-rischio-elevato/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali](https://www.securityinfo.it/wp-content/uploads/2025/09/cyber-security-3411499_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/ "SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali")

  [SonicWall vittima di un breach, la...](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/ "Permanent link to SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali")

  Set 19, 2025  [0](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai...