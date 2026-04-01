---
title: Arti 2.2.0 released: HTTP CONNECT, RPC, and Relay development.
url: https://blog.torproject.org/arti_2_2_0_released/
source: Tor Project blog
date: 2026-03-31
fetch_date: 2026-04-01T04:47:59.255535
---

# Arti 2.2.0 released: HTTP CONNECT, RPC, and Relay development.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 2.2.0 released: HTTP CONNECT, RPC, and Relay development.

by [Diziet](/author/diziet)
| March 31, 2026

![](/static/images/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in
Rust. We're happy to announce the latest release, Arti 2.2.0.

This release adds support for using HTTP CONNECT rather than SOCKS,
when connecting to the Tor network via Arti.
This previously-experimental feature is now included
a `full` build, and will then be enabled by default.
The HTTP CONNECT protocol is available over the same port as SOCKS.

The RPC client library (`arti-rpc-client-core`)
now supports non-blocking requests,
and integration with application event loops.
And the RPC system now supports administrative access to the Arti instance,
via a new "superuser" facility.

We also fixed a low-severity security issue,
[TROVE-2026-005](https://gitlab.torproject.org/tpo/core/arti/-/issues/2418),
which would somewhat weaken DoS resistance
in in certain unusual embedded build configurations.

Behind the scenes we have been working on relay support,
including relay channels and circuits, and directory server functionality
(mirrors and authorities).
As ever there are also lots of bugfixes, cleanups,
and test and CI improvements.

For full details on what we've done, including API changes,
and for information about many more minor and less-visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-220--30-march-2026).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/crates/arti/README.md).

Thanks to everybody who's contributed to this release, including
hjrgrn, HydroxideUnlaced, Nihal, and Tobias Stoeckmann.

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_2_2_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_2_2_0_released/&text=Arti%202.2.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_2_2_0_released/&text=Arti%202.2.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%202.2.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_2_2_0_released/)

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

## [Arti 2.2.0 released: HTTP CONNECT, RPC, and Relay development.](/arti_2_2_0_released/)

by [Diziet](/author/diziet)
| March 31, 2026

Arti 2.2.0 is released and ready for download.

## [New Release: Tails 7.6](/new-release-tails-7_6/)

by [tails](/author/tails)
| March 26, 2026

Tails 7.6 is now available.

## [New Release: Tor Browser 15.0.8](/new-release-tor-browser-1508/)

by [ma1](/author/ma1)
| March 24, 2026

Tor Browser 15.0.8 is now available from the Tor Browser download page and also from our distribution directory.

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