---
title: Vulnerabilità nel core crittografico di Threema, la società: “nessun impatto reale”. Cosa è successo?
url: https://www.insicurezzadigitale.com/vulnerabilita-nel-core-crittografico-di-threema-la-societa-nessun-impatto-reale-cosa-e-successo/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-13
fetch_date: 2025-10-04T03:49:13.219397
---

# Vulnerabilità nel core crittografico di Threema, la società: “nessun impatto reale”. Cosa è successo?

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

# Vulnerabilità nel core crittografico di Threema, la società: “nessun impatto reale”. Cosa è successo?

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
12 Gennaio 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/01/f6a65926aa055935a61dfdb935f4f327.jpeg)

Non è un segreto che il messenger svizzero Threema sia molto popolare e sia stato utilizzato principalmente per oltre 10 anni come alternativa sicura a WhatsApp. Inoltre questo post non intende in nessun modo cambiare questo concetto, semmai analizzare cosa l’azienda poteva fare in fase di sviluppo.

Dopo che Meta (ora riconosciuto come estremista nella Federazione Russa) ha acquisito WhatsApp e modificato la sua politica sulla privacy, l’attenzione degli utenti verso il messenger svizzero è aumentata notevolmente.

Un recente Paper di ricerca però, cerca le basi per una **compromissione del core crittografico di Threema**, la cui promessa di massima sicurezza è tuttora incomparabile in termini di livello con qualsiasi altro messenger concorrente.

Il messenger ha infatti ricevuto ampi riconoscimenti nel 2019 e l’amministrazione federale svizzera ne ha approvato l’uso anche per i contenuti classificati come “riservati”.

L’insicurezza della crittografia di Threema è una prima conclusione raggiunta da un gruppo di ricerca guidato dal professor **Kenneth Paterson** dell’ETH (Swiss Public Research University).

Come si è scoperto, ci sono difetti fondamentali nel concetto di crittografia Threema (<https://breakingthe3ma.app>/). Inoltre, i metodi di crittografia sono tecnologicamente indietro di diversi anni.

Un gruppo di ricercatori ha pubblicato una descrizione dettagliata di **7 vulnerabilità nei protocolli crittografici Threema**.

Il loro sfruttamento potrebbe consentire agli aggressori di clonare account, leggere la corrispondenza, rubare chiavi private e contatti, nonché di riprodurre materiali compromettenti per ulteriori ricatti contro la vittima presa di mira.

Con solita precisione, Threema ha risposto immediatamente e ha rilasciato un nuovo protocollo chiamato **Ibex** che rende obsoleti e irrilevanti una serie di problemi evidenziati e risolve il resto dei difetti riscontrati in poche settimane (la vicenda è iniziata ad ottobre 2022.

Nel loro [blog](https://threema.ch/en/blog/posts/news-alleged-weaknesses-statement), gli sviluppatori hanno tuttavia sottovalutato il numero di bug individuati nello studio, spiegando che le vulnerabilità sono state trovate in un protocollo che Threema non utilizza più.

Inoltre, hanno notato che gli errori rilevati possono essere interessanti da un punto di vista teorico, nessuno di essi ha avuto un impatto significativo nel mondo reale. Sappiamo bene però che questa conclusione non annulla la loro esistenza.

Una sequenza di eventi, di questa vicenda, fa pensare che si siano accavallate diverse coincidenze, tuttavia non possiamo sapere al momento se gli sviluppatori di Threema, abbiano sviluppato Ibex (a fine 2022) effettivamente sulla base di questi risultati di ricerca, anche se la società sostiene che il proprio team già ci stava lavorando da un anno e mezzo. Non possiamo nemmeno escluderlo, come anche il fatto che alcune delle vulnerabilità che sono state scoperte, potrebbero essere state presenti in Threema già da molto tempo.

Il gruppo di ricerca evidenzia, tra le lezioni che si possono imparare da questa storia, la mancanza di un’esame al nucleo crittografico dell’applicazione.

“Tale analisi dovrebbe essere un requisito minimo per qualsiasi messenger sicuro, in particolare uno utilizzato in ambienti sensibili. Idealmente, qualsiasi applicazione che utilizza nuovi protocolli crittografici dovrebbe essere accompagnata da proprie analisi di sicurezza formali (sotto forma di prove di sicurezza) per fornire solide garanzie di sicurezza”.

##### < tags />

[bug](https://insicurezzadigitale.com/tag/bug/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[Threema](https://insicurezzadigitale.com/tag/threema/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Vulnerabilit%C3%A0+nel+core+crittografico+di+Threema%2C+la+societ%C3%A0%3A+%26%238220%3Bnessun+impatto+reale%26%238221%3B.+Cosa+%C3%A8+successo%3F&url=https://insicurezzadigitale.com/vulnerabilita-nel-core-crittografico-di-threema-la-societa-nessun-impatto-reale-cosa-e-successo/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/vulnerabilita-nel-core-crittografico-di-threema-la-societa-nessun-impatto-reale-cosa-e-successo/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/vulnerabilita-nel-core-crittografico-di-threema-la-societa-nessun-impatto-reale-cosa-e-successo/&title=Vulnerabilit%C3%A0+nel+core+crittografico+di+Threema%2C+la+societ%C3%A0%3A+%26%238220%3Bnessun+impatto+reale%26%238221%3B.+Cosa+%C3%A8+successo%3F)

[== articolo precedente ==](https://insicurezzadigitale.com/tumulti-in-jp-morgan-per-il-ricorso-di-ray-ban-sulla-frode-nei-conti-bancari/)

[:: articolo successivo ::](https://insicurezzadigitale.com/scattered-spider-sfrutta-vulnerabilita-windows-per-attacchi-byovd/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/vulnerabilita-nel-core-crittografico-di-threema-la-societa-nessun-impatto-reale-cosa-e-successo/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Vulnerabilità nel core crittografico di Threema, la società: “nessun impatto reale”. Cosa è successo?*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Vulnerabilità+nel+core+crittografico+di).
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

* [Spcnet.it](...