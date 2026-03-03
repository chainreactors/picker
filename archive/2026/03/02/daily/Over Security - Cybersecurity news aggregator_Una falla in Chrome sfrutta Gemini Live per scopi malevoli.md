---
title: Una falla in Chrome sfrutta Gemini Live per scopi malevoli
url: https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-02
fetch_date: 2026-03-03T04:13:13.441861
---

# Una falla in Chrome sfrutta Gemini Live per scopi malevoli

Aggiornamenti recenti Marzo 2nd, 2026 2:30 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Una falla in Chrome sfrutta Gemini Live per scopi malevoli](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/)
* [Paradosso ransomware, pagamenti in calo ma attacchi ai massimi storici](https://www.securityinfo.it/2026/02/27/paradosso-ransomware-pagamenti-in-calo-ma-attacchi-ai-massimi-storici/)
* [Google API Keys: le chiavi pubbliche diventano credenziali sensibili](https://www.securityinfo.it/2026/02/27/google-api-keys-le-chiavi-pubbliche-diventano-credenziali-sensibili/)
* [Claude Code Security crea il panico, ma… non uccide la cyber](https://www.securityinfo.it/2026/02/25/claude-code-security-crea-il-panico-ma-non-uccide-la-cyber/)
* [Sandworm\_Mode: il “worm” della supply chain NPM](https://www.securityinfo.it/2026/02/24/sandworm_mode-il-worm-della-supply-chain-npm/)

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

## Una falla in Chrome sfrutta Gemini Live per scopi malevoli

Mar 02, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/#respond)

---

Palo Alto, azienda specializzata in sicurezza informatica, ha scoperto una vulnerabilità nel browser **Google Chrome** avrebbe potuto trasformare l’assistente AI integrato in uno strumento di sorveglianza e furto dati. Il problema è stato segnalato a Google dopodiché è stata catalogata come CVE-2026-0628 e corretta a gennaio con il rilascio di Chrome 143.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/Browser-Corrotto-1024x683.png)

Il problema riguardava **Gemini Live**, il pannello laterale AI di Chrome progettato per assistere l’utente nella navigazione tramite riassunti in tempo reale, esecuzione automatica di task e comprensione contestuale delle pagine web. Tutte funzioni molto utili, ma che che, come dimostra questo caso, ampliano in modo significativo la superficie d’attacco del browser.

### **L’AI nel browser: potere operativo e nuovi rischi**

Gemini Live è concepito per “vedere” ciò che vede l’utente: il modello accede al contenuto della pagina attiva, ne interpreta il contesto e può eseguire azioni complesse direttamente dall’interfaccia del browser. Questo approccio consente operazioni multi-step che, fino a poco tempo fa, richiedevano estensioni dedicate o interventi manuali.

Secondo l’analisi di Palo Alto Networks, proprio questo **accesso privilegiato all’ambiente di navigazione** rappresenta il punto critico. L’AI non è una semplice estensione: è un componente nativo del browser con capacità avanzate, incluse interazioni con file locali, screenshot delle schede, accesso a microfono e videocamera.

In altre parole, l’assistente dispone di permessi che vanno oltre quelli normalmente concessi a un’estensione tradizionale e se un attore malevolo riesce a inserirsi in quel flusso, eredita lo stesso livello di privilegio.

### **Come funzionava l’attacco: estensioni malevole e declarativeNetRequests**

La vulnerabilità CVE-2026-0628 avrebbe consentito a estensioni dannose di iniettare codice JavaScript all’interno del pannello Gemini Live. Per farlo, l’estensione doveva disporre di un set specifico di permessi attraverso l’API declarativeNetRequests che permette di intercettare e modificare richieste e risposte HTTPS.

Questa API nasce con finalità legittime, come il blocco di richieste intrusive o malevole, ma grazie alla possibilità di interagire con contenuti originati da Gemini e caricati nella scheda del sito **sarebbe potuta diventare un vettore** di compromissione.

In pratica, l’estensione avrebbe potuto intercettare il flusso tra il browser e il pannello AI, **inserendo codice in grado di sfruttare le capacità operative dell’assistente**. Tra gli scenari ipotizzati: attivazione silenziosa di microfono e videocamera, accesso ai file locali, cattura di screenshot delle schede aperte e persino l’orchestrazione di campagne phishing sfruttando l’interfaccia di Gemini.

Il punto più delicato è che il pannello Gemini è parte integrante del browser. Non si tratta di un plugin isolato, ma di un componente con accesso diretto alle risorse di sistema. **Il dirottamento dell’assistente avrebbe quindi permesso a un’estensione di aggirare i normali limiti di sicurezza**, ottenendo privilegi superiori rispetto a quelli previsti dal modello di sicurezza standard di Chrome.

### **Patch e implicazioni per la sicurezza dei browser AI-native**

Palo Alto Networks ha segnalato la vulnerabilità a Google lo scorso ottobre. La correzione è stata distribuita con le versioni 143.0.7499.192 e 143.0.7499.193 per Windows e macOS, e con la 143.0.7499.192 per Linux.

L’episodio evidenzia un tema destinato a diventare centrale nel dibattito sulla sicurezza applicativa: **l’integrazione nativa di modelli AI nei browser modifica radicalmente il perimetro di fiducia**. Se l’assistente dispone di accesso privilegiato per eseguire operazioni legittime, qualsiasi vulnerabilità nel suo canale di comunicazione diventa un moltiplicatore di rischio.

Per i professionisti della sicurezza IT, il caso CVE-2026-0628 rappresenta un campanello d’allarme che sentiamo ormai suonare sempre più spesso. L’evoluzione verso browser AI-native richiede una revisione delle strategie di hardening, monitoraggio delle estensioni e controllo dei permessi concessi. Non è più sufficiente valutare il rischio delle estensioni in modo isolato: occorre considerare anche l’interazione con componenti intelligenti ad alto privilegio

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AI assistant](https://www.securityinfo.it/tag/ai-assistant/), [browser security](https://www.securityinfo.it/tag/browser-security/), [Chrome 143 patch](https://www.securityinfo.it/tag/chrome-143-patch/), [CVE-2026-0628](https://www.securityinfo.it/tag/cve-2026-0628/), [declarativeNetRequests API](https://www.securityinfo.it/tag/declarativenetrequests-api/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [estensioni malevole](https://www.securityinfo.it/tag/estensioni-malevole/), [Gemini Live](https://www.securityinfo.it/tag/gemini-live/), [Google Chrome](https://www.securityinfo.it/tag/google-chrome/), [hijacking browser](https://www.securityinfo.it/tag/hijacking-browser/), [Palo Alto Networks](https://www.securityinfo.it/tag/palo-alto-networks/), [phishing via browser](https://www.securityinfo.it/tag/phishing-via-browser/), [sicurezza AI](https://www.securityinfo.it/tag/sicurezza-ai/), [vulnerabilità Chrome](https://www.securit...