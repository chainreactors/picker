---
title: New Release: Tor Browser 15.0
url: https://blog.torproject.org/new-release-tor-browser-150/
source: Tor Project blog
date: 2025-10-28
fetch_date: 2025-10-29T03:16:28.773762
---

# New Release: Tor Browser 15.0

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# New Release: Tor Browser 15.0

by [duncan](/author/duncan)
| October 28, 2025

![](/new-release-tor-browser-150/lead.png)

Tor Browser 15.0 is now available from the [Tor Browser download page](https://www.torproject.org/download/) and [distribution directory](https://www.torproject.org/dist/torbrowser/15.0/). This is our first stable release based on [Firefox ESR 140](https://www.firefox.com/en-US/firefox/140.0esr/releasenotes/), incorporating a year's worth of changes that have been shipped upstream in Firefox. As part of this process, we've also completed our annual ESR transition audit, where we [reviewed and addressed around 200 Bugzilla issues](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/?sort=updated_desc&state=all&label_name%5B%5D=esr-140&search=Review%20Mozilla&first_page_size=20) for changes in Firefox that may negatively affect the privacy and security of Tor Browser users. Our final reports from this audit are now available in the [tor-browser-spec repository](https://gitlab.torproject.org/tpo/applications/tor-browser-spec/-/tree/main/audits) on our GitLab instance.

The ongoing development of Tor Browser is made possible thanks to the support of our community. If Tor Browser is important to you, now is a great time to support our mission to **FREE THE INTERNET**, as all donations will be matched by [Power Up Privacy](https://powerupprivacy.com/) through December 31, 2025.

[![Donate button](/new-release-tor-browser-150/button-donate-yec25.png)](https://torproject.org/donate/donate-bp2-yec2025)

## What's new?

### Desktop

Tor Browser 15.0 inherits a multitude of useful new features and usability improvements from Firefox that have passed our audit. For desktop, these include vertical tabs: providing a more manageable, alternative layout with open and pinned tabs stacked in a sidebar rather than across the top of the window. For ease of access, Bookmarks can be retrieved directly from the sidebar when expanded too. However, regardless of whether you prefer horizontal or vertical tabs, everyone benefits from the addition of tab groups: helping you keep on top of the clutter by organizing tabs into collapsible groups that can be given names and color-coded. Tor Browser 15.0 also inherits elements of Firefox's recent address bar refresh, including a new unified search button that allows you to switch search engines on the fly, search bookmarks or tabs, and reference quick actions from the same menu.

Note that Tor Browser tabs are still private tabs, and will clear when you close the browser. This enforces a kind of natural tidiness in Tor Browser since each new session starts fresh â however for privacy-conscious power users, project managers, researchers, or anyone else who accumulates tabs frighteningly quickly, we hope these organizational improvements will give you a much needed productivity boost.

![A screenshot featuring Tor Browser for Desktop with vertical tabs enabled and three tab groups present in the resulting sidebar](/new-release-tor-browser-150/150-desktop.png)

### Android

On Android, screen lock adds an extra layer of security to your browsing sessions. After enabling screen lock in Settings > Tabs, your tabs will lock automatically when you switch away from the browser without closing it. Upon returning to the app, you'll be prompted to unlock your tabs using your fingerprint, face, or pass code, depending on which option your device is configured to use.

Like Tor Browser for Desktop, your browsing session will still be cleared when Tor Browser is closed. However, this feature provides peace of mind in a specific scenario: by ensuring that your browsing remains private even if someone has gained temporary access to your unlocked phone with Tor Browser open in the background â whether you've handed it to a friend, or left your device sitting on a table.

![A screenshot demonstrating screen lock for Tor Browser on an Android phone, followed by a second screenshot of a passcode being entered](/new-release-tor-browser-150/150-android.png)

## What's changing?

### Updates to Android and Linux device compatibility

At present, Firefox 140 and Tor Browser 15.0 support Android 5.0 or later, which was released almost 11 years ago. While Mozilla's commitment to support such an old version of Android is admirable, it introduces several technical and security challenges for developers. As a consequence, Firefox have announced their intention to increase the minimum support requirements to Android 8.0, and have also decided to drop support for x86 CPUs for [Android](https://blog.mozilla.org/futurereleases/2025/09/15/raising-the-minimum-android-version-for-firefox/) and [Linux](https://support.mozilla.org/en-US/kb/firefox-has-ended-support-32-bit-linux). Sadly, it's not possible for the Tor Project to maintain support for these platforms on our own without official support from Mozilla.

While these changes won't impact Tor Browser users immediately, we expect them to take effect with the release of Tor Browser 16.0 mid-next year. This means that Tor Browser 15.0 will be the last major release to support x86 for Linux and Android, in addition to Android 5.0, 6.0, and 7.0. However, we will continue to release minor updates with security fixes for these platforms until Tor Browser 16.0's eventual release.

Although nobody wants to see support for their platform get dropped, it's an important step to maintain the stability and security of both Firefox and Tor Browser over time, and will allow developers to utilize newer technologies in both browsers. In addition, supporting x86 for Android has been particularly challenging for our developers due to the 100MB package size limit imposed by Google Play. While we have deployed several workarounds to stay within this limit in the recent past, these often come at a cost â such as x86 Android users missing out on the Conjure pluggable transport, for example.

### Disabling of WebAssembly now managed by NoScript

WebAssembly (or Wasm) is a web technology that helps websites and web apps run faster. It allows web developers to write programs in languages like C, C++ or Rust, and compiles these into a special format that web browsers can run more efficiently.

As has been suggested in [this meta-analysis from 2024](https://arxiv.org/html/2407.12297v1), further investigation of Wasm's potential exploits is necessary â therefore Wasm is currently disabled in the Safer and Safest security levels in order to reduce Tor Browser's attack surface. Up until now, this was achieved by setting the global preference `javascript.options.wasm` to false â however this approach was no longer viable after Mozilla implemented part of their PDF reader in Wasm between versions 128 and 140. Consequently, we have decided to move control of Wasm to NoScript, which is bundled with Tor Browser, and already manages JavaScript and other security features. This means that Wasm now works on privileged browser pages such as the PDF renderer, but NoScript will continue blocking the technology on regular websites at the Safer and Safest security levels.

Users who have manually set `javascript.options.wasm` to "false" while in the Standard security level will see their security level represented as "Custom" instead. To mitigate any issues that may arise with the browser's PDF reader, we encourage those users to switch the preference back to "true", thereby passing management of Wasm over to NoScript. Furthermore, manually disabling Wasm at the Standard security level (either via NoScript or `javascript.options/wasm`) may also [make your fingerprint more unique](https://tb-manual.torproject.org/anti-fingerprinting...