---
title: Issues + Updates With 'Boots 2 Roots'
url: https://blog.g0tmi1k.com/2011/11/sitenews-issues-updates-with/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:34.354389
---

# Issues + Updates With 'Boots 2 Roots'

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Issues + Updates With 'Boots 2 Roots'

As I use [backtrack-linux](http://www.backtrack-linux.org/) for my attacker's operating system, the OS has gone though some major updates *(new tools have been added, some removed and most of them been updated)*!

As a result there are a few minor issues with my guides for [boot 2 roots](https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/). The general process is the same, so I didn't see a "need" to re-do it all - *I hope this quick note sums it all up!*

### Brute Forcing (Hydra)

It has been reported that Hydra isn't 'playing nice' with backtrack 5 R1 (which at the time is the latest release of backtrack), but it's happy with backtrack 5. On some machines running certain programs (e.g. hydra) inside VMware, it gives out tons of '**Waiting for child process**' error messages.

### [De-ICE.net v2.0 (2.100) {Level 2 - Disk 1}](https://blog.g0tmi1k.com/2010/02/de-icenet-v20-1100-level-2-disk-1/)

'JBroFuzz' is no longer included in backtrack. I would recommend using '[DirBuster](https://www.owasp.org/index.php/Category%3AOWASP_DirBuster_Project)' instead.

Eph demonstrates this in his ~~video (hxxp://www.get-root.com/?p=167)~~.

### [pWnOS](https://blog.g0tmi1k.com/2010/04/pwnos/)

The local privilege escape DOES work - don't have it connected to the Internet. (Auto updates?)

[F4l13n5n0w](http://fallensnow-jack.blogspot.com/2011/10/update-pwnos-v1.html) has also found a few more vulnerability related this challenge.

### [Kioptrix - Level 2](https://blog.g0tmi1k.com/2011/02/kioptrix-level-2-injection/)

Due to a coding bug (Line 16, missing a `'` (single quote) in `<td algin='center>`) & using a newer version of firefox, after logging in the 'ping' page isn't displayed correctly. You can either:

* Use the firefox addon '[Firebug](https://getfirebug.com/)' to edit the page content fixing the issue.
* Seen in MagiaMystery's video: <https://www.youtube.com/watch?v=sDR7oryS48g>
* Use '[BurpProxy](http://portswigger.net/burp/proxy.html)' and craft the post request manually.
* Seen in Lnxg33k's video: <https://lnxg33k.wordpress.com/2011/08/20/video-kioptrix-level2-war-game-solution/>

### [Kioptrix - Level 3](https://blog.g0tmi1k.com/2011/08/kioptrix-level-3/)

[Swappage](https://twitter.com/Swappage) has done another method to escape privates to gain root access. Instead of using 'ht' to write file(s) in which to gain access, Swappage walks though the process of discovering and creating a exploit for the program instead!

Video: <http://vimeo.com/28327470>.

### [VulnImage](https://blog.g0tmi1k.com/2011/12/vulnimage-manual-method/)

[\_pr0n\_](http://ghostinthelab.wordpress.com/) has discovered [another](https://twitter.com/#!/_pr0n_/status/150627688296624129) way to gain shell into this box by using [Exim](http://www.exploit-db.com/exploits/15725/) ([Proof](http://img543.imageshack.us/img543/480/p20o.png)).

### General message regarding all "[boot 2 roots](https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/)"

Don't use it on your main or production network as:

* You're adding a vulnerable machine on your network - just making it weaker!
* The machine could auto update - therefore breaking the challenge!

### The target's virtual machine isn't showing up! Its not working! I can't find it! Help!

If the challenge is a **ISO** then [VirtualBox](https://www.virtualbox.org/), [VMware](http://www.vmware.com/) and [Parallels](http://www.parallels.com/) etc - should **all work**.

However if its a Virtual Machine, check the format it in and use **that vendor**.

Most of them are in VMware as it has the market share.

You can try and use another vendor, however don't expect it to work, due to each product using different drivers for interfaces - therefore there might not be any network activity.

When using **VMware images**, always select '**moved it**'.

When you select 'copied it', it creates another interface, therefore it the automated, backend scripts are not configured to use the new interface.

The only issue with selecting 'move it', is if you have have another copy/version of that VM.

As you haven't got the another copy of it, it hasn't got anything to clash with.

Not every **challenge is setup to use DHCP**!

Some have **static IP addresses** (this is because the scripts & settings used have that IP assigned to it when it was created).

Read the 'readme' file and/or the homepage as it *could* mention the IP address/range which is used. Else I recommend using [netdiscover](http://www.nixgeneration.com/~jaime/netdiscover/).

Not every device respones to **ping (ICMP) requests** and these VM's are no exception. You might have to look into other methods of detecting machines on a network.

### Links

* [Blindly Installing VMs and Using Live CDs](http://www.digininja.org/blog/untrusted_vms.php)
* [How to set up a penetration testing lab](http://www.metasploit.com/learn-more/how-do-i-use-it/test-lab.jsp)

Posted by g0tmi1kNov 2nd, 2011 11:58 am [boot2root](/./boot2root/), [site news](/./site-news/)

[« Blogs, Feeds, Guides + Links](/2011/11/blog-guides-links/ "Previous Post: Blogs, Feeds, Guides + Links") [Vulnerable by Design (Part 3) »](/2011/11/vulnerable-by-design-part-3/ "Next Post: Vulnerable by Design (Part 3)")

[![g0tmi1k](/images/logo.png)](/)

# Recent Posts

* [DVWA - Brute Force (High Level) - Anti-CSRF Tokens](/dvwa/bruteforce-high/)
* [DVWA - Brute Force (Medium Level) - Time Delay](/dvwa/bruteforce-medium/)
* [DVWA Brute Force (Low Level) - HTTP GET Form [Hydra, Patator, Burp]](/dvwa/bruteforce-low/)
* [DVWA - Main Login Page - Brute Force HTTP POST Form With CSRF Tokens](/dvwa/login/)
* [Damn Vulnerable Web Application (DVWA)](/dvwa/index/)
* [Offensive Security Wireless Attacks (WiFu) + Offensive Security Wireless (OSWP)](/2014/01/offensive-security-wireless/)
* [Cracking the Perimeter (CTP) + Offensive Security Certified Expert (OSCE)](/2013/08/cracking-perimeter-ctp-offensive/)
* [pWnOS 2 (PHP Web Application)](/2012/09/pwnos-2-php-web-application/)
* [pWnOS 2 (SQL Injection)](/2012/09/pwnos-2-sql-injection/)
* [21LTR - Scene 1](/2012/09/21ltr-scene-1/)
* [Stripe CTF 2.0 (Web Edition)](/2012/09/stripe-ctf-20-web-edition/)
* [Kioptrix - Level 4 (Local File Inclusion)](/2012/02/kioptrix-level-4-local-file/)
* [Kioptrix - Level 4 (SQL Injection)](/2012/02/kioptrix-level-4-sql-injection/)
* [Kioptrix - Level 4 (Limited Shell)](/2012/02/kioptrix-level-4-limited-shell/)
* [Hackademic RTB2](/2012/01/hackademic-rtb2/)

[![RSS Feed](/images/social/rss.png "RSS")](/atom.xml "RSS") [![GitHub Profile](/images/social/github.png "GitHub")](https://github.com/g0tmi1k "GitHub") [![Twitter Profile](/images/social/twitter.png "Twitter")](https://twitter.com/g0tmi1k "Twitter") [![Google Plus Profile](/images/social/google-plus.png "Google Plus")](http://plus.google.com/110108403609022118432 "Google Plus")

Copyright © 2009-2021 g0tmi1k