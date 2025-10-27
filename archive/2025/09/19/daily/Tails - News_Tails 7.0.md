---
title: Tails 7.0
url: https://tails.net/news/version_7.0/
source: Tails - News
date: 2025-09-19
fetch_date: 2025-10-02T20:23:39.484446
---

# Tails 7.0

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
* Tails 7.0

# Tails 7.0

2025-09-18

* [announce](../../tags/announce/)

We are very excited to present you Tails 7.0, the first version of Tails based
on Debian 13 (Trixie) and GNOME 48 (Bengaluru). Tails 7.0 brings new versions
of many applications included in Tails.

# Dedication

Tails 7.0 is dedicated to the memory of Lunar (1982–2024).
Lunar was a traveling companion for Tails, a Tor volunteer, Free Software hacker,
and community organizer.

Lunar has always been by our side throughout Tails' history.
From the first baby steps of the project that eventually became Tails, to the
merge with Tor, he's provided sensible technical suggestions, out-of-the-box
product design ideas, outreach support, and caring organizational advice.

Outside of Tor, Lunar worked on highly successful Free Software projects such
as the [Debian](https://www.debian.org/) project, the Linux distribution on
which Tails is based, and the [Reproducible
Builds](https://reproducible-builds.org/) project, which helps us verify the
[integrity of Tails releases](../../contribute/build/reproducible/).

Lunar will be deeply missed, both in our community and in the many other
communities he participated in.

See also
[what other projects have written about Lunar](https://lunar.anargeek.net/liens/#autres-sites).

# Changes and updates

## Faster startup

Tails 7.0 starts 10–15 seconds faster on most computers.

We achieve this by changing the compression algorithm of the Tails USB and ISO
images from `xz` to `zstd`. As a consequence, the image is 10% bigger than it
would be with the previous algorithm.

While testing this change, we noticed that Tails on USB sticks of poor quality
can also start 20 seconds slower than on quality USB sticks.

If you are in a place where counterfeit electronics are common, we recommend
that you buy your USB stick from an international supermarket chain, which
should have a more reliable supply chain.

## Included software

* Replace [*GNOME Terminal*](https://gitlab.gnome.org/GNOME/gnome-terminal)
  with [*GNOME Console*](https://apps.gnome.org/Console/).
* Replace [*GNOME Image Viewer*](https://wiki.gnome.org/Apps/EyeOfGnome) with
  [*GNOME Loupe*](https://apps.gnome.org/Loupe/).
* Update *Tor Browser* to [14.5.7](https://blog.torproject.org/new-release-tor-browser-1457).
* Update the *Tor* client to 0.4.8.17.
* Update *Thunderbird* to [128.14.0esr](https://www.thunderbird.net/en-US/thunderbird/128.14.0esr/releasenotes/).
* Update *Electrum* from 4.3.4 to [4.5.8](https://github.com/spesmilo/electrum/blob/master/RELEASE-NOTES).
* Update *OnionShare* from 2.6.2 to [2.6.3](https://github.com/onionshare/onionshare/blob/main/CHANGELOG.md).
* Update *KeePassXC* from 2.7.4 to [2.7.10](https://github.com/keepassxreboot/keepassxc/blob/develop/CHANGELOG.md).
* Update *Kleopatra* from 4:22.12 to 4:24.12
* Update *Inkscape* from 1.2.2 to 1.4.
* Update *GIMP* from 2.10.34 to [3.0.4](https://www.gimp.org/release-notes/gimp-3.0.html).
* Update *Audacity* from 3.2.4 to 3.7.3.
* Update *Text Editor* from 43.2 to 48.3.
* Update *Document Scanner* from 42.5 to 46.0.

## Changes in GNOME

* Many sections of the *Settings* utility have been redesigned, for example
  Accessibility, Sound, and Mouse & Keyboard in [GNOME
  44](https://release.gnome.org/44/)

  Accessibility settings also include new accessibility features, such as
  Overamplication and Always Show Scrollbars.
* The Activities button has been replaced with a dynamic workspace indicator in
  [GNOME 45](https://release.gnome.org/45/).

  [![](../../doc/first_steps/desktop/upper-left.png)](../../doc/first_steps/desktop/upper-left.png)
* The Screen Reader has been improved in different ways, for example, with
  better table navigation and a sleep mode in [GNOME
  46](https://release.gnome.org/46/).
* A new option to preserve battery health is available in the power settings in
  [GNOME 48](https://release.gnome.org/48/).

## Removals

* Remove the **Places** menu.

  You can access the same shortcuts from the sidebar of the *Files* browser.
* Remove *Kleopatra* from the Favorites menu.

  To start *Kleopatra*, choose **Apps ▸ Accessories ▸ Kleopatra**.
* Remove `unar`.

  The *File Roller* utility still opens most RAR archives.
* Remove the `aircrack-ng` package.

  You can still install `aircrack-ng` using the [Additional
  Software](../../doc/persistent_storage/additional_software/index.en.html) feature.
* Remove the *Power Statistics* utility.
* Remove the `sq` package.
* Remove the obsolete Network Connection option from the Welcome Screen.

## Hardware support

* Update the *Linux* kernel to 6.12.43.

  This improves support for newer hardware: graphics, Wi-Fi, and so on.
* Increase the memory requirements from 2 GB of RAM to 3 GB. ([#21114](https://gitlab.tails.boum.org/tails/tails/-/issues/21114))

  Tails 7.0 displays a notification when the RAM requirements are not met.

  [![](../test_7.0-rc2/ram.png)](../test_7.0-rc2/ram.png)

  We estimate that less than 2% of users are affected.

# Fixed problems

* Fix selecting the correct keyboard for certain languages. ([#12638](https://gitlab.tails.boum.org/tails/tails/-/issues/12638))

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.0

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are only available from Tails 7.0~rc1 and 7.0~rc2 to 7.0.

  All other users have to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.0 on a new USB stick

Follow our installation instructions:

* [Install from Windows](../../install/windows/index.en.html)
* [Install from macOS](../../install/mac/index.en.html)
* [Install from Linux](../../install/linux/index.en.html)
* [Install from Debian or Ubuntu using the command line and GnuPG](../../install/expert/index.en.html)

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.0 directly:

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

#...