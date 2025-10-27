---
title: Vi ricordate di Spectre/MeltDown?
url: https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-04
fetch_date: 2025-10-06T18:53:12.307143
---

# Vi ricordate di Spectre/MeltDown?

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/)

## [Vi ricordate di Spectre/MeltDown?](https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/)

Published by

Rocco Sicilia

on

[3 ottobre 2024](https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/)

[![Vi ricordate di Spectre/MeltDown?](https://roccosicilia.com/wp-content/uploads/2024/10/spectre.png?w=545)](https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/)

Un argomento a dir poco glorioso per chi si ricorda di quei giorni nel 2018 (è passata una vita). Fa un po’ sorridere parlarne a ottobre 2024, ma evidentemente la ferita è ancora aperta.

Perché ne parlo? Ciclicamente questa vulnerabilità mi si presenta d’avanti e la domanda che gli interessati mi fanno è sempre la stessa: **avendo aggiornato gli hypervisor** (ormai è raro trovare server con O.S. Microsoft installato BareMetal) **devo preoccuparmi di eseguire il fix anche sulle Virtual Machine?** Risposta breve: **sì**. Due cenni sul perché e come.

## Perché?

Per chi è del settore invito alla lettura dei relativi paper che potete trovare qui: <https://meltdownattack.com/>. In questa occasione mi permetterete di iper-semplificare il tema per renderlo digeribile anche a chi non ha nozioni di architettura dei moderni processori. Il punto a cui prestare attenzione è che la vulnerabilità, oltre ad avere diverse varianti, si applica a diversi scenari, tra i quali esiste lo scenario che vede come target una Virtual Machine non fixed.

Microsoft ci regala questo documento in cui sono riassunti gli scenari relativi alla variante 4 (CVE-2018-3639): <https://msrc.microsoft.com/blog/2018/05/analysis-and-mitigation-of-speculative-store-bypass-cve-2018-3639/>. Per quanti mi riguarda è stato il documento che più mi ha aiutato a capire se, nei diversi contesti in cui ho lavorato, era opportuno procedere con l’applicazione delle fix/mitigation o meno.

## Come?

Qui viene il bello perché la mitigation é applicabile semplicemente creando due chiavi di registro il cui valore varia a seconda di diversi parametri tra cui l’architettura CPU e la variante su cui vogliamo operare. Come accennavo la variante che probabilmente molti si trovano a dover – ancora – gestire è la v4 la cui mitigation è spiegata nell’ultimo link.

Per i super pigri lascio il link ad uno script che vi consente di eseguire la mitigation se le chiavi non sono ancora presenti sul sistema target. Da considerare che è necessario il reboot della macchina una volta applicata la fix: <https://github.com/roccosicilia/VulnerabilityReview/blob/main/CVE-2018-3639/review.md>

![](https://roccosicilia.com/wp-content/uploads/2024/10/cve-2018-3639-screenshot-01.png?w=1024)

\_\_\_\_\_\_\_\_\_\_

Se ti interessano i miei articoli ad i miei video di approfondimento puoi sostenere il progetto tramite la community [patreon](https://patreon.com/roccosicilia). Per ricevere gli update puoi registrarti al blog:

Digita la tua e-mail…

Iscriviti

\_\_\_\_\_\_\_\_\_\_

## Minacce correlate

Una nota importante che dovrebbe contribuire a far comprendere la pericolosità di questa vulnerabilità: sono documentati diversi PoC della vulnerabilità discussa, non ci sono ragioni valide per non eseguire il fix.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2024/10/03/vi-ricordate-di-spectre-meltdown/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: “Da dove inizio?”](https://roccosicilia.com/2024/08/24/da-dove-inizio/)

[Successivo: Vulnerabilità e Attack Path](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/)→

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

* [Comment...