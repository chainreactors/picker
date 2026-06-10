---
title: I comandi Linux arrivano su Windows Microsoft integra le CoreUtils nel proprio OS
url: http://www.zeusnews.it/n.php?c=32136
source: Instapaper: Unread
date: 2026-06-09
fetch_date: 2026-06-10T06:17:24.608013
---

# I comandi Linux arrivano su Windows Microsoft integra le CoreUtils nel proprio OS

![](https://b.scorecardresearch.com/p?c1=2&c2=13879765&cv=2.0&cj=1)

[![Zeus News](/pic/logo.gif)](/)

[Salta il menu](#contenuto)

* [Home](http://www.zeusnews.it)
* [Editoriale](index.php3?ar=sezioni&numero=949)
* [Recensioni](index.php3?ar=sezioni&numero=912)
* [Focus](index.php3?ar=sezioni&numero=913)
* [Sicurezza](index.php3?ar=sezioni&numero=901)
* [Trucchi](index.php3?ar=sezioni&numero=906)
* [Maipiusenza](index.php3?ar=sezioni&numero=903)
* [Segnalazioni](index.php3?ar=sezioni&numero=905)
* [Sondaggi](index.php3?ar=sezioni&numero=902)
* [Antibufala](index.php3?ar=sezioni&numero=904)
* [Download](index.php3?ar=sezioni&numero=916)
* [News](index.php3?ar=sezioni&numero=907)
* [Flash](index.php3?ar=sezioni&numero=914)
* [Pag2](index.php3?ar=sezioni&numero=915)

[![Newsletter](pic/pulsanti/newsletter.png "Newsletter")](http://newsletter.zeusnews.it/index.php?p=subscribe&id=5)
[![RSS](pic/pulsanti/rss.png "Feed RSS")](http://feeds.feedburner.com/ZeusNews)
[![Facebook](pic/pulsanti/facebook.png "Zeus News su Facebook")](http://www.facebook.com/ZeusNews)
[![Forum Olimpo Informatico](pic/pulsanti/forum.png "Forum Olimpo Informatico")](http://forum.zeusnews.com/index.php?c=1)
[![Contatti](pic/pulsanti/contatti.png "Contatti")](http://www.zeusnews.it/index.php3?ar=staff)
[![Accadde oggi](pic/pulsanti/calendar3.png "Accadde oggi")](http://www.zeusnews.it/index.php3?ar=accaddeoggi)
[![Ricerca](pic/pulsanti/ricerca.png "Cerca in Zeus News")](http://www.zeusnews.it/index.php3?ar=ricerca)

[Newsletter](http://newsletter.zeusnews.it/index.php?p=subscribe&id=5)
[Feed RSS](http://feeds.feedburner.com/ZeusNews)
[Facebook](http://www.facebook.com/ZeusNews)
[Forum](http://forum.zeusnews.com/index.php?c=1)
[Contatti](http://www.zeusnews.it/index.php3?ar=staff)
[Accadde oggi](http://www.zeusnews.it/index.php3?ar=accaddeoggi)
[Cerca](http://www.zeusnews.it/index.php3?ar=ricerca)

# I comandi Linux arrivano su Windows: Microsoft integra le CoreUtils nel proprio OS

Ls, cp, mv, grep, find e molti altri comandi ancora ora sono disponibili in Windows.

[Tweet](https://twitter.com/share)

[*ZEUS News* - [www.zeusnews.it](https://www.zeusnews.it/) - 07-06-2026] Commenti (3)

![linux coreutils in windows](https://www.zeusnews.it/img/6/3/1/2/3/0/032136-620-linux-coreutils-in-windows.jpg)

Foto di [Fotis Fotopoulos](https://unsplash.com/it/%40ffstop).

Microsoft ha rilasciato [Coreutils per Windows](/link/47765 "https://learn.microsoft.com/en-us/windows/core-utils/overview"), introducendo per la prima volta un set nativo di comandi Linux direttamente all'interno del proprio sistema operativo. L'annuncio, presentato durante l'evento Build 2026, segna un cambiamento interessante con l'obiettivo di ridurre le differenze operative tra ambienti Linux, macOS, WSL e Windows stesso. Il pacchetto si basa sul progetto open‑source [uutils](/link/47766 "https://uutils.github.io"), una reimplementazione multipiattaforma delle [GNU Core Utilities](/link/47767 "https://it.wikipedia.org/wiki/GNU_Core_Utilities") scritta in [Rust](util/extlink/cerca_amazon.php?q=Rust "Cerca Rust su Amazon"). Microsoft ha integrato queste utilità in un unico eseguibile, coreutils.exe, dal quale vengono generati [hardlink NTFS](/link/47768 "https://it.wikipedia.org/wiki/Collegamento_fisico") che espongono i comandi con i nomi tradizionali come *ls, cp, mv, rm, cat, grep e find*. Questo approccio consente di mantenere un solo file binario da aggiornare, firmare e distribuire, semplificando la manutenzione e garantendo coerenza tra le varie utility.

Microsoft ha spiegato che l'obiettivo è ridurre il *«il carico cognitivo degli sviluppatori»* che si spostano tra sistemi operativi diversi: *«Gli sviluppatori si muovono costantemente tra piattaforme, ma i comandi familiari non funzionano in modo coerente, costringendo a continui cambi di contesto»*. La disponibilità nativa dei comandi Linux elimina la necessità di ricorrere a emulatori, shell alternative o terminali virtualizzati basati su WSL. Coreutils per Windows supporta oltre 75 comandi, tra cui strumenti essenziali per scripting, automazione e manipolazione dei file. Alcuni comandi non sono inclusi a causa di conflitti con le utility già presenti in CMD o PowerShell, come *dir*, *more*, *whoami* e *timeout*. Altri non sono disponibili perché richiedono funzionalità POSIX non implementate in Windows, come *chmod*, *chown*, *chroot* e *nohup*. Microsoft ha pubblicato una tabella di compatibilità che indica quali comandi funzionano nei diversi ambienti shell.

L'installazione avviene tramite WinGet con un singolo comando - *winget install Microsoft.Coreutils* e rende immediatamente disponibili le utility in CMD, [PowerShell](util/extlink/cerca_amazon.php?q=PowerShell "Cerca PowerShell su Amazon") e Windows Terminal. Microsoft ha sottolineato che l'iniziativa risponde alle richieste della comunità di sviluppo, che da anni chiede una maggiore compatibilità tra Windows e gli strumenti Unix. Ha dichiarato che *«i comandi e i flussi di lavoro costruiti nel corso degli anni funzionano ora anche in ambiente Windows»*: una frase che, tradotta, evidenzia l'intenzione di ridurre le barriere tra ecosistemi.

Il pacchetto Coreutils è disponibile come progetto open source su GitHub; Microsoft, che mantiene la build specifica per Windows, ha indicato che continuerà a migliorare la compatibilità e ad ampliare il set di comandi supportati, pur riconoscendo i limiti strutturali derivanti dalle differenze tra Windows e i sistemi [POSIX](util/extlink/cerca_amazon.php?q=POSIX "Cerca POSIX su Amazon").

Articoli suggeriti:

[![](/img/5/3/9/1/3/0/031935-620-windows-11-interventi-stabilita.jpg)](/zn/31935)

[Meno caos e più stabilità: in arrivo una serie di interventi struttura...](/zn/31935 "Meno caos e più stabilità: in arrivo una serie di interventi strutturali per Windows 11")

[![](/img/5/1/7/1/3/0/031715-620-windows-11-update-2026-errori.jpg)](/zn/31715)

[Windows 11, il primo aggiornamento del 2026 causa errori e instabilità](/zn/31715 "Windows 11, il primo aggiornamento del 2026 causa errori e instabilità")

[![](/img/1/2/1/1/3/0/031121-620-gates-torvalds.jpeg)](/zn/31121)

[Da rivali a commensali: Bill Gates e Linus Torvalds si incontrano a cena per la ...](/zn/31121 "Da rivali a commensali: Bill Gates e Linus Torvalds si incontrano a cena per la prima volta")

[![](/img/7/9/5/9/2/0/029597-620-wsl-general-availability.jpg)](/zn/29597)

[Ora tutti possono far girare le app per Linux sotto Windows](/zn/29597 "Ora tutti possono far girare le app per Linux sotto Windows")

|  |  |
| --- | --- |
| Se questo articolo ti è piaciuto e vuoi rimanere sempre informato con Zeus News  ti consigliamo di [**iscriverti alla Newsletter gratuita**](http://newsletter.zeusnews.it/index.php?p=subscribe&id=5). Inoltre puoi consigliare l'articolo utilizzando uno dei pulsanti qui sotto, inserire un [**commento**](http://forum.zeusnews.com/posting.php?mode=reply&t=81198) (anche **[anonimo](/n.php?c=32136#commenti "Commenta")**) o segnalare un [**refuso**](http://www.zeusnews.it/index.php3?ar=mailtoreda&ar2=refuso&cod=32136).   © RIPRODUZIONE RISERVATA |  |

|  |  |
| --- | --- |
| |  | | --- | |  | |

[Tweet](https://twitter.com/share)

Approfondimenti

[Windows adesso supporta le app per Linux distribuite via Snap](n.php?c=29501)

# [Commenti all'articolo (3)](http://forum.zeusnews.com/viewtopic.php?t=81198)

[![](https://www.zeusnews.it/avatar/13730885844cffa32e00514.jpg)](http://forum.zeusnews.com/search.php?search_author=Gladiator)
[Gladiator](http://forum.zeusnews.com/search.php?search_author=Gladiator)

Ultimamente le strategie di M$ mi sembrano sempre piÃ¹ ondivage, direi che danno sempre piÃ¹ adito a pensare che non sappiano bene in che direzione andare per il futuro, comunicare che il prossimo SO non sarÃ  un SO tradizionale ma un SO agentico e, una settimana dopo, rilasciare queste CoreUtils mi sbrano due cose completamente agli... [Leggi tutto](http://forum.zeusnews.com/viewtopic.php?p=7...