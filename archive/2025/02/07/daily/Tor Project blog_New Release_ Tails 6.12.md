---
title: New Release: Tails 6.12
url: https://blog.torproject.org/new-release-tails-6-12/
source: Tor Project blog
date: 2025-02-07
fetch_date: 2025-10-06T20:47:14.687419
---

# New Release: Tails 6.12

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 6.12

by [tails](/author/tails)
| February 6, 2025

![](/new-release-tails-6-12/lead.jpg)

## Important security fixes

The vulnerabilities described below were identified during an external
security audit by [Radically Open
Security](https://www.radicallyopensecurity.com/) and disclosed responsibly to
our team. We are not aware of these attacks being used against Tails users
until now.

These vulnerabilities can only be exploited by a powerful attacker who has
already exploited another vulnerability to take control of an application in
Tails.

* Prevent an attacker from monitoring Tor circuits. ([#20733](https://gitlab.tails.boum.org/tails/tails/-/issues/20733) and [#20744](https://gitlab.tails.boum.org/tails/tails/-/issues/20744))

  In Tails 6.11 or earlier, an attacker who has already taken control of an
  application in Tails could then exploit vulnerabilities in *Onion Circuits*
  and our *Tor Browser* wrapper that might lead to deanonymization.
* Prevent an attacker from changing the Persistent Storage settings. ([#20745](https://gitlab.tails.boum.org/tails/tails/-/issues/20745))

## Changes and updates

* Add a button to check for upgrades from the **About Tails** utility.

  ![](https://tails.net/news/version_6.12/check_for_upgrades.png)
* Add the keyboard shortcut **Ctrl+Alt+T** to open a *Terminal*.
* Update *Tor Browser* to [14.0.5](https://blog.torproject.org/new-release-tor-browser-1405).
* Update *Thunderbird* to [128.6.0esr](https://www.thunderbird.net/en-US/thunderbird/128.6.0esr/releasenotes/).

## Fixed problems

* Ensure all our Python code keeps running in *isolated mode*. ([#20719](https://gitlab.tails.boum.org/tails/tails/-/issues/20719))
* Simplify the troubleshooting instructions when an automatic upgrade fails. ([#20466](https://gitlab.tails.boum.org/tails/tails/-/issues/20466))
* Avoid freezing the Welcome Screen while activating the Persistent Storage. ([#20635](https://gitlab.tails.boum.org/tails/tails/-/issues/20635))
* Made time synchronization more reliable when restarting Tor. ([#20530](https://gitlab.tails.boum.org/tails/tails/-/issues/20530))
* Display an error message when upgrading the encryption of the Persistent Storage to LUKS2 fails. ([#20634](https://gitlab.tails.boum.org/tails/tails/-/issues/20634))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Get Tails 6.12

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 6.0 or later to 6.12.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 6.12 on a new USB stick

Follow our installation instructions:

* [Install from Windows](https://tails.net/install/windows/)
* [Install from macOS](https://tails.net/install/mac/)
* [Install from Linux](https://tails.net/install/linux/)
* [Install from Debian or Ubuntu using the command line and GnuPG](https://tails.net/install/expert/)

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
6.12 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-6-12/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-6-12/&text=Tails%206.12%20is%20out.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-6-12/&text=Tails%206.12%20is%20out.)
[Bluesky](https://bsky.app/intent/compose?text=Tails%206.12%20is%20out.%0Ahttps%3A//blog.torproject.org/new-release-tails-6-12/)

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