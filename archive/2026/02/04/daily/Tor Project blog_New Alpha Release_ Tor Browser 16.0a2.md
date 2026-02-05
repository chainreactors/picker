---
title: New Alpha Release: Tor Browser 16.0a2
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a2/
source: Tor Project blog
date: 2026-02-04
fetch_date: 2026-02-05T04:10:19.981326
---

# New Alpha Release: Tor Browser 16.0a2

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a2

by [morgan](/author/morgan)
| February 4, 2026

![](/new-alpha-release-tor-browser-160a2/lead.png)

Tor Browser 16.0a2 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a2/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

Finally, we would like to thank the following community members for their contributions this release:

* NoisyCoil for their fixes for [tor-browser-build#41706](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41706)

If you would like to contribute, our contributor guide can be found [here](https://gitlab.torproject.org/tpo/applications/wiki/-/wikis/Development-Information/Tor-Browser/Contributing-to-Tor-Browser).

## Catching up With Rapid-Release

Over the past few months we have been sprinting to catch Tor Browser Alpha up with Firefox Rapid-Release. Tor Browser Alpha is now based on Firefox 147 and the rebase to Firefox 148 is [now underway](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44510). We also have a massive head-start on our bugzilla triage and have already flagged dozens of upstream patches which we will need to [investigate further for ESR 153](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues?sort=created_date&state=opened&label_name%5B%5D=Apps%3A%3AType%3A%3AAudit&milestone_title=Browser%2016.0&first_page_size=100).

Unfortunately (though somewhat expectedly), all this progress has introduced some bugs and blockers.

### ð¤ Android APK Too Big

The upstream changes from Firefox pushed us over the approximate 100 MB size limit imposed by the Google Play Store on our Android packages. To trim off some more bytes and get us under the threshold we back-ported usage of the [terser JavaScript minifier](https://terser.org/) (to reduce the size of the JavaScript source) and we now conditionally compile out preferences for unrelated platforms (i.e. we no longer ship preferences on Tor Browser Android which only affect Desktop).

This issue has been resolved in [tor-browser-build#41688](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41688).

### ð Websites Failed to Load

In Tor Browser 16.0a1 we discovered an intermittent issue where websites would fail to load after bootstrapping. This has a resulted in the browser being essentially unusable for a significant number of testers.

The proximal cause for this that the NoScript extension would be put to sleep and unable to respond to requests made by the browser content process. Our engineers discovered this seems to have been fallout over upstream changes around how WebExtensions interact with the browser in permanent private-browsing mode. For now, we have worked-around this bug with patches to both NoScript and Tor Browser. When we know more, we will open an issue upstream with Mozilla.

This issue has been resolved in [tor-browser#44398](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44398).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a1 is:

* All Platforms
  + Updated NoScript to 13.5.11.90301984
  + Updated Tor to 0.4.9.4-rc
  + Updated OpenSSL to 3.5.5
  + [Bug tor-browser#44303](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44303): Extension update job might never work on Android
  + [Bug tor-browser#44416](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44416): Rebase alpha onto 147
  + [Bug tor-browser#44420](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44420): Drop "rights" from components.conf
  + [Bug tor-browser#44482](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44482): Script execution in Safest mode via data URI navigation
  + [Bug tor-browser#44492](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44492): Fix python linting warnings in our test files
  + [Bug tor-browser#44580](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44580): Registers noscript to check for updates on first run
  + [Bug tor-browser-build#41676](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41676): Update toolchains for Firefox 147
* Windows + macOS + Linux
  + Updated Firefox to 147.0a1
  + [Bug tor-browser#44289](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44289): RFPHelper console error when `--toolbar-field-color` is set to `inherit`
  + [Bug tor-browser#44343](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44343): Hide the default browser settings again after MozBug 1969949
  + [Bug tor-browser#44460](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44460): Payment methods and addresses setting headings are visible in settings
  + [Bug tor-browser#44522](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44522): Move common changes to about dialog to base-browser
  + [Bug tor-browser#44535](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44535): Letterboxing background colour is no longer used
  + [Bug tor-browser#44554](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44554): Unlabeled AI item in tab context menu in 147
* Linux
  + [Bug tor-browser#44410](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44410): Use system's size for UI font on Linux
* Android
  + Updated GeckoView to 147.0a1
  + [Bug tor-browser#44398](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44398): Unable to load websites after a short amount of time on Android
  + [Bug tor-browser#44469](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44469): Fix branding on Android RR
  + [Bug tor-browser#44507](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44507): Drop the dependency on Sentry
  + [Bug tor-browser#44523](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44523): New circuit seems to have disappeared from 147 on Android
  + [Bug tor-browser#44532](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44532): Backport Bug 1967968: Minify the pdf.js code in order to improve the loading performance
  + [Bug tor-browser#44533](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44533): Update NoScript to the version bundled with the browser on Android
  + [Bug tor-browser#44591](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44591): TBA Alpha fails to ini...