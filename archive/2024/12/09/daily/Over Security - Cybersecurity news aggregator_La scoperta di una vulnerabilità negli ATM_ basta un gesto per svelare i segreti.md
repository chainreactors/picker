---
title: La scoperta di una vulnerabilità negli ATM: basta un gesto per svelare i segreti
url: https://www.insicurezzadigitale.com/la-scoperta-di-una-vulnerabilita-negli-atm-basta-un-gesto-per-svelare-i-segreti/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-09
fetch_date: 2025-10-06T19:37:31.571171
---

# La scoperta di una vulnerabilità negli ATM: basta un gesto per svelare i segreti

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

# La scoperta di una vulnerabilità negli ATM: basta un gesto per svelare i segreti

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
8 Dicembre 2024

![](https://insicurezzadigitale.com/wp-content/uploads/2024/12/Preventive-Tech-Solutions-for-ATMs-1024x585-1.png)

Si parla di:

Toggle

* [Un problema nascosto nel sistema operativo](#Un_problema_nascosto_nel_sistema_operativo)
* [Come è stata scoperta la vulnerabilità](#Come_e_stata_scoperta_la_vulnerabilita)
* [Implicazioni della vulnerabilità](#Implicazioni_della_vulnerabilita)
* [Alcune plausibili soluzioni](#Alcune_plausibili_soluzioni)

Gli sportelli automatici (ATM), pilastri del nostro sistema bancario, sono generalmente percepiti come dispositivi sicuri. Tuttavia, come ci dimostra la ricerca condotta da Enes\_0425, un ricercatore di sicurezza informatica, queste macchine possono nascondere vulnerabilità insospettabili. In questo articolo provo a commentare la scoperta abbastanza inquietante, che dimostra come un semplice gesto sullo schermo di un ATM possa aprire le porte a un mondo di problemi.

## **Un problema nascosto nel sistema operativo**

**Enes\_0425** ha individuato una grave vulnerabilità in alcuni sportelli automatici basati sul sistema operativo Windows. Attraverso un semplice gesto di swipe sullo schermo, simile alla combinazione di tasti **Win+Tab**, è possibile accedere al desktop del sistema. Questo gesto, apparentemente innocuo, consente di raggiungere funzionalità critiche come il file explorer e le impostazioni di sistema, trasformando gli ATM in potenziali prede per i criminali informatici.

## **Come è stata scoperta la vulnerabilità**

La scoperta non è stata casuale, ma frutto di osservazioni e ispirazioni tratte da conferenze di sicurezza. Durante l’HackerConf 2022, Enes ha tratto spunto da un talk sulla manipolazione di sistemi mal configurati. Notando che gli ATM utilizzano Windows come sistema operativo, ha ipotizzato che questi dispositivi potessero essere vulnerabili a comandi non previsti per l’utente.

![](https://www.insicurezzadigitale.com/wp-content/uploads/2024/12/1_rzvcmCLeycCavatr275LhQ.webp)

Un semplice test su uno schermo touch ha rivelato che un gesto di swipe attivava funzioni del desktop, aprendo la strada a exploit come l’accesso non autorizzato, l’installazione di malware e il furto di dati sensibili.

## **Implicazioni della vulnerabilità**

Questa falla nella sicurezza non è un rischio teorico, ma un problema concreto che può avere gravi conseguenze. Ecco i principali pericoli individuati:

1. **Accesso non autorizzato**: chiunque sfrutti questa vulnerabilità può ottenere il controllo completo del sistema, accedendo a dati sensibili come dettagli delle carte e cronologia delle transazioni.
2. **Installazione di malware**: attraverso il file explorer, un attaccante può caricare software malevolo per manipolare o compromettere il sistema.
3. **Furto e manipolazione di dati**: i dati dei clienti possono essere copiati, eliminati o alterati con estrema facilità.

Questi scenari rappresentano un rischio significativo non solo per i consumatori ma anche per la reputazione delle aziende coinvolte.

## **Alcune plausibili soluzioni**

Per mitigare questo tipo di attacco, Enes suggerisce alcune strategie:

* **Disattivare i gesti touch**: sebbene sia una soluzione temporanea, può bloccare l’accesso immediato al desktop.
* **Modalità Kiosk**: configurare gli ATM in modo che possano eseguire solo applicazioni specifiche, limitando l’accesso alle funzioni di sistema.
* **Test di sicurezza regolari**: monitorare costantemente i sistemi per identificare e correggere eventuali vulnerabilità prima che possano essere sfruttate.

---

La ricerca di Enes\_0425 mette in luce come anche i dispositivi più familiari, come gli sportelli automatici, possano nascondere insidie tecnologiche. Questo caso sottolinea l’importanza di una sicurezza informatica proattiva, non solo per proteggere i dati sensibili dei clienti ma anche per mantenere la fiducia nei sistemi bancari.

Come ha concluso lo stesso ricercatore, **ogni vulnerabilità scoperta è un’opportunità per rafforzare la sicurezza**.

##### < tags />

[atm](https://insicurezzadigitale.com/tag/atm/)[banksecurity](https://insicurezzadigitale.com/tag/banksecurity/)[infosec](https://insicurezzadigitale.com/tag/infosec/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=La+scoperta+di+una+vulnerabilit%C3%A0+negli+ATM%3A+basta+un+gesto+per+svelare+i+segreti&url=https://insicurezzadigitale.com/la-scoperta-di-una-vulnerabilita-negli-atm-basta-un-gesto-per-svelare-i-segreti/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/la-scoperta-di-una-vulnerabilita-negli-atm-basta-un-gesto-per-svelare-i-segreti/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/la-scoperta-di-una-vulnerabilita-negli-atm-basta-un-gesto-per-svelare-i-segreti/&title=La+scoperta+di+una+vulnerabilit%C3%A0+negli+ATM%3A+basta+un+gesto+per+svelare+i+segreti)

[== articolo precedente ==](https://insicurezzadigitale.com/leak-di-dati-e-riciclaggio-un-hub-per-il-riciclaggio-di-denaro-in-sudafrica/)

[:: articolo successivo ::](https://insicurezzadigitale.com/la-tragedia-di-brianna-ghey-il-lato-oscuro-di-internet/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/la-scoperta-di-una-vulnerabilita-negli-atm-basta-un-gesto-per-svelare-i-segreti/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *La scoperta di una vulnerabilità negli ATM: basta un gesto per svelare i segreti*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=La+scoperta+di+una+vulnerabilità).
Condividi esempi, IOCs o tecniche di detection efficaci nel nostro 👉 [**forum community**](https://forum.ransomfeed.it/)

## [[ mastodon ]]

Su Mastodon mi trovi qui: [Mastodon](https://poliversity.it/%40nuke)

### :: i social ::

* [Facebook](https://www.facebook.com/spcnet.it)
* [Instagram](https://www.instagram.com/spcnet.it/)
* [Twitter](https://twitter.com/nuke86)
* [Linkedin](https://www.linkedin.com/in/dariofadda86/)

## == forum community ==

💬 Partecipa alla community con i nostri [For...