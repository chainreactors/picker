---
title: New Alpha Release: Tor Browser 16.0a13
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a13/
source: Tor Project blog
date: 2026-10-01
fetch_date: 2026-10-02T07:49:40.292659
---

# New Alpha Release: Tor Browser 16.0a13

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a13

by [morgan](/author/morgan)
| October 1, 2026

![](/new-alpha-release-tor-browser-160a13/lead.png)

Tor Browser 16.0a13 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a13/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a12 is:

* All Platforms
  + Updated NoScript to 13.6.34.90101984
  + Updated Tor to 0.4.9.13
  + Updated OpenSSL to 3.5.9
  + [Bug tor-browser#44815](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44815): Disable harmful addon URL blocking
  + [Bug tor-browser#45073](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45073): Review preference changes between Firefox 141 and 153
  + [Bug tor-browser#45080](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45080): Keep the Reporting API disabled.
  + [Bug tor-browser#45333](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45333): Disable the fast-path to skip proxy resolution
  + [Bug tor-browser#45359](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45359): Rebase alpha onto 153.4.0esr
  + [Bug tor-browser#45366](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45366): Backport Security Fixes from Firefox 157
  + [Bug tor-browser#45368](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45368): Account for onion aliases in NoScript site parsing
  + [Bug tor-browser#45371](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45371): Hook CharacterData/Range insertion sinks for content patches propagation
* Windows + macOS + Linux
  + Updated Firefox to 153.4.0esr
  + [Bug tor-browser#45218](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45218): Implement YEC 2026 Takeover for Desktop Stable
  + [Bug tor-browser#45343](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45343): Hide verifier and the related error for self-signed onion cert case
  + [Bug tor-browser#45346](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45346): Crash when clicking "Learn moreâ¦" in onion site error page
  + [Bug tor-browser#45360](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45360): Port our language preference customization to the new settings design
* Windows
  + [Bug tor-browser#45293](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45293): Set widget.windows.tablet\_detection\_override to -1
* Android
  + Updated GeckoView to 153.4.0esr
  + Bug 40627: [Android] "share" selected text only works once [tor-browser]
  + [Bug tor-browser#44913](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44913): Review Mozilla 2019009: Enable Download location Settings on Nightly
  + [Bug tor-browser#45363](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45363): Disable import bookmarks in Android until stable
* Build System
  + All Platforms
    - [Bug tor-browser#45334](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45334): Update marionette harness to accept multiple tags
    - [Bug tor-browser#45367](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45367): Backport Bugzilla 2075120: mach lint fails to create the lint virtualenv because rumdl 0.1.91 is no longer available on PyPI
    - [Bug tor-browser-build#41847](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41847): Sign all releases using new gpg subkey
  + Windows
    - [Bug tor-browser-build#41890](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41890): Update sign-exe wrapper to use new Windows signing cert
  + macOS
    - [Bug tor-browser-build#41883](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41883): Fix sha256sum definition in projects/hfsplus-tools/config

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a13/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a13/&text=Tor%20Browser%2016.0a13%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a13/&text=Tor%20Browser%2016.0a13%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2016.0a13%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-160a13/)

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

October 8, 2026

## [Avoiding the Internet Achilles' heel: locking the web open with Onion Services (Amsterdam)](/event/internet-archive-europe-2026/)

October 28, 2026 – October 30, 2026

## [Mozilla Festival 2026 (MozFest), Barcelona](/event/mozfest-2026/)

November 2, 2026

## [Ethereum Cypherpunk Congress Mumbai](/event/Ethereum-Cypherpunk-Congress-Mumbai/)

November 3, 2026 – November 6, 2026

## [Devcon 8 (Mumbai)](/event/devcon8/)

## Recent Updates

## [New Alpha Release: Tor Browser 16.0a13](/new-alpha-release-tor-browser-160a13/)

by [morgan](/author/morgan)
| October 1, 2026

Tor Browser 16.0a13 is now available from the Tor Browser download page and also from our distribution directory.

## [Arti 2.7.0 released](/arti_2_7_0_released/)

by [opara](/author/opara)
| October 1, 2026

Arti 2.7.0 is released and ready for download.

## [New Release: Tails 7.14](/new-...