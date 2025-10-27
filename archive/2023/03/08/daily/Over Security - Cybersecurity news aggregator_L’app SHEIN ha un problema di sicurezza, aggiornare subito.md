---
title: L’app SHEIN ha un problema di sicurezza, aggiornare subito
url: https://www.insicurezzadigitale.com/lapp-shein-ha-un-problema-di-sicurezza-aggiornare-subito/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-08
fetch_date: 2025-10-04T08:56:31.647008
---

# L’app SHEIN ha un problema di sicurezza, aggiornare subito

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

# L’app SHEIN ha un problema di sicurezza, aggiornare subito

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
7 Marzo 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/03/SHEIN_LOGO_Logo-1024x538.jpg)

SHEIN Logo (PRNewsfoto/SHEIN)

È stato identificato un importante bug di sicurezza in una versione Android della nota applicazione di shopping, SHEIN.

Il problema potrebbe raccogliere e inviare il contenuto in memoria degli appunti (copia/incolla, detta clipboard), ad un server esterno.

Secondo il [team di ricerca di Microsoft 365 Defender](https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/), la vulnerabilità è stata riscontrata nell’aggiornamento 7.9.2 dell’app, che venne reso disponibile il 16 dicembre 2021. A partire da maggio 2022, il problema è stato risolto.

Il negozio cinese di fast fashion online [Shein](https://play.google.com/store/apps/details?id=com.zzkko&hl=en&gl=US), precedentemente noto come ZZKKO, ha sede a Singapore. Quasi 100 milioni di persone hanno scaricato l’app Android, che è alla versione 9.0.0 ed è disponibile su Google Play Store.

La ricerca ha fatto notare che all’apertura del programma dopo aver copiato qualsiasi contenuto negli appunti del dispositivo, viene generata una richiesta HTTP POST contenente i dati copiati, che viene inviata automaticamente al server “api-service[.]shein[.]com”.

**Una vista al codice incriminato**

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/Figure-6.-Method-com.zzkko_.app_.BaseActivityCallBack.k-initiating-a-flow-which-performs-a-POST-request-to-the-server-at-BaseUrlConstant.APP_URL-marketingtinyurlphrase-2-1024x199-1.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/Figure-6.-Method-com.zzkko_.app_.BaseActivityCallBack.k-initiating-a-flow-which-performs-a-POST-request-to-the-server-at-BaseUrlConstant.APP_URL-marketingtinyurlphrase-2-1024x199-1.png)

Il metodo *com.zzkko.app.BaseActivityCallBack.k* che avvia un flusso, che esegue una richiesta POST al server in *BaseUrlConstant.APP\_URL* + ” */marketing/tinyurl/phrase*” che, al netto delle variabili, si risolve in *https://api-service[.]shein[ .]com/marketing/tinyurl/frase*

## Il bug su SHEIN è pericoloso perché può spianare la strada ai malintenzionati

In effetti il fatto grave è proprio nell’abuso di questa vulnerabilità, come sempre accade nel caso di problemi di sicurezza in app largamente utilizzate. Il grande pubblico dietro questa app, amplia notevolmente la superficie d’attacco per utenti malintenzionati.

I contenuti delle clipboard (così si chiamano le memorie che vengono alimentate quando copiamo un contenuto testuale, prima di incollarlo), sono sempre presi di mira e ambiti dai cyber criminali, perché consapevolmente tutti sanno quanto questa funzionalità viene utilizzata dagli utenti. Copiamo numeri di carte di credito, nomi, password, codici, indirizzi. Tutto viene copiato e incollato, nell’arco delle nostre giornate, all’interno dei nostri dispositivi.

Avere un dispositivo di questo tipo, contenente una app che a nostra insaputa fa transitare online i contenuti che l’utente copia in memoria, è senza dubbio un problema sensibile, proprio per il fatto che possono essere intercettate e abusate contro l’utente.

##### < tags />

[android](https://insicurezzadigitale.com/tag/android/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[SHein](https://insicurezzadigitale.com/tag/shein/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=L%26%238217%3Bapp+SHEIN+ha+un+problema+di+sicurezza%2C+aggiornare+subito&url=https://insicurezzadigitale.com/lapp-shein-ha-un-problema-di-sicurezza-aggiornare-subito/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/lapp-shein-ha-un-problema-di-sicurezza-aggiornare-subito/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/lapp-shein-ha-un-problema-di-sicurezza-aggiornare-subito/&title=L%26%238217%3Bapp+SHEIN+ha+un+problema+di+sicurezza%2C+aggiornare+subito)

[== articolo precedente ==](https://insicurezzadigitale.com/in-vendita-dati-interni-di-acer-potrebbe-essere-un-riciclo-di-dati-del-2021/)

[:: articolo successivo ::](https://insicurezzadigitale.com/ninasec-analisi-di-apt29-e-loperazione-contro-la-commissione-europea/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/lapp-shein-ha-un-problema-di-sicurezza-aggiornare-subito/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *L’app SHEIN ha un problema di sicurezza, aggiornare subito*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=L’app+SHEIN+ha+un+problema).
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