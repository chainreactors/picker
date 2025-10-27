---
title: New Release: Tor Browser 13.5.8 (Android only)
url: https://blog.torproject.org/new-release-tor-browser-1358/
source: Tor Project blog
date: 2024-10-15
fetch_date: 2025-10-06T18:54:53.531780
---

# New Release: Tor Browser 13.5.8 (Android only)

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 13.5.8 (Android only)

by [morgan](/author/morgan)
| October 14, 2024

![](/new-release-tor-browser-1358/lead.png)

Tor Browser 13.5.8 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/13.5.8/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

This is an unplanned release which backports the remaining Android-specific security fixes from Firefox 131 to Tor Browser 13.5. This is due to a release-process failure on our part during the 13.5.7 release.

## How did this happen?

The fundamental issue that led to us missing patches in the previous release is that we have two different ways of prepping Android releases, and we forgot a step.

To elaborate, Tor Browser 13.5 is based of Firefox 115. This version of Firefox uses a separate source-code repository for the Android-specific functionality. Tor Browser 14.0 is based off of Firefox 128 which has integrated Android and Desktop source-code into a single repository. So, to prep a 13.5 release we have to update two source-code tags, while in 14.0 we only have to update only one.

Since we have been mostly prepping 14.0 alpha-channel releases in recent weeks, this extra tag update was overlooked and these Android-specific updates never made it into the final release.

The good news is that this particular error won't happen again as we will not need to release any more Tor Browser 13.5 for Android after this because Tor Browser 14.0 will stabilise soon.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).
<https://www.mozilla.org/en-US/firefox/131.0.3/releasenotes/>

## Full changelog

The full changelog since [Tor Browser 13.5.7](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-13.5/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* Android
  + Updated NoScript to 11.4.42
  + [Bug tor-browser#43099](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43099): YEC 2024 Takeover for Android Stable
  + [Bug tor-browser#43173](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43173): Backport security fixes from Firefox 131

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1358/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1358/&text=Tor%20Browser%2013.5.8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1358/&text=Tor%20Browser%2013.5.8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2013.5.8%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1358/)

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