---
title: Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager
url: https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-14
fetch_date: 2025-10-07T00:49:17.064408
---

# Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager

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

## Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager

Ago 12, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/#respond)

---

Una nuova campagna di **attacchi informatici** sta prendendo di mira i sistemi Fortinet, iniziando con un’ondata coordinata di **tentativi di accesso brute-force** alle SSL VPN e proseguendo con un improvviso cambio di obiettivo verso i server **FortiManager**.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-1024x683.png)

Secondo i dati della società di threat intelligence **GreyNoise**, il picco di attività si è verificato il **3 agosto 2025**, quando sono stati rilevati oltre **780 indirizzi IP unici** coinvolti nell’operazione. Nel solo ultimo giorno di monitoraggio, **56 IP distinti** sono stati individuati come sorgenti malevole, provenienti da **Stati Uniti, Canada, Russia e Paesi Bassi**. Gli obiettivi colpiti includono infrastrutture in **Stati Uniti, Hong Kong, Brasile, Spagna e Giappone**.

GreyNoise ha sottolineato che il traffico malevolo era diretto in modo specifico verso il **profilo FortiOS**, un segnale che esclude un’attività casuale e indica invece un’azione **mirata e pianificata**.

### Due ondate di attacco distinte

L’analisi del traffico ha individuato **due fasi separate**. La prima, di lunga durata, è stata caratterizzata da **un’unica firma TCP** costante nel tempo. La seconda, invece, ha mostrato **un incremento improvviso e concentrato** di tentativi, con una firma TCP differente.

Dopo il **5 agosto**, il pattern di attacco è cambiato: la firma di rete non era più associata a **FortiOS** ma puntava **costantemente ai server FortiManager**. Questo, per gli analisti, suggerisce un **pivot degli attaccanti** verso un altro servizio Fortinet, forse utilizzando la stessa infrastruttura o lo stesso toolkit iniziale.

Un’analisi retrospettiva delle firme TCP utilizzate dopo il 5 agosto ha rivelato un **picco precedente**, a giugno, legato a **una firma client unica** che risultava collegata a un dispositivo **FortiGate** situato in un blocco IP gestito dall’ISP **Pilot Fiber Inc.**

Questo elemento apre a due ipotesi: o il tool di brute-force è stato **testato o lanciato da una rete domestica**, oppure gli aggressori hanno sfruttato **un proxy residenziale** per mascherare la propria origine.

### Il possibile preludio a una nuova vulnerabilità

Il contesto di questa attività desta ulteriori preoccupazioni. GreyNoise ha infatti evidenziato che **picchi simili di traffico malevolo** sono spesso seguiti, entro circa **sei settimane**, dalla pubblicazione di **un nuovo CVE** che colpisce la stessa tecnologia bersagliata.

Il fenomeno, osservato soprattutto su **tecnologie edge aziendali** come VPN, firewall e strumenti di accesso remoto, è già noto tra i team di threat intelligence: un segnale di possibile **attività di ricognizione e testing** da parte di gruppi avanzati, prima dello sfruttamento di **vulnerabilità ancora non divulgate**.

In questo scenario, gli esperti raccomandano ai responsabili IT e ai team di sicurezza di **monitorare attentamente i log di accesso alle VPN Fortinet**, rafforzare le **politiche di autenticazione** e tenere alta l’attenzione su eventuali aggiornamenti di sicurezza rilasciati dal vendor nelle prossime settimane.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi informatici](https://www.securityinfo.it/tag/attacchi-informatici/), [brute-force](https://www.securityinfo.it/tag/brute-force/), [CVE](https://www.securityinfo.it/tag/cve/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [firewall](https://www.securityinfo.it/tag/firewall/), [FortiManager](https://www.securityinfo.it/tag/fortimanager/), [fortinet](https://www.securityinfo.it/tag/fortinet/), [Fortios](https://www.securityinfo.it/tag/fortios/), [GreyNoise](https://www.securityinfo.it/tag/greynoise/), [sicurezza informatica](https://www.securityinfo.it/tag/sicurezza-informatica/), [VPN](https://www.securityinfo.it/tag/vpn/)

[Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/)
[Un invito Google Calendar bastava per prendere il controllo di Gemini](https://www.securityinfo.it/2025/08/11/un-invito-google-calendar-bastava-per-prendere-il-controllo-di-gemini/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/wp-content/uploads/2025/10/hacker-3342696_1920-120x85.jpg)](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/ "Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%")

  [Impennata delle scansioni dei portali...](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/ "Permanent link to Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%")

  Ott 06, 2025  [0](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/#respond)
* [![Microsoft Sentinel: arriva l’era degli...