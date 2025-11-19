---
title: Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure
url: https://www.securityinfo.it/2025/11/18/impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure/?utm_source=rss&utm_medium=rss&utm_campaign=impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure
source: Securityinfo.it
date: 2025-11-18
fetch_date: 2025-11-19T03:15:07.586780
---

# Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure

Aggiornamenti recenti Novembre 18th, 2025 10:17 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Rust riduce sensibilmente le vulnerabilità di memory safety in Android](https://www.securityinfo.it/2025/11/18/rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android/)
* [Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure](https://www.securityinfo.it/2025/11/18/impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure/)
* [Il protocollo di rete “Finger” rinasce in attacchi ClickFix](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/)
* [CERT-AGID 8–14 novembre: ondata di phishing su hosting, PagoPA e università](https://www.securityinfo.it/2025/11/17/cert-agid-8-14-novembre-ondata-di-phishing-su-hosting-pagopa-e-universita/)
* [Vulnerabilità di Fortinet FortiWeb sfruttata per creare utenti admin](https://www.securityinfo.it/2025/11/14/vulnerabilita-di-fortinet-fortiweb-sfruttata-per-creare-utenti-admin/)

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

## Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure

Nov 18, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/11/18/impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure/#respond)

---

Microsoft ha annunciato di aver subito un attacco massiccio di tipo DDoS che ha preso di mira la piattaforma Azure: il traffico immesso ha raggiunto un picco di 15,72 terabit al secondo (Tbps) e ha coinvolto **oltre 500.000 indirizzi IP distinti**. L’obiettivo era un indirizzo pubblico situato in Australia e l’evento **ha generato flussi UDP ad altissima intensità**, arrivando a circa 3,64 miliardi di pacchetti al secondo (bpps).

![](https://www.securityinfo.it/wp-content/uploads/2025/11/DDOS_Azure-1.jpg)

L’attacco è stato attribuito al botnet denominato Aisuru botnet che rientra nella categoria “Turbo Mirai-class” delle botnet basate su IoT. Il vettore sfruttava dispositivi IoT compromessi quali router domestici e telecamere IP, prevalentemente presso ISP residenziali negli Stati Uniti e in altri Paesi. Un dettaglio rilevante è che il traffico UDP generato mostrava **scarsa spoofing** degli indirizzi sorgente e utilizzava porte di origine casuali, un comportamento che ha facilitato le operazioni di traceback e l’intervento dei provider.

Questo evento non è isolato: pochi mesi prima, sempre Aisuru aveva generato un attacco da **22,2 Tbps e 10,6 miliardi di pacchetti al secondo**, mitigato da Cloudflare. Inoltre, la divisione di ricerca XLab della società cinese Qi’anxin aveva già attribuito al botnet un’operatività su circa 300.000 bot con capacità intorno agli 11,5 Tbps. Un meccanismo di propagazione particolarmente significativo è stato l’attacco alla catena di aggiornamento firmware di un produttore (TotoLink) che ha comportato **l’infezione di circa 100.000 dispositivi in un’unica operazione**.

### Le implicazioni per la supply-chain IoT e infrastrutturale

Dal punto di vista dell’ecosistema IT, l’evento mette in evidenza come la fusione tra dispositivi IoT di consumo e infrastrutture cloud di classe enterprise possa generare un effetto domino critico. Dispositivi domestici compromessi sono stati impiegati come vettore per un attacco diretto **contro una grande piattaforma cloud**. La **scelta di traffico UDP non spoofato** massivamente e con porte casuali suggerisce una fase pilota ben orchestrata e consapevole della gestione del rischio da parte dell’attaccante.

Per i provider cloud e gli operatori di rete la lezione è duplice. Da un lato occorre rafforzare le difese DDoS — in particolare la capacità di mitigazione a livelli oltre il “terabit” — dall’altro è necessario monitorare attivamente il fenomeno dei dispositivi IoT compromessi utilizzati come arma indiretta. In questo caso Azure è stata colpita da un bersaglio pubblico in Australia: la geografia, il volume e l’assetto del traffico implicano che **anche chi non è direttamente coinvolto nel target** può trovarsi a dover gestire ricadute su latenza, instradamento o capacità di risposta.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco 15 Tbps](https://www.securityinfo.it/tag/attacco-15-tbps/), [Azure](https://www.securityinfo.it/tag/azure/), [Azure sicurezza](https://www.securityinfo.it/tag/azure-sicurezza/), [botnet Aisuru](https://www.securityinfo.it/tag/botnet-aisuru/), [cloud provider](https://www.securityinfo.it/tag/cloud-provider/), [DDoS](https://www.securityinfo.it/tag/ddos/), [IoT botnet](https://www.securityinfo.it/tag/iot-botnet/), [mitigazione DDoS](https://www.securityinfo.it/tag/mitigazione-ddos/), [NIS2 compliance](https://www.securityinfo.it/tag/nis2-compliance/), [Turbo Mirai](https://www.securityinfo.it/tag/turbo-mirai/)

[Rust riduce sensibilmente le vulnerabilità di memory safety in Android](https://www.securityinfo.it/2025/11/18/rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android/)
[Il protocollo di rete "Finger" rinasce in attacchi ClickFix](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_ij19w5ij19w5ij19-120x85.png)](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/ "Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo")

  [Attacchi DDoS ipervolumetrici, ancora...](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/ "Permanent link to Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo")

  Lug 17, 2025  [0](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/#respond)
* [![Europa sotto attacco: aumentano le attività DDoS e dei gruppi hacktivisti](https://www.securityinfo.it/wp-content/uploads/2025/05/24496417_sl_031420_28950_02-scaled-120x85.jpg)](https://www.securityinfo.it/2025/05/15/europa-sotto-attacco-aumentano-le-attivita-ddos-e-dei-gruppi-hacktivisti/ "Europa sotto attacco: aumentano le attività DDoS e dei gruppi hacktivisti")

  [Europa sotto attacco: aumentano le...](https://www.securityinfo.it/2025/05/15/europa-sotto-attacco-aumentano-le-attivita-ddos-e-dei-gruppi-hacktivisti/ "Permanent link to Europa sotto attacco: aumentano le att...