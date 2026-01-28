---
title: PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene
url: https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/?utm_source=rss&utm_medium=rss&utm_campaign=packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene
source: Securityinfo.it
date: 2026-01-27
fetch_date: 2026-01-28T03:35:19.528676
---

# PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene

Aggiornamenti recenti Gennaio 27th, 2026 5:27 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/)
* [C’è Sandworm dietro l’attacco contro il settore energetico polacco](https://www.securityinfo.it/2026/01/26/ce-sandworm-dietro-lattacco-contro-il-settore-energetico-polacco/)
* [Zendesk, sfruttato il sistema di ticketing per una campagna di spam massiva](https://www.securityinfo.it/2026/01/23/zendesk-sfruttato-il-sistema-di-ticketing-per-una-campagna-di-spam-massiva/)
* [Sfruttate 37 vulnerabilità zero-day nel primo giorno di Pwn2Own Automotive](https://www.securityinfo.it/2026/01/21/sfruttate-37-vulnerabilita-zero-day-nel-primo-giorno-di-pwn2own-automotive/)
* [StackWarp: scoperta una nuova vulnerabilità nei processori AMD](https://www.securityinfo.it/2026/01/20/stackwarp-scoperta-una-nuova-vulnerabilita-nei-processori-amd/)

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

## PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene

Gen 27, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/#respond)

---

La società di sicurezza Koi Security [ha pubblicato](https://www.koi.ai/blog/packagegate-6-zero-days-in-js-package-managers-but-npm-wont-act) una ricerca che ha sta scuotendo la comunità degli sviluppatori: i ricercatori hanno scoperto **sei vulnerabilità zero-day nei principali package manager dell’ecosistema JavaScript** (npm, pnpm, vlt e Bun) che permettono agli attaccanti di aggirare le difese usate per mitigare gli attacchi alla supply-chain dei pacchetti.

Negli ultimi anni il mondo JavaScript è stato al centro di una serie di attacchi alla supply-chain, tra i quali la [campagna Shai-Hulud](https://www.securityinfo.it/2025/11/25/torna-shai-ulud-centinaia-di-pacchetti-compromessi/) avvenuta lo scorso novembre che ha compromesso pacchetti NPM per distribuire malware. In risposta a questi attacchi, la difesa standard adottata da aziende e progetti open source è diventata **disabilitare gli script automatizzati durante l’installazione** (ad esempio con l’opzione –ignore-scripts di npm) e committare sempre i lockfile (package-lock.json, pnpm-lock.yaml, ecc.) per vincolare le versioni e le integrità dei pacchetti.

![NPM zero day](https://www.securityinfo.it/wp-content/uploads/2026/01/ChatGPT-Image-27-gen-2026-17_26_31.png)

Sebbene queste due tecniche siano considerate delle best practice di sicurezza, la ricerca di Koi Security ha dimostrato che esistono delle vulnerabilità, complessivamente chiamate **PackageGate**, che permettono di aggirarle; nel dettaglio, i bug zero-day individuati consentono di eseguire l’esecuzione di codice anche quando gli script sono disabilitati e invalidare l’integrità dei lockfile.

**Le tecniche di attacco sono diverse a seconda del tool usato**: nel caso di npm, un pacchetto di dipendenza Git può includere un file .npmrc manipolato che reindirizza il binario Git a uno script malevolo, eseguendo codice arbitrario; in pnpm il meccanismo che disattiva gli script durante la build non copre la fase di fetch da un repository Git, permettendo l’esecuzione dei preparativi dei pacchetti malevoli; in vlt un bug di path traversal nell’estrazione dei pacchetti consente di scrivere file ovunque nel filesystem; infine, in Bun la whitelist per i pacchetti di fiducia non valida la fonte dei pacchetti, consentendo l’inclusione e l’esecuzione di artefatti malevoli con nomi considerati “trusted”.

## NPM si rifiuta di risolvere i bug zero-day

Il team di Koi ha notificato il problema a tutti i vendor coinvolti; tutti si sono occupati di risolvere le vulnerabilità, tranne **NPM che ha affermato che il comportamento dell’ecosistema è “*quello atteso*” e non è quindi intervenuto per sanare i bug zero-day.** Il vendor ha specificato che “*gli utenti di npm sono responsabili della verifica dei contenuti dei pacchetti che scelgono di installare*“, sottolineando che essendo Git uno strumento esterno, essi non sono responsabili di quello che l’utente sceglie di fare.

I ricercatori si sono opposti a questa visione spiegando che –ignore-scripts nella documentazione di npm è esplicitamente consigliato per difendersi dai malware e che quindi se esistono percorsi di esecuzione che lo bypassano allora il modello di sicurezza è incompleto; inoltre eseguendo “npm install” l’utente non sta eseguendo Git manualmente, ma lo fa tramite npm: Git è formalmente un tool esterno, ma operativamente, in questo caso, la questione è diversa.

“***Gli* a*****bbiamo chiesto più volte di riconsiderare la decisione, sottolineando l’errore nella documentazione. Nessuna risposta.** Come ultimo tentativo, abbiamo utilizzato le nostre conoscenze personali per contattare qualcuno del team npm che potesse riconsiderare la decisione. Purtroppo, anche questo tentativo è stato un fallimento*” ha spiegato il team di Koi Security.

I ricercatori hanno sottolineato che disabilitare gli script e committare i lock file rimangono due indicazioni valide, ma **non sono la soluzione completa al problema**. Finché PackageGate non sarà risolto del tutto, le organizzazioni che dipendono da npm dovrebbero trattare le dipendenze come potenzialmente malevole e agire di conseguenza.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [npm](https://www.securityinfo.it/tag/npm/), [package-manager](https://www.securityinfo.it/tag/package-manager/), [PackageGate](https://www.securityinfo.it/tag/packagegate/), [supply chain](https://www.securityinfo.it/tag/supply-chain/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[C'è Sandworm dietro l'attacco contro il settore energetico polacco](https://www.securityinfo.it/2026/01/26/ce-sandworm-dietro-lattacco-contro-il-settore-energetico-polacco/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Una vulnerabilità di ASUS Live Update di sette anni fa viene ancora sfruttata](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_8rl13l8rl13l8rl1-120x85.png)](https://www.securityinfo.it/2025/12/19/una-vulnerabilita-di-asus-live-update-di-sette-anni-fa-viene-ancora-s...