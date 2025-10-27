---
title: Arti 1.4.6 is released: Hidden Service resilience; work on flow control, Conflux, and CGO.
url: https://blog.torproject.org/arti_1_4_6_released/
source: Tor Project blog
date: 2025-08-06
fetch_date: 2025-10-07T01:00:24.496714
---

# Arti 1.4.6 is released: Hidden Service resilience; work on flow control, Conflux, and CGO.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.4.6 is released: Hidden Service resilience; work on flow control, Conflux, and CGO.

by [Diziet](/author/diziet)
| August 5, 2025

![](/arti_1_4_6_released/lead.png)

Arti is our ongoing project to create a next-generation Tor client in Rust.
We're happy to announce the latest release, Arti 1.4.6.

This release of Arti has some improvements for Onion Service (Hidden
Service) operators. There's better resistance to denial-of-service
([Proposal 362](https://spec.torproject.org/proposals/362-update-pow-control-loop.html)) and an experimental new utility for migration of
Hidden Service identity key from a C Tor keystore to Arti.

Also included are further developments towards supporting xon-based
([Proposal 324](https://spec.torproject.org/proposals/324-rtt-congestion-control.html)) flow control, multi-legged tunnels in Arti via our
[Conflux](https://spec.torproject.org/proposals/329-traffic-splitting.html) feature, and improving the cryptography used for data
transfer (Counter Galois Onion, [Proposal 359](https://spec.torproject.org/proposals/359-cgo-redux.html)).

Meanwhile we are continuing our work on the foundations of Arti to
support Relay and Bridge --- but there are no visible changes for this
in 1.4.6. Much of this work is currently occurring outside of the
Arti mainline.

For full details on what we've done, including API changes, and for information
about many more minor and less visible changes, please see the
[CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-146--5-August-2025).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md), and the
documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

Thanks to everybody who's contributed to this release, including
hashcatHitman, hjrgrn, nield, and tcyrus.

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_4_6_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_4_6_released/&text=Arti%201.4.6%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_4_6_released/&text=Arti%201.4.6%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.4.6%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_1_4_6_released/)

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