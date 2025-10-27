---
title: Crocodilus: l’evoluzione di un trojan bancario Android che minaccia le criptovalute a livello globale
url: https://www.insicurezzadigitale.com/crocodilus-levoluzione-di-un-trojan-bancario-android-che-minaccia-le-criptovalute-a-livello-globale/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-04
fetch_date: 2025-10-06T22:54:45.067891
---

# Crocodilus: l’evoluzione di un trojan bancario Android che minaccia le criptovalute a livello globale

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

# Crocodilus: l’evoluzione di un trojan bancario Android che minaccia le criptovalute a livello globale

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
3 Giugno 2025

![](https://insicurezzadigitale.com/wp-content/uploads/2025/06/GnIISLNWQAAA__v-1024x577.jpg)

Si parla di:

Toggle

* [Tecniche di distribuzione e ingegneria sociale](#Tecniche_di_distribuzione_e_ingegneria_sociale)
* [Evoluzione delle funzionalità](#Evoluzione_delle_funzionalita)
* [Raccomandazioni per la protezione](#Raccomandazioni_per_la_protezione)

Nel marzo 2025, il team di Mobile Threat Intelligence di ThreatFabric ha individuato un nuovo trojan bancario per Android denominato Crocodilus. Inizialmente osservato in campagne di test, il malware ha rapidamente ampliato il suo raggio d’azione, colpendo utenti in Europa e Sud America. Le campagne recenti hanno preso di mira utenti in Polonia, Spagna, Turchia, Argentina, Brasile, Stati Uniti, Indonesia e India, sfruttando tecniche di distribuzione sofisticate come pubblicità ingannevoli su social network, in particolare Facebook.

---

## **Tecniche di distribuzione e ingegneria sociale**

[Crocodilus](https://www.threatfabric.com/blogs/crocodilus-mobile-malware-evolving-fast-going-global) viene distribuito attraverso “dropper” che riescono a bypassare le restrizioni di sicurezza introdotte in Android 13 e versioni successive. Una volta installato, il malware richiede l’attivazione del “Servizio di Accessibilità”, ottenendo così ampi privilegi sul dispositivo. Questi privilegi permettono al malware di:

* Visualizzare sovrapposizioni che imitano interfacce di app bancarie e di criptovalute.
* Registrare le sequenze di tasti e monitorare l’attività sullo schermo.

Una delle tattiche di ingegneria sociale più efficaci utilizzate da Crocodilus è l’invio di messaggi falsi che sollecitano l’utente a eseguire un backup della chiave del portafoglio entro 12 ore, minacciando la perdita di accesso in caso contrario. Questo induce l’utente a navigare verso la seed phrase, che viene poi intercettata dal malware.

---

## **Evoluzione delle funzionalità**

Le versioni più recenti di Crocodilus presentano miglioramenti significativi:

* **Obfuscazione avanzata**: utilizzo di tecniche di packing e crittografia XOR per rendere più difficile l’analisi del codice.
* **Modifica della rubrica**: aggiunta di contatti fittizi, come “Assistenza Bancaria”, per facilitare attacchi di phishing telefonico.
* **Raccolta automatica di seed phrase**: implementazione di parser specifici per estrarre seed phrase e chiavi private da app di portafogli di criptovalute.

Crocodilus rappresenta una minaccia significativa per gli utenti di dispositivi Android, in particolare per coloro che gestiscono portafogli di criptovalute. La sua capacità di eludere le misure di sicurezza, combinata con tecniche di ingegneria sociale sofisticate, lo rende particolarmente pericoloso. Le campagne mirate e l’uso di pubblicità ingannevoli su piattaforme popolari aumentano il rischio di infezione.

---

## **Raccomandazioni per la protezione**

Per mitigare il rischio di infezione da Crocodilus, si consiglia di:

* Scaricare app solo da fonti ufficiali come Google Play Store.
* Evitare di concedere permessi di accessibilità a app non verificate.
* Essere cauti con messaggi che richiedono azioni urgenti, come il backup di chiavi.
* Mantenere aggiornato il sistema operativo e le app installate.
* Utilizzare soluzioni di sicurezza affidabili per dispositivi mobili.

La vigilanza e l’adozione di buone pratiche di sicurezza sono fondamentali per proteggersi da minacce come Crocodilus.

##### < tags />

[android](https://insicurezzadigitale.com/tag/android/)[Crocodilus](https://insicurezzadigitale.com/tag/crocodilus/)[spyware](https://insicurezzadigitale.com/tag/spyware/)[trojan](https://insicurezzadigitale.com/tag/trojan/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Crocodilus%3A+l%E2%80%99evoluzione+di+un+trojan+bancario+Android+che+minaccia+le+criptovalute+a+livello+globale&url=https://insicurezzadigitale.com/crocodilus-levoluzione-di-un-trojan-bancario-android-che-minaccia-le-criptovalute-a-livello-globale/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/crocodilus-levoluzione-di-un-trojan-bancario-android-che-minaccia-le-criptovalute-a-livello-globale/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/crocodilus-levoluzione-di-un-trojan-bancario-android-che-minaccia-le-criptovalute-a-livello-globale/&title=Crocodilus%3A+l%E2%80%99evoluzione+di+un+trojan+bancario+Android+che+minaccia+le+criptovalute+a+livello+globale)

[== articolo precedente ==](https://insicurezzadigitale.com/bitmex-sventa-un-attacco-di-lazarus-e-ne-espone-alcune-debolezze/)

[:: articolo successivo ::](https://insicurezzadigitale.com/cve-2025-45542-problemi-di-sql-injection-in-php-cloudclassroom/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/crocodilus-levoluzione-di-un-trojan-bancario-android-che-minaccia-le-criptovalute-a-livello-globale/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Crocodilus: l’evoluzione di un trojan bancario Android che minaccia le criptovalute a livello globale*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Crocodilus:+l’evoluzione+di+un+trojan).
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

##### (in)sicurezza d...