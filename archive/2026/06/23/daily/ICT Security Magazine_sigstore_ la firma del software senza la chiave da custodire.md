---
title: sigstore: la firma del software senza la chiave da custodire
url: https://www.ictsecuritymagazine.com/cyber-security/sigstore-firma-software/
source: ICT Security Magazine
date: 2026-06-23
fetch_date: 2026-06-24T06:06:14.699147
---

# sigstore: la firma del software senza la chiave da custodire

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

![sigstore](https://www.ictsecuritymagazine.com/wp-content/uploads/ChatGPT-Image-9-giu-2026-15_26_23.png)

# sigstore: la firma del software senza la chiave da custodire

A cura di:[Redazione](#molongui-disabled-link)  Ore 23 Giugno 20269 Giugno 2026

sigstore è il progetto che ha reso praticabile una cosa che la sicurezza predicava da decenni senza riuscire a farla adottare: firmare il software, per poter dimostrare chi lo ha prodotto e che non è stato manomesso. L’idea della firma digitale degli artefatti è sempre stata giusta, ma nella pratica è rimasta marginale per una ragione molto concreta: gestire una chiave privata di firma è difficile e pericoloso. Va generata, protetta per anni, ruotata, e se trapela tutto ciò che è stato firmato con essa diventa sospetto. Quella frizione ha tenuto la firma del software fuori dalla portata della maggior parte degli sviluppatori. sigstore la rimette in gioco togliendo dall’equazione proprio la parte più scomoda: la chiave.

Il risultato è un capovolgimento del modello di fiducia. Invece di affidarsi a una chiave che deve restare segreta e integra nel tempo, sigstore lega la firma a un’identità verificata e ne registra l’evento in un archivio pubblico e a prova di manomissione. La domanda di chi verifica non è più se una chiave sia ancora al sicuro dopo mesi o anni, ma se quel preciso atto di firma sia stato compiuto da quell’identità, in quel momento, e regolarmente registrato. È una differenza che cambia la scala del problema.

## La firma del software era giusta, e quasi nessuno la faceva

Per capire cosa risolve sigstore conviene ricordare perché la firma tradizionale ha fallito nell’adozione. Firmare un artefatto, un’immagine container, un pacchetto, un binario, richiedeva di possedere e custodire una chiave privata di lunga durata. Questo significava un onere costante: dove conservarla perché non venga rubata, come ruotarla, cosa fare se un dipendente che vi aveva accesso se ne va. E significava un rischio sistemico: una sola chiave compromessa mette in dubbio l’autenticità di tutto ciò che ha firmato, magari per anni a ritroso. Di fronte a questo costo, la maggioranza ha semplicemente rinunciato, lasciando la catena di distribuzione del software senza un modo affidabile per verificare la provenienza.

È esattamente la lacuna che gli attacchi alla supply chain sfruttano. Quando un [worm si infila nei pacchetti](https://www.ictsecuritymagazine.com/notizie/attacco-supply-chain-miasma/) di un repository pubblico e ne pubblica versioni compromesse, il problema non è solo l’intrusione: è che chi scarica quei pacchetti non ha uno strumento semplice per accorgersi che non provengono da chi dovrebbe. Senza una firma verificabile, l’integrità e l’origine di un artefatto restano un atto di fede. La firma del software risolverebbe il problema, se solo fosse abbastanza facile da usare da essere usata davvero.

## Firmare con l’identità, non con la chiave

La mossa di sigstore è la firma senza chiavi persistenti, ciò che viene chiamato firma *keyless*. Quando uno sviluppatore o, più spesso, una pipeline automatica vuole firmare un artefatto, non estrae una chiave da un caveau. Si autentica invece tramite OIDC presso un fornitore di identità, tipicamente la stessa piattaforma di integrazione continua che esegue il lavoro, e a quel punto la *certificate authority* del progetto, Fulcio, emette un certificato a vita brevissima, dell’ordine di dieci minuti, che lega quell’identità verificata a una coppia di chiavi effimere.

Con quel certificato lo strumento di firma, Cosign, firma l’artefatto, e subito dopo la chiave privata effimera viene scartata. Non viene mai scritta su disco, non è nota ai servizi di sigstore, non esiste più passati i pochi minuti necessari. Sparisce così l’intero problema della custodia: non c’è una chiave di lunga durata da proteggere, ruotare o temere di perdere, perché la chiave è vissuta giusto il tempo di una firma. La firma che ne resta non porta con sé un segreto da difendere, ma il riferimento a un’identità e a un certificato che chiunque può controllare.

C’è un di più che questo modello rende possibile, ed è forse il suo aspetto più potente. Quando la firma avviene dentro una pipeline automatica, il certificato non lega l’artefatto a una persona generica, ma al contesto preciso della build: quale flusso di lavoro, in quale repository, su quale ramo e quale commit lo ha prodotto e firmato. La verifica può quindi pretendere non solo che l’artefatto sia firmato da qualcuno di fidato, ma che sia stato costruito e firmato esattamente da quel flusso di lavoro, in quel repository e da quel ramo: una garanzia di provenienza che una firma tradizionale non avrebbe mai potuto esprimere.

## sigstore e il registro pubblico: Rekor sposta la fiducia

Il pezzo che tiene insieme il tutto è il registro di trasparenza, chiamato Rekor. Ogni evento di firma, con la firma stessa, il certificato e l’impronta dell’artefatto, viene scritto in un registro pubblico, ad accodamento e a prova di manomissione: una volta inserita, una voce non può più essere modificata, e l’integrità del registro è verificabile crittograficamente da chiunque. La [documentazione ...