---
title: HomeLab #1: ovftool
url: https://roccosicilia.com/2024/08/23/homelab-1-ovftool/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-24
fetch_date: 2025-10-06T18:06:16.581635
---

# HomeLab #1: ovftool

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [HomeLab #1: ovftool](https://roccosicilia.com/2024/08/23/homelab-1-ovftool/)

Published by

Rocco Sicilia

on

[23 agosto 2024](https://roccosicilia.com/2024/08/23/homelab-1-ovftool/)

[![HomeLab #1: ovftool](https://roccosicilia.com/wp-content/uploads/2024/08/homelab.png?w=545)](https://roccosicilia.com/2024/08/23/homelab-1-ovftool/)

Dedico una serie di post al mio HomeLab ed alle varie evoluzioni/modifiche che eseguo nel tempo. In questa serie non ci saranno riferimenti a specifiche attività in ambito cyber sec. ma mi limito a descrivere le scelte fatte a livello di lavoratorio e, ovviamente, a spiegarne le motivazioni.

Di base posso contate sul mio MacBook dove ho installato un paio di VM di servizio (una Linux e una Windows) e su cui installo buona parte dei tools che mi servono. L’ovvio limite dei moderni MacBook è il processore: in caso di esigenze x86 devo utilizzare altre piattaforme. Per questo mi sono dotato di un MiniPC (al momento molto limitato) per ambienti guest x86. Per varie ragioni al momento il MiniPC è una WinBox (mi serviva un Windows bare metal) con installato VirtualBox. Una piccola utility di cui dotarsi è, proprio per le esigenze di gestione delle guest, ovftool grazie alla quale è possibile creare archivi *ova* (open virtual appliance).

Oggi ho rimesso le mani su alcune macchine di VulnHub e buona parte di queste macchine sono rilasciate nel formato VMware, quindi con un *vmx* file che descrive la VM ed il disco nel formato *vmdk*. Convertendo la macchina in un archivio *ova* possiamo facilmente importarla in ambienti VMware e VirtualBox senza mettersi a copiare file su Datastore remoti o fare altri “accricchi”

> [Nota] Dispongo anche di un attrezzatissimo LAB messo a disposizione dalla mia company (vedi mio [profilo LinkedIn](https://www.linkedin.com/in/roccosicilia/)) con VMware vSphere e altri strumenti, utilissimo per le attività di testing e studio. Disporre di attrezzature di laboratorio adeguate è un supporto indispensabile alla crescita delle proprie abilità tecniche.

Il tool da utilizzare per questo piccolo task è ovftool che nella sua semplicità ci consente di creare il nostro *ovf/ova* file partendo appunto dal *vmx* e dal *vmdk*.

Nel contesto specifico – macchine create per far pratica di Penetration Testing – considerate che chi crea queste Virtual Machine non sempre si preoccupa di eseguire un’esportazione della macchina con condifurazioni di vHardware generiche, potrebbe capitare che la VM, una volta importata, presenti vDevice che non avete sul vostro host e questo potrebbe impedire il boot del sistema. In questo caso è sufficiente modificare la configurazione della VM a livello di vDevice.

---

In questi giorni sto pubblicando un po’ di video con delle “study session” che ho fatto in live, le rendo disponibili pubblicamente su [Patreon](https://patreon.com/roccosicilia), **basta il free access**.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2024/08/23/homelab-1-ovftool/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2024/08/23/homelab-1-ovftool/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2024/08/23/homelab-1-ovftool/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2024/08/23/homelab-1-ovftool/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Update #5](https://roccosicilia.com/2024/08/17/update-5/)

[Successivo: “Da dove inizio?”](https://roccosicilia.com/2024/08/24/da-dove-inizio/)→

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

* [Commenta](https://roccosicilia.com/2024/08/23/homelab-1-ovftool/#respond)
* Abbonati
  Abbonato

  + [![](https://roccosicilia.com/wp-content/uploads/2018/09/sheliak.jpg?w=50) Rocco Sicilia](https://roccosicilia.com)

  Unisciti ad altri 43 abbonati

  Registrami

  + Hai già un account WordPress.com? [Accedi ora.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252F...