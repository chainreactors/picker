---
title: Attacchi che sfruttano il sistema MotW di Microsoft, niente patch ufficiali ma arrivano fix di volontari
url: https://www.insicurezzadigitale.com/attacchi-che-sfruttano-il-sistema-motw-di-microsoft-niente-patch-ufficiali-ma-arrivano-fix-di-volontari/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-19
fetch_date: 2025-10-03T20:17:18.913538
---

# Attacchi che sfruttano il sistema MotW di Microsoft, niente patch ufficiali ma arrivano fix di volontari

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

# Attacchi che sfruttano il sistema MotW di Microsoft, niente patch ufficiali ma arrivano fix di volontari

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
18 Ottobre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/10/motw-win10-1024x614.jpeg)

0patch ha rilasciato un fix non ufficiale gratuito per correggere una vulnerabilità zero day ampiamente sfruttata nel meccanismo di sicurezza di Windows **Mark of the Web** (MotW).

Il bug consente agli aggressori di impedire l’applicazione dei controlli di Windows (MotW) ai file estratti da archivi ZIP scaricati da Internet.

Windows aggiunge automaticamente MotW a tutti i documenti e gli eseguibili scaricati da fonti non attendibili, inclusi i file estratti da archivi ZIP scaricati, utilizzando il flusso di dati alternativo Zone.Id, che fa sì che venga visualizzato un avviso all’apertura.

Il problema è stato segnalato a Microsoft a luglio da Will **Dormann** di ANALYGENCE, che per primo ha scoperto che gli archivi ZIP non aggiungevano correttamente i flag MoTW.

https://twitter.com/wdormann/status/1545169168961605634

Microsoft ha esaminato il rapporto più di due mesi fa, ma [non ha ancora rilasciato](https://twitter.com/wdormann/status/1579883432783794182) un aggiornamento per la sicurezza.

Secondo Micropatching Service 0patch, MotW è un importante meccanismo di sicurezza di Windows perché Smart App Control [funzionerà](https://support.microsoft.com/en-us/topic/what-is-smart%20-%20app-control-285ea03d-fa88-4d56-882e-6698afdb7003) solo su file con flag MotW e **Microsoft Office bloccherà solo le macro per i documenti contrassegnati con etichette MotW**.

Pertanto, gli aggressori, per ovvi motivi, preferiscono [bypassare](https://blog.0patch.com/2022/10/free-micropatches-for-bypassing-mark-of.html) tali contrassegni per il loro archivio ZIP, di modo che tutti i file Word o Excel dannosi estratti non verranno contrassegnati correttamente e le macro non verranno quindi bloccate.

Pertanto, senza attendere Microsoft, gli analisti di 0patch hanno sviluppato correzioni per tutte le versioni vulnerabili: Windows 10 v1803 e successive, Windows 7, Windows Server 2008 R2, 2012, 2012 R2, 2016, 2019, 2022.

Si consiglia vivamente ai clienti Microsoft pertanto di sfruttare questa patch direttamente direttamente del fornitore, poiché da quando è stato scoperto lo 0-day a luglio, sembra una vulnerabilità già sfruttata in [attacchi concreti](https://twitter.com/buffaloverflow/status/1579890297185923072) per fornire file dannosi alle vittime.

##### < tags />

[bug](https://insicurezzadigitale.com/tag/bug/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[microsoft](https://insicurezzadigitale.com/tag/microsoft/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Attacchi+che+sfruttano+il+sistema+MotW+di+Microsoft%2C+niente+patch+ufficiali+ma+arrivano+fix+di+volontari&url=https://insicurezzadigitale.com/attacchi-che-sfruttano-il-sistema-motw-di-microsoft-niente-patch-ufficiali-ma-arrivano-fix-di-volontari/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/attacchi-che-sfruttano-il-sistema-motw-di-microsoft-niente-patch-ufficiali-ma-arrivano-fix-di-volontari/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/attacchi-che-sfruttano-il-sistema-motw-di-microsoft-niente-patch-ufficiali-ma-arrivano-fix-di-volontari/&title=Attacchi+che+sfruttano+il+sistema+MotW+di+Microsoft%2C+niente+patch+ufficiali+ma+arrivano+fix+di+volontari)

[== articolo precedente ==](https://insicurezzadigitale.com/polizia-federale-australiana-colpita-da-guacamaya/)

[:: articolo successivo ::](https://insicurezzadigitale.com/sabato-22-ottobre-e-linux-day-la-manifestazione-anche-a-cagliari/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/attacchi-che-sfruttano-il-sistema-motw-di-microsoft-niente-patch-ufficiali-ma-arrivano-fix-di-volontari/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Attacchi che sfruttano il sistema MotW di Microsoft, niente patch ufficiali ma arrivano fix di volontari*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Attacchi+che+sfruttano+il+sistema).
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