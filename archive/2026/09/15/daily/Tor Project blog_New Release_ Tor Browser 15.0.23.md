---
title: New Release: Tor Browser 15.0.23
url: https://blog.torproject.org/new-release-tor-browser-15023/
source: Tor Project blog
date: 2026-09-15
fetch_date: 2026-09-16T07:06:13.921930
---

# New Release: Tor Browser 15.0.23

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 15.0.23

by [ma1](/author/ma1)
| September 15, 2026

![](/new-release-tor-browser-15023/lead.png)

Tor Browser 15.0.23 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/15.0.23/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Windows Package Signature Issue

The DigiCert EV code-signing certificate we use to sign Windows installation packages is expired since September 1st and we are currently in the process to renew it. Unfortunately, this process is delayed and not yet complete.

This has caused Windows users trying to install Tor Browser 15.0.21 and 15.0.22 from scratch to receive "bad signature" warnings.

As a temporary work-around, for Windows only we're keeping Tor Browser *15.0.20* (the latest correctly signed version) listed on our [download page](https://www.torproject.org/download/), relying on automatic updates (which are signed with a different key, not involving this expired certificate) to bring Windows users to the current version.

Users who prefer to download the latest version directly, ignoring the certificate expiration warning, can download it from <https://dist.torproject.org/torbrowser/15.0.23/>.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-15.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 15.0.22 is:

* All Platforms
  + Updated NoScript to 13.6.33.1984
  + [Bug tor-browser#45296](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45296): (H1) SharedWorker Identity Mismatch allows WebAssembly execution at Safer
  + [Bug tor-browser#45297](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45297): (H1) Missing setHTMLUnsafe hook leaves a permanent WebAssembly-capable child realm at Safer
  + [Bug tor-browser#45299](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45299): Backport Security Fixes from Firefox 156
  + [Bug tor-browser#45303](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45303): Rebase Tor Browser stable onto 140.16.0esr
  + [Bug tor-browser-build#41875](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41875): Update relprep.py for the new versions.ini URL
* Windows + macOS + Linux
  + Updated Firefox to 140.16.0esr
* Linux
  + [Bug tor-browser#44996](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44996): Change the 32-bit linux message to the expired version for the final 15.0 release
* Android
  + Updated GeckoView to 140.16.0esr
* Build System
  + All Platforms
    - [Bug tor-browser-build#41871](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41871): Update downloads repository references in relprep templates

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-15023/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-15023/&text=Tor%20Browser%2015.0.23%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-15023/&text=Tor%20Browser%2015.0.23%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2015.0.23%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-15023/)

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

## [New Release: Tor Browser 15.0.23](/new-release-tor-browser-15023/)

by [ma1](/author/ma1)
| September 15, 2026

Tor Browser 15.0.23 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tor Browser 15.0.22](/new-release-tor-browser-15022/)

by [ma1](/author/ma1)
| September 9, 2026

Tor Browser 15.0.22 is now available from the Tor Browser download page and also from our distribution directory.

## [Tor VPN Beta: What we've learned building our own VPN for Android from scratch](/tor-vpn-beta/)

by [pavel](/author/pavel)
| September 9, 2026

Last fall, we soft-launched Tor VPN Beta as a way to extend Tor's privacy protections beyond the browser to an entire Android device. Since then, we've been able to learn from how people are actually using it in real-world scenarios. This post walks through what makes our per-app circuit isolation different from commercial VPNs, the surprising UX lesson when trying to bypass blocks, and the mobile foundation we're building for what's next.

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