---
title: New Alpha Release: Tor Browser 16.0a7
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a7/
source: Tor Project blog
date: 2026-06-03
fetch_date: 2026-06-04T06:32:19.067590
---

# New Alpha Release: Tor Browser 16.0a7

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a7

by [ma1](/author/ma1)
| June 3, 2026

![](/new-alpha-release-tor-browser-160a7/lead.png)

Tor Browser 16.0a7 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a7/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a6 is:

* All Platforms
  + Updated NoScript to 13.6.19.90401984
  + Updated Tor to 0.4.9.9
  + [Bug tor-browser#42436](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42436): Allow for multiple configured (front, reflector) domain fronting pairs in Moat module
  + [Bug tor-browser#44869](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44869): Rebase alpha onto 151
  + [Bug tor-browser#44952](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44952): TOR\_PROVIDER=none throws an error at launch
  + [Bug tor-browser#44989](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44989): Backport Bug 2040704: Fix date format leak in Firefox 151
  + [Bug tor-browser#44990](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44990): CI failing due to dubious ownership of cached repo
  + [Bug tor-browser#44999](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44999): Privacy settings are broken in 151
  + [Bug tor-browser-build#41686](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41686): Copy more build artifacts to the artifacts directory
* Windows + macOS + Linux
  + Updated Firefox to 151.0a1
  + [Bug tor-browser#44903](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44903): Use the `support-page` instead of `tor-manual-page` in `moz-support-link`
  + [Bug tor-browser#44904](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44904): Use settings config for onion site settings
  + [Bug tor-browser#44991](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44991): Improve the no-authentication handling on the control port
  + [Bug tor-browser#44997](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44997): Captcha doesn't work in TB desktop
  + [Bug tor-browser#45005](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45005): Rename arrowpanel CSS variable
* Windows
  + [Bug tor-browser#44745](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44745): Change how we hide SSO setting for windows
* Android
  + Updated GeckoView to 151.0a1
  + [Bug tor-browser#43543](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43543): Make the dev icon distinct from the nightly one
  + [Bug tor-browser#44211](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44211): Disable "Shake it up. Skip the scroll."
  + [Bug tor-browser#44323](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44323): Audit Android Settings changes from 128 to 140
  + [Bug tor-browser#44917](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44917): Disable Ads client for all channels
  + [Bug tor-browser#45031](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45031): Disable AI features for Android
* Build System
  + All Platforms
    - [Bug tor-browser-build#41779](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41779): Update toolchains for Firefox 151
    - [Bug tor-browser-build#41781](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41781): Fix clean section in rbm.local.conf.example
    - [Bug tor-browser-build#41792](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41792): Switch from ftp.gnu.org to ftpmirror.gnu.org
    - [Bug tor-browser-build#41798](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41798): Update the URL to versions.ini in relprep.py
    - [Bug tor-browser-build#41806](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41806): `make list_toolchain_updates` should check var/firefox\_platform\_version
    - [Bug tor-browser-build#41807](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41807): Incorrectly generated Bugzilla query link in generate-bugzilla-triage-csv.py
  + Windows + Linux + Android
    - Updated Go to 1.26.3
  + macOS
    - [Bug tor-browser-build#41793](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41793): Stop copying permissions from .mar in dmg2mar
  + Android
    - [Bug tor-browser-build#41801](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41801): Hardlink artifacts in fix\_gradle\_deps.py

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a7/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a7/&text=Tor%20Browser%2016.0a7%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a7/&text=Tor%20Browser%2016.0a7%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2016.0a7%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-160a7/)

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

June 14, 2026 – June 14, 2025

## [W3PN Neo-Cypherpunk Summit](/event/W3PN-Summit-2026/)

June 23, 2026 – June 24, 2025

...