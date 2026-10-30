---
title: New Release: Tor Browser 16.0
url: https://blog.torproject.org/new-release-tor-browser-160/
source: Tor Project blog
date: 2026-10-29
fetch_date: 2026-10-30T07:56:21.850935
---

# New Release: Tor Browser 16.0

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 16.0

by [duncan](/author/duncan)
| October 29, 2026

![](/new-release-tor-browser-160/lead.png)

Tor Browser 16.0 is now available for [Desktop](https://download.torproject.org/tor-browser-for-desktop/) and [Android](https://download.torproject.org/tor-browser-for-android/). This is our first stable release based on Firefox ESR 153, incorporating a year's worth of changes that have been shipped upstream in Firefox. As part of this process, we've also completed our annual ESR transition audit, where we reviewed and addressed [over 270 Bugzilla](https://gitlab.torproject.org/tpo/applications/tor-browser/-/work_items?sort=updated_desc&state=all&search=Review%20Mozilla&milestone_title=Browser%2016.0&label_name%5B%5D=Apps%3A%3AType%3A%3AAudit&first_page_size=100) issues covering changes in Firefox that could negatively affect the privacy and security of Tor Browser users.

The ongoing development of Tor Browser is made possible thanks to the support of our community. Every donation helps power the tools that let people browse freely and privately. Consider [joining thousands of others who have already made a small contribution](https://torproject.org/donate/donate-bp2-yec2026) towards building a better internet for everyone.

## What's new for Desktop?

![](/new-release-tor-browser-160/160-desktop.png)

### Redesigned Settings

Tor Browser connects millions of people to the Tor network (and by extension, the free and open internet) out of the box. However, for those who need to circumvent advanced censorship, boost their security level, or tailor their browsing experience, clear and easy-to-use Settings are essential. To that end, Tor Browser 16.0 introduces a complete redesign of the Settings experience based on a parallel redesign [shipped in Firefox in June](https://blog.mozilla.org/en/firefox/firefox-settings/). Improvements include a cleaner layout, updated navigation, and clearer labels and descriptions aimed at making settings easier to find, understand, and manage. Other noteworthy changes include:

* The long-standing "General" page has been retired, with its contents distributed across new pages for Appearance, Downloads, Tabs and browsing, Accessibility and Languages.
* Pages and components that are unique to Tor browser like Connection and Security Level have been rebuilt from scratch using Firefox's new components so they look and feel consistent with the rest of Settings.
* Some settings that, if enabled, could compromise your privacy or make your browser [easier to fingerprint](https://support.torproject.org/tor-browser/features/fingerprinting-protections/) have either been hidden or feature clear warnings.

Fear not: your existing preferences will remain saved even if the original setting has moved or changed, and you can use the search bar at the top of Settings to find anything you're struggling to track down.

### Generic window titles

Another new addition to Settings is the option to use generic window titles, which can be found under Privacy and security â Protections from third-party applications. Like most browsers, Tor Browser uses the title of the page you're currently viewing for the names of its windows. However, other applications on your computer or your operating system itself can read these titles without special permissions. When enabled, this option simply replaces all window titles with "Tor Browser" â preventing other software from snooping on your browsing history. As always, for more comprehensive protection from third-party applications on your device, we recommend using [Tails](https://tails.net/).

For now, this option is strictly opt-in, as we did not have sufficient time during this release cycle to properly evaluate potential side-effects for users. In particular, we worry that enabling this setting may reduce the browser's usability for those who rely on accessibility tools (e.g. screen-readers) or those with highly customized systems (e.g. less-popular desktop managers, application switchers, etc). If you are one of these users, we would ask that you try using this setting, and report back any bugs or usability issues you find!

ð£ Generic window titles have also been upstreamed to Firefox as part of the [Tor Uplift Project](https://wiki.mozilla.org/Security/Tor_Uplift). Advanced Firefox users can enable this feature by opening `about:config` and setting `privacy.exposeContentTitleInWindow` (for normal windows) and `privacy.exposeContentTitleInWindow.pbm` (for private browsing windows) to `false`.

### New user manual

The Tor Browser manual, which can be found by visiting `about:manual` or through the application menu (â°) â Help â Tor Browser manual, has also received a complete revamp. Since the [release of our new Support portal in 2025](https://blog.torproject.org/new-user-support-portal-tor-tails/), the team has had to maintain two sets of documentation: one for the traditional manual that's available to read in Tor Browser, and another for the new Support site. With this release, we've solved that problem by replacing the older material in the Tor Browser manual with our latest and greatest help content from the new Support site. Like the previous iteration of the manual, the new version is bundled with Tor Browser for Desktop so it can be read offline, which comes in particularly handy when troubleshooting issues that prevent you from connecting to the Tor network.

### Linux on ARM

Finally, after a year of testing, Tor Browser 16.0 now features native support for Linux computers with 64-bit ARM (AArch64) processors, such as Raspberry Pis and Apple Silicon Macs running Linux. If you have been relying on Tor Browser Alpha for support for these devices, we recommend switching over to the stable release channel unless you plan to continue testing Alpha releases. Meanwhile, Tor Browser 16.0 follows Firefox in ending support for 32-bit x86 Linux computers. Fortunately, very few people should be affected, as we currently receive around 200 update checks from this platform a day, down from a peak of around 4,000 in 2019. Most remaining 32-bit users should be able to switch to the 64-bit version unless they're running outdated hardware or versions of Linux.

## What's new for Android?

![](/new-release-tor-browser-160/160-android.png)

Tor Browser for Android has also benefited from Mozilla's ongoing work to modernize Firefox, as seen in the Settings redesign on desktop. Over the past year, Firefox has been gradually transitioning to Jetpack Compose â Google's newest framework for building native Android interfaces. In this release, we've made significant progress applying the same changes to Tor Browser. As a result, large swaths of Tor Browser's user interface has been updated to Material Design 3 â the latest iteration of Google's design language for Android â with more yet to come in future releases.

Google Play limits the size of apps distributed as APKs to 100 MB. Since Firefox for Android continues to grow with each release, keeping Tor Browser within this limit has been an ongoing challenge â for example, this issue has prevented us from bundling Tor Browser's manual on Android so that it can be accessed offline. Nevertheless, we've found various ways to reduce the size of our Android package over the years and stay within the limit. Most recently, this involved carefully and creatively compressing some of the built-in resources Firefox uses to display its interface.

## What's in the works?

Tor Browser users can expect additional improvements over the next few months as we continue to refine the new Settings experience for desktop and Material Design 3 for Android. If you fi...