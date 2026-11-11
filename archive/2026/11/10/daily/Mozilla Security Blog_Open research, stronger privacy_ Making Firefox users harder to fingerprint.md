---
title: Open research, stronger privacy: Making Firefox users harder to fingerprint
url: https://blog.mozilla.org/security/2026/11/10/open-research-stronger-privacy-making-firefox-users-harder-to-fingerprint/
source: Mozilla Security Blog
date: 2026-11-10
fetch_date: 2026-11-11T08:34:08.274622
---

# Open research, stronger privacy: Making Firefox users harder to fingerprint

[Mozilla](https://www.mozilla.org/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav "Visit mozilla.org")

Menu

* [About Mozilla](https://www.mozilla.org/about/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Products](https://www.mozilla.org/firefox/products/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Give](https://donate.mozilla.org/?presets=50,30,20,10&amount=30&currency=usd&utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Discover Firefox](https://www.mozilla.org/firefox/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)

[#### Mozilla Security Blog](https://blog.mozilla.org/security/ "Go to the front page")

* Search this site

  Search

**Categories:**
[Privacy](https://blog.mozilla.org/security/category/privacy/)

# Open research, stronger privacy: Making Firefox users harder to fingerprint

Tom Ritter, Frederik Braun and Christoph Kerschbaumer
November 10, 2026

Firefox is strengthening protection against trackers that recognize you across websites, even when they don’t use cookies. The latest fingerprinting protections shipped in Firefox reduce the extractable distinguishing details, making more Firefox users look alike to tracking scripts and strengthening individuals’ privacy in everyday browsing.

These protections build on our research into browser and device fingerprinting, a technique that combines details about your browser and device to identify you across websites. We investigated which details contribute most to make users uniquely identifiable, turned those findings into practical protections for Firefox users, and shared our results openly so the wider web security and privacy community can build stronger defenses.

Our findings are documented in the research paper [*Large-Scale Measurement and Real-World Mitigation of Web Browser Fingerprinting in the Wild*,](https://research.mozilla.org/files/2026/11/large-Scale_measurement_and_real-world_mitigation_of_web_browser_fingerprinting_in_the_wild_extended_version.pdf) which has been accepted for publication at [Computer and Communications Security (CCS) 2026](https://www.sigsac.org/ccs/CCS2026/), a leading international conference on computer security and privacy. We’ve also created an easier-to-digest website [and browser test suite](https://fingerprinting.study/) to help explore the findings in the paper.

## **Cookie-less Tracking**

Browser fingerprinting combines details about your browser and device, such as available fonts, screen dimensions, and graphics hardware, to build a uniquely recognizable profile. Each piece may seem ordinary, but together, they can enable trackers to single you out across websites, even without storing a cookie.

Effective fingerprinting protection starts with understanding which browser details trackers rely on most. Our research found that protecting just a handful of browser features can significantly weaken popular fingerprinting techniques. That finding enabled us to focus on Firefox’s protections where they can make the biggest difference and bring those benefits to all Firefox users.

To evaluate these techniques, we simulated the browser measurements collected by fingerprinting scripts from Fingerprint Pro, Signifyd, and Akamai and examined how their combinations distinguish users. The study used measurements collected from nearly 25 million Firefox users, with additional privacy safeguards beyond Mozilla’s existing [data collection policies](https://docs.telemetry.mozilla.org/).

Those safeguards included [OHTTP](https://support.mozilla.org/en-US/kb/ohttp-explained), which routed encrypted requests through a relay. The relay sees the user’s IP address but not the request contents, while Mozilla receives the contents without the user’s IP address. We also tightly limited data access and retention: individual telemetry records were deleted several months ago and only aggregate results were retained and published for open science. Our research paper explains the method, safeguards and ethical considerations in detail.

## **Less distinctive, more private**

Our approach reduces unnecessary differences in the information Firefox exposes to websites. For example, Firefox limits the information exposed through screen resolution APIs to hide the size and position of the system taskbar or dock, preventing that desktop layout detail from contributing to a fingerprint. As another example, it can report processor counts as either 4 or 8 instead of exposing the exact count, which can make a browser more distinctive.

Our goal is to make more users’ browsers look similar to fingerprinting scripts while preserving the information websites need to function correctly, like language and timezone settings. Firefox also uses randomization to make other fingerprinting signals less useful to trackers, though the benefits of these techniques are harder to quantify and fall outside the measurements reported here.

In our evaluation, these protections (the most recent of which shipped in [Firefox 145](https://blog.mozilla.org/en/firefox/fingerprinting-protections/)) substantially degraded the precision of fingerprinting in Firefox both by reducing the number of users with unique fingerprints and increasing the size of the groups of users that share a fingerprint.

The research also enabled us to identify why certain measurements differed between users. Addressing these differences produced more consistent outputs for [image rendering](https://bugzilla.mozilla.org/show_bug.cgi?id=2046791), [Web Audio](https://bugzilla.mozilla.org/show_bug.cgi?id=2036977), and [mathematical operations on Android](https://bugzilla.mozilla.org/show_bug.cgi?id=2037094), reducing the distinguishing details available to fingerprinters.

These results show that substantial reductions in browser fingerprint uniqueness are achievable and provide meaningful progress toward stronger online privacy. These do not make fingerprinting impossible as trackers can surely adapt. But our research provides a concrete, measurable improvement in browser defenses against online tracking.

The built-in privacy protections in Firefox are complemented with capabilities and options to further strengthen the protection against online fingerprinters. Built-in and always-on [Total Cookie Protection](https://www.firefox.com/en-US/features/total-cookie-protection/) in Firefox segments stateful identifiers and prevents trackers from following you across your browsing using cookies. [Firefox Relay](https://relay.firefox.com/) provides you with unique email masks, preventing websites from linking your subscriptions to other sites via data brokers. And [Firefox now integrates a free VPN](https://www.firefox.com/en-US/features/browser-with-built-in-vpn-secure-browsing/) that masks your IP address to protect against tracking and fingerprinting. Together with Firefox’s enhanced fingerprinting protections, these capabilities provide everyone a very strong foundation to take back control of their privacy online.

## **Research that improves everyday browsing**

[Privacy protections need to work on the websites people use every day.](https://blog.mozilla.org/en/firefox/privacy-security/mozilla-anti-tracking-milestones-timeline/) These findings allow us to prioritize changes that deliver measurable privacy benefits while keeping those websites working.

Some of Firefox’s fingerprinting protections, such as hiding the size of your taskbar or dock, are on by default in all browsing modes. Others are introduced first in [Private Browsing](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history) and [Strict Enhanced Tracking Protection (ETP) mode](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop), while we work toward enabling them by default, following the [same strategy](https://blog.mozilla.org/en/mozilla/firefox-rolls-out-total-cookie-protectio...