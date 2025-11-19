---
title: Rust riduce sensibilmente le vulnerabilità di memory safety in Android
url: https://www.securityinfo.it/2025/11/18/rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android/?utm_source=rss&utm_medium=rss&utm_campaign=rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android
source: Securityinfo.it
date: 2025-11-18
fetch_date: 2025-11-19T03:15:06.142802
---

# Rust riduce sensibilmente le vulnerabilità di memory safety in Android

Aggiornamenti recenti Novembre 18th, 2025 10:17 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Rust riduce sensibilmente le vulnerabilità di memory safety in Android](https://www.securityinfo.it/2025/11/18/rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android/)
* [Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure](https://www.securityinfo.it/2025/11/18/impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure/)
* [Il protocollo di rete “Finger” rinasce in attacchi ClickFix](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/)
* [CERT-AGID 8–14 novembre: ondata di phishing su hosting, PagoPA e università](https://www.securityinfo.it/2025/11/17/cert-agid-8-14-novembre-ondata-di-phishing-su-hosting-pagopa-e-universita/)
* [Vulnerabilità di Fortinet FortiWeb sfruttata per creare utenti admin](https://www.securityinfo.it/2025/11/14/vulnerabilita-di-fortinet-fortiweb-sfruttata-per-creare-utenti-admin/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## Rust riduce sensibilmente le vulnerabilità di memory safety in Android

Nov 18, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Software](https://www.securityinfo.it/category/approfondimenti/software/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2025/11/18/rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android/#respond)

---

Dopo un anno dall’annuncio dell’aumento dell’uso di **Rust per Android**, Google [ha confermato](https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html) che questo linguaggio di programmazione sta portando numerosi vantaggi; tra questi, il più significativo è il **calo per la prima volta sotto il 20% delle vulnerabilità di memory safety.**

“*Abbiamo adottato Rust per il suo livello di sicurezza e **abbiamo assistito a una riduzione della densità di vulnerabilità di memory safety di 1000 volte** confrontato con il codice C e C++ di Android. Ma la sorpresa più grossa è stato l’impatto di Rust sulla delivery del software. Con Rust le modifiche hanno un tasso di rollback inferiore di 4 volte e si perde il 25% in meno di tempo nella revisione di codice*” ha spiegato Jeff Vander Stoep, software engineer di Android.

![Rust Android](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_n4jlo7n4jlo7n4jl.png)

Google ha cominciato a usare Rust in Android per la prima volta nel 2021, come alternativa a C e C++: il linguaggio, spiega Vander Stope, offre lo stesso livello di controllo degli altri due, ma con molti meno rischi. Negli anni, la compagnia ha man mano sostituito le linee di codice scritte in C e C++ con quelle scritte in Rust, arrivando nel 2025 ad avere più codice scritto in quest’ultimo linguaggio.

Dalle analisi, è emerso che **la nuova codebase richiede meno revisioni di codice**, le quali sono anche più veloci da completare; ciò significa una maggiore rapidità nello sviluppo e messa in funzione del codice. I vantaggi più significativi riguardano però la **stabilità e la qualità del codice**: il tasso di rollback su modifiche medio-grandi è ridotto di 4 volte. I rollback del codice, sottolinea Vander Stoep, oltre a minare la stabilità del codice rallentano anche la produttività poiché richiedono rework impattanti e più revisioni di codice.

Rust ovviamente non è la soluzione a tutti i problemi: il linguaggio soffre comunque di vulnerabilità di memory safety. Vander Stoep riporta infatti che il suo team ha individuato e risolto un bug di questo tipo in Rust prima che la release incriminata di Android andasse in produzione. Il linguaggio ha però il grande vantaggio di averne una densità drasticamente minore rispetto a C e C++: “*Con circa 5 milioni di linee di codice in Rust nella piattaforma Android e una sola potenziale vulnerabilità individuata (e risolta prima delle release)**, la densità stimata di vulnerabilità per Rust è di 0.2 per 1 milione di linee di codice***” ha affermato il ricercatore.

Il passaggio a Rust rappresenta quindi non solo un vantaggio per la velocità di sviluppo del codice, ma anche e soprattutto per la sicurezza. “***Invece di agire rapidamente e poi risolvere i problemi in un secondo momento, possiamo agire più rapidamente mentre risolviamo i problemi.** E chissà, man mano che il nostro codice diventa sempre più sicuro, forse potremo iniziare a recuperare ancora di più quelle prestazioni e quella produttività che abbiamo sacrificato in nome della sicurezza, il tutto migliorando anche la sicurezza stessa*” ha concluso Vander Stoep.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Android](https://www.securityinfo.it/tag/android/), [linguaggio di programmazione](https://www.securityinfo.it/tag/linguaggio-di-programmazione/), [Rust](https://www.securityinfo.it/tag/rust/), [sicurezza del codice](https://www.securityinfo.it/tag/sicurezza-del-codice/), [sviluppo software](https://www.securityinfo.it/tag/sviluppo-software/), [vulnerabilità codice](https://www.securityinfo.it/tag/vulnerabilita-codice/)

[Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure](https://www.securityinfo.it/2025/11/18/impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_lgvdyplgvdyplgvd-120x85.png)](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/ "Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo")

  [Fantasy Hub: scoperto un nuovo RAT...](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/ "Permanent link to Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo")

  Nov 12, 2025  [0](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/#respond)
* [![Notification Protection, da Kaspersky un sistema anti-phishing per Android](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_9yqi019yqi019yqi-120x85.png)](https://www.securityinfo.it/2025/10/09/notification-protection-da-kaspersky-un-sistema-anti-phishing-per-android/ "Noti...