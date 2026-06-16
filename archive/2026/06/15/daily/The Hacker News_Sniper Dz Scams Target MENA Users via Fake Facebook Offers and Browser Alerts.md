---
title: Sniper Dz Scams Target MENA Users via Fake Facebook Offers and Browser Alerts
url: https://thehackernews.com/2026/06/sniper-dz-scams-target-mena-users-via.html
source: The Hacker News
date: 2026-06-15
fetch_date: 2026-06-16T07:17:04.312640
---

# Sniper Dz Scams Target MENA Users via Fake Facebook Offers and Browser Alerts

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Sniper Dz Scams Target MENA Users via Fake Facebook Offers and Browser Alerts](https://thehackernews.com/2026/06/sniper-dz-scams-target-mena-users-via.html)

**Ravie Lakshmanan**Jun 15, 2026Social Engineering / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-L0YMpJQcSqCJeQR6NevaPeBZW1uc13Y3nV37mR6tEuSsuMxWV6RrohLtgsVqG_Ja_kBoZTAMcKXlaG-OfyjrLDAUwhO_pQifFv64iRc-HE0nAAMJ88BF_xEQwOj39EdAE5ZTNU7q7y3SjBjKsvBZckb_jcg1FzMM9YRe9OV9UFsNyjH2km2jAXvBIdTa/s1700-e365/phishing-sniperdz.jpg)

Cybersecurity researchers have disclosed details of fraudulent activity targeting users across the Middle East and North Africa by employing various fraudulent Facebook accounts impersonating politicians, public figures, and trusted organizations.

"These accounts promoted fake offers, including free mobile internet packages, financial compensation, and government subsidy programs," Group-IB analysts Anna Yurtaeva and Viacheslav Shevchenko [said](https://www.group-ib.com/blog/inside-sniperdz-phaas-ecosystem/).

"Victims were encouraged to click embedded links to claim the advertised benefits, but were instead redirected through a chain of intermediary websites that ultimately led to phishing and traffic monetization infrastructure."

The Singapore-headquartered cybersecurity company has these campaigns to [Sniper Dz](https://thehackernews.com/2026/06/interpol-takes-down-sniper-dz-phishing.html), a turnkey phishing-as-a-service (PhaaS) platform that was taken down last month in an INTERPOL-led operation. The findings indicate that the platform goes beyond facilitating credential theft, generating illicit revenue via browser notification abuse, premium SMS subscriptions, premium-rate calls, and investment scams.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

A "typical Sniper Dz scam victim funnel" begins with localized social engineering lures, with the scammers impersonating well-known telecom providers such as Algérie Télécom to promote fake offers, to direct users to domains hosted on Link in bio services that act as an intermediary layer between the social media post and the final destination.

"Rather than directing victims straight to a malicious website, the campaign first routes users through trusted link-aggregation platforms such as Linkbio and Linktree," Group-IB researchers said. "The attackers create decoy landing pages on domains operated by these services."

The attack ends with directing victims to a page that obtains browser notification permissions by prompting users to click "Allow" to continue. Behind the scenes, code embedded in the web page subscribes the web browser to a push notification system using a Voluntary Application Server Identification ([VAPID](https://blog.mozilla.org/services/2016/08/23/sending-vapid-identified-webpush-notifications-via-mozillas-push-service/)) public key.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWUCIqI6jKCCP3L-BD3TFpocrCa-UPpOKdfXqdMLJfDwhzlye9Zl6Ds7fg7d2TkvGnFehOFn1F67a7L8z7wxx3bt8Q4Ya_5akCOCatWoDlrjtgSZJllvCylZz-7BiJYlTKYclj4yfkyNLAV8vBcjfvrm5rgqep8NC_S6LJGsZ8i7Qz5hwSFf7kK5LAQwk-/s1700-e365/Sniperdz.png)

Group-IB said the same VAPID key has been observed across campaigns masquerading as telecommunications providers in Algeria and investment-related scams targeting users in multiple regions.

"Because VAPID public keys are used to identify the notification service responsible for delivering push messages, their reuse can provide valuable insight into underlying infrastructure relationships," the company said. "The consistent appearance of the same key across otherwise distinct campaigns suggests that the operators are relying on a shared push-notification ecosystem rather than independent infrastructure."

Furthermore, the page engages in back button hijacking by injecting 10 fake history states, tricking users into visiting sites that may serve unsolicited ads, or trapping them in a "back-button prison" and within attacker-controlled content to inflate ad impressions, promote scams, or deliver malicious content.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"The page also implements a tab-under technique that activates when users interact with certain links," the cybersecurity company noted. If a link opens a new browser tab, a delayed script silently redirects the original tab to another destination controlled by the operators.

"This allows the campaign to continue driving traffic through its redirection and monetization infrastructure even after the victim believes they have left the site. By combining browser notification abuse with history manipulation and tab-under redirections, the operators make it significantly more difficult for users to escape the scam ecosystem."

Once users are enrolled into the notification infrastructure, the attacks progress to the monetization phase, routing the victims to a traffic distribution system (TDS) that determines which scam to present based on factors like device type, location, and mobile carrier. Potential pathways include premium-rate call scams, premium SMS subscription fraud, and investment scams.

"This campaign demonstrates how modern fraud operations increasingly rely on the abuse of legitimate web technologies rather than traditional malware," Group-IB said. "Instead of infecting devices, the operators exploit trusted platforms, browser features, and social engineering techniques to guide victims through a carefully designed monetization funnel."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
...