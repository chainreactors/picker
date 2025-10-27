---
title: Debug Log: The mystery of usb 3-11 device
url: https://gynvael.coldwind.pl/?id=757
source: gynvael.coldwind//vx.log (en)
date: 2022-11-11
fetch_date: 2025-10-03T22:22:06.736071
---

# Debug Log: The mystery of usb 3-11 device

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

2022-11-10:

## [Debug Log: The mystery of usb 3-11 device](?id=757)

debuglog

**<PSA>** Twitter is going great! Here's my new profile on Mastodon: [@gynvael@infosec.exchange](https://infosec.exchange/%40gynvael). Now back to our show! **</PSA>**

I woke up today, turned on my PC, went to the kitchen to put on water for a cup of tea and came back to a set of black screens. This is pretty weird as Haven – my main workstation (named after a city from one of [my favorite book series](https://www.goodreads.com/series/50054-valdemar-chronological)) – while being a rather old computer starts pretty fast. But I patently waited and in a few seconds the typical BIOS/UEFI screen appeared followed by the OS booting... with some errors:

![Photo of part of an LCD showing two lines with the same error message: usb 3-11: device descriptor read/64, error -110](img/usb311_lcd_error.jpg)
Greeted by errors

This wasn't the first time it happened – rather than that it had a tendency to come and go. And to add a few minutes to the boot time. Being me I decided it's a great opportunity to wasted an odd hour to trace (and hopefully fix) the issue of the few minute longer boot. And you're invited to join me on this debugging adventure!

After my PC finally booted I was able to check dmesg:

`$ sudo dmesg | grep 3-11
[ 3.322054] usb 3-11: new full-speed USB device number 6 using xhci_hcd
[ 18.918083] usb 3-11: device descriptor read/64, error -110
[ 34.534084] usb 3-11: device descriptor read/64, error -110
[ 34.770056] usb 3-11: new full-speed USB device number 7 using xhci_hcd
[ 50.150082] usb 3-11: device descriptor read/64, error -110
[ 65.766082] usb 3-11: device descriptor read/64, error -110
[ 66.526056] usb 3-11: new full-speed USB device number 8 using xhci_hcd
[ 77.366057] usb 3-11: device not accepting address 8, error -62
[ 77.494056] usb 3-11: new full-speed USB device number 9 using xhci_hcd
[ 88.118054] usb 3-11: device not accepting address 9, error -62`

Seems a handful of devices numbered 6, 7, 8 and 9 connected to usb 3-11 port decided it's time to stop working. So, 3-11, which port is that? Luckily I have all the USB ports mapped out in my PC documentation (surprisingly yes, I really do keep a detailed set of notes – counting 29 pages at this moment – on Haven's configuration):

![Screenshot from my notes. The top part is a photo of the back plate of my PC's motherboard with drawn in lables for rows and columns of USB ports. This is followed with a hort list of bus numbers and xhci_hcd identifiers. And this in turn is followed by 3 tables denoting the usb id of every port, one table for each of USB 1.x, USB 2.0 and USB 3.x. There is no usb 3-11 device in any of the tables.](img/usb311_usb_map.png)
Notes on USB ports

Well. Uhm. There's no usb 3-11 in any of the tables. Which means it's most likely not a device connected to any of these ports. This left me with internal USB headers, a random USB-C connector on the opposite side of the motherboard which I always forget exists, and potentially any USB device soldered directly onto the motherboard.

Only one device is connected to the internal USB headers – a NZXT Kraken Z display on the water pump mounted the CPU (shows CPU temperature – useful). And lsusb showed it as Bus 003 Device 004 (i.e. usb 3-4) so it's not what I was looking for.

That random USB-C connector doesn't have anything connected either, so that left some kind of on-motherboard device. But which one? Given that it's broken and not visible in lsusb's output, checking this might be tricky. Thankfully I remember that [linux-hardware.org](https://linux-hardware.org/) exists – it's a huge community-driven database of all kinds of hardware related reports gathered from Linux computers – an ideal place to throw in my motherboard type (as shown by dmidecode – "X99A XPOWER GAMING TITANIUM (**MS-7A21**)") and check the USB related reports. This turned out to be [a perfect hit](https://linux-hardware.org/?probe=6faf6514f5&log=dmesg):

`[ 2.176749] usb 3-11: new full-speed USB device number 4 using xhci_hcd
[ 2.325805] usb 3-11: New USB device found, idVendor=<8087, idProduct=0a2b, bcdDevice= 0.01
[ 2.325806] usb 3-11: New USB device strings: Mfr=0, Product=0, SerialNumber=...`

So it's 8087:0a2b, which [apparently](https://linux-hardware.org/?id=usb:8087-0a2b) is an Intel Bluetooth wireless interface – here's its [page on Intel's website](https://www.intel.com/content/www/us/en/products/sku/86068/intel-dual-band-wirelessac-8260/specifications.html). The official name is "Intel® Dual Band Wireless-AC 8260" and it's a WiFi+Bluetooth adapter tha...