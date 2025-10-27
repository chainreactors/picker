---
title: QUIC trickery
url: https://c-skills.blogspot.com/2025/05/quic-trickery.html
source: C-skills
date: 2025-05-02
fetch_date: 2025-10-06T22:27:21.431877
---

# QUIC trickery

[skip to main](#main)  |
[skip to sidebar](#sidebar)

# [C-skills](https://c-skills.blogspot.com/)

## Thursday, May 1, 2025

### QUIC trickery

Its probably lesser known that *OpenSSL* in their [recent 3.5.0 Beta](https://openssl-library.org/roadmap/index.html) version has added full support (client and server side) for TLS over QUIC.

[RFC9001](https://www.rfc-editor.org/rfc/rfc9001.html) runs the TLS messages - including handshake and anything - on top of the QUIC transport layer. This is somewhat exciting, as it means that - if you already have an *OpenSSL* infra - you can get QUIC support with relatively little effort into your app. So I went ahead and added QUIC support for [crash](https://github.com/stealth/crash). As roaming/mobility is not yet supported with *OpenSSL's* QUIC impl, so it is neither supported in crash. For roaming and suspend/resume you still use DTLS. But SOCKSing your connections through GfW with QUIC is working.

As a funny side-note, as the QUIC support within *OpenSSL* is pretty new, it would not have been possible to use AI coding agents to add support for it, as they could not have learnt about it yet. This kind of model-rot has implications about malware development and forensics which I am not yet digging into here.

Whats the benefits and drawbacks of using QUIC in general and where is the fun ahead?

QUIC itself effectively was designed for HTTP/3 - as a replacement for HTTP/1 and HTTP/2 over TCP. It runs on top of UDP and has its own ordering, reliability and security layer. Unlike DTLS, which does not offer reliability beyond the handshake.

One of the drawbacks for me is, that it requires a [minimum MSS of 1200](https://www.rfc-editor.org/rfc/rfc9000.html#name-datagram-size), which means that QUIC is **not a tunneling-friendly protocol**, since it requires a lot more effort to tunnel it across links with a lesser MTU, e.g. DNS or reduced NTP (Tier1 networks sometimes limit NTP pkt sizes). But of course you can tunnel other protos across QUIC.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyFsvXxV-xCh1oPm22PjSK_yl4DXwICykauq9_-W34xJgY5w6Oy-4kkmuzaFGM7gmn5XXPx21Matl8jYP8nntK6zfxPmnG8Q-ayfZLvbKM9CBRaNIRT2vkgLvWgV_ieOr4OTJHf9KDVKfLSkRq5V_yRNkgGOUfQBBAqIAy-OKoiiiYnkGaFsXtmKJV-KCL/w627-h230/b3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyFsvXxV-xCh1oPm22PjSK_yl4DXwICykauq9_-W34xJgY5w6Oy-4kkmuzaFGM7gmn5XXPx21Matl8jYP8nntK6zfxPmnG8Q-ayfZLvbKM9CBRaNIRT2vkgLvWgV_ieOr4OTJHf9KDVKfLSkRq5V_yRNkgGOUfQBBAqIAy-OKoiiiYnkGaFsXtmKJV-KCL/s1571/b3.jpg)

So, whats good about QUIC? It adds new attack surfaces from many sides: Implementation wise with many new software stacks that could potentially contain bugs as well as from protocol side since its not using TCP and therefore it is easier to spoof and confuse monitoring systems and firewalls. This brings me to the point that QUIC is an **exfiltration-friendly protocol**. As there basically is no notion of [IP:port] endpoint pairs but IPs and ports [can be floating](https://www.rfc-editor.org/rfc/rfc9000.html#name-connection-migration). It is much harder, if not impossible, to detect or supress UL/DL of large amounts of data between networks. As there is no network-level connection as with TCP, there is no connection that could be resetted and blocking only works for that particular [IP:port] pair, which is a moving target. Whats more, as QUIC does not require OS/Kernel support, it would be possible by malware to carry free-standing implementations and run it on the most ancient systems, if it just speaks UDP.

I will not dig further in the pro's and con's of QUIC and TLS-over-QUIC, since the nifty details should be reserved for paying customers. :)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhO3X5eeolyt8MqLLycyT9TI5Mu6kZhAowzukt1oTOPJELAK4RSFCp_b79oqjgsc-qJkRpF6zuEScZgpspxW7k1eXtBusFWJlhtrKRK03PGWEZqCqshUAYMwJi8sjDqextBJUew59OuCtPgscbEP0SJpbKSA8dq8o8fOIT3uJVOFBPeeV9ijWooIZ4iHfJ-/w623-h114/logo-black.jpg)](https://github.com/c-skills/welcome)

Posted by

[Sebastian](https://www.blogger.com/profile/11886596387140041622 "author profile")

at
[6:04 AM](https://c-skills.blogspot.com/2025/05/quic-trickery.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/3606809368389861108/8845240421986717571 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3606809368389861108&postID=8845240421986717571&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=8845240421986717571&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=8845240421986717571&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=8845240421986717571&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=8845240421986717571&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=8845240421986717571&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/3606809368389861108/8845240421986717571)

[Newer Post](https://c-skills.blogspot.com/2025/06/luajit-trickery.html "Newer Post")

[Older Post](https://c-skills.blogspot.com/2025/04/new-bridge-protocol-trickery.html "Older Post")
[Home](https://c-skills.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://c-skills.blogspot.com/feeds/8845240421986717571/comments/default)

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

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2F8845240421986717571%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2F8845240421986717571%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](https://c-skills.blogspot.com/feeds/8845240421986717571/comments/default)

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
* [Nion's blog](https://nion...