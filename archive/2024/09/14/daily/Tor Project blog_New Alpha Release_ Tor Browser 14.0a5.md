---
title: New Alpha Release: Tor Browser 14.0a5
url: https://blog.torproject.org/new-alpha-release-tor-browser-140a5/
source: Tor Project blog
date: 2024-09-14
fetch_date: 2025-10-06T18:36:07.781005
---

# New Alpha Release: Tor Browser 14.0a5

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.0a5

by [morgan](/author/morgan)
| September 13, 2024

![](/new-alpha-release-tor-browser-140a5/lead.png)

Tor Browser 14.0a5 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0a5/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Bugzilla Triage and Review

We have 13 remaining upstream Bugzilla issues to review and potentially develop patches for.

This work can be tracked in [this Gitlab query](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=opened&search=Review%20Mozilla&label_name%5B%5D=14.0%20stable&first_page_size=100).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.0a4](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated NoScript to 11.4.37
  + [Bug tor-browser#42255](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42255): pdfjs.disabled used to be part of RFP until Bug 1838415; lock pref to false in stable
  + [Bug tor-browser#42746](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42746): Extend prefers-contrast rules to include forced-colors
  + [Bug tor-browser#43046](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43046): Review Mozilla 1866927: Adds ability to enable email tracker blocking protection in private mode
  + [Bug tor-browser#43054](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43054): check bounceTrackingProtection in PB mode does not persist to disk
* Windows + macOS + Linux
  + [Bug tor-browser#42647](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42647): "Switching to a new device" regressed on 128
  + [Bug tor-browser#42653](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42653): The Neterror page has a checkbox to report iframe origin errors to TPO
  + [Bug tor-browser#42777](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42777): Remove 'Website Privacy Preferences' and ensure sensible default prefs
  + [Bug tor-browser#43087](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43087): Onion pattern on about:torconnect needs a dark theme asset
  + [Bug tor-browser#43109](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43109): Remove mention of Firefox Relay from settings
  + [Bug tor-browser#43115](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43115): Height of search bar has collapsed on about:tor
  + [Bug tor-browser#43117](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43117): Hide 'Always underline links' option
  + [Bug tor-browser#43118](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43118): hide CFR
  + [Bug tor-browser#43131](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43131): Reduce layout jank when loading about:tor
* Linux
  + [Bug tor-browser#42702](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42702): Cannot access the clipboard for the crypto address check (wayland)
  + [Bug mullvad-browser#334](https://gitlab.torproject.org/tpo/applications/mullvad-browser/-/issues/334): When set as default browser on Linux in standard mode, links don't open correctly
* Android
  + [Bug tor-browser#42954](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42954): Remove product recommendation API integration (Review Mozilla 1857215)
  + [Bug tor-browser#43097](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43097): NoScript fails to install on Android
  + [Bug tor-browser#43108](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43108): Backport Android fullscreen notifications refactoring on ESR128
  + [Bug tor-browser#43128](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43128): Use DuckDuckGo HTML on the Safest security level for Android
* Build System
  + All Platforms
    - Updated Go to 1.23.1
  + macOS
    - [Bug tor-browser-build#41231](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41231): Use var/browser\_release\_date in tools/signing/gatekeeper-bundling.sh
  + Android
    - [Bug tor-browser-build#41106](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41106): Non matching builds after application-services not being rebuilt in a long time
    - [Bug tor-browser-build#41232](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41232): Re-implement single-arch builds after the monorepo migration
    - [Bug tor-browser-build#41234](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41234): More dependencies are needed when building Android as a release

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a5/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a5/&text=Tor%20Browser%2014.0a5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a5/&text=Tor%20Browser%2014.0a5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.0a5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-140a5/)

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

## [New Alpha Release: Tor Browser 15.0a3](/new-alpha-release-tor-browser-150a3/)

by [boklm](/author/boklm)
| September 22, 2025

Tor Browser 15.0a3 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.0](/new-release-tails-7_0/)

by [tails](/author/tails)
| September 18, 2025

We are very excited to present you Tails 7.0, the first version of Tails based
on Debian 13 (Trixie) and GNOME 48 (Bengaluru). Tails 7.0 brings new versions
of many applications included in Tails.

## [New Release: Tor Browser 14.5.7](/new-release-tor-browser-1457/)

by [ma1](/author/ma1)
| September 16, 2025

Tor Browser 14.5.7 is now available from the Tor Browser download page and also from our distribution directory.

### Download Tor Browser

Download Tor...