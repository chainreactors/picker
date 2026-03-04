---
title: Android: 129 vulnerabilità corrette, zero-day Qualcomm già sfruttata
url: https://www.securityinfo.it/2026/03/03/android-129-vulnerabilita-corrette-zero-day-qualcomm-gia-sfruttata/?utm_source=rss&utm_medium=rss&utm_campaign=android-129-vulnerabilita-corrette-zero-day-qualcomm-gia-sfruttata
source: Securityinfo.it
date: 2026-03-03
fetch_date: 2026-03-04T04:04:10.091796
---

# Android: 129 vulnerabilità corrette, zero-day Qualcomm già sfruttata

Aggiornamenti recenti Marzo 3rd, 2026 10:30 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Android: 129 vulnerabilità corrette, zero-day Qualcomm già sfruttata](https://www.securityinfo.it/2026/03/03/android-129-vulnerabilita-corrette-zero-day-qualcomm-gia-sfruttata/)
* [Una falla in Chrome sfrutta Gemini Live per scopi malevoli](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/)
* [Paradosso ransomware, pagamenti in calo ma attacchi ai massimi storici](https://www.securityinfo.it/2026/02/27/paradosso-ransomware-pagamenti-in-calo-ma-attacchi-ai-massimi-storici/)
* [Google API Keys: le chiavi pubbliche diventano credenziali sensibili](https://www.securityinfo.it/2026/02/27/google-api-keys-le-chiavi-pubbliche-diventano-credenziali-sensibili/)
* [Claude Code Security crea il panico, ma… non uccide la cyber](https://www.securityinfo.it/2026/02/25/claude-code-security-crea-il-panico-ma-non-uccide-la-cyber/)

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

## Android: 129 vulnerabilità corrette, zero-day Qualcomm già sfruttata

Mar 03, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/03/03/android-129-vulnerabilita-corrette-zero-day-qualcomm-gia-sfruttata/#respond)

---

Google ha rilasciato gli aggiornamenti di sicurezza Android di marzo correggendo **129 vulnerabilità**, tra cui una falla zero-day già sfruttata in attacchi mirati. La vulnerabilità, tracciata come CVE-2026-21385, interessa un componente grafico sviluppato da Qualcomm e, secondo quanto comunicato nel bollettino ufficiale, sarebbe oggetto di **“limited, targeted exploitation”**, ovvero di uno sfruttamento limitato, ma su bersagli precisi.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/Android_Vulnerabilità-1024x683.png)

### **CVE-2026-21385: overflow nel sottocomponente Graphics**

Secondo l’advisory pubblicato da Qualcomm il 3 febbraio, la vulnerabilità è un **integer overflow (o wraparound)** nel sottocomponente Graphics, sfruttabile da un attaccante locale per provocare **corruzione della memoria**.

L’azienda ha dichiarato di essere stato informato della vulnerabilità il 18 dicembre e di aver notificato i clienti il 2 febbraio. La falla, classificata come gravità elevata, coinvolgerebbe **235 chipset Qualcomm**, ampliando significativamente la superficie potenzialmente esposta.

**Dieci vulnerabilità critiche: RCE senza interazione utente**

Oltre alla zero-day Qualcomm, il bollettino Android di marzo include la correzione di **10 vulnerabilità critiche** nei componenti System, Framework e Kernel.

La più grave riguarda il componente System e potrebbe consentire **remote code execution senza necessità di privilegi aggiuntivi né interazione da parte dell’utente**. Una condizione che, se sfruttata in catene di exploit, potrebbe facilitare compromissioni silenziose su larga scala.

Le altre vulnerabilità critiche permettono escalation di privilegi o condizioni di denial-of-service, confermando come il livello di rischio nel layer basso del sistema operativo resti elevato, soprattutto in scenari dove gli aggiornamenti non vengono applicati tempestivamente.

### **Patch level 2026-03-01 e 2026-03-05: il nodo frammentazione**

Google ha distribuito **due livelli di patch**: 2026-03-01 e 2026-03-05. Il secondo include tutte le correzioni del primo, oltre a fix relativi a componenti closed-source di terze parti e a sottocomponenti del kernel, che potrebbero non essere applicabili a tutti i dispositivi.

Come noto, i dispositivi Google Pixel ricevono gli aggiornamenti in modo immediato, mentre gli altri vendor devono integrare, testare e adattare le patch alle specifiche configurazioni hardware. Questo passaggio **introduce ritardi** variabili che, in presenza di una zero-day già sfruttata, possono tradursi in finestre di esposizione significative.

Per i team di sicurezza mobile e per i CISO, l’episodio conferma la necessità di **monitorare costantemente i livelli di patch installati sui dispositivi aziendali**, soprattutto in ambienti BYOD o in flotte eterogenee. La presenza di chipset Qualcomm in centinaia di modelli rende la gestione del rischio ancora più complessa.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Android kernel vulnerability](https://www.securityinfo.it/tag/android-kernel-vulnerability/), [Android marzo 2026 patch](https://www.securityinfo.it/tag/android-marzo-2026-patch/), [Android security update](https://www.securityinfo.it/tag/android-security-update/), [Android vulnerability](https://www.securityinfo.it/tag/android-vulnerability/), [chipset Qualcomm exploit](https://www.securityinfo.it/tag/chipset-qualcomm-exploit/), [CVE-2026-21385](https://www.securityinfo.it/tag/cve-2026-21385/), [integer overflow graphics](https://www.securityinfo.it/tag/integer-overflow-graphics/), [memory corruption Android](https://www.securityinfo.it/tag/memory-corruption-android/), [patch level 2026-03-05](https://www.securityinfo.it/tag/patch-level-2026-03-05/), [Qualcomm zero-day](https://www.securityinfo.it/tag/qualcomm-zero-day/), [remote code execution Android](https://www.securityinfo.it/tag/remote-code-execution-android/), [sicurezza mobile enterprise](https://www.securityinfo.it/tag/sicurezza-mobile-enterprise/)

[Una falla in Chrome sfrutta Gemini Live per scopi malevoli](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

##### Altro in questa categoria

* [![Una falla in Chrome sfrutta Gemini Live per scopi malevoli](https://www.securityinfo.it/wp-content/uploads/2026/03/Browser-Corrotto-120x85.png)](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/ "Una falla in Chrome sfrutta Gemini Live per scopi malevoli")

  [Una falla in Chrome sfrutta Gemini Live...](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/ "Permanent link to Una falla in Chrome sfrutta Gemini Live per scopi malevoli")

  Mar 02, 2026
   [0](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/#respond)
* [![Paradosso ransomware, pagamenti in calo ma attacchi ai massimi storici](https://www.securityinfo.it/wp-content/uploads/2026/02/Ransomware-deipoveri2-120x85.png)](https://www.securityinfo.it/2026/02/27/paradosso-ransomware-pagamenti-in-calo-ma-attacchi-ai-massi...