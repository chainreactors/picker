---
title: Introducing Proof-of-Work Defense for Onion Services
url: https://blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/
source: Tor Project blog
date: 2023-08-24
fetch_date: 2025-10-04T12:03:41.871001
---

# Introducing Proof-of-Work Defense for Onion Services

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Introducing Proof-of-Work Defense for Onion Services

by [pavel](/author/pavel)
| August 23, 2023

![](/introducing-proof-of-work-defense-for-onion-services/lead.png)

Today, we are officially introducing a proof-of-work (PoW) defense for onion services designed to prioritize verified network traffic as a deterrent against denial of service (DoS) attacks with the release of Tor 0.4.8.

Tor's PoW defense is a dynamic and reactive mechanism, remaining dormant under normal use conditions to ensure a seamless user experience, but when an onion service is under stress, the mechanism will prompt incoming client connections to perform a number of successively more complex operations. The onion service will then prioritize these connections based on the effort level demonstrated by the client. We believe that the introduction of a proof-of-work mechanism will disincentivize attackers by making large-scale attacks costly and impractical while giving priority to legitimate traffic. Onion Services are encouraged to update to version [0.4.8.](https://forum.torproject.org/t/stable-release-0-4-8-4/8884)

## Why the need?

The inherent design of onion services, which prioritizes user privacy by obfuscating IP addresses, has made it vulnerable to [DoS attacks](https://blog.torproject.org/tor-network-ddos-attack/) and traditional IP-based rate limits have been imperfect protections in these scenarios. In need of alternative solutions, we devised a proof-of-work mechanism involving a client puzzle to thwart DoS attacks without compromising user privacy.Â

## How does it work?

Proof of work acts as a ticket system that is turned off by default, but adapts to network stress by creating a priority queue. Before accessing an onion service, a small puzzle must be solved, proving that some "work" has been done by the client. The harder the puzzle, the more work is being performed, proving a user is genuine and not a bot trying to flood the service. Ultimately the proof-of-work mechanism blocks attackers while giving real users a chance to reach their destination.

## What does this mean for attackers and users?

If attackers attempt to flood an onion service with requests, the PoW defense will kick into action and increase the computational effort required to access a .onion site. This ticketing system aims to disadvantage attackers who make a huge number of connection attempts to an onion service. Sustaining these kinds of attacks will require a lot of computational effort on their part with diminishing returns, as the effort increases.

For everyday users, however, who tend to submit only a few requests at a time, the added computational effort of solving the puzzle is manageable for most devices, with initial times per solve ranging from 5 milliseconds for faster computers and up to 30 milliseconds for slower hardware. If the attack traffic increases, the effort of the work will increase, up to roughly 1 minute of work. While this process is invisible to the users and makes waiting on a proof-of-work solution comparable to waiting on a slow network connection, it has the distinct advantage of providing them with a chance to access the Tor network even when it is under stress by proving their humanity.Â

## Where do we go from here?

Over the past year, we have put a lot of work into mitigating attacks on our network and enhancing our defense for onion services. The introduction of Tor's PoW defense not only positions onion services among the few communication protocols with built-in DoS protections but also, when adopted by major sites, promises to reduce the negative impact of targeted attacks on network speeds. The dynamic nature of this system helps balance the load during sudden surges in traffic ensuring more consistent and reliable access to onion services.

* [network](/category/network)
* [onion services](/category/onion-services)
* [releases](/category/releases)
* [usability](/category/usability)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/&text=Today%2C%20we%20are%20officially%20introducing%20a%20proof-of-work%20%28PoW%29%20defense%20for%20onion%20services%20designed%20to%20prioritize%20verified%20network%20traffic%20as%20a%20deterrent%20against%20denial%20of%20service%20%28DoS%29%20attacks%20with%20the%20release%20of%20Tor%200.4.8.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/&text=Today%2C%20we%20are%20officially%20introducing%20a%20proof-of-work%20%28PoW%29%20defense%20for%20onion%20services%20designed%20to%20prioritize%20verified%20network%20traffic%20as%20a%20deterrent%20against%20denial%20of%20service%20%28DoS%29%20attacks%20with%20the%20release%20of%20Tor%200.4.8.)
[Bluesky](https://bsky.app/intent/compose?text=Today%2C%20we%20are%20officially%20introducing%20a%20proof-of-work%20%28PoW%29%20defense%20for%20onion%20services%20designed%20to%20prioritize%20verified%20network%20traffic%20as%20a%20deterrent%20against%20denial%20of%20service%20%28DoS%29%20attacks%20with%20the%20release%20of%20Tor%200.4.8.%0Ahttps%3A//blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproject.org/c/news/11)!

## Recent Updates

## [New Alpha Release: Tor Browser 15.0a3](/new-alpha-release-tor-browser-150a3/)

by [boklm](/author/boklm)
| September 22, 2025

Tor Browser 15.0a3 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.0](/new-release-tails-7_0/)

by [tails](/author/tails)
| September 18, 2025

We are very excited to present you Tails 7.0, the first version of Tails based
on Debian 13 (Trixie) and GNOME 48 (Bengaluru). Tails 7.0 brings new versions
of many applications included in Tails.

## [New Release: Tor Browser 14.5.7](/new-release-tor-browser-1457/)

by [ma1](/author/ma1)
| September 16, 2025

Tor Browser 14.5.7 is now available from the Tor Browser download page and also from our distribution directory.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://www.torproject.org/download/)

### Subscribe to our Newsletter

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://newsletter.torproject.org/)

####

####

####

####

####

####

####

####

Trademark, copyright notices, and rules for use by third parties can be found in our [FAQ](https://www.torproject.org/about/trademark/).