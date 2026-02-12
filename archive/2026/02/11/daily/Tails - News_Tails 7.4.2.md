---
title: Tails 7.4.2
url: https://tails.net/news/version_7.4.2/
source: Tails - News
date: 2026-02-11
fetch_date: 2026-02-12T04:22:35.499360
---

# Tails 7.4.2

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
* Tails 7.4.2

# Tails 7.4.2

2026-02-11

* [announce](../../tags/announce/)

This release is an emergency release to fix critical security
vulnerabilities in the *Linux* kernel.

# Changes and updates

* Update the *Linux* kernel to 6.12.69, which fixes [DSA
  6126-1](https://lists.debian.org/debian-security-announce/2026/msg00035.html),
  multiple security vulnerabilities that could allow an application in Tails to
  gain administration privileges.

  For example, if an attacker was able to exploit other unknown security
  vulnerabilities in an application included in Tails, they might then use DSA
  6126-1 to take full control of your Tails and deanonymize you.

  This attack is very unlikely, but could be performed by a strong attacker,
  such as a government or a hacking firm. We are not aware of this attack being
  used in practice.
* Update *Thunderbird* to [140.7.1](https://www.thunderbird.net/en-US/thunderbird/140.7.1esr/releasenotes/).

# Fixed problems

* Fix opening the Wi-Fi settings from the *Tor Connection* assistant.
  ([#18587](https://gitlab.tails.boum.org/tails/tails/-/issues/18587))
* Fix reopening *Electrum* when it was not closed cleanly. ([#21390](https://gitlab.tails.boum.org/tails/tails/-/issues/21390))
* Fix applying the language saved to the USB stick in the Welcome Screen.
  ([#21383](https://gitlab.tails.boum.org/tails/tails/-/issues/21383))

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.4.2

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.4.2.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.4.2 on a new USB stick

Follow our installation instructions:

* [Install from Windows](../../install/windows/index.en.html)
* [Install from macOS](../../install/mac/index.en.html)
* [Install from Linux](../../install/linux/index.en.html)
* [Install from Debian or Ubuntu using the command line and GnuPG](../../install/expert/index.en.html)

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.4.2 directly:

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