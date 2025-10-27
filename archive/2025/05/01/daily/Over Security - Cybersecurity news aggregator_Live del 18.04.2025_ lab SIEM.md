---
title: Live del 18.04.2025: lab SIEM
url: https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-01
fetch_date: 2025-10-06T22:28:43.158120
---

# Live del 18.04.2025: lab SIEM

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [Live del 18.04.2025: lab SIEM](https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/)

Published by

Rocco Sicilia

on

[30 aprile 2025](https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/)

[![Live del 18.04.2025: lab SIEM](https://roccosicilia.com/wp-content/uploads/2025/04/screenshot-2025-04-20-at-23.54.59.png?w=1024)](https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/)

Il tema è stato scelto da una lista di argomenti che avevo in mente, ovviamente tutti legati tra di loro. La community su [Telegram](https://t.me/%2Ba7sF3JQV4bMzY2Nk) ha scelto: sessione lab di preparazione della piattaforma SIEM.

L’argomento si lega ad un filone che vorrei sviluppare nei prossimi mesi e su cui ha lavorato molto negli ultimi anni: gli strumenti di detection sono, a tutti gli effetti, gli strumenti che affronto durante i miei security test e conoscerli mi permette di sviluppare e provare tecniche di evasione sempre più efficaci. Inoltre conoscerne le potenzialità mi consente di dare suggerimenti precisi sui miglioramenti che possono essere fatti a livello di SIEM, EDR/XDR, design del SOC, ecc. Per finire questi strumenti funzionano tanto meglio quanto sono integrati tra loro e gestiti da persone che sanno quello che fanno (rif. [a questo post](https://roccosicilia.com/2025/04/19/misp-studio-ed-integrazione/)).

La sessione live l’ho dedicata al setup di una istanza Elastic all’interno del mio lab, strumento che va ad affiancare una istanza ***Splunk*** (di cui sono sempre stato fan) e diversi sistemi di detection. Lo stesso lab presenta una istanza MISP su cui lavoreremo come community.

---

Se gli argomenti che porto su questo blog e sulle altre piattaforme ti sono utili e vuoi supportare il progetto di divulgazione puoi sostenermi [iscrivendoti al mio Patreon](https://www.patreon.com/c/roccosicilia).

[![](https://roccosicilia.com/wp-content/uploads/2025/04/screenshot-2025-04-20-at-23.52.38.png?w=1024)](https://www.patreon.com/c/roccosicilia)

Sessione live archiviata su Patreon.

---

Ho scelto di usare una VM con sistema operativo Ubuntu Linux 24.04 per le solite questione di praticità. Il processo di installazione e configurazione di base è abbastanza semplice, ho seguito la [documentazione ufficiale disponibile qui](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-from-archive-on-linux-macos) dove è ben spiegato come installare Elasticsearch e Kibana. Partendo praticamente da zero (VM installata e aggiornata) ci ho messo circa un’ora tra installazione dei pacchetti e conf. di base per avviare l’istanza.

Post-live (quindi non presente nella registrazione) ho predisposto una delle mie macchine di laboratorio per inviare i logs all’istanza Elastic. Ho scelto il Domain Controller di test visto che ho intenzione di usare la stessa infrastruttura per gli esperimenti di evasione e bypass degli EDR.

Seguiranno i dettagli sul lab sia sul blog che nelle prossime live.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2025/04/30/live-del-18-04-2025-lab-siem/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: MISP: studio ed integrazione](https://roccosicilia.com/2025/04/19/misp-studio-ed-integrazione/)

[Successivo: Preparazione del prossimo talk: SOC e SIEM](https://roccosicilia.com/2025/05/19/preparazione-del-prossimo-talk-soc-e-siem/)→

Ciao,

### sono Rocco

![](https://sheliakblog.wordpress.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio sito personale dove condivido idee, riflessioni ed esperienze su hacking e sicurezza informatica.

### Let’s connect

* [Patreon](https://patreon.com/roccosicilia)

* [YouTube](https://youtube.com/%40roccosicilia)

* [LinkedIn](https://www.linkedin.com/in/roccosicilia/)

### Rimani aggiornato!

Iscriviti per ricevere gli update dei nuovi post e video.

Digita la tua e-mail…

→

### Recent posts

* [![Info Sec Unplugged [1b] – DR e Cyber recovery (parte 2)](https://roccosicilia.com/wp-content/uploads/2025/01/vlog.png?w=600)](https://roccosicilia.com/2025/10/04/info-sec-unplugged-1b-dr-e-cyber-recovery-parte-2/)

  ## [Info Sec Unplugged [1b] – DR e Cyber recovery (parte 2)](https://roccosicilia.com/2025/10/04/info-sec-unplugged-1b-dr-e-cyber-recovery-parte-2/)
* [![Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1/)

  ## [Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1/)
* [![Live del 05.09.2025: http_c2](https://roccosicilia.com/wp-content/uploads/2025/08/youtube-live.png?w=1024)](https://roccosicilia.com/2025/09/09/live-del-05-09-2025-http_c2/)

  ## [Live del 05.09.2025: http\_c2](https://roccosicilia.com/2025/09/09/live-del-05-09-2025-http_c2/)
* [![Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)

  ## [Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)
* [![Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/wp-content/uploads/2025/01/coding.png?w=562)](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)

  ## [Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)
* [![100 video](https://roccosicilia.com/wp-content/uploads/2025/08/youtube-live.png?w=1024)](https://roccosicilia.com/2025/08/28/100-video/)

  ## [100 video](https://roccosicilia.com/2025/08/28/100-video/)

# [Rocco Sicilia](https://roccosicilia.com)

* Mail
* [Patreon](https://patreon.com/roccosicilia)
* [YouTube](https://youtube.com/%40roccosicilia)
* [LinkedIn](https://www.linkedin.com/in/roccosicilia/)
* [GitHub](https://github.com/roccosicilia)
* [Telegram](https://t.me/%2Ba7sF3JQV4bMzY2Nk)
* [Link](https://discord.gg/Ys5AAbsyyH)

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[Inizia con un blog su WordPress.com](https://wordpress.com/?ref=footer_custom_blog).

##

##

Caricamento commenti...

Scrivi un Commento...

E-mail (Obbligatorio)

Nome (Obbligatorio)

Sito web

###

* [Commenta](https://roccosicilia.com/2025/04/30/live-del-18-04-2025-lab-siem/#respond)
* Abbonati
  Abbonato

  + [![](https://...