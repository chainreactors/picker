---
title: Arti 1.7.0 released: Onion service restricted discovery, experimental HTTP proxy, relay development, and more.
url: https://blog.torproject.org/arti_1_7_0_released/
source: Tor Project blog
date: 2025-11-03
fetch_date: 2025-11-04T03:11:40.436044
---

# Arti 1.7.0 released: Onion service restricted discovery, experimental HTTP proxy, relay development, and more.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.7.0 released: Onion service restricted discovery, experimental HTTP proxy, relay development, and more.

by [opara](/author/opara)
| November 3, 2025

![](/arti_1_7_0_released/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in Rust.
We're happy to announce the latest release, Arti 1.7.0.

Arti 1.7.0 stabilizes the onion service restricted discovery feature,
previously known as "client authorization".
This requires Arti to be built with the `restricted-discovery` feature enabled,
and for the appropriate [configuration options](https://gitlab.torproject.org/tpo/core/arti/-/blob/arti-v1.7.0/crates/arti/src/arti-example-config.toml#L581)
to be enabled and configured for the onion service.

In addition to Arti's existing SOCKS proxy,
Arti now has experimental support for running an HTTP CONNECT proxy.
When built with the experimental `http-connect` feature enabled,
Arti's SOCKS listeners will also accept `HTTP CONNECT` tunnel requests,
with support for [Tor extensions](https://spec.torproject.org/http-connect.html) as amended by [proposal 365](https://spec.torproject.org/proposals/365-http-connect-ext.html).

This release of Arti continues behind-the-scenes development of functionality
required to support relays and directory authorities.
This development has focused on the routing architecture and protocol implementation (circuits and channels),
parsing and generating Tor network documents,
directory cache support,
and the relay main-loop/front-end code.

Arti 1.7.0 increases our MSRV (Minimum Supported Rust Version)
to 1.86.0, in accordance with our [MSRV policy](https://gitlab.torproject.org/tpo/core/arti/#minimum-supported-rust-version).

For full details on what we've done, including API changes,
and for information about many more minor and less visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md?ref_type=heads#arti-170--30-october-2025).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

Thanks to everybody who's contributed to this release, including
5225225, hashcatHitman, hjrgrn, Neel Chauhan, and Niel Duysters.

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_1_7_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_1_7_0_released/&text=Arti%201.7.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_1_7_0_released/&text=Arti%201.7.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.7.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_1_7_0_released/)

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

November 12, 2025 – December 10, 2025

## [State of the Onion 2025](/event/state-of-the-onion-2025/)

## Recent Updates

## [Keeping the internet free together: Join us for State of the Onion 2025](/state-of-the-onion-2025/)

by [arturom](/author/arturom) and [pavel](/author/pavel)
| November 3, 2025

When censorship strikes, Tor provides a lifeline to access information--a lifeline to a FREE INTERNET. Tune in to this year's 2025 State of the Onion event to hear about how our teams and community work tirelessly behind the scenes to keep it alive.Â

## [Arti 1.7.0 released: Onion service restricted discovery, experimental HTTP proxy, relay development, and more.](/arti_1_7_0_released/)

by [opara](/author/opara)
| November 3, 2025

Arti 1.7.0 is released and ready for download.

## [A new home for Tor user documentation](/new-user-support-portal-tor-tails/)

by [gus](/author/gus)
| October 29, 2025

Finding support shouldn't be hard. That's why we're launching the new Tor User Support portal: a single, unified home that brings together the Tor Browser User Manual and the Support portal, making it easier for everyone to access the documentation they need to use Tor safely and confidently.

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