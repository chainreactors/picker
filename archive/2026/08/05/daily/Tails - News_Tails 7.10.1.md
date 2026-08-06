---
title: Tails 7.10.1
url: https://tails.net/news/version_7.10.1/
source: Tails - News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:34.604035
---

# Tails 7.10.1

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
* Tails 7.10.1

# Tails 7.10.1

2026-08-05

* [announce](../../tags/announce/)

This release is an emergency release to fix critical security vulnerabilities
in the *Linux* kernel and the *expat* XML library.

# Changes and updates

* Update the *Linux* kernel to 6.12.100, which fixes [CVE-2026-64560](https://www.cve.org/CVERecord?id=CVE-2026-64560),
  a vulnerability that could allow *Tor Browser* in
  Tails to gain administrator privileges.

  For example, if a malicious website that you visit is able to exploit
  CVE-2026-64560, they might take full control of your Tails and deanonymize
  you.

  This attack is very unlikely but could be performed by a strong attacker,
  such as a government or a hacking firm. We are not aware of this attack being
  used in practice until now.
* Update the *expat* XML library to 2.8.2, which fixes
  [DSA-6404-1](https://security-tracker.debian.org/tracker/DSA-6404-1), a set
  of vulnerabilities that could allow different applications in Tails to gain
  administrator privileges.

  For example, if an attacker tricks you into opening a malicious file in an
  application that uses *expat*, such as *LibreOffice*, *Audacity*, or *Git*,
  they might then use one of these vulnerabilities to take full control of your
  Tails and deanonymize you.

  This attack is very unlikely but could be performed by a strong attacker,
  such as a government or a hacking firm. We are not aware of this attack being
  used in practice until now.
* Compress automatic upgrades with `zstd` for a faster startup, as we already
  did for the USB image in [Tails 7.0](../version_7.0/).
* Make USB images and automatic upgrades 70 MB smaller by removing unused
  firmware.

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.10.1

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.10.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.10.1 on a new USB stick

Follow our [installation instructions](../../install/index.en.html).

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.10.1 directly:

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