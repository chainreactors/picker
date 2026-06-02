---
title: No Human at the Keyboard: Agentic AI e la nuova frontiera del cybercrime
url: https://www.ictsecuritymagazine.com/articoli/agentic-ai-cybercrime/
source: ICT Security Magazine
date: 2026-06-01
fetch_date: 2026-06-02T06:32:54.721521
---

# No Human at the Keyboard: Agentic AI e la nuova frontiera del cybercrime

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Agentic AI e cybercrime: l'intervento di John Sotiropoulos (OWASP) alla Cyber Crime Conference su prompt injection, MCP, identità agentica e forensics by design](https://www.ictsecuritymagazine.com/wp-content/uploads/DSC_2610-scaled.jpg)

# No Human at the Keyboard: Agentic AI e la nuova frontiera del cybercrime

A cura di:[Redazione](#molongui-disabled-link)  Ore 1 Giugno 202625 Maggio 2026

*Intervento di John Sotiropoulos (OWASP GenAI Security Project, Deep Cyber Ltd.), 1[4ª Cyber Crime Conference](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026), Roma, 6-7 maggio 2026*

Per trent’anni il *cybercrime* è stato un uomo, o una donna, davanti a una tastiera. L’AI *agentic* cambia l’equazione perché introduce un ingrediente nuovo, l’autonomia azionabile: non si automatizza più un compito, si delega *agency* e identità a un sistema che agisce nel nostro nome. Attorno a questo punto di svolta ha costruito il proprio intervento John Sotiropoulos, Board Director dell’[OWASP GenAI Security Project](https://genai.owasp.org/) e Co-Lead della [*Agentic Security Initiative*](https://genai.owasp.org/initiatives/agentic-security-initiative/), che alla 14ª Cyber Crime Conference ha aperto la sessione pomeridiana del primo giorno dedicata al rapporto fra intelligenza artificiale generativa e crimine informatico.

Sotiropoulos, autore della *UK Implementation Guide* per il *Cyber Security Code of Practice* (oggi standard globale ETSI EN 304 223 e TR 104 128) e Chair della *Top 10 for Agentic Applications*, ha strutturato il proprio intervento come una pièce in quattro atti: un caso clinico fittizio ma plausibile, l’inquadramento dell’*agentic crime*, il nodo dell’identità degli agenti, le contromisure operative. Il filo che attraversa l’intero discorso è una tesi netta: «la sicurezza non basta più; serve anche la *forensics by design*».

## Atto I. Un venerdì pomeriggio in uno studio medico di Londra

Lo scenario di apertura è una *composite story* tratta dall’*Healthcare Agentic Pack* presentato da Deep Cyber al *workshop* CSIT/OWASP dell’aprile 2026. La protagonista è la dottoressa K, medico di base in uno studio londinese con quattordici colleghi. Sono le quattro del pomeriggio di un venerdì, ha già completato ventotto consultazioni e ha un ultimo *eConsult* da evadere, una di quelle richieste asincrone via email che il sistema sanitario britannico utilizza quando non è possibile fissare un appuntamento. Il paziente lamenta mal di schiena. La dottoressa chiede al *copilot* integrato nel software di studio una bozza di prescrizione basata sulla storia clinica del paziente. Il *copilot* indicizza la casella, redige il documento, lei firma.

Tre settimane dopo, il General Medical Council apre un’inchiesta. Il farmaco prescritto era tramadol, sostanza controllata. La storia clinica citata, però, non era mai esistita: il paziente aveva nascosto nell’*eConsult* un’istruzione testuale formattata in carattere a dimensione 0,1, leggibile dal modello ma invisibile all’occhio umano. Nessuna competenza tecnica richiesta, nessun avviso del *copilot*. L’*audit log* dello studio registra un solo nome, quello della dottoressa K.

Tre attori, due umani e un agente, hanno concorso a quella prescrizione. Il sistema ne riconosce uno solo. È, in miniatura, l’intero problema dell’AI *agentic*.

![Agentic AI e cybercrime: l'intervento di John Sotiropoulos (OWASP) alla Cyber Crime Conference su prompt injection, MCP, identità agentica e forensics by design](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_e8XicWpoqA-700x393.png)

*John Sotiropoulos (OWASP GenAI Security Project, Deep Cyber Ltd.), Cyber Crime Conference 2026*

## Atto II. Agentic AI e cybercrime

##### Il punto di inflessione

La traiettoria è ormai chiara. La *predictive AI* ci ha dato modelli analitici, riconoscimento di *pattern*, *risk scoring*. La *generative AI* ha portato capacità di redazione, sintesi, generazione di codice e contenuti in linguaggio quasi umano. L’AI *agentic* aggiunge l’ingrediente decisivo, l’autonomia operativa: un agente decide, sceglie strumenti, li orchestra, scompone obiettivi, coordina altri agenti. Non stiamo automatizzando compiti, ha insistito Sotiropoulos: stiamo delegando *agency* e identità a sistemi che operano in nostro nome. Sono le due parole chiave dell’intera relazione.

##### La OWASP Top 10 for Agentic Applications

Per dare un linguaggio condiviso a questi rischi, l’OWASP GenAI Security Project ha rilasciato a dicembre la prima *Top 10* dedicata alle applicazioni *agentic*. Le dieci categorie, costruite in *open peer review* con il contributo di esperti a livello globale e validate anche da agenzie *cyber* nazionali, coprono l’intero perimetro: *Agent Goal Hijack* (ASI01), *Tool Misuse & Exploitation* (ASI02), *Identity & Privilege Abuse* (ASI03), *Agentic Supply Chain Vulnerabilities* (ASI04), *Unexpected Code Execution* (ASI05), *Memory & Context Injection* (ASI06), *Insecure Inter-Agent Communication* (ASI07), *Cascading Failures* (ASI08), *Human-Agent Trust Exploitation* (ASI09), *Rogue Agents* (ASI10). Quello che è capitato alla dottoressa K è classificabile come ASI01 supportato da ASI03.

##### Quando l’agente diventa il payload: il caso GitHub Copi...