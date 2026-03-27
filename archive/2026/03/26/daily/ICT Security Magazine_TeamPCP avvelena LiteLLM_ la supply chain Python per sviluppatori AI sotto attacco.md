---
title: TeamPCP avvelena LiteLLM: la supply chain Python per sviluppatori AI sotto attacco
url: https://www.ictsecuritymagazine.com/notizie/litellm-supply-chain/
source: ICT Security Magazine
date: 2026-03-26
fetch_date: 2026-03-27T04:33:34.443242
---

# TeamPCP avvelena LiteLLM: la supply chain Python per sviluppatori AI sotto attacco

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

![TeamPCP avvelena LiteLLM la supply chain Python per sviluppatori AI sotto attacco](https://www.ictsecuritymagazine.com/wp-content/uploads/TeamPCP-avvelena-LiteLLM-la-supply-chain-Python-per-sviluppatori-AI-sotto-attacco.png)

# TeamPCP avvelena LiteLLM: la supply chain Python per sviluppatori AI sotto attacco

A cura di:[Redazione](#molongui-disabled-link)  Ore 26 Marzo 2026

Il 24 marzo 2026 due versioni compromesse di LiteLLM, la libreria Python più utilizzata per integrare modelli di linguaggio AI, sono state pubblicate su PyPI contenendo un malware sofisticato capace di rubare chiavi SSH, credenziali cloud, token Kubernetes e wallet crypto. Con 95 milioni di download mensili e una presenza nel 36% degli ambienti cloud globali, la portata potenziale dell’attacco è devastante. Dietro l’operazione il gruppo TeamPCP, al termine di una campagna coordinata durata quasi un mese.

## Cosa è LiteLLM e perché conta

[LiteLLM](https://www.comet.com/site/blog/litellm-supply-chain-attack/) è la libreria Python che alimenta quasi ogni framework AI agent esistente: un’interfaccia unificata che consente alle applicazioni di comunicare con OpenAI, Anthropic, Google e decine di altri provider LLM attraverso un unico wrapper. Con oltre 40.000 stelle su GitHub e dipendenze dirette da progetti come CrewAI, DSPy, Mem0, Guardrails e Camel-AI, LiteLLM non è un semplice strumento: è l’infrastruttura portante dello sviluppo AI moderno. Come abbiamo approfondito analizzando i [rischi delle dipendenze open source](https://www.ictsecuritymagazine.com/notizie/dipendenze-open-source-best-practices-per-gli-sviluppatori/), colpire una singola libreria critica significa colpire tutto ciò che ci sta sopra.

#### L’attacco: quasi un mese di campagna sistematica

[L’operazione non è nata il 24 marzo](https://blog.dreamfactory.com/the-litellm-supply-chain-attack-a-complete-technical-breakdown-of-what-happened-who-is-affected-and-what-comes-next/): è l’atto finale di una campagna coordinata iniziata il 28 febbraio 2026, quando un bot autonomo ha sfruttato una vulnerabilità di workflow in Trivy rubando un Personal Access Token. Come documentato su ICT Security Magazine, i [supply chain attack](https://www.ictsecuritymagazine.com/articoli/supply-chain-attack-minaccia-invisibile-alla-sicurezza-informatica/) sfruttano la fiducia tra un’azienda e i suoi fornitori per colpire molteplici obiettivi attraverso un singolo punto di ingresso. La progressione in questo caso è stata deliberata e sistematica:

**28 febbraio:** bot automatico compromette Trivy per la prima volta, rubando un PAT. Aqua Security rimedia i danni superficiali, ma lascia un accesso residuo che TeamPCP sfrutterà settimane dopo.

**19 marzo:** [TeamPCP torna su Trivy](https://threatlabsnews.xcitium.com/blog/litellm-supply-chain-breach-how-a-compromised-scanner-delivered-a-backdoor/) con un nuovo attacco, iniettando malware in 76 dei 77 tag di release di aquasecurity/trivy-action e tutti e 7 i tag di aquasecurity/setup-trivy. Viene pubblicato anche un binario Trivy compromesso (v0.69.4). All’incidente viene assegnato il CVE-2026-33634 con CVSS score 9.4.

**21-23 marzo:** [TeamPCP colpisce Checkmarx](https://www.helpnetsecurity.com/2026/03/25/teampcp-supply-chain-attacks/), compromettendo le GitHub Actions KICS e ast-github-action, oltre alle estensioni OpenVSX cx-dev-assist 1.7.0 e ast-results, usando credenziali rubate nella compromissione di Trivy.

**24 marzo, ore 10:39 UTC:** [LiteLLM versione 1.82.7 viene pubblicata su PyPI](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/), seguita dalla versione 1.82.8 alle 10:52 UTC. I pacchetti rimangono disponibili per alcune ore prima che PyPI li metta in quarantena. Con 3,4 milioni di download giornalieri il danno potenziale è enorme.

Il meccanismo di accesso è stato preciso: [la pipeline CI/CD di LiteLLM usava Trivy per le scansioni di sicurezza senza pinnare la versione](https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/). Il Trivy compromesso ha esfiltrato il token PYPI\_PUBLISH del progetto dall’ambiente GitHub Actions runner. Con quella credenziale, TeamPCP ha pubblicato direttamente i pacchetti malevoli su PyPI, bypassando completamente il repository GitHub: nessun tag, nessuna pull request, nessuna review.

#### Il payload: tre stadi, cifratura RSA-4096

[Il malware funziona in tre fasi distinte](https://www.bleepingcomputer.com/news/security/popular-litellm-pypi-package-compromised-in-teampcp-supply-chain-attack/), con un livello di sofisticazione che va oltre la media del cybercrime ordinario:

**Fase 1: Furto massivo di credenziali.** Il codice raccoglie tutto ciò che trova sul sistema: chiavi SSH, variabili d’ambiente, credenziali AWS, GCP e Azure, configurazioni Kubernetes, password di database, file .gitconfig, cronologia della shell e wallet di criptovaluta. I dati vengono cifrati con AES-256-CBC, con la chiave a sua volta cifrata con una chiave RSA-4096 pubblica hardcoded, e inviati all’attaccante in un archivio denominato tpcp.tar.gz.

**Fase 2: Lateral movement Kubernetes.** Se vengono rilevati token di service account Kubernetes, il malware tenta di creare pod privilegiati nel namespace kube-system, leggendo tutti i segreti del cluste...