---
title: Outlook può essere usato per l’esecuzione di codice da remoto
url: https://www.securityinfo.it/2024/07/31/outlook-puo-essere-usato-per-lesecuzione-di-codice-da-remoto/?utm_source=rss&utm_medium=rss&utm_campaign=outlook-puo-essere-usato-per-lesecuzione-di-codice-da-remoto
source: Securityinfo.it
date: 2024-08-01
fetch_date: 2025-10-06T18:06:09.722928
---

# Outlook può essere usato per l’esecuzione di codice da remoto

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

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

## Outlook può essere usato per l’esecuzione di codice da remoto

Lug 31, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/07/31/outlook-puo-essere-usato-per-lesecuzione-di-codice-da-remoto/#respond)

---

I ricercatori di sicurezza di TrustedSec hanno sviluppato un framework che consente di sfruttare **Outlook per eseguire codice da remoto** sulle macchine infette.

Il framework, chiamato **[Specula](https://github.com/trustedsec/specula/wiki)**, permette di creare una home page personalizzata di Outlook, sfruttare le chiavi di registro e comunicare con un web server python. Il funzionamento di Specula si basa sulla CVE-2017-11774, una vulnerabilità di security feature bypass del servizio Microsoft.

“*In uno scenario di file sharing, **un attaccante può usare un file creato appositamente per sfruttare la vulnerabilità e convincere gli utenti ad aprire il documento e interagirci***” spiega Microsoft nell’[advisory](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2017-11774) relativo al bug.

![Outlook](https://www.securityinfo.it/wp-content/uploads/2024/07/security-6901712_1920.jpg)

Pixabay

Dopo aver installato un ambiente virtuale per Python, è possibile eseguire il framework specificando una serie di opzioni di setup, tra le quali dns\_name per definire l’homepage a cui si collegherà e la porta dove rimanere in ascolto degli agenti. **Gli agenti sono i responsabili dell’esecuzione di codice sulle macchine**; per “agganciarne” uno alla macchina sfruttando Outlook è necessario creare la chiave URL di tipo REG\_SZ nel percorso *HKCU\Software\Microsoft\Office\16.0\Outlook\WebView\Inbox* e valorizzarla con l’url del server di Specula.

Per eseguire il codice sulla macchina, un attaccante si serve della homepage custom per eseguire file VBscript.

**Specula è organizzato in moduli e può essere esteso a piacimento**. I moduli sono divisi in diverse categorie, tra le quali l’*enumerate*, dove ricadono tutte le funzionalità per ottenere informazioni sul sistema, *execute* per l’esecuzione di comandi, e il modulo *trolling* che comprende varie azioni fini a se stesse ma fastidiose per l’utente.

Il framework non è il primo che sfrutta l’home page di Outlook come vettore d’attacco: in passato sono stati sviluppati numerosi tool che usavano questo meccanismo. Il fix di **Microsoft ha eliminato quegli elementi della UI della home page** problematici che consentivano l’esecuzione dei file VBscript, **ma non i valori di registro associati** all’uso di questi elementi.

Microsoft ha rilasciato un workaround per gestire questo problema, ma in molti casi non viene applicato. “***TrustedSec è stata in grado di sfruttare questo canale specifico per l’accesso iniziale in centinaia di clienti, nonostante le conoscenze esistenti e le misure di protezione disponibili** per questa tecnica. Per questi motivi, stiamo rilasciando una versione ridotta del nostro tooling per attirare l’attenzione su questo vettore e, auspicabilmente, chiuderlo definitivamente*” [ha spiegato](https://trustedsec.com/blog/specula-turning-outlook-into-a-c2-with-one-registry-change) la compagnia.

I ricercatori di TrustedSec invitano gli utenti ad **applicare il prima possibile il [workaround](https://support.microsoft.com/en-us/topic/outlook-home-page-feature-is-missing-in-folder-properties-d207edb7-aa02-46c5-b608-5d9dbed9bd04) indicato da Microsoft** e verificare nei percorsi *HKCU\Software\Microsoft\Office\16.0\Outlook\WebView\\*\**la presenza di un valore URL.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [hack](https://www.securityinfo.it/tag/hack/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Outlook](https://www.securityinfo.it/tag/outlook/), [Specula](https://www.securityinfo.it/tag/specula/), [TrustedSec](https://www.securityinfo.it/tag/trustedsec/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Scoperta una massiccia campagna malware contro Android in più di 113 Paesi](https://www.securityinfo.it/2024/07/31/scoperta-una-massiccia-campagna-malware-contro-android-in-piu-di-113-paesi/)
[Stargazer Goblin ha creato 3.000 account GitHub per diffondere malware](https://www.securityinfo.it/2024/07/30/stargazer-goblin-ha-creato-3-000-account-github-per-diffondere-malware/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-1...