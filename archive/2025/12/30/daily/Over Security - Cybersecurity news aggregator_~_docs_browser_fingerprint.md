---
title: ~/docs/browser_fingerprint
url: https://blog.lobsec.com/2025/12/analisi-tecnica-browser-fingerprinting-webgl/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-30
fetch_date: 2025-12-31T03:25:28.447359
---

# ~/docs/browser_fingerprint

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)
* [GPG](https://blog.lobsec.com/gpg/)

# ~/docs/browser\_fingerprint

2025-12-30 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

## Prefazione

Nel panorama moderno della cybersecurity, l’identificazione univoca di un client è diventata una sfida tra guardie e ladri. Mentre i meccanismi di persistenza tradizionali (Cookie, IDFA, LocalStorage) vengono progressivamente castrati dalle policy dei browser e dalle normative sulla privacy, il **Browser Fingerprinting** emerge come la tecnica regina per il tracciamento stateless.

In questo articolo analizzeremo come questa tecnica possa essere armata da potenziali attaccanti e come le tecnologie di “anti-detect” tentino di contrastarla.

![](https://blog.lobsec.com/wp-content/uploads/2025/12/image-9.png)

## Concetti base

Il **browser fingerprinting** è una tecnica di tracciamento “stateless” che non si affida alla memorizzazione di dati sul lato client (come i cookie o il LocalStorage), ma sulla raccolta di attributi di configurazione del browser e del sistema operativo per creare un identificatore unico (o quasi unico).

## Come funziona: La superficie di attacco

Il principio si basa sull’entropia: più informazioni riusciamo a estrarre, più il profilo diventa univoco. Le macro-aree di raccolta includono:

* **Attributi Standard:** HTTP Headers (User-Agent, Accept-Language), fuso orario, risoluzione dello schermo, profondità del colore.
* **Enumerazione delle Risorse:** Elenco dei font installati, plugin (ormai meno rilevante post-Flash), estensioni del browser e tipi MIME supportati.
* **Hardware Fingerprinting (API Web):**
  + **Canvas Fingerprinting:** Il browser deve renderizzare una stringa di testo o una forma geometrica nascosta. A causa delle variazioni nei driver video e nell’anti-aliasing a livello hardware, il pixel-map risultante varia tra diverse macchine.
  + **AudioContext Fingerprinting:** Viene generata un’onda sinusoidale o applicato un filtro audio; le variazioni nel modo in cui lo stack audio elabora il segnale producono un’impronta distintiva.
  + **WebGL:** Informazioni dettagliate sulla GPU e sulle capacità di rendering 3D.
  + **Battery Status API:** (Sebbene limitata di recente) può fornire dati sui cicli di ricarica.
  + **Network Info:** Indirizzi IP locali (tramite WebRTC leak), latenza e throughput.

## Contesti d’uso: Dual-use Technology

Come molte tecnologie di sicurezza, il fingerprinting è un’arma a doppio taglio:

### Anti-Frode e Sicurezza (Il lato “buono”)

* **Account Takeover (ATO) Prevention:** Se un utente accede solitamente con un fingerprint specifico e improvvisamente il profilo cambia radicalmente (nuovo OS, nuovi font, diversa risoluzione), il sistema può triggerare un’autenticazione a due fattori (2FA) aggiuntiva.
* **Bot Detection:** Gli scraper e i bot spesso usano browser headless (come Puppeteer o Playwright). Sebbene possano camuffare lo User-Agent, spesso falliscono nel replicare perfettamente le risposte di un Canvas o la coerenza tra i parametri hardware dichiarati.
* **Prevention of Ad Fraud:** Identificare click-farm che tentano di simulare migliaia di utenti unici partendo dalla stessa infrastruttura virtualizzata.

### Tracciamento e Marketing (Il lato “oscuro”)

* **Cross-site Tracking:** Poiché il fingerprint non può essere “cancellato” come un cookie, permette di tracciare un utente anche dopo che ha pulito la cache o se naviga in modalità incognito.
* **Shadow Profiling:** Creazione di profili persistenti di utenti che non hanno mai prestato il consenso esplicito al tracciamento, eludendo le normative come il GDPR (sebbene legalmente sia una zona molto grigia).

## La Superficie di Attacco: Estrazione di Entropia

Il fingerprinting non è un singolo exploit, ma un processo di aggregazione di dati. L’obiettivo è massimizzare l’entropia combinando attributi che, presi singolarmente, sembrano banali.

### 1. Hardware-Level Fingerprinting

Gli attaccanti sfruttano le API standard per inferire le specifiche fisiche della macchina:

* **Canvas & WebGL Rendering:** Forzando il rendering di un frame complesso, l’attaccante può identificare il modello di GPU e la versione del driver. Differenze microscopiche nell’anti-aliasing dei font o nella rasterizzazione dei pixel creano un hash quasi univoco.
* **AudioContext Fingerprinting:** Elaborando segnali audio nel browser, è possibile mappare come il processore e la scheda audio gestiscono i calcoli in virgola mobile, rivelando sottili discrepanze hardware.

### 2. Enumerazione e Side-Channel

* **Font Enumeration:** Misurare la larghezza e l’altezza di stringhe di testo renderizzate con diversi font “fallback” permette di mappare l’intero set di caratteri installati nel sistema.
* **Clock Skew & Drift:** Analizzando la micro-deriva temporale dell’orologio di sistema rispetto a un server NTP, è possibile distinguere due macchine identiche sulla stessa rete.

## Il Fingerprinting come Vettore di Attacco

Mentre il marketing usa il fingerprinting per il tracking, un attaccante (o un attore malevolo sofisticato) lo utilizza per scopi più insidiosi:

### Reconnaissance e Targeted Exploitation

Un fingerprint dettagliato permette di mappare con precisione lo stack software della vittima. Se un attaccante rileva una specifica versione di un plugin o un particolare set di font associato a software vulnerabile, può personalizzare il payload (ad esempio un exploit per il motore JavaScript V8) aumentando il tasso di successo e riducendo il rischio di rilevamento da parte degli EDR.

### Session Hijacking e Bypass di Anti-Frode

Molti sistemi di banking online usano il fingerprinting come “secondo fattore invisibile”. Un attaccante che riesce a esfiltrare il profilo di fingerprinting della vittima può tentare di **emulare** esattamente quel profilo (User-Agent, risoluzione, GPU, set di font) per far apparire la propria sessione come “conosciuta” al sistema di prevenzione frodi, facilitando il takeover dell’account.

### Tracking di Utenti sotto VPN/Tor

Il fingerprinting è il principale nemico dell’anonimato di rete. Anche se un bersaglio cambia IP tramite VPN o rete Tor, il fingerprint rimane costante, permettendo a un attaccante (o a un ente di sorveglianza) di correlare attività diverse allo stesso individuo.

## Difesa e Contromisure: Canvas Poisoning

Per contrastare il tracciamento basato su Canvas, la tecnica più efficace è il **Canvas Poisoning**.

Invece di bloccare del tutto il rendering (cosa che renderebbe il browser “sospetto” e facilmente identificabile), le estensioni di sicurezza o i browser orientati alla privacy iniettano del rumore (noise) nei dati dei pixel. Ogni volta che un sito richiede il `toDataURL()` di un canvas, il browser restituisce una versione leggermente alterata in modo casuale.

* **Risultato:** L’hash risultante è diverso a ogni sessione o a ogni richiesta, rendendo l’impronta digitale instabile e quindi inutile per il tracciamento a lungo termine.

## Browser Anti-Detect: L’Evoluzione del Camuffamento

Per i professionisti che necessitano di gestire più identità digitali senza correlazione (es. attività di OSINT o penetration testing), sono nati i **Browser Anti-Detect** (come *Multilogin*, *AdsPower* o *GoLogin*).

A differenza di un browser standard con estensioni, questi software:

1. **Isolamento Totale:** Creano istanze separate con profili hardware unici e persistenti.
2. **Spoofing Nativo:** Non si limitano a nascondere i dati, ma modificano il codice sorgente del browser (spesso basato su Chromium) per restituire valori hardware “reali ma diversi” (es. una diversa architettura della CPU o un diverso ID della GPU) in modo coerente su tutte le API.
3. **Gestione dei WebRTC:** Impediscono i leak de...