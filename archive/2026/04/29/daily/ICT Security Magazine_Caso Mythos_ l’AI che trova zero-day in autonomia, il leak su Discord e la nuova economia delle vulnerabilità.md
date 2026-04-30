---
title: Caso Mythos: l’AI che trova zero-day in autonomia, il leak su Discord e la nuova economia delle vulnerabilità
url: https://www.ictsecuritymagazine.com/notizie/claude-mythos-leak-discord/
source: ICT Security Magazine
date: 2026-04-29
fetch_date: 2026-04-30T05:30:22.821490
---

# Caso Mythos: l’AI che trova zero-day in autonomia, il leak su Discord e la nuova economia delle vulnerabilità

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

![Caso Mythos: l'AI che trova zero-day in autonomia, il leak su Discord e la nuova economia delle vulnerabilità - Claude Mythos trova zero-day in autonomia, leak su Discord e nuove pressioni NIS2-CRA-DORA: cosa cambia per CISO italiani dopo Project Glasswing.](https://www.ictsecuritymagazine.com/wp-content/uploads/Claude-Mythos-trova-zero-day-in-autonomia-leak-su-Discord-e-nuove-pressioni-NIS2-CRA-DORA.png)

# Caso Mythos: l’AI che trova zero-day in autonomia, il leak su Discord e la nuova economia delle vulnerabilità

A cura di:[Redazione](#molongui-disabled-link)  Ore 29 Aprile 202629 Aprile 2026

Il 7 aprile 2026 [Anthropic ha annunciato Claude Mythos](https://www.ictsecuritymagazine.com/notizie/anthropic-project-glasswing/) Preview, un modello che individua in autonomia zero-day in ogni principale sistema operativo e browser. Due settimane dopo, Bloomberg ha rivelato che un gruppo Discord aveva avuto accesso al modello fin dal giorno del lancio. Tra hype, fact-checking indipendente e l’allarme di CERT-EU, il caso ridefinisce in poche settimane il rapporto tra capacità AI offensive, disclosure coordinata e obblighi NIS2, CRA e DORA.

## Una settimana che ha cambiato il vocabolario della sicurezza

Nicholas Carlini, ricercatore di Anthropic noto per i suoi lavori sulla robustezza dei modelli, lo ha riassunto così durante il briefing di lancio: in poche settimane ha trovato più bug di quanti ne avesse scovati in tutta la carriera precedente. La frase, rilanciata dal [blog di Simon Willison](https://simonwillison.net/2026/Apr/7/project-glasswing/), cattura meglio di qualunque comunicato l’umore della comunità di ricerca dopo il 7 aprile 2026.

Quel giorno Anthropic ha pubblicato un [System Card di 244 pagine](https://red.anthropic.com/2026/mythos-preview/) per Claude Mythos Preview e, contestualmente, ha annunciato di non rendere il modello pubblicamente disponibile. È la prima volta che un laboratorio di frontiera documenta in modo esaustivo un modello dichiarando subito dopo che non lo rilascerà. Il gesto vale già come notizia.

Le ragioni sono nel post tecnico del Frontier Red Team, e non lasciano molto spazio all’ambiguità. Durante i test, Mythos Preview ha individuato e in molti casi sfruttato in autonomia zero-day in tutti i principali sistemi operativi e browser. Tra le scoperte ci sono un bug rimasto nascosto per 27 anni in OpenBSD, una falla di 16 anni in FFmpeg e una vulnerabilità di memoria in un virtual machine monitor scritto in linguaggio memory-safe.

Il caso più documentato è [CVE-2026-4747](https://www.theregister.com/2026/04/15/project_glasswing_cves/), una RCE di 17 anni nell’implementazione NFS di FreeBSD. Mythos l’ha identificata, ha costruito una catena ROP da 20 gadget distribuita su più pacchetti, e ha dimostrato che un attaccante non autenticato, da qualunque punto di Internet, può ottenere root sul bersaglio. Senza intervento umano dopo il prompt iniziale.

#### I numeri che misurano la portata

Anthropic non ha rilasciato un conteggio totale delle vulnerabilità individuate, ma ha quantificato il salto di capacità con benchmark riproducibili. Sul motore JavaScript di Firefox 147, [Claude Opus 4.6 era riuscito a sviluppare exploit funzionanti due volte su diverse centinaia di tentativi](https://red.anthropic.com/2026/mythos-preview/). Mythos Preview ne ha prodotti 181, conquistando il controllo dei registri in altri 29 casi. Sul benchmark CyberGym il punteggio è salito dal 66,6% all’[83,1%](https://www.nxcode.io/resources/news/project-glasswing-claude-mythos-zero-day-ai-cybersecurity-2026).

Più delle percentuali conta però la trasformazione qualitativa. [Help Net Security](https://www.helpnetsecurity.com/2026/04/15/anthropic-claude-mythos-ai-vulnerability-discovery/) la sintetizza in una frase: il divario fra individuare un bug e costruire un exploit funzionante, da sempre il principale freno per gli attaccanti, si è ridotto drasticamente. Un esempio per tutti: partendo da un identificativo CVE e dall’hash di un commit, Mythos ha completato lo sviluppo di un exploit funzionante in meno di un giorno e con un costo inferiore a 2.000 dollari.

Il punto, lo precisa la stessa Anthropic nella [pagina ufficiale di Project Glasswing](https://www.anthropic.com/glasswing), è che Mythos non è un modello fine-tuned per la sicurezza offensiva. Le sue capacità sono emerse come effetto collaterale di un avanzamento generale in coding, ragionamento e autonomia. Il miglioramento che lo rende più efficace nel patching lo rende, simmetricamente, più efficace nell’exploitation.

#### Project Glasswing: dodici partner e una corsa contro il tempo

La risposta operativa era pronta prima dell’annuncio. Project Glasswing, presentato lo stesso 7 aprile, riunisce dodici organizzazioni partner fondatrici (AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks, oltre ad Anthropic stessa) e un secondo cerchio di oltre quaranta enti che mantengono software critico. Vale 100 milioni di dollari in usage credit per Mythos Preview e 4 milioni in donazioni dirette a organizzazioni di sicurezza open source, di cui 2,5 milioni ad Alpha-Omega e OpenSSF tramite la Linux Foundation, e 1,5 milioni alla Apache ...