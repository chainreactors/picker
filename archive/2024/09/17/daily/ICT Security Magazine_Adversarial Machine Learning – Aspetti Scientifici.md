---
title: Adversarial Machine Learning – Aspetti Scientifici
url: https://www.ictsecuritymagazine.com/articoli/adversarial-machine-learning-aspetti-scientifici/
source: ICT Security Magazine
date: 2024-09-17
fetch_date: 2025-10-06T18:28:12.991600
---

# Adversarial Machine Learning – Aspetti Scientifici

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/adversarial-attack-machine-learning.jpg)

# Adversarial Machine Learning – Aspetti Scientifici

A cura di:[Andrea Pasquinucci](#molongui-disabled-link)  Ore 16 Settembre 202415 Ottobre 2024

L’Adversarial Machine Learning rappresenta uno degli ambiti più complessi e stimolanti nel contesto della sicurezza dei sistemi di machine learning. Questo campo si caratterizza per la necessità di comprendere e mitigare le diverse tipologie di attacchi che possono compromettere l’integrità, la sicurezza e l’affidabilità dei modelli di apprendimento automatico. Tali attacchi rappresentano una sfida significativa non solo per gli esperti di sicurezza, ma anche per i ricercatori e i praticanti del machine learning che devono confrontarsi con un panorama in continua evoluzione e ricco di nuove minacce.

Questo contributo si inserisce in un percorso di approfondimento che ha già esaminato diverse prospettive di tali attacchi, come discusso nei contributi precedenti sugli “[Attacchi ai Modelli di Intelligenza Artificiale](https://www.ictsecuritymagazine.com/articoli/attacchi-ai-modelli-di-intelligenza-artificiale/)” e sugli “[Adversarial Attacks a Modelli di Machine Learning](https://www.ictsecuritymagazine.com/articoli/adversarial-attacks-a-modelli-di-machine-learning/)“. Questi argomenti sono fondamentali per comprendere l’ampiezza delle vulnerabilità che caratterizzano i moderni sistemi di intelligenza artificiale e per valutare le possibili contromisure.

## Adversarial Machine Learning: Gli Adversarial Examples sono vulnerabilità intrinseche ai modelli di machine learning

Gli Adversarial Examples, discussi nella sezione precedente, non costituiscono eventi di attacco diretti, ma rappresentano piuttosto vulnerabilità intrinseche ai modelli di machine learning che possono essere sfruttate da un avversario per manipolare i risultati ottenuti. Un Adversarial Example è una perturbazione accuratamente progettata, apparentemente insignificante per l’occhio umano, ma capace di indurre il modello a fare errori significativi. Questa capacità di indurre in errore un sistema ben addestrato mette in luce le carenze strutturali nella robustezza dei modelli, evidenziando la necessità di sviluppare strategie di difesa sempre più sofisticate. Analizzeremo come tali vulnerabilità possano essere sfruttate per aggirare i sistemi di machine learning, generando risultati imprevisti o potenzialmente pericolosi per l’integrità del modello, compromettendo così la sua affidabilità operativa.

![Adversarial Machine Learning - Adversarial Examples](https://www.ictsecuritymagazine.com/wp-content/uploads/fig3-1-1024x323.png)

Fig. 3 Reese Witherspoon o Russel Crowe? [Fonte Rif. 5]

Si consideri l’esempio riportato in Fig. 3, che riporta a sinistra un’immagine dell’attrice Reese Witherspoon, come tale riconosciuta da uno specifico modello ML studiato in [Rif. 5]. Analogamente l’immagine a destra riporta l’attore Russel Crowe, correttamente identificato dal modello ML. Viene poi sottoposta al modello ML l’immagine centrale di Reese Witherspoon a cui sono stati aggiunti dei particolari occhiali creati appositamente (la versione fisica di questi occhiali costa solo pochi Euro). Questa immagine è però riconosciuta dal modello ML come un’immagine di Russel Crowe e non di Reese Witherspoon.

Come per molti altri tipi di vulnerabilità dei sistemi IT, se questo modello ML fosse utilizzato in un sistema di controllo degli accessi, questa vulnerabilità potrebbe essere sfruttata da un attaccante per impersonare un’altra persona e accedere illegalmente a un sistema o servizio.

La presenza di *Adversarial Examples* non è l’unico tipo di vulnerabilità o l’unico modo per attaccare o abusare di un modello ML. Sono state proposte alcune tassonomie di attacchi e minacce ai modelli ML e in generale ai modelli di Intelligenza Artificiale, tra cui quella di Microsoft [Rif. 6] riassunta in Fig. 4 e quella di MITRE [Rif. 7], riassunta in Fig. 5.

![Adversarial Machine Learning - Adversarial Examples e machine learning ](https://www.ictsecuritymagazine.com/wp-content/uploads/fig4-1024x559.png)

Fig. 4 Microsoft Threat taxonomy – Failure modes in machine learning [Fonte Rif. 6]

![Adversarial Machine Learning - Adversarial Examples MITRE ATLAS ](https://www.ictsecuritymagazine.com/wp-content/uploads/fig5-1024x425.png)

Fig. 5 MITRE ATLAS [Fonte Rif. 7]

Senza addentrarsi in dettaglio in queste tassonomie, è utile approfondire i principali tipi di attacchi che possono sfruttare vulnerabilità dei modelli ML, inclusa quella degli *Adversarial Examples*.

## Attacchi ai dati di addestramento

La qualità e integrità dei dati utilizzati per l’addestramento di un modello ML sono cruciali per ottenere il comportamento atteso. Per l’addestramento è inoltre spesso necessaria una grande mole di dati, spesso forniti da terze parti.

Come semplice esempio, si consideri il caso di un modello ML utilizzato per identificare messaggi di posta elettronica di SPAM. Un attaccante che vuole organizzare una campagna di SPAM è interessato ad evitare che i propri messaggi siano identificati come SPAM dal modello ML. Per far questo può cercare di inserire i propri messaggi nei dati di addestramento classificandoli come no...