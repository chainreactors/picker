---
title: New Alpha Release: Tor Browser 14.0a3
url: https://blog.torproject.org/new-alpha-release-tor-browser-140a3/
source: Tor Project blog
date: 2024-08-29
fetch_date: 2025-10-06T18:12:49.657382
---

# New Alpha Release: Tor Browser 14.0a3

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.0a3

by [morgan](/author/morgan)
| August 28, 2024

![](/new-alpha-release-tor-browser-140a3/lead.png)

Tor Browser 14.0a3 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0a3/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## ESR Progress

As discussed in our [previous blog post](https://blog.torproject.org/new-alpha-release-tor-browser-140a1/), we are hard at work updating Tor Browser to the Firefox ESR-128.

Now that we have all of our platforms rebased and building, we will be making (roughtly) weekly releases until the final 14.0 release in September.

### Android APK Size Reduction

Over the past week we have made some progress on the Android APK size front, but we have not yet reduced the size beneath Google Play's threshold. So far we have shaved off about a megabyte by removing unused assets from the Android build.

In the short-term, we will likely be removing the Conjure pluggable-transport from our x86 and x86\_64 Android builds. This pluggable-transport is still in testing and none of our built-in bridges depend on it, so the vast majority of users would be unaffected by its removal. We will also be removing tor's unused Geoip database (used on Desktop for the circuit-display) from all Android builds. Neither of these are long-term solutions, but should be good enough for the 14.0 series.

We are also prototyping integrating [UPX](https://upx.github.io/) into our Android builds to reduce our executable sizes. We would prefer to not include this in our final release, due to potential performance regressions and reproducibility issues, though initial tests suggests neither are currently a problem.

### Desktop Styling Fixes

After a year of upstream changes, Tor Browser's user-interface patches tend to get a little 'dusty'. Styling choices which looked right in ESR-115 may now look a little off in ESR-128, pages may reference css rules which no longer exist, or we may be using colours which have since have been altered upstream. So, we've been working the past few releases on various patches to clean up these rough edges and polishing all of Tor Browser's custom frontend elements.

If you happen to find any Tor Browser UI which looks a bit off or could use some polish, please send us your feedback!

### Bugzilla Triage and Review

We have 180 remaining upstream Bugzilla issues to review and potentially develop patches for.

This work can be tracked in [this Gitlab query](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=opened&search=Review%20Mozilla&label_name%5B%5D=14.0%20stable&first_page_size=100).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Known Issues

There are a few known issues which we are aware of.

#### No Tor Browser 14.0a2 for x86 and x86\_64 on Google Play Store

Our alpha release exceeds the Google Play Store's limit on APK size for x86 and x86\_64 devices. This is being tracked here:

* <https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42607>

## Full changelog

The full changelog since [Tor Browser 14.0a2](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + [Bug tor-browser#40056](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40056): Ensure that the lazy loading attribute is ignored on script-disabled documents
  + [Bug tor-browser#42611](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42611): Set clipboard.imageAsFile.enabled to false
  + [Bug tor-browser#42646](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42646): Drop patch for tor-browser#40166
  + [Bug tor-browser#42830](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42830): Enable WebAudio APIs
  + [Bug tor-browser#43012](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43012): Mixed content: browser requests HTTPS images from onion domain accessed via HTTP
  + [Bug tor-browser#43013](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43013): security.mixed\_content.upgrade\_display\_content.image is true by default
  + [Bug tor-browser#43074](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43074): Pass the browser to TorDomainIsolator.newCircuitForBrowser
  + [Bug tor-browser#43085](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43085): Rebase Tor Browser Alpha onto 128.2.0esr
* Windows + macOS + Linux
  + Updated Firefox to 128.2.0esr
  + [Bug tor-browser#41811](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41811): Primary buttons that result in a connection attempt should be purple
  + [Bug tor-browser#41817](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41817): Add more color aliases that take dark mode into account
  + [Bug tor-browser#41820](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41820): Downloads warning styling improvements (use moz-message-bar)
  + [Bug tor-browser#42212](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42212): Fluent migration: onion services
  + [Bug tor-browser#42603](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42603): Remove safebrowsing URLs
  + [Bug tor-browser#42665](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42665): Drop "Learn More" spacing
  + [Bug tor-browser#43059](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43059): Drag and Drop issue in new update 13.5.2
  + [Bug tor-browser#43066](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43066): about:torconnect no longer changes the title icon on errors
  + [Bug tor-browser#43067](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43067): Use html:link rather than xml-stylesheet in our dialogs
  + [Bug tor-browser#43071](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43071): Make sure "tor-button" elements that are also "primary" still use the tor colors
  + [Bug tor-browser#43081](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43081): Remove hard-coded CSS `line-height`
* Linux
  + [Bug tor-browser#43064](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43064): Make copy/paste and drag/drop file filtering more specific
* Android
  + Updated GeckoView to 128.2.0esr
  + [Bug tor-browser#42386](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42386): Remove unused assets to reduce APK size
  + [Bug tor-browser#42590](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42590): âTor browserâ text in top left of home fragment/new tab view gets cut off with larger text sizes
  + [Bug tor-browser#43078](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43078): Disable Sharing Links to TBA
  + [Bug tor-browser-build#41223](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41223): Tor Browser Alpha version not displayed correctly
* Build System
  + All Platforms
    - [Bug tor-browser-build#41013](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41013): Add a README to each project
    - [Bug tor-browser-build#41198](https://gitlab.torproject.org/tpo/app...