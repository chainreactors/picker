---
title: Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-day
url: https://www.securityinfo.it/2025/12/11/patch-tuesday-microsoft-risolve-una-vulnerabilita-gia-sfruttata-e-due-zero-day/?utm_source=rss&utm_medium=rss&utm_campaign=patch-tuesday-microsoft-risolve-una-vulnerabilita-gia-sfruttata-e-due-zero-day
source: Securityinfo.it
date: 2025-12-11
fetch_date: 2025-12-12T03:23:08.546209
---

# Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-day

Aggiornamenti recenti Dicembre 11th, 2025 4:15 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-day](https://www.securityinfo.it/2025/12/11/patch-tuesday-microsoft-risolve-una-vulnerabilita-gia-sfruttata-e-due-zero-day/)
* [Prompt injection, un problema che potrebbe non venire mai risolto. La visione dell’NCSC](https://www.securityinfo.it/2025/12/10/prompt-injection-un-problema-che-potrebbe-non-venire-mai-risolto-la-visione-dellncsc/)
* [React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/)
* [CERT-AGID 29 novembre – 5 dicembre: phishing a tema Governo italiano e Agenzia delle Entrate](https://www.securityinfo.it/2025/12/08/cert-agid-29-novembre-5-dicembre-phishing-governo-italiano-agenzia-entrate/)
* [Iniezione indiretta di prompt: a rischio le informazioni aziendali](https://www.securityinfo.it/2025/12/05/iniezione-indiretta-di-prompt-a-rischio-le-informazioni-aziendali/)

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

## Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-day

Dic 11, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/12/11/patch-tuesday-microsoft-risolve-una-vulnerabilita-gia-sfruttata-e-due-zero-day/#respond)

---

Nel [bollettino](https://msrc.microsoft.com/update-guide/releaseNote/2025-Dec) del **Patch Tuesday di dicembre**Microsoft ha riportato di aver risolto **57 vulnerabilità**, di cui **una sfruttata attivamente e due zero-day già rese note**.

Il bug già sfruttato dagli attaccanti è il CVE-2025-62221, una vulnerabilità **Use-After-Free** che consente agli attaccanti di elevare i propri privilegi sul sistema e prenderne il controllo. Il bug colpisce il driver **Windows Cloud Files Mini Filter**. La vulnerabilità è particolarmente pericolosa perché non richiede né l’interazione dell’utente per essere sfruttata, né precondizioni particolari del sistema.

![Patch Tuesday](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_k6tcvck6tcvck6tc.png)

Le altre due vulnerabilità particolarmente d’interesse sono la CVE-2025-64671 e la CVE-2025-54100. Nel primo caso si parla di un **bug di command injection presente in Copilot** che consente agli attaccanti di eseguire codice da remoto sulla macchina compromessa. Anche in questo caso, non è necessaria l’interazione utente e non servono privilegi particolari per sfruttarlo.

“*Tramite un Cross Prompt Inject dannoso in file non attendibili o server MCP, un attaccante potrebbe eseguire comandi aggiuntivi aggiungendoli ai comandi consentiti nelle impostazioni di approvazione automatica del terminale dell’utente*” si legge nel [dettaglio](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-64671) della vulnerabilità.

La seconda vulnerabilità è sempre una **Command Injection, ma colpisce PowerShell.** Come il primo bug, anche questo permette a un attaccante di eseguire codice sulla macchina colpita; in questo caso, però, è necessaria l’interazione dell’utente per eseguire l’attacco.

Oltre a queste tre vulnerabilità, il Patch Tuesday di dicembre include le patch per 28 bug di elevation dei privilegi, 19 bug che consentono l’esecuzione di codice da remoto, 4 bug di information disclosure, 3 bug di denial of service e 2 bug di spoofing.

La lista di 57 vulnerabilità non considera le 13 CVE aggiuntive che colpiscono Edge e che sono state analizzate a inizio mese.

È ovviamente consigliato applicare il prima possibile le patch rilasciate dalla [compagnia](https://www.securityinfo.it/2025/06/11/microsoft-rilascia-patch-per-67-bug-di-cui-uno-gia-sfruttato/).

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [command injection](https://www.securityinfo.it/tag/command-injection/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Patch Tuesday](https://www.securityinfo.it/tag/patch-tuesday/), [Use-After-Free](https://www.securityinfo.it/tag/use-after-free/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[Prompt injection, un problema che potrebbe non venire mai risolto. La visione dell'NCSC](https://www.securityinfo.it/2025/12/10/prompt-injection-un-problema-che-potrebbe-non-venire-mai-risolto-la-visione-dellncsc/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_uj8xe1uj8xe1uj8x-120x85.png)](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/ "React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite")

  [React2Shell: più di 160.000 indirizzi...](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/ "Permanent link to React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite")

  Dic 09, 2025  [0](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/#respond)
* [![PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_ydrt5rydrt5rydrt-120x85.png)](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/ "PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML")

  [PickleScan, scoperti tre bug 0-day che...](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/ "Permanent link to PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML")

  Dic 03, 2025  [0](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/#respond)
* [![DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_87vil587vil587vi-120x85.png)](ht...