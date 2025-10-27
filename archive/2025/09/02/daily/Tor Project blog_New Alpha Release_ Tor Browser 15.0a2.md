---
title: New Alpha Release: Tor Browser 15.0a2
url: https://blog.torproject.org/new-alpha-release-tor-browser-150a2/
source: Tor Project blog
date: 2025-09-02
fetch_date: 2025-10-02T19:32:13.836858
---

# New Alpha Release: Tor Browser 15.0a2

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 15.0a2

by [ma1](/author/ma1)
| September 1, 2025

![](/new-alpha-release-tor-browser-150a2/lead.png)

Tor Browser 15.0a2 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/15.0a2/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

Thanks to **WhyNotHugo** for [fixing the "Contributing" link in our README file](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44061).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 15.0a1](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated NoScript to 13.0.9
  + Updated OpenSSL to 3.5.2
  + [Bug tor-browser#43727](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43727): Update moz-toggle customisation for ESR 140
  + [Bug tor-browser#43832](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43832): Drop eslint-env
  + [Bug tor-browser#43864](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43864): Remove features from the unified search button
  + [Bug tor-browser#44045](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44045): Drop AI and machine learning components
  + [Bug tor-browser#44048](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44048): Backport Bug 1979608
  + [Bug tor-browser#44069](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44069): Update `meek-azure` related strings to `meek`
  + [Bug tor-browser#44094](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44094): Rebase Tor Browser alpha onto 140.2.0esr
  + [Bug tor-browser#44100](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44100): Backport Security Fixes from Firefox 142
  + [Bug tor-browser#44140](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44140): Align PDF changes to 140esr
  + [Bug tor-browser-build#41442](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41442): Update our audit CSVs to use the new Audit template
* Windows + macOS + Linux
  + Updated Firefox to 140.2.0esr
  + [Bug tor-browser#43111](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43111): Delete our webextensions for search engines when Bug 1885953 is fixed upstream
  + [Bug tor-browser#43519](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43519): Replace tor-loading.png with SVG
  + [Bug tor-browser#43525](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43525): Check if our search engine customization still works after ESR 140 transition
  + [Bug tor-browser#43728](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43728): Update search engine icon sizes
  + [Bug tor-browser#43795](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43795): Restore the URL classifier XPCOM components.
  + [Bug tor-browser#43817](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43817): Write e2e test for verifying if the browser is connected to the Tor network
  + [Bug tor-browser#43844](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43844): Security level shield icon should be flipped for RTL locales
  + [Bug tor-browser#43874](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43874): Incorporate our unified extension button hiding logic into mozilla's changes for ESR 140
  + [Bug tor-browser#43901](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43901): Modify about:license for Tor Browser and drop about:rights
  + [Bug tor-browser#43902](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43902): Hide Sidebar buttons
  + [Bug tor-browser#43903](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43903): Report broken site is disabled rather than hidden
  + [Bug tor-browser#44030](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44030): Security Level selector does not get confirmation before restarting
  + [Bug tor-browser#44034](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44034): Update string used for checkbox on New Identity confirmation dialog
  + [Bug tor-browser#44040](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44040): Modify nsIPrompt and the commonDialog code to allow destructive buttons
  + [Bug tor-browser#44041](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44041): Letterboxing causes greyed out alert background to be mis-aligned
  + [Bug tor-browser#44090](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44090): Several of our XUL pages cause a crash because of missing CSP
  + [Bug tor-browser#44095](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44095): Rename connectionPane.xhtml and remove it from the jar
  + [Bug tor-browser#44106](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44106): Make sure background tasks are not used for shutdown cleanup
  + [Bug tor-browser#44115](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44115): Make remove all bridges dialog use a destructive red button
  + [Bug tor-browser#44125](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44125): Do not offer to save signatures by default in Private Browsing Mode
* Windows + Android
  + [Bug tor-browser#44062](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44062): Force touch enabled on Windows and Android
* Windows
  + [Bug tor-browser#44046](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44046): Replace BASE\_BROWSER\_UPDATE with BASE\_BROWSER\_VERSION in the font visibility list
* macOS
  + [Bug tor-browser#44127](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44127): Do not show macOS Privacy hint on network error pages
* Android
  + Updated GeckoView to 140.2.0esr
  + [Bug tor-browser#43179](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43179): Make persistent 'private tabs' notification distinct from Firefox's
  + Bug 43346: Remove the "[android] Stop PrivateNotificationService" patch [tor-browser]
  + [Bug tor-browser#43645](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43645): Swiping away doesn't always disconnect from tor
  + [Bug tor-browser#43699](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43699): Dummy "about:" pages are not cleared from recently closed tabs (and possibly elsewhere) because they are normal tabs, not private tabs.
  + [Bug tor-browser#43826](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43826): Review Mozilla 1960122: Use `MOZ_BUILD_DATE` in Fenix build configuration
  + [Bug tor-browser#44021](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44021): Android settings page colors are sometimes messed up (seems to be on the first launch)
  + [Bug tor-browser#44042](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44042): Debug crash when opening settings too quickly after launching app
  + [Bug tor-browser#44047](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/...