---
title: New Release: Tor Browser 12.0.4
url: https://blog.torproject.org/new-release-tor-browser-1204/
source: Tor Project blog
date: 2023-03-19
fetch_date: 2025-10-04T10:03:29.661992
---

# New Release: Tor Browser 12.0.4

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 12.0.4

by [richard](/author/richard)
| March 18, 2023

![](/new-release-tor-browser-1204/lead.png)

Tor Browser 12.0.4 is now available from the Tor Browser [download page](https://www.torproject.org/download/) and also
from our [distribution directory](https://dist.torproject.org/torbrowser/12.0.4/).

This release updates Firefox to 102.9.0esr, including bug fixes, stability improvements
and important [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-10/). We also backported the Android-specific [security updates](https://www.mozilla.org/en-US/security/advisories/mfsa2023-09/) from Firefox 111.

We use this opportunity to update various components of Tor Browser as well:

* NoScript 11.4.18

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 12.0.3](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-12.0/projects/browser/Bundle-Data/Docs/ChangeLog.txt) is:

* All Platforms
  + Updated Translations
  + Updated NoScript to 11.4.18
  + [Bug tor-browser#41598](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41598): Prevent NoScript from being removed / disabled until core functionality has been migrated to Tor Browser
  + [Bug tor-browser#41603](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41603): Customize the creation of MOZ\_SOURCE\_URL
  + [Bug tor-browser#41627](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41627): Enable network.http.referer.hideOnionSource in base-browser
  + [Bug tor-browser#41637](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41637): cherry-pick Mozilla 1814416: Generalize the app name in about:buildconfig. r=ahochheiden
  + [Bug tor-browser#41659](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41659): Add canonical color definitions to base-browser
  + [Bug tor-browser#41669](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41669): Rebase Tor Browser stable to 102.9.0esr
* Windows + macOS + Linux
  + Updated Firefox to 102.9esr
  + [Bug tor-browser#41542](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41542): Disable the creation of a default profile
  + [Bug tor-browser#41574](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41574): Use --warning-color variable for the "Custom" label in the security level popup.
  + [Bug tor-browser#41606](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41606): Move the changes to the hamburger menu out of the Torbutton commit
  + [Bug tor-browser#41626](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41626): Bridge-emojii tooltips not localized in ES locale
* Android
  + Updated GeckoView to 102.9esr
  + [Bug tor-browser#41679](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41679): Backport Android-specific security fixes from Firefox 111 to ESR 102.9-based Tor Browser
* Build System
  + All Platforms
    - Updated Go to 1.19.7
    - [Bug tor-browser-build#40764](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40764): Embed repo URL and git revision in Firefox
    - [Bug tor-browser-build#40782](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40782): Update tools/signing/download-unsigned-sha256sums-gpg-signatures-from-people-tpo to fetch from tb-build-04 and tb-build-05
  + macOS
    - [Bug tor-browser-build#40790](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40790): Fix dmg2mar after dmg changes from #28124
    - [Bug tor-browser-build#40791](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40791): tools/dmg2mar should exit with an error when there is an error creating the mar file
  + Android
    - [Bug tor-browser-build#40789](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/40789): Broken mirror links for glean: link 404 for version 5.0.1 hosted at aguestuser's tor people storage

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1204/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1204/&text=Tor%20Browser%2012.0.4%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1204/&text=Tor%20Browser%2012.0.4%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2012.0.4%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1204/)

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

## [New Alpha Release: Tor Browser 15.0a3](/new-alpha-release-tor-browser-150a3/)

by [boklm](/author/boklm)
| September 22, 2025

Tor Browser 15.0a3 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.0](/new-release-tails-7_0/)

by [tails](/author/tails)
| September 18, 2025

We are very excited to present you Tails 7.0, the first version of Tails based
on Debian 13 (Trixie) and GNOME 48 (Bengaluru). Tails 7.0 brings new versions
of many applications included in Tails.

## [New Release: Tor Browser 14.5.7](/new-release-tor-browser-1457/)

by [ma1](/author/ma1)
| September 16, 2025

Tor Browser 14.5.7 is now available from the Tor Browser download page and also from our distribution directory.

### Download Tor Browser

Download Tor Browser to experience real private browsing without tracking, surveillance, or censorship.

[Download Tor Browser](https://www.torproject.org/download/)

### Subscribe to our Newsletter

Get monthly updates and opportunities from the Tor Project:

[Sign up](https://newsletter.torproject.org/)

####

####

####

####

####

####

####

####

Trademark, copyright notices, and rules for use by third parties can be found in our [FAQ](https://www.torproject.org/about/trademark/).