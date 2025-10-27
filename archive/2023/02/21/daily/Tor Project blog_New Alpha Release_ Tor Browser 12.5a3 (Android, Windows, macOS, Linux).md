---
title: New Alpha Release: Tor Browser 12.5a3 (Android, Windows, macOS, Linux)
url: https://blog.torproject.org/new-alpha-release-tor-browser-125a3/
source: Tor Project blog
date: 2023-02-21
fetch_date: 2025-10-04T07:39:18.058519
---

# New Alpha Release: Tor Browser 12.5a3 (Android, Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 12.5a3 (Android, Windows, macOS, Linux)

by [richard](/author/richard)
| February 20, 2023

![](/new-alpha-release-tor-browser-125a3/lead.png)

Tor Browser 12.5a3 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/12.5a3/).

This release updates Firefox on Android, Windows, macOS, and Linux to 102.8.0esr. It includes important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-02/) to Firefox and GeckoView. There were no Android-specific security updates to backport from the Firefox 110 release.

We use this opportunity to update various other components of Tor Browser as well:

* NoScript 11.4.16
* OpenSSL 1.1.1t
* go 1.19.6

The full changelog since [Tor Browser 12.5a2](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Updated Translations
  + Updated OpenSSL to 1.1.1t
  + Updated NoScript to 11.4.16
  + [Bug tor-browser#40763](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40763): Stop using remote localized files in CFR
  + [Bug tor-browser#41351](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41351): Move the crypto protection patch earlier in the patchset
  + [Bug tor-browser#41361](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41361): Integrate the Conjure PT into alpha versions of Tor Browser
  + [Bug tor-browser#41424](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41424): Reduce disk activity by disabling some unnecessary tasks and telemetry
  + [Bug tor-browser#41565](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41565): Gate Telemetry Tasks behind AppConstants.MOZ\_TELEMETRY\_REPORTING
  + [Bug tor-browser#41568](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41568): Disable LaterRun
  + [Bug tor-browser#41598](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41598): Prevent NoScript from being removed / disabled until core functionality has been migrated to Tor Browser
  + [Bug tor-browser#41601](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41601): Apply Snowflake Remove HelloVerify Countermeasure
  + [Bug tor-browser#41603](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41603): Customize the creation of MOZ\_SOURCE\_URL
  + [Bug tor-browser#41624](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41624): Disable unused about: pages
  + [Bug tor-browser#41627](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41627): Enable network.http.referer.hideOnionSource in base-browser
  + [Bug tor-browser#41637](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41637): cherry-pick Mozilla 1814416: Generalize the app name in about:buildconfig. r=ahochheiden
* Windows + macOS + Linux
  + Updated Firefox to 102.8esr
  + [Bug tor-browser#20497](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/20497): Improve support for non-portable mode
  + [Bug tor-browser-build#40745](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40745): Allow customizing MOZ\_APP\_BASENAME
  + [Bug tor-browser-build#40773](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40773): Copy some documentation files only on Tor Browser
  + [Bug tor-browser-build#40781](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40781): Move translations to new paths
  + [Bug tor-browser#41080](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41080): Some users are choosing an adjacent country for circumvention settings
  + [Bug tor-browser#41084](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41084): Reserve red as a button color for dangerous actions
  + [Bug tor-browser#41540](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41540): Confusing build-id date in about:preferences in alphas
  + [Bug tor-browser#41542](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41542): Disable the creation of a default profile
  + [Bug tor-browser#41561](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41561): Maximize warning is broken (regression)
  + [Bug tor-browser#41577](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41577): Disable profile migration
  + [Bug tor-browser#41587](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41587): Disable the updater for Base Browser
  + [Bug tor-browser#41588](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41588): Use better words for the Tor Network description in the onboarding
  + [Bug tor-browser#41595](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41595): Disable pagethumbnails capturing
  + [Bug tor-browser#41606](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41606): Move the changes to the hamburger menu out of the Torbutton commit
  + [Bug tor-browser#41609](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41609): Move the disabling of Firefox Home (Activity Stream) to base-browser
  + [Bug tor-browser#41613](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41613): Skip Drang & Drop filtering for DNS-safe URLs (no hostname, e.g. RFC3966 tel:)
  + [Bug tor-browser#41626](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41626): Bridge-emojii tooltips not localized in ES locale
  + [Bug tor-browser#41633](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41633): Updating from 12.0.2 to 12.0.3 resets NoScript settings
* Windows
  + [Bug tor-browser#40717](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40717): UX: hide SSO
  + [Bug tor-browser-build#40772](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40772): Check and fix HiDPI issues in the NSIS installer
* Android
  + Updated GeckoView to 102.8esr
  + [Bug tor-browser#40283](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40283): Can't upload files with Tor browser on Android
  + [Bug tor-browser#40536](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40536): Proxy Refused if link from other app opens Android TBB
  + [Bug tor-browser#41185](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41185): Hide learn more about sync
  + [Bug tor-browser#41616](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41616): Backport Android-specific security fixes from Firefox 110 to ESR 102.8-based Tor Browser
  + [Bug tor-browser#41634](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41634): Google Play incorrectly detects that libTor.so is built with OpenSSL 1.1.1b
* Build System
  + All Platforms
    - Updated Go to 1.19.6
    - [Bug tor-browser-build#40723](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40723): Update upload-update\_responses-to-staticiforme step for new tor-browser-update-responses repository
    - [Bug tor-browser-build#40747](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40747): Remove empty line at the top of sha256sums-unsigned-build.txt
    - [Bug tor-browser-build#40748](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40748): When sha256sums-unsigned-build.txt contains an empty line, tools/dmg2mar prints a w...