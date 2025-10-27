---
title: New Release: Tor Browser 14.5
url: https://blog.torproject.org/new-release-tor-browser-145/
source: Tor Project blog
date: 2025-04-17
fetch_date: 2025-10-06T22:09:11.920739
---

# New Release: Tor Browser 14.5

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 14.5

by [duncan](/author/duncan)
| April 16, 2025

![](/new-release-tor-browser-145/lead.png)

Tor Browser 14.5 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and [distribution directory](https://www.torproject.org/dist/torbrowser/14.5/). This release marks the introduction of Connection Assist to Android, empowering mobile users who are subjected to strict censorship to unblock Tor at the press of a button. In addition, the Belarusian, Bulgarian and Portuguese (Portugal) languages are now available across all platforms.

## What's new?

### Connection Assist for Android

Tor aspires to connect as many people to the free and open internet as possible. But what happens if the Tor network itself is blocked in your country, by your ISP, or on your local network? The answer lies in [bridges](https://support.torproject.org/censorship/censorship-7/): a type of relay that's hidden from censors using various techniques we collectively call [Pluggable Transports](https://tb-manual.torproject.org/circumvention/). However, censors may have found and blocked certain bridges already, and what works for one country or network may not work for another. This means that the process to find a working bridge to unblock Tor required some trial and error, and placed an undue burden on users who are subjected to strict censorship.

To simplify this process and help more users connect to Tor, we released Connection Assist for Linux, macOS and Windows in [Tor Browser 11.5](https://blog.torproject.org/new-release-tor-browser-115/). Subsequently, should Tor Browser fail to establish a direct connection to the Tor network, Connection Assist will offer to find and try bridges for you. But before this feature could be made available on Android, we had to embark on a multi-year effort to refactor our tor integration across each platform first. This project has now reached an important milestone, and we're proud to announce the release of Connection Assist for Android today.

![Multiple screenshots of Tor Browser for Android showcasing Connection Assist, which successfully connecting to the Tor network after trying bridges](/new-release-tor-browser-145/145-connection-assist.png)

On a technical level, this means both desktop and Android now benefit from a shared backend (to a degree) and a leaner codebase, thanks to the elimination of a significant amount of legacy and redundant code. On a human level, not only is Connection Assist now available for Android, but Tor Browser users can expect more stable and less error-prone connections in general. In addition, this refactor provides a more robust foundation for future improvements too, such as making the [circuit display](https://support.torproject.org/glossary/circuit/) available on Android, or potentially transitioning to [arti](https://tpo.pages.torproject.net/core/arti/about) in the further future.

### ÐÑÐ¸Ð²ÐµÑ. ÐÐ´ÑÐ°Ð²ÐµÐ¹ÑÐµ. OlÃ¡.

In order for Tor Browser to be accessible to as many people as possible, it needs to speak their languages. Thanks to the hard work and dedication of our volunteers, and the continued support of [Localization Lab](https://www.localizationlab.org/), three additional languages are now available on both desktop and Android: Belarusian, Bulgarian and Portuguese (Portugal). To check these out, follow these steps to change Tor Browser's language:

* On Linux, macOS or Windows, go to â° > Settings > General > Language and Appearance > Language.
* On Android, go to â® > Settings > General > Language.

If you spot an error in these or any other language, you can learn more about how to contribute to the translation of Tor Browser, its documentation and our websites on our [Community portal](https://community.torproject.org/localization/). Becoming a Tor translator is one of the most impactful ways you can help at-risk and censored internet users safely access Tor.

![Multiple screenshots showcasing Tor Browser for Desktop and Android in the Belarusian, Bulgarian and Portuguese languages](/new-release-tor-browser-145/145-locales.png)

### Small but mighty improvements

It's easy to focus on the big features at the expense of smaller things in release posts like these. However, smaller improvements can be just as impactful as the big ticket items, and help contribute towards the long-term usability and stability of Tor Browser. For instance, over the last few months our developers have invested considerable time into fixes like these:

* Following similar improvements to Android in [Tor Browser 13.5](https://blog.torproject.org/new-release-tor-browser-135/), the layout of Tor logs on desktop has been enhanced to aid readability. Logs now "stream" live on desktop too, so that you no longer need to close and reopen the dialog to refresh your logs.
* Various edge-cases in Connection Assist's logic have been ironed out, and Tor Browser now makes fewer calls using [moat](https://support.torproject.org/glossary/moat/) (a type of brief, non-Tor connection that uses [domain fronting](https://support.torproject.org/glossary/domain-fronting/)) when diagnosing connection issues. Tor Browser for Desktop will also deliver warnings when changes to Tor Browser's Connection Settings (like configuring bridges) fail to apply, instead of failing silently, which wasn't good.
* Quitting Tor Browser via the "Quit" menu item on Android now does a more thorough job of ending background processes and clearing recent tasks. Similarly, we've restored an older feature whereby Tor Browser will quit itself and close all tabs in the process if you back out of the app in a hurry â which is handy in a pinch.

These are just a few examples of some of the smaller improvements we've been working on. For a full accounting of all changes, please see the changelog below.

## Known issues

Tor Browser 14.5 comes with a number of known issues that can be found in [Tor Browser's issue tracker](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues).

## Get involved

If you find a bug or have a suggestion for how we could improve this release, [we'd love to hear your feedback](https://support.torproject.org/misc/bug-or-feedback/). If you would like to contribute to a future release, please see [our guide for new contributors](https://gitlab.torproject.org/tpo/applications/team/-/wikis/Development-Information/Tor-Browser/Contributing-to-Tor-Browser) to get started.

### Contributors <3

Thanks to all of the teams across Tor, and the wider community, who contributed to this release. In particular we'd like to extend our gratitude to the following volunteers who have contributed their expertise, labor and time:

* cschutijser
* cypherpunks1
* NoisyCoil
* thorin

## Full changelog

The full changelog since [Tor Browser 14.0.9](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/maint-14.5/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt) is:

* All Platforms
  + [Bug tor-browser#41710](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41710): Refactor about:torconnects relation to TorConnectParent
  + [Bug tor-browser#41921](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41921): Clean up initialisation and bridges conflict between TorSettings and TorConnect
  + [Bug tor-browser#42300](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/42300): Do not store logs inside TorProvider
  + [Bug tor-browser#43308](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43308): Only allow "about:" pages to have access to contentaccessible branding assets
  + [Bug tor-browser#43323](https://gitlab.to...