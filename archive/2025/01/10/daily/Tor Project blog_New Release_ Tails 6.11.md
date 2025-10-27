---
title: New Release: Tails 6.11
url: https://blog.torproject.org/new-release-tails-611/
source: Tor Project blog
date: 2025-01-10
fetch_date: 2025-10-06T20:12:29.482661
---

# New Release: Tails 6.11

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 6.11

by [tails](/author/tails)
| January 9, 2025

![](/new-release-tails-611/lead.jpg)

## Critical security fixes

The vulnerabilities described below were identified during an external
security audit by [Radically Open
Security](https://www.radicallyopensecurity.com/) and disclosed responsibly to
our team. We are not aware of these attacks being used against Tails users
until now.

These vulnerabilities can only be exploited by a powerful attacker who has
already exploited another vulnerability to take control of an application in
Tails.

If you want to be extra careful and used Tails a lot since January 9 without
upgrading, we recommend that you do a [manual
upgrade](https://tails.net/upgrade/#manual) instead of an automatic upgrade.

* Prevent an attacker from installing malicious software permanently. ([#20701](https://gitlab.tails.boum.org/tails/tails/-/issues/20701))

  In Tails 6.10 or earlier, an attacker who has already taken control of an
  application in Tails could then exploit a vulnerability in *Tails Upgrader* to
  install a malicious upgrade and permanently take control of your Tails.

  Doing a [manual upgrade](https://tails.net/upgrade/#manual) would erase such
  malicious software.
* Prevent an attacker from monitoring online activity. ([#20709](https://gitlab.tails.boum.org/tails/tails/-/issues/20709) and [#20702](https://gitlab.tails.boum.org/tails/tails/-/issues/20702))

  In Tails 6.10 or earlier, an attacker who has already taken control of an
  application in Tails could then exploit vulnerabilities in other applications
  that might lead to deanonymization or the monitoring of browsing activity:

  + In *Onion Circuits* , to get information about Tor circuits and close them.
  + In *Unsafe Browser* , to connect to the Internet without going through Tor.
  + In *Tor Browser* , to monitor your browsing activity.
  + In *Tor Connection* , to reconfigure or block your connection to the Tor network.
* Prevent an attacker from changing the Persistent Storage settings. ([#20710](https://gitlab.tails.boum.org/tails/tails/-/issues/20710))

## New features

### Detection of partitioning errors

Sometimes, the partitions on a Tails USB stick get corrupted. This creates
errors with the Persistent Storage or during upgrades. Partitions can get
corrupted because of broken or counterfeit hardware, software errors, or
physically removing the USB stick while Tails is running.

Tails now warns about such partitioning errors earlier. For example, if
partitioning errors are detected when there is no Persistent Storage, Tails
recommends that you reinstall or use a new USB stick.

## Changes and updates

* Update *Tor Browser* to [14.0.4](https://blog.torproject.org/new-release-tor-browser-1404).
* Update *Thunderbird* to [128.5.0esr](https://www.thunderbird.net/en-US/thunderbird/128.5.0esr/releasenotes/).
* Remove support for hardware wallets in *Electrum*. Trezor wallets stopped working in Debian 12 (Bookworm), and so in Tails 6.0 or later.
* Disable *GNOME Text Editor* from reopening on the last file. ([#20704](https://gitlab.tails.boum.org/tails/tails/-/issues/20704))
* Add a link to the *Tor Connection* assistant from the menu of the Tor status icon on the desktop.
* Make it easier for our team to find useful information in *WhisperBack* reports.

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Get Tails 6.11

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 6.0 or later to 6.11.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 6.11 on a new USB stick

Follow our installation instructions:

* [Install from Windows](https://tails.net/install/windows/)
* [Install from macOS](https://tails.net/install/mac/)
* [Install from Linux](https://tails.net/install/linux/)
* [Install from Debian or Ubuntu using the command line and GnuPG](https://tails.net/install/expert/)

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
6.11 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-611/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-611/&text=Tails%206.11%20fixes%20several%20critical%20security%20vulnerabilities%20that%20were%20identified%20during%20an%20external%20audit.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-611/&text=Tails%206.11%20fixes%20several%20critical%20security%20vulnerabilities%20that%20were%20identified%20during%20an%20external%20audit.)
[Bluesky](https://bsky.app/intent/compose?text=Tails%206.11%20fixes%20several%20critical%20security%20vulnerabilities%20that%20were%20identified%20during%20an%20external%20audit.%0Ahttps%3A//blog.torproject.org/new-release-tails-611/)

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