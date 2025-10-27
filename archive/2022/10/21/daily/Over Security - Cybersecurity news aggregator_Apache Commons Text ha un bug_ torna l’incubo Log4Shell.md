---
title: Apache Commons Text ha un bug: torna l’incubo Log4Shell
url: https://www.securityinfo.it/2022/10/20/apache-commons-text-bug-log4shell/?utm_source=rss&utm_medium=rss&utm_campaign=apache-commons-text-bug-log4shell
source: Over Security - Cybersecurity news aggregator
date: 2022-10-21
fetch_date: 2025-10-03T20:31:15.813338
---

# Apache Commons Text ha un bug: torna l’incubo Log4Shell

Aggiornamenti recenti Ottobre 1st, 2025 2:22 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)
* [Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/)

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

## Apache Commons Text ha un bug: torna l’incubo Log4Shell

Ott 20, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/10/20/apache-commons-text-bug-log4shell/#respond)

---

**L’incubo del bug [Log4Shell](https://www.securityinfo.it/2022/04/27/log4shell-il-rischio-di-attacchi-e-ancora-alto/) è tornato**: su **Apache Commons Text**, una libreria Java, è stata individuata u**na vulnerabilità molto simile a quella di Log4J**. Si tratta di un bug molto grave che risiede ancora una volta nel **processo di interpolazione di stringhe**.

In Commons Text, un toolkit general-purpose per la manipolazione di testi, è presente un oggetto di tipo StringSubstitutor che permette di creare un interpolatore per sostituire le stringhe di input. **Tre funzioni, in particolare, rappresentano il pericolo maggiore: dns, script e url**. Tutte e tre permettono ai dati dall’esterno di essere processati e loggati nei server interni, provocando conseguenze diverse.

La prima funzione cerca il nome di un server e lo sostituisce con il valore inserito; l’attaccante può inserire un nome di dominio che controlla così che il processo di lookup termini sul DNS server di sua scelta, riuscendo a mappare parti della rete interna dell’organizzazione.

La funzione url funziona in modo analogo e si connette al server name specificato. Con la funzione script, invece, **l’attaccante può eseguire codice remoto inserendolo nell’input della stringa da interpolare.** Quest’ultima funziona con versioni più vecchie di Java (come la 8 e la 11) che però vengono ancora utilizzate da molte organizzazioni.

![Apache Commons Text](https://www.securityinfo.it/wp-content/uploads/2022/10/laptop-g687f587f5_1920.jpg)

**Il bug è presente in tutte le versioni di Apache Commons Text precedenti alla 1.10.0.** La prima cosa da fare per proteggersi dalla vulnerabilità è aggiornare la libreria all’ultima versione, dove le funzioni sono disabilitate di default. Apache consiglia di controllare tutti i propri progetti per individuare la presenza del toolkit ed eventualmente aggiornarlo.

**Occorre poi sanificare gli input controllando la presenza di sequenze di caratteri potenzialmente pericolose.** Si tratta di una buona pratica da applicare non solo per questa vulnerabilità, ma in generale in qualsiasi sistema che lavori con dati di input e sostituzione di stringhe.

Anche se il bug non è grave quanto quello di Log4Shell è importante mantenere aggiornata la libreria e seguire gli aggiornamenti di Apache.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APache](https://www.securityinfo.it/tag/apache/), [apache commons text](https://www.securityinfo.it/tag/apache-commons-text/), [Log4j](https://www.securityinfo.it/tag/log4j/), [Log4Shell](https://www.securityinfo.it/tag/log4shell/), [sostituzione di stringhe](https://www.securityinfo.it/tag/sostituzione-di-stringhe/), [string interpolation](https://www.securityinfo.it/tag/string-interpolation/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[CISA individua nuove vulnerabilità per Advantech e Hitachi](https://www.securityinfo.it/2022/10/21/cisa-vulnerabilita-advantech-hitachi/)
[Una soluzione temporanea ai problemi di Exchange Online in Outlook](https://www.securityinfo.it/2022/10/20/una-soluzione-temporanea-ai-problemi-di-exchange-online-in-outlook/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di...