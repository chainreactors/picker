---
title: BadSuccessor: come mitigare il rischio della vulnerabilità critica in Active Directory
url: https://www.cybersecurity360.it/news/badsuccessor-come-mitigare-il-rischio-della-vulnerabilita-critica-in-active-directory/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-29
fetch_date: 2025-10-06T22:30:10.635668
---

# BadSuccessor: come mitigare il rischio della vulnerabilità critica in Active Directory

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## BadSuccessor: come mitigare il rischio della vulnerabilità critica in Active Directory

* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [twitter](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

patch urgenti

# BadSuccessor: come mitigare il rischio della vulnerabilità critica in Active Directory

---

[Home](https://www.cybersecurity360.it)

[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)

---

Indirizzo copiato

---

L’allarme è un campanello d’allarme per chi si occupa di sicurezza enterprise, anche perché BadSuccessor ha un impatto sistemico e Active Directory rappresenta il cuore pulsante di molte reti aziendali. Ecco come mitigare il rischio, in attesa della patch di Microsoft

Pubblicato il 28 mag 2025

---

[Mirella Castigli](https://www.cybersecurity360.it/giornalista/mirella-castigli/)

Giornalista

---

---

![Sistemi ibridi Active Directory ed Entra ID: come mitigare i rischi legati all'identità](data:image/png;base64...)![Sistemi ibridi Active Directory ed Entra ID: come mitigare i rischi legati all'identità](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2025/01/Active-Directory-attacco-Kerberoasting.jpg)

---

Microsoft ha catalogato **[BadSuccessor](https://www.acn.gov.it/portale/w/badsuccessor-rilevata-vulnerabilita-critica-in-active-directory)**, la **vulnerabilità critica in [Active Directory](https://www.cybersecurity360.it/nuove-minacce/active-directory-cose-e-come-mitigare-authentication-server-response-roasting/)**, come “Moderate Severity”, scoperta subito dopo il [Patch Tuesday](https://www.cybersecurity360.it/news/aggiornamenti-microsoft-maggio-2025-corrette-7-zero-day-di-cui-5-gia-sfruttate-in-rete/) di giugno. Tuttavia non è affatto una falla di severità moderata, al contrario è molto insidiosa.

Infatti “è una red flag per chi si occupa di sicurezza enterprise. Non si parla di una semplice escalation: sfruttando i meccanismi di successor calculation, un attaccante può ottenere privilegi persistenti anche in ambienti già patchati. Dunque non bastano più le patch ufficiali”, commenta **Ada Spinelli**, Security engineer per Maticmind.

Ecco come mitigare il rischio, in attesa della patch ufficiale, mentre “le vulnerabilità evolvono, le minacce si adattano, e quindi anche la protezione può (e deve) fare altrettanto”, secondo **Raul Arisi**, Cybersecurity Marketing Director per Maticmind.

Indice degli argomenti

* [BadSuccessor, la vulnerabilità critica in Active Directory](#BadSuccessor_la_vulnerabilita_critica_in_Active_Directory)
  + [Che cos’è il dMSA (delegated managed service account)](#Che_cose_il_dMSA_delegated_managed_service_account)
  + [L’impatto sistemico di BadSuccessor](#Limpatto_sistemico_di_BadSuccessor)
  + [Perché il rischio è elevato](#Perche_il_rischio_e_elevato)
* [Come mitigare il rischio](#Come_mitigare_il_rischio)

## BadSuccessor, la vulnerabilità critica in Active Directory

Microsoft ha ammesso la vulnerabilità, ma l’ha catalogata come “Moderate Severity” e **la patch non è ancora disponibile**.

Ma il problema è grave “perché BadSuccessor agisce proprio sui meccanismi strutturali dell’Active Directory: i trust, i ticket Kerberos, le ACL (Access Control List), e i dati replicati fra i controller di dominio”, spiega **Ada Spinelli**: “Anche in un ambiente aggiornato, se queste strutture sono deboli o non monitorate, **l’attaccante può infiltrarsi e restare**. Questo dimostra, ancora una volta, quanto i modelli di trust e gestione dei privilegi in AD siano strutturalmente fragili”.

Infatti la vulnerabilità in **dMSA** (delegated managed service account), nuova funzionalità in Windows Server 2025 all’interno di Active Directory (AD), permettete la delega della creazione e della gestione di account di servizio a utenti privi di privilegi. “La presenza di un PoC pubblico e la possibilità di escalation a privilegi di dominio rendono questa criticità degna di massima attenzione operativa”, sottolinea **Andrea Mariucci**, Head of Cyber Defence Center per Maticmind.

### Che cos’è il **dMSA** (delegated managed service account)

Un dMSA permette di rimpiazzare un account di servizio legacy, per facilitare la gestione delle credenziali, tramite l’automatizzazione della gestione delle password e associando l’autenticazione all’identità del device. Per semplificare questa transizione, la configurazione dei dMSA consente di assumere i permessi o le funzionalità legate all’account legacy, via meccanismo di migrazione. Ma **l’abuso di questa opzione permette di attribuire impropriamente **alti**** **privilegi a un nuovo account sot...