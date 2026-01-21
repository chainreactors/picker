---
title: Framework SLSA: guida completa ai livelli di sicurezza e strategie di implementazione per la Software Supply Chain
url: https://www.ictsecuritymagazine.com/articoli/framework-slsa/
source: ICT Security Magazine
date: 2026-01-20
fetch_date: 2026-01-21T03:32:46.119796
---

# Framework SLSA: guida completa ai livelli di sicurezza e strategie di implementazione per la Software Supply Chain

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

![framework SLSA: livelli progressivi di sicurezza della supply chain software, ambienti di build isolati, attestazioni crittografiche e tracciabilità della provenienza degli artefatti digitali.](https://www.ictsecuritymagazine.com/wp-content/uploads/framework-slsa.jpg)

# Framework SLSA: guida completa ai livelli di sicurezza e strategie di implementazione per la Software Supply Chain

A cura di:[Redazione](#molongui-disabled-link)  Ore 20 Gennaio 202614 Gennaio 2026

L’ecosistema digitale contemporaneo poggia su fondamenta invisibili ma critiche: la catena di approvvigionamento del software. Ogni applicazione moderna integra centinaia di dipendenze, librerie e componenti esterni, creando una superficie di attacco che si estende ben oltre i confini del codice proprietario. Gli attacchi alla *supply chain* software hanno registrato un incremento del 200% nel 2023 rispetto all’anno precedente secondo il [State of the Software Supply Chain Report di Sonatype](https://www.sonatype.com/state-of-the-software-supply-chain/introduction), trasformando quello che era un vettore di attacco marginale in una minaccia sistemica per l’intero ecosistema tecnologico globale.

L’attacco a [SolarWinds](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a) nel dicembre 2020 ha rappresentato un punto di non ritorno: la compromissione del processo di *build* ha permesso la distribuzione di aggiornamenti malevoli a oltre 18.000 organizzazioni, incluse agenzie governative statunitensi e corporation Fortune 500. Questo evento ha catalizzato la nascita di SLSA, un *framework* che ambisce a definire standard universali per la sicurezza della *software supply chain*.

## Che cos’è il Framework SLSA: origini e architettura concettuale

SLSA (pronunciato “salsa”) è l’acronimo di *Supply-chain Levels for Software Artifacts*. Sviluppato originariamente da Google e successivamente adottato dalla [Open Source Security Foundation (OpenSSF)](https://openssf.org/projects/slsa/) come progetto *community-driven*, SLSA rappresenta un *framework* di sicurezza che definisce requisiti progressivi per proteggere l’integrità degli artefatti software durante l’intero ciclo di vita della produzione.

La filosofia architetturale di SLSA si distingue per tre caratteristiche fondamentali.

La prima è la progressività strutturata: anziché imporre requisiti monolitici, il *framework* articola la sicurezza in livelli incrementali che permettono un’adozione graduale, calibrata sulla maturità organizzativa e sulle risorse disponibili.

La seconda è la verificabilità empirica: ogni requisito SLSA è progettato per essere verificabile attraverso evidenze oggettive, principalmente mediante attestazioni crittograficamente firmate che documentano la *provenance* degli artefatti.

La terza è l’agnosticismo tecnologico: il *framework* prescinde da specifiche tecnologie o piattaforme, concentrandosi su principi universali applicabili a qualsiasi *stack* tecnologico.

La specifica corrente, [SLSA v1.0](https://slsa.dev/spec/v1.0/), rilasciata il 19 aprile 2023, ha consolidato anni di iterazioni e *feedback* dalla *community*, introducendo una struttura più coerente e requisiti più pragmatici rispetto alle versioni precedenti. Una novità significativa della v1.0 è la suddivisione dei requisiti in *track* separati: la versione attuale definisce il *Build Track* con i livelli 1-3, mentre altri *track* (come il *Source Track*) sono previsti per versioni future.

## Anatomia dei livelli SLSA: dal livello 0 al livello 3

Il *framework* SLSA nella versione 1.0 articola la maturità della *supply chain security* attraverso il *Build Track*, che comprende quattro livelli progressivi (da L0 a L3). Ciascun livello è caratterizzato da requisiti specifici che rafforzano le garanzie di integrità e *provenance* degli artefatti software.

### Build L0: assenza di requisiti

Il livello zero rappresenta l’assenza di SLSA: nessun requisito è soddisfatto e non esistono garanzie di integrità degli artefatti. Questo livello descrive lo stato di partenza della maggior parte dei progetti software prima dell’adozione del *framework*.

### Build L1: documentazione della provenance

Il primo livello operativo rappresenta il punto di ingresso nel *framework* e si focalizza sulla creazione di una traccia documentale del processo di *build*.

Il Livello 1 richiede che il processo di *build* produca attestazioni di *provenance* che documentino quale sorgente è stata utilizzata, quale processo di *build* è stato eseguito e quali artefatti sono stati generati. Queste attestazioni seguono il formato standardizzato [in-toto](https://in-toto.io/), un *framework* per la *supply chain integrity* sviluppato alla NYU Tandon School of Engineering e ora [progetto graduated della Cloud Native Computing Foundation](https://www.cncf.io/announcements/2025/04/23/cncf-announces-graduation-of-in-toto-security-framework-enhancing-software-supply-chain-integrity-across-industries/).

La *provenance* al Livello 1 non richiede ancora garanzie crittografiche robuste: l’obiettivo primario è stabilire visibilità sul processo di *build*, creando le fondamenta per i livelli successivi. Come specificato nella [documentazione SLSA](https://slsa.dev/spec/v1.0/levels), questo livello può essere facilmente aggirato o falsificato, ma fornisce comunque benefici significativi per *audit* e *incident response*.

Sebbene le garanzie di sicurezza al Livello 1 siano limitate, l’ado...