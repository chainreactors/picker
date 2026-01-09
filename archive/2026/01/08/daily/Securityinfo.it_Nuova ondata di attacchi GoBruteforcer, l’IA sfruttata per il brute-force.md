---
title: Nuova ondata di attacchi GoBruteforcer, l’IA sfruttata per il brute-force
url: https://www.securityinfo.it/2026/01/08/nuova-ondata-di-attacchi-gobruteforcer-lia-sfruttata-per-il-brute-force/?utm_source=rss&utm_medium=rss&utm_campaign=nuova-ondata-di-attacchi-gobruteforcer-lia-sfruttata-per-il-brute-force
source: Securityinfo.it
date: 2026-01-08
fetch_date: 2026-01-09T03:32:00.001241
---

# Nuova ondata di attacchi GoBruteforcer, l’IA sfruttata per il brute-force

Aggiornamenti recenti Gennaio 8th, 2026 3:31 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Nuova ondata di attacchi GoBruteforcer, l’IA sfruttata per il brute-force](https://www.securityinfo.it/2026/01/08/nuova-ondata-di-attacchi-gobruteforcer-lia-sfruttata-per-il-brute-force/)
* [Due estensioni Chrome hanno compromesso le chat di ChatGPT e DeepSeek](https://www.securityinfo.it/2026/01/07/due-estensioni-chrome-hanno-compromesso-le-chat-di-chatgpt-e-deepseek/)
* [Nel 2026 sempre più attacchi autonomi AI-driven e deepfake: le previsioni di sicurezza di ClearSkies](https://www.securityinfo.it/2026/01/05/nel-2026-sempre-piu-attacchi-autonomi-ai-driven-e-deepfake-le-previsioni-di-sicurezza-di-clearskies/)
* [Grave vulnerabilità nei chip Bluetooth Airoha: molti i marchi colpiti](https://www.securityinfo.it/2026/01/05/grave-vulnerabilita-nei-chip-bluetooth-airoha-molti-i-marchi-colpiti/)
* [Kaspersky: così funziona il mercato del lavoro nel dark web](https://www.securityinfo.it/2025/12/23/kaspersky-cosi-funziona-il-mercato-del-lavoro-nel-dark-web/)

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

## Nuova ondata di attacchi GoBruteforcer, l’IA sfruttata per il brute-force

Gen 08, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/01/08/nuova-ondata-di-attacchi-gobruteforcer-lia-sfruttata-per-il-brute-force/#respond)

---

I ricercatori di Check Point Research [hanno individuato](https://research.checkpoint.com/2026/inside-gobruteforcer-ai-generated-server-defaults-weak-passwords-and-crypto-focused-campaigns/) una nuova ondata di attacchi **GoBruteforcer**, una botnet modulare scritta in Go progettata per colpire server Linux esposti su internet.

Individuata per la prima volta nel 2023, nel corso del tempo la botnet si è evoluta specializzandosi in varianti sempre più sofisticate. Come suggerisce il nome, GoBruteforce sfrutta la tecnica brute-force per **forzare l’accesso a servizi critici come FTP, MySQL, PostgreSQL e phpMyAdmin**. Una volta preso il controllo, il server infetto viene arruolato nella botnet.

![GoBruteforcer](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_skcmbsskcmbsskcm.png)

La nuova ondata di attacchi preoccupa i ricercatori per via dell’efficacia dei dizionari di password utilizzati: nell’ultima campagna gli attaccanti non si stanno limitando a usare vecchi elenchi provenienti da leak, ma stanno sfruttando anche la **diffusione di configurazioni server generate da IA.**

Sempre più sistemisti si affidano infatti all’intelligenza artificiale per generare script di deployment o file Docker Compose; questi script condividono spesso username standard (come “appuser”, “myuser” o “dbadmin”) e password deboli di default che non vengono cambiate. “*I modelli linguistici di grandi dimensioni (LLM) vengono addestrati sulla stessa documentazione pubblica e sugli stessi codici di esempio. **Non sorprende quindi che spesso riproducano gli stessi esempi di configurazione con nomi utente predefiniti popolari** come appuser e myuser*” spiega il team di Check Point Research.

Se da una parte l’intelligenza artificiale abbassa la barriera d’accesso permettendo anche a persone con poca esperienza operativa di creare un database in pochi minuti, usare gli script generati a occhi chiusi comporta un uso più esteso di configurazioni standard e quindi una **proliferazione di username e password comuni.**Secondo i ricercatori della compagnia, è molto probabile che questa tendenza renda più efficaci gli attacchi GoBruteforcer.

Un altro punto critico evidenziato da Check Point è la persistenza di stack tecnologici datati come XAMPP su server Linux: questi pacchetti “tutto in uno” spesso espongono interfacce di amministrazione e server FTP con configurazioni di sicurezza minime o assenti, rendendoli bersagli ideali per l’automazione della botnet.

## La nuova campagna GoBruteforcer

Se in passato la botnet era usata in maniera generica, dall’ultima campagna osservata emerge una **chiara motivazione finanziaria.** Su uno dei server compromessi i ricercatori hanno trovato un kit di strumenti specializzati in criptovalute: uno scanner di bilancio per la rete TRON, alcune utility di “token-sweeping” per TRON e Binance Smart Chain usate per svuotare automaticamente i wallet non appena rilevano fondi e un database contenente circa 23.000 indirizzi TRON. L’analisi delle transazioni on-chain ha confermato che diversi attacchi hanno avuto successo.

![](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_ekz1qcekz1qcekz1.png)

L’accesso iniziale avviene sfruttando vulnerabilità in applicazioni web o credenziali deboli; in seguito, il malware installa un **bot IRC offuscato** che consente agli attaccanti di inviare comandi e ricevere aggiornamenti sullo stato del server. Gli attaccanti possono controllare i bot nella rete sia tramite web shell che tramite il bot IRC.

Il malware è in grado di sopravvivere al riavvio del serve e per il mascheramento utilizza tecniche di **process-masking** per nascondersi tra i processi di sistema legittimi. Terminato il setup, il server compromesso inizia a scansionare blocchi di indirizzi IP per **tentare l’accesso ad altri server e propagare l’infezione.**

“*GoBruteforcer è un esempio perfetto di come gli autori delle minacce utilizzino “bersagli facili” come tattiche apparentemente poco sofisticate (attacchi con password deboli, indirizzi IP casuali) per compromettere un gran numero di sistemi connessi a Internet con uno sforzo relativamente minimo*” sottolineano i ricercatori.

Il ritorno della botnet è un reminder importante del fatto che la sicurezza non passa solo per le patch dei software, ma anche per l’igiene delle configurazioni. Nel caso si utilizzi l’IA per generare script di configurazione, è fondamentale cambiare immediatamente ogni username e password suggeriti. È importante inoltre disabilitare l’accesso remoto root per i database e utilizzate l’autenticazione a due fattori o chiavi SSH ovunque possibile.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [botnet](https://www.securityinfo.it/tag/botnet/), [brute-force](https://www.securityinfo.it/tag/brute-force/), [Check Point Research](https://www.securityinfo.it/tag/check-point-research/), [configurazioni server](https://www.securityinfo.it/tag/configurazioni-server/), [GoBruteforcer](https://www.securityinfo.it/tag/gobruteforcer/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/)

[Due estensioni Chrome hanno compromesso le chat di ...