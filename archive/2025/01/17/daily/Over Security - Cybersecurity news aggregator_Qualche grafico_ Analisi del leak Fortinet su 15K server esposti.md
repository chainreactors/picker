---
title: Qualche grafico: Analisi del leak Fortinet su 15K server esposti
url: https://www.insicurezzadigitale.com/qualche-grafico-analisi-del-leak-fortinet-su-15k-server-esposti/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-17
fetch_date: 2025-10-06T20:12:02.320982
---

# Qualche grafico: Analisi del leak Fortinet su 15K server esposti

[(in)sicurezza digitale](https://insicurezzadigitale.com/)

* Incidenti e violazioni
  + [Roundup – Flash](https://insicurezzadigitale.com/category/roundup/)
  + [Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)
  + [Phishing](https://insicurezzadigitale.com/category/phishing/)
  + [Privacy](https://insicurezzadigitale.com/category/privacy/)
  + [Data Breach](https://insicurezzadigitale.com/category/data-breach/)
* [Ransomware](https://insicurezzadigitale.com/category/ransomware/)
* [Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)
  + [Analisi](https://insicurezzadigitale.com/category/analisi/)
* [La stampa dice](https://insicurezzadigitale.com/la-stampa-dice/)
* Altro…
  + [Chi siamo](https://insicurezzadigitale.com/chi-siamo/)
  + [> Whistleblowing <](https://insicurezzadigitale.com/whistleblowing/)
  + [Eventi](https://insicurezzadigitale.com/category/eventi/)
  + [Editoriali di Dario Fadda](https://blogsicurezza.myblog.it/)
  + [Data Leaks list](https://insicurezzadigitale.com/data-leaks-list/)
  + [Archivio Cyber Security Notes](https://insicurezzadigitale.com/archivio-cyber-security-notes/)
  + [Archivio Malware samples](https://insicurezzadigitale.com/archivio-malware-samples/)
  + [Infosec Tools list](/tool)
* Il Network
  + [NINAsec – Newsletter](https://ninasec.substack.com/)
  + [Spcnet.it](https://www.spcnet.it)
  + [Ziobudda](https://www.ziobudda.org)
  + [ilGlobale.it](https://www.ilglobale.it)
  + [SecureBulletin.com](https://securebulletin.com/)
* [I Forums](https://forum.ransomfeed.it/)

[Analisi](https://insicurezzadigitale.com/category/analisi/)

# Qualche grafico: Analisi del leak Fortinet su 15K server esposti

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
16 Gennaio 2025

![](https://insicurezzadigitale.com/wp-content/uploads/2025/01/Fortiguard-security-Services-banner-1.jpg)

Si parla di:

Toggle

* [Cosa è successo?](#Cosa_e_successo)
* [Torniamo al leak attuale](#Torniamo_al_leak_attuale)

Nelle ultime ore lo sfruttamento della vulnerabilità [CVE-2024-55591](https://nvd.nist.gov/vuln/detail/CVE-2024-55591) sul prodotto firewall FortiGate di Fortinet ha sicuramente attirato l’attenzione per la sua dimensione. Anche io ne ho fatto una analisi, per poterne descrivere l’importanza a livello globale, ma partiamo con ordine.

## Cosa è successo?

Il 14 gennaio scorso, Fortinet ha rivelato la vulnerabilità CVE-2024-55591, che consente un bypass dell’autenticazione in FortiOS e FortiProxy. Questa falla potrebbe permettere agli attaccanti di ottenere privilegi di super-amministratore attraverso richieste manipolate al modulo websocket di Node.js.

Il giorno successivo, il 15 gennaio, un gruppo di criminali noto come “Belsen Group” ha pubblicato online, sul dark web, dati riservati riguardanti circa 15.000 firewall FortiGate. Le informazioni trapelate includono indirizzi IP, password e configurazioni dei firewall, rappresentando un rischio considerevole per le organizzazioni coinvolte.

Analisi preliminari indicano che i dati risalgono a incidenti avvenuti nel 2022, suggerendo che la fuga non sia recente ma piuttosto il risultato di compromissioni passate, **oppure che i dispositivi siano rimasti senza risoluzione della vulnerabilità da oltre due anni**.

Kevin Beaumont, un ricercatore di sicurezza, infatti ha notato che la fuga di dati potrebbe essere correlata alla vulnerabilità **CVE-2022-40684**, un’altra falla zero-day scoperta nel 2022.

Per avere un dato generale sull’impatto (potenziale) che una vulnerabilità così grave può avere, possiamo controllare facilmente su Shodan quante istanze ci sono attualmente in giro per la rete. Ovviamente non tutte sono della versione vulnerabile ma serve per capire quanto questo software sia utilizzato, a livello mondo.

![](https://www.insicurezzadigitale.com/wp-content/uploads/2025/01/photo_2023-02-19_12-21-03-1024x538.jpg)

## Torniamo al leak attuale

L’analisi dei dati contenuti nel leak appena stato diffuso dal gruppo Belsen, come detto riporta informazioni di oltre 15.000 di questi dispositivi attualmente esposti.

Io mi sono limitato ad aggregare il leak di modo da avere qualche informazione visiva su questa mole di dati. Per esempio vedendo **quali sono le porte maggiormente utilizzate** sul totale:

![](https://www.insicurezzadigitale.com/wp-content/uploads/2025/01/chart.png)

Come evidente notiamo che oltre il 55% del totale è esposto sulla porta 443.

![](https://www.insicurezzadigitale.com/wp-content/uploads/2025/01/chart1.png)

Dando invece spazio all’Italia, ho provato a filtrare i dati relativi alla nostra nazione, elencandone i Provider italiani maggiormente impattati, che più o meno dovrebbero corrispondere a questo grafico, che riporta per ciascuno la sua dimensione per numero di IP ritrovati all’interno.

![](https://www.insicurezzadigitale.com/wp-content/uploads/2025/01/Provider-italiani-1024x486.png)

Questa invece la concentrazione per Paese, degli IP affetti

![](https://www.insicurezzadigitale.com/wp-content/uploads/2025/01/6525180d-582e-49db-b7e3-af8b5a6a89e8.png)

Anche il ricercatore **Emanuele De Lucia** ha fatto analisi su questo scenario, offrendo una statistica, basata sull’Italia, dividendo le imprese impattate per settore lavorativo.

> [#Fortinet](https://twitter.com/hashtag/Fortinet?src=hash&ref_src=twsrc%5Etfw) [#FortiGate](https://twitter.com/hashtag/FortiGate?src=hash&ref_src=twsrc%5Etfw) [#Belsen](https://twitter.com/hashtag/Belsen?src=hash&ref_src=twsrc%5Etfw) [#Dataleak](https://twitter.com/hashtag/Dataleak?src=hash&ref_src=twsrc%5Etfw) impatto, in percentuale, per settori su [#Italia](https://twitter.com/hashtag/Italia?src=hash&ref_src=twsrc%5Etfw) – Da notare che dalla presunta vulnerabilità sfruttata (CVE-2022–40684) al rilascio di questo archivio sono passati anni. Da quanto tempo i cattivi avevano questi dati ? [pic.twitter.com/jpZpvpgSQx](https://t.co/jpZpvpgSQx)
>
> — Emanuele De Lucia (@Manu\_De\_Lucia) [January 16, 2025](https://twitter.com/Manu_De_Lucia/status/1879934748472291478?ref_src=twsrc%5Etfw)

Fortinet ha fornito indicazioni per mitigare i rischi legati a CVE-2024-55591, raccomandando agli utenti di aggiornare immediatamente i loro sistemi a versioni corrette e di limitare l’accesso alle interfacce di gestione dei firewall da Internet.

È fondamentale cambiare le password degli utenti amministrativi e implementare l’autenticazione a più fattori (MFA) per aumentare la sicurezza.

Questi eventi evidenziano l’importanza della vigilanza continua nella sicurezza informatica e la necessità per le organizzazioni di rimanere aggiornate sulle ultime minacce e vulnerabilità.

##### < tags />

[databreach](https://insicurezzadigitale.com/tag/databreach/)[fortigate](https://insicurezzadigitale.com/tag/fortigate/)[fortinet](https://insicurezzadigitale.com/tag/fortinet/)[infosec](https://insicurezzadigitale.com/tag/infosec/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Qualche+grafico%3A+Analisi+del+leak+Fortinet+su+15K+server+esposti&url=https://insicurezzadigitale.com/qualche-grafico-analisi-del-leak-fortinet-su-15k-server-esposti/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/qualche-grafico-analisi-del-leak-fortinet-su-15k-server-esposti/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/qualche-grafico-analisi-del-leak-fortinet-su-15k-server-esposti/&title=Qualche+grafico%3A+Analisi+del+leak+Fortinet+su+15K+server+esposti)

[== articolo precedente ==](https://insicurezzadigitale.com/elezioni-usa-scoperte-operazioni-di-disinformazione-tramite-server-dedicati-e-ia/)

[:: articolo successivo ::](https://insicurezzadigitale.com/grazia-concessa-da-trump-al-fondatore-di-silk-road-ex-marketplace-dark/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/qua...