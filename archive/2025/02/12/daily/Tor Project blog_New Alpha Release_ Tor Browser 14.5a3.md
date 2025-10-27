---
title: New Alpha Release: Tor Browser 14.5a3
url: https://blog.torproject.org/new-alpha-release-tor-browser-145a3/
source: Tor Project blog
date: 2025-02-12
fetch_date: 2025-10-06T20:47:19.568024
---

# New Alpha Release: Tor Browser 14.5a3

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.5a3

by [morgan](/author/morgan)
| February 11, 2025

![](/new-alpha-release-tor-browser-145a3/lead.png)

Tor Browser 14.5a3 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.5a3/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Call for Testing

It is getting close to our soft-code freeze in early April and our scheduled release date of April 29th. Now would be an excellent time for the community to take the latest Alpha releases for a spin!

If you are interested in becoming a tester, please go and download the latest Tor Browser Alpha release for your preferred platform, give it a go, and report any problems you run into either on the [forum](https://forum.torproject.org/t/become-an-alpha-tester/31) or on our [gitlab instance](https://gitlab.torproject.org/tpo/applications/tor-browser).

### QA-Checklists

Beyond just âkicking the tiresâ (so to speak) we also have a test check-list/itinerary the devs will be going through for all of our supported platforms:

* Desktop (Windows, macOS, Linux): [Test Tor Browser Desktop 14.5 Release Candidates (tor-browser#43510)](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43510)
* Android: [Test Tor Browser Android 14.5 Release Candidates (tor-browser#43511)](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43511)

If you are feeling adventurous, we would also appreciate it if community members sampled from these checklists and ensure the scenarios you care about work as you would expect in Tor Browser 14.5 Alpha before it stabilizes.

### NoScript

We would ask the quite adventerous users familiar with Tor Browser's Security Level feature to try out the latest NoScript Release Candidate. NoScript 12.x, which has been rolled out to Tor Browser users at the beginning of 2025, has undergone massive "behind the scenes" changes to make it compatible with the newest Manifest V3 browser extensions API.

A lot of effort has been put in the transition to preserve 1-to-1 feature parity, but given the size of these changes some bugs have been introduced and promptly fixed. Other less obvious ones may still be lingering around!

It would be very helptul if alpha testers could:

1. Switch to [NoScript's Release Candidate channel](https://secure.informaction.com/download/betas/latest) to get the most up-to-date fixes and enhancements
2. Exercise the Tor Browser at different security levels and paying attention if anything seems odd either in the transition between levels or in the websites behavior compared to what is expected at that level
3. Report issues either on the Tor Browser [issue tracker](https://gitlab.torproject.org/dashboard/issues?sort=updated_desc&state=opened&label_name[]=NoScript) with the label `~NoScript` or on NoScript's own [issue tracker](https://github.com/hackademix/noscript/issues), specifying NoScript's version as can be read in Tor Browser by `â¡ > Addons and themes > Extensions`.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.5a2](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + [Bug tor-browser#41065](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41065): navigator.storage "best effort" + "persistent" leak partitionSize/totalSpace entropy
  + [Bug tor-browser#41921](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41921): Clean up initialisation and bridges conflict between TorSettings and TorConnect
  + [Bug tor-browser#43308](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43308): Only allow "about:" pages to have access to contentaccessible branding assets
  + [Bug tor-browser#43323](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43323): Expose a stable asset from chrome:// to identify Tor, Base, and Mullvad Browser
  + [Bug tor-browser#43449](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43449): Rebase Tor Browser alpha onto 128.7.0esr
  + [Bug tor-browser#43451](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43451): Backport security fixes from Firefox 135
  + [Bug tor-browser-build#41362](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41362): Remove meek azure from the builtin bridges
* Windows + macOS + Linux
  + Updated Firefox to 128.7.0esr
  + [Bug tor-browser#41831](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41831): Some .tor.onion sites are not displaying the underlying V3 onion address in alpha
  + [Bug tor-browser#43254](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43254): Cancel Moat requests when no longer needed
  + [Bug tor-browser#43386](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43386): Extension requests expose Firefox's minor version and custom app name
  + [Bug tor-browser#43398](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43398): tor-urlbar-button-plain hover styling is overwritten by tor-button rule
  + [Bug tor-browser#43406](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43406): 2 buttons displayed onion-available and connect when Tor daemon killed
  + [Bug tor-browser#43461](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43461): Drop our wordmark padding
  + [Bug tor-browser#43462](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43462): Use NetworkLinkService instead of Moat for the internet test
  + [Bug tor-browser#43466](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43466): Drop unnecessary CSS rules in branding aboutDialog.css
* Windows
  + [Bug tor-browser#43402](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43402): set browser.startup.blankWindow false
* macOS
  + [Bug tor-browser#43468](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43468): ScreenCaptureKit framework should be a weak link
* Linux
  + [Bug tor-browser-build#41297](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41297): Add video codecs dependencies (recommends) on the Debian package
* Android
  + Updated GeckoView to 128.7.0esr
  + [Bug tor-browser#43198](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43198): Remove "Learn more" link from Android's no-internet error
  + [Bug tor-browser#43199](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43199): Bootstrapping bar needs a little TLC on Android (Part 1)
  + [Bug tor-browser#43222](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43222): All tor logs timestamps reset to current time when opening screen
  + [Bug tor-browser#43351](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43351): Don't force ALL CAPS for the fenix snackbar action button text
  + [Bug tor-browser#43359](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43359): Improper handling of TorBootstrapChangeListener with respect to system onDestroy() calls for HomeActivity
  + [Bug tor-browser#43360](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43360): Replace custom variable isBeingRecreated with built-in isFinish...