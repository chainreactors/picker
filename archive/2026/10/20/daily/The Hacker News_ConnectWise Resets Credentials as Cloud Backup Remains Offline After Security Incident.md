---
title: ConnectWise Resets Credentials as Cloud Backup Remains Offline After Security Incident
url: https://thehackernews.com/2026/10/connectwise-resets-credentials-as-cloud.html
source: The Hacker News
date: 2026-10-20
fetch_date: 2026-10-21T06:51:13.045001
---

# ConnectWise Resets Credentials as Cloud Backup Remains Offline After Security Incident

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [ConnectWise Resets Credentials as Cloud Backup Remains Offline After Security Incident](https://thehackernews.com/2026/10/connectwise-resets-credentials-as-cloud.html)

**Ravie Lakshmanan**Oct 20, 2026Cloud Security / Incident Response

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgN8mboHojdAmthr-jUWvIgg5BgmRsrAFJRQFz-nEuPEAIGTqwVKwnf9c7E8jGzdpHfWZuDENURbDFFADIJ76Tf7h5lamLTOUoY5ui438ugfOJYw-2vkAuITMBMxt-0CWFxj43bdgDY19exYceRvJEScmPpWoYXBjkIHLOilUSF1wWmSta5o9ocPpLywQn/s1700-nu-rw-lo-l85-e365/connect.jpg)

ConnectWise on Monday said it has taken remediation measures, including strengthening administrative-access protections and resetting accounts and replacing application credentials, as it continues to respond to a security incident that led to [unauthorized access to application identities](https://thehackernews.com/2026/10/connectwise-suspends-cloud-backup-after.html) associated with Cloud Backup.

The company said it has [completed the following actions](https://www.connectwise.com/company/trust/advisories) since it began rolling out mitigations on October 17 at 5:00 a.m. UTC, three days after the incident was first identified -

* Disabling affected application connections and suspending Cloud Backup.
* Suspending SaaS Security and Cloud Management as a precaution because they are integrated with Cloud Backup.
* Enlisting the help of independent third-party specialists for incident response and remediation.
* Enhancing administrative-access protections.
* Publishing technical guidance to help partners investigate and remediate potential unauthorized activity in their own and managed customer environments.

ConnectWise said it's validating the effectiveness of its containment measures and emphasized that it has not seen any successful threat activity in the environments it monitors. There is no evidence that any ConnectWise products and services, other than Cloud Backup and the precautionary suspensions of SaaS Security and Cloud Management, are impacted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

"This observation does not establish whether individual partner or customer Microsoft 365 tenants have been affected," it said. "Reviewing each potentially affected tenant remains essential."

"Before making changes, preserve relevant evidence, validate findings, and assess potential operational impacts. Completing these steps does not guarantee that a tenant is unaffected or that all unauthorized access has been eliminated. Do not reconnect affected applications until ConnectWise provides formal restoration instructions."

Huntress has shared the following IP addresses observed in connection with the activity, adding that the password spray and failed login attempts linked to some of them are unlikely to be related to the application sign-in activity -

* 144.172.64[.]128 - Application sign-ins with a vendor credential (primary vector)
* 144.172.64[.]99 - Failed user password spray, concentrated (October 10 to 14, 2026)
* 144.172.64[.]60 - A few failed user logins (October 18, 2026)
* 144.172.94[.]243 - Broad failed login spray, ongoing against many organizations

"In a review of application sign-ins across more than 10,000 tenants with ConnectWise applications (where we can see those logs), 144.172.64[.]128 and Microsoft-internal ranges are the only addresses that produced application sign-in activity," Huntress researchers [said](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access) in an update.

"We did not see application sign-in activity from any of the other addresses listed below, all of which are in the same provider range as 144.172.64[.]128 (AS14956, RouterHosting). We did see password spray and failed login attempts from some of them."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The cybersecurity company said it also observed post-compromise actions on a second tenant, following the [same modus operandi as before](https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html), in which the application granted itself Global Administrator and then added a new secret on a small number of other applications in the tenant for persistence.

While the access may have been used for Microsoft Graph directory reads, there are no signs the attackers weaponized it for mailbox or file manipulation, or to make user or policy changes.

"The choice of which applications to backdoor appeared to be random in the two tenants we reviewed," Huntress added. "Across the two compromised tenants, the identical grant flow selected two completely different sets of applications. The only consistent criteria we can point to is structural: credentials were planted in applications that are registered inside the affected tenant, without regard to what those applications can actually do."

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

SHARE **

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [cyberattack](https://thehackernews.com/search/label/cyberattack), [Identity Security](https://t...