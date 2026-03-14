---
title: Il ransomware non è più il re, benvenuti nell’era del “parassita digitale”
url: https://www.ictsecuritymagazine.com/articoli/parassita-digitale/
source: ICT Security Magazine
date: 2026-03-13
fetch_date: 2026-03-14T04:14:13.925935
---

# Il ransomware non è più il re, benvenuti nell’era del “parassita digitale”

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
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![parassita digitale](https://www.ictsecuritymagazine.com/wp-content/uploads/parassita-digitale.jpeg)

# Il ransomware non è più il re, benvenuti nell’era del “parassita digitale”

A cura di:[Redazione](#molongui-disabled-link)  Ore 13 Marzo 20269 Marzo 2026

Il [Red Report 2026 di Picus Labs](https://www.picussecurity.com/red-report), pubblicato il [10 febbraio 2026](https://www.globenewswire.com/news-release/2026/02/10/3235422/0/en/Picus-Red-Report-2026-Finds-38-Drop-in-Ransomware-Attacks-as-Hackers-Choose-Silent-Residency-Over-Destruction.html), non è il solito bollettino annuale sulle minacce. È un referto autoptico su un modello di attacco che ha dominato un decennio – il ransomware distruttivo – e la certificazione della nascita di qualcosa di più insidioso: il parassita digitale.

Il dataset parla con una chiarezza che lascia poco spazio alle interpretazioni. Picus Labs ha analizzato 1.153.683 file unici, di cui il 94% classificato come malevolo, mappando oltre 15,5 milioni di azioni avversarie sul framework MITRE ATT&CK. Il risultato è una radiografia completa del comportamento offensivo nel 2025, e ciò che emerge rovescia le priorità difensive di migliaia di organizzazioni.

Il dato che definisce l’intero Red Report 2026 è questo: la tecnica “Data Encrypted for Impact” (T1486) – la firma operativa del ransomware – è crollata del 38%, passando dal 21% dei campioni nel 2024 al 12,94% nel 2025. Contemporaneamente, l’80% delle dieci tecniche MITRE ATT&CK più diffuse è ora dedicato a evasione delle difese, persistenza e comando e controllo stealth. La concentrazione più alta di tradecraft stealth mai registrata in sei edizioni del report.

Come ha sintetizzato il Dr. Süleyman Özarslan, co-fondatore e VP di Picus Labs: gli attaccanti hanno capito che è più redditizio abitare l’host che distruggerlo.

Nota metodologica: il Red Report 2026 è prodotto da [Picus Security](https://www.picussecurity.com), vendor specializzato in security validation. Questo non ne diminuisce il valore analitico – il dataset di oltre un milione di campioni e la mappatura su MITRE ATT&CK rappresentano uno dei corpus empirici più ampi disponibili sul comportamento avversario – ma è un elemento che il lettore professionista deve considerare nel valutare le raccomandazioni operative, che naturalmente convergono verso l’approccio di validazione continua propugnato dall’azienda.

## Dal predatore al parassita: anatomia di un cambio di paradigma

Per comprendere la portata di questo cambiamento, occorre partire da una premessa spesso dimenticata: il ransomware tradizionale – quello che cifra i file e chiede un riscatto – è sempre stato, dal punto di vista dell’attaccante, un modello ad alto rischio e rendimento decrescente.

L’encryption è rumorosa. Attiva alert, mobilita incident response, scatena comunicazioni di crisi. E soprattutto, negli ultimi anni, ha perso la sua leva principale: i backup. [Man mano che le organizzazioni hanno investito in strategie di recovery, la capacità del ransomware di estorcere pagamenti si è erosa](https://www.ictsecuritymagazine.com/articoli/le-peculiarita-delle-intrusioni-ransomware/).

I dati convergono da fonti indipendenti: [Chainalysis](https://www.chainalysis.com/blog/crypto-ransomware-2026/) ha stimato che nel 2025 solo il 28% delle vittime identificate ha pagato un riscatto, in netto calo rispetto al [62,8% del 2024](https://www.bleepingcomputer.com/news/security/ransomware-payment-rate-drops-to-record-low-as-attacks-surge/) e al 78,9% del 2022. I pagamenti on-chain si sono attestati intorno a 820 milioni di dollari, in calo dell’8% rispetto all’anno precedente. [Coveware](https://www.coveware.com/blog/2025/10/24/insider-threats-loom-while-ransom-payment-rates-plummet), da un campione diverso e con metodologia differente, riporta percentuali ancora più basse: il 23% nel Q3 2025, con un crollo al 19% per gli incidenti di sola esfiltrazione dati senza cifratura. Le percentuali esatte variano tra le fonti perché coprono campioni e periodi diversi, ma la direzione del trend è univoca e confermata da tutti gli analisti di settore.

Il Red Report 2026 documenta la risposta strategica degli attaccanti a questa crisi di redditività: l’abbandono dell’encryption a favore di ciò che Picus Labs definisce “residenza silenziosa”. Invece di cifrare e fare rumore, il malware moderno si insedia nei sistemi, si mimetizza tra i processi legittimi e opera sotto la soglia di rilevamento per settimane o mesi. L’obiettivo non è più bloccare le operazioni della vittima, ma alimentarsi di credenziali, dati sensibili e accessi privilegiati senza essere scoperto.

È la logica del parassita biologico: l’organismo che uccide il proprio ospite ha vita breve. Quello che lo sfrutta senza ucciderlo prospera.

## L’evoluzione in numeri: Red Report 2025 vs Red Report 2026

Prima di analizzare i tratti del parassita digitale, vale la pena inquadrare l’evoluzione anno su anno. Il confronto tra le due edizioni del report rivela una trasformazione accelerata.

Il [Red Report 2025](https://www.picussecurity.com/resource/report/red-report-2025), basato su oltre 1 milione di campioni e 14 milioni di azioni malevole mappate su ATT&CK, aveva già identificato l’ascesa degli infostealer e del...