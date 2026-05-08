---
title: New Alpha Release: Tor Browser 16.0a6
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a6/
source: Tor Project blog
date: 2026-05-07
fetch_date: 2026-05-08T04:56:57.822896
---

# New Alpha Release: Tor Browser 16.0a6

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a6

by [ma1](/author/ma1)
| May 7, 2026

![](/new-alpha-release-tor-browser-160a6/lead.png)

Tor Browser 16.0a6 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a6/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a5 is:

* All Platforms
  + Updated tor to 0.4.9.7
  + Updated NoScript to 13.6.18.90101984
  + Updated OpenSSL to 3.5.6
  + [Bug tor-browser#43857](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43857): Review in-source TODOs
  + [Bug tor-browser#44402](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44402): Re-enable ESLint rule mozilla/no-browser-refs-in-toolkit as an error
  + [Bug tor-browser#44749](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44749): Check search engines parameter replacements
  + [Bug tor-browser#44792](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44792): Rebase alpha onto 150.0a1
  + [Bug tor-browser#44796](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44796): Adjust TorProviderBuilder to report the provider state to consumers
  + [Bug tor-browser#44828](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44828): Remove browser module references from toolkit/modules/ActorManagerParent.sys.mjs
  + [Bug tor-browser#44841](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44841): TorDomainIsolator proxy filter returns null on exception instead of preserving SOCKS proxy
  + [Bug tor-browser#44865](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44865): Block chrome://*/locale/* to content
  + [Bug tor-browser#44868](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44868): Backport 138c33ea964b2e0a4875aadc39d8a948e0c2aace to 150 to fix Windows builds
  + [Bug tor-browser#44870](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44870): Remove legacy branch from gitlab templates
  + [Bug tor-browser#44895](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44895): Undo the patch for #44772
  + [Bug tor-browser-build#41775](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41775): Update list of Snowflake STUN servers in default bridge line, 2026 edition
  + [Bug tor-browser-build#41778](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41778): Remove base-browser from protected-branches.py
  + [Bug tor-browser-build#41780](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41780): Create sha256sums-unsigned-build.txt in artifacts/$platform directories
* Windows + macOS + Linux
  + Updated Firefox to 150.0a1
  + [Bug tor-browser#43824](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43824): Switch resource:// modules to use moz-src:
  + [Bug tor-browser#44288](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44288): New identity fails to block loading a custom home page
  + [Bug tor-browser#44458](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44458): Fix the "Connect" and ".onion available" button height
  + [Bug tor-browser#44560](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44560): Customize the flags for alternate 'Application Data' directories
  + [Bug tor-browser#44630](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44630): Use settings config to hide settings, rather than data-hidden-from-search or commenting out
  + [Bug tor-browser#44648](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44648): Unexpected changes to SearchService.sys.mjs
  + [Bug tor-browser#44685](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44685): Use border radius for letterboxing
  + [Bug tor-browser#44798](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44798): Don't load `about:torconnect` into iframes
  + [Bug tor-browser#44829](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44829): Hide the settings privacy card
  + [Bug tor-browser#44832](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44832): Hide the Firefox mascot in about:neterror
  + [Bug tor-browser#44846](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44846): about:torconnect redirect doesn't work with the new neterror page
  + [Bug tor-browser#44847](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44847): Drop letterboxing sidebar rounded corner logic
  + [Bug tor-browser#44902](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44902): Error in privacy preference initialisation due to missing `dataCollectionViewProfilesMultiProfileBackupWarning`
  + [Bug tor-browser-build#31860](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/31860): Start using LTO for firefox project
* Windows
  + [Bug tor-browser#44862](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44862): Fontvis is missing Segoe MDL2 Assets
  + [Bug tor-browser#44868](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44868): Backport 138c33ea964b2e0a4875aadc39d8a948e0c2aace to 150 to fix Windows builds
* macOS
  + [Bug tor-browser#44850](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44850): Wrong path for bootstrapped tor daemon on macOS
  + [Bug tor-browser-build#41476](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41476): Since 13.5-legacy is not longer supported, remove tools/signing/wrappers/sign-rcodesign
* Linux
  + [Bug tor-browser#44361](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44361): Notify Linux i686 users that they won't receive updates anymore
  + [Bug tor-browser#44521](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44521): Disable widget.wayland.fractional-scale.enabled
* Android
  + Updated GeckoView to 150.0a1
  + [Bug tor-browser#44615](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44615): Remove ability to "Rate/Review in Google Play" in app
  + [Bug tor-browser#44827](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44827): Always enable noscript for android
  + [Bug tor-browser#44842](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44842): Replace instances of SwitchPreference with S...