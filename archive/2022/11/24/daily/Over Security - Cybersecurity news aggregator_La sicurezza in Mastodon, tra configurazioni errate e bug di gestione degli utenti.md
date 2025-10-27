---
title: La sicurezza in Mastodon, tra configurazioni errate e bug di gestione degli utenti
url: https://www.insicurezzadigitale.com/la-sicurezza-in-mastodon-tra-configurazioni-errate-e-bug-di-gestione-degli-utenti/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-24
fetch_date: 2025-10-03T23:40:11.443518
---

# La sicurezza in Mastodon, tra configurazioni errate e bug di gestione degli utenti

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

# La sicurezza in Mastodon, tra configurazioni errate e bug di gestione degli utenti

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
23 Novembre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/11/mastodon-1024x576.jpg)

Si parla di:

Toggle

* [Configurazioni errate del server portano a facili compromissioni](#Configurazioni_errate_del_server_portano_a_facili_compromissioni)
* [Due bug nella gestione degli utenti](#Due_bug_nella_gestione_degli_utenti)

Mastodon sta ricevendo diversi flussi migratori da utenti scontenti di Twitter, vediamo però come configurazioni poco prudenti del server e bug nella gestione degli utenti, possano rendere la vita dell’istanza molto difficile

Le ultime settimane, segnate per lo più da azioni e Tweet controversi di Elon Musk (dopo il suo acquisto di Twitter), hanno visto una crescita esponenziale delle istanze Mastodon, gestite individualmente e volontariamente dai singoli amministratori che vogliono contribuire alla crescita del Fediverso. Anche *inSicurezzaDigitale* ha la sua istanza: [mastodon.insicurezzadigitale.com](https://mastodon.insicurezzadigitale.com/)

All’aumento del traffico, aumenta anche l’interesse della comunità *infosec* sull’argomento. In effetti sempre più esperti utilizzano la piattaforma e ne ricercano problemi al fine di migliorare l’ecosistema del social network open source.

## Configurazioni errate del server portano a facili compromissioni

Non è una novità, ma forse è meglio sottolinearlo, visto che l’esperto di sicurezza Lenin Alevski, [ha indagato](https://www.alevsk.com/2022/11/system-misconfiguration-is-the-number-one-vulnerability-at-least-for-mastodon/) la vicenda e scoperto che il problema è parecchio diffuso.

Da sempre un server esposto in Rete è soggetto a controlli che possono arrivare da diversi fronti, i più preoccupanti sono ovviamente quelli malevoli. Se la configurazione del server non rispetta neppure gli standard minimi di sicurezza è quasi implicito avere dei problemi con attacchi che la piattaforma ospitata possa ricevere.

Quello che è stato scoperto è che l’istanza **infosec.exchange** di Mastodon (molto nota) carica i propri contenuti in bucket di archiviazione senza alcun vincolo di accesso. Sfruttando questa vulnerabilità, il ricercatore è stato in grado di sostituire l’immagine del profilo di tutti gli utenti con un meme archiviato nell’istanza infosec.exchange.

Una breve occhiata al codice sorgente della pagina indica che *https://media.infosec.exchange/infosecmedia* è la sorgente dei dati. Sembra una risposta XML di AWS S3 e la risposta del server dice anche “minio” per indicare che MinIO è in uso. MinIO è un applicativo compatibile con Amazon AWS S3 e permette lo storage mediante API.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/Mastodon-flaw1.jpg)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/Mastodon-flaw1.jpg)

In definitiva, con l’occasione si scopre che i bucket non hanno alcun tipo di autenticazione per l’accesso e tutti i contenuti non sono bloccati al pubblico, quindi accessibili e facilmente reperibili con qualsiasi client MinIO.

Inoltre la disattivazione del blocco degli accessi pubblici di AWS S3, interessava anche i permessi in scrittura, infatti qualsiasi attore delle minacce può (in questo caso) ottenere tutti i file sul server sfruttando questa “vulnerabilità”, compresi quelli scambiati tramite messaggi diretti, eliminare tutti i file del server e anche possibile modificare l’immagine del profilo di tutti.

Grazie a questa ricerca e segnalazione, l’istanza ha potuto correggere il problema, tuttavia Alevski ha constatato e segnalato la stessa errata configurazione ad altre istanze Mastodon, ricercando tra le più popolari nel Fediverso.

A titolo esemplificativo, una configurazione di un bucket AWS S3, che deve ospitare dati degli utenti Mastodon, deve specificare il seguente dettaglio nel tab *Autorizzazioni* delle informazioni del bucket:

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/Screenshot-2022-11-23-at-15-10-56-undefined-social-S3-bucket-1024x495.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/Screenshot-2022-11-23-at-15-10-56-undefined-social-S3-bucket.png)

## Due bug nella gestione degli utenti

Diversa natura sono invece i problemi riscontrati su altre istanze, nostra compresa, per la quale risoluzione, dipende meno l’amministratore dell’istanza e più lo sviluppo del progetto Mastodon. Sono infatti considerati bug aperti e non ancora risolti.

### Il caso del reset password utenti LDAP non-LDAP

Il problema principale su Github si chiama **#20655** (<https://github.com/mastodon/mastodon/issues/20655>) ed è un bug della piattaforma che non consente, agli utenti che si registrano ed autenticano su un’istanza che utilizza sistemi esterni di autenticazione, di modificare la propria password, resettarla o eliminare il proprio account.

Questo problema è grosso, soprattutto per il fatto che impatta sulle istanze che implementano buone pratiche di sicurezza informatica.

Utilizzare infatti un sistema terzo di autenticazione (supportato dalla piattaforma), in questo caso LDAP, circoscritto al container che fa il deployer dell’applicazione Mastodon, è una buona pratica di sicurezza. Visto che normalmente i dati degli utenti sarebbero invece parte del server che ospita l’istanza.

Questa interoperabilità che Mastodon offre, per autenticazione di terze parti, non è completa e produce i non semplici disservizi appena elencati.

Se un utente dimentica la password e fa la procedura di reset, la piattaforma invierà correttamente l’email con il link di conferma, ma il token non sarà in grado di completare la richiesta per comunicare a LDAP la password nuova dell’utente esterno (quindi non-LDAP di sistema, ma LDAP di container).

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/Screenshot_2022-11-23_15_43_49-1024x413.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2022/11/Screenshot_2022-11-23_15_43_49.png)

Il risultato del click sul link della email di reset password

“You are logged in via an external service, so password and e-mail settings are not avail...