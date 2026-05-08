---
title: Arti 2.3.0 released: Logging, Relay, Directory authority, and RPC development.
url: https://blog.torproject.org/arti_2_3_0_released/
source: Tor Project blog
date: 2026-05-07
fetch_date: 2026-05-08T04:56:58.136634
---

# Arti 2.3.0 released: Logging, Relay, Directory authority, and RPC development.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 2.3.0 released: Logging, Relay, Directory authority, and RPC development.

by [wesleyac](/author/wesleyac)
| May 7, 2026

![](/static/images/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in
Rust. We're happy to announce the latest release, Arti 2.3.0.

This release bumps the minimum MacOS version supported by Arti to 10.14,
up from 10.12. Despite being supported on a technical level,
we do not recommend the use of MacOS versions that old,
as they are no longer receiving updates from Apple and may have unpatched security issues.

This release continues our ongoing development towards using Arti as a relay
and as a directory authority. It also continues development on RPC,
including adding a new RPC API for inspecting tunnel paths.

Additionally, there are a couple new logging related features.
Arti now supports logging to syslog when the `syslog` feature is enabled
and the `logging.syslog` config option is enabled. We've also added a new
`logging.protocol_warnings` option to log protocol violations as warnings.

Developers who use the `arti-client` crate should note that in the release after this one,
we plan to change `TorClient` to be wrapped in an `Arc` explicitly,
rather than implicitly having `Arc`-like semantics. Be prepared for this breaking change,
and if you have any thoughts about it, please speak up in [#2469](https://gitlab.torproject.org/tpo/core/arti/-/work_items/2469).

As usual, there is also a signigicant amount of cleanup, improvements to testing,
infrastructure, and documentation, and many small bugfixes.

For full details on what we've done, including API changes,
and for information about many more minor and less-visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-230--7-may-2026).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/crates/arti/README.md).

Thanks to everybody who's contributed to this release, including
Andrew Kloet, hjrgrn, and moumenalaoui.

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_2_3_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_2_3_0_released/&text=Arti%202.3.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_2_3_0_released/&text=Arti%202.3.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%202.3.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_2_3_0_released/)

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

June 14, 2026 – June 14, 2025

## [W3PN Neo-Cypherpunk Summit](/event/W3PN-Summit-2026/)

June 23, 2026 – June 24, 2025

## [DW Global Media Forum (GMF) 2026](/event/global-media-forum-2026/)

## Recent Updates

## [New Release: Tor Browser 15.0.13](/new-release-tor-browser-15013/)

by [ma1](/author/ma1)
| May 8, 2026

Tor Browser 15.0.13 is now available from the Tor Browser download page and also from our distribution directory.

## [New Alpha Release: Tor Browser 16.0a6](/new-alpha-release-tor-browser-160a6/)

by [ma1](/author/ma1)
| May 7, 2026

Tor Browser 16.0a6 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tor Browser 15.0.12](/new-release-tor-browser-15012/)

by [ma1](/author/ma1)
| May 7, 2026

Tor Browser 15.0.12 is now available from the Tor Browser download page and also from our distribution directory.

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