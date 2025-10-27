---
title: Debug Log: Internet doesn't work (it was the PSU)
url: https://gynvael.coldwind.pl/?id=793
source: gynvael.coldwind//vx.log (en)
date: 2024-09-01
fetch_date: 2025-10-06T18:24:46.105679
---

# Debug Log: Internet doesn't work (it was the PSU)

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

2024-08-31:

## [Debug Log: Internet doesn't work (it was the PSU)](?id=793)

debug log

[![A photo of an open-bench mounted server in a server rack.](img/t_daemon_in_red.jpg)](img/daemon_in_red.jpg)

I woke up in the morning, got to the desk in my home office, checked my email, discord, and the news. Then I switched from my desktop to my laptop and... there's no internet.

That's weird. I just browsed the net on my PC, so what's up with the laptop? Both are connected to the same network, so it's not the problem of the network not having connectivity. As such, the problem lies between my ISP's modem and the laptop (inclusive).

I started with disconnecting and reconnecting the ethernet network cable (it's a pretty stationary laptop, so I keep it wired). That didn't fix anything, apart from displaying a short spinning animation indicating it's trying to get an IP address assigned (a DHCP issue then?). Just to be sure it's nothing on the laptop side I did a reboot, and then power-cycled the nearest network switch for good measure as well. No luck.

Following up on the DHCP lead I logged into my home server, which runs the DHCP daemon... wait... what is this?

`ssh: connect to host home server port 22: No route to host`

So I moved the chair a bit to check my server rack, and found the home server dark. That's unusual. On closer inspection actually the LEDs on the motherboard next to the power/reboot buttons were lit. A minor explanation here: I use customized [Open Benchtable](https://openbenchtable.com/) mounts, so the mobo is easily accessible; at the same time it means there are no power/reboot buttons on the case – as there is no case – so I rely on mobos having power/reboot buttons directly on them (or, failing that, small buttons-on-PCBs that you hook into the normal case button connector on the mobo).

I clicked the power button, and... even the two last LEDs went dark. Not great. They did light back up a few seconds later though, so re-tried a couple of times, with the same result. The closest I got to a "fully functional and running server" was the CPU fan spinning up for 0.5 seconds.

At this point I had good news and bad news:

* Good news: I found the problem! DHCP server is down because...
* Bad news: ...the server is dead.

The next step was to turn on some DHCP server in the network so that the Internet actually works in the household, and to let everyone using the server know that there are problems.

**By the way...**
If want to improve your binary file and protocol skills, check out the workshop I'll be running between April and June → [Mastering Binary Files and Protocols: The Complete Journey](https://hackarcana.com/workshop-session/2025-Q1-Q1-mastering-binary/buy?utm=gyn-blog-inad)

Of course it's rarely that the whole computer dies – usually it's just one component. As such, the next step was to figure out which component(s) are defective.

The usual algorithm for this is:

1. Disconnect power and let it chill for 10-20 seconds (i.e. wait for all/most capacitors to discharge).
2. Disconnect all unnecessary peripherals like: all storage devices (HDDs, SSDs), all PCIe cards, all USB devices, etc. Hint: make a couple of photos of what is connected where – even if you keep detailed documentation on the setup (you do, right?), it can save some time.
3. Remove all RAM modules apart from one. You basically want to be left only with mobo, CPU, PSU, and one RAM stick (and PC case connectors – these are usually fine).
4. Connect power, attempt to turn on the computer.
5. If nothing boots at this moment, go to point 1 and try a different RAM module or try putting it in a different RAM slot. Repeat this until you run out of options.
6. If you get the computer to boot in this "minimized" state...
7. Power everything down (see point 1).
8. Add one random device or RAM module from the batch you've disconnected earlier (usually starting with the GPU makes most sense, as that way you get a display later on).
9. Connect power, attempt to turn on the computer.
10. If things boot, go to point 7 (IMPORTANT: don't do after-POST hard power offs from the moment you connect any storage device).
11. If things don't boot, you found the culprit (though it might be either the slot/connector, cable, or actual device; pretty easy to figure out at this point though using a similar approach to the one described below).

In my case I basically run out of options at point 5, which translates to: it's what's left, i.e. the problem lies either in the CPU, the motherboard, the PSU, or ?all the RAM dice? (unlikely, but at the end of the day anything can break). ...