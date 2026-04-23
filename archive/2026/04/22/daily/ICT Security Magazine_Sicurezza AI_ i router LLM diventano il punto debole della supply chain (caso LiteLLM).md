---
title: Sicurezza AI: i router LLM diventano il punto debole della supply chain (caso LiteLLM)
url: https://www.ictsecuritymagazine.com/notizie/sicurezza-ai-router-llm/
source: ICT Security Magazine
date: 2026-04-22
fetch_date: 2026-04-23T04:44:55.081289
---

# Sicurezza AI: i router LLM diventano il punto debole della supply chain (caso LiteLLM)

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

![Sicurezza AI i router LLM diventano il punto debole della supply chain (caso LiteLLM)](https://www.ictsecuritymagazine.com/wp-content/uploads/Sicurezza-AI-i-router-LLM-diventano-il-punto-debole-della-supply-chain-caso-LiteLLM.jpeg)

# Sicurezza AI: i router LLM diventano il punto debole della supply chain (caso LiteLLM)

A cura di:[Redazione](#molongui-disabled-link)  Ore 22 Aprile 202621 Aprile 2026

*Una ricerca sistematica di UC Santa Barbara, UC San Diego, Fuzzland e World Liberty Financial ha analizzato 428 router commerciali e gratuiti, individuando intermediari che riscrivono attivamente le tool-call degli agenti di coding ed esfiltrano credenziali. L’incidente LiteLLM del marzo 2026 conferma, su scala industriale, che la minaccia non è più teorica.*

## Sicurezza AI a rischio: perché i router LLM stanno diventando il nuovo punto debole negli attacchi informatici

Ogni volta che un agente LLM, un Claude Code, un Codex o un Cursor, invia una richiesta a un provider di modelli, il traffico attraversa quasi sempre uno o più intermediari applicativi. Si chiamano router, o API gateway, e aggregano decine di provider dietro un’unica interfaccia compatibile con OpenAI. Gestiscono fallback, bilanciamento di carico e ottimizzazione dei costi; un singolo cambio di *base URL* e una nuova chiave API bastano per instradare un’intera flotta di agenti attraverso un servizio terzo.

La scelta è così banale che, in molte organizzazioni, viene presa al livello di una configurazione di sviluppo. Il fatto che, una volta puntato quel percorso, il client non abbia alcun modo di verificare crittograficamente cosa abbia davvero prodotto il modello a monte è un dettaglio che, fino a poco tempo fa, quasi nessuno ha considerato.

Un gruppo di ricercatori guidato da Hanzhi Liu (UC Santa Barbara), con Chaofan Shou (Fuzzland), Hongbo Wen (UCSB), Yanju Chen (UC San Diego), Ryan Jingyang Fang (World Liberty Financial) e Yu Feng (UCSB), ha deciso di misurarlo. Il paper [«Your Agent Is Mine»](https://arxiv.org/abs/2604.08407) (arXiv:2604.08407v1, cs.CR, 9 aprile 2026) è il primo studio sistematico sull’ecosistema dei router LLM visti come confine di fiducia della *[supply chain](https://www.ictsecuritymagazine.com/articoli/litellm-supply-chain-attack-cyber-supply-chain-ia/)* dell’IA. Il risultato è meno rassicurante del previsto.

#### Un man-in-the-middle “legittimo” nella sicurezza AI

Il modello di minaccia formalizzato dagli autori parte da un’osservazione architetturale semplice: il router, per sua natura, termina la sessione TLS lato client e ne apre una nuova verso il provider. Occupa quindi una posizione di *man-in-the-middle* applicativo non accidentale, ma intenzionalmente configurata dall’utente. Nessun *TLS downgrade*, nessuna forgery di certificati: basta che il client abbia puntato l’endpoint a quel servizio. Da lì il router vede in chiaro tool definition, prompt di sistema, chiavi API, output dei tool e, soprattutto, le tool-call che l’agente sta per eseguire. Può leggerle, trattenerle, riscriverle o fabbricarle ex novo.

La chain-integrity, notano gli autori, è una proprietà del tipo *weakest link*: in una catena di *k* hop (utente -> rivenditore -> aggregatore -> OpenRouter -> provider, tanto per restare su uno scenario realistico), un singolo router malevolo in qualunque posizione è sufficiente a compromettere l’intera traiettoria. Gli hop onesti a valle non possono né rilevare né annullare la modifica, perché non hanno alcun riferimento alla risposta originale prodotta dal provider.

##### Attacchi hacker AI: le 4 tecniche che sfruttano i router LLM

Su questa base, il team costruisce una tassonomia di quattro classi. Le due primitive di base sono **AC-1**, ovvero *response-side payload injection*, in cui il router riscrive gli argomenti JSON di una tool-call dopo che il modello ha risposto ma prima che il client la esegua, e **AC-2**, ovvero *passive secret exfiltration*, in cui il router si limita a leggere il traffico e a conservare asincronamente chiavi API, PAT GitHub, token AWS, chiavi private Ethereum, chiavi PEM.

A queste si aggiungono due varianti di evasione adattiva. **AC-1.a** (*dependency-targeted injection*) sostituisce nel comando di installazione un nome di pacchetto legittimo con un typosquat preregistrato su PyPI o npm, lasciando invariato il resto della riga di comando e ingannando così le approval UI basate sui domini. L’esempio che figura nel paper è istruttivo:
`pip install requests`
viene riscritto in
`pip install reqeusts`
, una singola lettera invertita, un pacchetto preregistrato dall’attaccante, una dipendenza che viene memorizzata nella cache locale e reimportata in ogni sessione futura.

Un foothold di supply chain durevole ottenuto in uno scambio JSON. **AC-1.b** (*conditional delivery*) attiva la riscrittura solo quando un predicato di sessione è verificato: dopo *N* richieste benigne, per client in modalità autonoma (cosiddetta YOLO, in cui l’agente esegue i tool senza chiedere conferma comando per comando), in determinate finestre orarie o per progetti scritti in linguaggi target. Il predicato vive server-side, è opaco al client, e rende strutturalmente inadeguato qualunque audit black-box di lunghezza finita.

Il punto architettura...