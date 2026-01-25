---
title: Nuovo sito, stesso MuHack
url: https://muhack.org/news/nuovo-sito-stesso-muhack/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-24
fetch_date: 2026-01-25T03:56:27.469447
---

# Nuovo sito, stesso MuHack

[![MuHack Logo](https://raw.githubusercontent.com/muhack/muhack_svg/refs/heads/master/loghi/logo.svg)

MUHACK](/)

[Home](/)
[About](/about/)
[Blog](/blog/)
[Wiki](https://wiki.muhack.org/)
[Status](https://status.muhack.org/)

×
[Home](/)
[About](/about/)
[Blog](/blog/)
[Wiki](https://wiki.muhack.org/)
[Status](https://status.muhack.org/)

×

Premi `ESC` per chiudere

[Home](/)
/
[Blog](/blog/)
/
Nuovo sito, stesso MuHack

News
22 January 2026
1 min

# NUOVO SITO, STESSO MUHACK

AGAIN(!?)

P

p3sc1
MuHack Member

È arrivato quel periodo dell’anno in cui, inevitabilmente, torna fuori l’idea di riscrivere il sito di MuHack.
Questa volta però, diciamolo, **ci stava**: il design precedente era vecchio, fragile e sempre meno rappresentativo di quello che MuHack è oggi.

## Cosa c’è di nuovo

Il layout è stato **riscritto da zero**. Nuova identità visiva, struttura più pulita e meno roba “messa lì che poi vediamo”.

Qualche highlight:

* **Dark mode** — Si adatta alle preferenze di sistema oppure si può forzare manualmente. In dark mode gli accenti si invertono, perché sì.
* **Search** — `Ctrl+K` (o `Cmd+K` su Mac) apre una ricerca globale. Cerca per titolo, contenuto, autore e categoria. Funziona.
* **Terminale interattivo** — La home ha un terminale funzionante. Digita `help` per i comandi disponibili. Sì, c’è anche `cowsay`. No, non lo toglieremo.
* **Performance** — CSS snellito, immagini lazy-loaded, animazioni canvas che si fermano quando il tab va in background. @Ceres ringrazia, la batteria pure.

## Le parti noiose (ma importanti)

Stack invariato, perché se funziona non si butta: **Jekyll su GitHub Pages**. Niente framework JavaScript, niente build step esoterici. Solo HTML, CSS e vanilla JS.

Il CSS usa **variabili semantiche** che si ribaltano automaticamente tra light e dark mode, quindi meno duplicazioni e meno casini futuri.

```
:root {
  --accent: var(--red);
  --accent-alt: var(--cyan);
}
[data-theme="dark"] {
  --accent: var(--cyan);
  --accent-alt: var(--red);
}
```

La search è basata su **lunr.js**, tutta client-side. Zero chiamate a server esterni, zero tracking.

## Cosa manca ancora

Alcune parti verranno rifinite o aggiunte col tempo, man mano che nasce l’esigenza.
Per il resto, MuHack vive altrove: nei progetti, nelle discussioni e nei cavi che spariscono misteriosamente.

## Bug e feedback

Se trovi qualcosa che non va, rompici le scatole. Il codice è su [GitHub](https://github.com/muhack/muhack.github.io), le issue sono aperte e accettiamo segnalazioni, patch e rant ben argomentati.

---

*Il redesign è stato un lavoro collaborativo tra umani, caffeina e qualche `div` particolarmente testardo gentilmente consegnato all’oblio.*

[Precedente

Street Party 2k25](/events/street-party-2k25/)

## POST CORRELATI

[News
27 May 2025

### SoS - State of the Space 2025,5

Hello, it’s about time we give you an update on what we’ve been up to in the
...](/news/SoS-2025-5/)
[News
24 Mar 2025

### International Open Hackerspace Day 2025 @ MuHack

Ciao a tutti, sabato 29 marzo 2025 si tiene l’International Open Hackerspace ...](/news/open-hackerspace-2025/)
[News
17 Dec 2024

### SoS - State of the Space 2024

Hi everyone, ceres-c here, the newly elected president of MuHack. I’m here to...](/news/SoS-2024/)

© 2026 MuHack — Brescia

[Facebook](https://www.facebook.com/muhackIT)
[Twitter](https://twitter.com/muhackIT)
[Instagram](https://www.instagram.com/hackerspace_muhack)
[YouTube](https://youtube.com/%40MuHack)
[GitHub](https://github.com/muhack)
[Telegram](https://t.me/muhack)
[RSS](/feed.xml)

[sede.muhack.org](https://status.muhack.org/)