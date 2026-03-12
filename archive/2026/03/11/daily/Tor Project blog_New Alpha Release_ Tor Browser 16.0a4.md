---
title: New Alpha Release: Tor Browser 16.0a4
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a4/
source: Tor Project blog
date: 2026-03-11
fetch_date: 2026-03-12T04:08:53.244251
---

# New Alpha Release: Tor Browser 16.0a4

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a4

by [ma1](/author/ma1)
| March 11, 2026

![](/new-alpha-release-tor-browser-160a4/lead.png)

Tor Browser 16.0a4 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a4/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a3 is:

* All Platforms
  + Updated NoScript to 13.6.6.90401984
  + Updated zlib to 1.3.2
  + [Bug tor-browser#44663](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44663): NoScript behavior on âSaferâ security level prevents integrity checks for dynamically loaded javascript
  + [Bug tor-browser#44675](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44675): Restore "BB 43850: Modify the Contrast Control settings for RFP" dropped during the 148.0a1 rebase
  + [Bug tor-browser#44679](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44679): Review Mozilla 2006066: Credit cards autofill settings are not visible
  + [Bug tor-browser#44680](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44680): Properly handle subdocuments created by data: URLs
  + [Bug tor-browser#44687](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44687): Security level requires a restart in a new profile after 148 update
  + [Bug tor-browser#44689](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44689): Forwardport tor-browser#44668 from legacy to alpha: Set detailsURL in update XML to be useful for 13.5 users
  + [Bug tor-browser#44701](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44701): Unexpected change to `netwerk/url-classifier/components.conf`
  + [Bug tor-browser#44706](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44706): creating a new profiles causes crash ENOTTY
  + [Bug tor-browser-build#41738](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41738): Allow to specify an unsupportedURL on update responses
* Windows + macOS + Linux
  + Updated Firefox to 148.0a1
  + [Bug tor-browser#42664](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42664): Use mozilla token sizes in CSS
  + [Bug tor-browser#44634](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44634): Review Mozilla 2006250: add ai window about:preferences section within ai features
  + [Bug tor-browser#44682](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44682): Wrong pid in the exit log
  + [Bug tor-browser#44709](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44709): Hide the AI settings panel
  + [Bug tor-browser#44710](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44710): Hide about:preferences#translations
  + [Bug tor-browser#44713](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44713): The about dialog is missing some padding in 148.0a1
  + [Bug tor-browser#44717](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44717): Search suggestion settings are visible in 148
* Windows + Linux
  + [Bug tor-browser-build#40892](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40892): Move torrc-defaults, geoip and geoip6 on Windows and Linux
* Windows
  + [Bug tor-browser#44461](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44461): Window controls are missing on Windows
  + [Bug tor-browser#44633](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44633): Move D3D11 function from local webrtc changes to tbb webrtc patches
* Linux
  + [Bug tor-browser#44394](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44394): Do not read default prefs from /etc/firefox
* Android
  + Updated GeckoView to 148.0a1
  + [Bug tor-browser#43349](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43349): Add user feedback for when Tor connects (Android)
  + [Bug tor-browser#43909](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43909): Review Mozilla: TBD: new Android tab-strip feature
  + [Bug tor-browser#44226](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44226): Disable all link sharing functionality
  + [Bug tor-browser#44274](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44274): Review Mozilla 1986534: Disable screenshots in PBM
  + [Bug tor-browser#44469](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44469): Fix branding on Android RR
  + [Bug tor-browser#44506](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44506): Remove more sync from 147
  + [Bug tor-browser#44582](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44582): Fix or remove new settings search functionality on Android
  + [Bug tor-browser#44661](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44661): Restore or fix new rebase-148 uses of moz assets instead of TB ones
  + [Bug tor-browser#44718](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44718): Fix splash screen branding and other issues in RR
  + [Bug tor-browser#44721](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44721): Android build failure in nightlyOssLicensesTask: missing dependencies.json file
* Build System
  + All Platforms
    - [Bug tor-browser-build#41690](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41690): Merge list\_toolchain\_updates-firefox-\* commands into one
    - [Bug tor-browser-build#41725](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41725): Update toolchains for Firefox 148
    - [Bug tor-browser-build#41726](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41726): Check in list\_toolchain\_updates that the sha512sum we have for the macOS SDK is the same as Mozilla
    - [Bug tor-browser-build#41727](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41727): Split the list\_toolchain\_updates\_checks script in two
    - [Bug tor-browser-build#41728](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41728): Update projects/application-services/list\_toolchain\_updates\_checks to check nss sha256sum
  + Windows + macOS + Linux
    - [Bug tor-browser#44406](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44406): Fix CSS linting issues introduced by 146
  +...