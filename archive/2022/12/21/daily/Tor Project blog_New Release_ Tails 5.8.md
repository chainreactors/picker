---
title: New Release: Tails 5.8
url: https://blog.torproject.org/new-release-tails-58/
source: Tor Project blog
date: 2022-12-21
fetch_date: 2025-10-04T02:10:14.935006
---

# New Release: Tails 5.8

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 5.8

by [tails](/author/tails)
| December 20, 2022

![](/new-release-tails-58/lead.jpg)

Tails 5.8 is the most important release of Tails in years. It includes both
major redesign of existing features, important usability improvements, and
hardened security.

This work has been made possible by donations from users like you. If you like
these changes and want more, donate now to fund our work in 2023.

[**Donate now to fund our work in 2023.**](https://tails.boum.org/donate/)

# New features

## New Persistent Storage

After 2 years of hard work, we are extremelly proud to present you a complete
redesign of the Persistent Storage.

The Persistent Storage hasn't changed much since its first release in 2012
because the code was hard to modify and improve. But, we learned from users
that the Persistent Storage could do a lot more for you if it had more
features and was easier to use.

![Screenshot showing Persistent Storage creation](/new-release-tails-58/create.png)

![Screenshot showing Persistent Storage configuration](/new-release-tails-58/configure.png)

* You don't have to restart anymore after creating the Persistent Storage or each time you activate a new feature.
* You can change the password of your Persistent Storage from this new application.
* You can choose to create a Persistent Storage directly from the Welcome Screen, if you don't have one already.

  ![Screenshot showing offer to create Persistent Storage](/new-release-tails-58/onboard.png)

## Wayland and better Unsafe Browser

We replaced the deprecated X.Org display system with Wayland.

Even if you won't notice any visual difference, Wayland brings more security
in depth to Tails by making it harder for a compromised application in Tails
to compromise or misuse another application.

For example, since [Tails 4.8](/new-release-tails-58/version_4.8/), the *Unsafe Browser* was
disabled by default because a security vulnerability in another application in
Tails could start an invisible *Unsafe Browser* , reveal your IP address, and
[deanonymize
you](https://tails.boum.org/doc/anonymous_internet/unsafe_browser/#security).

Wayland fixes this vulnerability and makes it safe to reenable the *Unsafe
Browser* by default. You can still disable the *Unsafe Browser* in the Welcome
Screen.

Wayland also brings in other features that were not working yet in the *Unsafe
Browser* :

* Sound
* Uploads and downloads
* Alternative input methods for Chinese and other non-Latin languages
* Accessibility features like the screen reader and virtual keyboard

## QR code scanning of Tor bridges

We made it easier to enter new Tor bridges in Tails by scanning a QR code.

To get a QR code, you can either:

* Send an empty email to bridges@torproject.org from a Gmail or Riseup email address.
* Get bridges from <https://bridges.torproject.org/> and print the QR code on paper.

We are aware that the QR codes that are currently provided are too big to be
easy to scan. We are [working with
Tor](https://gitlab.torproject.org/tpo/anti-censorship/bridgedb/-/issues/40052) to make them smaller and easier to scan.

![Screenshot showing QR code scanning](/new-release-tails-58/qr_code.png)

# Changes and updates

* Update *Tor Browser* to [12.0.1](https://blog.torproject.org/new-release-tor-browser-1201).
* Update *Thunderbird* to [102.6.0](https://www.thunderbird.net/en-US/thunderbird/102.6.0/releasenotes/).
* Update *Tor* to 0.4.7.12.

# Fixed problems

We fixed 3 usability issues in the *Tor Connection* assistant:

* Display a percentage on the connection progress bar. ([#19208](https://gitlab.tails.boum.org/tails/tails/-/issues/19208))

  ![Screenshot showing Tor connection progress bar](/new-release-tails-58/progress.png)
* Fix links to documentation. ([#19172](https://gitlab.tails.boum.org/tails/tails/-/issues/19172))
* Add a **Bridge** label in front of the line to enter a custom bridge. ([#19169](https://gitlab.tails.boum.org/tails/tails/-/issues/19169))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Known issues

* The switches that turn on and off the different features of the Persistent Storage are very slow to respond on some USB sticks. Please report on [#19291](https://gitlab.tails.boum.org/tails/tails/-/issues/19291) if this happens to you.
* The top of the Welcome Screen is cut out on small displays (800Ã600), like virtual machines. ([#19324](https://gitlab.tails.boum.org/tails/tails/-/issues/19324))

You can press **Alt+S** to start Tails.

* When using a custom Tor `obfs4` bridge, the progress bar of *Tor Connection* sometimes gets stuck halfway through and becomes extremelly slow. ([#19173](https://gitlab.tails.boum.org/tails/tails/-/issues/19173))

To fix this, you can either:

```
* Close and reopen _Tor Connection_ to speed up the initial connection.

* Try a different `obfs4` bridge.
```

This issue only affects outdated obfs4 bridges and does not happen with obfs4
bridges that run version 0.0.12 or later.

See the list of [long-standing
issues](https://tails.boum.org/support/known_issues/).

# Get Tails 5.8

## To upgrade your Tails USB stick and keep your persistent storage

* Automatic upgrades are available from Tails 5.0 or later to 5.8.

You can [reduce the size of the
download](https://tails.boum.org/doc/upgrade/#reduce) of future automatic
upgrades by doing a manual upgrade to the latest version.

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
5.8 directly:

* [For USB sticks (USB image)](https://tails.boum.org/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.boum.org/install/download-iso/)

# Support and feedback

For support and feedback, visit the [Support
section](https://tails.boum.org/support/) on the Tails website.

* [partners](/category/partners)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-58/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-58/&text=Tails%205.8%20is%20the%20most%20important%20release%20of%20Tails%20in%20years.%20It%20includes%20both%20major%20redesign%20of%20existing%20features%2C%20important%20usability%20improvements%2C%20and%20hardened%20security.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-58/&text=Tails%205.8%20is%20the%20most%20important%20release%20of%20Tails%20in%20years.%20It%20includes%20both%20major%20redesign%20of%20existing%20features%2C%20important%20usability%20improvements%2C%20and%20hardened%20security.)
[Bluesky](https://bsky.app/intent/compose?text=Tails%205.8%20is%20the%20most%20important%20release%20of%20Tails%20in%20years.%20It%20includes%20both%20major%20redesign%20of%20existing%20features%2C%20important%20usability%20improvements%2C%20and%20hardened%20security.%0Ahttps%3A//blog.torproject.org/new-release-tails-58/)

## Comments

We encourage respectful...