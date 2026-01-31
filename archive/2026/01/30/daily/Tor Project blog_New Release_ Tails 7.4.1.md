---
title: New Release: Tails 7.4.1
url: https://blog.torproject.org/new-release-tails-7_4_1/
source: Tor Project blog
date: 2026-01-30
fetch_date: 2026-01-31T04:05:13.467757
---

# New Release: Tails 7.4.1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 7.4.1

by [tails](/author/tails)
| January 30, 2026

![](/new-release-tails-7_4_1/lead.jpg)

This release is an emergency release to fix critical security vulnerabilities
in OpenSSL, a network encryption library used by Tor.

## Changes and updates

### Included software

* Update the OpenSSL library to 3.5.4, which fixes [DSA 6113-1](https://lists.debian.org/debian-security-announce/2026/msg00022.html), a set of vulnerabilities that could be critical. Using this set of vulnerabilities, an malicious Tor relay might be able to deanonymize a Tails user.

  We are not aware of these vulnerabilities being exploited in practice.
* Update the *Tor* client to 0.4.8.22.
* Update *Thunderbird* to [140.7.0](https://www.thunderbird.net/en-US/thunderbird/140.7.0esr/releasenotes/).

## Fixed problems

* Fix Gmail authentication in *Thunderbird*. ([#21384](https://gitlab.tails.boum.org/tails/tails/-/issues/21384))
* Add a spinner when opening the Wi-Fi settings from the Tor Connection assistant. ([#18594](https://gitlab.tails.boum.org/tails/tails/-/issues/18594))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Known issues

The homepage of Tor Browser incorrectly says you are still using Tails 7.4,
even after you have upgraded to 7.4.1. It also links to the release notes for
that older version.

If in doubt, to verify that you are using Tails 7.4.1, choose **Apps â¸ Tails
â¸ About Tails**.

## Get Tails 7.4.1

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.4.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 7.4.1 on a new USB stick

Follow our installation instructions:

* [Install from Windows](https://tails.net/install/windows/)
* [Install from macOS](https://tails.net/install/mac/)
* [Install from Linux](https://tails.net/install/linux/)
* [Install from Debian or Ubuntu using the command line and GnuPG](https://tails.net/install/expert/)

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
7.4.1 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-7_4_1/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-7_4_1/&text=This%20release%20is%20an%20emergency%20release%20to%20fix%20critical%20security%20vulnerabilities%20in%20OpenSSL%2C%20a%20network%20encryption%20library%20used%20by%20Tor.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-7_4_1/&text=This%20release%20is%20an%20emergency%20release%20to%20fix%20critical%20security%20vulnerabilities%20in%20OpenSSL%2C%20a%20network%20encryption%20library%20used%20by%20Tor.)
[Bluesky](https://bsky.app/intent/compose?text=This%20release%20is%20an%20emergency%20release%20to%20fix%20critical%20security%20vulnerabilities%20in%20OpenSSL%2C%20a%20network%20encryption%20library%20used%20by%20Tor.%0Ahttps%3A//blog.torproject.org/new-release-tails-7_4_1/)

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

January 31, 2026 – February 1, 2026

## [FOSDEM'26 (Brussels)](/event/fosdem-2026/)

## Recent Updates

## [New Release: Tails 7.4.1](/new-release-tails-7_4_1/)

by [tails](/author/tails)
| January 30, 2026

This release is an emergency release to fix critical security vulnerabilities
in OpenSSL, a network encryption library used by Tor.

## [New Release: Tor Browser 15.0.5](/new-release-tor-browser-1505/)

by [morgan](/author/morgan)
| January 29, 2026

Tor Browser 15.0.5 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.4](/new-release-tails-7_4/)

by [tails](/author/tails)
| January 15, 2026

Tails 7.4 is now available.

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