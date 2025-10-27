---
title: Lenovo, il chatbot AI “Lena” era troppo loquace
url: https://www.securityinfo.it/2025/08/20/lenovo-il-chatbot-ai-lena-era-troppo-loquace/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-21
fetch_date: 2025-10-07T00:49:50.842549
---

# Lenovo, il chatbot AI “Lena” era troppo loquace

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## Lenovo, il chatbot AI “Lena” era troppo loquace

Ago 20, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/08/20/lenovo-il-chatbot-ai-lena-era-troppo-loquace/#respond)

---

Il chatbot di assistenza clienti di Lenovo, chiamato **Lena**, è risultato esposto a una grave vulnerabilità che avrebbe permesso a un attaccante remoto di eseguire codice malevolo e sottrarre dati sensibili. La falla, individuata [dai ricercatori di Cybernews](https://cybernews.com/security/lenovo-chatbot-lena-plagued-by-critical-vulnerabilities/) e resa pubblica a inizio agosto, dimostra ancora una volta quanto i sistemi basati su intelligenza artificiale possano trasformarsi in un veicolo di rischio se non adeguatamente protetti.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/Lenovo20-ago-2025CG-1024x683.png)

**L’attacco con un solo prompt**

Il problema risiedeva nella gestione degli input forniti al chatbot. Attraverso un prompt appositamente costruito, lungo circa 400 caratteri, era possibile indurre Lena a restituire contenuti in formato HTML e JSON che includevano codice potenzialmente eseguibile dal browser della vittima. In questo modo, con un semplice comando, il sistema avrebbe inviato i cookie di sessione verso un server controllato dall’attaccante, consentendo di prendere il controllo delle conversazioni e di accedere a informazioni riservate.

Una volta ottenuti i cookie, gli aggressori avrebbero potuto muoversi liberamente nel portale di supporto, leggere dati personali, interagire con i sistemi e persino tentare installazioni di backdoor per mantenere un accesso persistente.

**Il ruolo della scarsa validazione**

Secondo l’analisi dei ricercatori, il cuore della vulnerabilità risiedeva nella mancanza di filtri adeguati su input e output del modello. Il chatbot non solo accettava comandi malevoli senza alcun controllo, ma li restituiva all’utente senza applicare procedure di sanificazione. L’assenza di regole di escaping e di restrizioni sull’esecuzione di codice lato client ha amplificato l’impatto della falla, trasformando un semplice prompt in un’arma capace di compromettere l’intero sistema di assistenza.

La vulnerabilità è stata scoperta e segnalata il 22 luglio 2025. Lenovo ha riconosciuto ufficialmente il problema il 6 agosto e, poco meno di due settimane più tardi, ha rilasciato una patch correttiva.

Con il diffondersi dei sistemi di AI, diventa sempre più impellente la creazione di un know how di sicurezza su questi sistemi che, per forza di cose, avrà bisogno di tempo per formarsi. Quello del prompt engineering è un settore ancora in rapida espansione, ma che bisogna tenere ben presente per evitare altri casi come questo.

**Aggiornamento:**
Lenovo ha rilasciato una dichiarazione sull’accaduto che riportiamo di seguito:

> *Lenovo prende molto seriamente la sicurezza dei propri prodotti e la protezione dei propri clienti. Di recente siamo stati informati da un ricercatore di sicurezza esterno di una vulnerabilità di tipo cross-site scripting (XSS) nel chatbot. Non appena venuti a conoscenza del problema, abbiamo valutato tempestivamente il rischio e adottato misure correttive per mitigare l’impatto potenziale e risolvere la questione. Ringraziamo i ricercatori per la segnalazione responsabile, che ci ha permesso di implementare una soluzione senza mettere a rischio i nostri clienti.*

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi AI customer service](https://www.securityinfo.it/tag/attacchi-ai-customer-service/), [exploit chatbot Lenovo](https://www.securityinfo.it/tag/exploit-chatbot-lenovo/), [Lenovo chatbot attacco](https://www.securityinfo.it/tag/lenovo-chatbot-attacco/), [Lenovo Lena vulnerabilità](https://www.securityinfo.it/tag/lenovo-lena-vulnerabilita/), [Lenovo patch agosto 2025](https://www.securityinfo.it/tag/lenovo-patch-agosto-2025/), [prompt injection AI](https://www.securityinfo.it/tag/prompt-injection-ai/), [rischio sicurezza AI](https://www.securityinfo.it/tag/rischio-sicurezza-ai/), [sicurezza AI chatbot](https://www.securityinfo.it/tag/sicurezza-ai-chatbot/), [vulnerabilità intelligenza artificiale](https://www.securityinfo.it/tag/vulnerabilita-intelligenza-artificiale/), [XSS chatbot Lena](https://www.securityinfo.it/tag/xss-chatbot-lena/)

[Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/)
[PyPI blocca i “domain resurrection”: disattivate 1.800 email](https://www.securityinfo.it/2025/08/19/pypi-blocca-i-domain-resurrection-disattivate-1-800-email/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)](https://www.securityinfo.it/wp-content/uploads/2025/06/LLMScope13-giu-2025CG-120x85.png)](https://www.securityinfo.it/2025/06/13/echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot/ "EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)")

  [EchoLeak: è arrivata la prima...](https://www.securityinfo.it/2025/06/13/echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot/ "Permanent link to EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)")

  Giu 13, 2025  [0](https://www.secur...