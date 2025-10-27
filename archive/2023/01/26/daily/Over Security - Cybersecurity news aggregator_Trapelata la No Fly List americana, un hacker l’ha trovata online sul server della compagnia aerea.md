---
title: Trapelata la No Fly List americana, un hacker l’ha trovata online sul server della compagnia aerea
url: https://www.insicurezzadigitale.com/trapelata-la-no-fly-list-americana-un-hacker-lha-trovata-online-sul-server-della-compagnia-aerea/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-26
fetch_date: 2025-10-04T04:54:14.579180
---

# Trapelata la No Fly List americana, un hacker l’ha trovata online sul server della compagnia aerea

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

# Trapelata la No Fly List americana, un hacker l’ha trovata online sul server della compagnia aerea

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
25 Gennaio 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/01/5707720583_bf532dea60_b.jpg)

Si parla di:

Toggle

* [Di cosa si tratta](#Di_cosa_si_tratta)
* [Trovare NOFLY.csv](#Trovare_NOFLYcsv)
* [Dentro la No Fly List](#Dentro_la_No_Fly_List)
* [Il problema è la mala gestione](#Il_problema_e_la_mala_gestione)

Si chiama **maia arson crimew**, ed è la ricercatrice di sicurezza informatica (di base in Svizzera) che ha trovato **per noia** un server della compagnia aerea CommutAir che, non essendo adeguatamente protetto, ne ha esposto online il contenuto per chissà quanto tempo.

Non va tutto bene, ma il vero problema è che il contenuto, appunto, riguarda la sicurezza nazionale degli Stati Uniti: **su quel server c’era una versione della No Fly List**, un documento di sicurezza che le autorità utilizzano per sapere se ad una persona è proibito volare all’interno o dall’esterno per gli Stati Uniti.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/01/FnKnVG_XkAAaffH-1024x769.jpeg)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/01/FnKnVG_XkAAaffH.jpeg)

maia arson crimew

# La No Fly List, dentro ci sono anche italiani

Come parte di quelle pratiche di sicurezza, messe in atto per fronteggiare il terrorismo dagli Stati Uniti, la No Fly List nasce prima dell’11 settembre 2001, ma è da novembre di quell’anno in poi (dopo i noti attentati), che la lista prende forma e diventa sempre più lunga e corposa.

## Di cosa si tratta

Basti pensare che prima degli attentati la lista era composta da 16 nominativi, a novembre erano 400 e oggi sono oltre 1,5 milioni.

A cosa serve la No Fly List? Funziona come una blacklist, **chi compare all’interno di quella lista non può imbarcarsi** né volare per (e negli) Stati Uniti.

È un documento federale, non è pubblico ma non è classificato perché viene utilizzato quotidianamente proprio per effettuare i controlli negli aeroporti.

## Trovare NOFLY.csv

Il problema evidenziato da **maia** però è relativo al come sia possibile che una piccola compagnia aerea, possa permettersi di trattare con così troppa superficialità, documenti così importanti per la sicurezza delle persone. Il file è trapelato proprio perché maia ha cercato, su Shodan, i server esposti online al fine di vedere se all’interno ci poteva essere del materiale rilevante (insomma, un passatempo qualsiasi!). Si è concentrata sulla **ricerca di server Jenkins aperti**. Jenkins fornisce server di automazione che aiutano nella creazione, nel test e nel deploy del software (via repository di sviluppo).

Quello che è stato rilevato è dunque un server di sviluppo (di test) della compagnia aerea, abbandonato a se stesso, aperto ed esposto online, il cui contenuto disponibile alla mercé di tutti. Maia [lo rileva](https://maia.crimew.gay/posts/how-to-hack-an-airline/) e indaga all’interno per portare alla luce ciò che espone. La sua attenzione viene subito catturata da “tre file csv, `employee_information.csv`, `NOFLY.CSV` e `SELECTEE.CSV`. Tutti impegnati nel repository nel luglio 2022″.

Ha trovato materiale sensibile. Oltre ai dati di circa 1000 dipendenti della CommutAir, compresi “nomi completi, indirizzi, numeri di telefono, numeri di passaporto, numeri di licenza di pilota, quando è previsto il loro prossimo [controllo in linea](https://icadet.com/aviation-term/line-check/) e molto altro”, afferma maia sul suo blog. Inoltre la lista completa, aggiornata al 2019, di tutte le persone che gli Stati Uniti reputano pericolose e sospette, alle quali non è consentito volare.

## Dentro la No Fly List

Questo leak ci dà la possibilità di aggiornare anche il numero di righe, al 2019 presenti all’interno, ora sappiamo con certezza che all’interno ci sono 1.566.063 persone, tra cui terroristi di tutto il mondo, ma **anche persone che non hanno alcun sospetto di terrorismo**, che per varie ragioni hanno dovuto viaggiare in stati ritenuti pericolosi dagli Stati Uniti e quindi, rappresentati su questa lista.

È utile far presente che la lista è parte di un database più grande mantenuto dal Terrorist Screening Center (TSC) che contiene molti più nominativi ma che evidenziano persone pericolose da sottoporre a controlli più stringenti, ma per i quali il volo è consentito. Chi è presente su questa lista invece, ha proprio l’impossibilità ad imbarcarsi.

Per l’Italia notiamo famosi esponenti delle Brigate Rosse come **Giorgio Frau** e latitanti ricercati legati alla malavita mafiosa come **Giovanni Alimonti, Enzo Calvitti, Roberta Cappelli, Marina Petrella, Giorgio Pietrostefani** e **Sergio Tornaghi**.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/01/Screenshot_2023-01-24_23_50_21.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/01/Screenshot_2023-01-24_23_50_21.png)

Il curioso nominativo del Toto Riina del 1986

Non solo terroristi. Dentro la lista, come detto, vengono inserite anche tutte quelle personalità che effettuano viaggi in Paesi poco graditi agli Stati Uniti, impedendogli così (per un intervallo di tempo) di effettuare viaggi negli USA.

## Il problema è la mala gestione

I file che sono trapelati, dopo di che il server è stato messo offline, sono due, nofly.csv (1,5 milioni di righe 75 MB) e selectee.csv (251mila righe e 11,5 MB). La differenza dei due è da ricercare nella [gestione del sistema](https://en.wikipedia.org/wiki/No_Fly_List) di TSC americano. In effetti la No Fly List è l’elenco dei nominativi a cui è proibito volare, la Selectee list è invece una lista di sospettati, non presenti in NoFly, per i quali è obbligatorio effettuare controlli aggiuntivi ma che possono volare.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/01/Screenshot_2023-01-25_11_23_31.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/01/Screenshot_2023-01-25_11_23_31.png)

Il problema grave è come sia possibile lasciare file di così elevata rilevanza e sensibilità, a compagnie private, senza aver traccia di come vengono conservati. Il fatto che i file non siano secretati è comprensibile...