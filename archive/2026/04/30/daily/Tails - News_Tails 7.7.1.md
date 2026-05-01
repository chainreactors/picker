---
title: Tails 7.7.1
url: https://tails.net/news/version_7.7.1/
source: Tails - News
date: 2026-04-30
fetch_date: 2026-05-01T05:39:44.629022
---

# Tails 7.7.1

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
* Tails 7.7.1

# Tails 7.7.1

2026-04-30

* [announce](../../tags/announce/)

This release is an emergency release to fix important security
vulnerabilities in *Tor Browser*.

# Changes and updates

* Update *Tor Browser* to
  [15.0.11](https://blog.torproject.org/new-release-tor-browser-15011/), which
  fixes [several vulnerabilities in *Firefox*
  140.10.1](https://www.mozilla.org/en-US/security/advisories/mfsa2026-36/).

  We are not aware of these vulnerabilities being exploited in practice until now.
* Update *Thunderbird* to [140.10.0](https://www.thunderbird.net/en-US/thunderbird/140.10.0esr/releasenotes/).
* Stop making it possible to start our ISO images from a USB stick.

  Since [2019](../version_3.12/), we recommend *USB images* to start Tails
  from a USB stick, which is by far the most common way of running Tails.

  We still distribute [*ISO images*](../../install/download-iso/index.en.html) to start Tails from
  a DVD or in a virtual machine. Until now, these ISO images worked on USB
  sticks as well, but provided a degraded experience without automatic upgrades
  or Persistent Storage.

  Our ISO images no longer work on USB sticks to save a few megabytes and
  prevent confusion for people who use USB sticks.

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.7.1

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.7.1.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.7.1 on a new USB stick

Follow our [installation instructions](../../install/index.en.html).

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.7.1 directly:

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