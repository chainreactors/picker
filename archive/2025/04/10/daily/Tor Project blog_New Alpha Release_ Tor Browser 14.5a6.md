---
title: New Alpha Release: Tor Browser 14.5a6
url: https://blog.torproject.org/new-alpha-release-tor-browser-145a6/
source: Tor Project blog
date: 2025-04-10
fetch_date: 2025-10-06T22:08:46.414774
---

# New Alpha Release: Tor Browser 14.5a6

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Alpha Release: Tor Browser 14.5a6

by [ma1](/author/ma1)
| April 9, 2025

![](/new-alpha-release-tor-browser-145a6/lead.png)

Tor Browser 14.5a6 is now available from the [Tor Browser download page](https://www.torproject.org/download/alpha/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/14.5a6/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

We would like to thank the folowing community members for their contributions this release:

* cschutijser for their fixup to [tor-browser#43628](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43628)

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 14.5a5](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated Tor to 0.4.9.2-alpha
  + [Bug tor-browser#43322](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43322): Stop blocking all fonts in FontFace
  + [Bug tor-browser#43443](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43443): Drop effective top level domain for `au.securedrop.tor.onion`
  + [Bug tor-browser#43585](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43585): Rebase Tor Browser alpha onto 128.9.0esr
  + [Bug tor-browser#43601](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43601): Backport security fixes from Firefox 137
  + [Bug tor-browser#43628](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43628): Handle unavailability of NetworkLinkService API in Tor Connect
  + [Bug tor-browser-build#41425](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41425): Snowflake needs to be listed separately on torrc-defaults
* Windows + macOS + Linux
  + Updated Firefox to 128.9.0esr
  + [Bug tor-browser#41919](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41919): Add temporarily visible web content-size overlay after resizing window when letterboxing is enabled
  + [Bug tor-browser#43130](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43130): Adjust preferences for contrast theme or forced colors
  + [Bug tor-browser#43531](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43531): Use "label" attribute rather than textContent for the bridge dialog XUL buttons
  + [Bug tor-browser#43563](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43563): TorConnect country/region names should change based on the app language
* Android
  + Updated GeckoView to 128.9.0esr
  + [Bug tor-browser#43464](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43464): TBA Alpha and Nightly cannot be debugged with about:debugging
  + [Bug tor-browser#43565](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43565): The quit button on Android doesn't actually exit
  + [Bug tor-browser#43576](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43576): Connection Assist on Android Polish
  + [Bug tor-browser#43581](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43581): Bookmarks are failing to load on Tor Browser Android Alpha 14.5a5
  + [Bug tor-browser#43593](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43593): Use "region" instead of "country" in connect assist
  + [Bug tor-browser#43604](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43604): TorDomainIsolator routinely clears Android browser circuit data
  + [Bug tor-browser-build#41422](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41422): Patch viaduct in Application Services to always return a backend error
* Build System
  + All Platforms
    - Updated Go to 1.23.8
    - [Bug tor-browser-build#41365](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41365): Indent download\*.json files
    - [Bug tor-browser-build#41406](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41406): Restore -desktop and -android Makefile targets.
    - [Bug tor-browser-build#41407](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41407): Use Lyrebird also for the Snowflake PT
    - [Bug tor-browser-build#41409](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41409): Create a script for quickly setting up protected branches
    - [Bug tor-browser-build#41411](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41411): Update licenses for PTs
    - [Bug tor-browser-build#41417](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41417): Bump the conjure version we ship
    - [Bug tor-browser-build#41419](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41419): Add comment in downloads.json to mention that the file is deprecated, and that download-$platform.json should be used instead
    - [Bug tor-browser-build#41420](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41420): Update the changelog script for label updates
    - [Bug tor-browser-build#41426](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41426): Set the Lyrebird version
    - [Bug rbm#40083](https://gitlab.torproject.org/tpo/applications/rbm/-/issues/40083): rbm creates out/$project directories with mode 0700
  + macOS
    - [Bug tor-browser-build#41403](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41403): The rcodesign step has a wrong dmg name in alpha
  + Android
    - [Bug tor-browser-build#41400](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41400): Add branding localization to GeckoView
    - [Bug tor-browser-build#41410](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41410): Use the Lyrebird name on Android

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-alpha-release-tor-browser-145a6/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-145a6/&text=Tor%20Browser%2014.5a6%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-alpha-release-tor-browser-145a6/&text=Tor%20Browser%2014.5a6%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2014.5a6%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-alpha-release-tor-browser-145a6/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or w...