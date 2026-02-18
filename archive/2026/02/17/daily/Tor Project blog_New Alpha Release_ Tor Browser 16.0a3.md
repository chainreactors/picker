---
title: New Alpha Release: Tor Browser 16.0a3
url: https://blog.torproject.org/new-alpha-release-tor-browser-160a3/
source: Tor Project blog
date: 2026-02-17
fetch_date: 2026-02-18T04:16:18.360552
---

# New Alpha Release: Tor Browser 16.0a3

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 16.0a3

by [ma1](/author/ma1)
| February 17, 2026

![](/new-alpha-release-tor-browser-160a3/lead.png)

Tor Browser 16.0a3 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/16.0a3/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

â ï¸ **Reminder**: The Tor Browser Alpha release-channel is for [testing only](https://community.torproject.org/user-research/become-tester/). As such, Tor Browser Alpha is not intended for general use because it is more likely to include bugs affecting usability, security, and privacy.

Moreover, Tor Browser Alphas are now based on Firefox's betas. Please read more about this important change in the [Future of Tor Browser Alpha](https://blog.torproject.org/future-of-tor-browser-alpha/) blog post.

If you are an at-risk user, require strong anonymity, or just want a reliably-working browser, please stick with the [stable release channel](https://www.torproject.org/download/).

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 16.0a2 is:

* All Platforms
  + Updated Tor to 0.4.9.5
  + Updated NoScript to 13.5.12.90301984
  + [Bug tor-browser#44562](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44562): Set the new online Suggest prefs to false
  + [Bug tor-browser#44571](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44571): Disable restrict\_to\_adults for potential fingerprintability
  + [Bug tor-browser#44619](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44619): Add custom logs to Tor logs
  + [Bug tor-browser#44625](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44625): metamask.io won't load on Safer security level
  + [Bug tor-browser#44626](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44626): Propagate WASM blocking to workers
  + [Bug tor-browser#44647](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44647): Clean up patch for `SearchEngineSelector.sys.mjs`.
  + [Bug tor-browser#44652](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44652): Backport fix for Firefox Bug 2014390
  + [Bug tor-browser-build#41713](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41713): Try to find a component for bugs found with commits in triage spreadsheets
* Windows + macOS + Linux
  + [Bug tor-browser#43560](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43560): Add "UTC" to the end of the timestamp on tor logs (Desktop)
  + [Bug tor-browser#44459](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44459): Letterboxing content alignment setting is missing styling
  + [Bug tor-browser#44520](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44520): Make sure "Firefox labs" is hidden by default
* Windows
  + [Bug tor-browser#44623](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44623): 16.0a2: about:preferences#privacy is empty
* Linux
  + [Bug tor-browser#44050](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44050): Consider changing the domain in DBus interfaces
* Android
  + [Bug tor-browser#43403](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43403): Add "UTC" to the end of the timestamp on tor logs (Android)
  + [Bug tor-browser#44057](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44057): Drop about:torconnect from android
  + [Bug tor-browser#44620](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44620): Move the Android IPC directory
  + [Bug tor-browser-build#28595](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/28595): Remove the need to update var/gradle\_dependencies\_version
* Build System
  + All Platforms
    - [Bug tor-browser-build#40338](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40338): Running `make release` multiple times fails
    - [Bug tor-browser-build#41660](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41660): Add a Firefox target to build unpatched Firefox in tor-browser-build
    - [Bug tor-browser-build#41693](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41693): Drop base-browser targets
    - [Bug tor-browser-build#41720](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41720): cp -l in release/build fails when crossing file systems
    - [Bug rbm#40093](https://gitlab.torproject.org/tpo/applications/rbm/-/issues/40093): Make it easy to get the sha256sum of an input\_files file
    - [Bug rbm#40103](https://gitlab.torproject.org/tpo/applications/rbm/-/issues/40103): Allow having multiple tmp\_dir values
  + Windows + Linux + Android
    - Updated Go to 1.25.7
  + Android
    - [Bug tor-browser-build#41719](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41719): Enable network when var/generate\_gradle\_dependencies\_list is set in geckoview

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a3/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a3/&text=Tor%20Browser%2016.0a3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-160a3/&text=Tor%20Browser%2016.0a3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2016.0a3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-160a3/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproject.org/c/news/11)!

## Recent Updates

## [New Alpha Release: Tor Browser 16.0a3](/new-alpha-release-tor-browser-160a3/)

by [ma1](/author/ma1)
| February 17, 2026

Tor Browser 16.0a3 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tor Browser 15.0.6](/new-release-tor-browser-1506/)

by [ma1](/author/ma1)
| February 16, 2026

Tor Browser 15.0.6 is now available from the Tor Browser download page and also from our distribution directory.

## [Keeping track of decisions using th...