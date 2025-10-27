---
title: La combinazione di CVE e nuovi problemi software nel demone Multipathd, favoriscono escalation di privilegi
url: https://www.insicurezzadigitale.com/la-combinazione-di-cve-e-nuovi-problemi-software-nel-demone-multipathd-favoriscono-escalation-di-privilegi/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-06
fetch_date: 2025-10-04T00:35:41.576383
---

# La combinazione di CVE e nuovi problemi software nel demone Multipathd, favoriscono escalation di privilegi

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

# La combinazione di CVE e nuovi problemi software nel demone Multipathd, favoriscono escalation di privilegi

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
5 Dicembre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/12/index.jpeg)

Qualys Threat Research ha dimostrato come collegare una vulnerabilità in Linux ad altri due difetti apparentemente innocui al fine di ottenere privilegi di root sul sistema interessato.

La nuova vulnerabilità viene tracciata come **CVE-2022-3328** e interessa **snap-confine** di Snapd, uno strumento sviluppato da Canonical utilizzato per creare un ambiente di runtime per le applicazioni software Snap.

Il programma predefinito è presente in Ubuntu, i cui appunto sviluppatori hanno censito la [CVE-2022-3328](https://ubuntu.com/security/CVE-2022-3328) come una grave vulnerabilità che può essere sfruttata per l’escalation dei privilegi locali e RCE.

I ricercatori di Qualys sono stati in grado di combinare CVE-2022-3328 con due problemi scoperti di recente che interessano **Multipathd** per lanciare un potente attacco.

Multipathd è il demone di controllo del percorso che viene eseguito come root su un’installazione standard di Ubuntu e altre distribuzioni (maggiormente Debian-like).

Multipathd è interessato da un [problema di bypass](https://www.qualys.com/2022/10/24/leeloo-multipath/leeloo-multipath.txt) dell’autorizzazione che un utente senza privilegi può utilizzare per eseguire comandi da root in Multipathd (CVE- 2022-41974) e un problema sui collegamenti simbolici (CVE-2022-41973) che può essere sfruttato per RCE (Esecuzione di Codice Remoto).

La combinazione di una vulnerabilità Snapd con due difetti Multipathd **potrebbe consentire a qualsiasi utente senza privilegi di ottenere privilegi di root** su un dispositivo vulnerabile.

Di conseguenza, Qualys ha sviluppato un exploit che consente di ottenere privilegi di super utente completi durante l’installazione predefinita di Ubuntu.

Sebbene la vulnerabilità non possa essere sfruttata da remoto, i ricercatori avvertono che un utente non privilegiato potrebbe sfruttarla, all’interno di una struttura fisica.

Qualys ha fornito un avviso con [informazioni tecniche](https://www.qualys.com/2022/11/30/cve-2022-3328/advisory-snap.txt) dettagliate e ha deciso di non rilasciare il PoC data la sensibilità del risultato potenziale.

##### < tags />

[bug](https://insicurezzadigitale.com/tag/bug/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[ubuntu](https://insicurezzadigitale.com/tag/ubuntu/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=La+combinazione+di+CVE+e+nuovi+problemi+software+nel+demone+Multipathd%2C+favoriscono+escalation+di+privilegi&url=https://insicurezzadigitale.com/la-combinazione-di-cve-e-nuovi-problemi-software-nel-demone-multipathd-favoriscono-escalation-di-privilegi/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/la-combinazione-di-cve-e-nuovi-problemi-software-nel-demone-multipathd-favoriscono-escalation-di-privilegi/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/la-combinazione-di-cve-e-nuovi-problemi-software-nel-demone-multipathd-favoriscono-escalation-di-privilegi/&title=La+combinazione+di+CVE+e+nuovi+problemi+software+nel+demone+Multipathd%2C+favoriscono+escalation+di+privilegi)

[== articolo precedente ==](https://insicurezzadigitale.com/quando-il-sistema-di-sicurezza-trasforma-la-nostra-casa-in-un-data-breach-il-caso-brinks/)

[:: articolo successivo ::](https://insicurezzadigitale.com/il-belgio-sbatte-contro-il-ransomware-anversa-ricorre-a-carta-e-penna/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/la-combinazione-di-cve-e-nuovi-problemi-software-nel-demone-multipathd-favoriscono-escalation-di-privilegi/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *La combinazione di CVE e nuovi problemi software nel demone Multipathd, favoriscono escalation di privilegi*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=La+combinazione+di+CVE+e).
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