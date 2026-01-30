---
title: New Release: Tor Browser 15.0.5
url: https://blog.torproject.org/new-release-tor-browser-1505/
source: Tor Project blog
date: 2026-01-29
fetch_date: 2026-01-30T04:04:25.994565
---

# New Release: Tor Browser 15.0.5

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 15.0.5

by [morgan](/author/morgan)
| January 29, 2026

![](/new-release-tor-browser-1505/lead.png)

Tor Browser 15.0.5 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/15.0.5/).

## Vietnamese Text Vandalism

A few days ago, one of our community members reported that some of the Vietnamese text translations in Tor Browser Android had been vandalised by a malicious contributor. Unfortunately, this mis-translated text ended up shipping in Tor Browser 15.0.4. These changes did *not* affect the browser's functionality or security properties in any way.

In addition to shipping an unscheduled release to fix this problem, we are also reviewing the processes around accepting translation updates so that something like this does not again make it into Tor Browser Stable. Our goal is to keep community contributions open and welcome, while adding safeguards where needed.

Finally, we want to thank our community of volunteer translators and in particular user **SweetSea** for reporting this issue to [our localisation developer channel (#tor-l10n)](https://support.torproject.org/get-in-touch/chat-with-us/). If you would like to help improve translations and join the community, please consider [becoming a Tor translator](https://community.torproject.org/localization/becoming-tor-translator/)!

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The [full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-15.0/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) since Tor Browser 15.0.3 is:

* All Platforms
  + [Bug tor-browser#44418](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44418): Update built-in obfs4 bridges
  + [Bug tor-browser#44433](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44433): Weird Â§:domain.com label in the Blocked Objects window
  + [Bug tor-browser#44470](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44470): Rebase Tor Browser stable onto 140.7.0esr
  + [Bug tor-browser#44474](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44474): Backport Security Fixes from Firefox 147
  + [Bug tor-browser#44482](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/44482): (H1) Script execution in Safest mode via data URI navigation
* Windows + macOS + Linux
  + Updated Firefox to 140.7.0esr
* Android
  + Updated GeckoView to 140.7.0esr
  + [Bug tor-browser-build#41681](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41681): Keep public suffixes up-to-date on 140esr-based Tor Browser for Android
* Build System
  + All Platforms
    - [Bug tor-browser-build#41654](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41654): Make relprep.py update Moat settings
    - [Bug tor-browser-build#41682](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41682): relprep.py should fail when a GitHub release is not found
    - [Bug rbm#40090](https://gitlab.torproject.org/tpo/applications/rbm/-/issues/40090): Make the cleanup faster
    - [Bug rbm#40095](https://gitlab.torproject.org/tpo/applications/rbm/-/issues/40095): cached checksums should not be used for input files when refresh\_input is enabled
  + Android
    - [Bug tor-browser-build#41679](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41679): Android tor-expert-bundle archives missing version in filename

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1505/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1505/&text=Tor%20Browser%2015.0.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1505/&text=Tor%20Browser%2015.0.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2015.0.5%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1505/)

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

January 31, 2026 – February 1, 2026

## [FOSDEM'26 (Brussels)](/event/fosdem-2026/)

## Recent Updates

## [New Release: Tor Browser 15.0.5](/new-release-tor-browser-1505/)

by [morgan](/author/morgan)
| January 29, 2026

Tor Browser 15.0.5 is now available from the Tor Browser download page and also from our distribution directory.

## [New Release: Tails 7.4](/new-release-tails-7_4/)

by [tails](/author/tails)
| January 15, 2026

Tails 7.4 is now available.

## [New Release: Tor Browser 15.0.4](/new-release-tor-browser-1504/)

by [ma1](/author/ma1)
| January 13, 2026

Tor Browser 15.0.4 is now available from the Tor Browser download page and also from our distribution directory.

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