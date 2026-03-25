---
title: Detecting IP KVMs, (Tue, Mar 24th)
url: https://isc.sans.edu/diary/rss/32824
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-24
fetch_date: 2026-03-25T04:18:10.229899
---

# Detecting IP KVMs, (Tue, Mar 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32820)
* [next](/diary/32826)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Detecting IP KVMs](/forums/diary/Detecting%2BIP%2BKVMs/32824/)

**Published**: 2026-03-24. **Last Updated**: 2026-03-24 13:55:25 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Detecting%2BIP%2BKVMs/32824/#comments)

I have written about how to [use IP KVMs securely](https://isc.sans.edu/diary/32598), and recently, researchers at Eclypsium published yet another report on [IP KVM vulnerabilities.](https://eclypsium.com/blog/your-kvm-is-the-weak-link-how-30-dollar-devices-can-own-your-entire-network/) But there is another issue I haven't mentioned yet with IP KVMs: rogue IP KVMs. IP KVMs are often used by criminals. For example, North Koreans used KVMs to connect remotely to laptops sent to them by their employers. The laptops were located in the US, and the North Korean workers used IP KVMs to remotely connect to them. IP KVMs could also be used to access office PCs, either to enable undetected "work from home" or by threat actors who use them to gain remote access after installing the device on site.

IP KVMs usually connect to the system in two ways:

* USB for keyboard/mouse
* HDMI for the monitor connection (some older variants may also use VGA)

For my testing, I used two different IP KVMs. A "PiKVM" and a "NanoKVM" (Sipeed). Both were connected to Linux systems, but the techniques should work on other operating systems as well.

### USB

For the Sipeed NanoKVM, "lsusb" give away the device:

> $ lsusb
> Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
> Bus 001 Device 002: ID 0bda:c821 Realtek Semiconductor Corp. Bluetooth Radio
> Bus 001 Device 004: ID 051d:0002 American Power Conversion Uninterruptible Power Supply
> **Bus 001 Device 005: ID 3346:1009 sipeed NanoKVM**
> Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

PiKVM is a little bit less obvious, but this USB entry appears to be associated with PiVKM

> `Bus 001 Device 004: ID 1d6b:0104 Linux Foundation Multifunction Composite Gadget
> Bus 001 Device 017: ID 1b3f:2008 Generalplus Technology Inc. USB Audio Device`

This needs a bit more testing for the PiKVM.

### HDMI

HDMI devices send "EDID" (Extended Display Identification Data) to the system the display is connected to. The main purpose of EDID is to communicate available video modes and resolutions. But it also includes manufacturer information.

For the NanoKVM:

> `sudo get-edid | parse-edid
> ...
> Section "Monitor"
>         Identifier "Connector"
>         ModelName "Connector"
>         VendorName "VCS"
> ...`

Not very obvious, but the "VCS" vendor name could be a reasonable indicator (check for false positives)

For PiKVM, the "Identified" and "ModelName"  are more telling:

> `Section "Monitor"
>         Identifier "PiKVM V3"
>         ModelName "PiKVM V3"
>         VendorName "LNX"`

### Evasion

Of course, a more sophisticated attacker can modify these strings. PiKVM offers a configuration file to do so, in part to allow for better compatibility. I do not know whether the NanoKVM provides a similar, simple way to evade detection (but it is likely not terribly hard). So "sophisticated attacker" may translate to "able and willing to read the manual".

Many endpoint protection solutions monitor USB devices and may alert on odd devices being connected. But I am not aware of any that check monitor EDID strings. This may be another neat feature for any solutions. In office environments, most organizations provide a limited set of monitor types. For home office use, things may be more complex as users often connect their own monitors.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [ipvkm](/tag.html?tag=ipvkm)

[0 comment(s)](/diary/Detecting%2BIP%2BKVMs/32824/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32820)
* [next](/diary/32826)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)