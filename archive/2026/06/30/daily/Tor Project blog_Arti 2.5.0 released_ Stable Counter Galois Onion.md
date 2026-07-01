---
title: Arti 2.5.0 released: Stable Counter Galois Onion
url: https://blog.torproject.org/arti_2_5_0_released/
source: Tor Project blog
date: 2026-06-30
fetch_date: 2026-07-01T06:24:34.352322
---

# Arti 2.5.0 released: Stable Counter Galois Onion

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 2.5.0 released: Stable Counter Galois Onion

by [cve](/author/cve)
| June 30, 2026

![](/arti_2_5_0_released/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in
Rust. We're happy to announce the latest release, Arti 2.5.0.

This release marks [Counter Galois Onion](https://blog.torproject.org/introducing-cgo/) as a stable feature and includes it in
full feature builds. Likewise, [Congestion Control](https://blog.torproject.org/congestion-contrl-047/) is now enabled in default
builds of Arti, increasing the overall speed without any further configuration.

Unfortunately, this release also comes with the disclosure of two medium-severity
DoS security issues, [TROVE-2026-024](https://gitlab.torproject.org/tpo/core/arti/-/work_items/2566) as well as [TROVE-2026-027](https://gitlab.torproject.org/tpo/core/arti/-/work_items/2601), whose fixes
are of course included within the release.

Additionally, this release continues our ongoing development towards using
Arti as a relay and as a directory authority.

Another noteworthy change is that we've increased our minimum supported Rust
version to Rust 1.91, released in October 2025.

Of course, this release also contains a number of bugfixes, cleanups, and
improvements throughout various parts of the code base.

For full details on what we've done, including API changes,
and for information about many more minor and less-visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md?ref_type=heads#arti-250--30-june-2026).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/crates/arti/README.md).

Thanks to everybody who's contributed to this release, including
5225225, Neel Chauhan, hjrgrn, moumenalaoui, pryty26.

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_2_5_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_2_5_0_released/&text=Arti%202.5.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_2_5_0_released/&text=Arti%202.5.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%202.5.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_2_5_0_released/)

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

## [Arti 2.5.0 released: Stable Counter Galois Onion](/arti_2_5_0_released/)

by [cve](/author/cve)
| June 30, 2026

Arti 2.5.0 is released and ready for download.

## [New Release: Tor Browser 15.0.17](/new-release-tor-browser-15017/)

by [ma1](/author/ma1)
| June 28, 2026

Tor Browser 15.0.17 is now available from the Tor Browser download page and also from our distribution directory.

## [Sunsetting Tor 0.4.8 â Please update to 0.4.9 by September](/sunsetting-tor-048/)

by [ahf](/author/ahf)
| June 23, 2026

We want to sunset Tor 0.4.8. Please update before September.

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