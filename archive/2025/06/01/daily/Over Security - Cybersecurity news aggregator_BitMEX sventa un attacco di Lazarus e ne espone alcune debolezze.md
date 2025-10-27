---
title: BitMEX sventa un attacco di Lazarus e ne espone alcune debolezze
url: https://www.insicurezzadigitale.com/bitmex-sventa-un-attacco-di-lazarus-e-ne-espone-alcune-debolezze/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-01
fetch_date: 2025-10-06T22:53:08.164104
---

# BitMEX sventa un attacco di Lazarus e ne espone alcune debolezze

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

# BitMEX sventa un attacco di Lazarus e ne espone alcune debolezze

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
1 Giugno 2025

![](https://insicurezzadigitale.com/wp-content/uploads/2025/06/BitMEX-1024x576.jpeg)

Si parla di:

Toggle

* [La dinamica dell’attacco](#La_dinamica_dellattacco)
* [La falla operativa decisiva](#La_falla_operativa_decisiva)
* [Struttura e tattiche del Lazarus Group](#Struttura_e_tattiche_del_Lazarus_Group)
* [Implicazioni per il settore crittografico](#Implicazioni_per_il_settore_crittografico)

BitMEX, una delle principali piattaforme di trading di Bitcoin, ha recentemente neutralizzato un sofisticato attacco di ingegneria sociale attribuito al gruppo nordcoreano Lazarus, rivelando nuove vulnerabilità nelle tattiche del collettivo criminale. L’episodio offre un case study prezioso per gli esperti di cybersecurity, mostrando sia l’evoluzione delle minacce APT (Advanced Persistent Threat) sia gli errori operativi che persino gruppi avanzati possono commettere.

## **La dinamica dell’attacco**

L’incidente è [iniziato](https://blog.bitmex.com/bitmex-busts-lazarus-group/) con un approccio su LinkedIn a un dipendente BitMEX da parte di presunti recruiter, che proponevano una collaborazione su un marketplace NFT. Questo espediente classico di social engineering nascondeva l’obiettivo reale: distribuire il malware **BeaverTail**, già associato a Lazarus da Unit 42 di Palo Alto Networks. Il codice malevolo, progettato per raccogliere credenziali e indirizzi IP, avrebbe potuto compromettere l’infrastruttura critica dell’exchange.

![](https://www.insicurezzadigitale.com/wp-content/uploads/2025/06/immagine-885x1024.png)

BeaverTail: telemetria del mese di maggio 2025

## **La falla operativa decisiva**

Nonostante l’uso di tecniche avanzate, i threat actor hanno commesso un errore cruciale: non mascherare l’IP originario durante le comunicazioni C2 (Command and Control). Questa negligenza ha permesso a BitMEX di sviluppare uno strumento di tracciamento ad hoc, identificando almeno 10 account collegati allo sviluppo del malware. L’analisi forense ha evidenziato una disparità tra le capacità di exploitation avanzate del gruppo e le elementari pratiche di phishing impiegate.

## **Struttura e tattiche del Lazarus Group**

L’indagine rivela un’organizzazione segmentata: il gruppo opererebbe attraverso cellule autonome con diversi livelli di expertise tecnica. Questa modularità operativa, mentre aumenta la superficie d’attacco, introduce punti deboli nel coordinamento. La presenza simultanea di TTP (Tactics, Techniques, Procedures) sofisticate e basiche suggerisce una possibile esternalizzazione parziale delle attività a contractor meno esperti.

## **Implicazioni per il settore crittografico**

L’episodio si inserisce in un contesto allarmante: solo a febbraio 2023, l’hack di Bybit ha registrato perdite record, mentre la recente violazione dei dati di Coinbase evidenzia vulnerabilità sistemiche. BitMEX ha dimostrato che un rilevamento tempestivo (con tempi di risposta sotto le 24 ore) e l’analisi proattiva delle IoC (Indicator of Compromise) possono mitigare danni potenziali, anche contro avversari di livello statale.

1. Implementare sistemi di threat intelligence integrati con feed APT-specifici
2. Addestrare il personale a riconoscere varianti avanzate di social engineering
3. Sviluppare capacità interne di malware analysis per decodificare le TTP in tempo reale

L’attacco conferma che la cybersecurity nel settore crypto richiede un approccio stratificato, dove l’hardening tecnologico deve essere accompagnato da continuous monitoring e threat hunting attivo. La sfida non è solo respingere gli attacchi, ma trasformare ogni incidente in intelligence operativa per anticipare le mosse successive degli avversari.

##### < tags />

[BeaverTail](https://insicurezzadigitale.com/tag/beavertail/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[lazarus](https://insicurezzadigitale.com/tag/lazarus/)[malware](https://insicurezzadigitale.com/tag/malware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=BitMEX+sventa+un+attacco+di+Lazarus+e+ne+espone+alcune+debolezze&url=https://insicurezzadigitale.com/bitmex-sventa-un-attacco-di-lazarus-e-ne-espone-alcune-debolezze/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/bitmex-sventa-un-attacco-di-lazarus-e-ne-espone-alcune-debolezze/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/bitmex-sventa-un-attacco-di-lazarus-e-ne-espone-alcune-debolezze/&title=BitMEX+sventa+un+attacco+di+Lazarus+e+ne+espone+alcune+debolezze)

[== articolo precedente ==](https://insicurezzadigitale.com/vulnerabilita-critica-non-corretta-nel-plugin-ti-woocommerce-wishlist-cve-2025-47577/)

[:: articolo successivo ::](https://insicurezzadigitale.com/crocodilus-levoluzione-di-un-trojan-bancario-android-che-minaccia-le-criptovalute-a-livello-globale/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/bitmex-sventa-un-attacco-di-lazarus-e-ne-espone-alcune-debolezze/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *BitMEX sventa un attacco di Lazarus e ne espone alcune debolezze*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=BitMEX+sventa+un+attacco+di).
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

Notizie cybersecurity, malw...