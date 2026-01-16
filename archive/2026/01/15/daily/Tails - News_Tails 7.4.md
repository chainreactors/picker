---
title: Tails 7.4
url: https://tails.net/news/version_7.4/
source: Tails - News
date: 2026-01-15
fetch_date: 2026-01-16T03:30:32.923118
---

# Tails 7.4

[Skip to main content](#page-body)

[Tails
![](../../lib/logo.png)](../../index.en.html)

Search

[Donate](https://donate.torproject.org/)

* [Home](../../index.en.html)
* [How Tails works](../../about/index.en.html)
* [Install Tails](../../install/index.en.html)
* [Documentation](../../doc/index.en.html)
* [Support](../../support/index.en.html)
* [News](../index.en.html)

* [news](../index.en.html)
* Tails 7.4

# Tails 7.4

2026-01-15

* [announce](../../tags/announce/)

# New feature

## Persistent language and formats

You can now save your language, keyboard layout, and formats from the *Welcome
Screen* to the USB stick. These settings will be applied automatically when
restarting Tails.

If you turn on this option, your language and formats settings are saved
unencrypted on the USB stick to help you type the passphrase of your Persistent
Storage more easily.

[![](./persistent_language.png)](./persistent_language.png)

# Changes and updates

* Update *Tor Browser* to [15.0.4](https://blog.torproject.org/new-release-tor-browser-1504/).
* Update *Thunderbird* to [140.6.0](https://www.thunderbird.net/en-US/thunderbird/140.6.0esr/releasenotes/).
* Update the *Linux* kernel to 6.12.63.
* Drop support for BitTorrent download.

  With the ongoing transition from BitTorrent v1 to v2, the BitTorrent v1 files
  that we provided until now can become a security concern. We don't think that
  updating to BitTorrent v2 is [worth the extra
  migration and maintenance cost](https://gitlab.tails.boum.org/tails/tails/-/issues/19275) for our team.

  Direct download from one of our mirrors is usually faster.

# Fixed problems

* Fix opening *.gpg* encrypted files in *Kleopatra* when double-clicking or
  selecting *Open with Kleopatra* from the shortcut menu. ([#21281](https://gitlab.tails.boum.org/tails/tails/-/issues/21281))
* Fix the desktop crashing when unlocking *VeraCrypt* volumes with a wrong
  password. ([#21286](https://gitlab.tails.boum.org/tails/tails/-/issues/21286))
* Use 24-hour time format consistently in the top navigation bar and the lock
  screen. ([#21310](https://gitlab.tails.boum.org/tails/tails/-/issues/21310))

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.4

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.4.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.4 on a new USB stick

Follow our installation instructions:

* [Install from Windows](../../install/windows/index.en.html)
* [Install from macOS](../../install/mac/index.en.html)
* [Install from Linux](../../install/linux/index.en.html)
* [Install from Debian or Ubuntu using the command line and GnuPG](../../install/expert/index.en.html)

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.4 directly:

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