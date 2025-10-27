---
title: New Alpha Release: Tor Browser 12.5a4 (Android, Windows, macOS, Linux)
url: https://blog.torproject.org/new-alpha-release-tor-browser-125a4/
source: Tor Project blog
date: 2023-03-23
fetch_date: 2025-10-04T10:25:39.353820
---

# New Alpha Release: Tor Browser 12.5a4 (Android, Windows, macOS, Linux)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 12.5a4 (Android, Windows, macOS, Linux)

by [richard](/author/richard)
| March 22, 2023

![](/new-alpha-release-tor-browser-125a4/lead.png)

Tor Browser 12.5a4 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/12.5a4/).

This release updates Firefox 102.9.0esr, including bug fixes, stability improvements and important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-10/). We also backported the Android-specific [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-09/) from Firefox 111.

We use this opportunity to update various other components of Tor Browser as well:

* NoScript 11.4.20

Tor Browser 12.5a4 also adds support the Finnish language on all platforms. We would like to thank volunteer olavinto for making this possible!

## Full changelog

The full changelog since [Tor Browser 12.5a3](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Updated Translations
  + Updated NoScript to 11.4.20
  + [Bug tor-browser-build#40353](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40353): Re-enable rlbox
  + [Bug tor-browser-build#40810](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40810): Enable Finnish (fi) in alpha builds
  + [Bug tor-browser-build#40817](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40817): Add basebrowser-incrementals-nightly makefile target
  + [Bug tor-browser#41599](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41599): about:networking#networkid should be normalized
  + [Bug tor-browser#41635](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41635): Disable the Normandy component at compile time
  + [Bug tor-browser#41636](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41636): Disable back webextension.storage.sync after ensuring NoScript settings won't be lost
  + [Bug tor-browser#41646](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41646): Regression in 12.5a3: the system font patch should also set a font-size
  + [Bug tor-browser#41647](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41647): Turn --enable-base-browser in --with-base-browser-version
  + [Bug tor-browser#41659](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41659): Add canonical color definitions to base-browser
  + [Bug tor-browser#41662](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41662): Disable about:sync-logs
  + [Bug tor-browser#41670](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41670): Rebase Tor Browser Alpha to 102.9.0esr
  + [Bug tor-browser#41671](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41671): Turn media.peerconnection.ice.relay\_only to true as defense in depth against WebRTC ICE leaks
* Windows + macOS + Linux
  + Updated Firefox to 102.9esr
  + [Bug tor-browser#40144](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40144): about:privatebrowsing Firefox branding
  + [Bug tor-browser-build#40788](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40788): Remove all languages but en-US for privacy-browser build target
  + [Bug tor-browser-build#40808](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40808): Set update URL for nightly base-browser
  + [Bug tor-browser#41085](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41085): Refactor the UI to remove all bridges
  + [Bug tor-browser#41093](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41093): Users don't understand the purpose of bridge-moji
  + [Bug tor-browser#41574](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41574): Use --warning-color variable for the "Custom" label in the security level popup.
  + [Bug tor-browser#41657](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41657): Remove --enable-tor-browser-data-outside-app-dir
* Windows
  + [Bug tor-browser-build#40793](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40793): Add some metadata also to the Windows installer
  + [Bug tor-browser-build#40801](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40801): Correct the ExecShell for system-wide installs in the NSIS script
* Android
  + Updated GeckoView to 102.9esr
  + [Bug tor-browser-build#40800](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40800): WebTunnel Integration in Tor Browser mobile
  + [Bug tor-browser#41667](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41667): Enable media.peerconnection.ice.obfuscate\_host\_addresses on Android for defense-in-depth
  + [Bug tor-browser#41677](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41677): Remove the --disable-tor-browser-update flag on Android
* Build System
  + All Platforms
    - Updated Go to 1.19.7
    - [Bug tor-browser-build#40750](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40750): Find why rlbox hurts reproducibility
    - [Bug tor-browser-build#40763](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40763): Add support for signing multiple browsers in tools/signing/nightly
    - [Bug tor-browser-build#40794](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40794): Include the build-id in firefox-l10n output name
    - [Bug tor-browser-build#40795](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40795): Trim down tor-browser-build release prep issue templates
    - [Bug tor-browser-build#40796](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40796): Bad UX for the changelogs script when using the issue number
    - [Bug tor-browser-build#40805](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40805): Define the version flag for all browsers
    - [Bug tor-browser-build#40807](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40807): Add config for signing base-browser nightly in tools/signing/nightly
    - [Bug tor-browser-build#40812](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40812): Make var/rezip in projects/firefox/config quiet
    - [Bug tor-browser#41649](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41649): Create rebase and security backport gitlab issue templates
    - [Bug tor-browser#41682](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41682): Add base-browser nightly mar signing key
  + Windows + macOS + Linux
    - [Bug tor-browser-build#40809](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40809): Remove --enable-tor-browser-update and --enable-verify-mar from projects/firefox/mozconfig
    - [Bug tor-browser-build#40813](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40813): Enable var/updater\_enabled for basebrowser nightly
  + macOS
    - [Bug tor-browser-build#40790](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40790): Fix dmg2mar after dmg changes from #28124
    - [Bug tor-browser-build#40791](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40791): tools/dmg2mar should exit with an error when there is an ...