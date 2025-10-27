---
title: New Alpha Release: Tor Browser 13.5a8
url: https://blog.torproject.org/new-alpha-release-tor-browser-135a8/
source: Tor Project blog
date: 2024-05-18
fetch_date: 2025-10-06T16:52:18.345794
---

# New Alpha Release: Tor Browser 13.5a8

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 13.5a8

by [richard](/author/richard)
| May 17, 2024

![](/new-alpha-release-tor-browser-135a8/lead.png)

Tor Browser 13.5a8 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/13.5a8/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

We would like to thank the folowing community members for their contributions this release:

* NoisyCoil for their work on [tor-browser-build#41137](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41137)

If you would like to contribute, our contributor guide can be found [here](https://gitlab.torproject.org/tpo/applications/team/-/wikis/Development-Information/Tor-Browser/Contributing-to-Tor-Browser).

## End of Life for Windows versions â¤ 8.1 and macOS versions â¤ 10.14

Users running Tor Browser on older versions of Windows and macOS will start seeing messages warning them their operating systems will no longer be supported. This is an upstream change we are inheriting from Mozilla. Starting with version 116 Firefox Windows users will require Windows 10 or later while macOS users will require macOS 10.15 or later to continue receiving Tor Browser updates. Users have until October 1st, 2024 to upgrade!

## Continued Improvements on Android!

This release has removed the legacy bootstrapping functionality from Tor Browser for Android entirely. This legacy functionality depended on the `tor-android-service` and `tor-onion-proxy-library` components. With this functionality gone and replaced with the unified Tor backend living in GeckoView, we will be able to drop these components in the next release, which *should* result in slightly smaller .apk sizes.

We have made a few UI changes and improvements with this release. The UI which allowed users to fallback to the legacy bootstrapping process has been removed (since the backend is also gone).

Additionally various Android-specific privacy and security bugs have been fixed.

## Various User Experience Improvements

On desktop, we have been working on various UI improvements and polish. The `about:torconnect` (aka Connect Assist) page has been restyled to better fit with Firefox's existing UI. We have also fixed various minor bugs related to letterboxing, the onion-service client-authentication dialgo, and the circuit display.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 13.5a7](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + [Bug tor-browser#42290](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42290): "DuckDuckGoOnion" is a weird naming format for onion search engines
  + [Bug tor-browser#42549](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42549): Remove brand.dtd
  + [Bug tor-browser#42560](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42560): Rebase Tor Browser alpha onto 115.11.0esr
  + [Bug tor-browser#42565](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42565): Backport Android and desktop security fixes from Firefox 126
  + [Bug tor-browser#42583](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42583): Modify moz-support-link
  + [Bug tor-browser-build#41137](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41137): Build gcc-cross and tor-expert-bundle for linux-aarch64
  + [Bug mullvad-browser#241](https://gitlab.torproject.org/tpo/applications/mullvad-browser/-/issues/241): Move network.proxy.failover\_direct=false pref to base-browser
* Windows + macOS + Linux
  + Updated Firefox to 115.11.0esr
  + [Bug tor-browser#41621](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41621): Tweak about:torconnect styling
  + [Bug tor-browser#41930](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41930): intl.accept\_languages gets into a stuck modifed state
  + [Bug tor-browser#42391](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42391): IndexDB's private directory not removed on browser shutdown in global private browsing mode
  + [Bug tor-browser#42405](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42405): Fix betterboxing + findbar horizontal bounce if the scrollbar is not an overlay
  + [Bug tor-browser#42541](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42541): Circuit Display does not work when using Conjure pluggable transport
  + [Bug tor-browser#42542](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42542): Quirks when onion authentication prompt is shared between two tabs
  + [Bug tor-browser#42557](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42557): Fix regression in Onion Services authentication prompt focus
  + [Bug tor-browser#42573](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42573): Tweak language notification to avoid formatValue
  + [Bug tor-browser#42574](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42574): Exempt pdf.js from letterboxing
* Windows + macOS
  + [Bug tor-browser#41405](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41405): Win â¤8.1 and macOS â¤10.14 not supported in ESR 128
  + [Bug tor-browser#42347](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42347): Add a banner warning users about the upcoming EOL for Win â¤8.1 and macOS â¤10.14
* Linux
  + [Bug tor-browser-build#41136](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41136): Include \*.deb in the list of files to gpg sign
* Android
  + Updated GeckoView to 115.11.0esr
  + [Bug tor-browser#42317](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42317): Update "Security Settings" menu item
  + [Bug tor-browser#42409](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42409): TTP-03-011 WP3: Potential DoS due to Deep Link abuse
  + [Bug tor-browser#42552](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42552): TBA: formatting APIs are en-US only
  + [Bug tor-browser#42562](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42562): Restrict the accepted languages to the ones whose localization is available
  + [Bug tor-browser#42566](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42566): Remove 'Enable beta connection features' menu item in stable release channel
  + [Bug tor-browser#42567](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42567): Remove 'Enable beta connection features' toggle
  + [Bug tor-browser#42571](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42571): The new bootstrap on Android breaks if the browser goes in background
  + [Bug tor-browser#42576](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42576): Backport Bug 1885171: use the private keyboard for prompts on Android
  + [Bug tor-browser#42578](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42578): Reject Android "open in Tor Browser" intent
  + [Bug tor-browser#42582](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42582): Accepted languages should use id and he on Android
  + [Bug tor-browser-...