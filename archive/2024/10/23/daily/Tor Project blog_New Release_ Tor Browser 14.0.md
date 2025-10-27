---
title: New Release: Tor Browser 14.0
url: https://blog.torproject.org/new-release-tor-browser-140/
source: Tor Project blog
date: 2024-10-23
fetch_date: 2025-10-06T18:55:32.939425
---

# New Release: Tor Browser 14.0

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 14.0

by [duncan](/author/duncan)
| October 22, 2024

![](/new-release-tor-browser-140/lead.png)

Tor Browser 14.0 is now available from the Tor Browser [download page](https://www.torproject.org/download/) and our [distribution directory](https://dist.torproject.org/torbrowser/14.0/). This is our first stable release based on [Firefox ESR 128](https://www.mozilla.org/en-US/firefox/128.0esr/releasenotes/), incorporating a year's worth of changes shipped upstream in Firefox. As part of this process we've also completed our annual ESR transition audit, where we [reviewed and addressed over 200 Bugzilla issues](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=all&search=Review%20Mozilla&label_name%5B%5D=14.0%20stable&first_page_size=20) for changes in Firefox that may negatively affect the privacy and security of Tor Browser users. Our final reports from this audit are now available in the [tor-browser-spec repository](https://gitlab.torproject.org/tpo/applications/tor-browser-spec/-/tree/main/audits) on our Gitlab instance.

Firefox's design also continues to evolve, and the ESR transition is our opportunity to update Tor Browser to reflect the most recent patterns and styles used in Firefox. For example, eagle-eyed Tor Browser users will notice updates to Tor Browser's typography that we've inherited from Firefox, including heavier headings and changes to line heights intended to improve font compatibility and accessibility.

In addition to the ESR, we overcame many other technical challenges that you can read more about in Morgan's series of blog posts chronicling the team's progress with Tor Browser Alpha, including: [unifying Tor Browser for Android's codebase into a monorepo](https://blog.torproject.org/new-alpha-release-tor-browser-140a2/), [addressing reproducibility issues in our Android APK generation](https://blog.torproject.org/new-alpha-release-tor-browser-140a2/), [reducing Android's APK size for x86 and x86\_64 platforms](https://blog.torproject.org/new-alpha-release-tor-browser-140a3/), and [changes to how we spoof Tor Browser's user agent](https://blog.torproject.org/new-alpha-release-tor-browser-140a4/), to name a few. This release also includes a series of improvements to the usability and compatibility of our fingerprinting protections without compromising their effectiveness, allowing us to enable useful features like picture-in-picture, screenshots and more.

The ongoing development of Tor Browser is made possible thanks to the support of our community. If Tor Browser is important to you, now is a [great time to support our mission](https://donate.torproject.org), as [all donations will be matched](https://blog.torproject.org/2024-fundraiser-donations-matched/) through the end of the year.

## What's new?

### New circuit for Android

In previous versions of Tor Browser for Android, users could request a "New identity" by interacting with a persistent notification that appeared while Tor Browser was running. However this was unusual for a couple of reasons â firstly, no such feature was available in the app's user interface itself, and it could only be enabled outside the app via Android's notification drawer. Secondly, this feature did not perform the same steps as Tor Browser for desktop to reset your identity, such as closing all tabs, clearing all cookies and wiping your browsing history. In actuality, it functioned more like a "refresh all circuits" button.

We've since learned that most Android users were relying on this feature as workaround to request a new circuit for a broken website, rather than reset their identity as such. So when this notification inadvertently disappeared in Tor Browser 13.5, we didn't rush to bring it back in its original state. Instead, we chose to focus our efforts on porting the desktop feature "New circuit for this site" to Android, allowing our mobile users to request a new circuit in a more targeted fashion.

![A screenshot of Tor Browser for Android with the overflow menu open, featuring an arrow pointing to a new entry in the menu reading "New circuit"](/new-release-tor-browser-140/140-new-circuit.png)

### Extended support for legacy platforms

With the release of Tor Browser 13.5, we began warning users of Windows 7, 8 and 8.1 and macOS 10.12, 10.13 and 10.14 that this would be the last major release to support their platforms. In short, that situation has now changed, and users of these legacy platforms will continue to receive critical security updates updates on a temporary basis until at least March 2025.

Microsoft ended support for Windows 7, 8 and 8.1 in January of 2023, and Apple typically provides support for the previous three versions of macOS. In turn, Mozilla moved support for these versions to the Extended Support Release (ESR) of Firefox last year, and ESR 115 will be the final version of Firefox to support these platforms. However, Mozilla have since announced that ESR 115 will continue to receive critical security updates until at least March 2025, with the intention to re-evaluate the situation at the beginning of the year.

So how does this affect Tor Browser users? That's where it gets a little complicated: Tor Browser 13 is currently based on Firefox ESR 115, whereas Tor Browser 14 is based on ESR 128 â which doesn't support these legacy platforms. This means that the Tor Browser user base will be split across two update paths:

* Users of Windows 10 or later and macOS 10.15 or later will be updated to Tor Browser 14.0.
* User of Windows 7, 8 and 8.1 and macOS 10.12, 10.13 and 10.14 will remain on Tor Browser 13.5.

In turn, the Tor Project will continue to release new versions of Tor Browser 13.5 whenever critical security updates are made available for Firefox ESR 115. Ultimately, this support is only temporary, and is dependent on Mozilla's timetable. Therefore we strongly recommend users of legacy Windows and macOS platforms upgrade their operating systems in order to update to Tor Browser 14.0 before the extended support window ends. Keeping Tor Browser up to date is critical to protect your privacy, security and anonymity online.

![A graphic demonstrating the split in Tor Browser for Desktop's update path, whereby users of Windows 7, 8 and 8.1 and macOS 10.12, 10.13 and 10.14 will remain on Tor Browser 13.5, whereas users of newer platforms will receive the 14.0 update](/new-release-tor-browser-140/140-legacy-support.png)

## Known issues

Tor Browser 14.0 comes with a number of known issues that are searchable on [Tor Browser's Gitlab project](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues). In particular, Windows and Android users should be aware of the following:

### Android

We are currently working on a fix for an issue with [Guardian Project's F-Droid repo](https://guardianproject.info/fdroid/) that's been preventing F-Droid users from updating since Tor Browser 13.5.3's release. Until this issue is resolved, Android users who have installed Tor Browser via Guardian Project's F-Droid repo will not receive the 14.0 update. Google Play is unaffected by this issue, and Tor Browser 14.0 can be [downloaded from there](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) in the interim. Alternatively, affected users may download and install the APK for Tor Browser 14.0 directly from our [download page](https://www.torproject.org/download/), however please note that APKs do not update automatically. For more details, see [tor-browser#43208](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/43208).

### Windows

Running Tor Browser in compatibility mode ...