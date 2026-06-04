---
title: Non-Human Identity (NHI) secondo NIS2 e D.Lgs. 138/2024
url: https://www.ictsecuritymagazine.com/notizie/non-human-identity-nis2-e-d-lgs-138-2024/
source: ICT Security Magazine
date: 2026-06-03
fetch_date: 2026-06-04T06:32:08.485986
---

# Non-Human Identity (NHI) secondo NIS2 e D.Lgs. 138/2024

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

![Identità non umane secondo NIS2 e D.Lgs. 1382024](https://www.ictsecuritymagazine.com/wp-content/uploads/Identita-non-umane-secondo-NIS2-e-D.Lgs_.-1382024.png)

# Non-Human Identity (NHI) secondo NIS2 e D.Lgs. 138/2024

A cura di:[Redazione](#molongui-disabled-link)  Ore 3 Giugno 202626 Maggio 2026

Per ogni dipendente registrato a libro paga, un’organizzazione gestisce mediamente ottantadue identità digitali non umane: chiavi API, *service principal*, *OAuth grant*, certificati TLS, *secret* applicativi, account di agenti autonomi. Il dato proviene dal [CyberArk 2025](https://www.cyberark.com/resources/ebooks/2025-identity-security-landscape) Identity Security Landscape, indagine internazionale su organizzazioni pubbliche e private di almeno 500 dipendenti, ora confluita nel perimetro Palo Alto Networks.

Il rapporto ottantadue a uno non è una curiosità statistica. È l’ammissione, nel linguaggio delle proporzioni, che il perimetro di sicurezza che CISO e Direzioni Sistemi Informativi pensano di governare è una frazione minoritaria del perimetro reale. E che il *cost center* delle identità, finora dimensionato sulla popolazione degli account utente, è sottostimato di quasi due ordini di grandezza nel momento esatto in cui il D.Lgs. 4 settembre 2024, n. 138, le determinazioni ACN del dicembre 2025 e il pacchetto di determinazioni di aprile 2026 sono entrati a regime e iniziano a generare obblighi probatori vincolanti.

Il [Verizon 2026 DBIR](https://www.verizon.com/business/resources/reports/dbir/), pubblicato il 20 maggio su un campione di oltre 22.000 violazioni confermate in 145 Paesi, registra un incremento del 60% anno su anno dei *breach* veicolati da terze parti, che oggi rappresentano il 48% del totale; nello stesso report Verizon raccomanda esplicitamente di:

> “prestare particolare attenzione agli account di servizio e di macchina, perché sono quelli che verranno probabilmente sfruttati nel nostro potenziale futuro di AI agentica”.

## Che cosa intendiamo per *non-human identity*

Una *non-human identity* (NHI) è qualsiasi credenziale digitale che autentica un soggetto non persona fisica all’interno di un sistema informativo. Le categorie operative consolidate nella letteratura di settore, e in particolare nella [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/) del 2025, sono cinque.

Le **chiavi API** sono stringhe statiche emesse da una piattaforma per autenticare chiamate verso le proprie *application programming interface*. Vengono spesso incorporate nel codice, conservate in variabili d’ambiente o, nei casi peggiori, in repository pubblici.

I ***service principal*** sono identità organizzative che impersonano applicazioni o servizi all’interno di un *directory* aziendale (Microsoft Entra ID, AWS IAM, Google Cloud IAM). Hanno ruoli e permessi propri, possono detenere credenziali (segreti, certificati) e operare con privilegi non di rado superiori a quelli degli amministratori umani.

Gli ***OAuth grant*** sono autorizzazioni emesse da un *Identity Provider* a un’applicazione terza affinché quest’ultima acceda a risorse per conto di un utente. La compromissione di un singolo *OAuth token* può aprire l’accesso a interi ambienti SaaS senza interagire con MFA o policy condizionali, come dimostrato dagli incidenti documentati nel 2025 sulla supply chain Salesloft-Drift.

I ***workload identity*** e i certificati *machine-to-machine* (mTLS, certificati di container, *spiffe ID*) autenticano nodi infrastrutturali: cluster Kubernetes, *microservizi*, pipeline CI/CD.

Le ***agent identity*** sono la categoria emersa nell’ultimo anno con l’adozione di agenti autonomi: ogni agente AI capace di leggere CRM, generare report, eseguire transazioni opera con una propria identità digitale che invoca tool, scrive in database, comunica con altri agenti.

La caratteristica comune a queste cinque categorie è dirompente per la governance: non hanno *manager*, non firmano contratti, non vengono iscritte alle visite mediche, non ricevono comunicazioni di *offboarding*. Si moltiplicano per clonazione, ereditano permessi per *copy-paste* di configurazioni, sopravvivono al dipendente che le ha create. Una porzione non trascurabile di esse, secondo le analisi periodiche dei principali fornitori di *identity security*, dispone di privilegi paragonabili a quelli di un amministratore di sistema.

#### Il quadro normativo: art. 24 e l’inventario degli asset come prerequisito probatorio

Il [D.Lgs. 138/2024](https://www.acn.gov.it/portale/nis), che recepisce in Italia la direttiva (UE) 2022/2555, all’articolo 24, comma 2, impone a soggetti essenziali e importanti l’adozione di misure tecniche, operative e organizzative adeguate e proporzionate alla gestione dei rischi per la sicurezza dei propri sistemi informativi e di rete. La norma elenca dieci ambiti minimi, fra cui la sicurezza nell’acquisizione, sviluppo e manutenzione dei sistemi, la gestione delle vulnerabilità, la gestione degli incidenti, le politiche sui controlli di accesso e la gestione degli asset.

La traduzione operativa è contenuta nella Determinazione ACN n. 379907/2025 del 19 dicembre 2025, applicabile dal 15 gennaio 2026, che abroga e sostituisce la precedente Determinazione n. 164179/2025....