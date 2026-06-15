---
title: Secrets management: il segreto migliore è quello che non esiste
url: https://www.ictsecuritymagazine.com/cyber-security/secrets-management/
source: ICT Security Magazine
date: 2026-06-14
fetch_date: 2026-06-15T07:10:03.060098
---

# Secrets management: il segreto migliore è quello che non esiste

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

![Secrets management](https://www.ictsecuritymagazine.com/wp-content/uploads/Secrets-management.png)

# Secrets management: il segreto migliore è quello che non esiste

A cura di:[Redazione](#molongui-disabled-link)  Ore 14 Giugno 20269 Giugno 2026

Secrets management è una di quelle discipline che quasi nessuno dichiara di trascurare e quasi tutti trascurano. La prova arriva dai numeri: secondo il report State of Secrets Sprawl 2026 di GitGuardian, nel solo 2025 sono finiti nei *commit* pubblici di GitHub 28,65 milioni di nuovi segreti scritti direttamente nel codice, il 34 per cento in più dell’anno precedente e il salto annuale più alto mai registrato. Il dato misura ciò che è visibile sui repository pubblici, quindi è per definizione la punta dell’iceberg, ma la direzione è inequivocabile: credenziali, chiavi API, *token* e password continuano a moltiplicarsi più in fretta di quanto le organizzazioni riescano a governarle.

Il riflesso comune, davanti a questo problema, è cercare una cassaforte migliore. È l’istinto sbagliato. La gestione dei segreti non si risolve custodendo meglio una quantità crescente di credenziali, ma riducendone il numero e la durata, fino al punto in cui la chiave più sicura diventa quella che non esiste. È un capovolgimento di prospettiva che cambia tutto: l’obiettivo non è proteggere il segreto, è farne a meno il più possibile.

## La proliferazione è il problema, non la custodia

Il primo malinteso da smontare è che il rischio stia nella conservazione. Il rischio sta nella proliferazione incontrollata, ciò che in inglese si chiama *secret sprawl*. I segreti si annidano ovunque: nel codice sorgente, nei file di configurazione, nelle variabili d’ambiente, nei messaggi di chat, nei *ticket*, nelle immagini dei container. Lo stesso report GitGuardian rileva che, nei perimetri analizzati, i repository interni risultano circa sei volte più esposti di quelli pubblici, perché lì la guardia si abbassa nella convinzione, falsa, che il perimetro basti a proteggere.

Il problema si aggrava per una ragione tanto banale quanto trascurata: i segreti non scadono quasi mai. GitGuardian riporta che, nel campione analizzato, il 64 per cento delle credenziali risultate valide nel 2022 era ancora attivo nel 2026, non revocato a distanza di anni, e attribuisce la cosa alla debolezza dei processi, all’assenza di una procedura ripetibile per revocare o ruotare un segreto dopo una fuga. Una credenziale messa nel posto sbagliato e mai disattivata resta una porta aperta a tempo indeterminato. La scrittura di credenziali direttamente nel codice, catalogata da MITRE come [debolezza CWE-798](https://cwe.mitre.org/data/definitions/798.html), è nota da decenni e segnalata come grave da ogni analizzatore statico, eppure resta tra le scoperte più frequenti in qualunque verifica di sicurezza. Non è un problema di conoscenza, è un problema di disciplina.

## Togliere i segreti dal codice

Il primo movimento, prima ancora di qualunque strumento sofisticato, è separare nettamente i segreti dal codice. La regola dell’OWASP è categorica: un segreto non va mai messo nel sorgente, nemmeno in un repository privato, perché il codice viene condiviso, clonato, biforcato e copiato in modi che aggirano i controlli di accesso. Vale lo stesso per i log e per le immagini dei container, dove le credenziali finiscono per inerzia e restano leggibili. Nemmeno le variabili d’ambiente sono una scorciatoia sempre sicura: in ambienti containerizzati possono essere esposte tramite configurazioni, dump o log, e andrebbero perciò popolate dall’orchestratore o dal gestore dei segreti, non scritte nell’immagine.

Tradurre questa regola in pratica significa due cose concrete. La prima è la prevenzione all’origine: analisi del codice e *secret scanning* integrati nella pipeline, controlli prima del *commit* e in fase di *push* che impediscano fisicamente a una credenziale di entrare nel repository. È il terreno naturale di una cultura di [secure coding](https://www.ictsecuritymagazine.com/articoli/secure-coding/) che sposta il controllo a sinistra, dove correggere costa meno. La seconda è la centralizzazione: tutti i segreti in un gestore dedicato, non sparsi per decine di sistemi. Un *secret manager*, che si tratti di HashiCorp Vault o dei servizi gestiti dai provider cloud, concentra in un solo punto le tre cose che altrimenti mancano: registro degli accessi, controllo dei permessi e rotazione.

## Secrets management come disciplina: vault, rotazione, segreti dinamici

Centralizzare è la condizione, non il traguardo. La vera maturità del secrets management sta in come quei segreti vivono nel tempo. Un segreto statico, per quanto ben custodito, è una bomba a orologeria: prima o poi trapela, e il danno è proporzionale a quanto a lungo resta valido. Per questo la disciplina si misura sulla rotazione e sulla durata.

La direzione indicata dalle best practice OWASP è ridurre al minimo la vita utile del segreto: farlo esistere solo per il tempo necessario, renderlo revocabile e, dove possibile, generarlo dinamicamente. Tradotto, significa privilegiare i segreti dinamici, creati su richiesta al momento dell’uso e revocati automaticame...