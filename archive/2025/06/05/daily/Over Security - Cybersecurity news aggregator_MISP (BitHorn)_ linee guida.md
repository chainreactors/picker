---
title: MISP (BitHorn): linee guida
url: https://roccosicilia.com/2025/06/04/misp-bithorn-linee-guida/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-05
fetch_date: 2025-10-06T22:54:04.991494
---

# MISP (BitHorn): linee guida

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [MISP (BitHorn): linee guida](https://roccosicilia.com/2025/06/04/misp-bithorn-linee-guida/)

Published by

Rocco Sicilia

on

[4 giugno 2025](https://roccosicilia.com/2025/06/04/misp-bithorn-linee-guida/)

[![MISP (BitHorn): linee guida](https://roccosicilia.com/wp-content/uploads/2025/06/screenshot-2025-06-04-at-22.26.20.png?w=1024)](https://roccosicilia.com/2025/06/04/misp-bithorn-linee-guida/)

In questi giorni sto ragionando sulle linee guida da proporre alla community, nel senso “MISPoso” del termine, per inserire nuovi eventi all’interno dell’istanza che gestisco/gestiamo: <https://misp.bithorn.org>.

## Concetto di *evento*

Chi fa ricerca in ambito Threat Intelligence o lavora in contesti di difesa avrà probabilmente più occasioni per creare un evento. Il concetto di base prevede la registrazione delle informazioni di un certo evento (es: un incidente o un report) in un “contenitore”. In questi casi il ricercatore potrà creare un evento nella piattaforma MISP con i relativi oggetti e attributi.

## Aggregati

Solitamente, come appena detto, ad uno specifico contesto corrisponde un evento: due incident == due eventi distinti, un incident ed un’analisi di un malware == due eventi distinti. Ma nel nostro progetto vorrei prevedere una eccezione.

Aggregare attributi in un singolo evento MISP è accettabile se hanno senso insieme: possiamo quindi mettere più indicatori (IP, domini, hash, ecc.) nello stesso evento se fanno parte dello stesso incidente (come detto), della stessa campagna, **o arrivano dallo stesso report o fonte di intelligence**. Quindi l’aggregazione solo perché sono tutti IP non è una buona idea, ma se si stanno analizzando tutti gli IP usati da Shodan.io per eseguire le scansioni allora ha senso creare un evento unico.

## Sighting / Segnalazione

La gestione di questo parametro degli attributi/artefatti è ciò che ha fatto nascere il progetto ***eg0n*** ora esteso ad una integrazione con MISP. Purtroppo anche MISP su questo tema ha delle rigidità a livello di integrazione. Ad ogni modo per la community è fondamentale anche poter ricevere dei feedback sulla presenza di specifici IoCs all’interno delle reti o dei sistemi di chi ha attivato un processo di hunting all’interno del proprio team.

È fondamentale che la segnalazione non sia “a sentimento”: decidere di confermare un IoC significa averlo osservato sui propri logs/sistemi di detection. Sull’attribuzione delle segnalazioni definiremo un processo di verifica/qualifica, ma resta una parametro “della community”.

## Prossimamente ne parliamo …

![](https://roccosicilia.com/wp-content/uploads/2025/06/image.png?w=449)

Ho aperto un sondaggio sul [server Discord](https://discord.com/channels/980421363078664222/980421363078664225/1379490553498046586) per trovare una data comoda alla maggior parte degli interessati al progetto ed organizzare un piccolo virtual-meeting per discutere delle linee guida e del progetto.

L’occasione è anche perfetta per fare una piccola panoramica della struttura sino ad ora attivata e dei task che stiamo ipotizzando di mettere in roadmap. Il sondaggio **resta aperto fino alla sera dell’08.06.2025**.

Al momento è disponibile la repo dedicata al progetto in cui raccoglieremo documentazione, scripts, integrazioni e tutto quello che la community produrrà: <https://github.com/b1th0rn/bh-misp>.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/06/04/misp-bithorn-linee-guida/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/06/04/misp-bithorn-linee-guida/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/06/04/misp-bithorn-linee-guida/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2025/06/04/misp-bithorn-linee-guida/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Info Sec Unplugged [16] – Threat Int. (1a parte)](https://roccosicilia.com/2025/06/03/info-sec-unplugged-16-threat-int-1a-parte/)

[Successivo: CVE-2024-4577: analisi di un payload](https://roccosicilia.com/2025/06/11/cve-2024-4577-analisi-di-un-payload/)→

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
* [English ve...