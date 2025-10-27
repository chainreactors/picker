---
title: Firefox Security Response to pwn2own 2025
url: https://blog.mozilla.org/security/2025/05/17/firefox-security-response-to-pwn2own-2025/
source: Mozilla Security Blog
date: 2025-05-18
fetch_date: 2025-10-06T22:27:14.154345
---

# Firefox Security Response to pwn2own 2025

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
[Announcements](https://blog.mozilla.org/security/category/announcements/) [Firefox](https://blog.mozilla.org/security/category/firefox/) [Security](https://blog.mozilla.org/security/category/security/) [Security Updates](https://blog.mozilla.org/security/category/security-updates/)

# Firefox Security Response to pwn2own 2025

Frederik Braun
May 17, 2025

At Mozilla, we consider security to be a paramount aspect of the web. This is why not only does Firefox have a long running bug bounty program but also mature release management and security engineering practices. These practices combined with well-trained and talented Firefox teams are also the reason why we respond to security bugs as quickly as we do. This week at the security hacking competition pwn2own, security researchers demonstrated two new content-process exploits against Firefox. Neither of the attacks managed to break out of our sandbox, which is required to gain control over the user’s system.

Out of abundance of caution, **we just released new Firefox versions in response to these attacks** – all within the same day of the second exploit announcement. The updated versions are Firefox 138.0.4, Firefox ESR 128.10.1, Firefox ESR 115.23.1 and Firefox for Android. Despite the limited impact of these attacks, all users and administrators are advised to update Firefox as soon as possible.

Just last year at the same security event, we [responded to an exploitable security bug within 21 hours](https://blog.mozilla.org/security/2024/04/04/rapidly-leveling-up-firefox-security/), for which we earned an [award as the fastest to patch](https://www.zerodayinitiative.com/blog/2024/8/1/introducing-the-vanguard-awards). But this year was special. This year, two security researchers signed up to attack Firefox at pwn2own. We continued the same rapid security response this year too.

# Background

[Pwn2Own](https://en.wikipedia.org/wiki/Pwn2Own) is an annual computer hacking contest where participants aim to find security vulnerabilities in major software such as browsers. This year, the event was held in Berlin, Germany, and a lot of [popular software was listed as potential targets for security research](https://www.zerodayinitiative.com/blog/2025/2/24/announcing-pwn2own-berlin-2025). As part of the event preparation, we were informed that Firefox was also listed as a target. But it took until the day before the event when we learned that not just one but **two groups signed up** to demonstrate their work.

Typically, people attacking a browser require a multi-step exploit. At first, they need to compromise the web browser tab to gain limited control of the user’s system. But due to Firefox’s robust security architecture, another bug (a sandbox escape) is required to break out of the current tab and gain wider system access. Unlike prior years, neither participating group was able to escape our sandbox this year. We have verbal confirmation that this is attributed to the [recent architectural improvements](https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html) to our Firefox sandbox which have neutered a wide range of such attacks. This continues to build confidence in Firefox’s strong security posture.

To review and fix the reported exploits a diverse team of people from all across the world and in various roles (engineering, QA, release management, security and many more) rushed to work. We tested and released a new version of Firefox for all of our supported platforms, operating systems, and configurations with rapid speed.

Our work does not end here. We continue to use opportunities like this to improve our incident response. We will also continue to study the reports to identify new hardening features and security improvements to keep all of our Firefox users across the globe protected.

### Related Resources

If you’re interested in learning more about Mozilla’s security initiatives or Firefox security, here are some resources to help you get started:

[Mozilla Security](https://www.mozilla.org/en-US/security/)[Mozilla Security Blog](https://blog.mozilla.org/security/)[Bug Bounty Program](https://www.mozilla.org/en-US/security/bug-bounty/)

Furthermore, if you want to kickstart your own security research in Firefox, we invite you to follow our deeply technical blog at [Attack & Defense – Firefox Security Internals for Engineers, Researchers, and Bounty Hunters](https://attackanddefense.dev/) .

## Update – August 7th, 2025

We are pleased to share that Mozilla was awarded the Vanguard “Speedrunner” Award by the Zero Day Initiative (ZDI). This is in regonition to being consistently fast throghout the last 20 years of Zero Day Initiative’s pwn2own events.

[![Photo of the trophy. It looks like a big V-letter shaped wooden block, on top of a metal foot. The left side of the V says  Vanguards Awards 2025 and the right side says Speedrunner. There is also text indicating this was awarded by the Trend Micro Zero Day Initiative (ZDI)](https://blog.mozilla.org/security/files/2025/05/img_0215-600x800.jpg)](https://blog.mozilla.org/security/files/2025/05/img_0215-scaled.jpg)

“Speedrunner” trophy, awarded to Mozilla Firefox for an outstanding security response during pwn2own.

#### Browse fast. Browse free.

[Download Firefox](https://www.mozilla.org/firefox/new/?utm_source=blog.mozilla.org&utm_campaign=firefox_frontier&utm_medium=referral)

[Previous article
**Updated GPG key for signing Firefox Releases**
April 1, 2025](https://blog.mozilla.org/security/2025/04/01/updated-gpg-key-for-signing-firefox-releases-2/)

#### More articles in “Announcements”

* ##### [Enhancing CA Practices: Key Updates in Mozilla Root Store Policy, v3.0](https://blog.mozilla.org/security/2025/03/12/enhancing-ca-practices-key-updates-in-mozilla-root-store-policy-v3-0/)

  March 12, 2025
* ##### [Firefox will upgrade more Mixed Content in Version 127](https://blog.mozilla.org/security/2024/06/05/firefox-will-upgrade-more-mixed-content-in-version-127/)

  June 5, 2024
* ##### [Mozilla VPN Security Audit 2023](https://blog.mozilla.org/security/2023/12/06/mozilla-vpn-security-audit-2023/)

  December 6, 2023
* ##### [Firefox 90 supports Fetch Metadata Request Headers](https://blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/)

  July 12, 2021
* ##### [Updating GPG key for signing Firefox Releases](https://blog.mozilla.org/security/2021/06/02/updating-gpg-key-for-signing-firefox-releases/)

  June 2, 2021

#### Recent articles

* ##### [Updated GPG key for signing Firefox Releases](https://blog.mozilla.org/security/2025/04/01/updated-gpg-key-for-signing-firefox-releases-2/)

  April 1, 2025
* ##### [Enhancing CA Practices: Key Updates in Mozilla Root Store Policy, v3.0](https://blog.mozilla.org/security/2025/03/12/enhancing-ca-practices-key-updates-in-mozilla-root-store-policy-v3-0/)

  March 12, 2025
* ##### [Behind the Scenes: Fixing an In-the-Wild Firefox Exploit](https://blog.mozilla.org/security/2024/10/11/behind-the-scenes-fixing-an-in-the-wild-firefox-exploit/)

  October 11, 2024
* ##### [Firefox will upgrade more Mixed Content in Version 127](https://bl...