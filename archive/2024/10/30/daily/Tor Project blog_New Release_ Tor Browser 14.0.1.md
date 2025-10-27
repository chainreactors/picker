---
title: New Release: Tor Browser 14.0.1
url: https://blog.torproject.org/new-release-tor-browser-1401/
source: Tor Project blog
date: 2024-10-30
fetch_date: 2025-10-06T18:55:54.597756
---

# New Release: Tor Browser 14.0.1

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 14.0.1

by [morgan](/author/morgan)
| October 29, 2024

![](/new-release-tor-browser-1401/lead.png)

Tor Browser 14.0.1 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0.1/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Known Issues

The tor daemon for aarch64 macOS (M1 and friends) will crash when visiting some onion-service sites, resulting in an inoperable Tor Browser (you can restart Tor Browser to work around this for now, but the particular failing onion-service sites will be inaccessible until we develop a fix). This issue is being tracked in [tor-browser#43245](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43245)

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.0](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-14.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated Tor to 0.4.8.13
  + [Bug tor-browser#43231](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43231): Rebase Tor Browser 128-based stable and alpha onto 128.4.0esr
  + [Bug tor-browser#43240](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43240): Backport security fixes from Firefox 132
* Windows + macOS + Linux
  + Updated Firefox to 128.4.0esr
* Android
  + Updated GeckoView to 128.4.0esr
* Build System
  + All Platforms
    - [Bug tor-browser-build#41289](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41289): Fix single-browser in relprep.py
  + Linux
    - [Bug tor-browser-build#41282](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41282): Add SSL to our custom Python for MozBug 1924022

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1401/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1401/&text=Tor%20Browser%2014.0.1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1401/&text=Tor%20Browser%2014.0.1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.0.1%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1401/)

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