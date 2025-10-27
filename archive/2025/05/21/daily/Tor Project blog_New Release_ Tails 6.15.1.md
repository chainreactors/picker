---
title: New Release: Tails 6.15.1
url: https://blog.torproject.org/new-release-tails-6_15_1/
source: Tor Project blog
date: 2025-05-21
fetch_date: 2025-10-06T22:29:35.174285
---

# New Release: Tails 6.15.1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 6.15.1

by [tails](/author/tails)
| May 20, 2025

![](/new-release-tails-6_15_1/lead.jpg)

This release is an emergency release to fix important security vulnerabilities
in Tor Browser.

## Changes and updates

* Update *Tor Browser* to [14.5.2](https://blog.torproject.org/new-release-tor-browser-1452), which fixes [Mozilla Foundation Security Advisory 2025-37](https://www.mozilla.org/en-US/security/advisories/mfsa2025-37/). These vulnerabilities allow an attacker to perform an out-of-bounds read or write on a JavaScript object, but [don't allow breaking out of the Firefox sandbox](https://blog.mozilla.org/security/2025/05/17/firefox-security-response-to-pwn2own-2025/).
* Update *Thunderbird* to [128.10.1](https://www.thunderbird.net/en-US/thunderbird/128.10.1esr/releasenotes/).
* Remove the *Tor Browser* and *Tor Browser (persistent)* folders: they are not necessary anymore, thanks to the more flexible confinement of *Tor Browser* we introduced in [Tails 6.14.1](/new-release-tails-6_15_1/version_6.14.1/). ([#15028](https://gitlab.tails.boum.org/tails/tails/-/issues/15028))

## Fixed problems

* Fix the *Unsafe Browser* appearing in the window list with the *Tor Browser* icon. ([#20934](https://gitlab.tails.boum.org/tails/tails/-/issues/20934))
* Make reporting an error using *WhisperBack* more robust. ([#20921](https://gitlab.tails.boum.org/tails/tails/-/issues/20921))
* Fix *USB tethering*. ([#20940](https://gitlab.tails.boum.org/tails/tails/-/issues/20940))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Get Tails 6.15.1

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 6.0 or later to 6.15.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 6.15.1 on a new USB stick

Follow our installation instructions:

* [Install from Windows](https://tails.net/install/windows/)
* [Install from macOS](https://tails.net/install/mac/)
* [Install from Linux](https://tails.net/install/linux/)
* [Install from Debian or Ubuntu using the command line and GnuPG](https://tails.net/install/expert/)

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
6.15.1 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-6_15_1/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-6_15_1/&text=This%20release%20is%20an%20emergency%20release%20to%20fix%20important%20security%20vulnerabilities%20in%20Tor%20Browser.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-6_15_1/&text=This%20release%20is%20an%20emergency%20release%20to%20fix%20important%20security%20vulnerabilities%20in%20Tor%20Browser.)
[Bluesky](https://bsky.app/intent/compose?text=This%20release%20is%20an%20emergency%20release%20to%20fix%20important%20security%20vulnerabilities%20in%20Tor%20Browser.%0Ahttps%3A//blog.torproject.org/new-release-tails-6_15_1/)

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