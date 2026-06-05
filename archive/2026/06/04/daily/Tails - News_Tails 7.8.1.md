---
title: Tails 7.8.1
url: https://tails.net/news/version_7.8.1/
source: Tails - News
date: 2026-06-04
fetch_date: 2026-06-05T06:14:15.830713
---

# Tails 7.8.1

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
* Tails 7.8.1

# Tails 7.8.1

2026-06-04

* [announce](../../tags/announce/)

This release is an emergency release to fix a serious security vulnerability in
the Linux kernel, as well as security vulnerabilities in the *Tor* client.

# Changes and updates

* Update the *Tor* client to 0.4.9.9, which fixes [several security
  vulnerabilities](https://gitlab.torproject.org/tpo/core/tor/-/raw/release-0.4.9/ReleaseNotes).
* Update the *Linux* kernel to 6.12.90-2, which fixes
  [CVE-2026-43503](https://security-tracker.debian.org/tracker/CVE-2026-43503),
  a vulnerability that could allow an application in Tails to gain
  administration privileges.

  For example, if an attacker was able to exploit other unknown security
  vulnerabilities in an application included in Tails, they might then use this
  vulnerability to take full control of your Tails and deanonymize you.

  This attack is very unlikely, but could be performed by a strong attacker,
  such as a government or a hacking firm. We are not aware of this vulnerability
  being used in practice until now.

# Get Tails 7.8.1

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.8.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.8.1 on a new USB stick

Follow our [installation instructions](../../install/index.en.html).

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.8.1 directly:

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