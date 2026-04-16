---
title: Tails 7.6.2
url: https://tails.net/news/version_7.6.2/
source: Tails - News
date: 2026-04-15
fetch_date: 2026-04-16T04:53:45.542510
---

# Tails 7.6.2

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
* Tails 7.6.2

# Tails 7.6.2

2026-04-15

* [announce](../../tags/announce/)

This release is an emergency release to fix an important security
vulnerability in the confinement of *Tor Browser*.

# Changes and updates

* Update *Flatpak* to 1.16.6, which fixes
  [CVE-2026-34078](https://www.cve.org/CVERecord?id=CVE-2026-34078), a major
  sandbox escape vulnerability. Using this vulnerability, an attacker could
  break the [security confinement of *Tor
  Browser*](../../doc/anonymous_internet/Tor_Browser/index.en.html#confinement) and access all
  files that don't require an administration password, including in the
  Persistent Storage.

  This vulnerability can only be exploited by a powerful attacker who has
  already exploited another vulnerability to take control of *Tor
  Browser*.

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.6.2

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.6.2.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.6.2 on a new USB stick

Follow our [installation instructions](../../install/index.en.html).

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.6.2 directly:

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