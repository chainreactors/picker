---
title: Il punto sul report Microsoft per Raspberry Robin worm con collegamenti a ransomware gangs
url: https://www.insicurezzadigitale.com/il-punto-sul-report-microsoft-per-raspberry-robin-worm-con-collegamenti-a-ransomware-gangs/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-01
fetch_date: 2025-10-03T21:27:08.368005
---

# Il punto sul report Microsoft per Raspberry Robin worm con collegamenti a ransomware gangs

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

# Il punto sul report Microsoft per Raspberry Robin worm con collegamenti a ransomware gangs

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
31 Ottobre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/10/03CUQ7U2cg45O8dsz7CB32l-1..v1656925842-1024x576.jpg)

Si parla di:

Toggle

* [Raspberry Robin Worm](#Raspberry_Robin_Worm)
* [Ultime scoperte](#Ultime_scoperte)

A partire da giovedì scorso (27/10) e per tutto il fine settimana, tanto è stato scritto sulla ricerca portata avanti dal team security di Microsoft. Tuttavia alcune affermazioni e deduzioni in merito non sembrano essere corrette.

Questo post per fare un punto rapido e senza fronzoli, sul contenuto del report, ripreso da molteplici testate e organizzazioni di tutto il mondo (compreso il nostro [CSIRT](https://www.csirt.gov.it/contenuti/rilevate-nuove-attivita-associate-al-worm-raspberry-robin-bl01-221028-csirt-ita-2), che ne riporta alcuni dettagli in maniera poco corretta, come mi è stato fatto notare da alcuni attenti ricercatori che l’hanno letto).

## Raspberry Robin Worm

Ciò che è stato analizzato è che le infezioni del worm Raspberry Robin, sono in aumento negli ultimi mesi. Il malware, inizialmente diffuso tramite unità USB esterne, ora utilizza metodi di infezione aggiuntivi e collabora con altre famiglie di malware (anche ransomware) nei suoi recenti attacchi informatici.

Studiato per la prima volta nel settembre 2021, Raspberry Robin è stato identificato come parte di un complesso sistema di malware interconnesso, che ora si sta diffondendo a macchia d’olio.

Si fa notare che si è diffuso appunto, su quasi 3.000 sistemi appartenenti a circa 1.000 organizzazioni nell’ultimo mese.

**Molti di questi attacchi sono collegati a un gruppo di minacce tracciato come DEV-0950, che nei suoi attacchi distribuisce il ransomware Cl0p**.

Sebbene Raspberry Robin non sia stato osservato con alcun exploit post-infezione, ha iniziato a funzionare come *loader* per altri malware, in particolare per DEV-0950.

## Ultime scoperte

Secondo [Microsoft](https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/), **DEV-0950 sta utilizzando il ransomware Cl0p** per crittografare la rete delle vittime, che sono già infettate dal worm Raspberry Robin.

A settembre, DEV-0950 ha iniziato a utilizzare Raspberry Robin per l’infezione iniziale, **rilasciando il ransomware Cl0p** e altri payload di seconda fase come IcedID, Bumblebee e Truebot su dispositivi compromessi.

Qui doverosa una precisazione. **IcedID** non è un ransomware; è un malware, della famiglia dei trojan bancari. **Bumblebee** non è un ransomware; è un malware utilizzato per compromettere i servizi di dominio (Active Directory), normalmente veicolato da file ISO apparentemente, spesso sfruttato da ransomware gang per l’accesso iniziale (es. Conti), ma non per l’operazione di crittografia. Anche **Truebot** non è un ransomware. Malware di tipo trojan per operare spionaggio nel device infetto: es. catturare screenshots del desktop.

Da ottobre, le infezioni da worm Raspberry Robin sembrano essere accompagnate dalle infezioni di Cobalt Strike e Truebot per implementare attacchi da parte del ransomware Cl0p.

L’attività dannosa di DEV-0950 si sovrappone ai gruppi di hacking tracciati come FIN11 e TA505, già noti per gli attacchi del ransomware Cl0p.

Questi cambiamenti e aggiornamenti di attività criminale che sono stati ora identificati, indicano che gli operatori di Raspberry Robin stanno vendendo l’accesso iniziale ai vari sistemi compromessi, a gruppi di ransomware e affiliati. Queste bande a loro volta possono facilmente stabilire un punto d’appoggio tranquillo e pianificare la loro prossima mossa, avendo parte della strada già spianata.

##### < tags />

[infosec](https://insicurezzadigitale.com/tag/infosec/)[malware](https://insicurezzadigitale.com/tag/malware/)[ransomware](https://insicurezzadigitale.com/tag/ransomware/)[raspberryrobin](https://insicurezzadigitale.com/tag/raspberryrobin/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Il+punto+sul+report+Microsoft+per+Raspberry+Robin+worm+con+collegamenti+a+ransomware+gangs&url=https://insicurezzadigitale.com/il-punto-sul-report-microsoft-per-raspberry-robin-worm-con-collegamenti-a-ransomware-gangs/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/il-punto-sul-report-microsoft-per-raspberry-robin-worm-con-collegamenti-a-ransomware-gangs/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/il-punto-sul-report-microsoft-per-raspberry-robin-worm-con-collegamenti-a-ransomware-gangs/&title=Il+punto+sul+report+Microsoft+per+Raspberry+Robin+worm+con+collegamenti+a+ransomware+gangs)

[== articolo precedente ==](https://insicurezzadigitale.com/polizia-senza-confini-linterpol-sbarca-nel-metaverso/)

[:: articolo successivo ::](https://insicurezzadigitale.com/lockbit-rivendica-attacco-ransomware-contro-thales-group/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/il-punto-sul-report-microsoft-per-raspberry-robin-worm-con-collegamenti-a-ransomware-gangs/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Il punto sul report Microsoft per Raspberry Robin worm con collegamenti a ransomware gangs*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Il+punto+sul+report+Microsoft).
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
...