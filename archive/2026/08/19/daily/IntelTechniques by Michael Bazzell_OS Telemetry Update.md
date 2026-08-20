---
title: OS Telemetry Update
url: https://inteltechniques.com/blog/posts/telemetryupdate.html
source: IntelTechniques by Michael Bazzell
date: 2026-08-19
fetch_date: 2026-08-20T02:56:37.357379
---

# OS Telemetry Update

[# IntelTechniques](../../index.html)

* [Training](../../training.html)
* [Services](../../services.html)
* [Resources](../../links.html)
* [Tools](../../tools/index.html)
* [Blog](../../blog/)
* [Magazine](https://unredactedmagazine.com)
* [Books](../../books.html)
* [Contact](../../contact.html)

#### OS Telemetry Update

---

Shortly after publishing the [OS Telemetry Guide](https://inteltechniques.com/2026.telemetry.html), we received a lot of feedback. A lot. There were two concerns. First, when enabling telemetry in order to update, would all of the locally-stored telemetry be delivered, making the protections useless? Second, many people asked why we excluded Linux from our guide. Let's tackle both.

The Linux response is easy. Linux does not natively collect much telemetry. Many distributions collect none at all. There is no central repository snooping on your daily activity. Therefore, we have no recommended DNS block list for Linux in general. If you are concerned, we recommend a software firewall such as Open Snitch instead of DNS filtering.

The other concern is more complicated. Yes, enabling all connections to Apple or Microsoft does open the flood gates for telemetry delivery, but not the way you might think. If you never use Apple's Music, News, Photos, or other stock applications, there is no telemetry to deliver. If you use those apps but have not opened them since the last reboot, much of the logs have been purged. If you are following our previous guides on purging logs, even less is stored (and transmitted). This is why I insist on only applying updates after a reboot with everything closed. Also, if you have no Apple account associated with the macOS device, there is no account to store all of the details. The general idea was to block the non-stop sending of data every minute to Apple or Microsoft and only allow connection when we need something from them. However, I respect the concerns and agree that opening the flood gates is not ideal.

Therefore, let's modify things a bit. When attempting to update macOS with DNS filtering set to block all connections, I can see in the DNS logs that things are working as desired.

![](../images/te01.png)

I can also see that the updates were blocked.

![](../images/te02.png)

If I disabled all blocking, it should all work fine but would leak out too much data. Instead, I applied the following to my "Allowlist" within NextDNS.

![](../images/te03.png)

These are the bare minimum connections required to allow Apple to update macOS without openeing every connection on the domain. We are blocking every connection to apple.com but allowing swdist.apple.com (software distribution). These specific domains are related to updates and would not send telemetry based on applications such as News, Photos, Music, etc. After enabling these, I attempted updates again.

![](../images/te04.png)

Everything worked and I allowed my machine to update. When complete, I simply disabled each rule but left them in the Allowlist for future use.
![](../images/te05.png)

This could be replicated for Windows by watching your NextDNS logs while attempting an update. It takes a bit of trial and error, but should be straight-forward. However, both Apple and Microsoft constantly tweak these connections so expect failure at some point. When that happens, simply repeat the process and see what changed, adding the new domain to your Allowlist.

#### RSS Feed

---

Subscribe to our RSS feed:

https://inteltechniques.com/blog/rss.xml

#### Privacy Book

---

Our latest (5th Edition) book on Extreme Privacy is now available. Click [HERE](../../book7.html) for details.
[![](../../img/EP5-3D.png)](../../book7.html)

[Buy the Book](../../book7.html)

* Copyright © 2009-2026 IntelTechniques.com
* All Rights Reserved
* [Privacy Policy](../../privacy.html)