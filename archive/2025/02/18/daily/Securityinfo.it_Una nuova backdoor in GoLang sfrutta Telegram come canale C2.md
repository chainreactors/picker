---
title: Una nuova backdoor in GoLang sfrutta Telegram come canale C2
url: https://www.securityinfo.it/2025/02/17/una-nuova-backdoor-in-golang-sfrutta-telegram-come-canale-c2/?utm_source=rss&utm_medium=rss&utm_campaign=una-nuova-backdoor-in-golang-sfrutta-telegram-come-canale-c2
source: Securityinfo.it
date: 2025-02-18
fetch_date: 2025-10-06T20:47:29.019468
---

# Una nuova backdoor in GoLang sfrutta Telegram come canale C2

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

## Una nuova backdoor in GoLang sfrutta Telegram come canale C2

Feb 17, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2025/02/17/una-nuova-backdoor-in-golang-sfrutta-telegram-come-canale-c2/#respond)

---

La scorsa settimana **Netskope** [ha individuato](https://www.netskope.com/blog/telegram-abused-as-c2-channel-for-new-golang-backdoor) una nuova **backdoor** **che sfrutta Telegram come canale di comunicazione C2.**

“*Anche se l’uso di app cloud come canali C2 non è qualcosa che vediamo tutti i giorni, è un metodo molto efficace utilizzato dai cybercriminali non solo perché non è necessario implementare un’intera infrastruttura, rendendo la vita degli attaccanti più facile, ma anche perché **è molto difficile, dal punto di vista di chi si occupa di sicurezza, differenziare un normale utente che utilizza un’API e una comunicazione C2***” ha spiegato Leandro Fróes, ricercatore senior di Netskope.

![backdoor Telegram](https://www.securityinfo.it/wp-content/uploads/2025/02/telegram-5952449_1920.jpg)

Scritta in GoLang, la backdoor sfrutta un **package Go open-source per interagire con Telegram**, facendone il proprio meccanismo C2. Il package inizialmente crea un bot usando la feature **BotFather** dell’app di messaggistica; in seguito, crea un canale dove controlla la ricezione di nuovi comandi per eseguirli.

Secondo quanto riportato da Fróes, il malware supporta quattro diversi comandi: `/cmd`, per eseguire comandi tramite Powershell; `/persist`, per rieseguire se stessa sotto C:\Windows\Temp\svchost.exe; `/screenshot`, attualmente non implementato; `/selfdestruct` per autodistruggersi.

**Il comando `/cmd` è l’unico che richiede due messaggi per essere eseguito** dalla backdoor: il primo contenente il comando stesso, il secondo il comando Powershell da eseguire. Dopo aver ricevuto il primo comando, il malware risponde con “Inserisci il comando:” in russo e si mette in attesa di ricevere istruzioni.

Vista la lingua usata per la comunicazione, è molto probabile che la backdoor sia di **origine russa**, anche se non ci sono ancora indicazioni sull’identità degli attaccanti.

Fróes ha sottolineato che, vista la semplicità con cui viene eseguito, la minaccia analizzata non va presa sottogamba. **“*L’uso di applicazioni cloud rappresenta una sfida complessa per gli esperti di sicurezza e gli attaccanti ne sono consapevoli*“** ha ribadito. La presenza di un comando non ancora implementato indica che la backdoor è ancora in fase di sviluppo, ma è comunque funzionante. Al momento non si hanno informazioni su se e contro chi sia stato usato il malware.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [BotFather](https://www.securityinfo.it/tag/botfather/), [C2](https://www.securityinfo.it/tag/c2/), [GoLang](https://www.securityinfo.it/tag/golang/), [malware](https://www.securityinfo.it/tag/malware/), [telegram](https://www.securityinfo.it/tag/telegram/)

[Acronis: AI e ransomware le minacce del 2024, l’Italia tra i più colpiti](https://www.securityinfo.it/2025/02/17/acronis-threat-research-ai-ransomware-minacce-2024-italia/)
[CERT AGID 08-14 febbraio: GoldenLeaks diffonde una combolist di 90.000 account italiani](https://www.securityinfo.it/2025/02/17/cert-agid-08-14-febbraio-goldenleaks-combolist-di-90-000-account-italiani/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/#respond)
* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  [Cina contro Nvidia: dubbi sulla...](https://www.securit...