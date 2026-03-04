---
title: Arti 2.1.0 released: Relay and RPC development.
url: https://blog.torproject.org/arti_2_1_0_released/
source: Tor Project blog
date: 2026-03-03
fetch_date: 2026-03-04T04:04:27.451542
---

# Arti 2.1.0 released: Relay and RPC development.

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 2.1.0 released: Relay and RPC development.

by [gabi](/author/gabi)
| March 3, 2026

![](/arti_2_1_0_released/lead.png)

Arti is our ongoing project to create a next-generation Tor implementation in
Rust. We're happy to announce the latest release, Arti 2.1.0.

This release contains a lot of behind-the-scenes work on relay support
and on RPC development. While Arti still cannot run as a relay,
we are making good progress, and we think it will soon be ready for
Arti developers to test it as a middle relay.

Additionally, we have overhauled all of Arti's configuration to use a new,
[`derive-deftly`](https://crates.io/crates/derive-deftly)-based approach. We believe this will make
defining new configuration types easier, saving us development time
in the long run.

This release also contains a number of bugfixes, cleanups,
as well as improvements to our CI infrastructure.

Finally, Arti 2.1.0 increases our MSRV (Minimum Supported Rust Version)
to 1.89.0, in accordance with our [MSRV policy](https://gitlab.torproject.org/tpo/core/arti/#minimum-supported-rust-version).

For full details on what we've done, including API changes,
and for information about many more minor and less-visible changes,
please see the [CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-210--2-march-2026).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the documentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/crates/arti/README.md).

Thanks to everybody who's contributed to this release, including
Niel Duysters, Nihal, Nuhiat-Arefin, Robert Bartlensky, carti-it, hjrgrn,
moumenalaoui, robertb, and sjcobb!

Also, our deep thanks to our [sponsors](https://www.torproject.org/about/sponsors/) for funding the development of Arti!

* [announcements](/category/announcements)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_2_1_0_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_2_1_0_released/&text=Arti%202.1.0%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_2_1_0_released/&text=Arti%202.1.0%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%202.1.0%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_2_1_0_released/)

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

March 6, 2026 – March 7, 2026

## [Parallel Society (Lisbon)](/event/Parallel-Society/)

March 8, 2026 – March 10, 2026

## [FOSSASIA Summit 2026](/event/fossasia-2026/)

## Recent Updates

## [Arti 2.1.0 released: Relay and RPC development.](/arti_2_1_0_released/)

by [gabi](/author/gabi)
| March 3, 2026

Arti 2.1.0 is released and ready for download.

## [New Release: Tails 7.5](/new-release-tails-7_5/)

by [tails](/author/tails)
| February 26, 2026

Tails 7.5 is now available.

## [New Release: Tor Browser 15.0.7](/new-release-tor-browser-1507/)

by [ma1](/author/ma1)
| February 24, 2026

Tor Browser 15.0.7 is now available from the Tor Browser download page and also from our distribution directory.

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