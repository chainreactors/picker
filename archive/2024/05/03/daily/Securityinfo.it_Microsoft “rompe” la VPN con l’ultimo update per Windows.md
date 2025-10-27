---
title: Microsoft “rompe” la VPN con l’ultimo update per Windows
url: https://www.securityinfo.it/2024/05/02/microsoft-rompe-la-vpn-con-lultimo-update-per-windows/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-rompe-la-vpn-con-lultimo-update-per-windows
source: Securityinfo.it
date: 2024-05-03
fetch_date: 2025-10-06T17:15:41.399880
---

# Microsoft “rompe” la VPN con l’ultimo update per Windows

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

## Microsoft “rompe” la VPN con l’ultimo update per Windows

Mag 02, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/05/02/microsoft-rompe-la-vpn-con-lultimo-update-per-windows/#respond)

---

L’ultimo aggiornamento di sicurezza per Windows 11 sta creando un po’ di problemi: la versione 23H2 rilasciata ad aprile **sta bloccando il corretto funzionamento delle VPN**, e non solo.

“I dispositivi Windows potrebbero imbattersi in **problemi di connessione della VPN** dopo aver installato l’aggiornamento di sicurezza di aprile 2024 o la preview dell’aggiornamento di non-sicurezza” [si legge](https://learn.microsoft.com/en-us/windows/release-health/status-windows-11-23h2#vpn-connections-might-fail-after-installing-the-april-2024-security-update) sul blog di Microsoft.

Le piattaforme colpite dal bug comprendono anche le versioni 22H2 e 21H2 di Windows 11 e le versioni 22H2 e 21H2 di Windows 10, oltre a Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 e Windows Server 2008.

La compagnia non ha specificato qual è la causa di questo problema, né quanto ci vorrà per risolverlo.

![](https://www.securityinfo.it/wp-content/uploads/2024/04/hacking-3112539_1920-1.png)

Pixabay

I problemi dell’aggiornamento non hanno colpito solo la VPN, ma anche BitLocker, alcuni driver Smart Sound Technology di Intel e Copilot. I primi due bug sono stati già gestiti, mentre per l’ultimo il fix è ancora in lavorazione; nel dettaglio, **l’update di Edge installa un nuovo pacchetto non richiesto che mostra Microsoft Copilot tra le applicazioni installate.**

L’aggiornamento di Edge scarica infatti il pacchetto “Microsoft chat provider for Copilot in Windows” senza il permesso dell’utente, facendo sì che Copilot compaia tra le applicazioni installate sul dispositivo. Il pacchetto, spiega Microsoft, serve a preparare alcuni dispositivi Windows a una compatibilità futura con Copilot, ma **non installa né abilita l’effettiva esecuzione della feature.** La compagnia sottolinea inoltre che il provider non esegue alcun codice o processo e non raccoglie alcun dato sul dispositivo.

**Microsoft ha** **temporaneamente mitigato il problema** con un nuovo aggiornamento di Edge che però non è ancora disponibile per tutti i dispositivi. Si attende un nuovo update definitivo nelle prossime settimane.

La compagnia sta lavorando a dei fix per i due problemi e per il primo al momento non esistono workaround per mitigarlo; l’unica soluzione è **disinstallare l’aggiornamento** e attendere nuove comunicazioni, consapevoli però che in questo modo anche tutte le nuove funzionalità di sicurezza verranno disinstallate.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [aggiornamento](https://www.securityinfo.it/tag/aggiornamento/), [copilot](https://www.securityinfo.it/tag/copilot/), [Edge](https://www.securityinfo.it/tag/edge/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [VPN](https://www.securityinfo.it/tag/vpn/), [Windows](https://www.securityinfo.it/tag/windows/)

[Gli U.S.A. pubblicano nuove linee guida per gestire i rischi dell'IA](https://www.securityinfo.it/2024/05/02/gli-u-s-a-pubblicano-nuove-linee-guida-per-gestire-i-rischi-dell-ia/)
[Okta rileva un importante aumento di attacchi di credential stuffing](https://www.securityinfo.it/2024/04/30/okta-rileva-un-importante-aumento-di-attacchi-di-credential-stuffing/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  [Ondata di attacchi brute-force contro...](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Permanent link to Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  Ago 12, 2025  [0](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/#respond)
* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74-120x85.png)](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  [Secret Blizzard attacca le ambasciate...](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Permanent link to Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/#respond)
* [![Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-120x85.png)](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Grave alerta SharePoint: attacco in corso che elude le difese")
...