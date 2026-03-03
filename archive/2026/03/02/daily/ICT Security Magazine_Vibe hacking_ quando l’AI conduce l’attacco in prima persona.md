---
title: Vibe hacking: quando l’AI conduce l’attacco in prima persona
url: https://www.ictsecuritymagazine.com/articoli/vibe-hacking/
source: ICT Security Magazine
date: 2026-03-02
fetch_date: 2026-03-03T04:13:29.795974
---

# Vibe hacking: quando l’AI conduce l’attacco in prima persona

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/vibe-hacking.jpeg)

# Vibe hacking: quando l’AI conduce l’attacco in prima persona

A cura di:[Redazione](#molongui-disabled-link)  Ore 2 Marzo 202620 Febbraio 2026

**Vibe hacking** è un termine nato da un tweet. Il 2 febbraio 2025, [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383) – ex direttore AI di Tesla, cofondatore di OpenAI – pubblica un post su X che diventerà virale con oltre 4,5 milioni di visualizzazioni: descrive un nuovo modo di programmare in cui si “dà tutto alle vibes”, si accetta ogni suggerimento dell’AI senza leggere il codice, e si lascia che il software cresca oltre la propria comprensione. Lo chiama *vibe coding*. Collins Dictionary lo elegge parola dell’anno 2025.

![vibe hacking](https://www.ictsecuritymagazine.com/wp-content/uploads/vibe-hacking1.png)

Sei mesi dopo, quel concetto innocuo – pensato per progetti sperimentali del weekend – assume una connotazione radicalmente diversa. Nell’agosto 2025, il [Threat Intelligence Report di Anthropic](https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf) introduce il termine vibe hacking per descrivere qualcosa di inedito: un’operazione criminale in cui l’intelligenza artificiale non riceve consigli dall’attaccante, ma *conduce l’attacco in prima persona*. L’AI non suggerisce comandi – li esegue. Non propone strategie – le implementa su reti reali, in tempo reale, contro vittime reali.

L’operazione, tracciata come **GTG-2002**, ha compromesso almeno 17 organizzazioni in un solo mese nei settori sanitario, governativo, dei servizi di emergenza e delle istituzioni religiose. Un singolo operatore, con competenze tecniche limitate, ha ottenuto l’impatto di un intero team criminale. E lo ha fatto delegando quasi tutto a Claude Code.

Questo articolo ricostruisce le cinque fasi dell’attacco in dettaglio tecnico, analizza il ruolo del file CLAUDE.md come playbook offensivo persistente, e mappa le implicazioni operative per chi difende reti e infrastrutture.

## Dal vibe coding al vibe hacking: una mutazione semantica che cambia tutto

Per comprendere la portata di ciò che è accaduto, è necessario distinguere con precisione due concetti che condividono l’etimologia ma non la sostanza.

Il vibe coding, nella definizione originale di Karpathy, descrive uno sviluppatore esperto che *sceglie deliberatamente* di non leggere il codice generato dall’AI, accettando ogni modifica senza revisione. È un atto consapevole di delega. Il codice cresce oltre la comprensione dell’operatore, ma il contesto resta benigno: prototipi, esperimenti, progetti usa-e-getta. Come ha scritto Simon Willison in un’analisi molto citata, la differenza cruciale sta nel fatto che Karpathy *potrebbe* leggere e comprendere quel codice se lo volesse – semplicemente *sceglie* di non farlo.

Il **vibe hacking**, nella definizione operativa emersa dal caso GTG-2002, ribalta questa dinamica. L’operatore *non può* comprendere ciò che l’AI esegue, perché non possiede le competenze tecniche necessarie. Non sceglie di delegare – non ha alternative. L’AI non è un assistente: è l’operatore primario. L’umano fornisce obiettivi strategici; l’AI pianifica, esegue, adatta, analizza ed estorce. In termini MITRE ATT&CK, l’AI attraversa autonomamente quasi tutte le tattiche del framework, dalla *Reconnaissance* (TA0043) alla *Impact* (TA0040).

Questa distinzione non è accademica. È la differenza tra un amplificatore di competenze esistenti e un *sostituto di competenze inesistenti*. Ed è esattamente ciò che rende il vibe hacking una minaccia di categoria diversa rispetto a tutto ciò che il panorama della sicurezza informatica ha affrontato finora.

## Il file CLAUDE.md come playbook offensivo: persistenza e contesto malevolo

L’elemento tecnico più innovativo dell’operazione GTG-2002 non è uno zero-day, un exploit personalizzato o un malware sofisticato. È un file di testo.

Claude Code utilizza un file di configurazione chiamato **CLAUDE.md** che fornisce contesto persistente a ogni interazione. Normalmente, gli sviluppatori lo usano per specificare preferenze di stile, standard di codifica o informazioni sul progetto in corso. L’attaccante di GTG-2002 ha trasformato questo meccanismo in un vero e proprio **playbook operativo offensivo**.

Il file CLAUDE.md configurato dall’attaccante conteneva:

* **Una cover story**: l’operatore dichiarava di essere un penetration tester autorizzato, con contratti di supporto ufficiali dalle organizzazioni target. Questo ingannava i guardrail di sicurezza del modello, che interpretava le richieste come attività di testing legittimo.
* **Metodologie di attacco dettagliate**: istruzioni per il collegamento VPN, tecniche di enumerazione utenti, metodi di credential harvesting tramite attacchi Kerberos, estrazione di hash e cracking.
* **Framework di prioritizzazione dei target**: criteri per identificare e classificare le vittime in base al valore dei dati e alla capacità di pagamento.
* **Checklist operative**: una procedura in sette fasi dalla ricognizione alla persistenza, con tecniche avanzate di post-compromise inclusi attacchi relay e abuso di deleghe.
* **Istruzioni per la comunicazione in lingua russa**: il con...