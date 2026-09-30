---
title: New Release: Tor Browser 15.0.24
url: https://blog.torproject.org/new-release-tor-browser-15024/
source: Tor Project blog
date: 2026-09-29
fetch_date: 2026-09-30T07:43:02.915626
---

# New Release: Tor Browser 15.0.24

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 15.0.24

by [morgan](/author/morgan)
| September 29, 2026

![](/new-release-tor-browser-15024/lead.png)

Tor Browser 15.0.24 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/15.0.24/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Windows Package Signature Issue

The DigiCert EV code-signing certificate we use to sign Windows installation packages is expired since September 1st and we are currently in the process to renew it. Unfortunately, this process is delayed and not yet complete.

This has caused Windows users trying to install Tor Browser 15.0.21 and 15.0.22 from scratch to receive "bad signature" warnings.

As a temporary work-around, for Windows only we're keeping Tor Browser *15.0.20* (the latest correctly signed version) listed on our [download page](https://www.torproject.org/download/), relying on automatic updates (which are signed with a different key, not involving this expired certificate) to bring Windows users to the current version.

Users who prefer to download the latest version directly, ignoring the certificate expiration warning, can download it from <https://dist.torproject.org/torbrowser/15.0.24/>.

## New PGP subkey

This release is signed using a new subkey. If you previously used gpg to verify Tor Browser downloads, you may need to refresh the Tor Browser signing key (0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290) in your local keyring. For more details you can read [our page about signature verification](https://support.torproject.org/tor-browser/getting-started/verifying-tor-browser/), specifically the section "Refreshing the PGP key".

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-15.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 15.0.23 is:

* All Platforms
  + Updated NoScript to 13.6.35.1984
  + Updated Tor to 0.4.9.13
  + [Bug tor-browser#45358](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45358): Rebase Tor Browser stable onto 140.17.0esr
  + [Bug tor-browser#45366](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45366): Backport Security Fixes from Firefox 157
  + [Bug tor-browser#45368](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45368): Account for onion aliases in NoScript site parsing
  + [Bug tor-browser#45371](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45371): Hook CharacterData/Range insertion sinks for content patches propagation
* Windows + macOS + Linux
  + Updated Firefox to 140.17.0esr
  + [Bug tor-browser#45218](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45218): Implement YEC 2026 Takeover for Desktop Stable
* Linux
  + [Bug tor-browser#44996](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44996): Change the 32-bit linux message to the expired version for the final 15.0 release
* Android
  + Updated GeckoView to 140.17.0esr
  + [Bug tor-browser#45217](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45217): Implement YEC 2026 Takeover for Android Stable
* Build System
  + All Platforms
    - [Bug tor-browser-build#41847](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41847): Sign all releases using new gpg subkey
  + macOS
    - [Bug tor-browser-build#41883](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41883): Fix sha256sum definition in projects/hfsplus-tools/config

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-15024/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-15024/&text=Tor%20Browser%2015.0.24%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-15024/&text=Tor%20Browser%2015.0.24%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2015.0.24%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-15024/)

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

## Upcoming Events

October 28, 2026 – October 30, 2026

## [Mozilla Festival 2026 (MozFest), Barcelona](/event/mozfest-2026/)

November 2, 2026

## [Ethereum Cypherpunk Congress Mumbai](/event/Ethereum-Cypherpunk-Congress-Mumbai/)

November 3, 2026 – November 6, 2026

## [Devcon 8 (Mumbai)](/event/devcon8/)

## Recent Updates

## [New Release: Tor Browser 15.0.24](/new-release-tor-browser-15024/)

by [morgan](/author/morgan)
| September 29, 2026

Tor Browser 15.0.24 is now available from the Tor Browser download page and also from our distribution directory.

## [New Alpha Release: Tor Browser 16.0a12](/new-alpha-release-tor-browser-160a12/)

by [ma1](/author/ma1)
| September 22, 2026

Tor Browser 16.0a12 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.13](/new-release-tails-7_13/)

by [tails](/author/tails)
| September 16, 2026

Tails 7.13 is now available.

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

Trademark, copyright notices, and rules for use by third parties can be found in our [FAQ](https://www.torproject.org/about/trademark/).