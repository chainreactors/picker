---
title: Apple interviene su due zero-day sfruttati attivamente in attacchi mirati
url: https://www.securityinfo.it/2025/12/12/apple-interviene-su-due-zero-day-sfruttati-attivamente-in-attacchi-mirati/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-13
fetch_date: 2025-12-14T03:29:23.246238
---

# Apple interviene su due zero-day sfruttati attivamente in attacchi mirati

Aggiornamenti recenti Dicembre 12th, 2025 2:01 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Apple interviene su due zero-day sfruttati attivamente in attacchi mirati](https://www.securityinfo.it/2025/12/12/apple-interviene-su-due-zero-day-sfruttati-attivamente-in-attacchi-mirati/)
* [Misterioso guasto satellitare: centinaia di Porsche “bloccate” in Russia](https://www.securityinfo.it/2025/12/12/misterioso-guasto-satellitare-centinaia-di-porsche-bloccate-in-russia/)
* [Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-day](https://www.securityinfo.it/2025/12/11/patch-tuesday-microsoft-risolve-una-vulnerabilita-gia-sfruttata-e-due-zero-day/)
* [Prompt injection, un problema che potrebbe non venire mai risolto. La visione dell’NCSC](https://www.securityinfo.it/2025/12/10/prompt-injection-un-problema-che-potrebbe-non-venire-mai-risolto-la-visione-dellncsc/)
* [React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/)

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

## Apple interviene su due zero-day sfruttati attivamente in attacchi mirati

Dic 12, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/12/12/apple-interviene-su-due-zero-day-sfruttati-attivamente-in-attacchi-mirati/#respond)

---

Apple ha rilasciato degli aggiornamenti di sicurezza straordinari per correggere due vulnerabilità zero-day che, secondo quanto confermato dall’azienda, risultano essere state sfruttate in attacchi reali ad elevata sofisticazione. Il fatto che Apple parli esplicitamente di **attacchi mirati contro individui specifici** è particolarmente significativa in quanto già in passato si è dimostrata coerente con campagne di sorveglianza avanzata e operazioni di compromissione ad alto valore.

L’intervento fuori ciclo rafforza l’idea che **l’ecosistema Apple sia ormai un obiettivo stabile** per gruppi capaci di sviluppare exploit complessi e catene di attacco mirate, spesso utilizzate prima che le vulnerabilità vengano individuate e corrette pubblicamente.

![](https://www.securityinfo.it/wp-content/uploads/2025/12/MelaMorsicataeBuggata-1024x559.png)

**Vulnerabilità a livello di motore web e gestione della memoria**

Entrambe le falle corrette da Apple ricadono nell’ambito della **gestione della memoria all’interno di WebKit**, il motore di rendering utilizzato da Safari e obbligatorio per tutti i browser su iOS e iPadOS. La prima vulnerabilità riguarda **una condizione di tipo use-after-free**, una classe di bug particolarmente critica perché consente a un attaccante di manipolare aree di memoria già liberate, **aprendo la strada all’esecuzione di codice arbitrario**. La seconda vulnerabilità è invece riconducibile a un problema di corruzione della memoria, anch’esso attivabile **attraverso la visualizzazione di contenuti web** appositamente costruiti.

**Prodotti Apple effettivamente coinvolti**

Le vulnerabilità interessano un insieme ben definito di prodotti Apple attualmente supportati. Sul fronte mobile, risultano coinvolti iPhone a partire **da iPhone XS e successivi**, oltre a numerosi modelli di iPad, inclusi iPad Pro da 13 pollici, iPad Pro da 12,9 pollici dalla terza generazione in poi, iPad Pro da 11 pollici dalla prima generazione, iPad Air dalla terza generazione, iPad dalla settima generazione e iPad mini dalla quinta generazione.

Per quanto riguarda l’ambiente desktop, le correzioni riguardano macOS nelle versioni supportate, inclusi i rami **Sonoma, Ventura e Monterey**, oltre al browser Safari su macOS. La presenza di WebKit come componente condivisa rende trasversale l’impatto delle vulnerabilità, indipendentemente dal fatto che l’utente utilizzi Safari o un browser di terze parti.

**Aggiornamenti di sicurezza e mitigazioni introdotte**

Apple ha distribuito le patch attraverso aggiornamenti dedicati di iOS e iPadOS, aggiornamenti correttivi per macOS e un update specifico per Safari. Dal punto di vista tecnico, le mitigazioni introdotte puntano a **migliorare la gestione della memoria e a rafforzare i controlli interni** per prevenire condizioni di utilizzo improprio delle aree di memoria.

![](https://www.securityinfo.it/wp-content/uploads/2025/12/Apple_Aggiornamento.jpg)

Come da prassi in presenza di zero-day sfruttati attivamente, i dettagli tecnici forniti restano volutamente limitati. Questa scelta riduce il rischio che le informazioni pubbliche possano essere utilizzate per **sviluppare exploit affidabili** prima che una quota significativa di dispositivi venga aggiornata.

**Implicazioni operative per organizzazioni e utenti**

Dal punto di vista operativo, l’episodio conferma la necessità di trattare **gli aggiornamenti di sicurezza Apple con la stessa priorità riservata alle patch critiche in ambienti enterprise** tradizionali. La diffusione di dispositivi iOS e macOS in contesti aziendali rende essenziale disporre di processi di aggiornamento rapidi, in grado di ridurre al minimo la finestra di esposizione.

Per gli utenti ad alto profilo e per le organizzazioni che operano in settori sensibili, l’applicazione tempestiva degli aggiornamenti resta una delle poche contromisure realmente efficaci contro attacchi basati su zero-day. L’ennesima correzione di vulnerabilità già sfruttate in the wild ribadisce che **la sicurezza delle piattaforme Apple non può essere considerata implicitamente garantita**, ma va gestita con un approccio strutturato e continuo, allineato alle dinamiche delle minacce più avanzate.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Apple patch sicurezza](https://www.securityinfo.it/tag/apple-patch-sicurezza/), [Apple sicurezza](https://www.securityinfo.it/tag/apple-sicurezza/), [Attacchi mirati](https://www.securityinfo.it/tag/attacchi-mirati/), [cybersecurity Apple](https://www.securityinfo.it/tag/cybersecurity-apple/), [exploit browser](https://www.securityinfo.it/tag/exploit-browser/), [iOS sicurezza](https://www.securityinfo.it/tag/ios-sicurezza/), [iPadOS vulnerabilità](https://www.securityinfo.it/tag/ipados-vulnerabilita/), [macOS sicurezza](https://www.securityinfo.it/tag/macos-sicurezza/), [Safari exploit](https://www.securityinfo.it/tag/safari-exploit/), [spyware iOS](https://www.securityinfo.it/tag/spyware-ios/), [vulnerabilità zero-day](https://www.securityinfo.it/tag/vulnerabilita-zero-day/), [webkit](https://www.securityinfo.it/tag/webkit/)

[Misterioso guasto satellitare: centinaia di Porsche "bloccate" in Russia](https://www.securi...