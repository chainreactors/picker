---
title: New Attack Against Wi-Fi
url: https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html
source: Schneier on Security
date: 2026-03-09
fetch_date: 2026-03-10T04:04:00.727276
---

# New Attack Against Wi-Fi

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

## New Attack Against Wi-Fi

It’s called [AirSnitch](https://arstechnica.com/security/2026/02/new-airsnitch-attack-breaks-wi-fi-encryption-in-homes-offices-and-enterprises/):

> Unlike previous Wi-Fi attacks, AirSnitch exploits core features in Layers 1 and 2 and the failure to bind and synchronize a client across these and higher layers, other nodes, and other network names such as SSIDs (Service Set Identifiers). This cross-layer identity desynchronization is the key driver of AirSnitch attacks.
>
> The most powerful such attack is a full, bidirectional [machine-in-the-middle (MitM) attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), meaning the attacker can view and modify data before it makes its way to the intended recipient. The attacker can be on the same SSID, a separate one, or even a separate network segment tied to the same AP. It works against small Wi-Fi networks in both homes and offices and large networks in enterprises.
>
> With the ability to intercept all link-layer traffic (that is, the traffic as it passes between Layers 1 and 2), an attacker can perform other attacks on higher layers. The most dire consequence occurs when an Internet connection isn’t encrypted­—something that Google [recently estimated](https://transparencyreport.google.com/https/overview) occurred when as much as 6 percent and 20 percent of pages loaded on Windows and Linux, respectively. In these cases, the attacker can view and modify all traffic in the clear and steal authentication cookies, passwords, payment card details, and any other sensitive data. Since many company intranets are sent in plaintext, traffic from them can also be intercepted.
>
> Even when HTTPS is in place, an attacker can still intercept domain look-up traffic and use DNS cache poisoning to corrupt tables stored by the target’s operating system. The AirSnitch MitM also puts the attacker in the position to wage attacks against vulnerabilities that may not be patched. Attackers can also see the external IP addresses hosting webpages being visited and often correlate them with the precise URL.

Here’s the [paper](https://www.ndss-symposium.org/ndss-paper/airsnitch-demystifying-and-breaking-client-isolation-in-wi-fi-networks/).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [man-in-the-middle attacks](https://www.schneier.com/tag/man-in-the-middle-attacks/), [Wi-Fi](https://www.schneier.com/tag/wi-fi/)

[Posted on March 9, 2026 at 6:57 AM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html) •
[7 Comments](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html#comments)

### Comments

AlexT •
[March 9, 2026 9:36 AM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html/#comment-452737)

Interisting one.

Just skimmed the paper but does it necessitate specialzed hardware?

Clive Robinson •
[March 9, 2026 9:57 AM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html/#comment-452740)

@ AlexT,

Like you, I’ve only had a brief look through the paper.

That said, the conclusion is quite short and the latter part of,

> “*We*“

Is quite revealing in what it says, in that it basically portraits all parts of the design process as not what they could or should have been for a robust and secure system…

Bernie •
[March 9, 2026 10:04 AM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html/#comment-452741)

A quick note: Just below the article on Ars are a few highlighted comments that help explain things. If you read the article, make sure you scroll down past its end for those comments.

Peter A. •
[March 9, 2026 11:30 AM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html/#comment-452743)

Do I understand correctly that this attack applies only after a rogue device is already authenticated and allowed on the network (SSID), such as an a known-password “guest” or “public” WiFi, or when it has been provided, guessed or cracked the password, and only after that the attacker is able to MiTM traffic to/from other devices on the same SSID?

Rontea •
[March 9, 2026 1:14 PM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html/#comment-452745)

AirSnitch is another reminder that the foundations of our wireless networking stack are far weaker than we’d like to believe. Attacks like this don’t rely on breaking WPA3 encryption directly—they exploit the trust assumptions baked into the hardware and firmware that implement Wi-Fi. Client isolation, a feature that was supposed to keep devices safely siloed, is now demonstrably unreliable.

Defense against AirSnitch isn’t about a single patch. It’s about layered mitigations:

1. Update your infrastructure – Apply firmware updates from your router vendors immediately, even if they only partially address the issue.
2. Segment and monitor your network – Treat Wi-Fi as an untrusted medium. Use VLANs, network segmentation, and active monitoring to detect unusual traffic between clients.
3. Use end-to-end encryption – TLS, VPNs, and encrypted protocols remain your best defense against traffic interception.
4. Consider zero-trust principles – Don’t rely on client isolation or SSID separation alone. Assume the network can be compromised and authenticate at higher layers.

Ultimately, AirSnitch reinforces a point we’ve seen before: security bolted onto inherently insecure protocols will always be fragile. Long-term solutions require redesigning the underlying systems, not just patching the symptoms.

Clive Robinson •
[March 9, 2026 4:20 PM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html/#comment-452750)

@ ALL,

For those trying to read either the ARS article or the paper you first need to understand the notion of

1, A class of attacks.
2, Instances of attacks in a class.

The paper is about both… And thus so is the article. That is it’s about several different instances of attacks in a general class, all interoperating.

Thus the key bit in the ARS article is,

> “*The isolation can effectively be nullified through AirSnitch, the name the researchers gave to **a series of attacks that capitalize on the newly discovered weaknesses**.*“

Note the plurals “attacks” and “weaknesses”

You also need to understand what happens with network,

1, Bridges
2, Switches
3, Routers

And what layers they do or do not operate at.

Worse that networks can be layered on top of each other. That is in normal use people get taught about a physical layer and assume it is the “base layer” often not realising or considering that it could be another high level network like X25 or another routed IP network. Or it could be another “implicit network” like having three different frequency 2.5GHz / 5.0GHz / 6.0GHz interfaces in the same “Access Point”(...