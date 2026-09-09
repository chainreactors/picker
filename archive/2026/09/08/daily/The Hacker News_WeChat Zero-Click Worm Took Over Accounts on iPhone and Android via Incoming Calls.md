---
title: WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls
url: https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html
source: The Hacker News
date: 2026-09-08
fetch_date: 2026-09-09T06:56:58.589406
---

# WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)

**Swati Khandelwal**Sep 08, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMjSG5iYgxvsWLWeFe2E-z5UDx0S4Q6zBQjkFEiKuFxcfplz39pE90jWcuiV7NcYqT6t2l8j5WWVBHdV-upHuzQVoy-pt4nL4WP7l-Uz_9AYFqOw1Pn0yI8LzM6OThlXJZY8_b4RVK0WzZYIsjWL96-2O-HHY1SH2FCtrE5c6nV0QJ0aU1X8FVlIvOs3g/s1700-nu-rw-lo-l85-e365/wechat.jpg)

Researchers at the security firm **Calif** have built a worm that takes over a WeChat account via an incoming call and [demonstrated it spreading](https://calif.io/research/weworm) among three test phones.

The person being called does not have to answer or touch their phone for it to work, but the caller must already be one of their WeChat contacts. Calif reported the flaw to Tencent in July and says the company has since blocked the exploit for all users.

No attacks using the flaw have been reported, and Calif does not say there were any. Attacks that require no action from the target, known as zero-click attacks, are not new. Last year, WhatsApp [patched a flaw](https://thehackernews.com/2025/08/whatsapp-issues-emergency-update-for.html) it said may have been used in targeted attacks.

Answering the call does not stop the attack. Calif said a person who picks up hears nothing and the exploit still works. Declining the call ends that attempt, but the attacker can call again later, for example while the target is asleep.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The caller has to be on the target's WeChat contact list. Calif said that is not much of a barrier, because once a contact is taken over, the extra trust WeChat gives to contacts works for the attacker rather than the user.

That handover is the part the demo shows. One Android phone called an iPhone and took over its WeChat while the phone was still ringing. The compromised iPhone then called a second Android phone and took control of it the same way.

Calif's post describes routes an attacker could use rather than ones it tested. Once the exploit runs, the researchers said, the attacker has full control of the WeChat account and can read and send messages, make calls, and act as the account's owner. On its own, it does not give control of the phone itself.

For many users, that account is not only a chat app. WeChat's [App Store listing](https://apps.apple.com/us/app/wechat/id414478124) covers payments, official accounts and mini programs inside the app. Tencent put the combined monthly active users of WeChat and Weixin at 1.439 billion as of 30 June 2026 in its [second-quarter results](https://www.prnewswire.com/apac/news-releases/tencent-announces-2026-second-quarter-results-302849608.html).

Tencent released version 8.0.77 for Android and 8.0.76 for iOS on 21 August, according to its own [release log](https://weixin.qq.com/updates?platform=ios&version=8.0.76). Calif said those releases mitigated the bug and that, on 28 August, it confirmed the exploit was blocked on Tencent's servers as well.

The researchers said Tencent has "mitigated our exploit for all users." Asked whether the underlying flaw had also been fixed, Calif told The Hacker News it could not comment. Tencent has published no advisory about the flaw, and its release notes for the iOS version and its App Store entry describe the update as only bug fixes.

According to Calif, the block runs on Tencent's servers, so it does not require users to install anything. Running a current version is still the safer choice, and on 8 September that listing showed 8.0.76, released on 21 August, as the current version.

Calif told The Hacker News it tested the exploit against WeChat 8.0.76 for Android and 8.0.75 for iOS, in each case the version numbered one below the release Tencent shipped on 21 August. It said the tests ran on iOS 26.6 and some older Android versions. Neither company has published a full list of affected versions, so a user on a different build cannot tell whether it was vulnerable.

Tencent also ships WeChat clients for HarmonyOS, Windows, Mac and Linux on their own release schedules. Calif declined in the same reply to say whether it had tested any of them, and Tencent has not addressed them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

Calif is holding back the technical details and plans to present the full analysis at a conference. It has not published anything a defender could search for, and there is no way for a user to tell whether they were called.

Checks on 8 September found no CVE identifier for the flaw and no advisory on Tencent's security response site, which lists the latest announcement as April 2022. The Hacker News has contacted Tencent for comment.

Calif said it worked with AI to find the bug and write the first exploit that could run code on the phone in about two days. Building the worm took another week, it said.

Calif told The Hacker News it had designed a set of skills that guide an AI in exploring and identifying potential attack surfaces in messaging apps, and that the AI discovered this flaw using them.

Its own timeline gives longer gaps. Its engineering team knew of the bug on 23 July, the first Android exploit was finished on 30 July, and the worm demo on 11 August. The post does not say whether the shorter figures count only working time.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#l...