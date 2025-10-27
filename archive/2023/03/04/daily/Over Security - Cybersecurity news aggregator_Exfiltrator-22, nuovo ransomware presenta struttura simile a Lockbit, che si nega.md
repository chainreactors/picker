---
title: Exfiltrator-22, nuovo ransomware presenta struttura simile a Lockbit, che si nega
url: https://www.insicurezzadigitale.com/exfiltrator-22-nuovo-ransomware-presenta-struttura-simile-a-lockbit-che-si-nega/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-04
fetch_date: 2025-10-04T08:40:00.821665
---

# Exfiltrator-22, nuovo ransomware presenta struttura simile a Lockbit, che si nega

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

[Ransomware](https://insicurezzadigitale.com/category/ransomware/)

# Exfiltrator-22, nuovo ransomware presenta struttura simile a Lockbit, che si nega

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
3 Marzo 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/03/mediadc.brightspotcdn.com_-1024x576.jpeg)

I ricercatori di Cyfirma hanno pubblicato un rapporto su un framework post-exploit chiamato **Exfiltrator-22** (EX22) e affermano possa essere correlato a Lockbit 3.0.

In questo post, l’analisi del rapporto.

I ricercatori hanno annunciato che lo sviluppo di questo framework è stato completato il 27 novembre 2022 (o appena prima) e gli attori delle minacce hanno lanciato un canale Telegram per pubblicizzare i loro strumenti il ​​7 dicembre 2022.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/exfiltrator-1-jpg.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/exfiltrator-1-jpg.png)

Scansionando questo framework il 13 febbraio 2023, solo 5 antivirus lo rilevano, il che dimostra che gli agenti dietro di esso conoscono bene le tecniche anti-analisi e le tecniche di rilevamento.

Gli operatori dietro questo malware hanno annunciato nel loro canale Telegram alla fine di **dicembre 2022** di aver aggiunto una nuova funzionalità che consente di nascondere il traffico o di farlo sembrare legittimo. Nel **gennaio 2023**, hanno annunciato che questo **malware ha raggiunto lo sviluppo dell’87%** e il modello del suo utilizzo è il noleggio (condiviso).

1.000 dollari/mese e 5.000 dollari per l’accesso a vita.

Dopo l’acquisto, verrà fornito un collegamento al pannello del server EX22, che si trova su un server VPS. Il 10 febbraio 2023 è stato pubblicato su YouTube un video delle caratteristiche di questo framework.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/exfiltrator-2-jpg.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/exfiltrator-2-jpg.png)

Questo strumento è progettato per distribuire ransomware nelle reti aziendali senza identificazione e ha varie funzionalità, tra cui:

* Fornire un reverse shell con un punteggio elevato.
* Carica il file sul sistema della vittima e scarica il file dal sistema della vittima su C2
* Funzionalità di keylogger per rubare informazioni digitate
* Funzionalità ransomware che crittografa i file sul sistema della vittima
* Funzionalità di screenshot che consente di raccogliere informazioni dal sistema di destinazione.
* Accesso in tempo reale al sistema della vittima tramite VNC
* Capacità di aumentare i punti nel sistema vittima
* Capacità persistente di durare più a lungo sul sistema della vittima Il malware offre anche la possibilità di spostarsi lateralmente per consentire all’infezione di diffondersi ad altri sistemi.
* Dump LSASS per raccogliere le credenziali
* Utilizzo della funzione hash per identificare, individuare file specifici e modifiche agli eventi
* Raccolta dei processi in esecuzione per raccogliere informazioni e identificare potenziali vulnerabilità sui programmi
* Rubare token sensibili per accedere ad altri account vittima

**Pannello di gestione dei malware:** come accennato in precedenza, gli acquirenti di questo malware hanno accesso a un pannello di gestione. Questo pannello fornisce all’attaccante varie funzionalità come l’esecuzione di comandi, la raccolta di informazioni, la creazione di una campagna, l’automazione della campagna, ecc. La figura seguente è una vista del pannello C2 del malware.

![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/ex-22_5-1024x849.png)

Nel canale di questo malware, gli attori della minaccia hanno pubblicato un’immagine di quanto è stato rilevato dagli antivirus:

In questa immagine sono specificati l’ora registrata nella scansione e l’ora sul sistema, che sono distanti 8 ore. Nella sezione delle attività di rete, troverai un IP che è riconducibile a CDN di Akamai.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/exfiltrator-3-jpg.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/exfiltrator-3-jpg.png)

Gli aggressori utilizzano la tecnica del fronting del dominio. In questa tecnica, gli aggressori utilizzano un plug-in chiamato MEEK, che è un plug-in di offuscamento per Tor e implementa la tecnica di fronting del dominio nascondendo il traffico Tor. Posizionando il server di Meek dietro una CDN, gli aggressori rendono MEEK in grado di nascondere il traffico Tor attraverso una connessione HTTPS legittima a servizi noti.

Questa tecnica rende non rilevabile il C2 dell’attaccante. Questa tecnica è utilizzata anche da Lockbit 3.0. I ricercatori hanno anche trovato un esempio di questo ransomware che utilizzava la stessa infrastruttura di rete C2 riportata in questo framework.

Di conseguenza, i ricercatori ritengono che questo framework sia stato sviluppato da rappresentanti o dal team di sviluppo del ransomware Lockbit3.0.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/photo_2023-03-01_20-07-04.jpg)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/photo_2023-03-01_20-07-04.jpg)

**Lockbit però ha negato** qualsiasi affiliazione con gli sviluppatori del framework EXFILTRATOR-22 e li ha accusati di aver abusato del loro nome Lockbit, senza accordi.

##### < tags />

[EX22](https://insicurezzadigitale.com/tag/ex22/)[Exfiltrator22](https://insicurezzadigitale.com/tag/exfiltrator22/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[lockbit](https://insicurezzadigitale.com/tag/lockbit/)[ransomware](https://insicurezzadigitale.com/tag/ransomware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Exfiltrator-22%2C+nuovo+ransomware+presenta+struttura+simile++a+Lockbit%2C+che+si+nega&url=https://insicurezzadigitale.com/exfiltrator-22-nuovo-ransomware-presenta-struttura-simile-a-lockbit-che-si-nega/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/exfiltrator-22-nuovo-ransomware-presenta-struttura-simile-a-lockbit-che-si-nega/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/exfiltrator-22-nuovo-ransomware-presenta-struttura-simile-a-lockbit-che-si-nega/&title=Exfiltrator-22%2C+nuovo+ransomware+presenta+strut...