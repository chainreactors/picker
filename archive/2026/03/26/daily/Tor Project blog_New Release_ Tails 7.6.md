---
title: New Release: Tails 7.6
url: https://blog.torproject.org/new-release-tails-7_6/
source: Tor Project blog
date: 2026-03-26
fetch_date: 2026-03-27T04:33:47.124783
---

# New Release: Tails 7.6

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tails 7.6

by [tails](/author/tails)
| March 26, 2026

![](/new-release-tails-7_6/lead.jpg)

## New features

### Automatic Tor bridges

You can now learn about Tor bridges directly from the *Tor Connection*
assistant in Tails.

Tor bridges are secret Tor relays that hide that you are connecting to Tor. If
connecting to Tor is blocked from where you are, you can use a bridge as your
first Tor relay to circumvent this censorship.

In Tails 7.6, choose **Connect to Tor automatically** when opening *Tor
Connection*. If access to the Tor network is blocked, the bridge configuration
screen offers a new option called **Ask for a Tor bridge based on your
region**.

[![](https://tails.net/doc/anonymous_internet/tor/bridge.png)](https://tails.net/doc/anonymous_internet/tor/bridge.png)

This feature uses the same technology as the connection assistant in *Tor
Browser* outside of Tails, which was introduced in [Tor Browser
11.5](https://blog.torproject.org/new-release-tor-browser-115/) (July 2022).

Tails downloads information about bridges that are most likely to work in your
region from the [Moat API](https://gitlab.torproject.org/tpo/anti-censorship/rdsys/-/blob/main/doc/moat.md) of the Tor Project. To circumvent
censorship, this connection is disguised as a connection to another website
using [domain fronting](https://en.wikipedia.org/wiki/domain%20fronting).

### GNOME Secrets

In Tails 7.6, the [*Secrets*](https://gitlab.gnome.org/World/secrets) password
manager replaces [*KeePassXC*](https://keepassxc.org/).

*Secrets* has a simpler interface and is better integrated in the GNOME
desktop. For example, accessibility features, such as the screen keyboard and
cursor size, are working again with *Secrets*.

*Secrets* offers to unlock your previous *KeePassXC* database automatically,
because both *Secrets* and *KeePassXC* use the same file format to store
passwords.

If you miss more advanced features from *KeePassXC* , you can install
*KeePassXC* as [additional
software](https://tails.net/doc/persistent_storage/additional_software/).

[![](https://tails.net/news/version_7.6/secrets.png)](https://tails.net/news/version_7.6/secrets.png)

The main keyboard shortcuts of *Secrets* are similar to the ones of
*KeePassXC* , with **Shift** in addition to **Ctrl** :

* **Shift+Ctrl+C** : copy password
* **Shift+Ctrl+V** : copy address
* **Shift+Ctrl+B** : copy username
* **Shift+Ctrl+T** : copy one-time password

To see the full list of keyboard shortcuts of *Secrets* , press **Ctrl+?**.

## Changes and updates

* Update *Electrum* from 4.5.8 to [4.7.0](https://github.com/spesmilo/electrum/blob/master/RELEASE-NOTES).
* Update *Tor Browser* to [15.0.8](https://blog.torproject.org/new-release-tor-browser-1508/).
* Update *Thunderbird* to [140.8.0](https://www.thunderbird.net/en-US/thunderbird/140.8.0esr/releasenotes/).
* Update most firmware packages. This improves support for newer hardware: graphics, Wi-Fi, and so on.

## Fixed problems

* Translate the confirmation dialog that appears before saving the language and keyboard layout on the USB stick. ([#21448](https://gitlab.tails.boum.org/tails/tails/-/issues/21448))

[![](https://tails.net/news/version_7.6/save.png)](https://tails.net/news/version_7.6/save.png)

* Fix the **Learn More** button in the *Thunderbird* migration notification. ([#21455](https://gitlab.tails.boum.org/tails/tails/-/issues/21455))

[![](https://tails.net/doc/anonymous_internet/thunderbird/additional_software/manual.png)](https://tails.net/doc/anonymous_internet/thunderbird/additional_software/manual.png)

* Fix automated upgrades in Turkish. ([#21466](https://gitlab.tails.boum.org/tails/tails/-/issues/21466))

For more details, read our
[changelog](https://gitlab.tails.boum.org/tails/tails/-/blob/master/debian/changelog).

## Get Tails 7.6

### To upgrade your Tails USB stick and keep your Persistent Storage

* Automatic upgrades are available from Tails 7.0 or later to 7.6.
* If you cannot do an automatic upgrade or if Tails fails to start after an automatic upgrade, please try to do a [manual upgrade](https://tails.net/doc/upgrade/#manual).

### To install Tails 7.6 on a new USB stick

Follow our installation instructions:

* [Install from Windows](https://tails.net/install/windows/)
* [Install from macOS](https://tails.net/install/mac/)
* [Install from Linux](https://tails.net/install/linux/)
* [Install from Debian or Ubuntu using the command line and GnuPG](https://tails.net/install/expert/)

The Persistent Storage on the USB stick will be lost if you install instead of
upgrading.

### To download only

If you don't need installation or upgrade instructions, you can download Tails
7.6 directly:

* [For USB sticks (USB image)](https://tails.net/install/download/)
* [For DVDs and virtual machines (ISO image)](https://tails.net/install/download-iso/)

## Support and feedback

For support and feedback, visit the [Support
section](https://tails.net/support/) on the Tails website.

* [tails](/category/tails)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tails-7_6/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tails-7_6/&text=Tails%207.6%20is%20now%20available.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tails-7_6/&text=Tails%207.6%20is%20now%20available.)
[Bluesky](https://bsky.app/intent/compose?text=Tails%207.6%20is%20now%20available.%0Ahttps%3A//blog.torproject.org/new-release-tails-7_6/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproject.org/c/news/11)!

## Recent Updates

## [New Release: Tails 7.6](/new-release-tails-7_6/)

by [tails](/author/tails)
| March 26, 2026

Tails 7.6 is now available.

## [New Release: Tor Browser 15.0.8](/new-release-tor-browser-1508/)

by [ma1](/author/ma1)
| March 24, 2026

Tor Browser 15.0.8 is now available from the Tor Browser download page and also from our distribution directory.

## [Setting Up a Tor Relay at National Taiwan Normal University: A Practical Experience of Communicating with the University and Leaving Open Possibilities](/setting-up-tor-university-relay-taiwan/)

by [toomore](/author/toomore)
| March 23, 2026

A computer science student at National Taiwan Normal University successfully set up a Tor Relay on campus by working within institutional processesâcommunicating with administrators, completing paperwork, and explaining the difference between relays and exit nodes. This guest post from anoni.net shares practical advice for deploying Tor relays on university networks.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://www.torproject.org/download/)

### Subscribe to our Newsletter

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://newsletter.torproject.org/)

####

####

####

####

####

####

####

####

Trademark, copyright notices, and rules for use by third parties can be found in our [...