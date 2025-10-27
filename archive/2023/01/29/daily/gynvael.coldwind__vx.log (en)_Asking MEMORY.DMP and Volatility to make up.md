---
title: Asking MEMORY.DMP and Volatility to make up
url: https://gynvael.coldwind.pl/?id=762
source: gynvael.coldwind//vx.log (en)
date: 2023-01-29
fetch_date: 2025-10-04T05:07:52.946165
---

# Asking MEMORY.DMP and Volatility to make up

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

2023-01-28:

## [Asking MEMORY.DMP and Volatility to make up](?id=762)

volatility:forensics

A few days ago I've posted [RE category write-ups from the KnightCTF 2023](/?lang=en&id=761). Another category I've looked at – quite intensely at that – was forensics. While this blog post isn't a write-up for that category, I still wanted (and well, was asked to actually) write down some steps I took to make [Volatility](https://www.volatilityfoundation.org/) work with MEMORY.DMP file provided in the "Take care of this" challenge series. Or actually steps I took to convert MEMORY.DMP into something volatility could work with. I have to add that I didn't get the flags for these challenges\*, so again, this isn't a write-up.
\* It turned out that the flags weren't based on the MEMORY.DMP – the sole resource provided – at all due to an oversight in challenge creation. It was a pretty amusing situation we've learnt about after the CTF, but what can you do.

Let's start by stating the problem: neither Volatility 2 nor Volatility 3 were able to use MEMORY.DMP as input. WinDBG on the other hand had no issues at all, so we knew the file was correct.

`$ python2 vol.py --profile Win7SP1x64 -f ../MEMORY.DMP pslist
Volatility Foundation Volatility Framework 2.6
No suitable address space mapping found
Tried to open image as:
MachOAddressSpace: mac: need base
LimeAddressSpace: lime: need base
WindowsHiberFileSpace32: No base Address Space
WindowsCrashDumpSpace64BitMap: No base Address Space
WindowsCrashDumpSpace64: No base Address Space
...`

If you're unfamiliar with Volatility, it's an open-source forensics framework written in Python 2 and Python 3 respectively, which allows an investigator to run queries on computer system's memory dumps. Technically it understands internal Windows and Linux kernel memory objects and can walk through them to do stuff like listing running processes, dumping console buffers or the content of the clipboard, digging through the registry (it's in-memory version), etc. See [this example](https://volatility3.readthedocs.io/en/stable/getting-started-windows-tutorial.html#example) for instance. Pretty neat tool!

## Some theory on how Volatility works

As said, the input is a system memory dump. These however come in different shapes and sizes, depending on how one might have acquired it. For example, the one common source is a Blue Screen of Death-time automatic memory dump creation – it's usual purpose is to allow folks to put it in WinDBG and figure out why the system crashed. Another typical example includes providing a raw dump of physical memory – these can be acquired in a multitude of ways, though they don't really include any useful metadata (will get to this later). Either way, usually what you get is a dump of physical memory – *physical* being the keyword here.

Physical memory however won't do. That's because the great majority of the kernel structures – as well as literally everything in user-land – operates on *virtual* memory. So the first thing volatility has to do is basically load the proper parser for the given input format and then provide a *virtual* memory view for it. This can of course be done easily based on the [page table structure](https://en.wikipedia.org/wiki/Page_table) which maps virtual addresses to physical addresses.

One important thing to note here is that there isn't just one page table structure in memory. There are a lot of them – usually one per process, though in some cases even each thread might have one. That's OK however, since even if you find only a single page table in memory you'll be able to access the process/task/thread list, and these in turn hold physical addresses of their respective page tables. This means that each process/task/thread "sees different things" in memory, though usually at least the kernel part is seen by all of them in the same way.

Once Volatility has a virtual memory view it can proceed to do the required analysis by finding and walking through the aforementioned kernel structures. Of course each kernel version might have a bit different looking internal structures – this is best observed either on ReWolf's Terminus project website ([\_EPROCESS example](http://terminus.rewolf.pl/terminus/structures/ntdll/_EPROCESS_x64.html)) or Svitlana Storchak's / Sergey Podobry's Vergilius project website ([\_EPROCESS example again](https://www.vergiliusproject.com/kernels/x64/Windows%2011/21H2%20%28RTM%29/_EPROCESS)). To handle these differences Volatility 2 uses per-version profiles, which in turn refer to vtypes – these are kernel structure definitions in Python form:

...