---
title: Tails 7.6
url: https://tails.net/news/version_7.6/
source: Tails - News
date: 2026-03-26
fetch_date: 2026-03-27T04:33:29.289584
---

# Tails 7.6

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
* Tails 7.6

# Tails 7.6

2026-03-26

* [announce](../../tags/announce/)

# New features

## Automatic Tor bridges

You can now learn about Tor bridges directly from the *Tor Connection*
assistant in Tails.

Tor bridges are secret Tor relays that hide that you are connecting to Tor.
If connecting to Tor is blocked from where you are, you can use a
bridge as your first Tor relay to circumvent this censorship.

In Tails 7.6, choose **Connect to Tor automatically** when opening *Tor
Connection*. If access to the Tor network is blocked, the bridge configuration
screen offers a new option called **Ask for a Tor bridge based on your
region**.

[![](../../doc/anonymous_internet/tor/bridge.png)](../../doc/anonymous_internet/tor/bridge.png)

This feature uses the same technology as the connection assistant in *Tor
Browser* outside of Tails, which was introduced in [Tor Browser
11.5](https://blog.torproject.org/new-release-tor-browser-115/) (July 2022).

Tails downloads information about bridges that are most likely to work in
your region from the [Moat
API](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/blob/main/doc/moat.md)
of the Tor Project. To circumvent censorship, this connection is disguised as
a connection to another website using [domain fronting](https://en.wikipedia.org/wiki/domain%20fronting).

## GNOME Secrets

In Tails 7.6, the [*Secrets*](https://gitlab.gnome.org/World/secrets) password
manager replaces [*KeePassXC*](https://keepassxc.org/).

*Secrets* has a simpler interface and is better integrated in the GNOME
desktop. For example, accessibility features, such as the screen keyboard and
cursor size, are working again with *Secrets*.

*Secrets* offers to unlock your previous *KeePassXC* database automatically,
because both *Secrets* and *KeePassXC* use the same file format to store
passwords.

If you miss more advanced features from *KeePassXC*, you can install
*KeePassXC* as [additional
software](../../doc/persistent_storage/additional_software/index.en.html).

[![](./secrets.png)](./secrets.png)

The main keyboard shortcuts of *Secrets* are similar to the ones of
*KeePassXC*, with **Shift** in addition to **Ctrl**:

* **Shift+Ctrl+C**: copy password
* **Shift+Ctrl+V**: copy address
* **Shift+Ctrl+B**: copy username
* **Shift+Ctrl+T**: copy one-time password

To see the full list of keyboard shortcuts of *Secrets*, press
**Ctrl+?**.

# Changes and updates

* Update *Electrum* from 4.5.8 to [4.7.0](https://github.com/spesmilo/electrum/blob/master/RELEASE-NOTES).
* Update *Tor Browser* to [15.0.8](https://blog.torproject.org/new-release-tor-browser-1508/).
* Update *Thunderbird* to [140.8.0](https://www.thunderbird.net/en-US/thunderbird/140.8.0esr/releasenotes/).
* Update most firmware packages. This improves support for newer hardware:
  graphics, Wi-Fi, and so on.

# Fixed problems

* Translate the confirmation dialog that appears before saving the language and
  keyboard layout on the USB stick. ([#21448](https://gitlab.tails.boum.org/tails/tails/-/issues/21448))

  [![](./save.png)](./save.png)
* Fix the **Learn More** button in the *Thunderbird* migration notification. ([#21455](https://gitlab.tails.boum.org/tails/tails/-/issues/21455))

  [![](../../doc/anonymous_internet/thunderbird/additional_software/manual.png)](../../doc/anonymous_internet/thunderbird/additional_software/manual.png)
* Fix automated upgrades in Turkish. ([#21466](https://gitlab.tails.boum.org/tails/tails/-/issues/21466))

For more details, read our [changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

# Get Tails 7.6

## To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.6.
* If you cannot do an automatic upgrade or if Tails fails to start after an
  automatic upgrade, please try to do a [manual upgrade](../../doc/upgrade/index.en.html#manual).

## To install Tails 7.6 on a new USB stick

Follow our installation instructions:

* [Install from Windows](../../install/windows/index.en.html)
* [Install from macOS](../../install/mac/index.en.html)
* [Install from Linux](../../install/linux/index.en.html)
* [Install from Debian or Ubuntu using the command line and GnuPG](../../install/expert/index.en.html)

The Persistent Storage on the USB stick will be lost if
you install instead of upgrading.

## To download only

If you don't need installation or upgrade instructions, you can download
Tails 7.6 directly:

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