---
title: Rsync: cos’è e come usarlo per creare backup dati sincronizzati sotto sistemi Linux
url: https://www.cybersecurity360.it/soluzioni-aziendali/rsync-cose-e-come-usarlo-per-creare-backup-dati-sincronizzati-in-cartelle-locali-e-remote/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-09
fetch_date: 2025-10-06T22:07:44.423377
---

# Rsync: cos’è e come usarlo per creare backup dati sincronizzati sotto sistemi Linux

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Rsync: cos’è e come usarlo per creare backup dati sincronizzati sotto sistemi Linux

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

LA GUIDA PRATICA

# Rsync: cos’è e come usarlo per creare backup dati sincronizzati sotto sistemi Linux

---

[Home](https://www.cybersecurity360.it)

[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)

---

Indirizzo copiato

---

Rsync è un tool open source che consente di effettuare in maniera semplice ed efficiente il backup dei dati sincronizzando i file e le cartelle tra la directory sorgente e la directory di destinazione, sia in locale che in remoto. Ecco come

Pubblicato il 8 apr 2025

---

[Fabio Ferraro](https://www.cybersecurity360.it/giornalista/fabio-ferraro/)

Consulente informatico

[Daniele Marino](https://www.cybersecurity360.it/giornalista/daniele-marino/)

Programmatore Web

---

---

![rsync per creare backup dati sincronizzati](data:image/png;base64...)![rsync per creare backup dati sincronizzati](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2021/12/rsync.jpg)

#### rsync sotto sistemi Linux: come si fa il backup dei dati

---

Importanza del Backup e di rsync: Il backup dei dati è una componente essenziale del piano di Disaster Recovery per proteggere i dati aziendali. Rsync è un software economico e professionale per il backup remoto e locale, che consente la sincronizzazione efficiente dei file attraverso il mirroring e il trasferimento incrementale.

Funzionalità di rsync: Rsync sostituisce i comandi cp e scp, offre una perfetta integrazione con il protocollo SSH per una sessione remota sicura e supporta la creazione di copie specchiate di directory sia in locale che su host remoti. L’articolo spiega come usare rsync e le opzioni disponibili per personalizzare i backup.

Pianificazione e automazione del Backup: Utilizzando cron, è possibile pianificare backup automatici senza intervento manuale, evitando l’interruzione della procedura di backup. Viene spiegato come configurare rsync per eseguire backup pianificati, inclusa la creazione e gestione di chiavi SSH per un accesso sicuro senza password.

---

Il [**backup dei dati**](https://www.cybersecurity360.it/soluzioni-aziendali/backup-dei-dati-cose-a-cosa-serve-e-le-soluzioni-per-farlo-anche-sul-cloud/) rappresenta la **prima politica informatica** anche nel piano di [Disaster Recovery](https://www.cybersecurity360.it/tag/disaster-recovery/) **per salvaguardare i dati utilizzati all’interno del processo produttivo**, in modo da eseguirne l’eventuale ripristino in caso di necessità.

Ad esempio in seguito a un [attacco ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/attacchi-ransomware-aziende-italiane-oggi/): è necessario progettare una soluzione ottimale che sia un giusto compromesso tra i dispositivi hardware e i software presenti nell’infrastruttura ICT e il potenziale economico aziendale in termini di budget da destinare alla salvaguardia delle informazioni aziendali.

Una delle soluzioni software che ci consente di eseguire il salvataggio dei dati in modo professionale ma nello stesso tempo economico è il tool **rsync** da remote synchronization.

Indice degli argomenti

* [Cos’è rsync e perché usare questo software per il backup in remoto](#Cose_rsync_e_perche_usare_questo_software_per_il_backup_in_remoto)
  + [Prerequisiti per creare un sistema di backup con rsync](#Prerequisiti_per_creare_un_sistema_di_backup_con_rsync)
* [Come installare rsync](#Come_installare_rsync)
* [Sintassi e opzioni per installare rsync](#Sintassi_e_opzioni_per_installare_rsync)
* [Come effettuare un backup in una cartella locale](#Come_effettuare_un_backup_in_una_cartella_locale)
* [Come effettuare un backup in una cartella remota](#Come_effettuare_un_backup_in_una_cartella_remota)
* [Pianificare una procedura di backup con rsync](#Pianificare_una_procedura_di_backup_con_rsync)
* [Storage del backup su Cloud](#Storage_del_backup_su_Cloud)
* [pCloud: il Cloud rigoroso](#pCloud_il_Cloud_rigoroso)
* [Internxt: Cloud attento alla privacy](#Internxt_Cloud_attento_alla_privacy)

## Cos’è rsync e perché usare questo software per il backup in remoto

rsync è un tool gratuito rilasciato sotto licenza GNU GPL che consente attraverso la programmazione da riga di comando (ed eventualmente inserito in uno script) di effettuare in modo snello (anche in termini di manutenzione nel caso sia necessaria la modifica della configurazione dei device interessati nel processo di salvataggio dei dati) il backup dei dati sincronizzando i file e...