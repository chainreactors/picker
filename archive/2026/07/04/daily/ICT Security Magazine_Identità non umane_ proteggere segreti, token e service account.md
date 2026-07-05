---
title: Identità non umane: proteggere segreti, token e service account
url: https://www.ictsecuritymagazine.com/digital-id-security/identita-non-umane-2/
source: ICT Security Magazine
date: 2026-07-04
fetch_date: 2026-07-05T05:56:24.686564
---

# Identità non umane: proteggere segreti, token e service account

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

![Identità non umane: chiavi, token e ingranaggi digitali interconnessi in una rete, illustrazione concettuale a colori pop accesi.](https://www.ictsecuritymagazine.com/wp-content/uploads/2026-06-08_evergreen_identita-non-umane.jpg)

# Identità non umane: proteggere segreti, token e service account

A cura di:[Redazione](#molongui-disabled-link)  Ore 4 Luglio 20269 Giugno 2026

Identità non umane (NHI, Non-Human Identities) è il termine con cui la sicurezza informatica indica oggi una delle superfici d’attacco in più rapida crescita: gli account macchina, le chiavi e i segreti che permettono a software, servizi e automazioni di autenticarsi e operare senza un essere umano alla tastiera. Per anni la sicurezza delle identità si è concentrata sulle persone, con password, autenticazione a più fattori e gestione degli accessi; nel frattempo, però, il numero delle identità non umane è cresciuto a dismisura, spesso senza controllo, diventando il punto debole da cui passano sempre più violazioni.

## Che cosa sono le identità non umane

Con identità non umane si intende l’insieme delle credenziali e degli account associati non a persone ma a entità tecniche: i *service account* che fanno girare i processi, le chiavi API che collegano due applicazioni, i *token* OAuth che autorizzano l’accesso a un servizio cloud, i certificati che identificano un server, i *secret* che proteggono le connessioni ai database, fino alle identità dei carichi di lavoro (*workload*) in container e funzioni serverless. A questi si aggiungono, nell’ultimo anno, le identità assegnate agli agenti di intelligenza artificiale, che agiscono in autonomia con strumenti e permessi propri.

La differenza con le identità umane non è solo numerica. Un dipendente viene assunto e cessa con processi noti, ha un volto, cambia la password, supera una verifica MFA (Multi-Factor Authentication, autenticazione a più fattori). Una identità macchina, invece, nasce spesso in modo informale durante lo sviluppo, riceve permessi ampi per comodità, non ha un proprietario chiaro e tende a sopravvivere a lungo, anche quando il progetto che l’ha creata è stato dismesso. È un’identità silenziosa, che nessuno spegne.

## Perché sono esplose e quanto pesano

La spinta è arrivata dalla combinazione di cloud, microservizi, automazione e DevOps: ogni integrazione, ogni *pipeline* CI/CD, ogni connettore aggiunge nuove credenziali macchina. Le stime sul rapporto tra identità non umane e identità umane variano molto a seconda della metodologia, ed è bene presentarle come ordini di grandezza più che come numeri esatti: secondo la ricerca di Orca Security il rapporto medio è di circa 50 a 1, mentre il report di Entro Labs per la prima metà del 2025 lo colloca a 144 a 1, in crescita dai 92 a 1 dell’anno precedente; in organizzazioni fortemente automatizzate si arriva a citare punte di 500 a 1. Al di là della cifra specifica, il messaggio è univoco: le macchine che si autenticano sono ormai molte decine di volte più numerose delle persone, e crescono ogni anno a doppia cifra.

L’arrivo dell’intelligenza artificiale generativa ha accelerato ulteriormente il fenomeno, moltiplicando integrazioni e chiamate tra servizi. Questo cambia la scala del problema: difendere qualche migliaio di account umani è un conto, governare centinaia di migliaia di credenziali macchina effimere è un’altra disciplina.

## I rischi principali: l’OWASP NHI Top 10

Per dare ordine a questo dominio, nel 2025 OWASP (Open Worldwide Application Security Project) ha pubblicato la [Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/), una classifica dei rischi più critici legati alle identità macchina. Al primo e al secondo posto figurano l’*improper offboarding*, cioè la mancata disattivazione delle credenziali quando un servizio o un dipendente che le aveva create non c’è più, e il *secret leakage*, la fuga di segreti hardcoded nel codice o nei file di configurazione. Più in basso nella classifica compaiono altri problemi molto concreti da tenere d’occhio: le identità con privilegi eccessivi (*overprivileged NHI*, al quinto posto), che violano il principio del minimo privilegio, e i *long-lived secrets* (al settimo), le credenziali a vita lunga che non vengono mai ruotate e restano valide per anni.

Sono esattamente le caratteristiche che rendono le identità non umane appetibili per un attaccante: una chiave API dimenticata in un repository, con permessi ampi e senza scadenza, è un passe-partout silenzioso che non fa scattare i controlli pensati per gli utenti umani, come la verifica MFA o l’analisi dei comportamenti di login anomali.

Non è teoria. Nell’agosto 2025 l’incidente noto come Salesloft-Drift lo ha mostrato su larga scala: sfruttando *token* OAuth sottratti al connettore tra Drift e Salesforce, gli attaccanti (tracciati come UNC6395) hanno avuto accesso ai dati di oltre 700 organizzazioni, tra cui nomi noti della stessa industria della sicurezza, scavalcando l’autenticazione a più fattori per la semplice ragione che un *token* valido non la richiede. È il ritratto perfetto del rischio legato alle identità non umane: nessuna password rubata, nessun login s...