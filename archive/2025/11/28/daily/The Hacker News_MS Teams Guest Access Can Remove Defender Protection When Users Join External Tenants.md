---
title: MS Teams Guest Access Can Remove Defender Protection When Users Join External Tenants
url: https://thehackernews.com/2025/11/ms-teams-guest-access-can-remove.html
source: The Hacker News
date: 2025-11-28
fetch_date: 2025-11-29T03:13:02.945081
---

# MS Teams Guest Access Can Remove Defender Protection When Users Join External Tenants

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [MS Teams Guest Access Can Remove Defender Protection When Users Join External Tenants](https://thehackernews.com/2025/11/ms-teams-guest-access-can-remove.html)

**Nov 28, 2025**Ravie LakshmananEmail Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_Md0lsjItddYFH1gCm6LZYxVDobM4ZWOweikeQFAT0yZNSYS8WKfg61LxSRjc49watAPtqESgvWx0UwppGQuw9FU8OMQDf9EOi1fWnVXF_H8L7QNOplD1-vdDAO-oU4cRg9CX2jky45M7SkmAF6b7GGi7UwMZQN4_7wnlG2D1mYl28_sUC7hLta8u37Oa/s790-rw-e365/msteams.jpg)

Cybersecurity researchers have shed light on a cross-tenant blind spot that allows attackers to bypass Microsoft Defender for Office 365 protections via the [guest access](https://learn.microsoft.com/en-us/microsoftteams/guest-experience) feature in Teams.

"When users operate as guests in another tenant, their protections are determined entirely by that hosting environment, not by their home organization," Ontinue security researcher Rhys Downing [said](https://www.ontinue.com/resource/blog-microsoft-chat-with-anyone-understanding-phishing-risk/) in a report.

"These advancements increase collaboration opportunities, but they also widen the responsibility for ensuring those external environments are trustworthy and properly secured."

The development comes as Microsoft has begun rolling out a new feature in Teams that allows users to chat with anyone via email, including those who don't use the enterprise communications platform, starting this month. The change is expected to be globally available by January 2026.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"The recipient will receive an email invitation to join the chat session as a guest, enabling seamless communication and collaboration," Microsoft [said](https://mc.merill.net/message/MC1182004) in its announcement. "This update simplifies external engagement and supports flexible work scenarios."

In the event the recipient already uses Teams, they are notified via the app directly in the form of an external message request. The feature is enabled by default, but organizations can turn it off using the TeamsMessagingPolicy by [setting](https://learn.microsoft.com/en-us/powershell/module/microsoftteams/set-csteamsmessagingpolicy) the "UseB2BInvitesToAddExternalUsers" parameter to "false."

That said, this setting only prevents users from sending invitations to other users. It does not stop them from receiving invitations from external tenants.

At this stage, it's worth mentioning that [guest access](https://learn.microsoft.com/en-us/microsoftteams/guest-access) is different from [external access](https://learn.microsoft.com/en-us/microsoftteams/communicate-with-users-from-other-organizations), which allows users to find, call, and chat with people who have Teams but are outside of their organizations.

The "fundamental architectural gap" highlighted by Ontinue stems from the fact that [Microsoft Defender for Office 365 protections](https://learn.microsoft.com/en-us/defender-office-365/mdo-support-teams-about) for Teams may not apply when a user accepts a guest invitation to an external tenant. In other words, by entering the other tenant's security boundary, the user is subjected to security policies where the conversation is hosted and not where the user's account lives.

What's more, it opens the door to a scenario where the user can become an unprotected guest in a malicious environment that's dictated by the attacker's security policies.

In a hypothetical attack scenario, a threat actor can create "protection-free zones" by disabling all safeguards in their tenants or avail licenses that lack certain options by default. For instance, the attacker can spin up a malicious Microsoft 365 tenant using a low-cost license such as Teams Essentials or Business Basic that doesn't come with Microsoft Defender for Office 365 out of the box.

Once the unprotected tenant is set up, the attacker can then conduct reconnaissance of the target organization to gather more information and initiate contact via Teams by entering a victim's email address, causing Teams to send an automated invitation to join the chat as a guest.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Perhaps the most concerning aspect of the attack chain is that the email lands on the victim's mailbox. Given that the message originates from Microsoft's own infrastructure, it effectively bypasses [SPF, DKIM, and DMARC checks](https://thehackernews.com/2025/01/neglected-domains-used-in-malspam-to.html). As a result, email security solutions are unlikely to flag the email as malicious.

Should the victim end up accepting the invitation, they are granted guest access in the attacker's tenant, where all subsequent communication takes place. The threat actor can send phishing links or distribute malware-laced attachments by taking advantage of the lack of Safe Links and Safe Attachments scans.

"The victim's organization remains completely unaware," Downing said. "Their security controls never triggered because the attack occurred outside their security boundary."

To safeguard against this line of attack, organizations are recommended to restrict B2B collaboration settings to only allow guest invitations from trusted domains, implement cross-tenant access controls, restrict external Teams communication if not required, and train users to watch out for unsolicited Teams invites from external sources.

The Hacker News has reached out to Microsoft for comment, and we will update the story if we hear back.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[...