---
title: Cyber spionaggio “cinese”, l’infezione parte dai dispositivi USB
url: https://www.insicurezzadigitale.com/cyber-spionaggio-cinese-linfezione-parte-dai-dispositivi-usb/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-30
fetch_date: 2025-10-04T00:06:13.380545
---

# Cyber spionaggio “cinese”, l’infezione parte dai dispositivi USB

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

# Cyber spionaggio “cinese”, l’infezione parte dai dispositivi USB

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
29 Novembre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/11/Chinese-Cyber-Espionage-980x300-1.jpg)

Mandiant segnala la scoperta di una campagna di spionaggio informatico che **utilizza i dispositivi USB come vettore iniziale** di infezione.

L’attore è **geolocalizzato nelle Filippine** e viene tracciato dai ricercatori come **UNC4191**, che associano alla RPC (Repubblica Popolare Cinese). La campagna stessa **è potenzialmente riconducibile fino a settembre 2021**, a giudicare dalle date (timestamp) tracciate sulle compilazioni del file binari (più di un anno di attività).

Le operazioni dell’UNC4191 hanno interessato una serie di organizzazioni del settore pubblico e privato, principalmente nel sud-est asiatico, ma anche negli Stati Uniti e in Europa, nelle cui infrastrutture, i sistemi target si trovavano però fisicamente nelle Filippine.

Dopo aver inizialmente infettato tramite dispositivi USB, l’aggressore ha utilizzato binari firmati legalmente per scaricare malware, inclusi tre nuovi ceppi: **MISTCLOAK, DARKDEW e BLUEHAZE**, che riflettono le fasi del ciclo di infezione complessivo di questa campagna.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/unc4191-malware-infection-1024x643.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/unc4191-malware-infection.png)

La catena di infezione inizia quando un utente monta un dispositivo rimovibile compromesso ed esegue manualmente un file binario firmato e rinominato dalla directory principale del volume di archiviazione.

I file binari di origine denominati Removable Drive.exe o USB Drive.exe sono versioni di un’applicazione legalmente firmata denominata **USB Network Gate** sviluppata da *Electronic Team, Inc*. Vengono utilizzati per trasferire il malware MISTCLOAK che finge di essere una DLL.

**MISTCLOAK** è un launcher scritto in C++ che esegue un payload eseguibile crittografato memorizzato in un file su disco, avviando in effetti un file *usb.ini* crittografato.

Il file **usb.ini** contiene un payload DLL crittografato chiamato **DARKDEW**, un dropper C++ in grado di infettare i supporti rimovibili implementando un metodo di auto-replicazione e trasferimento file.

Il passaggio finale utilizza **BLUEHAZE**, un launcher scritto in C/C++ che avvia una copia dell’utilità di rete NCAT (scritta per Nmap per eseguire un’ampia gamma di attività di sicurezza e amministrazione) per creare un wrapper di comando e controllo codificati (C2), che **fornisce all’attaccante l’accesso backdoor**.

Pertanto, il malware si auto-replica infettando nuove unità rimovibili connesse al sistema compromesso, consentendo al payload del malware di propagarsi a sistemi aggiuntivi e, potenzialmente, raccogliere dati da sistemi air-gap.

![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/Screenshot-2022-11-29-at-22-44-12-Always-Another-Secret-Lifting-the-Haze-on-China-nexus-Espionage-in-Southeast-Asia-Mandiant.png)

Gli indicatori di compromissione e YARA vengono presentati in dettaglio nel [report](https://www.mandiant.com/resources/blog/china-nexus-espionage-southeast-asia), dai ricercatori.

##### < tags />

[cybercrime](https://insicurezzadigitale.com/tag/cybercrime/)[cyberspionaggio](https://insicurezzadigitale.com/tag/cyberspionaggio/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[USB](https://insicurezzadigitale.com/tag/usb/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Cyber+spionaggio+%26%238220%3Bcinese%26%238221%3B%2C+l%26%238217%3Binfezione+parte+dai+dispositivi+USB&url=https://insicurezzadigitale.com/cyber-spionaggio-cinese-linfezione-parte-dai-dispositivi-usb/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/cyber-spionaggio-cinese-linfezione-parte-dai-dispositivi-usb/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/cyber-spionaggio-cinese-linfezione-parte-dai-dispositivi-usb/&title=Cyber+spionaggio+%26%238220%3Bcinese%26%238221%3B%2C+l%26%238217%3Binfezione+parte+dai+dispositivi+USB)

[== articolo precedente ==](https://insicurezzadigitale.com/shopping-di-natale-e-aumento-delle-frodi-informatiche/)

[:: articolo successivo ::](https://insicurezzadigitale.com/quando-il-sistema-di-sicurezza-trasforma-la-nostra-casa-in-un-data-breach-il-caso-brinks/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/cyber-spionaggio-cinese-linfezione-parte-dai-dispositivi-usb/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Cyber spionaggio “cinese”, l’infezione parte dai dispositivi USB*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Cyber+spionaggio+“cinese”,+l’infezione+parte).
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

© 2025 (in)sicurezz...