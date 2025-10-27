---
title: L’attività di WIP26 prende di mira provider di telecomunicazioni in medio oriente
url: https://www.insicurezzadigitale.com/lattivita-di-wip26-prende-di-mira-provider-di-telecomunicazioni-in-medio-oriente/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-22
fetch_date: 2025-10-04T07:44:14.575751
---

# L’attività di WIP26 prende di mira provider di telecomunicazioni in medio oriente

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

# L’attività di WIP26 prende di mira provider di telecomunicazioni in medio oriente

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
21 Febbraio 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/02/596c_shutterstock_1936992973.jpeg)

Si parla di:

Toggle

* [La campagna WIP26](#La_campagna_WIP26)
* [A proposito delle backdoor](#A_proposito_delle_backdoor)
* [In sintesi](#In_sintesi)

I ricercatori hanno identificato un gruppo di attività informatiche, soprannominato WIP26, che prendono di mira i fornitori di telecomunicazioni in Medio Oriente. La particolarità di questo insieme di attività di spionaggio, è la forte dipendenza dall’infrastruttura del cloud pubblico, tra cui Microsoft Azure, Microsoft 365 Mail, Google Firebase e Dropbox per l’esfiltrazione di dati, la consegna di malware e operatività C2 (comando e controllo).

## La campagna WIP26

Uno [studio collaborativo](https://www.sentinelone.com/labs/wip26-espionage-threat-actors-abuse-cloud-infrastructure-in-targeted-telco-attacks/) sul malware e sull’infrastruttura utilizzata da WIP26 afferma che si tratta di una missione di raccolta di informazioni con avversari che utilizzano il traffico di rete da servizi cloud legittimi, sfruttandolo per nascondersi dietro di esso.

**L’attacco inizia con un messaggio WhatsApp** inviato ai dipendenti dell’organizzazione presa di mira.

Questo messaggio contiene un **collegamento Dropbox** a un file di archivio, che finge di essere un documento sui problemi legati alla povertà in Medio Oriente.

L’archivio contiene il suddetto documento e un payloader di malware (PDFelement.exe) mascherato da applicazione PDFelement.

Questo caricatore è progettato per rilasciare backdoor personalizzate tra cui **CMD365** e **CMDEmber**.

## A proposito delle backdoor

I ricercatori [hanno rilevato](https://thehackernews.com/2023/02/new-threat-actor-wip26-targeting.html) diversi campioni CMD365 o CMDEmber che abusano di Google Firebase e Microsoft 365 Mail per svolgere compiti C2 ed eseguono i comandi ricevuti dagli aggressori sul sistema compromesso.

**CMD365** è un eseguibile .NET (denominato Update.exe) che finge di essere una vera applicazione Postman. Crea un’attività pianificata sul sistema infetto per garantire la persistenza. Inoltre, è in grado di esfiltrare i dati, escalation dei privilegi, ricognizione e staging di malware aggiuntivo.

**CMDEmber**, un altro eseguibile .NET (denominato Launcher.exe) si maschera da browser Opera. Utilizza la libreria Firebase open source per interagire con le istanze di Google Firebase tramite richieste HTTP.

Il suo compito è sottrarre i dati del browser e le informazioni di ricognizione degli host di alto valore, scelte dagli operatori. Questi dati vengono trasmessi alle istanze di Azure controllate dal gruppo tramite i comandi di PowerShell.

## In sintesi

Gli attacchi di spionaggio alle organizzazioni mediorientali non sono nuovi. Tuttavia, ciò che distingue questo è **l’uso massiccio dell’infrastruttura di cloud pubblico** da parte di WIP26, che indica che si vuole eseguire attacchi senza sollevare alcuna bandiera rossa. Per proteggersi da attacchi così sofisticati, i ricercatori suggeriscono di tenere aggiornati con le ultime attività informatiche in tutto il settore e di sfruttare una piattaforma di intelligence sulle minacce che soddisfi le proprie esigenze, nel controllo del perimetro anche attraverso la ricerca OSINT.

##### < tags />

[cyberspionaggio](https://insicurezzadigitale.com/tag/cyberspionaggio/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[malware](https://insicurezzadigitale.com/tag/malware/)[WIP26](https://insicurezzadigitale.com/tag/wip26/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=L%26%238217%3Battivit%C3%A0+di+WIP26+prende+di+mira+provider+di+telecomunicazioni+in+medio+oriente&url=https://insicurezzadigitale.com/lattivita-di-wip26-prende-di-mira-provider-di-telecomunicazioni-in-medio-oriente/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/lattivita-di-wip26-prende-di-mira-provider-di-telecomunicazioni-in-medio-oriente/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/lattivita-di-wip26-prende-di-mira-provider-di-telecomunicazioni-in-medio-oriente/&title=L%26%238217%3Battivit%C3%A0+di+WIP26+prende+di+mira+provider+di+telecomunicazioni+in+medio+oriente)

[== articolo precedente ==](https://insicurezzadigitale.com/hyundai-e-kia-challenge-per-rubare-le-auto-con-bug-immobilizer/)

[:: articolo successivo ::](https://insicurezzadigitale.com/attacco-informatico-russo-allitalia-ma-anche-meno/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/lattivita-di-wip26-prende-di-mira-provider-di-telecomunicazioni-in-medio-oriente/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *L’attività di WIP26 prende di mira provider di telecomunicazioni in medio oriente*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=L’attività+di+WIP26+prende+di).
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
* [Cookie Poli...