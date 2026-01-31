---
title: Tails 7.4.1
url: https://tails.net/news/version_7.4.1/
source: Tails - News
date: 2026-01-30
fetch_date: 2026-01-31T04:04:52.075229
---

# Tails 7.4.1

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
* Tails 7.4.1

# Tails 7.4.1

2026-01-30

* [announce](../../tags/announce/)

This release is an emergency release to fix critical security vulnerabilities
in OpenSSL, a network encryption library used by Tor.

# Changes and updates

## Included software

* Update the OpenSSL library to 3.5.4, which fixes [DSA
  6113-1](https://lists.debian.org/debian-security-announce/2026/msg00022.html),
  a set of vulnerabilities that could be critical. Using this set of
  vulnerabilities, an malicious Tor relay might be able to deanonymize a Tails
  user.

  We are not aware of these vulnerabilities being exploited in practice.
* Update the *Tor* client to 0.4.8.22.
* Update *Thunderbird* to [140.7.0](https://www.thunderbird.net/en-US/thunderbird/140.7.0esr/releasenotes/).

# Fixed problems

* Fix Gmail authentication in *Thunderbird*. ([#21384](https://gitlab.tails.boum.org/tails/tails/-/issues/21384))
* Add a spinner when opening the Wi-Fi settings from the Tor Connection
  assistant. ([#18594](https://gitlab.tails.boum.org/tails/tails/-/issues/18594))

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Known issues

The homepage of Tor Browser incorrectly says you are still using Tails 7.4, even
after you have upgraded to 7.4.1. It also links to the release notes for that
older version.

If in doubt, to verify that you are using Tails 7.4.1, choose **Apps ▸
Tails ▸ About Tails**.

# Get Tails 7.4.1

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.4.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.4.1 on a new USB stick

Follow our installation instructions:

* [Install from Windows](../../install/windows/index.en.html)
* [Install from macOS](../../install/mac/index.en.html)
* [Install from Linux](../../install/linux/index.en.html)
* [Install from Debian or Ubuntu using the command line and GnuPG](../../install/expert/index.en.html)

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.4.1 directly:

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