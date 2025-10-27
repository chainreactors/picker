---
title: Router wireless Robustel minacciati da nove bug, aggiornare subito
url: https://www.insicurezzadigitale.com/router-wireless-robustel-minacciati-da-nove-bug-aggiornare-subito/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-14
fetch_date: 2025-10-03T19:52:28.181053
---

# Router wireless Robustel minacciati da nove bug, aggiornare subito

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

[Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)

# Router wireless Robustel minacciati da nove bug, aggiornare subito

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
13 Ottobre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/10/Robustel-R3000-Family.png)

Cisco Talos ha [recentemente scoperto](https://blog.talosintelligence.com/2022/10/vuln-spotlight-robustel-router.html) nove vulnerabilità nel router cellulare industriale **Robustel R1510**, alcune delle quali potrebbero portare ad attacchi RCE e DoS.

Robustel R1510 è un router wireless a doppia porta Ethernet che condivide segnali wireless 3G e 4G per applicazioni industriali e IoT.

Include l’uso del tunneling VPN aperto, una piattaforma di gestione basata su cloud per altri dispositivi e router e varie soluzioni di sicurezza.

I ricercatori hanno notato che cinque vulnerabilità RCE possono essere attivate inviando una richiesta di rete appositamente predisposta al dispositivo di destinazione: [TALOS-2022-1578](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1578) (CVE-2022-34850), [TALOS -2022-1577](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1577) (CVE-2022-33150), [TALOS-2022-1576](https://talosintelligence.com/vulnerability_reports/TALOS-%202022-1576) (CVE-2022-32765), [TALOS-2022-1573](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1573) (CVE-2022-33325 – CVE-2022-33329) e [TALOS-2022-1572](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1572) (CVE-2022-33312 – CVE-2022-33314).

Tutti sono state contrassegnate con un punteggio di gravità CVSS di 9,1 su 10.

Gli altri due [TALOS-2022-1580](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1580) (CVE-2022-34845) e [TALOS-2022-1570](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1570) (CVE-2022-32585) possono permettere attacchi RCE, ma da pannello di amministrazione.

Un utente malintenzionato potrebbe anche inviare una richiesta di rete appositamente predisposta per attivare [TALOS-2022-1575](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1575) (CVE-2022-35261 – CVE-2022-35271) e causare un **Denial of Service** nella funzione *hashFirst* del server web del dispositivo.

La vulnerabilità [TALOS-2022-1571](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1571) (CVE-2022-28127) è presente in un server web del dispositivo, ma può invece essere sfruttata per eliminare file arbitrari, nonostante ci sia un controllo di lettura del percorso.

Cisco Talos ha collaborato con Robustel per fornire una soluzione ai problemi identificati e agli aggiornamenti per i clienti interessati.

Si consiglia quindi di aggiornare i prodotti **Robustel R1510** interessati all’ultima *versione 3.3.0 e 3.1.16* il prima possibile per evitare che queste vulnerabilità, vengano attivamente sfruttate in attacchi mirati.

##### < tags />

[bugs](https://insicurezzadigitale.com/tag/bugs/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[robustel](https://insicurezzadigitale.com/tag/robustel/)[router](https://insicurezzadigitale.com/tag/router/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Router+wireless+Robustel+minacciati+da+nove+bug%2C+aggiornare+subito&url=https://insicurezzadigitale.com/router-wireless-robustel-minacciati-da-nove-bug-aggiornare-subito/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/router-wireless-robustel-minacciati-da-nove-bug-aggiornare-subito/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/router-wireless-robustel-minacciati-da-nove-bug-aggiornare-subito/&title=Router+wireless+Robustel+minacciati+da+nove+bug%2C+aggiornare+subito)

[== articolo precedente ==](https://insicurezzadigitale.com/ministero-della-difesa-del-messico-un-data-breach-con-implicazioni-nella-sorveglianza-di-massa/)

[:: articolo successivo ::](https://insicurezzadigitale.com/trapelato-database-con-informazioni-di-monitoraggio-sui-droni/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/router-wireless-robustel-minacciati-da-nove-bug-aggiornare-subito/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Router wireless Robustel minacciati da nove bug, aggiornare subito*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Router+wireless+Robustel+minacciati+da).
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

© 2025 (in)sicurezza digitale. Tutti i diritti riservati.