---
title: Solving a VM-based CTF challenge without solving it properly
url: https://gynvael.coldwind.pl/?id=763
source: gynvael.coldwind//vx.log (en)
date: 2023-02-06
fetch_date: 2025-10-04T05:47:15.118291
---

# Solving a VM-based CTF challenge without solving it properly

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

2023-02-05:

## [Solving a VM-based CTF challenge without solving it properly](?id=763)

ctf:re:side-channel

A pretty common reverse-engineering CTF challenge genre for the hard/very-hard bucket are virtual machines. There are several flavors to this\*, but the most common one is to implement a custom VM in a compiled language and provide it together with bytecode of a flag checker. This was the case for the **More Control** task from [Byte Bandits CTF 2023](https://ctftime.org/event/1877) – the task this entry is about. The typical approach to these kind of challenges is to reverse the binary and "look" at the bytecode enough to understand the opcode format and write at least a disassembler (and ideally reimplement the VM in Python), and then to analyze what's going on in the bytecode itself. **Sometimes however you can take a shortcut**. This post is a semi-complete write-up of a side-channel based solution for the aforementioned task.

\* Other flavors include: 1) not providing the VM binary, but providing network access to some "system" running on it where you can run bytecode you provide and observe results; 2) not providing the VM binary; this hard-core sub-genre is rare and requires players to determine opcode encoding by just looking at unknown bytecode, which they can't even execute; 3) instead of a flag checker you get something that writes out the flag, but it takes literal years to write it out - so it's a typical "optimize me".

### Side-channel attacks

You can safely skip this section if you know what a side-channel is.

A side-channel is basically a somewhat obscure and somewhat hidden weak source of information about an observed process. For example, the main channel of information for a program is what you see as the output on the screen. A side-channel however could be e.g. CPU usage graph, computer's power usage, electro-magnetic emission, or electronic component sound emission. And – or maybe first and foremost – measuring elapsed time. Here's a typical example (pseudo-code... well, that's actually Python):

`def check_password(good_password, entered_password):
if len(good_password) != len(entered_password):
return False
for i in range(len(good_password)):
if good_password[i] != entered_password[i]:
return False
return True`

Now assume that:

* you don't know the correct password,
* you can enter any password you like, how many times you like,
* you can measure in great resolution how long does it take for the check\_password function to execute.

The first check there is the password length. If the length doesn't match, we short-circuit into a function exit in form of return False. If it matches however, a bit more code gets executed – loop setup, range "generator" creation, checking the first password letter, etc. This means that if we try a wrong password with the right length the measured execution time will be longer than if we try a wrong password with the wrong length.

`Trying Measured time
"a" 73 ns
"aa" 72 ns
"aaa" 71 ns
"aaaa" 74 ns
"aaaaa" 73 ns
"aaaaaa" 73 ns
"aaaaaaa" 72 ns
"aaaaaaaa" 73 ns
"aaaaaaaaa" 72 ns
"aaaaaaaaaa" 133 ns
"aaaaaaaaaaa" 71 ns
"aaaaaaaaaaaa" 73 ns`

In the example above, it's pretty clear that the 10-character candidate password caused the execution to be almost twice as long. From this we can easily infer that the password should be 10 characters long. Note that measuring time above has some noise in it – usually that noise is much worse, but let's keep this simple.

Next step is to brute-force the password character-by-character. When we hit the right letter at the given position, we'll ~~hear a characteristic \*click\* sound~~ observe time measurement increase for the given character.

`Trying Measured time
"aaaaaaaaaa" 134 ns
"baaaaaaaaa" 131 ns
"caaaaaaaaa" 130 ns
"daaaaaaaaa" 155 ns
"eaaaaaaaaa" 132 ns
...
"yaaaaaaaaa" 130 ns
"zaaaaaaaaa" 133 ns`

And eventually we would arrive at the whole password.

Of course in real world no one™ does that kind of comparisons (first of all because passwords are hashed, but let's ignore that for a second). Usually folks use just plain old return good\_password == entered\_password which would internally use some form of optimized multiple-bytes-at-the-same-time comparisons – the "multiple-bytes" part there basically disables the character-by-character attack. Additionally, folks that know a bit about cryptography would use a constant-time comparison schema – no side-channels here.

On top of that measuring execution time using a wall clock (i.e. real human time) is hard, as the operating system usually has multiple other threads running which pu...