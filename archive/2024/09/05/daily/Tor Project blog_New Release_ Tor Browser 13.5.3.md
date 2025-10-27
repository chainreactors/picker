---
title: New Release: Tor Browser 13.5.3
url: https://blog.torproject.org/new-release-tor-browser-1353/
source: Tor Project blog
date: 2024-09-05
fetch_date: 2025-10-06T18:30:28.621734
---

# New Release: Tor Browser 13.5.3

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 13.5.3

by [morgan](/author/morgan)
| September 4, 2024

![](/new-release-tor-browser-1353/lead.png)

Tor Browser 13.5.3 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and also from our [distribution directory](https://www.torproject.org/dist/torbrowser/13.5.3/).

This version includes important [security updates](https://www.mozilla.org/en-US/security/advisories/) to Firefox.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, [please let us know](https://support.torproject.org/misc/bug-or-feedback/).

## Full changelog

The full changelog since [Tor Browser 13.5.2](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-13.5/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + Updated NoScript to 11.4.35
  + [Bug tor-browser#40056](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40056): Ensure that the lazy loading attribute is ignored on script-disabled documents
  + [Bug tor-browser#42686](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42686): Backport Mozilla 1885101
  + [Bug tor-browser#42829](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42829): Prevent CSS-based scriptless interaction tracking
  + [Bug tor-browser#43084](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43084): Rebase Tor Browser Stable onto 115.15.0esr
  + [Bug tor-browser#43100](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43100): Backport security fixes from Firefox 130
  + [Bug tor-browser-build#41207](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41207): Upgrade lyrebird to 0.3.0
* Windows + macOS + Linux
  + Updated Firefox to 115.15.0esr
  + [Bug tor-browser#42596](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42596): Several console errors: Console.maxLogLevelPref used with a non-existing pref:
  + [Bug tor-browser#42622](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42622): Offline state is unreachable in about:torconnect (first bootstrap attempt)
  + [Bug tor-browser#42642](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42642): Downloads button warning no longer announced on Orca
  + [Bug tor-browser#42661](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42661): Re-run update\_emojis.py and update locales
  + [Bug tor-browser#42691](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42691): Simplified bridge cards prevent censored users from modifying built-in bridges
  + [Bug tor-browser#42696](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42696): Update `mail` icon used in "Find more bridges"
  + [Bug tor-browser#42697](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42697): Remove padding to left of `tor-bridges-provider-list` under "Find more bridges"
  + [Bug tor-browser#43059](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43059): Drag and Drop issue in new update 13.5.2
  + [Bug tor-browser#43066](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43066): about:torconnect no longer changes the title icon on errors
* Linux
  + [Bug tor-browser#43064](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43064): Make copy/paste and drag/drop file filtering more specific
* Android
  + Updated GeckoView to 115.15.0esr
* Build System
  + All Platforms
    - Updated Go to 1.21.13
    - [Bug tor-browser-build#41213](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41213): Update the update\_manual.py script to notify when no changes needed
    - [Bug tor-browser-build#41218](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41218): Use new Tor Browser gpg subkey for signing stable releases
    - [Bug tor-browser-build#41222](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41222): link\_old\_mar\_filenames still referenced in torbrowser-incrementals-{release,alpha}-unsigned
  + Android
    - [Bug tor-browser-build#41206](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/issues/41206): GeckoView ignores the number of processors

* [applications](/category/applications)
* [releases](/category/releases)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/new-release-tor-browser-1353/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/new-release-tor-browser-1353/&text=Tor%20Browser%2013.5.3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/new-release-tor-browser-1353/&text=Tor%20Browser%2013.5.3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.)
[Bluesky](https://bsky.app/intent/compose?text=Tor%20Browser%2013.5.3%20is%20now%20available%20from%20the%20Tor%20Browser%20download%20page%20and%20also%20from%20our%20distribution%20directory.%0Ahttps%3A//blog.torproject.org/new-release-tor-browser-1353/)

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