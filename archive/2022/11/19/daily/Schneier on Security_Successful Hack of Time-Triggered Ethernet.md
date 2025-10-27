---
title: Successful Hack of Time-Triggered Ethernet
url: https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html
source: Schneier on Security
date: 2022-11-19
fetch_date: 2025-10-03T23:15:07.686807
---

# Successful Hack of Time-Triggered Ethernet

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

## Successful Hack of Time-Triggered Ethernet

Time-triggered Ethernet (TTE) is used in spacecraft, basically to use the same hardware to process traffic with different timing and criticality. Researchers have [defeated it](https://arstechnica.com/information-technology/2022/11/researchers-break-security-guarantees-of-tte-networking-used-in-spacecraft/):

> On Tuesday, researchers [published findings](https://web.eecs.umich.edu/~barisk/public/pcspoof.pdf) that, for the first time, break TTE’s isolation guarantees. The result is PCspooF, an attack that allows a single non-critical device connected to a single plane to disrupt synchronization and communication between TTE devices on all planes. The attack works by exploiting a vulnerability in the TTE protocol. The work was completed by researchers at the University of Michigan, the University of Pennsylvania, and NASA’s Johnson Space Center.
>
> “Our evaluation shows that successful attacks are possible in seconds and that each successful attack can cause TTE devices to lose synchronization for up to a second and drop tens of TT messages—both of which can result in the failure of critical systems like aircraft or automobiles,” the researchers wrote. “We also show that, in a simulated spaceflight mission, PCspooF causes uncontrolled maneuvers that threaten safety and mission success.”

Much more detail in the article—and the [research paper](https://web.eecs.umich.edu/~barisk/public/pcspoof.pdf).

Tags: [cyberattack](https://www.schneier.com/tag/cyberattack/), [embedded systems](https://www.schneier.com/tag/embedded-systems/), [hardware](https://www.schneier.com/tag/hardware/), [spoofing](https://www.schneier.com/tag/spoofing/)

[Posted on November 18, 2022 at 10:04 AM](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html) •
[7 Comments](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html#comments)

### Comments

Kent England •
[November 18, 2022 11:14 AM](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html/#comment-412619)

Does anyone remember the battle between Ethernet and Token Ring? One so-called advantage of token ring was a predictable response time to messages. This was allegedly to prevent factory robots from killing humans. More intelligent designers moved the safety protocol into the robot to avoid network failures. Wonder why NASA didn’t remember any of these old lessons?

lurker •
[November 18, 2022 1:02 PM](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html/#comment-412625)

ARP poisoning and EMI – sheesh. When did they stop schools teaching how to mitigate these?

Clive Robinson •
[November 18, 2022 2:23 PM](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html/#comment-412629)

@ ALL,

The problem arises because TTE does something incredibly dumb.

It takes an existing and well established technology that has a “channel” (MAC destination address) that has no “in-band-signalling” and forces it to have “in-band-signalling” (Two fields TTE specific fields of, Critical Trafic Marker and Virtual Link ID). BUT lays no requirment on equipment designed with the existing protocols of “no in-band-signalling” to be upgraded to “With in-band-signalling” so the stable door is left open.

I’ve discussed in-band-signaling and out-of-band-signalling[1] on this blog a number of times in the past and highlighted a number of issues that arise. Overloading an established specification without requiring all parts of a system to recognise the overload is a fairly obvious and basic mistake.

The fact the TTE spec alows this is realy stupid as it’s a know way for vulnerabilities to occure thus exploits to happen.

In this case the little “pinch of magic” used to exploit it is something else I’ve discussed on this blog in the past and it’s “EM Active Fault Injection” that I discovered and researched back in the 1980’s to attack the likes of electronic wallets and pocket gambling machines. I’ve even described how to get signals to get from wire to wire inside a shielded and supposadly issolated piece of equipment…

Fun side note : The self oscilating single transistor circuit they show, I used back in 1977 to make what you might call a “light-saber”. I’d originally used a relay wired in self oscilating mode and an autotransformer that I’d made as a highly illegal “Spark Gap Transmitter” but it sucked power from the bateries. I made the saber using the rubber handle from a wheel barrow and a three foot fluorescent tube –instead of the spark gap– with a thin return wire running down the outside of the tube I glued in place with my then favourit glue “evostic”, and then slid a clear plastic tube over the florescent tube (obtained from Transalantic Plastics in Surbiton). As it was a very high voltage there was no real current so I used 40AWG wire. Also because the tube was “directly struck” I did not have to use the heater wires, so it would not burn out. My fellow students at school thought it was rather good, not so the physics master a Mr Mugglton who realised it’s “high-voltage stops heart” potential, as well as the RF noise it generated wiped out near by radios and took the Victorian attitude of “We are not amused”.

[1] The simplest examples most programmers know are “C-Strings” that use 0x00 for inband signalling to indicatecthe end of a string and “Pascal-Strings” that use an out of string byte that has the stringlength in it. Some also know the nightmares that occure with C-strings when that inband signal gets misused or lost by a bit flip etc. It’s the basis of many serialization issues resulting in errors that are infact vulnerabilities that then only require an exploit to be developed ranging from an annoying denial of service attack to a full take over…

Sumadelet •
[November 19, 2022 6:00 PM](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html/#comment-412694)

@Clive Robinson

SpaceLifeForm •
[November 19, 2022 7:08 PM](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html/#comment-412696)

@ Sumadelet, Clive

<https://xkcd.com/2700/>

Funny. Good one.

Input sanitation can be tricky when using different libraries or scripted filters that are not on the same page with regard to the rules.

Clive Robinson •
[November 19, 2022 8:55 PM](https://www.schneier.com/blog/archives/2022/11/successful-hack-of-time-triggered-ethernet.html/#comment-412703)

@ SpaceLifeForm, Sumadelet,

Meanwhile over on,

‘https://www.explainxkcd.com/wiki/index.php/2700:\_Account\_Problems

It appears a couple of troll types are dukeing it out trying to prove one is a better neo-trash than the other…

Mind you, with regard to the cartoon, I do feel sorry for “ponytail” I’ve said ...