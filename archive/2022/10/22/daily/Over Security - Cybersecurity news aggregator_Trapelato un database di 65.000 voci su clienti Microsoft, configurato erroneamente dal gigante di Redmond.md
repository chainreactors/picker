---
title: Trapelato un database di 65.000 voci su clienti Microsoft, configurato erroneamente dal gigante di Redmond
url: https://www.insicurezzadigitale.com/trapelato-un-database-di-65-000-voci-su-clienti-microsoft-configurato-erroneamente-dal-gigante-di-redmond/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-22
fetch_date: 2025-10-03T20:37:32.059446
---

# Trapelato un database di 65.000 voci su clienti Microsoft, configurato erroneamente dal gigante di Redmond

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

[Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)

# Trapelato un database di 65.000 voci su clienti Microsoft, configurato erroneamente dal gigante di Redmond

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
21 Ottobre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/10/microsoft-power-apps-data-leak-fallout-38-million-records-exposed-state-and-city-governments-among-those-breached_1500-1024x587.jpg)

La storia si è trasformata in una diatriba di opinioni e smentite, con conseguenti minimizzazioni che forse non fanno molto bene alla consapevolezza su temi cyber, oggi molto bassa. Invece la perdita è ingente e il lavoro di SOCRadar lo dimostra

I ricercatori di SOCRadar hanno registrato e segnalato una perdita di informazioni riservate dei clienti Microsoft, resa possibile da **server mal configurati accessibili via Internet**.

L’incidente è stato [identificato](https://msrc-blog.microsoft.com/2022/10/19/investigation-regarding-misconfigured-microsoft-storage-location-2) il 24 settembre 2022. Una configurazione errata ha comportato un potenziale accesso senza autenticazione ad alcuni dati delle transazioni aziendali relativi alle interazioni tra Microsoft e potenziali clienti.

L’[indagine](https://socradar.io/sensitive-data-of-65000-entities-in-111-countries-leaked-due-to-a-single-misconfigured-data-bucket/) non ha riscontrato alcuna indicazione sul fatto che gli account o i sistemi dei clienti fossero stati compromessi.

Secondo Microsoft, le informazioni divulgate includono **nomi, indirizzi e-mail, contenuto e-mail, nome dell’azienda e numeri di telefono** e dettagli sui clienti dell’azienda.

Redmond ha affermato che la fuga di notizie è stata causata da un’errata configurazione inconsapevole di un endpoint non utilizzato nell’ecosistema Microsoft e non da una vulnerabilità di sicurezza. Errore umano dunque.

A sua volta, SOCRadar ha segnalato che i dati sono stati archiviati nell’[archivio](https://socradar.io/sensitive-data-of-65000-entities-in-111-countries-leaked-due-to-a-single-misconfigured-data-bucket/) BLOB identificato contenente informazioni riservate su 65.000 oggetti provenienti da 111 paesi, datate dal 2017 ad agosto 2022.

Secondo l’analisi, i dati trapelati includono Proof of Implementation e Terms of Reference, informazioni sugli utenti, ordini/offerte di prodotti, dettagli del progetto, dati su informazioni personali e documenti che potrebbero rivelare la proprietà intellettuale.

Microsoft ha ribattuto (minimizzato) e ha aggiunto di ritenere che SOCRadar abbia esagerato grossolanamente la portata e i numeri del problema.

Tuttavia SOCRadar segnala che solo sul server sono stati trovati 2,4 TB di dati contenenti informazioni sensibili, con oltre 335.000 e-mail, 133.000 progetti e 548.000 utenti non protetti.

Inoltre, Redmond è estremamente indignato dalla decisione di SOCRadar di raccogliere dati e renderli ricercabili attraverso un portale dedicato, [BlueBleed](https://socradar.io/labs/bluebleed). Per questo ha approfittato della situazione per ribadire che l’attività non è nel migliore interesse della privacy o della sicurezza dei clienti e li espone potenzialmente a rischi inutili, questa la convinzione di Microsoft.

##### < tags />

[databreach](https://insicurezzadigitale.com/tag/databreach/)[infosec](https://insicurezzadigitale.com/tag/infosec/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Trapelato+un+database+di+65.000+voci+su+clienti+Microsoft%2C+configurato+erroneamente+dal+gigante+di+Redmond&url=https://insicurezzadigitale.com/trapelato-un-database-di-65-000-voci-su-clienti-microsoft-configurato-erroneamente-dal-gigante-di-redmond/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/trapelato-un-database-di-65-000-voci-su-clienti-microsoft-configurato-erroneamente-dal-gigante-di-redmond/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/trapelato-un-database-di-65-000-voci-su-clienti-microsoft-configurato-erroneamente-dal-gigante-di-redmond/&title=Trapelato+un+database+di+65.000+voci+su+clienti+Microsoft%2C+configurato+erroneamente+dal+gigante+di+Redmond)

[== articolo precedente ==](https://insicurezzadigitale.com/sabato-22-ottobre-e-linux-day-la-manifestazione-anche-a-cagliari/)

[:: articolo successivo ::](https://insicurezzadigitale.com/il-ransomware-non-e-cambiato-e-gli-attacchi-continuano-a-non-venir-arginati/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/trapelato-un-database-di-65-000-voci-su-clienti-microsoft-configurato-erroneamente-dal-gigante-di-redmond/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Trapelato un database di 65.000 voci su clienti Microsoft, configurato erroneamente dal gigante di Redmond*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Trapelato+un+database+di+65.000).
Condividi esempi, IOCs o tecniche di detection efficaci nel nostro 👉 [**forum community**](https://forum.ransomfeed.it/)

## [[ mastodon ]]

Su Mastodon mi trovi qui: [Mastodon](https://poliversity.it/%40nuke)

### :: i social ::

* [Facebook](https://www.facebook.com/spcnet.it)
* [Instagram](https://www.instagram.com/spcnet.it/)
* [Twitter](https://twitter.com/nuke86)
* [Linkedin](https://www.linkedin.com/in/dariofadda86/)

## == forum community ==

💬 Partecipa alla community con i nostri [Forum](https://forum.ransomfeed.it), unico spazio per tutto il Network!

### ~~ il network ~~

* [Spcnet.it](https://www.spcnet.it/)
* [ZioBudda.org](https://www.ziobudda.org)
* [dariofadda.it](https://dariofadda.it)
* [SecureBulletin.com](https://securebulletin.com)

### [[ NINAsec - la newsletter ]]

##### (in)sicurezza digitale

Notizie cybersecurity, malware, ransomware e sicurezza dei dati

Cerca

##### :: navigazione ::

* [A proposito di…](https://insicurezzadigitale.com/chi-siamo/)
* [La stampa dice](https://insicurezzadigitale.com/la-stampa-dice/)
* [Privacy Policy](https://insicurezzadigitale.com/privacy-policy/)
* [Cookie Policy](https://insicurezzadigitale.com/cookie-policy/)

##### ~~ contatti ~~

* info@spcnet.it
* [Whistleblowing](/whistleblowing/)
* [DarioFadda.it](https://me.dariofadda.it/)

---

© 2025 (in)sicurezza d...