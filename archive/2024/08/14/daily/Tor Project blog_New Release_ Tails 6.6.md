---
title: New Release: Tails 6.6
url: https://blog.torproject.org/new-release-tails-66/
source: Tor Project blog
date: 2024-08-14
fetch_date: 2025-10-06T18:05:59.312753
---

# New Release: Tails 6.6

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 6.6

by [tails](/author/tails)
| August 13, 2024

![](/new-release-tails-66/lead.jpg)

## Changes and updates

* Update *Tor Browser* to [13.5.2](https://blog.torproject.org/new-release-tor-browser-1352).
* Update *Thunderbird* to [115.14.0](https://www.thunderbird.net/en-US/thunderbird/115.14.0/releasenotes/).
* Update [many](https://salsa.debian.org/kernel-team/firmware-nonfree/-/blob/master/debian/changelog?ref_type=heads) firmware packages. This improves the support for newer hardware: graphics, Wi-Fi, and so on.

## Fixed problems

#### Persistent Storage

* Increase the maximum waiting time to 4 minutes when unlocking the Persistent Storage before returning an error. ([#20475](https://gitlab.tails.boum.org/tails/tails/-/issues/20475))
* Made the creation of the Persistent Storage more robust after starting a Tails USB stick for the first time. ([#20451](https://gitlab.tails.boum.org/tails/tails/-/issues/20451))
* Prevent the Persistent Storage settings from freezing after opening a link to the documentation. ([#20438](https://gitlab.tails.boum.org/tails/tails/-/issues/20438))
* Prevent Additional Software from crashing when installing virtual packages. ([#20477](https://gitlab.tails.boum.org/tails/tails/-/issues/20477))

#### Networking

* Fix connecting to the Tor network using default bridges. ([#20467](https://gitlab.tails.boum.org/tails/tails/-/issues/20467))
* Allow enabling multiple network interfaces again. ([#20128](https://gitlab.tails.boum.org/tails/tails/-/issues/20128))

#### Tails Cloner

* Remove 30 seconds of waiting time when installing by cloning. ([#20131](https://gitlab.tails.boum.org/tails/tails/-/issues/20131))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Get Tails 6.6

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 6.0 or later to 6.6.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 6.6 on a new USB stick

Follow our installation instructions:

* [Install from Windows](https://tails.net/install/windows/)
* [Install from macOS](https://tails.net/install/mac/)
* [Install from Linux](https://tails.net/install/linux/)
* [Install from Debian or Ubuntu using the command line and GnuPG](https://tails.net/install/expert/)

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
6.6 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-66/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-66/&text=Tails%206.6%20is%20out.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-66/&text=Tails%206.6%20is%20out.)
[Bluesky](https://bsky.app/intent/compose?text=Tails%206.6%20is%20out.%0Ahttps%3A//blog.torproject.org/new-release-tails-66/)

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