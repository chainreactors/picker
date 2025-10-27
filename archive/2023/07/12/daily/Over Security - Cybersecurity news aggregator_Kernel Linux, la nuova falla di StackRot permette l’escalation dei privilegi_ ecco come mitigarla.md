---
title: Kernel Linux, la nuova falla di StackRot permette l’escalation dei privilegi: ecco come mitigarla
url: https://www.cybersecurity360.it/news/kernel-linux-la-nuova-falla-di-stackrot-permette-lescalation-dei-privilegi/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-12
fetch_date: 2025-10-04T11:57:46.589317
---

# Kernel Linux, la nuova falla di StackRot permette l’escalation dei privilegi: ecco come mitigarla

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Kernel Linux, la nuova falla di StackRot permette l’escalation dei privilegi: ecco come mitigarla

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

Memoria del kernel

# Kernel Linux, la nuova falla di StackRot permette l’escalation dei privilegi: ecco come mitigarla

* [Home](https://www.cybersecurity360.it)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)

Il ricercatore di sicurezza Ruihan Li ha scoperto e segnalato la falla nel Kernel Linux. In un post spiega che la vulnerabilità di StackRot riguarda il sottosistema di gestione della memoria del kernel. Ecco come mitigare il rischio

Pubblicato il 11 Lug 2023

[Mirella Castigli](https://www.cybersecurity360.it/giornalista/mirella-castigli/)

Giornalista

![Kernel Linux: la nuova falla di StackRot permette l'escalation dei privilegi](data:image/png;base64...)![Kernel Linux: la nuova falla di StackRot permette l'escalation dei privilegi](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2022/07/Zero-trust-Security-privilegi-minimi.jpg)

Una vulnerabilità riguarda più versioni del Kernel [Linux](https://www.cybersecurity360.it/news/tsunami-botnet-infetta-server-linux-ssh-come-proteggersi/). StackRot (CVE-2023-3269) richiede “capacità minime” per l’attivazione e potrebbe consentire l’**escalation dei privilegi**.

“La falla StackRot (CVE-2023-3269) è estremamente insidiosa”, mette in guardia **Pierluigi Paganini**, analista di cyber security e CEO Cybhorus, “in quanto consente ad un attaccante di compromettere il kernel del sistema operativo e di elevare i propri privilegi”.

“Classificata con un CVSS score pari a 7.9, tale vulnerabilità”, conferma **Antonio Minnella**, Ricercatore Sicurezza di Exprivia, “affligge le versioni del kernel dalla 6.1 alla 6.4 e, se sfruttata con successo, può portare all’esecuzione di codice arbitrario e al privilege escalation fino all’ottenimento dei permessi di
root sulla macchina target”.

**Dal primo luglio è disponibile una patch per i kernel stabili interessati**, dal momento che l’impatto riguarda le configurazioni del kernel nelle versioni di Linux dalla 6.1 alla 6.4. Ecco come mitigare il rischio.

Indice degli argomenti

* [Kernel Linux: la nuova falla di StackRot](#Kernel_Linux_la_nuova_falla_di_StackRot)
  + [I dettagli tecnici](#I_dettagli_tecnici)
  + [La logica di espansione dello stack](#La_logica_di_espansione_dello_stack)
  + [Race condition](#Race_condition)
* [Come mitigare il rischio](#Come_mitigare_il_rischio)

## Kernel Linux: la nuova falla di StackRot

Il ricercatore di sicurezza Ruihan Li ha scoperto e segnalato la falla nel Kernel Linux. In un post spiega che la vulnerabilità di StackRot riguarda il sottosistema di gestione della memoria del kernel, un componente incaricato di implementare la memoria virtuale e demand paging, l’allocazione della memoria per le esigenze del kernel e dei programmi dello spazio utente, oltre alla mappatura dei file nello spazio degli indirizzi dei processi.

StackRot ha infatti un impatto su tutte le configurazioni del kernel nelle versioni di Linux dalla 6.1 alla 6.4. “**A rendere più grave la scoperta della falla è l’annuncio da parte del ricercatore che ha scoperto la vulnerabilità** di **divulgare i dettagli tecnici e di pubblicare un proof-of-concept (PoC) exploit entro la fine di luglio”**, aggiunge Paganini.

Sebbene Li abbia inviato la segnalazione della vulnerabilità a metà giugno, la creazione di una correzione ha richiesto quasi due settimane a causa della sua complessità. “La scoperta risale al 15 giugno scorso e per fixarla ci sono volute due settimane di **duro lavoro da parte del rescue team guidato da Linus Torvalds in persona**. Lo scorso 28 giugno sono state mergiate su git tutte le modifiche e dal 1 luglio sono disponibili una serie di patch per i kernel ‘stable’ (6.1.37, 6.3.11, 6.4.1)”, commenta **Antonio Minnella.**

“Il 28 giugno, durante la finestra di fusione per il kernel Linux 5.5, la correzione è stata inserita nell’albero di Linus. Linus ha fornito un messaggio di fusione completo per chiarire la serie di patch da un punto di vista tecnico. Queste patch sono state successivamente riportate nei kernel stabili (6.1.37, 6.3.11 e 6.4.1), risolvendo di fatto il bug ‘Stack Rot’ il 1° luglio”, ha [chiarito](http://github.com/lrh2000/StackRot) il ricercatore.

### I dettagli tecnici

Entrando nel dettaglio della vulnerabilità, “possiamo constatare che la stessa sia stata introdotta con l’avvento della versione 6.1 del kernel ovvero quando il sottosistema di ...