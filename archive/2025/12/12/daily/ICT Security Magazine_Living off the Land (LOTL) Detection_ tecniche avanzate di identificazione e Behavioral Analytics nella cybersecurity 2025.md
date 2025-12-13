---
title: Living off the Land (LOTL) Detection: tecniche avanzate di identificazione e Behavioral Analytics nella cybersecurity 2025
url: https://www.ictsecuritymagazine.com/articoli/living-off-the-land-lotl/
source: ICT Security Magazine
date: 2025-12-12
fetch_date: 2025-12-13T03:15:45.634734
---

# Living off the Land (LOTL) Detection: tecniche avanzate di identificazione e Behavioral Analytics nella cybersecurity 2025

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

![living off the land LOTL.](https://www.ictsecuritymagazine.com/wp-content/uploads/living-off-the-land-LOTL.jpeg)

# Living off the Land (LOTL) Detection: tecniche avanzate di identificazione e Behavioral Analytics nella cybersecurity 2025

A cura di:[Redazione](#molongui-disabled-link)  Ore 12 Dicembre 202518 Novembre 2025

**Living off the land (LOTL)** rappresenta oggi la metodologia di attacco più insidiosa nel panorama della cybersecurity contemporanea. Quando un attaccante riesce a penetrare una rete aziendale senza installare malware riconoscibile, utilizzando esclusivamente strumenti già presenti nel sistema operativo della vittima, ci troviamo di fronte a uno scenario che ridefinisce completamente il concetto di minaccia informatica. Nel 2024, secondo il [CrowdStrike 2025 Global Threat Report](https://www.crowdstrike.com/), il **79% delle detection erano malware-free**, segnando un aumento drammatico rispetto al 40% del 2019. Questo dato conferma che [l’84% degli attacchi high-severity](https://newsletter.cybersecurityhq.com/p/the-rise-of-living-off-the-land-attacks-in-2025-and-how-cisos-must-retool-detection) sfrutta strumenti di sistema legittimi anziché malware custom.

Le tecniche LOTL incarnano un paradigma fondamentale: attacchi che si mimetizzano perfettamente nel traffico legittimo, sfruttando strumenti nativi come **PowerShell**, [Windows Management Instrumentation (WMI)](https://attack.mitre.org/techniques/T1047/), certutil o psexec per condurre operazioni di ricognizione, movimento laterale ed esfiltrazione dati.

Il paradosso della sicurezza moderna risiede proprio qui: gli strumenti più potenti a disposizione di amministratori di sistema e security analyst sono esattamente gli stessi che un threat actor competente utilizzerà per raggiungere i propri obiettivi. Non si tratta più di individuare un file eseguibile sospetto o un hash malevolo noto, ma di distinguere l’uso legittimo di PowerShell da parte di un amministratore dall’abuso dello stesso interprete da parte di un operatore APT.

### Breakout Time: la corsa contro il tempo nella detection LOTL

Una delle metriche più critiche nella detection LOTL è il **breakout time** – il tempo che intercorre tra l’accesso iniziale e il momento in cui l’attaccante inizia a muoversi lateralmente nella rete. Secondo CrowdStrike, nel 2024 il breakout time medio per le intrusioni eCrime interattive è sceso a **48 minuti**, in diminuzione rispetto ai 62 minuti del 2023. Ancora più allarmante, il **breakout time più veloce registrato è stato di soli 51 secondi**, il che significa che i defender hanno meno di un minuto per rilevare e rispondere prima che gli attaccanti stabiliscano un controllo più profondo.

## L’evoluzione delle tecniche LOTL: dai gruppi APT ai ransomware-as-a-service

La proliferazione di queste metodologie è documentata in modo inequivocabile dai report di incident response degli ultimi anni. Gruppi come [FIN7, APT29 e numerosi operatori ransomware](https://medium.com/%40d3lt4labs/non-malware-and-living-off-the-land-tactics-in-modern-cyber-operations-67c882a4126b) hanno progressivamente abbandonato l’uso di malware custom in favore di catene di attacco basate quasi esclusivamente su binari legittimi del sistema operativo. Nel 2024, CrowdStrike ha tracciato **26 nuovi adversary**, portando il totale a **257 adversary nominati**, oltre a 140 cluster di attività malevola e gruppi emergenti.

[APT29, associato a operazioni di spionaggio russo](https://utopianknight.com/living-off-the-land-in-cyber-security-understanding-the-silent-threat/), ha utilizzato frequentemente PowerShell, WMI e scheduled tasks durante campagne di spionaggio, riducendo significativamente le possibilità di detection. FIN7, gruppo finanziariamente motivato, ha abbracciato LOTL per ragioni pratiche e scalabili, utilizzando estensivamente Sysinternals PsExec per il movimento laterale e ProcDump per estrarre credenziali dalla memoria LSASS.

### China-nexus adversaries: l’escalation delle operazioni LOTL

Un trend particolarmente preoccupante emerso nel 2024 riguarda l’**attività China-nexus**, che è aumentata del **150% in tutti i settori** rispetto al 2023. I settori finanziario, media, manufacturing e industrials hanno registrato aumenti ancora più drammatici, tra il 200% e il 300%. Questi adversary hanno dimostrato crescente sofisticazione nell’uso di tecniche LOTL, implementando **operational relay box (ORB) networks** composti da centinaia o migliaia di dispositivi compromessi per offuscare le loro operazioni.

### Il progetto LOLBAS e la catalogazione sistematica degli strumenti weaponizzabili

Il cuore del problema risiede nella natura stessa degli strumenti coinvolti. Il [progetto LOLBAS (Living Off The Land Binaries and Scripts)](https://lolbas-project.github.io/) documenta sistematicamente i binari e gli script legittimi presenti in Windows che possono essere abusati da attaccanti, mappandoli al [framework MITRE ATT&CK](https://attack.mitre.org/). Questo database open-source, mantenuto dalla community di sicurezza, cataloga oltre 200 binari Windows che possono essere weaponizzati per scopi malevoli.

**PowerShell**, ad esempio, è un framework di automazione estremamente potente, progettato per semplificare l’amministrazione di sistemi Windows attraverso accesso diretto a .NET Framework, COM e WMI. [PowerShell appare nel 71% dei casi LOTL](https://www.vectra.ai/topics/living-off-the-land), poiché questa ste...