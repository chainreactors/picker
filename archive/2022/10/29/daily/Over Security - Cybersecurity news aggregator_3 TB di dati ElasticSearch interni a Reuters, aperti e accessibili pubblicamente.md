---
title: 3 TB di dati ElasticSearch interni a Reuters, aperti e accessibili pubblicamente
url: https://www.insicurezzadigitale.com/3-tb-di-dati-elasticsearch-interni-a-reuters-aperti-e-accessibili-pubblicamente/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-29
fetch_date: 2025-10-03T21:15:14.344770
---

# 3 TB di dati ElasticSearch interni a Reuters, aperti e accessibili pubblicamente

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

[Data Breach](https://insicurezzadigitale.com/category/data-breach/)

# 3 TB di dati ElasticSearch interni a Reuters, aperti e accessibili pubblicamente

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
29 Ottobre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/10/TDM2WP7ZJNMIRGGVQ4VEDJY2WU.jpg)

FILE PHOTO: The Thomson Reuters logo is seen on the company building in Times Square, New York. REUTERS/Carlo Allegri

Un problema che non si fa altro che minimizzare, quello delle strutture di rete accessibili pubblicamente, senza alcuna protezione, perché mal configurate. Colpisce grandi e piccoli e alimenta il traffico illecito dei dati, dando pane quotidiano per attacchi mirati

Il gruppo aziendale dei media Thomson Reuters ha appreso per caso di aver lasciato aperti almeno tre dei suoi database, facendo trapelare quasi 3 TB di informazioni riservate sui clienti e altre informazioni aziendali.

L’incidente è stato [segnalato](https://cybernews.com/security/thomson-reuters-leaked-terabytes-sensitive-data/) dai ricercatori di Cybernews che hanno scoperto una perdita in ElasticSearch con 3 TB di informazioni riservate aggiornate, comprese le password per server di terze parti.

Inoltre, secondo la prassi anti best practices, il tutto veniva archiviato in forma non crittografata e consisteva in dati di registrazione raccolti durante l’interazione degli utenti con i clienti.

La perdita scoperta è una miniera d’oro per gli aggressori che possono utilizzare i dati per attaccare, supply chain, in altre frodi mirati. Sappiamo bene quanto siano ricercati elenchi di dati personali, a questo scopo, per lanciare campagne.

I timestamp sui campioni ottenuti dai ricercatori mostrano che i dati sono aggiornati e registrati di recente, alcuni dei quali sono datati 26 ottobre di quest’anno.

Oltre alle credenziali, la fuga include documenti con informazioni aziendali e legali su aziende e individui specifici.

I ricercatori di Cybernews hanno anche scoperto che uno dei database aperti includeva la convalida interna di altre piattaforme come YouTube, i log di accesso dei clienti di Thomson Reuters e le stringhe di connessione ad altri database.

Si noti che la divulgazione delle stringhe di connessione è particolarmente pericolosa perché consente di rivelare elementi della rete interna di Reuters, che probabilmente hanno già dato agli aggressori l’opportunità di spostarsi lateralmente e migrare attraverso i sistemi interni dell’azienda.

Infine, i ricercatori hanno trovato la reimpostazione della password e i registri di accesso. Senza rivelare password vecchie o nuove, i log mostrano l’indirizzo e-mail del proprietario dell’account e l’ora esatta in cui è stata inviata una richiesta di modifica della password.

Cybernews ha contattato Thomson Reuters dopo aver scoperto la perdita del database. Dopo aver ricevuto una notifica, la società ha immediatamente chiuso l’accesso di quanto segnalato.

**Thomson Reuters ha tentato di minimizzare la divulgazione affermando che due dei server erano per uso pubblico e il terzo era un server di prova per il prodotto “ONESOURCE Global Trade Offering” di Thomson Reuters**.

Il rappresentante della società ha spiegato che i server contengono le informazioni necessarie per il supporto operativo della piattaforma e non comportano un rischio colossale. Se questo è vero o no diventerà presto chiaro.

Tuttavia, la società ha avviato un’indagine interna per andare a fondo del problema e ha affermato di aver avviato un processo di notifica per i clienti potenzialmente interessati.

È normale che apprendere di aver avviato un processo di notifica per le persone potenzialmente interessate, collima brutalmente con il fatto che i database contenessero solo informazioni operative della piattaforma. Sembra quanto meno lampante che i dati siano sfuggiti di mano, come sempre più spesso accade, rilasciando in mani sconosciute listati enormi di email, nomi e cognomi, **numeri di telefono** che sono il pane quotidiano alla base di qualsiasi attacco fraudolento.

Piuttosto che minimizzare, sarebbe interessante evidenziare come tutto questo alimenti gli attacchi di social engineering, oggi sempre più diffusi, che fonda le sue basi proprio a partire da dati come questi.

Email e numeri di telefono sono i più sfruttati in questo campo. Il primo metodo si riferisce all’invio di e-mail dannose per indurre le persone a fare qualcosa per conto dell’aggressore. Di solito si tratta di aprire un link pericoloso o un allegato contenuti nell’e-mail. Ricerche condotte da Proofpoint nel report “[2022 State of the Phish](https://www.proofpoint.com/us/resources/threat-reports/state-of-phish)” mostrano quanto questa tecnica sia diffusa ed efficace: nel 2021, l’86% delle organizzazioni ha dovuto affrontare [attacchi phishing di massa](https://www.proofpoint.com/us/threat-reference/phishing). Nelle simulazioni di phishing, un utente su 5 ha aperto un allegato e-mail e uno su 10 ha cliccato su un link.

Come evidenziato nel report di Proofpoint “Human Factor2022”, negli ultimi mesi si è assistito a un’impennata di attacchi telefonici, noti anche come call-back phishing. Fulcro di questo approccio è la conversazione telefonica tra persone. Naturalmente, questi attacchi richiedono la partecipazione attiva della vittima, iniziano con un’email che sembra provenire da una fonte legittima e include un numero di telefono per l’assistenza ai clienti. I chiamanti vengono collegati a falsi rappresentanti del customer service che guidano la vittima attraverso l’attacco, alla quale potrebbero chiedere di consentire l’accesso al proprio computer da remoto o di scaricare un file che si rivela essere un malware.

##### < tags />

[databreach](https://insicurezzadigitale.com/tag/databreach/)[infosec](https://insicurezzadigitale.com/tag/infosec/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=3+TB+di+dati+ElasticSearch+interni+a+Reuters%2C+aperti+e+accessibili+pubblicamente&url=https://insicurezzadigitale.com/3-tb-di-dati-elasticsearch-interni-a-reuters-aperti-e-accessibili-pubblicamente/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/3-tb-di-dati-elasticsearch-interni-a-reuters-aperti-e-accessibili-pubblicamente/)
[LinkedIn](https://www.linke...