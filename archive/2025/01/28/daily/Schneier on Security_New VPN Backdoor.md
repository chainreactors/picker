---
title: New VPN Backdoor
url: https://www.schneier.com/blog/archives/2025/01/new-vpn-backdoor.html
source: Schneier on Security
date: 2025-01-28
fetch_date: 2025-10-06T20:25:46.130424
---

# New VPN Backdoor

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

## New VPN Backdoor

A newly discovered [VPN backdoor](https://arstechnica.com/security/2025/01/backdoor-infecting-vpns-used-magic-packets-for-stealth-and-security/) uses some interesting tactics to avoid detection:

> When threat actors use backdoor malware to gain access to a network, they want to make sure all their hard work can’t be leveraged by competing groups or detected by defenders. One countermeasure is to equip the backdoor with a passive agent that remains dormant until it receives what’s known in the business as a “magic packet.” On Thursday, researchers revealed that a never-before-seen backdoor that quietly took hold of dozens of enterprise VPNs running Juniper Network’s Junos OS has been doing just that.
>
> J-Magic, the tracking name for the backdoor, goes one step further to prevent unauthorized access. After receiving a magic packet hidden in the normal flow of TCP traffic, it relays a challenge to the device that sent it. The challenge comes in the form of a string of text that’s encrypted using the public portion of an RSA key. The initiating party must then respond with the corresponding plaintext, proving it has access to the secret key.
>
> The lightweight backdoor is also notable because it resided only in memory, a trait that makes detection harder for defenders. The combination prompted researchers at Lumin Technology’s Black Lotus Lab to sit up and take notice.
>
> […]
>
> The researchers found J-Magic on [VirusTotal](https://www.virustotal.com/gui/home/upload) and determined that it had run inside the networks of 36 organizations. They still don’t know how the backdoor got installed.

Slashdot [thread](https://tech.slashdot.org/story/25/01/24/0039249/backdoor-infecting-vpns-used-magic-packets-for-stealth-and-security).

EDITED TO ADD (2/1): Another [article](https://www.theregister.com/2025/01/25/mysterious_backdoor_juniper_routers/).

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [malware](https://www.schneier.com/tag/malware/), [VPN](https://www.schneier.com/tag/vpn/)

[Posted on January 27, 2025 at 7:02 AM](https://www.schneier.com/blog/archives/2025/01/new-vpn-backdoor.html) •
[14 Comments](https://www.schneier.com/blog/archives/2025/01/new-vpn-backdoor.html#comments)

### Comments

zajic •
[January 27, 2025 8:36 AM](https://www.schneier.com/blog/archives/2025/01/new-vpn-backdoor.html/#comment-442675)

I wonder if regularly rebooting network devices helps in this case – since if it got infected in the first place, it probably won’t be too much of a hassle to reinfect it again?

lurker •
[January 27, 2025 12:48 PM](https://www.schneier.com/blog/archives/2025/01/new-vpn-backdoor.html/#comment-442676)

“They still don’t know how the backdoor got installed.”

When they find out, come back to us with the real story. cd00r has been around for a while now, but it looks like it has been ignored by those who will be affected by it.

Me •
[January 27, 2025 1:09 PM](https://www.schneier.com/blog/archives/2025/01/new-vpn-backdoor.html/#comment-442677)

How long before malware requires captchas to submit these responses so that cracking cannot be automated?

Clive Robinson •
[January 27, 2025 4:45 PM](https://www.schneier.com/blog/archives/2025/01/new-vpn-backdoor.html/#comment-442678)

@ ALL,

On the face of it as given this is just an upgrade of “knock codes”.

Back before electronic communications people would knock on closed and defended doors in a way that gave a crude method of identification by the “rat-a-tat-tat” which developed into an “Identification Friend or Foe”(IFF) with another knock code response. As such a joke version is the “shave and a haircut”,

<https://en.m.wikipedia.org/wiki/Shave_and_a_Haircut>

This idea became the notion behind “port knocking” as a way to start a service on an IP based network. A series of effectively “null packets” would be sent in a time based pattern. If the pattern was approximately right the service behind a given port would be enabled for a short while (sometimes only to the originating address of the “knocker”). Thus in effect from 20,000ft a two stage process,

1, Identify and verify

Here we see an identification stage made rather more complex, but essentially the process is the same.

The use of PubKey to do this sort of thing is not new, and it’s been discussed on this blog before in a more secure form.

Crudely for understanding only, the authentication step is,

The service “Requester” sends a “nonce+ID” and it’s PubKey to the service “Provider” under the service “provider” “covert PubKey” (in effect a “shared secret”). The service “Provider” returns “a modified version of the “Requester” nonce and a symmetric encryption key” that is encrypted under the “requester” PubKey (or similar). From that point on much more efficient symetric encryption can be used.

The fact this has now been “seen in the wild” a decade later is curious, and thus sparks the question,

“Why Now?”

Or more involved,

“What has changed in the attack domain to warrant the extra effort?”

I’m thinking that,

> *“… they want to make sure all their hard work can’t be leveraged by competing groups or detected by defenders.”*

Is not only “too pat” an explanation it’s also incorrect. Defenders will see such “in bound packets” from the external communications network, if they are even half way competent.

The fact they might not be able to do anything with it, does not mean they cannot see it and act on it.

Think on it in the same way you would the difference between “cryptanalysis” and “Traffic Analysis”…

Hence the comment,

> *“After receiving a magic packet hidden in the normal flow of TCP traffic, it relays a challenge to the device that sent it.”*

But “hidden in the normal flow” is actually insufficient if the defenders are actually instrumenting correctly.

Which is where I suspect,

> *‘[T]he researchers wrote. “The combination of targeting Junos OS routers that serve as a VPN gateway and deploying a passive listening in-memory only agent, makes this an interesting confluence of tradecraft worthy of further observation.”‘*

It’s not said, but there is a reason the “routers” are being targeted only. Put simply few defenders instrument the external side of their “Gateway Router”, for various reasons it’s not that easy to do.

It has a similar advantage to the NSA occupying the “first upstream router” from the target. In that in nearly all cases the “target” “can not see the wire” thus “instrument the communications” there.

However there is another reason the NSA went for the “upstream router”, and you can see why with,

> *“The lightweight backdoor is also notable because it resided only in memory, a trait that makes detection harder for defenders.”*

Yes and no… PubKey encryption is CPU cycle heavy and thus produces a fairly visible “Power Spectrum” that can be spotted by fairly simple techniques and correlated with incoming d...