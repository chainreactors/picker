---
title: Valutazione dei Rischi nella IA Generativa
url: https://www.ictsecuritymagazine.com/articoli/rischi-ia-generativa/
source: ICT Security Magazine
date: 2025-02-26
fetch_date: 2025-10-06T20:47:58.162065
---

# Valutazione dei Rischi nella IA Generativa

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

![Framework di gestione dei rischi nella IA Generativa, con rappresentazione grafica delle dimensioni di minaccia, conseguenza e vulnerabilità nei sistemi AI.](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design_82hD9RQI.png)

# Valutazione dei Rischi nella IA Generativa

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 25 Febbraio 202512 Marzo 2025

Questo articolo fa parte di una [serie](https://www.ictsecuritymagazine.com/articoli/intelligenza-artificiale-generativa/) dedicata al tema della IA Generativa, concentrandosi specificatamente sulla comprensione e valutazione dei rischi associati ai sistemi di Generative AI. Il testo esplora un framework analitico per la gestione del rischio dell’AI, attingendo alle metodologie consolidate nel campo della sicurezza informatica e introducendo prospettive innovative per comprendere le sfide uniche poste dai moderni sistemi di intelligenza artificiale.

## Rischi dei Sistemi di IA Generativa

I sistemi di Generative Artifical Intelligence (GenIA) pongono nuovi tipi di rischi, diversi dai classici rischi informatici, molti dei quali sono consequenziali e poco noti. Nonostante ciò, stiamo assistendo a una forte crescita dell’implementazione e diffusione di nuovi sistemi basati sulla GenAI in qualsiasi ambito sociale e lavorativo. Questa criticità ha, di fatto, accelerato la ricerca e lo sviluppo di modelli efficaci per realizzare il test e la valutazione dei sistemi di AI.

In questo paragrafo proviamo a descrivere un framework per la gestione del rischio dell’AI seguendo il modello del rischio informatico. Nello specifico, sono illustrate alcune potenziali strategie per inquadrare le attività di T&E sulla base di un approccio olistico al rischio dell’AI. È opportuno basare lo sviluppo di questo framework sulle lezioni apprese nei decenni di ricerca per individuare soluzioni analoghe già implementate per la modellazione e la valutazione del rischio informatico. Le valutazioni del rischio informatico sono imperfette e continuano a evolversi, ma, comunque, forniscono vantaggi significativi, tant’è che sono divenute un obbligo normativo nei contesti delle infrastrutture critiche, nel settore finanziario, nell’ambito dei servizi pubblici essenziali, ecc.

La modellazione e la valutazione del rischio per l’AI sono poco comprese sia dal punto di vista tecnico, che legale; esiste, comunque, una domanda urgente sia da parte degli utilizzatori, che dei fornitori[[1]](#_ftn1). A riguardo, nel luglio del 2024 la Coalition for Secure AI[[2]](#_ftn2) ha fornito un importante contributo a far avanzare le norme del settore relative al miglioramento della sicurezza delle moderne implementazioni dell’AI. Il NIST AI *Risk Management Framework* (RMF) è un primo esempio di questo apporto. Ad oggi, le metodologie proposte sono ancora in fase di sviluppo, con costi e benefici incerti; pertanto, le valutazioni del rischio dell’AI risultano meno applicate rispetto alle valutazioni del rischio informatico.

La modellazione e la valutazione del rischio sono importanti non solo per effettuare il T&E, ma anche per informare i processi di progettazione, come sta avvenendo nell’ingegneria della sicurezza informatica e nell’emergente ingegneria dell’AI. È importante ricordare che l’ingegneria dell’AI non comprende solo i singoli elementi dell’AI incorporati nei sistemi, ma anche la progettazione complessiva di sistemi resilienti basati sull’AI, insieme ai *workflow* e alle interazioni umane che consentono le attività operative.

La modellazione del rischio dell’AI può avere un’influenza positiva non solo nella fase di T&E, ma durante l’intero ciclo di vita dell’AI, che va dalle scelte di progettazione alle specifiche fasi di mitigazione del rischio. I punti deboli e le vulnerabilità correlate all’AI hanno caratteristiche uniche (vd. gli esempi nel paragrafo precedente), ma si sovrappongono anche ai rischi informatici. Dopotutto, gli elementi di sistema dell’AI sono componenti software, quindi presentano vulnerabilità non correlate alla loro funzionalità di AI. Tuttavia, le loro caratteristiche uniche e spesso non note, sia all’interno dei modelli, che nelle strutture software che le ospitano, possono renderli particolarmente attraenti per i cybercriminali.

### Attributi Funzionali e Qualitativi della IA Generativa

Le valutazioni funzionali e qualitative contribuiscono a garantire che i sistemi svolgano le attività in maniera corretta e affidabile. Tuttavia, correttezza e affidabilità non sono concetti assoluti, ma devono essere inquadrati nel contesto degli obiettivi specifici di un componente o di un sistema, compresi i limiti operativi che devono essere rispettati. Le specifiche comprendono necessariamente sia la funzionalità, ossia ciò che il sistema è destinato a realizzare, sia le qualità del sistema, ovvero il modo in cui il sistema intende funzionare. inclusi gli attributi relativi alla sicurezza e all’affidabilità. Queste peculiarità, o specifiche di sistema, possono riguardare sia il sistema che il suo ruolo nell’operatività, comprese le aspettative relative a fattori di stress da minacce avverse.

I sistemi basati sull’intelligenza artificiale presentano rilevanti sfide tecniche in ognuno dei seguenti aspetti: dalla formulazione delle spe...