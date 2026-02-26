---
title: Claude Code Security crea il panico, ma… non uccide la cyber
url: https://www.securityinfo.it/2026/02/25/claude-code-security-crea-il-panico-ma-non-uccide-la-cyber/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-25
fetch_date: 2026-02-26T04:11:56.988154
---

# Claude Code Security crea il panico, ma… non uccide la cyber

Aggiornamenti recenti Febbraio 25th, 2026 9:30 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Claude Code Security crea il panico, ma… non uccide la cyber](https://www.securityinfo.it/2026/02/25/claude-code-security-crea-il-panico-ma-non-uccide-la-cyber/)
* [Sandworm\_Mode: il “worm” della supply chain NPM](https://www.securityinfo.it/2026/02/24/sandworm_mode-il-worm-della-supply-chain-npm/)
* [Ring: una taglia a 4 zeri per forzare l’esecuzione in locale](https://www.securityinfo.it/2026/02/23/ring-una-taglia-a-4-zeri-per-forzare-lesecuzione-in-locale/)
* [Finanza nel mirino, incidenti raddoppiati nel 2025](https://www.securityinfo.it/2026/02/20/finanza-nel-mirino-incidenti-raddoppiati-nel-2025/)
* [Davvero si può fare “jailbreak” di un caccia F-35?](https://www.securityinfo.it/2026/02/18/davvero-si-puo-fare-jailbreak-a-un-caccia-f-35/)

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

## Claude Code Security crea il panico, ma… non uccide la cyber

Feb 25, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Mercato](https://www.securityinfo.it/category/news/mercato-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/02/25/claude-code-security-crea-il-panico-ma-non-uccide-la-cyber/#respond)

---

Venerdì scorso Anthropic ha presentato **Claude Code Security**, una nuova funzione che analizza intere codebase alla ricerca di vulnerabilità e propone patch correttive. Il rilascio, per ora, è in modalità **research preview limitata** per clienti enterprise e team, mentre i maintainer open source possono chiedere accesso gratuito accelerato. L’effetto immediato, però, non si è visto nei bug tracker: si è visto in Borsa, con una reazione nervosa su diversi titoli cyber e un dibattito istantaneo sul “fine dei vendor di sicurezza”.

**La “tempesta perfetta”: hype sull’AI, paura di disintermediazione e un mercato già nervoso**

Il sell-off è stato alimentato da un’idea semplice, quasi cinematografica: se un LLM può scansionare codice e suggerire fix, allora una fetta del lavoro di sicurezza potrebbe essere automatizzata e “commoditizzata”. In realtà, analisti e osservatori hanno rapidamente raffreddato la lettura apocalittica: l’AI sta entrando in modo sempre più profondo nella sicurezza, ma **non elimina i bisogni strutturali** di detection, risposta, threat intel, governance e controllo del rischio. La reazione del mercato viene descritta come un’overreaction, più legata al timing e al sentiment che a un impatto immediato sui modelli di business.

Per drammatizzare, George Kurtz (CEO di CrowdStrike) ha chiesto a Claude se il nuovo strumento potesse rimpiazzare ciò che fa la sua azienda. **La risposta del modello è stata sostanzialmente un “no”** e il punto non è l’aneddoto in sé, ma ciò che riflette: l’AI può essere molto brava su compiti delimitati, ma la sicurezza reale è un sistema socio-tecnico fatto di contesto, priorità, trade-off e responsabilità.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/BugHuntingSupport-1024x683.png)

**“500 vulnerabilità high-severity”: un claim potente, ma il diavolo è nei dettagli**

Il lancio di Claude Code Security arriva dopo che Anthropic aveva dichiarato che **Claude Opus 4.6** avrebbe individuato e validato più di 500 vulnerabilità “ad alta pericolosità” in progetti open source. È un numero che colpisce l’immaginazione, perché sposta l’immagine dalla semplice individuazione di pattern alla capacità di proporre un percorso di validazione e remediation. Ma nel mondo della sicurezza contano almeno due domande: qual è il tasso di falsi positivi e qual è il costo (in risorse e in tempo) per ottenere quei risultati. Su questo, chi lavora quotidianamente su strumenti per developer security chiede più trasparenza e metriche pubbliche.

Anthropic posiziona Claude Code Security come uno strumento **context-aware**, capace di “ragionare” sul codice in modo simile a un ricercatore umano: “comprende” interazioni tra componenti, “segue” il movimento dei dati e intercetta bug complessi che sfuggono a regole statiche. Se la promessa regge alla prova dei fatti, l’impatto pratico potrebbe essere notevole per team che gestiscono codebase ampie e stratificate, dove la vulnerabilità non è un pattern banale ma nasce da logica di business, integrazioni e condizioni limite. Resta però un punto chiave: Anthropic dice che **nessuna modifica viene applicata senza approvazione umana**.

**Non è un unicum: Amazon, Microsoft e Google stanno correndo nella stessa direzione**

Claude Code Security è la novità “più chiacchierata”, ma non è la prima tessera del mosaico. In parallelo, praticamente tutti i grandi player stanno usando agenti AI per scoprire vulnerabilità e accelerare il ciclo di patching. Google aveva già parlato di Big Sleep come strumento LLM-based per caccia ai bug e più di recente DeepMind ha presentato **CodeMender** come agente per automatizzare la creazione di patch, individuare la root cause e generare una correzione verificabile. L’AI sta diventando un moltiplicatore di produttività nella sicurezza del software e questo non è un segreto per nessuno, si applica a tutti i campi, ma non è una bacchetta magica che sostituisce processi e responsabilità.

Inoltre, il vero banco di prova non è “se trova qualche bug”, ma **se regge a scala industriale** senza esplodere in falsi positivi, rumore e patch discutibili. Isaac Evans (Semgrep) ha centrato una questione che nella narrazione mainstream viene spesso messa in secondo piano: senza statistiche pubbliche su precision/recall, falsi positivi e costi, il rischio è che parte della comunicazione sia per lo più marketing. Anche ammesso che l’AI migliori sensibilmente la discovery, rimane il processo: triage, priorità, compatibilità, regressioni e governance del cambiamento in ambienti di produzione.

**Perché “umani nel loop” non è una clausola di stile, ma un requisito di sicurezza**

Il punto non è la sfiducia verso gli LLM: è la responsabilità. Una patch proposta da un modello può essere tecnicamente corretta e allo stesso tempo **funzionalmente pericolosa**, perché sposta un controllo, rompe un’integrazione o introduce un comportamento inatteso. Inoltre, gli stessi modelli che aiutano a trovare vulnerabilità possono anche produrre codice fragile o aprire nuovi vettori, soprattutto quando diventano parte del toolchain quotidiano. L’adozione sensata passa quindi da controlli: code review, test, policy di merge, e soprattutto ownership chiara su ciò che entra in produzione.

La traiettoria più credibile è che Claude Code Security e strumenti analoghi diventino una difesa aggiuntiva: un livello che anticipa problemi, accelera remediation e ...