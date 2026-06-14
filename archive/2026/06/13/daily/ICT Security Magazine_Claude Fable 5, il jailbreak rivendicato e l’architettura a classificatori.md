---
title: Claude Fable 5, il jailbreak rivendicato e l’architettura a classificatori
url: https://www.ictsecuritymagazine.com/notizie/claude-fable-5-jailbreak-architettura-classificatori/
source: ICT Security Magazine
date: 2026-06-13
fetch_date: 2026-06-14T06:28:20.081903
---

# Claude Fable 5, il jailbreak rivendicato e l’architettura a classificatori

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

![Claude Fable 5, il jailbreak rivendicato e l'architettura a classificatori: cosa conta davvero](https://www.ictsecuritymagazine.com/wp-content/uploads/Claude-Fable-5-il-jailbreak-rivendicato-e-larchitettura-a-classificatori.png)

# Claude Fable 5, il jailbreak rivendicato e l’architettura a classificatori

A cura di:[Redazione](#molongui-disabled-link)  Ore 13 Giugno 202613 Giugno 2026

Claude Fable 5 è arrivato martedì 9 giugno 2026 come potente modello di classe *Mythos* [reso sicuro](https://www.anthropic.com/news/claude-fable-5-mythos-5) per l’uso generale, con *guardrail* che ne limitano l’impiego in domini ad alto rischio come la cybersicurezza. Entro pochi giorni un *red-teamer* ne ha rivendicato il *jailbreak*, Anthropic ha negato che fosse tale e, in parallelo, il governo statunitense ne ha imposto la sospensione con un [provvedimento di *export control*](https://www.ictsecuritymagazine.com/notizie/export-control-usa-anthropic-mythos-fable/). Al netto del clamore, per chi si occupa di sicurezza i due elementi davvero rilevanti sono altri: l’architettura a classificatori che regge il prodotto e il precedente di uno Stato che impone il ritiro di un modello commerciale per una vulnerabilità contestata.

## Un solo modello, due prodotti

Il punto di partenza è il design. Anthropic ha rilasciato lo stesso modello sottostante come due prodotti distinti: il più capace e ristretto Mythos 5, riservato a un gruppo limitato di partner fidati (incluso il governo USA, nell’ambito del programma Project Glasswing), e il più blindato Claude Fable 5, destinato al pubblico. La differenza non sta nella capacità di base, ma in uno strato di classificatori di sicurezza posto davanti al modello: sistemi di AI separati che rilevano l’abuso e impediscono al modello principale di produrre l’output. Quando una richiesta tocca categorie sensibili come cybersicurezza, biologia o chimica, Fable 5 ripiega automaticamente sul meno capace Claude Opus 4.8, avvisando l’utente del *fallback*. Secondo Anthropic l’innesco scatta in meno del 5% delle sessioni, falsi positivi compresi.

## La rivendicazione e la replica

Poco dopo il rilascio, un ricercatore noto online come “Pliny the Liberator” [ha dichiarato di aver “liberato” Fable 5](https://x.com/elder_plinius/status/2064776322979676227) con una strategia di *prompting* multi-agente, sostenendo di aver estratto informazioni su temi sensibili e pubblicando alcuni *screenshot* e quello che sarebbe il [system prompt](https://www.techtimes.com/articles/318268/20260612/claude-fable-5-hit-jailbreak-claims-secret-sabotage-backlash-days-after-launch.htm) interno del modello su GitHub.

Le tattiche descritte ricadono in categorie già documentate (offuscamento dei caratteri, diluizione dell’intento lungo conversazioni molto estese, *framing* accademico o narrativo, scomposizione di un obiettivo in sotto-richieste innocue) e non costituiscono, di per sé, una novità tecnica.

Anthropic [contesta il jailbreak](https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/). L’azienda sostiene che un vero *jailbreak* dovrebbe aggirare le protezioni di base e fornire un aiuto concreto verso attività ad alto rischio, mentre l’approccio mostrato si limita a indurre il modello a proseguire nonostante i rifiuti conversazionali, un limite noto e di lunga data in quasi tutti i *large language model*. Le protezioni più forti, aggiunge, sono affidate a classificatori indipendenti che operano separatamente dal modello, per cui superare i rifiuti del modello non le disattiva. Dopo aver esaminato gli esempi, l’azienda afferma che alcuni output non erano stati prodotti da Fable 5, mentre quelli effettivamente generati contenevano solo informazioni generali già pubbliche, senza *uplift* concreto verso danni reali. Stando al comunicato di lancio, tra *red teaming* interno ed esterno (inclusa una *bug bounty*) oltre 1.000 ore di test non avrebbero prodotto alcun *jailbreak* universale, cioè un metodo capace di disattivare le protezioni in modo ampio e generalizzato; l’unica eccezione parziale è l’AI Security Institute britannico, che in una breve finestra iniziale si sarebbe avvicinato al risultato senza però raggiungerlo.

## Cosa dicono gli esperti indipendenti

Per [gli esperti indipendenti](https://www.darkreading.com/vulnerabilities-threats/claude-fable-5-doesnt-change-mythos-security-story) sentiti da Dark Reading, la sostanza non cambia. Daniel Shechter di Miggo definisce l’approccio a *rate-limiting* “un dosso, non un muro”: la capacità di base esiste, altri modelli la replicheranno e seguiranno le varianti *open source*, per cui scommettere la propria sicurezza sull’idea che le protezioni anti-*jailbreak* reggano su larga scala è la scommessa sbagliata. Rob T. Lee del SANS Institute lavora assumendo che modelli di pari livello siano già in mani ostili, e segnala un effetto collaterale spesso ignorato: il classificatore blocca anche la ricerca difensiva, perché un tentativo di costruire una *skill* di *digital forensics* lo ha fatto retrocedere a Opus 4.8. Per Rich Mogull della Cloud Security Alliance, infine, per il professionista medio “la storia non è cambiata”: il rilascio di Fa...