---
title: Sunsetting Tor 0.4.8 – Please update to 0.4.9 by September
url: https://blog.torproject.org/sunsetting-tor-048/
source: Tor Project blog
date: 2026-06-23
fetch_date: 2026-06-24T06:06:23.480175
---

# Sunsetting Tor 0.4.8 – Please update to 0.4.9 by September

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Sunsetting Tor 0.4.8 â Please update to 0.4.9 by September

by [ahf](/author/ahf)
| June 23, 2026

![](/static/images/lead.png)

Hello Tor Community!

As you know, different teams inside the Tor Project are working on the Arti
Relay project where we hope to be able to begin the upgrade of the network
towards our Rust implementation of Tor in the near future. To support this
work, we would like to announce that we intend to actively stop compatibility
for 0.4.8 and earlier C Tor versions soon. This means that these versions will
*no longer work on the network at all* after our target date, which is
currently September 1st, 2026.

If youâre a Tor Browser user running an up-to-date version of Tor Browser, this
won't impact you. If you're running an older, perhaps not-so-well-maintained,
Onion Service somewhere, or youâre building an app that integrates C Tor, you
may want to read along here.

[Tor 0.4.8 reached End of Life on the 1st of
June](https://gitlab.torproject.org/tpo/core/team/-/wikis/NetworkTeam/CoreTorReleases#list-of-releases),
and there will not be any more updates to this release series. We highly
encourage people to upgrade to the Tor 0.4.9 series (or later).

Usually, we try not to break existing releases, even if they are unsupported,
unless we have a pretty good reason. In this case, we have several reasons.
With the work towards Arti on both the client and relay, the Network Team has
identified a couple of features we would like to remove from the Tor ecosystem.
Removing support for 0.4.8 will help us facilitate a smooth transition, and reduce effort associated with
difficult to maintain features that provide very little value. Unfortunately,
because Torâs Directory Protocol layer works the way it does, we cannot remove
these features without affecting older clients.

The most important reason is this: in 0.4.9, we have made some former fields in
our directory data obsolete -- specifically, [TAP onion
keys](https://spec.torproject.org/proposals/350-remove-tap.html) and [family
lines](https://spec.torproject.org/proposals/321-happy-families.html). Removing
these fields will let us save a great deal of client directory bandwidth for
everyone. This, in turn, will make all Tor clients bootstrap a little faster,
especially those on slow connections. But when we remove these fields, clients
and relays running earlier versions of Tor will no longer work, since they
expect the TAP onion keys to be present. Therefore, in order to deliver
improved performance faster, we need to accelerate the date on which 0.4.8 will
stop working.

The secondary reason for sunsetting 0.4.8: Our Arti directory authority
implementation needs network integration soon, and it will be easier to write
if it doesnât support deprecated fields.

With this blog post out, we will begin reaching out to the downstreams of Tor
we identified as shipping older versions and try to get them to upgrade. We
appreciate community help here, too. If you identify that your favorite project
that bundles Tor uses an outdated version of Tor, please reach out to them and
(politely!) encourage them to upgrade. We are tracking some of this outreach in
[network-health/team#460](https://gitlab.torproject.org/tpo/network-health/team/-/work_items/460).
If you have a very good reason for needing a longer time with 0.4.8 support
than 1 September 2026, please let us know by leaving a comment on that ticket.

Thank you!

* [tor](/category/tor)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/sunsetting-tor-048/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/sunsetting-tor-048/&text=We%20want%20to%20sunset%20Tor%200.4.8.%20Please%20update%20before%20September.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/sunsetting-tor-048/&text=We%20want%20to%20sunset%20Tor%200.4.8.%20Please%20update%20before%20September.)
[Bluesky](https://bsky.app/intent/compose?text=We%20want%20to%20sunset%20Tor%200.4.8.%20Please%20update%20before%20September.%0Ahttps%3A//blog.torproject.org/sunsetting-tor-048/)

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

## Upcoming Events

June 23, 2026 – June 24, 2025

## [DW Global Media Forum (GMF) 2026](/event/global-media-forum-2026/)

## Recent Updates

## [Sunsetting Tor 0.4.8 â Please update to 0.4.9 by September](/sunsetting-tor-048/)

by [ahf](/author/ahf)
| June 23, 2026

We want to sunset Tor 0.4.8. Please update before September.

## [New Release: Tails 7.9](/new-release-tails-7_9/)

by [tails](/author/tails)
| June 18, 2026

Tails 7.9 is now available.

## [New Release: Tor Browser 15.0.16](/new-release-tor-browser-15016/)

by [boklm](/author/boklm)
| June 17, 2026

Tor Browser 15.0.16 is now available from the Tor Browser download page and also from our distribution directory.

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