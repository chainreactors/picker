---
title: Supply chain software: cosa insegna l’attacco LiteLLM
url: https://www.ictsecuritymagazine.com/articoli/supply-chain-software-litellm/
source: ICT Security Magazine
date: 2026-05-13
fetch_date: 2026-05-14T05:47:14.643772
---

# Supply chain software: cosa insegna l’attacco LiteLLM

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

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![supply chain software LiteLLM](https://www.ictsecuritymagazine.com/wp-content/uploads/supply-chain-software-LiteLLM.jpeg)

# Supply chain software: cosa insegna l’attacco LiteLLM

A cura di:[Redazione](#molongui-disabled-link)  Ore 13 Maggio 202622 Aprile 2026

Alle 10:39 UTC del 24 marzo 2026, qualcuno ha caricato su PyPI una versione di LiteLLM che non avrebbe dovuto esistere. Non c’era nessun tag corrispondente su GitHub, nessun commit nel repository ufficiale, nessuna release note. Solo un pacchetto Python, apparentemente identico a quello che milioni di sviluppatori scaricano ogni giorno, con qualcosa di nascosto dentro.

Nel giro di tredici minuti ne è arrivata un’altra, ancora più sofisticata. Le due versioni malevole sono rimaste disponibili per meno di tre ore. È bastato.

## Supply chain software: come nasce un attacco alla fiducia nell’ecosistema open source

LiteLLM non è un pacchetto qualsiasi: è il gateway che permette alle applicazioni AI di parlare con oltre 100 provider di modelli linguistici, da OpenAI ad Anthropic, da AWS Bedrock a Google Vertex. Chi lo installa gli affida, spesso senza pensarci, le chiavi di accesso a quasi tutto. Ed è esattamente per questo che il gruppo criminale TeamPCP lo ha scelto come bersaglio nella fase 09 di una campagna che aveva già compromesso Trivy e Checkmarx nelle settimane precedenti.

La vicenda, documentata dalla [stessa BerriAI](https://docs.litellm.ai/blog/security-update-march-2026), da [Snyk](https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/), [Arctic Wolf](https://arcticwolf.com/resources/blog/teampcp-supply-chain-attack-campaign-targets-trivy-checkmarx-kics-and-litellm-potential-downstream-impact-to-additional-projects/), [Trend Micro](https://www.trendmicro.com/en_us/research/26/c/inside-litellm-supply-chain-compromise.html) e altri, è molto più di un incident report. È una radiografia del modo in cui l’ecosistema software moderno si fida dei propri strumenti, e di quanto quella fiducia possa essere sfruttata. Come ha [già riportato ICT Security Magazine](https://www.ictsecuritymagazine.com/notizie/litellm-supply-chain/), si tratta di uno degli attacchi alla supply chain AI più consequenziali e meglio documentati degli ultimi anni, e le lezioni che offre riguardano chiunque sviluppi, distribuisca o utilizzi software che dipende da pacchetti open source.

## Un attacco a cascata: da Trivy a LiteLLM

L’incidente LiteLLM non è nato isolato. Il 19 marzo 2026, alle 17:43 UTC, gli attaccanti di TeamPCP hanno riscritto i tag Git nel repository GitHub Action di trivy-action per puntare a una release malevola (v0.69.4) contenente lo stesso payload di credential harvesting e la stessa infrastruttura di esfiltrazione poi usata nelle operazioni successive.

L’attacco ha seguito lo stesso schema utilizzato per compromettere lo scanner di sicurezza Trivy di Aqua e le relative GitHub Actions il 19 marzo, e le estensioni VS Code e GitHub Actions di Checkmarx il 23 marzo. Aqua ha confermato che la compromissione è avvenuta a causa di un contenimento e remediation incompleto di un precedente attacco alla supply chain: la rotazione delle credenziali non è stata atomica e l’attaccante ha potuto utilizzare un token valido per esfiltrare i segreti appena ruotati durante la finestra di rotazione, durata alcuni giorni.

Il meccanismo è un attacco transitivo a cascata. La pipeline CI/CD di LiteLLM eseguiva Trivy come parte del proprio processo di build, scaricandolo da apt senza una versione fissata. L’action compromessa ha esfiltrato il token PYPI\_PUBLISH dall’ambiente del runner GitHub Actions.

Come ha sintetizzato Jacob Krell di Suzu Labs nella sua analisi per [ReversingLabs](https://www.reversinglabs.com/blog/teampcp-supply-chain-attack-spreads), TeamPCP non aveva bisogno di attaccare LiteLLM direttamente: aveva compromesso Trivy, uno scanner di vulnerabilità in esecuzione nella pipeline CI di LiteLLM senza version pinning. Quella singola dipendenza non gestita ha consegnato le credenziali di pubblicazione su PyPI, permettendo di inserire una backdoor in una libreria con 95 milioni di download al mese, una dipendenza, una reazione a catena, cinque ecosistemi compromessi in meno di un mese.

## La timeline esatta dell’attacco

La [fonte primaria ufficiale di LiteLLM](https://docs.litellm.ai/blog/security-update-march-2026) e la ricerca di [Snyk](https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/) permettono di ricostruire con precisione ogni fase.

Il **23 marzo 2026** viene registrato il dominio models.litellm.cloud, il server di esfiltrazione, il giorno prima dell’attacco vero e proprio. Il **24 marzo alle 10:39 UTC** viene pubblicata su PyPI la versione malevola 1.82.7, contenente il payload iniettato direttamente nel file proxy\_server.py. Tredici minuti dopo, alle **10:52 UTC**, viene pubblicata la versione 1.82.8, che introduce un meccanismo di delivery escalato tramite il file.pth. Alle **11:48 UTC**, Callum McMahon di FutureSearch apre la issue GitHub numero 24512 con la dicitura: “CRITICO: LiteLLM\_init.pth malevolo nel pacchetto PyPI LiteLLM 1.82.8, credential stealer.” Alle circa **13:38 UTC** PyPI mette in quarantena il pacchetto. Alle **15:27 UTC** i pacchetti compromess...