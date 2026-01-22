---
title: Hacking Wheelchairs over Bluetooth
url: https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html
source: Instapaper: Unread
date: 2026-01-21
fetch_date: 2026-01-22T03:36:46.416345
---

# Hacking Wheelchairs over Bluetooth

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Hacking Wheelchairs over Bluetooth

Researchers have [demonstrated](https://www.securityweek.com/researchers-expose-whill-wheelchair-safety-risks-via-remote-hacking/) remotely controlling a wheelchair over Bluetooth. CISA has issued an [advisory](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-25-364-01).

> CISA said the WHILL wheelchairs did not enforce authentication for Bluetooth connections, allowing an attacker who is in Bluetooth range of the targeted device to pair with it. The attacker could then control the wheelchair’s movements, override speed restrictions, and manipulate configuration profiles, all without requiring credentials or user interaction.

Tags: [Bluetooth](https://www.schneier.com/tag/bluetooth/), [hacking](https://www.schneier.com/tag/hacking/), [Internet of Things](https://www.schneier.com/tag/internet-of-things/), [transportation](https://www.schneier.com/tag/transportation/)

[Posted on January 14, 2026 at 2:22 PM](https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html) •
[10 Comments](https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html#comments)

### Comments

lurker •
[January 14, 2026 3:32 PM](https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html/#comment-451320)

Theo was right, again …

Not Really Anonymous •
[January 14, 2026 4:58 PM](https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html/#comment-451321)

Being able to hack wheelchairs as delivered is a good thing. The companies leasing / selling them screw over their customers and being able to work around the DRM to fix things is good.

Clive Robinson •
[January 14, 2026 6:01 PM](https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html/#comment-451322)

@ lurker,

With regards,

> “Theo was right, again…”

Not just Theo, several others myself included have made comment on the lack of security mechanisms in “Industrial Control Systems”(ICS) including “Remote Telemetry Units”(RTUs) and “Supervisory Control And Data Acquisition”(SCADA) systems and very importantly the “open and insecure” communications between them, the sensors and actuators and the overall command systems from the SCADA systems and operators.

It worried me greatly when the latter got moved by “accountants” to the Internet. And some Governments actually woke up to this eventually and insisted on higher levels of communications and access systems, but by no means all. As for the lower level comunications some of which got piped across 2G GSM paths again with no security you might want to avoid construction sites and railway yards for the foreseeable future if not indefinitely.

The major issue is the “don’t roll your own” mantra that appears to have become an inviolable rule throughout the ISC and Embedded device design cultures as “no security”. Which is unfortunate as Engineers like “Simple thus easily tested” interfaces and test harnesses which are basically just old fashioned RS232 or RS422 hardware and ASCII characters from the very early 1960’s TTY style data comms,

<https://ipc2u.com/articles/knowledge-base/the-main-differences-between-rs-232-rs-422-and-rs-485/>

Which might have structured plaintext like XML with occasionally added checksums and error correction, but certainly not secured in any way (not even plaintext logins and passwords…).

But the “Embedded Systems” cover a variety of sins and securty wise just as bad if not worse. You find these in just about everything that is not PC/Mainframe Computer networking. So infrastructure systems including ICS but also Smart Meters etc, Medical implants and much else with an expected 20-50year burried out of sight lifetime. And… because they are “embedded” the old Masked ROM ethos gets carried forward with mostly the software not get upgraded or patched in any way… Which from a security aspect is appalling…

Back last century it was accepted that development would take a year to 18months for simple systems due to the amount of engineering time devoted to “test” because of the vast expense a simple mistake or error would cause. But the introduction of EEPROM and Flash whilst bringing the cost of errors/omissions down significantly ment that Senior Management could push through more complex designs and significantly reduced test time. This was made worse by the notions of the upstream “edge devices” and down stream “Internet of Things”(IoT) devices “just hung on the network”. With in effect Zero Security Testing and actually minimal at best functional test.

I made noises about not letting such crap into the world as it was guarenteed to be a security nightmare (and so it has been with “Distributed Denial of Service”(DDoS) attacks being the most obvious.

I even argued that NIST should stop doing what had in effect become “vanity crypto competitions” and do something usefull like “security frameworks” for infrastructure, embedded, implanted and IoT and Edge Device systems such that security updates would be part of standard operating thus making us all safer. You should have heard some of the vilifying comments… Basically manufacturing managment saw “mistakes” as a way to sell more product…

However when challenged they would get quite nasty and attack not on technical and security merit but by using “cancel culture” style techniques.

But ask yourself a question,

“If I have a medical device that could kill me implanted, say a pacemaker, how secure do I want it to be?”

And,

“Do I want them cracking my chest open just to put in a software upgrade?”

Like a bunch of psychopaths running an asylum they did not want such questions being asked because of the issues of profit and liability…

So your pacemaker has a more than reasonable chance of being “less secure” than this wheelchair…

lurker •
[January 14, 2026 8:13 PM](https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html/#comment-451323)

@Clive Robinson, ALL

There was a discussion 5 years ago on y-combinator about why OpenBSD has no Bluetooth support. Some people admitted to using usb dongles that presented to the OS as a soundcard, supposedly isolating all the BT risks. An anonymous user summed it up as

“Bluetooth has unfixable security risks baked into the protocol, it’s ideal for OpenBSD to ignore it.”

Clive Robinson •
[January 14, 2026 9:09 PM](https://www.schneier.com/blog/archives/2026/01/hacking-wheelchairs-over-bluetooth.html/#comment-451324)

@ lurker, ALL,

With Regards,

> “Bluetooth has unfixable security risks baked into the protocol, it’s ideal for OpenBSD to ignore it.”

It’s not just Bluetooth with “unfixable security risks baked [in]”

In fact nearly all comms protocols have issue from the physical wires all the way up.

For instance take data diodes and the like they are supposed to be “one way” to “isola...