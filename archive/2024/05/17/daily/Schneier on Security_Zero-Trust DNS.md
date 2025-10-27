---
title: Zero-Trust DNS
url: https://www.schneier.com/blog/archives/2024/05/zero-trust-dns.html
source: Schneier on Security
date: 2024-05-17
fetch_date: 2025-10-06T17:17:29.551198
---

# Zero-Trust DNS

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

## Zero-Trust DNS

Microsoft is [working on](https://arstechnica.com/security/2024/05/microsoft-plans-to-lock-down-windows-dns-like-never-before-heres-how/) a promising-looking protocol to lock down DNS.

> ZTDNS aims to solve this decades-old problem by integrating the Windows DNS engine with the Windows Filtering Platform—the core component of the Windows Firewall—directly into client devices.
>
> Jake Williams, VP of research and development at consultancy Hunter Strategy, said the union of these previously disparate engines would allow updates to be made to the Windows firewall on a per-domain name basis. The result, he said, is a mechanism that allows organizations to, in essence, tell clients “only use our DNS server, that uses TLS, and will only resolve certain domains.” Microsoft calls this DNS server or servers the “protective DNS server.”
>
> By default, the firewall will deny resolutions to all domains except those enumerated in allow lists. A separate allow list will contain IP address subnets that clients need to run authorized software. Key to making this work at scale inside an organization with rapidly changing needs. Networking security expert Royce Williams (no relation to Jake Williams) called this a “sort of a bidirectional API for the firewall layer, so you can both trigger firewall actions (by input \*to\* the firewall), and trigger external actions based on firewall state (output \*from\* the firewall). So instead of having to reinvent the firewall wheel if you are an AV vendor or whatever, you just hook into WFP.”

Tags: [DNS](https://www.schneier.com/tag/dns/), [Microsoft](https://www.schneier.com/tag/microsoft/)

[Posted on May 16, 2024 at 7:03 AM](https://www.schneier.com/blog/archives/2024/05/zero-trust-dns.html) •
[58 Comments](https://www.schneier.com/blog/archives/2024/05/zero-trust-dns.html#comments)

### Comments

Blerik •
[May 16, 2024 8:03 AM](https://www.schneier.com/blog/archives/2024/05/zero-trust-dns.html/#comment-436913)

Does this mean removing or locking down /etc/hosts (or the Windows equivalent)? Which then makes certain use-cases of private dns resolving (like lab machine access, or near-production testing) impossible?

Also I see no mention of ip-address based access being blocked. Is this also in scope? It will make accessing your at home wifi access point difficult. But if it’s not blocked, your firewall is full of holes…

RapidGeek •
[May 16, 2024 8:05 AM](https://www.schneier.com/blog/archives/2024/05/zero-trust-dns.html/#comment-436914)

This could be a Trojan Horse. Better security or the opportunity to block any content not approved by the ruling political party or whatever insane ideology comes along.

If you trust someone to provide security for you, then you trust your vulnerability to them as well

echo •
[May 16, 2024 8:11 AM](https://www.schneier.com/blog/archives/2024/05/zero-trust-dns.html/#comment-436917)

This is a good idea in theory if viewed in isolation. The problems start happening once you step out of the technical quadrant and begin looking around the technical, human rights, economics, and social model.

Variants of this kind of idea and this general pool of problems have been evolving since around the early 2000’s. Notable examples include online Windows authentication and games (DLC) Downloadable Content, and various wheezes which have pinged the headlines very briefly from time to time.

One question I ask is “Security but security for whom?” Without credible human rights mechanisms in place (and adequate economic and social policy) I really can’t see facilitating locked down DNS as a good idea. Like, if you had locked down DNS, bit level permissions on internet access, and a locked down hardware-OS-application stack? Add in captured/complicit media and banning public protest? A more rounded structural/meta discussion is rarely had in the media until it’s too late, and the tech industry rarely if ever considers it with a “If we don’t do these projects someone else will” argument in some quarters. The work is very context and history free and never asks the what happens in four, fix, or six steps. What is the direction of travel?

Around 15+ years ago Microsoft Research produced a paper which they used to lobby the UK government which proposed an internet model which could give permissions down to the bit level. Again, another idea which is good on paper if viewed in isolation. I’m guilty of it myself as I had without knowing about Microsoft’s push which only became public a few years later had lobbied on this myself. I later came to see this (and a few other bright ideas I subsequently had) as still a good idea on paper but… There’s another story in here about paths crossing involving journalism and human rights and the fact it can be a very small world at times. That one is not for today though.

As for the boss class of corporations not all but too many don’t respect human rights. They don’t respect DEI or unions. They don’t respect fair pay and conditions. (In the US corporations get huge discounts on healthcare insurance which pushed costs up for everyone else and as a system your only value as a human being is how much money you have.) They spend their disproportionate income lobbying and use their resources to keep it that way.

We’re back to the “security but security for whom” question. You create perfect technical security then what? What’s to prevent bad actors in politics walking through the side door with a bad lock and tearing up your democracy and human rights and dignity then using this enhanced security to make sure it stays that way? This security doesn’t look like such a good idea after all.

A Wall is a Wall •
[May 16, 2024 8:52 AM](https://www.schneier.com/blog/archives/2024/05/zero-trust-dns.html/#comment-436918)

@ALL

A wall can keep you out or keep you in, and a castle is also a prison.

Security only benefits those who control it. We have seen this with both Google and Apple with their mobile phone OS’s and their forced App Stores.

Microsoft have been desperate for years to get the same level of control over users. Look back to their DRM and Trusted Platform nonsense. Supposedly for protection of first the ‘Entertainment Corps from users’ and then ‘Corporate employers from users’.

But ultimately Microsoft controling the keys to not just the castle but the kingdom. Thus defacto making them King of the Castle and Country, with every one held prisoner to their whim.

Long before we had technology that could be controlled so easily by others beyond our own control, Benjamin Franklin wrote “Those who would give up essential Liberty, to purchase a little temporary Safety, deserve neither Liberty nor Safety.”

In essence most today have sleepwalked into a guilded cage.

The price of the illusion of safety from unknown attackers is to be not just controlled but bled by those who actually control the ...