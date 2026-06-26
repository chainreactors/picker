---
title: Le due facce dello stesso rischio CI/CD: Cordyceps e la falla agentica di Claude Code
url: https://www.ictsecuritymagazine.com/notizie/due-facce-rischio-cicd-cordyceps-claude-code/
source: ICT Security Magazine
date: 2026-06-25
fetch_date: 2026-06-26T06:09:34.683055
---

# Le due facce dello stesso rischio CI/CD: Cordyceps e la falla agentica di Claude Code

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![rischio CICD Cordyceps e la falla agentica di Claude Code](https://www.ictsecuritymagazine.com/wp-content/uploads/rischio-CICD-Cordyceps-e-la-falla-agentica-di-Claude-Code.png)

# Le due facce dello stesso rischio CI/CD: Cordyceps e la falla agentica di Claude Code

A cura di:[Redazione](#molongui-disabled-link)  Ore 25 Giugno 202625 Giugno 2026

La sicurezza CI/CD ha due facce, e due ricerche pubblicate a poche settimane di distanza le raccontano da angolazioni opposte come un’unica storia. C’è *Cordyceps*, la classe di vulnerabilità nei *workflow* CI/CD che colpisce oltre 300 repository GitHub pienamente sfruttabili, con riscontri confermati su progetti di Microsoft, Google, Apache e Cloudflare. E c’è la falla individuata nella GitHub Action di Claude Code, in cui un agente di intelligenza artificiale viene convinto a leggere e a far uscire i segreti del *runner*. Tecnicamente sono fenomeni diversi: una composizione insicura di automazioni deterministiche, l’altra un *prompt injection* contro un agente. La radice, però, è identica, e capirla conta più di entrambi i singoli casi.

## La radice comune della sicurezza CI/CD: il workflow è codice

Il punto di partenza è una svista concettuale diffusa: trattare i file di automazione (gli *YAML* di GitHub Actions e i loro equivalenti) come semplice configurazione, e non come codice critico per la sicurezza. Questi *workflow* eseguono comandi di shell, custodiscono chiavi di firma, si autenticano verso i cloud provider e pubblicano release. In mezzo c’è sempre un confine di fiducia: input che arriva dall’esterno (una *pull request*, un commento, il corpo di una *issue*) e automazioni che girano con permessi elevati e accesso ai segreti. Quando quel confine non e’ presidiato, l’input non attendibile attraversa la barriera e raggiunge ciò che dovrebbe restargli precluso. *Cordyceps* e la falla di Claude Code sono due modi diversi di far attraversare quel confine alla stessa cosa sbagliata.

## Prima faccia: Cordyceps, la composizione insicura

Nella [ricerca di Novee](https://novee.security/blog/cordyceps/) pubblicata il 23 giugno il problema non è un bug puntuale con un CVE, è un pattern sistemico: configurazioni che concedono alle *pull request* più permessi del dovuto, così che una richiesta non attendibile attiva *workflow* privilegiati. Le catene più pericolose sono multi-step: un *workflow* a basso privilegio passa il proprio output a uno ad alto privilegio, il cui *token* si autentica al cloud con il ruolo più elevato (
`roles/owner`
su GCP, in uno dei casi confermati). Nessun passaggio, isolato, sembra pericoloso; la vulnerabilità vive solo nella composizione. Su circa 30.000 repository scansionati, Novee ne ha segnalati 654 in una singola passata e ne ha confermati oltre 300 pienamente sfruttabili, con un dettaglio dirimente: si tratta di sfruttabilità provata con *proof of concept* in laboratorio, non di abusi osservati in rete. E’ la stessa logica che ICT Security Magazine ha già documentato con l’[attacco a LiteLLM](https://www.ictsecuritymagazine.com/articoli/supply-chain-software-litellm/), dove uno scanner di sicurezza compromesso in GitHub Actions è diventato il punto di ingresso alla *supply chain*.

Un tratto rende *Cordyceps* particolarmente insidioso: l’exploit non richiede un account privilegiato. Secondo Novee basta un utente anonimo con un profilo gratuito per forgiare approvazioni, iniettare codice o sottrarre credenziali.

## Seconda faccia: l’agente che legge troppo

Il secondo caso aggiunge un attore nuovo dentro la pipeline: un agente AI che interpreta testo. La GitHub Action di Claude Code esegue Claude dentro il *runner* di CI per smistare *issue*, applicare etichette e revisionare *pull request*, e per impostazione predefinita dispone di accesso in lettura e scrittura a codice, *issue*, *pull request* e file di *workflow*. La [ricerca di GMO Flatt](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) firmata da RyotaK ha mostrato come una singola *issue* malevola, sfruttando un *prompt injection* indiretto, possa indurre l’agente a leggere
`/proc/self/environ`
e a riscrivere i valori nella *issue* stessa, dove l’attaccante li raccoglie. Il bottino più prezioso non e’ la chiave API in sé: sono le credenziali con cui il *workflow* richiede il *token* OIDC, che Claude Code scambia con il backend di Anthropic per un *token* di installazione della GitHub App con permessi di scrittura, fino al controllo del repository. Poichè lo stesso *workflow* girava anche sul repository ufficiale dell’azione, un attacco riuscito avrebbe potuto iniettare codice nell’azione stessa, con effetto a cascata su tutti i progetti a valle.

La [analisi di Microsoft](https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/) Threat Intelligence, pubblicata il 5 giugno, ha messo a fuoco il dettaglio architetturale: lo strumento *Read* non era soggetto allo stesso *sandboxing* applicato all’esecuzione via *Bash*, e poteva quindi leggere
`/proc/self/environ`
e ricavarne
`ANTHROPIC_API_KEY`
. Per aggirare i filtri di sicurezza del modello e il *...