---
title: I criminali hanno iniziato a usare il framework Havoc
url: https://www.securityinfo.it/2023/02/16/i-criminali-hanno-iniziato-a-usare-il-framework-havoc/?utm_source=rss&utm_medium=rss&utm_campaign=i-criminali-hanno-iniziato-a-usare-il-framework-havoc
source: Over Security - Cybersecurity news aggregator
date: 2023-02-17
fetch_date: 2025-10-04T06:53:21.004363
---

# I criminali hanno iniziato a usare il framework Havoc

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## I criminali hanno iniziato a usare il framework Havoc

Feb 16, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Keylogger](https://www.securityinfo.it/category/minacce-2/keylogger/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Trojan](https://www.securityinfo.it/category/minacce-2/trojan/)
 [0](https://www.securityinfo.it/2023/02/16/i-criminali-hanno-iniziato-a-usare-il-framework-havoc/#respond)

---

Diversi i ricercatori di sicurezza hanno iniziato a rilevare l’uso sempre più frequente di un **nuovo framework open source di comando e controllo** chiamato [Havoc](https://github.com/HavocFramework/Havoc) da parte della criminalità informatica, come alternativa a prodotti commerciali come Cobalt Strike

Havoc offre molte funzioni interessanti, tra cui la capacità di **lavorare su più piattaforme** e di evitare la rilevazione di Microsoft Defender su dispositivi Windows 11 aggiornati.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/FullSessionGraph.jpeg)

La dashboard di Havoc

Il kit di Havoc contiene una vasta gamma di moduli che consentono agli attaccanti di **eseguire varie attività sui dispositivi compromessi**, tra cui l’esecuzione di comandi, la gestione dei processi e il download di payload aggiuntivi.

Tutte queste attività possono essere **controllate attraverso una console di gestione basata sul web**, che fornisce una visione completa dei dispositivi, degli eventi e dell’output.

## Primi avvistamenti in the wild

Un gruppo sconosciuto ha usato Havoc **all’inizio di gennaio in un attacco contro un’organizzazione governativa** di cui non è stata resa nota l’identità, in un’azione individuata dal team di ricerca [Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace).

Il loader rilasciato sui sistemi compromessi disabilita l’Event Tracing for Windows (ETW) e il payload finale Havoc Demon viene **caricato senza le intestazioni** DOS e NT, per evitare il rilevamento.

Il framework è stato distribuito anche tramite **un pacchetto npm dannoso** che utilizza il typosquatting di un modulo legittimo (Aabquerys), come rilevato dal team di ricerca di [ReversingLabs](https://www.reversinglabs.com/).

Lucija Valentić, ricercatrice di ReversingLabs, ha commentato: “Demon.bin è un agente dannoso con funzionalità tipiche RAT (trojan di accesso remoto) che è stato generato utilizzando un framework open source C&C post compromissione chiamato Havoc. **Questo tool consente la creazione di agenti dannosi in diversi formati**, tra cui eseguibile di Windows PE, DLL PE e shellcode”.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/1628338308927.jpg)

Lucija Valentić, ricercatrice di ReversingLabs

## Alla ricerca di alternative

[Cobalt Strike](https://www.cobaltstrike.com/) è stato a lungo **lo** **strumento preferito da molti attori delle minacce** per rilasciare beacon sulle reti delle vittime e inviare ulteriori payload.

A causa dell’aumento della capacità di rilevazione dei difensori, **molti attaccanti stanno cercando alternative**, come [Brute Ratel](https://bruteratel.com/) e [Sliver](https://github.com/BishopFox/sliver), che aiutano ad eludere le soluzioni antivirus e di EDR.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/multi_pivot.jpeg)

Brute Ratel

Brute Ratel è stato utilizzato in attacchi sospettati di essere legati al gruppo sponsorizzato dalla Russia APT29, ma **alcune delle sue licenze sono finite nelle mani degli ex membri del gruppo ransomware Conti**.

Sliver è un framework C2 basato su Go sviluppato dai ricercatori della società di sicurezza informatica BishopFox, che è stato **utilizzato come alternativa a Cobalt Strike da vari attori delle minacce**, dai gruppi state-sponsored alle bande di criminali informatici.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Brute Ratel](https://www.securityinfo.it/tag/brute-ratel/), [Cobalt Strike](https://www.securityinfo.it/tag/cobalt-strike/), [Command and Control](https://www.securityinfo.it/tag/command-and-control/), [Havoc](https://www.securityinfo.it/tag/havoc/), [ReversingLabs](https://www.securityinfo.it/tag/reversinglabs/), [Sliver](https://www.securityinfo.it/tag/sliver/), [zscaler](https://www.securityinfo.it/tag/zscaler/)

[L'approccio DevSecOps risponde al bisogno di sicurezza](https://www.securityinfo.it/2023/02/17/lapproccio-devsecops-risponde-al-bisogno-di-sicurezza/)
[Aggiornamento d'emergenza per 8 milioni di veicoli Kia e Hyundai](https://www.securityinfo.it/2023/02/16/aggiornamento-di-emergenza-per-8-milioni-di-veicoli-kia-e-hyundai/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Indagine Zscaler: le aziende devono investire sulla resilienza informatica](https://www.securityinfo.it/wp-content/uploads/2025/03/2151841667-120x85.jpg)](https://www.securityinfo.it/2025/03/06/indagine-zscaler-le-aziende-devono-investire-sulla-resilienza-informatica/ "Indagine Zscaler: le aziende devono investire sulla resilienza informatica")

  [Indagine Zscaler: le aziende devono...](https://www.securityinfo.it/2025/03/06/indagine-zscaler-le-aziende-devono-investire-sulla-resilienza-informatica/ "Permanent link to Indagine Zscaler: le aziende devono investire sulla resilienza informatica")

  Mar 06, 2025  [0](https://www.securityinfo.it/2025/03/06/indagine-zscaler-le-aziende-devono-investire-sulla-resilienza-informatica/#respond)
* [![Zscaler...