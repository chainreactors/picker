---
title: CyberVolk: la ricerca di SentinelLabs sul gruppo hacktivista filo-russo
url: https://www.securityinfo.it/2024/12/06/cybervolk-la-ricerca-di-sentinellabs-sul-gruppo-hacktivista-filo-russo/?utm_source=rss&utm_medium=rss&utm_campaign=cybervolk-la-ricerca-di-sentinellabs-sul-gruppo-hacktivista-filo-russo
source: Securityinfo.it
date: 2024-12-07
fetch_date: 2025-10-06T19:40:46.959419
---

# CyberVolk: la ricerca di SentinelLabs sul gruppo hacktivista filo-russo

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

## CyberVolk: la ricerca di SentinelLabs sul gruppo hacktivista filo-russo

Dic 06, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Campagne malware](https://www.securityinfo.it/category/approfondimenti/campagne-malware/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [Ransomware](https://www.securityinfo.it/category/minacce-2/ransomware/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/12/06/cybervolk-la-ricerca-di-sentinellabs-sul-gruppo-hacktivista-filo-russo/#respond)

---

Sempre più gruppi hacker stanno sfruttando gli eventi geopolitici per colpire nuovi obiettivi. Tra questi c’è anche **CyberVolk**, un gruppo di hacktivisti originario dell’India e pro-Russia.

![CyberVolk](https://www.securityinfo.it/wp-content/uploads/2024/12/download-1.png)

I ricercatori dei **[SentinelLabs](https://www.sentinelone.com/labs/cybervolk-a-deep-dive-into-the-hacktivists-tools-and-ransomware-fueling-pro-russian-cyber-attacks/)** hanno approfondito le origini e le modalità di azione del gruppo, il quale **ha lanciato il proprio Ransomware-as-a-Service lo scorso giugno.** La gang, diventata in breve tempo uno dei player più noti del mondo del cybercrimine, utilizza sia attacchi ransomware che DDoS per ostacolare le operazioni contro la Russia.

Il team di SentinelLabs spiega che CyberVolk è particolarmente **abile a sfruttare il malware esistente e modificarlo in base alle proprie esigenze**, rendendolo più sofisticato. “***Il collettivo CyberVolk è uno dei principali esempi di come attaccanti esperti possono accedere e sviluppare builder di ransomware pericolosi** come AzzaSec, Diamond, LockBit, Chaos e altri*” scrivono i ricercatori.

Attivo da maggio 2024, ma già noto da prima con altri nomi, il gruppo ha legami con **LAPSUS$**, **Anonymous** e i **Moroccan Dragons**, oltre a collaborare con **NONAME057(16)** e altri gruppi filo-russi. Il ransomware creato dalla gang deriva dal codice di AzzaSec, un altro gruppo pro-Russia, anti-Israele e anti-Ucraina.

Il ransomware è in grado di terminare qualsiasi processo di Microsoft Management Console o del Task Manager prima di cominciare con la cifratura dei dati. Per la cifratura il malware inizialmente usava l’algoritmo AES, mentre per la generazione delle chiavi utilizzava lo SHA512; il gruppo in seguito ha aggiornato i propri metodi usando **ChaCha20-Poly1305 insieme a AES, RSA e a degli algoritmi quantum resistant.**

Nella nota del riscatto il gruppo chiede un pagamento di 1000 dollari in bitcoin contattando un canale Telegram specifico.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/ransomware-gd594ebff0_1920.jpg)

## I gruppi legati a CyberVolk

CyberVolk conta diversi gruppi ransomware tra i suoi complici; tra essi c’è il **Doubleface Team**, una gang emersa ad agosto 2024, nata dalla convergenza ta CyberVolk e la Moroccan Black Cyber Army.

Questo gruppo utilizza il ransomware Invisible (conosciuto anche come Doubleface), dal funzionamento identico a quello di CyberVolk e anch’esso derivante da AzzaSec. Il codice di Invisible è stato distribuito gratuitamente su numerosi canali di cybercriminali, soprattutto su Telegram.

Tra i gruppi legati a CyberVolk c’è anche **LAPSUS$** che ha utilizzato **HexaLocker**, un ransomware scritto in Golang specifico per sistemi Windows. Lo scorso 20 ottobre il manutentore del canale Telegram usato per distribuire il ransomware ha annunciato di abbandonare il progetto a causa dei rischi elevati dell’attività. **Il malware è stato messo in vendita e al momento sembra che non sia utilizzato.**

Tra gli affiliati più recenti spicca il gruppo di **Parano Ransomware v1,** annunciato come un **“*nuovo ransomware sviluppato con un algoritmo del tutto unico*“**, come si legge sul canale Telegram degli affiliati. Il ransomware offre anche altre funzionalità malevole oltre a quelle base, compreso un infostealer scritto in Python in grado di esfiltrare dati del browser, dettagli degli account Discord e informazioni dei portafogli di criptovalute.

![](https://www.securityinfo.it/wp-content/uploads/2024/12/CyberVolk_15.jpg)

Credits: SentinelLabs

L’attività di CyberVolk non si limita solo al ransomware: il gruppo sviluppa e **distribuisce anche infostealer e webshell** (quest’ultima disponibile da fine ottobre).

A novembre la gang è scomparsa da Telegram, ma non dal web: il gruppo ha annunciato che a**vrebbe continuato la propria attività tramite alcuni post su X**, l’unico social dove è presente attualmente.

“*Il numero di famiglie di ransomware associate al gruppo di hacktivisti CyberVolk evidenzia la c**apacità di questo gruppo di cambiare rapidamente rotta**, basandosi su strumenti esistenti per soddisfare le proprie esigenze e promuovere le proprie cause*” avvertono i ricercatori dei SentinelLabs. Il gruppo si sta evolvendo velocemente, riuscendo ad adattarsi alle risposte delle organizzazioni.

CyberVolk continuerà a sfruttare tool pubblici per modificarli e aumentarne la complessità, così da superare più facilmente le difese aziendali e colpire con successo le sue vittime. “***Le operazioni di ransomware non faranno che diventare più complesse** e aumentare la quantità di informazioni che i team di cybersecuri...