---
title: Gestione delle chiavi crittografiche: ciclo di vita, rotazione e scadenze
url: https://www.ictsecuritymagazine.com/articoli/gestione-chiavi-crittografiche/
source: ICT Security Magazine
date: 2026-11-07
fetch_date: 2026-11-08T08:14:53.117628
---

# Gestione delle chiavi crittografiche: ciclo di vita, rotazione e scadenze

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.350 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

  Minacce e attacchi

  + [Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)

  Rischio, norme e privacy

  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)

  Tecnologie

  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)

  Scenari

  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)

  Ultimi in **Cyber Security**

  [Tutti gli articoli di Cyber Security →](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Approfondimenti](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* [Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Eventi ↗](https://eventi.ictsecuritymagazine.com/)

[Newsletter](/newsletter/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca

Attiva/disattiva menu

[Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

# Gestione delle chiavi crittografiche: ciclo di vita, rotazione e scadenze

Dove vivono le chiavi crittografiche, chi le può usare, ogni quanto si ruotano e che cosa succede quando un certificato scade: la guida con NIST, CA/B Forum, NIS2 e DORA.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il7 Novembre 20264 Novembre 2026  Condividi

![Gestione delle chiavi crittografiche: ciclo di vita, rotazione e scadenze: Chiave 3D con timer arancio nella serratura di un modulo di sicurezza; accanto un certificato con sigillo si sfalda in cubi](https://www.ictsecuritymagazine.com/wp-content/uploads/gestione-chiavi-crittografiche.webp)

In sintesi

* Il NIST divide la vita di una chiave in quattro fasi e sei stati, dalla pre-attivazione alla distruzione, e suggerisce un crittoperiodo per ogni tipo.
* Ruotare una chiave nel KMS cloud non ricifra i dati già protetti: la ricifratura è un'operazione distinta da pianificare.
* I certificati TLS pubblici durano al massimo 200 giorni dal 15 marzo 2026, 100 dal 2027 e 47 dal 2029: senza automazione le scadenze passano inosservate.

La gestione delle chiavi crittografiche stabilisce se la cifratura protegge davvero dati e comunicazioni o li protegge soltanto sulla carta. Un algoritmo solido serve a poco se la chiave è copiata in dieci posti, se la può usare chiunque o se nessuno ricorda quando scade. Questa guida segue la vita di una chiave dalla generazione alla distruzione e la confronta con le regole del NIST, del CA/B Forum, della direttiva NIS2 e del regolamento DORA.

Il tema è attuale per tre ragioni. Dal 15 marzo 2026 i certificati TLS pubblicamente attendibili non possono durare più di 200 giorni, come prevede il [ballot SC-081v3 del CA/B Forum](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/). Dopo il 21 settembre 2026 i certificati FIPS 140-2 passano nell’elenco storico del [programma di validazione dei moduli crittografici](https://csrc.nist.gov/projects/cryptographic-module-validation-program) del NIST. E la norma di riferimento sul ciclo di vita delle chiavi, la SP 800-57, ha una [bozza di revisione](https://csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd) che entra nell’era post-quantistica.

## Perché la gestione delle chiavi crittografiche pesa più dell’algoritmo

Chi cifra un archivio, firma un software o apre un tunnel TLS affida la sicurezza a un segreto breve: la chiave. Se la chiave esce, l’algoritmo non può più difendere nulla. Per questo il NIST dedica alla gestione delle chiavi un’intera serie di raccomandazioni, la [SP 800-57 parte 1, revisione 5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), pubblicata nel maggio 2020.

Questo pezzo si colloca a valle di altri tre già pubblicati dalla testata. L’inventario delle primitive e delle chiavi in uso è l’oggetto della [Cryptographic Bill of Materials](/articoli/cryptographic-bill-of-materials-cbom/). La capacità di sostituire un algoritmo senza fermare i sistemi è la [crypto-agility](/notizie/crypto-agility-quantum/). Il passaggio agli algoritmi resistenti ai computer quantistici è la [migrazione alla crittografia post-quantum](/cyber-security/migrazione-post-quantum-cryptography/). Secondo la lettura della redazione, nessuno dei tre funziona se manca lo strato operativo descritto qui: sapere chi custodisce ogni chiave, per quanto tempo e con quali regole.

## Il ciclo di vita di una chiave secondo il NIST

### Quattro fasi e sei stati

Nella gestione delle chiavi crittografiche ogni chiave ha una vita, e ogni momento di quella vita ha regole proprie. La SP 800-57 la divide in quattro fasi: pre-operativa, operativa, post-operativa e di distruzione. Dentro queste fasi il documento definisce sei stati: pre-attivazione, attiva, sospesa, disattivata, compromessa e distrutta.

La distinzione ha un risvolto pratico. Una chiave disattivata non cifra più nuovi dati, ma può ancora servire a leggere quelli già protetti. Una chiave compromessa richiede invece un percorso diverso, perché va ritirata subito e può imporre di ricostruire ciò che ha protetto. La norma prevede per questo un piano di recupero dalla compromissione, da preparare prima che serva.

### Il crittoperiodo: quanto può durare una chiave

Il NIST chiama crittoperiodo l’intervallo in cui una chiave è autorizzata all’uso. La Tabella 1 della revisione 5 propone valori orientativi per ogni tipo di chiave.

![Gestione delle chiavi crittografiche: ciclo di vita, rotazione e scadenze](https://www.ictsecuritymagazine.com/wp-content/uploads/tabella-crittoperiodi-1-646x700.webp)

Le chiavi private di firma restano in uso da uno a tre anni. Le chiavi simmetriche di cifratura dei dati hanno un periodo di utilizzo per cifrare inferiore a due anni, mentre per decifrare si può arrivare al periodo di cifratura più tre anni. Le chiavi master e di derivazione durano circa un anno. Le chiavi effimere di accordo valgono una sola transazione.

Il documento precisa che periodi più lunghi o più brevi possono essere giustificati dal contesto, ma chi allunga il crittoperiodo deve valutare con attenzione i rischi. Ogni chiave, inoltre, dovrebbe servire a un solo scopo: usare la stessa chiave per cifrare e per firmare a...