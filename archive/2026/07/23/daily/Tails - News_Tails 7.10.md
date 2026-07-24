---
title: Tails 7.10
url: https://tails.net/news/version_7.10/
source: Tails - News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:32.903329
---

# Tails 7.10

[Skip to main content](#page-body)

[Tails
![](../../lib/logo.png)](../../index.en.html)

Search

[Donate](https://tails.net/donate/)

* [Home](../../index.en.html)
* [How Tails works](../../about/index.en.html)
* [Install Tails](../../install/index.en.html)
* [Documentation](../../doc/index.en.html)
* [Support](../../support/index.en.html)
* [News](../index.en.html)

* [news](../index.en.html)
* Tails 7.10

# Tails 7.10

2026-07-23

* [announce](../../tags/announce/)

# New features

## New shutdown procedure

Tails now uses the standard shutdown procedure from GNOME.

The [standard shutdown](../../doc/first_steps/shutdown/index.en.html) procedure is a bit slower,
but better prevents data loss.

For example, the **Power Off** confirmation dialog informs you if an
application needs to be closed or an open document needs to be saved before
shutting down.

[![](../../doc/first_steps/shutdown/power_off_with_inhibitor.png)](../../doc/first_steps/shutdown/power_off_with_inhibitor.png)

Even without confirming or saving the open documents, Tails will shut down
after 60 seconds.

You can still use the faster [emergency
shutdown](../../doc/first_steps/shutdown/index.en.html#emergency) as before.

## *Celluloid* video player

We replaced *GNOME Videos* with *Celluloid*, a more modern and reliable video
player.

[![](./celluloid.png)](./celluloid.png)

For added security, *Celluloid* cannot access the network. You can
either:

* Open online videos, like MP4 and AVI files, in *Tor Browser*.
* Open online streaming addresses, like IPTV and HLS addresses, in
  *VLC*, installed as [additional
  software](../../doc/persistent_storage/additional_software/index.en.html).

*Celluloid* doesn't work on some computer from 2011 or earlier.

You can use *VLC* instead, installed as [additional
software](../../doc/persistent_storage/additional_software/index.en.html).

# Changes and updates

* Update *Tor Browser* to [15.0.19](https://blog.torproject.org/new-release-tor-browser-15019/).
* Update some firmware packages. This improves support for newer
  hardware: graphics, Wi-Fi, and so on.

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.10

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.10.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.10 on a new USB stick

Follow our [installation instructions](../../install/index.en.html).

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.10 directly:

* [For USB sticks (USB image)](../../install/download/index.en.html)
* [For DVDs and virtual machines (ISO image)](../../install/download-iso/index.en.html)

##### Tails

* [Home](../../index.en.html)
* [How Tails works](../../about/index.en.html)
* [Install Tails](../../install/index.en.html)
* [Documentation](../../nav/doc/index.en.html)
* [Support](../../support/index.en.html)
* [News](../index.en.html)

##### Support

* [FAQs](../../support/faq/index.en.html)
* [Known issues](../../support/known_issues/index.en.html)
* [Warnings](../../doc/about/warnings/index.en.html)
* [Security advisories](../../security/index.en.html)
* [Accessibility](../../doc/first_steps/accessibility/index.en.html)
* [Upgrade](../../doc/upgrade/index.en.html)

##### Contribute

* [Contribute](../../contribute/index.en.html)
* [Report an error](../../doc/first_steps/whisperback/index.en.html)
* [Translate](../../contribute/how/translate/)
* [Source code](../../contribute/how/code/)
* [GitLab](https://gitlab.tails.boum.org/tails/tails/-/issues)
* [Donate](../../donate/index.en.html)

##### About us

* [Contact](../../doc/about/contact/index.en.html)
* [Mission and values](../../contribute/mission/)
* [Social contract](https://community.torproject.org/policies/social_contract/)
* [Supporters](https://www.torproject.org/about/supporters/)
* [Code of conduct](https://community.torproject.org/policies/code_of_conduct/)
* [License](../../doc/about/license/index.en.html)
* [Jobs](../../jobs/)

##### News

Subscribe to our [newsletter](../index.en.html)

Subscribe

![](../../lib/tor-black.png)

Tails is made by the [Tor Project](https://torproject.org/).