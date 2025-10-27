---
title: Largest Recorded DDoS Attack is 3.8 Tbps
url: https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html
source: Schneier on Security
date: 2024-10-08
fetch_date: 2025-10-06T18:53:47.169277
---

# Largest Recorded DDoS Attack is 3.8 Tbps

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

## Largest Recorded DDoS Attack is 3.8 Tbps

Cloudflare just blocked the current record DDoS attack: [3.8 terabits per second](https://blog.cloudflare.com/how-cloudflare-auto-mitigated-world-record-3-8-tbps-ddos-attack/). (Lots of good information on the attack, and DDoS in general, at the link.)

News [article](https://www.bleepingcomputer.com/news/security/cloudflare-blocks-largest-recorded-ddos-attack-peaking-at-38tbps/).

Tags: [denial of service](https://www.schneier.com/tag/denial-of-service/)

[Posted on October 7, 2024 at 7:02 AM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html) •
[9 Comments](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html#comments)

### Comments

Mark Johnson •
[October 7, 2024 7:13 AM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html/#comment-440967)

I think my numbers check out. WOW!

“A terabit is a multiple of the unit bit (b) for digital information or computer storage. The prefix tera (T) is defined in the International System of Units (SI) as a multiplier of 1012 (1 trillion, short scale), and therefore 1 terabit = 1012 bits = 1000000000000 bits = 1000 gigabits (Gb). The terabit is represented by the symbols Tbit and Tb.”

With 8 bits in a byte we have 1000000000000/8=125000000000 bytes (a byte is used to express 1 character of text).

Lexxica reports that the average page has 1800 characters (including spaces). So

125000000000/1800=15,625,000,000 (pages per Tb).

This attack was sending 3.8 times that PER SECOND (59,375,000,000 PAGES of content PER SECOND).

<https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html>

Clive Robinson •
[October 7, 2024 8:19 AM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html/#comment-440970)

I guess it’s not surprising that data rates on DDoS are,

“On the up and up”

Because two things are immediately obvious,

1, The performance / cost of hardware is rising rapidly

Whilst there are other factors to consider, these two appear to be in effect “runaway without control”.

Though how you would get effective control and reign things in is something that is not going to be easy to do.

Morley •
[October 7, 2024 11:48 AM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html/#comment-440973)

DDOS gives power to a few mitigation companies. I hope we have a solution via Internet infrastructure before IoT gets much bigger. I haven’t heard of that.

Clive Robinson •
[October 8, 2024 4:26 AM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html/#comment-440982)

@ Morley,

With regards,

> “I hope we have a solution via Internet infrastructure before IoT gets much bigger”

Simple answer is we don’t.

The reason is the IP protocols are packet based and designed to “route around damage”.

Blocking traffic to a destination is seen as “damage” by the upstream nodes towards the source. So they try to re-route. Thus you still get a flood of traffic.

The “correct way” to stop such traffic is with TCP to quench the connection request –send RST– but that does not work with UDP. But to distinguish what should or should not be quenched takes a lot of CPU cycles, and in theory and practice can only be reliably done by the destination host.

What is being done is to create a virtual or ghost networks where backbone routers close to the source get told to fake a response from the host. This does not stop the DDoS attack but sweeps much of it into a bit bucket off of the real network thus diminishing it’s effects.

The problem is the attacker has agency and can try different things to get around blocks. But the setting up of blocks is both reactive and takes time, which gives an attacker a time window to achieve their objective.

A past suggestion has been to make the “connection” phase expensive to the source. But as with Spam Email such suggestions do not work as the attacker is using other peoples resources thus does not see the cost etc.

Each potential preventative measure you look at almost always ends up causing some kind of harm that directly or indirectly achieves the attackers aim.

The only way to reliably limit DDoS attacks is “perfect security” on host systems such that an attacker can not subvert them into what are “Bot nets”.

Homer Beard •
[October 8, 2024 11:32 AM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html/#comment-440993)

As a corollary to what Clive wrote, internet access is getting cheaper just as hardware is. Even people in traditionally deprived areas, such as the USA, are starting to get good connections.

Mark’s numbers make this sound like a crazy amount of data, but it actually only requires about 4000 compromised devices—if they’re on gigabit connections, and are evenly distributed so as not to be sharing bandwidth. Think of your “favorite” terrible and insecure internet-of-things device. If they’ve been sold in the tens of thousands, they’re ready to be turned into a bot-net for attacks just like this one.

I think we need some sort of distributed filtering feature for stuff like this, in which each router could ask an upstream router to stop sending it packets matching some criteria. Of course, doing that insecurely would lead to its own problems, but we do have ways to prove ownership of internet protocol addresses.

[Jesse Thompson](https://www.lightsecond.com) •
[October 8, 2024 4:04 PM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html/#comment-441001)

DDoS is also a technique used *by* at least some mitigation companies to create a problem they are then magically able to sell solutions for.

I don’t have data on whether or not Cloudflare directly practices anything like that, but I *have* caught at least one provider I am not at liberty to name in the act before.

Homer Beard •
[October 8, 2024 8:05 PM](https://www.schneier.com/blog/archives/2024/10/largest-recorded-ddos-attack-is-3-8-tbps.html/#comment-441007)

Clive wrote:

> The “correct way” to stop such traffic is with TCP to quench the connection request –send RST– but that does not work with UDP.

It doesn’t work with TCP either, unless the remote end is “playing nicely”. Maybe they are, like if the flaw used to create the bot-net leaves the TCP stack un-exploited, or if some external device enforces it. I recall seeing some proposal, long ago, for on-path routers to drop traffic (for a while) in response to such things; I’m not aware of anything like that ever being widely implemented.

For now, a victim can ignore the traffic, or send all the TCP RSTs or ICMP errors they like, and it won’t change a thing about IP datagram routability. The attacker can often ignore that s...