---
title: New Release: Tails 5.10
url: https://blog.torproject.org/new-release-tails-510/
source: Tor Project blog
date: 2023-02-17
fetch_date: 2025-10-04T06:54:42.315559
---

# New Release: Tails 5.10

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 5.10

by [tails](/author/tails)
| February 16, 2023

![](/new-release-tails-510/lead.jpg)

# Changes and updates

* Update *Tor Browser* to [12.0.3](https://blog.torproject.org/new-release-tor-browser-1203).
* Ask for confirmation when starting without unlocking the Persistent Storage.
* Update our [documentation on the Persistent Storage](https://tails.boum.org/doc/persistent_storage/).

# Fixed problems

* Avoid crashing when the download of an upgrade is stopped and resumed. ([#18435](https://gitlab.tails.boum.org/tails/tails/-/issues/18435))
* Solve a possible privilege escalation through a symlink attack. ([#19424](https://gitlab.tails.boum.org/tails/tails/-/issues/19424))

  Dennis's Brinkrolf discovered that an adversary who could already run arbitrary
  code as the amnesia user in Tails 5.9, could have escalated their privileges
  to reading arbitrary files on the system. It might have been possible to use
  this as part of an exploit chain to gain root privileges.

## Persistent Storage

* Avoid opening the Persistent Storage settings each time after login. ([#19410](https://gitlab.tails.boum.org/tails/tails/-/issues/19410))
* Solve some cases of failure to activate the Persistent Storage by bumping the unlocking timeout to 120 seconds. ([#19432](https://gitlab.tails.boum.org/tails/tails/-/issues/19432))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Known issues

None specific to this release.

See the list of [long-standing
issues](https://tails.boum.org/support/known_issues/).

# Get Tails 5.10

## To upgrade your Tails USB stick and keep your persistent storage

* Automatic upgrades are available from Tails 5.0 or later to 5.10.

  You can [reduce the size of the download](https://tails.boum.org/doc/upgrade/#reduce) of future automatic upgrades by doing a manual upgrade to the latest version.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.boum.org/doc/upgrade/#manual).

## To install Tails on a new USB stick

Follow our installation instructions:

* [Install from Windows](https://tails.boum.org/install/windows/)
* [Install from macOS](https://tails.boum.org/install/mac/)
* [Install from Linux](https://tails.boum.org/install/linux/)
* [Install from Debian or Ubuntu using the command line and GnuPG](https://tails.boum.org/install/expert/)

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download Tails
5.10 directly:

* [For USB sticks (USB image)](https://tails.boum.org/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.boum.org/install/download-iso/)

# What's coming up?

Tails 5.11 is [scheduled](https://tails.boum.org/contribute/calendar/) for
March 14.

Have a look at our [roadmap](https://tails.boum.org/contribute/roadmap) to see
where we are heading to.

# Support and feedback

For support and feedback, visit the [Support
section](https://tails.boum.org/support/) on the Tails website.

* [partners](/category/partners)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-510/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-510/&text=Tails%205.10%20is%20out.%20It%20fixes%20small%20issues%20in%20the%20Persistent%20Storage%20and%20Upgrader.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-510/&text=Tails%205.10%20is%20out.%20It%20fixes%20small%20issues%20in%20the%20Persistent%20Storage%20and%20Upgrader.)
[Bluesky](https://bsky.app/intent/compose?text=Tails%205.10%20is%20out.%20It%20fixes%20small%20issues%20in%20the%20Persistent%20Storage%20and%20Upgrader.%0Ahttps%3A//blog.torproject.org/new-release-tails-510/)

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