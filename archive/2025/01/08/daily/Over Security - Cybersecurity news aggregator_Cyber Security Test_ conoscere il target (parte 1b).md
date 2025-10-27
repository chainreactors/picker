---
title: Cyber Security Test: conoscere il target (parte 1b)
url: https://roccosicilia.com/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-08
fetch_date: 2025-10-06T20:12:31.586967
---

# Cyber Security Test: conoscere il target (parte 1b)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Cyber Security Test: conoscere il target (parte 1b)](https://roccosicilia.com/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/)

Published by

Rocco Sicilia

on

[6 gennaio 2025](https://roccosicilia.com/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/)

[![Cyber Security Test: conoscere il target (parte 1b)](https://roccosicilia.com/wp-content/uploads/2025/01/cybersecurity-test-serie.png?w=595)](https://roccosicilia.com/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/)

Ho deciso di estendere la “parte 1” prima di passare oltre per fare un piccolo focus sull’analisi del sito web istituzionale del target (e dei siti che troveremo). Nelle fasi iniziali del test ogni informazione è preziosa (mi ripeto, lo so) e le fonti vanno spremute bene.

Oltre ai contenuti dei siti web possiamo analizzare ciò che siamo in grado leggere lato client: la struttura HTML, file e componenti di servizio, link, media. Andare a caccia di informazioni in siti di una certa dimensione potrebbe essere difficoltoso se non impossibile, una possibile soluzione è il download di tutte le componenti “statiche” del sito per analizzarle con calma e soprattutto con l’aiuto della CLI.

L’operazione non è esattamente “silenziosa” considerando che ogni nostra richiesta HTTP verrà registrata nei logs del webserver. Inoltre tentare di nascondere la nostra provenienza tramite una VPN o la rete Tor potrebbe peggiorare le cose: ad una eventuale analisi dei logs è molto probabile che gli exit node della rete Tor sia facilmente riconoscibili e questo potrebbe insospettire il target. Si tratta di una precauzione che ha senso solo in contesti di simulazione di attacco, modello che viene sempre più applicato ed apprezzato dalle aziende che chiedono di eseguire test di sicurezza.

Un tool utile ad una rapida analisi delle informazioni legate al dominio web ed alle tecnologie usate dall’host è netcraft. Dalla risorsa <https://sitereport.netcraft.com> è possibile eseguire una scansione di un sito ed ottenere un report relativo a diversi aspetti tecnici. Come sempre un esempio è molto più utile delle parole.

![](https://roccosicilia.com/wp-content/uploads/2025/01/image-5.png?w=1024)

Esempio da roccosicilia.com

Tra le informazioni disponibili c’è il rilevamento della tecnologia usata per le componenti server-side e client-side, viene inoltre verificato se è possibile stabilire il CMS in uso. Vengono inoltre raccolte le informazioni a livello host IP e provider.

![](https://roccosicilia.com/wp-content/uploads/2025/01/image-6.png?w=1024)

DNS query

Questi ultimi dati ci prendiamo in considerazione in modo dettagliato nel prossimo post, in concetto di base è analizzare il sito web in ogni sua parte in modo da avere una completa panoramica di quanto esposto da questa singola applicazione.

---

La serie di post e [video](https://www.patreon.com/c/roccosicilia/posts?filters%5Btag%5D=cyber+security+test) sui security test prenderà in esame diversi aspetti legati al mondo del Penetration Testing. Per rimanere aggiornato sui prossimi post puoi iscriverti al blog:

Digita la tua e-mail…

Iscriviti

---

Nel prossimo post terminiamo la parte di raccolta informazioni passiva con l’obiettivo, già dichiarato, di ottenere un elenco di hosts che si possono riferire al nostro target.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2025/01/06/cyber-security-test-conoscere-il-target-parte-1b/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Twitch Live 03.01.2025](https://roccosicilia.com/2025/01/03/twitch-live-03-01-2025/)

[Successivo: Riflessione sulle Free WiFi](https://roccosicilia.com/2025/01/20/riflessione-sulle-free-wifi/)→

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
* [English v...