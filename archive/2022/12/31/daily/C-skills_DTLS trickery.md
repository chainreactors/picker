---
title: DTLS trickery
url: https://c-skills.blogspot.com/2022/12/dtls-trickery.html
source: C-skills
date: 2022-12-31
fetch_date: 2025-10-04T02:46:39.789924
---

# DTLS trickery

[skip to main](#main)  |
[skip to sidebar](#sidebar)

# [C-skills](https://c-skills.blogspot.com/)

## Friday, December 30, 2022

### DTLS trickery

Probably the last post in 2022.

I fixed *SOCKS5* handling in [psc](https://github.com/stealth/psc) and [crash](https://github.com/stealth/crash) so that it is now possible to use it with *curl* and IPv6. Also added **DTLS** (read: **TLS** over **UDP**) support for *crash* in order to make it possible to use anti censorship *SOCKS* proxies in countries that block outgoing **TCP** connections such as in Iran (see previous post).

When I read about *LibreSSL* having **QUIC** support, I tried to use this, but their bold announcement was a spoiler. They only "support" the **QUIC** handshake to obtain keying materials by means of **TLS** integration. I wouldn't really call this "QUIC support", although I love *LibreSSL* much more than *OpenSSL* (due to their permanent API changes). As **DTLS** has only reliability for its handshake, I had to add my own TCP-style data flow mechanisms to handle packet loss and re-orders. *OpenSSL* also wants to add **QUIC** support, so lets see in a couple of years how far this goes (hopefully with full proto and API support and not just the handshake) to finally have a usable **QUIC** lib.

*Crash* also switched from **TLS** v1.2 to v1.3 being mandatory, i.e. it is not proto compatible to the 2.x versions anymore. As soon as **DTLS** v1.3 will be widely deployed, it will also switch to **DTLS** v1.3. Due to all these new features and compat things the crash-3 versions are dubbed experimental (although working stable).

Wish you a nice rest of 2022 and a Guten Rutsch for 2023!

Posted by

[Sebastian](https://www.blogger.com/profile/11886596387140041622 "author profile")

at
[2:37 AM](https://c-skills.blogspot.com/2022/12/dtls-trickery.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/3606809368389861108/1839359451887080540 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3606809368389861108&postID=1839359451887080540&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=1839359451887080540&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=1839359451887080540&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=1839359451887080540&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=1839359451887080540&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=1839359451887080540&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/3606809368389861108/1839359451887080540)

[Newer Post](https://c-skills.blogspot.com/2023/01/tunneling-trickery.html "Newer Post")

[Older Post](https://c-skills.blogspot.com/2022/11/sni-trickery.html "Older Post")
[Home](https://c-skills.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://c-skills.blogspot.com/feeds/1839359451887080540/comments/default)

## Where ya from

## Subscribe To

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](https://c-skills.blogspot.com/feeds/posts/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2F1839359451887080540%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2F1839359451887080540%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](https://c-skills.blogspot.com/feeds/1839359451887080540/comments/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

## Like c-skills' projects?

![](https://www.paypalobjects.com/de_DE/i/scr/pixel.gif)

## Links/Rechts

* [this](http://c-skills.blogspot.com/)
* [my github](http://github.com/stealth)
* [follow me on twitter](http://twitter.com/steaith)
* [MTU Ninja blog](https://vincent.bernat.ch/en/blog)
* [Geoff Hustons network blog](https://www.potaroo.net/)
* [bits please](https://bits-please.blogspot.de/)
* [my aimful life](http://blog.cr4.sh/)
* [GDR crypto archive](http://scz.bplaced.net)
* [communists computers](https://eser-ddr.de)
* [Top Level Telcos](https://electrospaces.blogspot.com)
* [Kees' codeblog](http://www.outflux.net/blog/)
* [jeffrey carr on cyberwar](https://jeffreycarr.blogspot.com)
* [Nion's blog](https://nion.modprobe.de/blog/)
* [packet foo](https://blog.packet-foo.com/)
* [grugq's hacker opsec](https://grugq.github.io/)
* [c++ blog](https://isocpp.org/blog)
* [frama-C blog](http://blog.frama-c.com/)
* [lcamtuf's](https://lcamtuf.coredump.cx/)
* [Harld Welte's blog](https://laforge.gnumonks.org/weblog/)
* [openbts chronicles](https://openbts.blogspot.de/)
* [google security blog](https://security.googleblog.com)
* [nerdling sapple](https://blog.zx2c4.com/)
* [home.regit.org](https://home.regit.org/)
* [root labs rdist](https://rdist.root.org/)
* [xorl %eax, %eax](https://xorl.wordpress.com/)
* [Trail of Bits](https://trailofbits.com/)
* [Julien's blog](https://blog.cr0.org/)
* [ithilgore's blog](https://sock-raw.org/blog/)
* [Openwall Project](https://openwall.com/)
* [trapkit](https://trapkit.de/)
* [pagetable.com](https://pagetable.com/)
* [grsecurity](https://grsecurity.net/)
* [recurity lablog](https://blog.recurity-labs.com/)
* [Halvars blog](https://addxorrol.blogspot.com/)
* [OSS Security Wiki](https://oss-security.openwall.org/wiki/)
* [Modern C++ stories](https://www.cppstories.com/p/start-here/)
* [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
* [phoronix news](https://www.phoronix.com/)
* [coindesk](https://www.coindesk.com/)
* [distrowatch](https://distrowatch.com/)
* [Fefe's blog](https://blog.fefe.de)

## Blog Archive

* ►
  [2025](https://c-skills.blogspot.com/2025/)
  (4)
  + ►
    [June](https://c-skills.blogspot.com/2025/06/)
    (1)
  + ►
    [May](https://c-skills.blogspot.com/2025/05/)
    (1)
  + ►
    [April](https://c-skills.blogspot.com/2025/04/)
    (1)
  + ►
    [February](https://c-skills.blogspot.com/2025/02/)
    (1)

* ►
  [2024](https://c-skills.blogspot.com/2024/)
  (3)
  + ►
    [September](https://c-skills.blogspot.com/2024/09/)
    (1)
  + ►
    [March](https://c-skills.blogspot.com/2024/03/)
    (2)

* ►
  [2023](https://c-skills.blogspot.com/2023/)
  (6)
  + ►
    [December](https://c-skills.blogspot.com/2023/12/)
    (1)
  + ►
    [November](https://c-skills.blogspot.com/2023/11/)
    (1)
  + ►
    [September](https://c-skills.blogspot.com/2023/09/)
    (1)
  + ►
    [July](https://c-skills.blogspot.com/2023/07/)
    (1)
  + ►
    [March](https://c-skills.blogspot.com/2023/03/)
    (1)
  + ►
    [January](https://c-skills.blogspot.com/2023/01/)
    (1)

* ▼
  [202...