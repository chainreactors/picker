---
title: xz/liblzma: Bash-stage Obfuscation Explained
url: https://gynvael.coldwind.pl/?id=782
source: gynvael.coldwind//vx.log (en)
date: 2024-03-31
fetch_date: 2025-10-04T12:08:23.111111
---

# xz/liblzma: Bash-stage Obfuscation Explained

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

2024-03-30:

## [xz/liblzma: Bash-stage Obfuscation Explained](?id=782)

xz:liblzma

Yesterday [Andres Freund emailed oss-security@](https://www.openwall.com/lists/oss-security/2024/03/29/4) informing the community of the discovery of a backdoor in xz/liblzma, which affected OpenSSH server (huge respect for noticing and investigating this). Andres' email is an amazing summary of the whole drama, so I'll skip that. While admittedly most juicy and interesting part is the obfuscated binary with the backdoor, the part that caught my attention – and what this blogpost is about – is the initial part in bash and the simple-but-clever obfuscation methods used there. Note that this isn't a full description of what the bash stages do, but rather a write down of how each stage is obfuscated and extracted.

P.S. Check the comments under this post, there are some good remarks there.

## Before we begin

We have to start with a few notes.

First of all, there are two versions of xz/liblzma affected: 5.6.0 and 5.6.1. Differences between them are minor, but do exist. I'll try to cover both of these.

Secondly, the bash part is split into three (four?) stages of interest, which I have named Stage 0 (that's the start code added in m4/build-to-host.m4) to Stage 2. I'll touch on the potential "Stage 3" as well, though I don't think it has fully materialized yet.

Please also note that the obfuscated/encrypted stages and later binary backdoor are hidden in two test files: tests/files/bad-3-corrupt\_lzma2.xz and tests/files/good-large\_compressed.lzma.

## [Stage 0](#stage0)

As pointed out by Andres, things start in the [m4/build-to-host.m4](https://salsa.debian.org/debian/xz-utils/-/blob/debian/unstable/m4/build-to-host.m4?ref_type=heads#L63) file. Here are the relevant pieces of code:

`...
gl_[$1]_config='sed \"r\n\" $gl_am_configmake | eval $gl_path_map | $gl_[$1]_prefix -d 2>/dev/null'
...
gl_path_map='tr "\t \-_" " \t_\-"'
...`

This code, which I believe is run somewhere during the build process, extracts Stage 1 script. Here's an overview:

1. Bytes from tests/files/bad-3-corrupt\_lzma2.xz are read from the file and outputted to standard output / input of the next step – this chaining of steps is pretty typical throughout the whole process. After everything is read a newline (\n) is added as well.
2. The second step is to run tr (translate, as in "map characters to other characters", or "substitute characters to target characters"), which basically changes selected characters (or byte values) to other characters (other byte values). Let's work through a few features and examples, as this will be imporant later.

   The most basic use looks like this:
   `echo "BASH" | tr "ABCD" "1234"
   21SH`
   What happend here is "A" being mapped to (translated to) "1", "B" to "2", and so on.

   Instead of characters we can also specify ranges of characters. In our initial example we would just change "ABCD" to "A-D", and do the same with the target character set: "1-4":
   `echo "BASH" | tr "A-D" "1-4"
   21SH`

   Similarly, instead of specyfing characters, we can specify their ASCII codes... in octal. So "A-D" could be changed to "\101-\104", and "1-4" could become "\061-\064".
   `echo "BASH" | tr "\101-\104" "\061-\064"
   21SH`

   This can also be mixed - e.g. "ABCD1-9\111-\115" would create a set of A, B, C, D, then numbers from 1 to 9, and then letters I (octal code 111), J, K, L, M (octal code 115). This is true both for the input characters set and the target character set.

   Going back to the code, we have tr "\t \-\_" " \t\_\-", which does the following substitution in bytes streamed from the tests/files/bad-3-corrupt\_lzma2.xz file:
   * 0x09 (\t) are replaced with 0x20,
   * 0x20 (whitespace) are replaced with 0x09,
   * 0x2d (-) are replaced with 0x5f,
   * 0x5f (\_) are replaced with 0x2d,This actually "uncorrupts" the bad-3-corrupt\_lzma2.xz, which forms a proper xz stream again.
3. In the last step of this stage the fixed xz byte stream is extracted with errors being ignored (the stream seems to be truncated, but that doesn't matter as the whole meaningful output has already been written out). The outcome of this is the Stage 1 script, which is promptly executed.

**By the way...**
If want to improve your binary file and protocol skills, check out the workshop I'll be running between April and June → [Mastering Binary Files and Protocols: The Complete Journey](https://hackarcana.com/workshop-session/2025-Q1-Q1-mastering-binary/buy?utm=gyn-blog-inad)

## [Stage 1](#stage1)

In Andres' email that's the bash file starting with "####Hello####", which ...