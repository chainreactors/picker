---
title: Test 7.0~rc2
url: https://tails.net/news/test_7.0-rc2/
source: Tails - News
date: 2025-08-22
fetch_date: 2025-10-07T00:18:31.028016
---

# Test 7.0~rc2

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
* Test 7.0~rc2

# Test 7.0~rc2

2025-08-21

* [announce](../../tags/announce/)

Tails 7.0~rc2 is the second release candidate of the upcoming Tails 7.0.

We plan to release Tails 7.0 officially on September 18 or on October 16. You can help us by
testing this release candidate already.

Tails 7.0 will be the first version of Tails based on Debian 13 (Trixie) and
GNOME 48. It will bring new versions of many applications included in Tails.

We have tested 7.0~rc2 with the same extensive
[automatic](../../contribute/release_process/test/automated_tests/) and
[manual](../../contribute/release_process/test/) test suites that we use for regular
releases. But, Tails 7.0~rc2 might still contain undiscovered issues.

We will provide automatic security upgrades for Tails 7.0~rc2, like we do for
regular versions.

# Changes and updates

## Changes since 7.0~rc1

* Increase the memory requirements from 2 GB of RAM to 3 GB. ([#21114](https://gitlab.tails.boum.org/tails/tails/-/issues/21114))

  Tails 7.0~rc2 displays a notification when the RAM requirements are not met.

  [![](./ram.png)](./ram.png)

  We estimate that less than 2% of current users will be affected.
* Remove the **Places** menu. ([#21086](https://gitlab.tails.boum.org/tails/tails/-/issues/21086))
* Rename *Root Terminal* as *Root Console*. ([#21110](https://gitlab.tails.boum.org/tails/tails/-/issues/21110))
* Skip the onboarding of *Inkscape*. ([#21091](https://gitlab.tails.boum.org/tails/tails/-/issues/21091))

## Other changes compared with 6.18

* Replace [*GNOME Terminal*](https://gitlab.gnome.org/GNOME/gnome-terminal)
  with [*GNOME Console*](https://apps.gnome.org/Console/). ([#20161](https://gitlab.tails.boum.org/tails/tails/-/issues/20161))
* Replace [*GNOME Image Viewer*](https://wiki.gnome.org/Apps/EyeOfGnome) with
  [*GNOME Loupe*](https://apps.gnome.org/Loupe/) ([#20640](https://gitlab.tails.boum.org/tails/tails/-/issues/20640))
* Remove *Kleopatra* from the Favorites menu. ([#21072](https://gitlab.tails.boum.org/tails/tails/-/issues/21072))

  To start *Kleopatra* choose **Apps ▸ Accessories ▸ Kleopatra**.
* Remove the obsolete Network Connection option from the Welcome Screen.
  ([#21074](https://gitlab.tails.boum.org/tails/tails/-/issues/21074))

## Included software

* Update the *Tor* client to 0.4.8.17.
* Update *Thunderbird* to [128.13.0esr](https://www.thunderbird.net/en-US/thunderbird/128.13.0esr/releasenotes/).
* Update the *Linux* kernel to 6.12.41.

  This improves support for newer hardware: graphics, Wi-Fi, and so on.
* Update *Electrum* from 4.3.4 to 4.5.8.
* Update *OnionShare* from 2.6.2 to 2.6.3.
* Update *KeePassXC* from 2.7.4 to 2.7.10.
* Update *Kleopatra* from 4:22.12 to 4:24.12
* Update *Inkscape* from 1.2.2 to 1.4.
* Update *GIMP* from 2.10.34 to 3.0.4.
* Update *Audacity* from 3.2.4 to 3.7.3.
* Update *Text Editor* from 43.2 to 48.3.
* Update *Document Scanner* from 42.5 to 46.0.

## Removed software

* Remove `unar`. ([#20946](https://gitlab.tails.boum.org/tails/tails/-/issues/20946))
* Remove `aircrack-ng`. ([#21044](https://gitlab.tails.boum.org/tails/tails/-/issues/21044))
* Remove `sq`. ([#21042](https://gitlab.tails.boum.org/tails/tails/-/issues/21042))

# Fixed problems

* Fix selecting the correct keyboard for certain languages. ([#12638](https://gitlab.tails.boum.org/tails/tails/-/issues/12638))

For more details, see the list of [closed issues on the 7.0 milestone in
GitLab](https://gitlab.tails.boum.org/tails/tails/-/issues/?milestone_title=Tails_7.0&state=closed).

# Known issues

* Tails 7.0~rc2 takes longer to start.

  We plan to fix this in the final Tails 7.0.

For more details, see the list of [issues on the 7.0 milestone in
GitLab](https://gitlab.tails.boum.org/groups/tails/-/milestones/144#tab-issues).

# Send your feedback

Please, report any new problem to either:

* tails-testers@boum.org (public mailing list)
* support@tails.net (private email)

# Get Tails 7.0~rc2

### Direct download

* For USB sticks (USB image)

  OpenPGP signature
* For DVDs and virtual machines (ISO image)

  OpenPGP signature

### BitTorrent download

* For USB sticks (USB image)
* For DVDs and virtual machines (ISO image)

## To upgrade your Tails USB stick and keep your Persistent Storage

You can do a [manual upgrade](../../doc/upgrade/index.en.html#manual) to Tails 7.0~rc2.

Automatic upgrades are not available to Tails 7.0~rc2.

## To install Tails 7.0~rc2 on a new USB stick

Follow our installation instructions:

* [Install from Windows](../../install/windows/index.en.html)
* [Install from macOS](../../install/mac/index.en.html)
* [Install from Linux](../../install/linux/index.en.html)
* [Install from Debian or Ubuntu using the command line and GnuPG](../../install/expert/index.en.html)

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

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