---
title: New Alpha Release: Tor Browser 16.0a5
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a5/
source: Tor Project blog
date: 2026-04-01
fetch_date: 2026-04-02T04:31:38.416400
---

# New Alpha Release: Tor Browser 16.0a5

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a5

by [ma1](/author/ma1)
| April 1, 2026

![](/new-alpha-release-tor-browser-160a5/lead.png)

Tor Browser 16.0a5 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a5/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a4 is:

* All Platforms
  + Updated NoScript to 13.6.14.90101984
  + Updated Tor to 0.4.9.6
  + [Bug tor-browser#43858](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43858): Clean out deprecated or unused methods in TorConnect
  + [Bug tor-browser#44251](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44251): Drop pt\_config.json meek-azure migration logic
  + [Bug tor-browser#44546](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44546): Rename `appearance-chooser-item` to `setting-chooser-item` after we reach nightly 149
  + [Bug tor-browser#44621](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44621): Move about:torconnect back to browser
  + [Bug tor-browser#44702](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44702): Rebase alpha onto 149.0a1
  + [Bug tor-browser#44720](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44720): Migrate New Identity commit to Tor Browser
  + [Bug tor-browser#44753](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44753): Drop TorProvider.isBootstrapDone
  + [Bug tor-browser#44755](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44755): Trusted Types (Firefox 148 and above) + Web Workers broken on Safer Level
  + [Bug rebase-149#44757](https://gitlab.torproject.org/tpo/applications/rebase-149/-/issues/44757): Update tests for removed Services.search [tor-browser]
  + [Bug tor-browser#44761](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44761): Safer Level's worker patching filters out Worker constructor options
  + [Bug tor-browser#44763](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44763): Disable WebGPU until audited
  + [Bug tor-browser#44764](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44764): Review Mozilla 2012344: Hide main AI settings when the feature is blocked
  + [Bug tor-browser#44765](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44765): Review Mozilla 1972073: Convert Sidebar to config-based prefs
  + [Bug tor-browser#44767](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44767): Safer Level's worker patching throws on new about:blank frames with Trusted Types
  + [Bug tor-browser#44772](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44772): Review Mozilla 1980264: Canvas randomization is too slow
  + [Bug tor-browser#44778](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44778): Safer Level: xray causes patched TrustedTypePolicy instances to be unusable by content.
  + [Bug tor-browser#44801](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44801): Redact onion origins from Location.ancestorOrigins.
  + [Bug tor-browser#44814](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44814): Disable trustpanel until our new designs are ready
* Windows + macOS + Linux
  + Updated Firefox to 149.0a1
  + [Bug tor-browser#44714](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44714): The browser opens a new about:blank tab in 148
  + [Bug tor-browser#44780](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44780): AIFeature.sys.mjs failures in 149 desktop builds
  + [Bug tor-browser#44781](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44781): Use a static page title for about:torconnect
  + [Bug tor-browser#44793](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44793): `privacy.spoof_english` console error in about:preferences
  + [Bug tor-browser#44797](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44797): Clean up `about:torconnect` styling
  + [Bug tor-browser#44799](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44799): Onionize toggle in `about:tor` uses blue text color
* Android
  + Updated GeckoView to 149.0a1
  + [Bug tor-browser#43790](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43790): Address "Various android workarounds" commit introduced in the 138 rebase
  + [Bug tor-browser#44332](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44332): Fix android tor logs screen issues presented in 144 rebase
  + [Bug tor-browser#44594](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44594): DoH is visible on Android
  + [Bug tor-browser#44653](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44653): Disable "Allow search suggestions in private sessions" prompt presented in RR 148 android
  + [Bug tor-browser#44694](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44694): Remove new "Tab bar" feature on Android
  + [Bug tor-browser#44698](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44698): Clean up comments in AccountSettingsFragment.kt. FIXME: Update A-S
  + [Bug tor-browser#44700](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44700): Untracked change to `HomepageHeader.kt`
  + [Bug tor-browser#44751](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44751): Noscript (and likely any extension) can be accidently turned off on Android alpha
  + [Bug tor-browser#44752](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44752): Remove new expanded toolbar option on Android due to fingerprintability
  + [Bug tor-browser#44785](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44785): Fix SiteSecurityRobot.kt after the 149 rebase
  + [Bug tor-browser#44788](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44788): Extensions are unreachable via 3 dot menu in alpha (android)
  + [Bug tor-browser#44789](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44789): Icon of "New Circuit" is not centered but lies in top left corner
* Build System
  + All Platforms
    - [Bug tor-browser#43180](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43180): Remove translation CI 13.5 legacy extension
    - [Bug tor-browser-build#41758](https://gitla...