---
title: URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat
url: https://thehackernews.com/2026/07/urgent-progress-tells-sharefile.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:36.494435
---

# URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat](https://thehackernews.com/2026/07/urgent-progress-tells-sharefile.html)

**Swati Khandelwal**Jul 10, 2026Enterprise Security / Security Incident

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgULXOG2_Ph1198nw2lOea2pYE9u1GkPHaaMlzhpO48pOmejpWKFuHbchUac5JIRQHGiIMMTefXq-LktA8AjsqqMIsBS54bLaludxIJbq7chYfo_Vsoqf9Xi7YomnSUL9wHAYa5InCST76k1aP10VMmNKK_MDLD3o5zNXyB4ODMRMl0DbLkz9f2mg2k2S8/s1700-e365/progress.jpg)

Progress Software has told ShareFile customers to shut down the Windows servers running their Storage Zone Controllers, confirming to **The Hacker News** that it is responding to a "credible external security threat."

The company has temporarily disabled access to the affected accounts, a step it says it took "out of an abundance of caution" while it works with internal and external security experts.

It says it has no indication of unauthorized access to any ShareFile accounts or data, and that it notified customers after learning of the threat.

What Progress has not said is what the threat is or who is behind it.

The order became public when a customer posted the company's email to Reddit's [r/sysadmin](https://www.reddit.com/r/sysadmin/comments/1usohco/psa_shutdown_your_sharefile_storage_zone/) on July 10. Progress [confirmed the disruption](https://status.sharefile.com/) on its status page, listing Storage Zone Controller customers as "not operational" and the incident as under investigation as of a 12:12 p.m. EDT update.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Only the Storage Zone Controller is affected, not standard cloud-only ShareFile accounts. The controller is a server that a company runs itself, so files can stay on its own storage while it still uses ShareFile's cloud to share and manage them.

The controller usually sits at the network's edge, reachable from the internet. That exposure makes it both useful and a target. Ordering customers to take it fully offline, rather than just patch it, is a notable step.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuIEperKcgWWot-nes4WRvJrO5SGh6v427wpkWQooK_eTA9AGQzfo1YTPo9aSmrCZ25_e9NKLgRAGG9wiYyjY0Sf7tXiigFaTpLveXt6waUA2BSXpU2Ec5zWqAJaWMnM0f9sKuYOF0QklaPLgl1GZwPZbtFkVQJn9H_MpMWwJeKMkgC33dCEISt8SGS54/s1700-e365/email.jpg)

That choice is itself a tell. If a fix for this threat existed, Progress would be telling customers to apply it; the shutdown order suggests there is none yet. That usually means a newly found flaw the company is racing to close, though the same step would also fit a threat a patch cannot address, such as stolen keys or a problem on Progress's own side.

Its statement that no accounts or data were accessed is careful wording, too, and does not rule out trouble on the controllers themselves.

## What to do now

1. Follow the shutdown order first. Keep the affected controllers offline until Progress says what the threat is and when it is safe to restart.
2. Separately, confirm your version is current: 5.12.4 or later on the 5.x line, or a 6.x release. That closes the flaws fixed earlier this year, but Progress has not said it clears the current threat, so do not treat it as permission to restart.
3. If a controller is reachable from the internet, handle it as a possible incident. Preserve the logs and start your incident-response process, then check for unfamiliar .aspx files in the web folders and storage paths you did not set. A clean-looking server is not proof that it is clean.

ShareFile has faced this before. In 2023, while the product still belonged to Citrix, attackers exploited an unauthenticated flaw in the same Storage Zones Controller (CVE-2023-24489).

CISA [flagged it as actively exploited](https://thehackernews.com/2023/08/cisa-adds-citrix-sharefile-flaw-to-kev.html), and Citrix cut unpatched controllers off from the ShareFile cloud, the same access block Progress has now imposed.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Progress, which acquired ShareFile in 2024, had already weathered a mass file-transfer attack of its own: MOVEit, whose 2023 zero-day was exploited by the Clop group and hit more than 2,700 organizations.

The Storage Zones Controller also had two critical flaws that watchTowr [disclosed in April](https://thehackernews.com/2026/04/threatsday-bulletin-pre-auth-chains.html) and Progress patched in March, though the company has not connected the current threat to them, and neither has been reported as exploited.

The central question is still unanswered: Progress has pulled these systems offline and is working with outside experts, but has not said what the threat is or when customers can safely bring them back online.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

...