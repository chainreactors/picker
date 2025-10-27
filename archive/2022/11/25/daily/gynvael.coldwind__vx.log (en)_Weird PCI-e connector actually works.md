---
title: Weird PCI-e connector actually works
url: https://gynvael.coldwind.pl/?id=759
source: gynvael.coldwind//vx.log (en)
date: 2022-11-25
fetch_date: 2025-10-03T23:43:36.397522
---

# Weird PCI-e connector actually works

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

2022-11-24:

## [Weird PCI-e connector actually works](?id=759)

pcie

This is actually a follow-up to the last paragraph from my previous [Debug Log](/?id=757). To save you some reading, I was trying to find which device causes boot delays on my PC. Eventually I traced it to a Bluetooth module, which – to my surprise – was a part of a detachable WiFi+BT module connected to a custom 20-pin header on the motherboard (electrically that was an M.2 key E, i.e. PCI-e x1 + USB). The afore mentioned last paragraph goes like this:

The only question that remains is whether one can attach a GPU through an adapter to this slot (will be pretty slow, especially that it's PCI Express x1 version 2.0 – since it's attached to the chipset and X99 does only PCIe 2.0). Not that there is any reason to do it. Anyway, I might or might not have ordered a proper cursed adapter from a certain Chinese electronics site, so guess we'll find out.

Well, the adapter arrived yesterday, so I took it for a spin. The rest of this blogpost consists mostly of photos.

[![](img/keye_adapter.jpg)](img/keye_adapter.jpg)
Top: M.2 key E adapter to PCI-e x1 slot, with a 20cm ribbon cable in between
Bottom: SATA power cable used to give PCI-e device some power
[![](img/keye_adapter_full.jpg)](img/keye_adapter_full.jpg)
M.2 side of the adapter connected to the M.2–to–20-pin-header adapter that previously housed the WiFi+BT module
[![](img/keye_adapter_in_adapter.jpg)](img/keye_adapter_in_adapter.jpg)
Close up of said adapters. The part of metal housing is there only because the screw keeping the M.2 device in place is screwed into the housing
[![](img/keye_card.jpg)](img/keye_card.jpg)
A ZOTAC GeForce GT 710 PCI-e x1 GPU (ZT-71304-20L) connected into the adapter. This is an "as cheap as it gets" card – I keep a bunch of these as a "I need only to enter BIOS please don't occupy too many PCI-e lanes" graphic cards
[![](img/keye_header.jpg)](img/keye_header.jpg)
Left side of the image: the 20-pin header socket on the motherboard; technically it's a 19-pin keyed header socket, since one pin holes is filled up
[![](img/keye_adapter_installed_mobo.jpg)](img/keye_adapter_installed_mobo.jpg)
Adapter connected to the header on the motherboard
[![](img/keye_running.jpg)](img/keye_running.jpg)
This GPU was light enough I could just literally put it on the USB/TOSLINK cables for it to hang there

After all of this was connected I powered up the PC. To my surprised, it both POSTed and detected the GPU:

`23:16:30 root:haven# lspci | grep -i nvidia
0a:00.0 VGA compatible controller: NVIDIA Corporation GK208B [GeForce GT 710] (rev a1)
0a:00.1 Audio device: NVIDIA Corporation GK208 HDMI/DP Audio Controller (rev a1)`

The link, as expected, was PCI-e 2.0 x1 (i.e. 5 gigatransfers per second times 1):

`0a:00.0 VGA compatible controller: NVIDIA Corporation GK208B [GeForce GT 710] (rev a1) (prog-if 00 [VGA controller])
Subsystem: ZOTAC International (MCO) Ltd. GK208B [GeForce GT 710]
...
LnkSta: Speed 5GT/s (ok), Width x1 (downgraded)`

Next came connecting an LCD panel. This also worked without any issues, though the image quality was a bit iffy and it was flickering:

**By the way...**
If want to improve your binary file and protocol skills, check out the workshop I'll be running between April and June → [Mastering Binary Files and Protocols: The Complete Journey](https://hackarcana.com/workshop-session/2025-Q1-Q1-mastering-binary/buy?utm=gyn-blog-inad)

[![](img/keye_1080i.jpg)](img/keye_1080i.jpg)
The picture looks like the scan lines were doubled

My best guess is that for some reason this GPU together with my OS decided to output the image using a 1080i ([interlaced](https://en.wikipedia.org/wiki/1080i)) format, but my LCD had no idea what to do about with it and just doubled the scan lines, hence the flickering. On a screenshot everything was fine. That said, since all this was just to test if it would actually work, I didn't follow up on this.

Of course I do not plan to use this for anything, but since I am a fan of cursed stuff in computing I had to check if this would actually work. And, somewhat to my surprise, it did. Nice.

## Add a comment:

|  |  |
| --- | --- |
| Nick: |  |
| URL (optional): |  |
| Math captcha: 9 ∗ 3 ＋ 9 = |  |
|  | |