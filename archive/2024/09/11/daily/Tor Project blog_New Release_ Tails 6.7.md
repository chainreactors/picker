---
title: New Release: Tails 6.7
url: https://blog.torproject.org/new-release-tails-67/
source: Tor Project blog
date: 2024-09-11
fetch_date: 2025-10-06T18:33:50.198708
---

# New Release: Tails 6.7

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 6.7

by [tails](/author/tails)
| September 10, 2024

![](/new-release-tails-67/lead.jpg)

## Changes and updates

* Update *Tor Browser* to [13.5.3](https://blog.torproject.org/new-release-tor-browser-1353).
* Update *Thunderbird* to [115.15.0](https://www.thunderbird.net/en-US/thunderbird/115.15.0esr/releasenotes/).
* Update *OnionShare* from 2.2 to 2.6, which includes a feature to create an anonymous chat room.

## Fixed problems

* Keep the firewall on even during shutdown. ([#20536](https://gitlab.tails.boum.org/tails/tails/-/issues/20536))
* Stop reporting an error when starting an old Tails USB stick with a system partition of 2.5 GB. ([#20519](https://gitlab.tails.boum.org/tails/tails/-/issues/20519))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Known issues

### Shim SBAT verification error

If you get the following error message when starting your regular Linux
operating system, then it means that your Linux operating system is outdated.

Verifying shim SBAT data failed: Security Policy Violation
Something has gone seriously wrong: SBAT self-check failed: Security Policy
Violation

1. Edit your UEFI settings to disable Secure Boot.

With Secure Boot disabled, your regular Linux operating system should start
again.

To learn how to edit the BIOS or UEFI settings, search for the user manual of
the computer on the support website of the manufacturer.

1. Update your regular Linux operating system.
2. Try to enable Secure Boot again in your UEFI settings.

If your regular Linux operating system still doesn't start, then disable
Secure Boot again. You can try to enable Secure Boot again in the future.

It might take several months for your Linux distribution to provide updates
before you can enable Secure Boot again.

## Get Tails 6.7

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 6.0 or later to 6.7.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a manual upgrade.

### To install Tails 6.7 on a new USB stick

Follow our installation instructions:

* Install from Windows
* Install from macOS
* Install from Linux
* Install from Debian or Ubuntu using the command line and GnuPG

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
6.7 directly:

* For USB sticks (USB image)
* For DVDs and virtual machines (ISO image)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**

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