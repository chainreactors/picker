---
title: New Release: Rdsys 1.0
url: https://blog.torproject.org/new-release-rdsys-1-0/
source: Tor Project blog
date: 2025-02-25
fetch_date: 2025-10-06T20:58:09.653054
---

# New Release: Rdsys 1.0

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Rdsys 1.0

by [meskio](/author/meskio)
| February 24, 2025

![](/new-release-rdsys-1-0/lead.png)

After years of development, we are officially releasing [Rdsys 1.0](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/). Although Rdsys has already been the sole mechanism for distributing bridges [since it replaced BridgeDB last October](/making-connections-from-bridgedb-to-rdsys/), this version 1.0 milestone officially marks its new status.

We now consider Rdsys stable, but our work is far from finished. We are committed to improving Rdsys and fixing issues as they arise, and to adapting quickly to censors' evolving tactics.

Full changelog since 0.14.2 (when we fully replaced BridgeDB for Rdsys):

* fix multiple race conditions ([#223](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/issues/223))
* core: propagate non working bridges to distributors ([#245](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/issues/245))
* moat: the type of the captcha bridge response is 'moat-bridges'
* email: fix imap freeze ([#129](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/issues/129))
* email: attach a qr of the bridgelines ([#244](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/issues/244))
* telegram: send a qr of the bridgelines ([#243](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/issues/243))
* https: distribute vanilla bridges ([#239](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/issues/239))
* https: reduce logs for common failures
* bridgedb-metrics: use country if available ([#235](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/issues/235))

* [circumvention](/category/circumvention)
* [community](/category/community)
* [releases](/category/releases)
* [human rights](/category/human-rights)
* [announcements](/category/announcements)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-rdsys-1-0/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-rdsys-1-0/&text=Rdsys%201.0%20has%20been%20released%2C%20officially%20marking%20the%20first%20stable%20version%20of%20Tor%27s%20next-generation%20bridge%20distribution%20software.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-rdsys-1-0/&text=Rdsys%201.0%20has%20been%20released%2C%20officially%20marking%20the%20first%20stable%20version%20of%20Tor%27s%20next-generation%20bridge%20distribution%20software.)
[Bluesky](https://bsky.app/intent/compose?text=Rdsys%201.0%20has%20been%20released%2C%20officially%20marking%20the%20first%20stable%20version%20of%20Tor%27s%20next-generation%20bridge%20distribution%20software.%0Ahttps%3A//blog.torproject.org/new-release-rdsys-1-0/)

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