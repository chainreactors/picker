---
title: New Release: Tor Browser 15.0.1
url: https://blog.torproject.org/new-release-tor-browser-1501/
source: Tor Project blog
date: 2025-11-11
fetch_date: 2025-11-12T03:13:12.608773
---

# New Release: Tor Browser 15.0.1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 15.0.1

by [morgan](/author/morgan)
| November 11, 2025

![](/new-release-tor-browser-1501/lead.png)

Tor Browser 15.0.1 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/15.0.1/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-15.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 15.0 is:

* All Platforms
  + Updated NoScript to 13.4
  + [Bug tor-browser#44319](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44319): Rebase Tor Browser onto 140.5.0esr
  + [Bug tor-browser#44325](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44325): Backport Security Fixes from Firefox 145
  + [Bug tor-browser#44333](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44333): Add the "No AI" version of DuckDuckGo to available search engines
  + [Bug mullvad-browser#487](https://gitlab.torproject.org/tpo/applications/mullvad-browser/-/issues/487): Search engines are sorted alphabetically rather than the desired order
* Windows + macOS + Linux
  + Updated Firefox to 140.5.0esr
  + [Bug tor-browser#44310](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44310): Default zoom always resets to 100%
  + [Bug tor-browser#44314](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44314): Upgrade message not shown in about:tor
* Linux
  + [Bug tor-browser#44273](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44273): Restore Noto CJK as Jigmo has a too low readability
  + [Bug tor-browser#44315](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44315): Font/text issue with self-upgrade window
* Android
  + Updated GeckoView to 140.5.0esr
  + [Bug tor-browser#44303](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44303): Extension update job might never work on Android
* Build System
  + All Platforms
    - [Bug tor-browser-build#41618](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41618): Restore the expert bundle's version in the final release directory
  + Windows + Linux + Android
    - Updated Go to 1.24.10
  + Android
    - [Bug tor-browser-build#41617](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41617): Pass page size to zipalign
    - [Bug tor-browser-build#41620](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41620): Do not rerun zipalign when signing
    - [Bug tor-browser-build#41621](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41621): Remove support using older android build tools when signing 14.5 releases in tools/signing/wrappers/sign-apk

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1501/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1501/&text=Tor%20Browser%2015.0.1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1501/&text=Tor%20Browser%2015.0.1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2015.0.1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1501/)

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

## Upcoming Events

November 12, 2025 – December 10, 2025

## [State of the Onion 2025](/event/state-of-the-onion-2025/)

## Recent Updates

## [New Release: Tor Browser 15.0.1](/new-release-tor-browser-1501/)

by [morgan](/author/morgan)
| November 11, 2025

Tor Browser 15.0.1 is now available from the Tor Browser download page and also from our distribution directory.

## [Keeping the internet free together: Join us for State of the Onion 2025](/state-of-the-onion-2025/)

by [arturom](/author/arturom) and [pavel](/author/pavel)
| November 4, 2025

When censorship strikes, Tor provides a lifeline to access information--a lifeline to a FREE INTERNET. Tune in to this year's 2025 State of the Onion event to hear about how our teams and community work tirelessly behind the scenes to keep it alive.Â

## [Arti 1.7.0 released: Onion service restricted discovery, experimental HTTP proxy, relay development, and more.](/arti_1_7_0_released/)

by [opara](/author/opara)
| November 3, 2025

Arti 1.7.0 is released and ready for download.

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