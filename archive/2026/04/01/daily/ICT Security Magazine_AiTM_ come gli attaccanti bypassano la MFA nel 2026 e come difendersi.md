---
title: AiTM: come gli attaccanti bypassano la MFA nel 2026 e come difendersi
url: https://www.ictsecuritymagazine.com/notizie/aitm-attaccanti-mfa/
source: ICT Security Magazine
date: 2026-04-01
fetch_date: 2026-04-02T04:31:27.432891
---

# AiTM: come gli attaccanti bypassano la MFA nel 2026 e come difendersi

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

![mfa aitm](https://www.ictsecuritymagazine.com/wp-content/uploads/mfa-aitm.jpeg)

# AiTM: come gli attaccanti bypassano la MFA nel 2026 e come difendersi

A cura di:[Redazione](#molongui-disabled-link)  Ore 1 Aprile 202627 Marzo 2026

Il 4 marzo 2026, Europol ha coordinato lo smantellamento di Tycoon 2FA, la piattaforma di phishing-as-a-service che [Microsoft ha definito](https://blogs.microsoft.com/on-the-issues/2026/03/04/how-a-global-coalition-disrupted-tycoon/) la piattaforma più prolifera da essa osservata nel 2025. A metà 2025, Tycoon 2FA era responsabile di circa il 62% di tutte le email di phishing bloccate da Microsoft, con oltre 30 milioni di messaggi intercettati in un singolo mese. L’operazione aveva colpito [96.000 vittime accertate](https://www.darkreading.com/threat-intelligence/tycoon-2fa-europol-vendors-bust-phishing-platform), di cui oltre 55.000 clienti Microsoft. Già due settimane prima del takedown, il 19 febbraio 2026, [Abnormal AI aveva documentato](https://abnormal.ai/blog/starkiller-phishing-kit) un nuovo kit chiamato Starkiller, dimostrando che la tecnica è ormai commoditizzata e indipendente da qualsiasi singola piattaforma.

Il messaggio è inequivocabile: la MFA tradizionale basata su TOTP, push notification e SMS è superata come difesa contro attaccanti motivati. Non perché la MFA sia inutile: è perché gli attaccanti hanno risolto il problema in modo elegante, senza nemmeno doverla rompere.

## Cos’è un attacco AiTM e perché supera la MFA

Il phishing tradizionale clona una pagina di login e cattura credenziali. Un attacco Adversary-in-the-Middle (AiTM) non clona nulla: fa da proxy alla pagina reale. Il flusso è il seguente:

![aitm mfa](https://www.ictsecuritymagazine.com/wp-content/uploads/aitm.png)

La vittima sta interagendo con il servizio legittimo. La pagina che vede è quella autentica, perché è il proxy a servirla in tempo reale. L’autenticazione va a buon fine: l’utente inserisce la password, fornisce il codice TOTP dall’app, Microsoft o Google inviano il session token al browser. Il proxy lo intercetta prima che raggiunga il browser legittimo.

Questo è il motivo per cui la MFA tradizionale non ferma l’attacco: l’utente si sta autenticando correttamente. Non c’è nessun errore da rilevare. Il proxy copia il risultato. Come spiegato da [Cloudflare nel suo briefing sul takedown di Tycoon 2FA](https://blog.cloudflare.com/cloudflare-helps-disrupt-tycoon-2fa/), la piattaforma trasmetteva in tempo reale i prompt di autenticazione per catturare session token e cookie attivi.

## Il mercato delle piattaforme AiTM: Tycoon 2FA, EvilProxy e il fenomeno PhaaS

La differenza tra il 2022 e il 2026 non è tecnica: è economica. Secondo la [ricerca Sekoia.io pubblicata a giugno 2025](https://blog.sekoia.io/global-analysis-of-adversary-in-the-middle-phishing-threats/), basata su dati raccolti tra gennaio e aprile 2025, 11 kit PhaaS di rilievo circolano con capacità AiTM. Non si tratta di strumenti per nation-state actor: sono abbonamenti mensili da poche centinaia di euro, con dashboard, template e documentazione.

[Tycoon 2FA](https://www.proofpoint.com/us/blog/threat-insight/disruption-targets-tycoon-2fa-popular-aitm-phaas) è apparso nell’agosto 2023 targettando Microsoft 365 e Gmail. Il suo punto di forza era la sofisticazione evasiva: CAPTCHA per filtrare i bot, verifica dello user-agent per escludere i crawler delle aziende di sicurezza, obfuscation del JavaScript, e un sistema di precision-validated phishing che valida se l’utente è un target prima di mostrare la pagina di phishing. [Proofpoint ha rilevato](https://www.proofpoint.com/us/blog/email-and-cloud-threats/aitm-phishing-attacks-evolving-threat-microsoft-365) campagne che hanno targettato migliaia di organizzazioni in tutto il mondo nell’aprile 2025.

[EvilProxy](https://blog.sekoia.io/global-analysis-of-adversary-in-the-middle-phishing-threats/) ha introdotto tecniche di fingerprinting del browser per aggirare i sistemi di rilevamento e supporta la registrazione di nuovi metodi di autenticazione post-compromissione: dopo aver rubato il session token, un attaccante può accedere al portale di sicurezza dell’utente e registrare una propria chiave FIDO2, ottenendo accesso persistente anche dopo la scadenza del token rubato.

[Starkiller](https://abnormal.ai/blog/starkiller-phishing-kit), documentato da Abnormal AI il 19 febbraio 2026 circa due settimane prima del takedown di Tycoon 2FA, usa headless Chrome all’interno di un container Docker per le richieste, rendendo inefficace il browser fingerprinting. Come analizzato da [Dev.to](https://dev.to/iamdevbox/aitm-phishing-2026-how-starkiller-and-tycoon-2fa-bypass-your-mfa-3igd) e [KrebsOnSecurity](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/), l’operazione è gestita da un threat group che si chiama Jinkusu e offre il kit come subscription service con dashboard UI. La presenza di Starkiller già prima del takedown di Tycoon 2FA dimostra che l’ecosistema si rigenera indipendentemente dagli interventi delle forze dell’ordine.

Il dato più allarmante non è il volume degli attacchi: è il loro tasso di successo. Secondo il [2025 SaaS Security Threat Report di Obsidian Security](https://www....