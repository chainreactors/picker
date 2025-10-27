---
title: Gli hub smart home a rischio hacking: il caso ChutterHub
url: https://www.securityinfo.it/2022/11/22/hub-smart-home-rischio-hacking/?utm_source=rss&utm_medium=rss&utm_campaign=hub-smart-home-rischio-hacking
source: Over Security - Cybersecurity news aggregator
date: 2022-11-23
fetch_date: 2025-10-03T23:30:30.130630
---

# Gli hub smart home a rischio hacking: il caso ChutterHub

Aggiornamenti recenti Ottobre 3rd, 2025 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)

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

## Gli hub smart home a rischio hacking: il caso ChutterHub

Nov 22, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/)
 [0](https://www.securityinfo.it/2022/11/22/hub-smart-home-rischio-hacking/#respond)

---

**Gli hub delle smart home non sono così sicuri come pensiamo.** Alcuni ricercatori dell’Università della Georgia hanno sviluppato un sistema in grado di collegarsi a un hub e monitorarne l’attività.

Questi sistemi centralizzati gestiscono i dispositivi smart presenti nelle case, come telecamere, serrature intelligenti, frigoriferi e molti altri. Gli hub sono considerati una soluzione sicura per la gestione dei device, perché questi ultimi **non devono essere più collegati alla rete per funzionare.** L’hub centrale si occupa di inviare pacchetti criptati al singolo dispositivo per recapitargli le azioni da compiere.

![hub smart home](https://www.securityinfo.it/wp-content/uploads/2022/11/smart-home-3574545_1280.jpg)

Un team di ricercatori dell’UGA ha però dimostrato che è possibile venire a conoscenza di tutte le attività all’interno di una smart home, per di più senza bisogno di decifrare i pacchetti scambiati tra l’hub e i dispositivi.

## Gli attacchi contro gli hub delle smart home

**ChutterHub**, questo il nome del sistema sviluppato dal team, **è riuscito ad accedere all’attività del 90% degli hub smart home presi in esame**. Se è vero che il traffico dei dispositivi è cifrato, la brutta notizia è che nella maggior parte dei casi non serve avere i dati in chiaro per monitorare le attività della casa.

Sebbene un hacker non riesca ad accedere al contenuto dei pacchetti, può comunque analizzarne i pattern, la lunghezza e il tempismo per ottenere le informazioni di cui ha bisogno.

**Un attaccante potrebbe estrapolare le abitudini degli inquilini e sapere quando la casa è vuota**; inoltre è sempre possibile iniettare un pacchetto nella comunicazione tra l’hub e i dispositivi per generare dei malfunzionamenti. Si potrebbe, ad esempio, **impedire la corretta chiusura della porta senza che risulti sull’applicazione centrale**, o sommergere l’hub di pacchetti per consumare la batteria rimasta e mettere fuori uso il sistema.

![hub smart home](https://www.securityinfo.it/wp-content/uploads/2022/11/pexels-fabian-hurnaus-977296.jpg)

Solo le compagnie produttrici di smart hub possono risolvere il problema. Ci sono diverse soluzioni percorribili, due delle quali sono di semplice implementazione: la prima è **l’aggiunta di un padding ai pacchetti per renderli tutti della stessa lunghezza**; la seconda è **l’implementazione di una *random sequence injection* per inviare pacchetti inutili a intervalli irregolari** e rendere più difficile per gli attaccanti individuare quelli veri.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [chutterhub](https://www.securityinfo.it/tag/chutterhub/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [Hacking](https://www.securityinfo.it/tag/hacking/), [hub smart home](https://www.securityinfo.it/tag/hub-smart-home/), [iot device](https://www.securityinfo.it/tag/iot-device/), [Smart Home](https://www.securityinfo.it/tag/smart-home/)

[Il settore dei trasporti nel mirino dello smishing](https://www.securityinfo.it/2022/11/23/il-settore-dei-trasporti-nel-mirino-dello-smishing/)
[La crisi energetica e i conflitti tra Stati favoriranno gli attacchi all’industria](https://www.securityinfo.it/2022/11/22/la-crisi-energetica-e-i-conflitti-tra-stati-favoriranno-gli-attacchi-allindustria/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![TeamItaly, presentata la nuova squadra di giovani cyber defender](https://www.securityinfo.it/wp-content/uploads/2025/09/conferenza_stampa_gruppo_TeamItaly_Marco_Cervellini_CNA_e_Paolo_Prinetto_CINI-scaled-120x85.jpg)](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/ "TeamItaly, presentata la nuova squadra di giovani cyber defender")

  [TeamItaly, presentata la nuova squadra...](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/ "Permanent link to TeamItaly, presentata la nuova squadra di giovani cyber defender")

  Set 15, 2025  [0](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/#respond)
* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  [Ondata di attacchi brute-force contro...](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Permanent link to Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  Ago 12, 2025  [0](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/#respond)
* [![Un invito Google Calendar bastava per prendere il controllo di Gemini](https://www.securityinfo.it/wp-content/uploads/2025/08/Calendar11-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/11/un-invito-google-calendar-bastava-per-prendere-il-controllo-di-gemini/ "Un invito Google Calendar bastava per prendere il controllo di Gemini")

  [Un invito Google Calendar bastava per...](https://www.securityinfo.it/2...