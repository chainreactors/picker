---
title: KnightCTF 2023 write-ups (RE category)
url: https://gynvael.coldwind.pl/?id=761
source: gynvael.coldwind//vx.log (en)
date: 2023-01-23
fetch_date: 2025-10-04T04:35:28.671917
---

# KnightCTF 2023 write-ups (RE category)

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

2023-01-22:

## [KnightCTF 2023 write-ups (RE category)](?id=761)

ctf

On Friday/Saturday (yeah, right about [when layoff news](https://blog.google/inside-google/message-ceo/january-update/) hit) I played a CTF for fun/to relax with some friends. Our choice was [KnightCTF 2023](https://ctftime.org/event/1792)and here are some writeups of the tasks I solved or helped solve (Reverse Engineering category only for now).

Update: Added a guest write-up for the Stegorev challenge by Sir P. Gently.

* [[RE 100] Help Jimmy](#helpjimmy)
* [[RE 150] The Activator](#theactivator)
* [[RE 200] KrackMe 1.0](#krackme)
* [[RE 250] Fan](#fan)
* [[RE 250] Take RISC five times](#riscv)
* [[RE 400] Stegorev](#stegorev)

## [[RE 100] Help Jimmy](#helpjimmy)

Help Jimmy was a 64-bit Linux ELF binary, with a simple "game" implementation where the player had the choice to venture either into the Jungle or into the Sea. Regardless of the chosen path, it ended with Jimmy getting attacked by tigers or pirates and not getting the flag.

The game part was actually a distraction, as the actual purpose of the task was to notice that on the very top of the main() function there is something like this:

`int x = 5;
int y = 5;
if (x != y) {
some_function();
}`

While this is quite easy to spot in assembly, some decompilers (e.g. Ghidra) optimized out that branch and never showed it, thus making it easy to be missed.

![Screenshot from Ghidra showing assembly with the visible function call just after a comparison, and decompiler view with the if and function call missing.](img/kctf23_helpjimmy.png)

Anyway, since this is a "just NOP the check" type of reverse engineering challenge (basically a classical *crackme*), the easiest way to solve is to either swap the comparison or NOP it out. This time around I've done the latter using GDB:

`break *0x0000555555555629
r
set *(unsigned char*)0x555555555653 = 0x90
set *(unsigned char*)0x555555555654 = 0x90
c`

Flag: **KCTF{y0u\_may\_ch00s3\_to\_look\_7h3\_other\_way\_but\_y0u\_can\_n3v3r\_say\_4gain\_that\_y0u\_did\_n0t\_know}**

## [[RE 150] The Activator](#theactivator)

Actually this was a super similar task to Help Jimmy – i.e. it was also a classic *crackme*. In this case we were greeted in the main() function with with a whole set of complicated checks, which eventually just set one single flag (as in a boolean value denoting whether the input was deemed acceptable). This flag was then checked, and when true, the CTF flag was displayed.

`if (checks_ok) {
show_flag();
} else {
std::cout << "Invalid Key." << std::endl;
}`

This time around, instead of NOPing out the check, I just set RIP just before the show\_flag() call:

`KnightOS License Checker.
Enter KnightOS Activation Key: ^C
Program received signal SIGINT, Interrupt.
0x00007ffff7b52992 in __GI___libc_read ...
(gdb) finish
Run till exit from #0 0x00007ffff7b52992 in __GI___libc_read ...
asdf
...
Value returned is $1 = 5
(gdb) set $rip=0x555555555bce
(gdb) c
Continuing.
KCTF{Th47_License_ch3cker_w4S_similar_t0_Wind0ws_95_OSR_Activator_Right?}
munmap_chunk(): invalid pointer
Program received signal SIGABRT, Aborted.`

## [[RE 200] KrackMe 1.0](#krackme)

KrackMe 1.0 was actually solved in 99% by my friends and I just jumped in in the last moment to help with the final step. In general the task consists of a flag being split into four 9-character parts. Then each part was XORed with – effectively – a constant byte, and compared to static hardcoded values.

The issue we faced was with the 3rd part of the flag – for some reason we were getting the constant wrong. But, since the constant was just one byte, we eventually just brute forced it. Here's the script:

`` v13 = "mer`]MtGeaUG9UeDoU"
v14 = "(G~Ty_G{(v}QlOto|s"
v17 = "You don't have access to KrackMe 1.0 !"
v18 = "Since you are here let me ask you something..."
v15 = "Please enter the flag : "
v16 = "Oh My God ! What is that ?"
v20 = "Did you know, Bangladesh has the longest natural beach?..."
v13r = "mer`]MtGeaUG9UeDoU"
v14r = "(G~Ty_G{(v}QlOto|s"
for m in range(0,255):
flag = ""
for i in range(9):
flag += (chr((ord(v13r[i]) ^ ord(v20[14]) ^ ord(v16[8])) & 0xff))
for i in range(9):
flag += (chr((ord(v13r[i + 9]) ^ ord(v17[1]) ^ ord(v13r[1])) & 0xff))
mid = ""
for i in range(9):
mid += (chr((ord(v14[i]) ^ m) & 0xff))
flag += mid
for g in range(9):
flag += (chr((ord(v14r[g + 9]) ^ ord(v17[11]) ^ ord(v17[1])) & 0xff))
if "_" in mid: # Output filtering by guessing there will be _ in this part.
print(flag) ``

And the flag:

`$ python go.py
KCTF{kRaCk_M3_oNe_(G~Ty_G{(xs_bAzar}
KCTF{kRaCk_M3_oNe_#Lu_rTLp#xs_bAzar}
KCTF{kRaCk_M3...