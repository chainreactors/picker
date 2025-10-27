---
title: A clever Python challenge – find flag
url: https://gynvael.coldwind.pl/?id=758
source: gynvael.coldwind//vx.log (en)
date: 2022-11-14
fetch_date: 2025-10-03T22:40:32.241248
---

# A clever Python challenge – find flag

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

2022-11-13:

## [A clever Python challenge – find flag](?id=758)

ctf:python

SECCON CTF 2022 Quals are over and I have to say that the tasks which I looked at were of pretty amazing quality. The task that I started with was called "find flag" and was authored by [ptr-yudai](https://twitter.com/ptrYudai). While it's a tiny warmup challenge, I found it extremely clever! So, here's a writeup.

`#!/usr/bin/env python3.9
import os
FLAG = os.getenv("FLAG", "FAKECON{*** REDUCTED ***}").encode()
def check():
try:
filename = input("filename: ")
if open(filename, "rb").read(len(FLAG)) == FLAG:
return True
except FileNotFoundError:
print("[-] missing")
except IsADirectoryError:
print("[-] seems wrong")
except PermissionError:
print("[-] not mine")
except OSError:
print("[-] hurting my eyes")
except KeyboardInterrupt:
print("[-] gone")
return False
if __name__ == '__main__':
try:
check = check()
except:
print("[-] something went wrong")
exit(1)
finally:
if check:
print("[+] congrats!")
print(FLAG.decode())`

When taking the task at the face value it looks like it's about finding a file containing the flag on the filesystem. This in all honesty was my initial thought as well. And due to reasons (a certain exercise I make some of people I'm mentoring do\*) I've solved the task by accident before I fully understood what's going on. Let's look at the details.

\* The exercise goes as follows: "having open(CONTROLLED) in Python, make it throw as many different exceptions as you can manage; do this on Windows and Linux separately". The idea there is to point out how misleading the documentation can be ([it literally says](https://docs.python.org/3/library/functions.html#open) "[if] the file cannot be opened, an OSError is raised"), push for a bit of creativity and a hacker's mindset, and show that dealing with files is complicated.

There are basically two pieces of code: the check function and the "main" part of the code in global space, which for simplicity I will call the main function.

The main function basically calls the check function and verifies whether it returns True – or rather something that evaluates as true; note the difference between if check: and if check is True. In case of any exception it prints out "something went wrong" and calls exit(1).

The check function tries to open a file – the player controls its name – then reads its content and compares it with the actual flag. If it matches, True is returned. If any of the handled exceptions happens or the flag does not match the read content, False is returned.

So, on face value, to get the flag one needs to discover where is it stored on the filesystem, be it intentionally or due to some inner workings of the operating system. For example, /proc/self/environ immediately comes to mind (as the flag is originally read from environment variables), however it won't work since the condition requires for the flag to be at the very beginning of the file read.

**The thing is... that's not what the task is about at all.**

Let me start by saying how I solved it: I passed a null-byte as the file name.

I encourage the reader to take a break and look at the code again knowing the solution. It is still not trivial to see why that would work! And that's how we reach the beauty of this challenge.

There are several things one has to notice (or know) in this case:

1. The first one is pretty obvious and I've already hinted at it. Not all exceptions have been handled in the check function. Case in point being the null-byte which – as part of [poison null-byte](https://cwe.mitre.org/data/definitions/626.html) protection – raises a ValueError. This causes the exception to "walk up the call stack" to find an except-block which will handle it. In case of this task that's the catch-all except-block in the main function.
2. Second is harder to spot and is commonly a subject of confusion for more junior programmers – [shadowing](https://en.wikipedia.org/wiki/Variable_shadowing). Note that there are two checks. There's the check function, but there's also the check local variable in the main function. If we look at the finally-block in the main function, we notice that check is used there as a condition to show the flag. However it's actually not clear whether it refers to the function or the local variable. To be more precise, there are two options. If no exception is thrown, then the check = check() line will call the check function and only then create the check local variable and initialize its value with whatever the function call returned. When an exception is raised inside the check function however, then ...