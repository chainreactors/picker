---
title: New Release: Tor Browser 12.0
url: https://blog.torproject.org/new-release-tor-browser-120/
source: Tor Project blog
date: 2022-12-08
fetch_date: 2025-10-04T00:56:34.368579
---

# New Release: Tor Browser 12.0

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 12.0

by [duncan](/author/duncan)
| December 7, 2022

![](/new-release-tor-browser-120/lead.png)

Tor Browser 12.0 is now available from the Tor Browser [download page](https://www.torproject.org/download/) and also from our [distribution directory](https://dist.torproject.org/torbrowser/12.0/). This new release updates Tor Browser to Firefox Extended Support Release 102.

## What's new?

### Upgraded to Extended Support Release 102

![Image reading "Firefox Extended Support Release 102"](/new-release-tor-browser-120/12-esr-102.png)

Once again, the time has come to upgrade Tor Browser to Firefox's newest Extended Support Release. We've spent the past few months since [Tor Browser 11.5's release](/new-release-tor-browser-115/) reviewing [ESR 102's release notes](https://www.mozilla.org/en-US/firefox/102.0esr/releasenotes/) to ensure each change is compatible with Tor Browser. As part of that process, anything that may conflict with Tor Browser's strict privacy and security principles has been carefully disabled.

### Multi-locale support for desktop

[

![Visualization of the menu used to select Tor Browser 12.0's display language](12-multi-locale.png)
](12-multi-locale.mp4)

Previously, if you wanted to use Tor Browser for desktop in a language other than English, you needed to find and download one of the matching language versions from our download page. Switching language after installing Tor Browser wasn't an easy task either, and would either require adding the new language pack to your existing installation, or redownloading Tor Browser from scratch.

As of today we're pleased to announce that this is a thing of the past: Tor Browser for desktop is now truly multi-locale, meaning all supported languages are now included in a single bundle. For new users, Tor Browser 12.0 will update itself automatically when launched to match your system language. And if you've upgraded from Tor Browser 11.5.8, the browser will attempt to maintain your previously chosen display language.

Either way, you can now switch display language without any additional downloads via the Language menu in General settings â but we'd still recommend giving Tor Browser a quick restart before the change can take complete effect.

Naturally, bundling multiple languages in a single download should increase Tor Browser's filesize â we are very conscious of this; however, we've found a way to make efficiency savings elsewhere, meaning the difference in filesize between Tor Browser 11.5 and 12.0 is minor.

### Native Apple Silicon support

![Apple Silicon logo](/new-release-tor-browser-120/12-native-apple-support.png)

This was no small task, but we're happy to say that Tor Browser 12.0 now supports Apple Silicon natively. Like Mozilla's approach for Firefox, we've opted for a Universal Binary too â meaning both x86-64 (i.e. Intel compatible) and ARM64 (i.e. Apple Silicon compatible) builds are bundled together with the correct version chosen automatically when run.

### HTTPS-Only by default for Android

![Image reading "HTTPS Only Mode" and a switch turned on](/new-release-tor-browser-120/12-https-only-android.png)

Back in July, we shared an update about Tor Browser for Android and our aspirations for its near future in the [Tor Browser 11.5 release post](/new-release-tor-browser-115/). Since the beginning of the year our developers have been working hard to recommence regular updates for Android, improve the app's stability, and catch up to Fenix's (Firefox for Android's) release cycle.

The next phase in our plan for Android is to begin porting selected, high-priority features that have recently been launched for desktop over to Android â starting with enabling HTTPS-Only Mode by default. This change will help provide the same level of protection against SSL stripping attacks by [malicious exit relays](/bad-exit-relays-may-june-2020/) that we introduced to desktop in Tor Browser 11.5.

### Prioritize .onion sites for Android

[

![Visualization of the option to prioritize onion sites in Tor Browser for Android's Privacy and Security settings screen](12-prioritize-onions-android.png)
](12-prioritize-onions-android.mp4)

Another small but mighty improvement to Tor Browser 12.0 for Android is the option to "prioritize .onion sites" where available. When enabled, you will be redirected automatically to the matching .onion site for any web site that has [Onion-Location](https://community.torproject.org/onion-services/advanced/onion-location/) configured â helping you to discover new .onion sites in the wild.

You can turn "Prioritize .onion sites" on under the Privacy and Security section within Tor Browser for Android's Settings menu. Please note that this update does not include the purple ".onion avilable" button in the address bar, which is still unique to Tor Browser for desktop.

### And more...

12.0 is the first stable release of Tor Browser that supports Albanian (sq) and Ukranian (uk). We owe a huge thank you to all the volunteers who worked hard to translate Tor Browser into each language <3

If you spot a string that still needs to be translated, or would like to contribute towards the localization of another language, please visit our [Community portal](https://community.torproject.org/localization/) to find out how to get started.

We've also been busy making various behind-the-scenes improvements to features like tor-launcher (which starts tor within Tor Browser), the code for which has undergone a significant refactoring. As such, if you run a non-standard Tor Browser setup (like using system tor in conjunction with Tor Browser, or very partiular network settings) and experience an unexpected error message when launching Tor - please let us know by [filing an issue in our Gitlab repo](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues).

Lastly, Tor Browser's [letterboxing](https://support.torproject.org/tbb/maximized-torbrowser-window/) feature has received a number of minor improvements to its user experience, including (but not limited to) fixing potantial leaks and bypasses, removing the 1px border in fullscreen videos, and disabling the feature entirely on trusted pages like the Connect to Tor screen, among others.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/). Thanks to all of the teams across Tor, and the many volunteers, who contributed to this release.

## Full changelog

The full changelog since [Tor Browser 11.5.10](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-12.0/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Update Translations
  + Update tor to 0.4.7.12
  + [Bug tor-browser#17228](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/17228): Consideration for disabling/trimming referrers within TBB
  + [Bug tor-browser#24686](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/24686): In Tor Browser context, should network.http.tailing.enabled be set to false?
  + [Bug tor-browser#27127](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/27127): Audit and enable HTTP/2 push
  + [Bug tor-browser#27258](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/27258): font whitelist means we don't have to set gfx.downloadable\_fonts.fallback\_delay
  + [Bug tor-browser#40057](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40057): ensure that CSS4 system colors are not a fingerprinting vector
  + [Bug tor-browser#40058](https://gitlab.torproject.org/tpo/app...