---
title: Fuji 1.2.0 permette l’acquisizione forense dei Mac anche in recovery mode
url: https://andrealazzarotto.com/2026/02/28/fuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode/
source: Instapaper: Unread
date: 2026-03-02
fetch_date: 2026-03-03T04:13:51.393606
---

# Fuji 1.2.0 permette l’acquisizione forense dei Mac anche in recovery mode

[Vai al contenuto](#content)

[Andrea Lazzarotto](https://andrealazzarotto.com/)

Informatica forense, sviluppo software e consulenza

[ ]

Menu +
×
esteso
chiuso

* [Home](https://andrealazzarotto.com/)
* [Chi sono](https://andrealazzarotto.com/about/)
* [Informatica forense](https://andrealazzarotto.com/informatica-forense/)
* [Servizi](https://andrealazzarotto.com/servizi/)
* [Blog](https://andrealazzarotto.com/blog/)
* [Contatti](https://andrealazzarotto.com/contatti/)

* [Facebook](https://www.facebook.com/AndreaLazzarottoSoftware/)
* [Twitter](https://twitter.com/TheLazza/)
* [Mastodon](https://mastodon.social/%40lazza)
* [LinkedIn](https://www.linkedin.com/in/andrealazzarotto/)
* [GitHub](https://github.com/Lazza/)
* [YouTube](https://www.youtube.com/c/AndreaLazzarotto)

# Fuji 1.2.0 permette l’acquisizione forense dei Mac anche in recovery mode

Pubblicato da[Lazza](https://andrealazzarotto.com/author/lazza/)[28 Febbraio 202628 Febbraio 2026](https://andrealazzarotto.com/2026/02/28/fuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode/)Pubblicato in: [Digital forensics](https://andrealazzarotto.com/category/digital-forensics/)Tag:[apple](https://andrealazzarotto.com/tag/apple/), [Fuji](https://andrealazzarotto.com/tag/fuji/), [mac](https://andrealazzarotto.com/tag/mac/), [programmi](https://andrealazzarotto.com/tag/programmi/), [software](https://andrealazzarotto.com/tag/software/), [software libero](https://andrealazzarotto.com/tag/software-libero/)

![Illustrazione che mostra l'icona di una Fuji Cartridge a forma di cartuccia di videogioco, con l'etichetta che raffigura il logo di Fuji, cioè l'omonimo monte al tramonto con il sole che è anche una succosa mela. Lo sfondo scuro mostra in leggera sovraimpressione la scritta "FUJI" a caratteri cubitali.](https://andrealazzarotto.com/wp-content/uploads/2026/02/fuji-1.2.0-1568x784.jpg)

L’inizio del 2026 è stato un periodo di forte sviluppo per Fuji, il mio **programma open-source per l’acquisizione forense di macOS.**

Dopo alcuni mesi di poca attività, ho ricominciato un intenso lavoro per includere nuove funzioni, correzioni di bug e miglioramenti generali. Sono davvero soddisfatto del risultato ottenuto e i [vari](https://www.linkedin.com/posts/activity-7428669232894078977-1c-o) [commenti](https://www.linkedin.com/posts/activity-7429901741845794816-kau8) [ricevuti](https://www.linkedin.com/posts/luca-cadonici-41299b4b_fuji-macos-dfir-activity-7429867149134962688-cHdc), anche da [esponenti](https://www.linkedin.com/posts/m%C3%A9ven-l%C3%A9austic-744206264_macos-forensics-digitalforensics-activity-7428755544758325248-oCNZ) delle [forze dell’ordine](https://www.linkedin.com/posts/emarlierealbrecht_macos-forensics-digitalforensics-activity-7428738449555423234-MF4m) di diversi paesi, sembrano condividere l’entusiasmo.

La novità più interessante della nuova versione di Fuji è **la possibilità di avviare il programma tramite la *recovery mode,*** e questo funziona sia con i Mac di tipo Intel che Apple Silicon.

Qualora il dispositivo non abbia la funzionalità FileVault attiva, ciò rende possibile effettuare la copia forense del Mac senza conoscere la password dell’utilizzatore.

Viene introdotto il concetto di **Fuji Cartridge,** cioè un dispositivo USB che si può usare per far partire Fuji in questa modalità. Una caratteristica innovativa è che il dispositivo può essere disconnesso non appena il programma è partito, in quanto Fuji si auto-replica in un *RAM disk* e rende di nuovo disponibile la porta USB.

L’analista forense può [creare una Fuji Cartridge](https://fujiapp.top/docs/drive-preparation/) con qualunque computer, indipendentemente dal sistema operativo utilizzato, anche riciclando una vecchia chiavetta di scarsa capacità. La metafora della cartuccia è piaciuta a molti e ha ispirato qualche idea piuttosto originale.

> Exploring [@thelazza](https://twitter.com/thelazza?ref_src=twsrc%5Etfw)’s new release of Fuji for Mac acquisitions sparked a fun take on making a “Fuji Cartridge” necessary for it to replicate to RAM-disk in recovery mode.<https://t.co/u7aJyy1k7Y> [pic.twitter.com/x3M9ujONKN](https://t.co/x3M9ujONKN)
>
> — derek eiri 👻 (@MrEerie) [27 Febbraio 2026](https://twitter.com/MrEerie/status/2027523373589532824?ref_src=twsrc%5Etfw)

L’esperto di analisi forense Derek Eiri ha pubblicato le foto di un dispositivo USB artigianalmente inserito nel guscio di una vera cartuccia. Il risultato è ragguardevole!

![](https://andrealazzarotto.com/wp-content/uploads/2026/02/derek-eiri-fuji-cartridge-1024x768.jpg)

Fuji Cartridge realizzata da Derek Eiri

Fuji 1.2.0 include anche altre migliorie:

* **Nuovo metodo di acquisizione Ditto,** necessario in *recovery mode* dove Rsync non si può utilizzare
* **Pulizia dei file temporanei,** a volte fonte di confusione
* **Selezione automatica del volume dati,** dove risiedono tutti i file dell’utente
* **Raccolta degli *Unified Logs*** molto più completa di prima
* **Produzione di un file ZIP** per l’acquisizione con metodo Sysdiagnose e conversione dei dati in JSONL invece di SQLite
* **Nuovo formato del DMG di Fuji,** masterizzabile con balenaEtcher

Infine, con l’occasione è stato pubblicato un nuovo sito web dedicato alla documentazione del programma. Qui sotto riporto i link del progetto:

[Note di rilascio](https://github.com/Lazza/Fuji/releases/tag/1.2.0)

[Documentazione](https://fujiapp.top)

[Donazioni](https://ko-fi.com/thelazza)

Fuji sta riscuotendo un discreto successo sia tra i consulenti tecnici che tra le forze dell’ordine e mi piacerebbe che tutti potessero provarlo. Se trovate interessante il progetto, vi esorto a diffonderlo tra i vostri colleghi. 😉

### Condividi:

Share on Email[Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fandrealazzarotto.com%2F2026%2F02%2F28%2Ffuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode%2F)[Share on X (Twitter)](https://twitter.com/intent/tweet?text=Fuji%201.2.0%20permette%20l%E2%80%99acquisizione%20forense%20dei%20Mac%20anche%20in%20recovery%20mode&url=https%3A%2F%2Fandrealazzarotto.com%2F2026%2F02%2F28%2Ffuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode%2F&via=thelazza&related=thelazza) [Share on Mastodon](https://toot.kytta.dev/?text=Fuji%201.2.0%20permette%20l%E2%80%99acquisizione%20forense%20dei%20Mac%20anche%20in%20recovery%20mode%20%E2%80%94%20https%3A%2F%2Fandrealazzarotto.com%2F2026%2F02%2F28%2Ffuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode%2F)[Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=1&url=https%3A%2F%2Fandrealazzarotto.com%2F2026%2F02%2F28%2Ffuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode%2F&title=Fuji%201.2.0%20permette%20l%E2%80%99acquisizione%20forense%20dei%20Mac%20anche%20in%20recovery%20mode&source=https%3A%2F%2Fandrealazzarotto.com)[Share on Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fandrealazzarotto.com%2F2026%2F02%2F28%2Ffuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode%2F&text=Fuji%201.2.0%20permette%20l%E2%80%99acquisizione%20forense%20dei%20Mac%20anche%20in%20recovery%20mode)[Share on WhatsApp](https://api.whatsapp.com/send?text=Fuji%201.2.0%20permette%20l%E2%80%99acquisizione%20forense%20dei%20Mac%20anche%20in%20recovery%20mode%20%E2%80%94%20https%3A%2F%2Fandrealazzarotto.com%2F2026%2F02%2F28%2Ffuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode%2F)[Share on Pocket](https://getpocket.com/save?url=https%3A%2F%2Fandrealazzarotto.com%2F2026%2F02%2F28%2Ffuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode%2F&title=Fuji%201.2.0%20permette%20l%E2%80%99acquisizione%20forense%20dei%20Mac%20anche%20in%20recovery%20mode)

Pubblicato da[Lazza](https://andrealazzarotto.com/author/lazza/)[28 Febbraio 202628 Febbraio 2026](https://andrealazzarotto.com/2026/02/28/fuji-1-2-0-permette-lacquisizione-forense-dei-mac-anche-in-recovery-mode/)Pubblicato in...