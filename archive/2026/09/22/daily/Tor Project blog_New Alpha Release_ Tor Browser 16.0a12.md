---
title: New Alpha Release: Tor Browser 16.0a12
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a12/
source: Tor Project blog
date: 2026-09-22
fetch_date: 2026-09-23T06:55:26.261958
---

# New Alpha Release: Tor Browser 16.0a12

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a12

by [ma1](/author/ma1)
| September 22, 2026

![](/new-alpha-release-tor-browser-160a12/lead.png)

Tor Browser 16.0a12 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a12/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Windows Package Signature Issue

The DigiCert EV code-signing certificate we use to sign Windows installation packages is expired since September 1st and we are currently in the process to renew it. Unfortunately, this process is delayed and not yet complete.

Therefore, trying to install Tor Browser 16.0a12 or 16.0a11 from scratch will cause a "bad signature" warning on Windows.

Automatic updates from a previous version will work normally, though: you can install [16.0a10](https://archive.torproject.org/tor-package-archive/torbrowser/16.0a10/tor-browser-windows-x86_64-portable-16.0a10.exe) and let it update to the lastest version.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a11 is:

* All Platforms
  + Updated Tor to 0.4.9.12
  + Updated NoScript to 13.6.33.90101984
  + [Bug tor-browser#45304](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45304): Rebase Tor Browser alpha onto 153.3.0esr
  + [Bug tor-browser#45336](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45336): Pass --disable-proxy-direct-failover in our mozconfigs
  + [Bug tor-browser#45299](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45299): Backport Security Fixes from Firefox 156
  + [Bug tor-browser-build#41846](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41846): Sign alpha releases using new gpg subkey
  + [Bug tor-browser-build#41875](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41875): Update relprep.py for the new versions.ini URL
* Windows + macOS + Linux
  + Updated Firefox to 153.3.0esr
  + [Bug tor-browser#42065](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42065): Security exception warning and button for Onion Services with self-signed certificates
  + [Bug tor-browser#45133](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45133): Disable `browser.toolbars.share-button.enabled`
  + [Bug tor-browser#45177](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45177): Remove websiteSpoofEnglishControl
  + [Bug tor-browser#45249](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45249): Remove the duplicate "Verified by" from the old site identity panel
  + [Bug tor-browser#45255](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45255): Add YEC 2026 Strings (Desktop)
  + [Bug tor-browser#45262](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45262): Disable reset PBM burn button and related UI migration
  + [Bug tor-browser#45277](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45277): Change setting icon for About Tor Browser
  + [Bug tor-browser#45278](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45278): Explicitly disable WebXR
* Linux
  + [Bug tor-browser#44887](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44887): Drop Linux 32-bit deprecation notice
* Android
  + Updated GeckoView to 153.3.0esr
  + [Bug tor-browser#44548](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44548): Remove "Passwords" UI from Android
  + [Bug tor-browser#44936](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44936): Search widget icon is too small on android alpha
  + [Bug tor-browser#45100](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45100): Regression in #43229 "Buttons that open links can be accessed before torbrowser is bootstrapped, leaving the app in a bad state"
  + [Bug tor-browser#45172](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45172): Move our "Connect to Tor before opening links" code from the deprecated openToBrowserAndLoad to the recommended loadUrlOrSearch
  + [Bug tor-browser#45217](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45217): Implement YEC 2026 Takeover for Android Stable
  + [Bug tor-browser#45225](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45225): Remove "Share" and "Translate" options from "Settings" -> "Customize" -> "Toolbar shortcut"
  + [Bug tor-browser#45250](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45250): Remove "Privacy report" in tabs settings in Android
  + [Bug tor-browser#45251](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45251): Turn off and hide the remote improvements UI
  + [Bug tor-browser#45252](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45252): Remove the change wallpaper menu item
  + [Bug tor-browser#45256](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45256): Add YEC 2026 Strings (Android)
  + [Bug tor-browser#45261](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45261): Add linter check: only `MAIN+LAUNCHER` components may be exported="true"
  + [Bug tor-browser#45269](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45269): Completely disable search suggestion feature
  + [Bug tor-browser#45275](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45275): Drop clearOnShutdown on Android-specific profile
  + [Bug tor-browser#45280](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45280): about:config broken on Android
  + [Bug tor-browser#45281](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/45281): Fix or remove broken "Use screen lock to hide Tor Browser tabs" feature
* Build System
  + All Platforms
    - [Bug tor-browser-build#41867](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41867): Update tails-dev email address in release prep templates
    - [Bug tor-browser-build#41871](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41871): Update downloads repository references in relprep templates
  + Windows
    - [Bug tor-browser-build#41877](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41877): `make list_toolchain_updates` is not checking windows-app-sdk
    - [Bug tor-browser-build#41878](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41878): Update the Windows app SDK and add some additional DLLs
  + Android
    - [Bug tor-browser-build#41876](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41876): Add missing firefox\_platform\_version.txt file in android a...