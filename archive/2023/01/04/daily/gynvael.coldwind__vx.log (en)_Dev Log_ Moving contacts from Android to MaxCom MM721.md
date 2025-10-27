---
title: Dev Log: Moving contacts from Android to MaxCom MM721
url: https://gynvael.coldwind.pl/?id=760
source: gynvael.coldwind//vx.log (en)
date: 2023-01-04
fetch_date: 2025-10-04T02:59:00.282387
---

# Dev Log: Moving contacts from Android to MaxCom MM721

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

2023-01-03:

## [Dev Log: Moving contacts from Android to MaxCom MM721](?id=760)

devlog

![](img/mm721.png)As the old IT joke goes, in holiday season all IT workers visit their families to fix their computer. This time for me however it wasn't about fixing a computer, but copying contacts from an old Sony Ericsson (SE) Android phone to a new MaxCom\* MM721 comfort phone. I'm not really sure what OS its running, but the whole idea behind that device is that it's supposed to be really simple to use, with the target audience being e.g. older people. And the MM721 indeed is simple to the extreme. Simple enough that moving ~200 contacts from the old phone to the new one proved to be an interesting (programming) challenge, mostly because I definitely didn't want to do it manually.

\* As an editor I try to always get capitalization of company/product names correct, but MaxCom is not making it easy. In the official User Manual for said phone the logo says "MaxCom", the title says "Maxcom", and the official company address says "MAXCOM". I will stick with MaxCom.

On paper the whole thing should go like this:

1. Write contacts on the old phone to the SIM card.
2. Put the SIM card in the new phone.
3. Optionally agree to copy the contacts from the SIM card to the new phone.

If you're used to smartphones and stick only with a given family – be it iOS or Android – this whole concept of using the SIM card might sound weird, since contacts are copied via the cloud, right? This device is just too simple for that – there is no cloud sync. Actually there's no web browser on it either.

In any case the issue was that the SIM card I had could only hold 150 contacts. And I had 200 to move. Well then.

Of course one might rightfully point out, that I could first move half of the contacts, use the aforementioned "copy the contacts from SIM to phone memory" option, and then move the second half. Unfortunately the automatic backup function on the device auto-selected always the first 150 entries, and then threw an error. I could have perhaps manually removed the first 150 contacts or manually marked the last 50 contacts as "stored on SIM" (I didn't check if that was an option on the SE device, but I'm guessing it was), but I really wanted to avoid having to stuff manually.

So instead I decided to look for a more automated solution. Was it faster in the end? Not sure to be completely honest. But at least it was pretty fun!

In the manual I found that while the MM721 is a really simple device, you can actually connect it to a computer using USB. Once you do that, you have two options:

1. Mass Storage Device
2. COM Port

In the *Mass Storage Device* (MSD) mode you get access to part of the directory structure of the device. Unfortunately the phone book doesn't seem to be there. This was a bit unlucky, since I'm pretty sure I could have dealt even with a custom contact list format.

This left the *COM Port* option, which actually spawned /dev/ttyUSB0 and /dev/ttyUSB1 devices in my device tree (a serial connection, as expected). Or /dev/ttyACM0 and /dev/ttyACM1 (a USB modem, which does make sense). Wait, so which one is it? A serial port or a modem? Well, that turned out to be pretty random. Sometimes when I connected it it was the first one, and sometimes it was the other. I am also not sure why exactly were there two serial ports (or two modems). Oh well. Eventually I did disable the cdc\_acm kernel module so that it doesn't interfere with what I wanted to do.

And what I wanted to do is chat with the modem. You see, what I somewhat remembered from the olden days is that the [AT modem commands](https://en.wikipedia.org/wiki/Hayes_command_set#GSM) for cellphones could do a lot more than just initiate a modem connection. I figured it's possible they can modify the internal phone book. And it turned out I was correct!

* [AT+CPBR=12,34](https://m2msupport.net/m2msupport/atcpbr-read-phonebook-entries/) – read phone book entries from 12 to 34.
* [AT+CPBW=5,"123456789",129,"Gynvael"](https://m2msupport.net/m2msupport/atcpbw-write-phonebook-entry/) - overwrite phone book entry 5 with number 123456789 and name Gynvael.

Given this feature the plan was pretty simple: export all the contacts from SE to the pretty universal vCard format, read it into Python with some library, and convert to a set of AT commands to execute using /dev/ttyUSBx on the phone. Easy.

The first issue turned out to be reading in the exported vCard format. I've tried one or two libraries and both failed on multiline entries – usually base64 encoded photos (which I didn't need) or really long names (w...