---
title: Le appliance Fortinet sono sotto attacco da giorni
url: https://www.securityinfo.it/2023/02/27/le-appliance-fortinet-sono-sotto-attacco-da-giorni/?utm_source=rss&utm_medium=rss&utm_campaign=le-appliance-fortinet-sono-sotto-attacco-da-giorni
source: Securityinfo.it
date: 2023-02-28
fetch_date: 2025-10-04T08:15:39.005287
---

# Le appliance Fortinet sono sotto attacco da giorni

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

## Le appliance Fortinet sono sotto attacco da giorni

Feb 27, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Concept](https://www.securityinfo.it/category/minacce-2/concept/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/02/27/le-appliance-fortinet-sono-sotto-attacco-da-giorni/#respond)

---

Le appliance Fortinet esposte a Internet sono **sotto attacco da alcuni giorni** da parte di diversi attori, che stanno sfruttando la vulnerabilità [CVE-2022-39952](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39952).

Il problema, legato alla manipolazione del percorso dei file nel server FortiNAC, può essere abusato per **l’esecuzione di comandi remoti** ed era stato svelato dai ricercatori di Horizon3. Il team ha rilasciato un [exploit proof-of-concept](https://github.com/horizon3ai/CVE-2022-39952) che utilizza cron per avviare una shell inversa su sistemi compromessi con privilegi root.

> CVE-2022-39952, announced today, allows for unauthenticated RCE against [#Fortinet](https://twitter.com/hashtag/Fortinet?src=hash&ref_src=twsrc%5Etfw) FortiNAC as the root user. Blog post and POC to be released soon.
>
> See Fortinet’s PSIRT: <https://t.co/sBsrs8Wxqb> [pic.twitter.com/EqkIo3ap4s](https://t.co/EqkIo3ap4s)
>
> — Horizon3 Attack Team (@Horizon3Attack) [February 17, 2023](https://twitter.com/Horizon3Attack/status/1626692778062237713?ref_src=twsrc%5Etfw)

Fortinet ha reso pubblica la vulnerabilità in un avviso di sicurezza rivelando che **il bug riguarda più versioni del suo sistema di controllo degli accessi** FortiNAC e consente agli aggressori di eseguire codice o comandi non autorizzati.

L’azienda ha subito **rilasciato patch di sicurezza** e ha esortato tutti i clienti dei sistemi interessati ad aggiornare le appliance alle ultime versioni disponibili. L’azienda non ha fornito indicazioni o soluzioni alternative per la mitigazione, l’aggiornamento è quindi l’unico modo per contrastare i tentativi di attacco.

## Sfruttamento massivo

Molti aggressori hanno però **iniziato subito a sfruttare la vulnerabilità** per attaccare le appliance FortiNAC non ancora aggiornate, come hanno segnalato molte aziende di sicurezza, tra cui [Shadowserver](https://www.shadowserver.org/), [GreyNoise](https://viz.greynoise.io/tag/fortinac-rce-attempt?days=3) e [CronUp](https://www.cronup.com/explotacion-masiva-de-fortinet-fortinac-cve-2022-39952-rce-no-autenticado-en-progreso/).

![](https://www.securityinfo.it/wp-content/uploads/2023/02/CVE-2022-39952-exploit-payload.png)

Il payload dell’attacco (Fonte: CronUp)

Il ricercatore Germán Fernández di CronUp ha rivelato in un rapporto che l’azienda sta “registrando **un massiccio sfruttamento dei dispositivi Fortinet** FortiNAC tramite la vulnerabilità CVE-2022-39952”.

“Questa vulnerabilità è fondamentale nell’ecosistema della sicurezza informatica, poiché **potrebbe consentire l’accesso iniziale alla rete aziendale**”, ha affermato Fernández.

L’attività dannosa osservata durante l’analisi di questi attacchi **corrisponde alla modalità operativa del PoC** di Horizon3: CronUp ha notato come gli attori delle minacce utilizzino proprio cron per aprire shell inverse verso indirizzi IP degli aggressori.

La soluzione al problema è ormai nota da diversi giorni, e prevede un semplice **aggiornamento del software operativo** alla versione più recente; come accade sempre più spesso, però, in molti casi l’applicazione degli update si è fatta attendere troppo a lungo, lasciando le appliance e il resto della rete alla mercé degli attaccanti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cron](https://www.securityinfo.it/tag/cron/), [FortiNAC](https://www.securityinfo.it/tag/fortinac/), [fortinet](https://www.securityinfo.it/tag/fortinet/), [Reverse Enegineering](https://www.securityinfo.it/tag/reverse-enegineering/)

[Tre aziende su quattro hanno subito un attacco e-mail](https://www.securityinfo.it/2023/02/27/tre-aziende-su-quattro-hanno-subito-un-attacco-e-mail/)
[Niente più TikTok per i funzionari europei](https://www.securityinfo.it/2023/02/27/tiktok-commissione-europea/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  [Ondata di attacchi brute-force contro...](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Permanent link to Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  Ago 12, 2025  [0](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/#respond)
* [![Scoperto un RAT per Windows che corrompe gli header DOS e PE per l’elusione](https://www.securityinfo.it/wp-content/uploads/2025/05/banner-5185767_1920-120x85.jpg)](https://www.securityinfo.it/2025/05/30/scoperto-un-rat-per-windows-che-corrompe-gli-header-dos-e-pe-per-lelusione/ "Scoperto un RAT per Windows che corrompe gli header DOS e PE per l’elusione")

  [Scoperto un RAT per Windows che...](https://www.securityinfo.it/2025/05/30/scoperto-un-rat-per-...