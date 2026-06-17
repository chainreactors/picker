---
title: SearchLeak: un solo clic trasformava Microsoft 365 Copilot in uno strumento di esfiltrazione
url: https://www.ictsecuritymagazine.com/notizie/searchleak-microsoft-365-copilot-cve-2026-42824/
source: ICT Security Magazine
date: 2026-06-16
fetch_date: 2026-06-17T07:04:02.373023
---

# SearchLeak: un solo clic trasformava Microsoft 365 Copilot in uno strumento di esfiltrazione

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

![SearchLeak un solo clic trasformava Microsoft 365 Copilot in uno strumento di esfiltrazione](https://www.ictsecuritymagazine.com/wp-content/uploads/SearchLeak-un-solo-clic-trasformava-Microsoft-365-Copilot-in-uno-strumento-di-esfiltrazione.png)

# SearchLeak: un solo clic trasformava Microsoft 365 Copilot in uno strumento di esfiltrazione

A cura di:[Redazione](#molongui-disabled-link)  Ore 16 Giugno 202616 Giugno 2026

I ricercatori di Varonis Threat Labs hanno [dimostrato](https://www.varonis.com/blog/searchleak) come un singolo clic su un link ospitato su un dominio Microsoft autentico potesse trasformare *Microsoft 365 Copilot Enterprise Search* in un canale di furto dati silenzioso. La catena di attacco, battezzata *SearchLeak*, è stata corretta da Microsoft sul proprio backend e identificata come [CVE-2026-42824](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42824), classificata critica dal vendor. Non c’è quindi alcuna azione di *patching* richiesta ai clienti, ma il caso ridefinisce il modello di minaccia degli [assistenti AI](https://www.ictsecuritymagazine.com/articoli/intelligenza-artificiale/) in ambito *enterprise* e merita attenzione strategica.

La dinamica è quella che gli analisti iniziano a riconoscere come ricorrente: la *prompt injection* riapre classi di vulnerabilità web che si davano per superate. *SearchLeak* impila infatti una debolezza specifica dell’AI su due bug classici, e ogni anello serve al successivo.

## Tre bug, un clic

Il punto di ingresso è il parametro **q** nell’URL di Copilot Enterprise Search, pensato per ospitare una query in linguaggio naturale. Copilot però interpreta quel contenuto come istruzioni, non come semplice stringa di ricerca: Varonis chiama questa tecnica *parameter-to-prompt injection*. Un attaccante costruisce un URL che ordina a Copilot di cercare nella casella di posta, prelevare il titolo di un’email e collocarlo dentro l’URL di un’immagine. La vittima non digita nulla; clicca, e l’assistente esegue.

Il secondo anello è una *race condition* nel rendering della risposta. Il *guardrail* di Microsoft incapsula l’output di Copilot in blocchi di codice perché il browser lo tratti come testo, ma la sanitizzazione avviene dopo la generazione, mentre il browser disegna lo *streaming* man mano che arriva. Il tag **img** iniettato viene quindi reso, e invia la sua richiesta, prima che il filtro entri in azione.

Il terzo anello supera la *Content Security Policy* della pagina. La *CSP* su m365.cloud.microsoft blocca le immagini da domini arbitrari, ma include in *allowlist* \*.bing.com. L’endpoint Search by Image di Bing accetta l’URL di un’immagine e lo recupera lato server: puntando quel recupero verso il server dell’attaccante, con il testo rubato codificato nel percorso, Bing diventa il proxy di esfiltrazione e la *CSP* non si applica mai, perché la richiesta parte dall’infrastruttura di Bing.

## Cosa ottiene un attaccante

Copilot Enterprise può raggiungere tutto ciò a cui accede l’utente autenticato, attraverso il suo accesso a Microsoft Graph, e l’attaccante eredita quella portata senza mai effettuare il *login*. Il bottino più sensibile al tempo è nella posta: codici monouso, codici *MFA* e link di reset password, spesso ancora validi per pochi minuti, sufficienti a prendere il controllo di un account prima che qualcuno se ne accorga. Lo stesso accesso arriva a inviti del calendario, note di riunione e qualsiasi file SharePoint o OneDrive indicizzato da Copilot, dove vivono dati salariali, cifre di bilancio e piani di acquisizione.

Va precisato, per correttezza: Microsoft cataloga formalmente la falla come *M365 Copilot Information Disclosure Vulnerability*, tecnicamente una *command injection* (neutralizzazione impropria di elementi speciali usati in un comando). I punteggi *CVSS* divergono, 6,5 secondo Microsoft e 7,5 secondo il [National Vulnerability Database](https://nvd.nist.gov/vuln/detail/CVE-2026-42824), e Varonis ha presentato una *proof-of-concept*, non uno sfruttamento osservato in the wild. La coesistenza dell’etichetta “critical” con un base score di 6,5 non è una contraddizione: la prima appartiene alla *severity* proprietaria del vendor, il secondo ricade in fascia “Medium” sulla scala *CVSS* standard. Le due metriche misurano cose diverse, e leggerle insieme è più informativo che sintetizzarle.

## Perché conta per chi difende

*SearchLeak* non è un caso isolato, anche se i precedenti non vanno appiattiti. La famiglia di problema è la stessa: la *prompt injection* riattiva classi di bug web vecchie come *SSRF* e *race* nei sanitizzatori. Cambiano però i meccanismi. *EchoLeak* (CVE-2025-32711, divulgata nel 2025 da Aim Security) era un attacco *zero-click*, innescato via email malevola con la tecnica *LLM Scope Violation* e un punteggio *CVSS* di 9,3, e non passava né dalla *SSRF* di Bing né dalla *race condition* descritta qui. *SearchLeak* è invece *one-click* via URL. Lo stesso schema *one-click* era già stato mostrato da Varonis con l’attacco *Reprompt* contro Copilot Personal, e ha retto contro Enterprise Search nonostante i *guardrail* aggiuntivi che quel livello dovrebbe imporre.

Poiché Copilo...