---
title: Wstęp do inżynierii wstecznej
url: https://gynvael.coldwind.pl/?id=792
source: gynvael.coldwind//vx.log (pl)
date: 2024-08-14
fetch_date: 2025-10-06T18:02:36.799019
---

# Wstęp do inżynierii wstecznej

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

2024-08-13:

## [Wstęp do inżynierii wstecznej](?id=792)

re:asm

[![](img/reasm2024pl.png)](https://sklep.securitum.pl/zobacz-reversing-na-zywo?utm=gyn-blog)

Być może niektórzy z Was pamiętają moje kursy z serii ReverseCraft sprzed 15 lat. Serie tę zacząłem jeszcze mieszkając we Wrocławiu i nawet miałem ambicję, żeby rozwinąć to w porządny, kompletny zestaw kursów z inżynierii wstecznej i asemblera. Życie jednak miało swoje plany i niedługo później byłem zajęty przeprowadzką do Zurychu i rozpoczęciem pracy w Google. Przez lata co jakiś czas wracałem do publikowania materiałów dydaktycznych o RE – był mój kurs asemblera na YouTube (ten używający painta jako tablicy), książka "Praktyczna Inżynieria Wsteczna", trochę prelekcji, wpisów i artykułów, i sporo livestreamów. Przez cały ten czas obiecywałem sobie, że jeszcze wrócę do mojego coraz to starszego pomysłu.

I wiecie co? Wygląda na to, nadszedł czas, żeby coś robić w tym kierunku (choć w zasadzie coś tam w tle już się działo nawet rok temu).

Co za tym idzie, chciałbym zacząć od podstaw i **zaprosić Was na szkolenie "[RE+ASM! Wstęp do inżynierii wstecznej i asemblera](https://sklep.securitum.pl/zobacz-reversing-na-zywo?utm=gyn-blog)"** (x86-64).

Szkolenie odbędzie się w połowie września:

* **Część 1: Reversing na żywo!**
  10 września 2024, 19:00 (darmowe, tj. zapłać–ile–chcesz) – pierwsze z trzech spotkań w serii.
* **Część 2: Asembler x86-64**
  17 września 2024, 19:00 (płatne w pakiecie 1+2+3) – drugie z trzech spotkań w serii.
* **Część 3: Inżynieria Wsteczna**
  20 września 2024, 19:00 (płatne w pakiecie 1+2+3) – ostatnie z trzech spotkań w serii.

Jak widać wyżej, szkolenie jest rozbite na 3 części, po dwie i pół godziny każda (w tym czas na pytania). W zasadzie całość miała być płatna, ale ponieważ nikt nie lubi kupować kota w worku, to **na pierwszą część można przyjść za darmo i zobaczyć jak to wygląda (rejestracja wymagana)**.

**Cały pakiet (części 1+2+3) kosztuje natomiast 184 PLN z VAT**.

Agenda i wszystkie szczegóły można znaleźć w sklepie u naszych partnerów (Securitum):

* [Zobacz reversing na żywo!](https://sklep.securitum.pl/zobacz-reversing-na-zywo?utm=gyn-blog) (część 1)
* [RE+ASM! Wstęp do inżynierii wstecznej i asemblera](https://sklep.securitum.pl/wstep-do-inzynierii-wstecznej-i-asemblera?utm=gyn-blog) (części 1+2+3)

Serdecznie zapraszam!

P.S. Na bloga firmowego wrzuciliśmy wczoraj z Danem też [Top 100 instrukcji asemblera x86-64](https://hexarcana.pl/b/2024-08-12-top-100-instrukcji-asm-x86_64/), tj. coś co potrzebowaliśmy przy projektowaniu kursów z tej serii.

## Comments:

2024-08-16 18:55:30 = [Piotr](http://)

{

Dzień dobry. Czy będzie coś o Ghidra.

}

2024-08-17 06:34:47 = [Gynvael Coldwind](.)

{

@Piotr
Cześć! Ghidra będzie jednym z narzędzi, które się przewiną. Natomiast nie będzie to kurs Ghidry.

}

2024-08-17 10:29:12 = [Piotr](http://)

{

Ok. Dziękuję.

}

2025-03-25 20:04:57 = [Miki](http://)

{

Cześć! Widziałem, że szkolenie z RE + ASM już nie jest dostępne do kupienia – czy jest jeszcze jakaś szansa, żeby obejrzeć nagrania? :)

}

2025-03-25 21:09:57 = [Gynvael Coldwind](.)

{

@Miki
Będziemy powtarzać to szkolenie w tym roku prawdopodobnie. Ew gdzieś pojawią się nagrania do kupienia prędzej czy później – będę o jednym i drugim pisał tu i wszędzie indziej ;)

}

## Add a comment:

|  |  |
| --- | --- |
| Nick: |  |
| URL (optional): |  |
| Math captcha: 5 ∗ 3 ＋ 5 = |  |
|  | |