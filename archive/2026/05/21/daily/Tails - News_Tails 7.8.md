---
title: Tails 7.8
url: https://tails.net/news/version_7.8/
source: Tails - News
date: 2026-05-21
fetch_date: 2026-05-22T06:08:41.216337
---

# Tails 7.8

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
* Tails 7.8

# Tails 7.8

2026-05-21

* [announce](../../tags/announce/)

# Changes and updates

* Update *Tor Browser* to [15.0.14](https://blog.torproject.org/new-release-tor-browser-15014/).
* Remove *Thunderbird*.

  You can still [install *Thunderbird* as additional
  software](../../doc/anonymous_internet/thunderbird/index.en.html).

  If you have both the **Thunderbird Email Client** and **Additional Software**
  features of the Persistent Storage turned on, Tails automatically adds
  *Thunderbird* to your list of [additional
  software](../../doc/persistent_storage/additional_software/index.en.html).

  A new version of *Thunderbird* is released in Debian shortly after each Tails
  release, because both *Tails* and *Thunderbird* follow the [release calendar
  of *Firefox*](https://whattrainisitnow.com/calendar/). As a consequence,
  until Tails 7.5 (February 2026), the version of *Thunderbird* in Tails was
  almost always outdated, with known security vulnerabilities.

  By installing *Thunderbird* as additional software, the latest version
  of *Thunderbird* is installed automatically from your Persistent Storage each
  time you start Tails.

# Fixed problems

* Fix multiple security vulnerabilities in the Linux kernel and haveged, that
  could allow an application in Tails to gain administration privileges.

  For example, if an attacker was able to exploit other unknown security
  vulnerabilities in an application included in Tails, they might then use one
  of these vulnerabilities to take full control of your Tails and
  deanonymize you.

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.8

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.8.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.8 on a new USB stick

Follow our installation instructions:

* [Install from Windows](../../install/windows/index.en.html)
* [Install from macOS](../../install/mac/index.en.html)
* [Install from Linux](../../install/linux/index.en.html)
* [Install from Debian or Ubuntu using the command line and GnuPG](../../install/expert/index.en.html)

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.8 directly:

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