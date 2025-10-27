---
title: Vulnerabilità e Attack Path
url: https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-11
fetch_date: 2025-10-06T18:55:14.336851
---

# Vulnerabilità e Attack Path

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/), [vlog & podcast](https://roccosicilia.com/category/vlog-podcast/)

## [Vulnerabilità e Attack Path](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/)

Published by

Rocco Sicilia

on

[10 ottobre 2024](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/)

[![Vulnerabilità e Attack Path](https://roccosicilia.com/wp-content/uploads/2024/10/attack-path.png?w=545)](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/)

Era un po’ che volevo trattare l’argomento e approfitto di quanto discusso ieri (9 ottobre) durante l’evento che [NTS Italy](https://nts.eu) ha organizzato a Verona: assieme ad Andrea abbiamo presentato alcune riflessioni a seguito di quello che abbiamo visto “su campo” nell’ultimo anno ed uno dei temi era relativo alla gestione delle vulnerabilità in contesti complessi dove solitamente il processo di Vuln. Management c’è ma se ne misuriamo le *performance* qualche dubbio ci viene.

Probabilmente i video dell’evento verranno pubblicati sul canale di NTS, eventualmente vi lascerò il link. Per ora fatevi bastare il mio approfondimento sulla questione relativa all’analisi degli Attack Path.

L’argomento è abbastanza complesso e sono ovviamente disponibile a discuterne con chi è interessato al tema. I miei riferimenti [li trovate qui](https://roccosicilia.com/about/) e se vi interessano i contenuti che porto e volete restare aggiornati potete iscrivervi al blog:

Digita la tua e-mail…

Iscriviti

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2024/10/10/vulnerabilita-e-attack-path/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Vi ricordate di Spectre/MeltDown?](https://roccosicilia.com/2024/10/03/vi-ricordate-di-spectre-meltdown/)

[Successivo: Non trascurare la raccolta delle informazioni: port scan.](https://roccosicilia.com/2024/11/09/non-trascurare-la-raccolta-delle-informazioni-port-scan/)→

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

* [Commenta](https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/#respond)
* Abbonati
  Abbonato

  + [![](https://roccosicilia.com/wp-content/uploads/2018/09/sheliak.jpg?w=50) Rocco Sicilia](https://roccosicilia.com)

  Unisciti ad altri 43 abbonati

  Registrami

  + Hai già un account WordPress.com? [Accedi ora.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Froccosicilia.com%252F2024%252F10%252F10%252Fvulnerabilita-e-attack-path%252F)
* + [![](https://roccosicilia.com/wp-content/uploads/2018/09/sheliak.jpg?w=50) Rocco Sicilia](https://roccosicilia.com)
  + Abbonati
    Abbonato
  + [Registrati](https://wordpress.com/start/)
  + [Accedi](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Froccosicilia.com%252F2024%252F10%252F10%252Fvulnerabilita-e-attack-path%252F)
  + [Copia shortlink](https://wp.me/pachgi-Mk)
  + [Segnala questo contenuto](https://wordpress.com/abuse/?report_url=https://roccosicilia.com/2024/10/10/vulnerabilita-e-attack-path/)
  + [Visualizza articolo nel Reader](https://wordpress.com/reader/blogs/150689654/posts/2996)
  + [Gestisci gli abbonamenti](https://subscribe.wordpress.com/)
  + Riduci la barra

%d

![](https://pixel.wp.com/b.gif?v=noscript)