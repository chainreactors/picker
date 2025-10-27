---
title: Arti 1.1.1 is released: Groundwork for onion services
url: https://blog.torproject.org/arti_111_released/
source: Tor Project blog
date: 2023-02-02
fetch_date: 2025-10-04T05:31:52.501755
---

# Arti 1.1.1 is released: Groundwork for onion services

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Arti 1.1.1 is released: Groundwork for onion services

by [nickm](/author/nickm)
| February 1, 2023

![](/arti_111_released/lead.png)

Arti is our ongoing project to create an next-generation Tor client
in Rust. In late November, we released [Arti 1.1.0](https://blog.torproject.org/arti_110_released/). Now we're announcing
the next release in its series, Arti 1.1.1.

Since our last release, our primary focus has been preparation for
onion service support in Arti. To that end, we've broken the work
down into a [bunch of tickets](https://gitlab.torproject.org/tpo/core/arti/-/milestones/11#tab-issues), designed our [major](https://tpo.pages.torproject.net/core/doc/rust/tor_hsclient/index.html)
[internal](https://tpo.pages.torproject.net/core/doc/rust/tor_hsservice/index.html) [APIs](https://tpo.pages.torproject.net/core/doc/rust/tor_hscrypto/index.html), and started to work on
the lower-level features. There's nothing you can use here yet, but
the work is coming!

We hope to deliver experimental support for onion service
clientsâthen, support for running services later in the year.
Finally, we will build the security features allow onion services and
clients to be at least as safe as in C tor.

We've also made a number of other changes, including improved logging
security, new convenience APIs, and better handling of some SOCKS
requests. You can find a more complete list of changes in our
[CHANGELOG](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md#arti-111-1-february-2022).

For more information on using Arti, see our top-level [README](https://gitlab.torproject.org/tpo/core/arti/-/blob/main/README.md),
and the docmentation for the [`arti` binary](https://gitlab.torproject.org/tpo/core/arti/-/tree/main/crates/arti).

Thanks to everyone who has contributed to this release, including
Alexander FÃ¦rÃ¸y, coral, Dimitris Apostolou, Emil Engler, Jim Newsome,
Michael van Straten, Neel Chauhan, and Trinity Pointard.

Also, our deep thanks to [Zcash Community Grants](https://zcashcommunitygrants.org/) for funding the
development of Arti 1.1.1!

* [announcements](/category/announcements)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/arti_111_released/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/arti_111_released/&text=Arti%201.1.1%20is%20released%20and%20ready%20for%20download.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/arti_111_released/&text=Arti%201.1.1%20is%20released%20and%20ready%20for%20download.)
[Bluesky](https://bsky.app/intent/compose?text=Arti%201.1.1%20is%20released%20and%20ready%20for%20download.%0Ahttps%3A//blog.torproject.org/arti_111_released/)

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