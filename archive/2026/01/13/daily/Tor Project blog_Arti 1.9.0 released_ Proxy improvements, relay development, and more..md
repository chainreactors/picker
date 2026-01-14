---
title: Arti 1.9.0 released: Proxy improvements, relay development, and more.
url: https://blog.torproject.org/arti_1_9_0_released/
source: Tor Project blog
date: 2026-01-13
fetch_date: 2026-01-14T03:36:01.213114
---

# Arti 1.9.0 released: Proxy improvements, relay development, and more.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.9.0 released: Proxy improvements, relay development, and more.

by [cve](/author/cve)
| January 13, 2026

![](/arti_1_9_0_released/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in
Rust. We're happy to announce the latest release, Arti 1.9.0.

This release includes some behind-the-scences work on relays and directory
authority development, and adds improved support for running with dynamically
assigned ports. For example, Arti now accepts `proxy.socks_listen = "auto"`
to configure its SOCKS proxy with an operating-system-assigned port, and writes
the assigned port to a structured JSON file in Arti's data directory.

Following this change to dynamic port assignments, we also depreacted `0` as
a port number for making it disabling this feature all together.

There has also been some interesting development going on with onion services,
namely that Arti's key manager is now available as an experimental public API,
intended for use by Arti's key management CLI. This is an API change only,
users of the CLI are not affected by it.

Our effort to support relays in Arti also made notable progress. Namely, the
relay circuit reactor is now capable of handling incoming data stream requests,
something crucial for the overall operational design of this component.

Likewise, development in the domain of directory authorities also progressed
significantly. This release contains some refactoring of various network
document types and APIs and adds experimental support for directory authority
key certificates. Similarly, the directory mirror got the relevant logic
for downloading network documents from directory authorities.

For full details on what we've done, including API changes,
and for information about many more minor and less-visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md?ref_type=heads#arti-190--13-january-2026).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

Thanks to everybody who's contributed to this release, including
Benjamin Erhart, JÃ©rÃ´me Charaoui, Neel Chauhan, Nihal, Pier Angelo Vendrame,
Yaksh Bariya, hjrgrn, and tla.

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_9_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_9_0_released/&text=Arti%201.9.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_9_0_released/&text=Arti%201.9.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.9.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_1_9_0_released/)

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

## [New Release: Tor Browser 15.0.4](/new-release-tor-browser-1504/)

by [ma1](/author/ma1)
| January 13, 2026

Tor Browser 15.0.4 is now available from the Tor Browser download page and also from our distribution directory.

## [Arti 1.9.0 released: Proxy improvements, relay development, and more.](/arti_1_9_0_released/)

by [cve](/author/cve)
| January 13, 2026

Arti 1.9.0 is released and ready for download.

## [Code audit for the Tor Project completed by 7aSecurity](/code-audit-network-health-tools/)

by [gaba](/author/gaba)
| December 18, 2025

[7aSecurity](https://7asecurity.com/) conducted a comprehensive code audit for several tools we use to monitor the health of the Tor network. This blog post outlines key recommendations and links to the full report.

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