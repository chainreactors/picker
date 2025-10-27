---
title: New Alpha Release: Tor Browser 14.0a6
url: https://blog.torproject.org/new-alpha-release-tor-browser-140a6/
source: Tor Project blog
date: 2024-09-22
fetch_date: 2025-10-06T18:27:02.099649
---

# New Alpha Release: Tor Browser 14.0a6

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.0a6

by [morgan](/author/morgan)
| September 21, 2024

![](/new-alpha-release-tor-browser-140a6/lead.png)

Tor Browser 14.0a6 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.0a6/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

We would like to thank the folowing community members for their contributions this release:

* cypherpunks1 for their work on:
  + [tor-browser#41550](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41550)
  + [tor-browser#43052](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43052)
  + [tor-browser#43129](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43129)
  + [tor-browser#43146](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43146)
  + [tor-browser#43147](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43147)

**NOTE**: an earlier version of this post mis-attributed these resolved issues to another volunteer

If you would like to contribute, our contributor guide can be found [here](https://gitlab.torproject.org/tpo/applications/team/-/wikis/Development-Information/Tor-Browser/Contributing-to-Tor-Browser).

## Bugzilla Triage and Review

We have 9 remaining upstream Bugzilla issues to review and potentially develop patches for.

This work can be tracked in [this Gitlab query](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=opened&search=Review%20Mozilla&label_name%5B%5D=14.0%20stable&first_page_size=100).

## Send us your feedback

We are closing in on the end of this release cycle. The release scheduled for next should be our first release-candidate build for 14.0. If you are interested in [becoming an alpha-tester](https://community.torproject.org/user-research/become-tester/), now is the time!

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.0a5](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + [Bug tor-browser#42831](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42831): Remove the shopping components
  + [Bug tor-browser#43144](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43144): Ensure non-privacy browsing also sets the GPC header
* Windows + macOS + Linux
  + [Bug tor-browser#42698](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42698): Bridge card background contrast is low for bridge-moji
  + [Bug tor-browser#42718](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42718): Remove the firefox-view button from UI, even when always-on private-browsing mode is disabled
  + [Bug tor-browser#42740](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42740): Stop trying to hide "Restore previous session"
  + [Bug tor-browser#43072](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43072): moz-message-bar does not get announced on Orca screen-reader
  + [Bug tor-browser#43083](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43083): Backport fix for Mozilla 1436462
* Linux
  + [Bug tor-browser#43141](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43141): Hardcode Arimo as a system-ui font
  + [Bug tor-browser-build#41237](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41237): Add some aliases to our Linux font config for compatibility
* Android
  + [Bug tor-browser#41550](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41550): Remove unused extensions from Tor Browser for Android
  + [Bug tor-browser#43052](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43052): Remove non private tabs icon and "other device tabs" from tab view
  + [Bug tor-browser#43129](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43129): about:neterror cannot display SVG on Android with Security Level Safest
  + [Bug tor-browser#43145](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43145): Backport Android security fix from 130.0.1
  + [Bug tor-browser#43146](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43146): Update the icon of DuckDuckGo onion search engine on Android
  + [Bug tor-browser#43147](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43147): Remove unused search plugins from the apk files

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a6/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a6/&text=Tor%20Browser%2014.0a6%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-140a6/&text=Tor%20Browser%2014.0a6%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.0a6%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-140a6/)

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

Trademark, copyright notices, a...