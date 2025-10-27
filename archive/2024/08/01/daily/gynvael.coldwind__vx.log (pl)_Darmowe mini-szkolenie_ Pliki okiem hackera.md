---
title: Darmowe mini-szkolenie: Pliki okiem hackera
url: https://gynvael.coldwind.pl/?id=790
source: gynvael.coldwind//vx.log (pl)
date: 2024-08-01
fetch_date: 2025-10-06T18:02:57.580822
---

# Darmowe mini-szkolenie: Pliki okiem hackera

# [![gynvael.coldwin//vx.log](/img/logo.gif)](/?blog=1)

![](/images/something_suspicious.png)

[Available for Consulting and Projects](https://hexarcana.ch/?utm=gyn-blog)
[hackArcana (edu+CTF)](https://hackarcana.com/?utm=gyn-blog-w)

![](/img/gynvael-close.jpg)

* [Return to dashboard ⇪](/)

### *Sections*

* **lang**: [![PL](/images/lang_pl.png)](?blog=1&lang=pl) | [![EN](/images/lang_en.png)](?blog=1&lang=en)
* **RSS**: [![RSS PL](/images/lang_pl.png)](/rss_pl.php) | [![RSS EN](/images/lang_en.png)](/rss_en.php)
* [About me](?id=50)
* [Tools](?id=182)
* [→ YT YouTube (EN)](https://youtube.com/c/GynvaelEN)
* [→ D Discord](/discord)* [→ M Mastodon](https://infosec.exchange/%40gynvael)* [→ T Twitter](https://twitter.com/gynvael)* [→ GH GitHub](https://github.com/gynvael)

        [![](/img/hA-logo.png)](https://hackarcana.com)

        [My edu+CTF site](https://hackarcana.com)

        [![](/img/hexarcana160_2.png)](https://hexarcana.ch)

        [My consulting company](https://hexarcana.ch)

        [![](/img/po_issue_5_rbanner.png)](https://pagedout.institute/)

        [Paged Out! zine](https://pagedout.institute/)

        [![](/img/ds_logo_160.jpg)](https://dragonsector.pl/)

        [Dragon Sector CTF Team](https://dragonsector.pl/)

### *Links / Blogs*

* **Security/Hacking:**
  + [j00ru's blog](https://j00ru.vexillium.org/)
  + [lcamtuf's thing](https://lcamtuf.substack.com/)
  + [pi3's blog](http://blog.pi3.com.pl/)
  + [tavis ormandy's site](https://lock.cmpxchg8b.com/)
  + [pawel golen's blog](http://wampir.mroczna-zaloga.org/)
  + [zaufana trzecia strona](http://zaufanatrzeciastrona.pl/)
  + [niebezpiecznik](https://niebezpiecznik.pl/)
  + [sekurak](https://sekurak.pl/)
* **Reverse Eng./Low-Level:**
  + [security news](https://www.secnews.pl/)
  + [rev3rsed](http://rev3rsed.blogspot.com/)
* **Programming/Code:**
  + [adam sawicki](http://asawicki.info/)

### *Posts*

* [Paged Out! prints are here, and so is #7 CFP deadline,](?id=805)
* [CONFidence 2025 is next week,](?id=804)
* [No, CTRL+D in Linux terminal doesn't send EOF signal,](?id=801)
* [New edu platform and 'Sanitization and Validation and Escaping, Oh My!' article,](?id=800)
* [On hackers, hackers, and hilarious misunderstandings,](?id=799)
* [Paged Out! #5 is out,](?id=797)
* [CVEs of SSH talk this Thursday,](?id=796)
* [Debug Log: Internet doesn't work (it was the PSU),](?id=793)
* [FAQ: The tragedy of low-level exploitation,](?id=791)
* [Solving Hx8 Teaser 2 highlight videos!,](?id=789)
* [→ see all posts on main page](/)

// copyright © Gynvael Coldwind
// design & art by Xa
// logo font (birdman regular) by utopiafonts / Dale Harris

/\* the author and owner of this blog hereby allows anyone to test the security of this blog (on HTTP level only, the server is not mine, so let's leave it alone ;>), and try to break in (including successful breaks) without any consequences of any kind (DoS attacks are an exception here) ... I'll add that I planted in some places funny photos of some kittens, there are 7 of them right now, so have fun looking for them ;> let me know if You find them all, I'll add some congratz message or sth ;> \*/

**Vulns found in blog:**
\* XSS *(pers, user-inter)* by ged\_
\* XSS *(non-pers)* by Anno & Tracerout
\* XSS *(pers)* by Anno & Tracerout
\* Blind SQLI by Sławomir Błażek
\* XSS *(pers) by* Sławomir Błażek

2024-07-31:

## [Darmowe mini-szkolenie: Pliki okiem hackera](?id=790)

hexarcana

[![](img/hexarcana-pliki-2024.jpg)](https://sklep.securitum.pl/pliki-okiem-hackera?utm=gyn-blog)

**W skrócie**: zebrałem masę różnych trików, ciekawostek, sztuczek, kruczków i szczególików o plikach z perspektywy systemu operacyjnego / użytkownika / admina / tudzież hackera, i [razem z sekurak.pl / Securitum robimy o tym webinar](https://sklep.securitum.pl/pliki-okiem-hackera?utm=gyn-blog). Wstęp w systemie "zapłać ile chcesz (w tym 0 PLN)", ale trzeba się zarejestrować. Na oko potrwa 2 godziny.

A teraz trochę szczegółów:

* **Kiedy:** 21. sierpnia 2024
* **Gdzie:** online
* **Za ile:** zapłać ile chcesz, w tym 0 PLN (bo podobno za darmo to dobra cena).
  + Jest też opcja z dodatkowymi materiałami i certyfikatem uczestnictwa za około 48 PLN.
* **Rejestracja:** [klik](https://sklep.securitum.pl/pliki-okiem-hackera?utm=gyn-blog)
* **O czym będzie (ale tak w skrócie):**
  + ficzery systemów plików,
  + atrybuty plików (np. szyfrowanie w NTFS),
  + pseudo pliki,
  + prawa dostępu do plików i katalogów (i różne podejścia do tego),
  + operacje na plikach (i czemu tworzenie plików czasem jest niebezpiecznie trudne),
  + ścieżki do plików (i czemu to jest jeszcze trudniejsze),
  + deliktanie też poruszę temat informatyki śledczej (forensics),
  + i jeszcze garść innych losowych ciekawostek.
    Generalnie sądzę, że każdego czymś zaskoczę ;)* **Gdzie można więcej o tym poczytać:**
    + [Na stronie rejestracji](https://sklep.securitum.pl/pliki-okiem-hackera?utm=gyn-blog) (jest tam masa info).
    + [Na blogu HexArcana](https://hexarcana.pl/b/2024-07-30-mini-szkolenie-pliki-okiem-hackera/)
    + [Na ładnej stronce reklamowej.](https://hexarcana.pl/lp/pliki/)

Zachęcam do udziału – powinno być ciekawie ;)

*Gynvael*

## Add a comment:

|  |  |
| --- | --- |
| Nick: |  |
| URL (optional): |  |
| Math captcha: 8 ∗ 9 ＋ 7 = |  |
|  | |