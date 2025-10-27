---
title: A Cyberattack Victim Notification Framework
url: https://www.schneier.com/blog/archives/2025/09/a-cyberattack-victim-notification-framework.html
source: Schneier on Security
date: 2025-09-13
fetch_date: 2025-10-02T20:06:59.267863
---

# A Cyberattack Victim Notification Framework

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## A Cyberattack Victim Notification Framework

Interesting [analysis](https://securityandtechnology.org/virtual-library/report/improving-private-sector-cyber-victim-notification-and-support/):

> When cyber incidents occur, victims should be notified in a timely manner so they have the opportunity to assess and remediate any harm. However, providing notifications has proven a challenge across industry.
>
> When making notifications, companies often do not know the true identity of victims and may only have a single email address through which to provide the notification. Victims often do not trust these notifications, as cyber criminals often use the pretext of an account compromise as a phishing lure.
>
> […]
>
> This report explores the challenges associated with developing the native-notification concept and lays out a roadmap for overcoming them. It also examines other opportunities for more narrow changes that could both increase the likelihood that victims will both receive and trust notifications and be able to access support resources.
>
> The report concludes with three main recommendations for cloud service providers (CSPs) and other stakeholders:
>
> 1. Improve existing notification processes and develop best practices for industry.- Support the development of “middleware” necessary to share notifications with victims privately, securely, and across multiple platforms including through native notifications.- Improve support for victims following notification.
>
> While further work remains to be done to develop and evaluate the CSRB’s proposed native notification capability, much progress can be made by implementing better notification and support practices by cloud service providers and other stakeholders in the near term.

Tags: [cyberattack](https://www.schneier.com/tag/cyberattack/), [disclosure](https://www.schneier.com/tag/disclosure/)

[Posted on September 12, 2025 at 5:04 PM](https://www.schneier.com/blog/archives/2025/09/a-cyberattack-victim-notification-framework.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/09/a-cyberattack-victim-notification-framework.html#comments)

### Comments

KC •
[September 13, 2025 7:56 AM](https://www.schneier.com/blog/archives/2025/09/a-cyberattack-victim-notification-framework.html/#comment-447828)

A few unpacked observations from the report:

part 1:

When thinking about notifying individuals about cyber incidents, it’s a helpful parallel to think about the Dept of Defense. The DOD alerts on incidents in a band a level up, e.g., Unclassified to Secret, Secret to Top Secret.

For individuals, first and third party notifiers can help fill this role.

KC •
[September 13, 2025 7:59 AM](https://www.schneier.com/blog/archives/2025/09/a-cyberattack-victim-notification-framework.html/#comment-447829)

part 2:

Consider Apple as a mature first party notifier. When Apple detects zero-click spyware, it sends notifications to individuals through various channels like the customer portal, email, and Apple Messages. The notice directs individuals to seek assistance from a non-profit organization like Access Now via their Digital Security Helpline. Access Now received over 4,337 requests for assistance in 2024.

Additionally, proxies or third party notifiers can own this responsibility. The UK’s NCSC has developed a registry for UK companies to register for “Early Warning” alerts. The same responsibility could be given to banks, ISPs, counsel, etc.

KC •
[September 13, 2025 8:01 AM](https://www.schneier.com/blog/archives/2025/09/a-cyberattack-victim-notification-framework.html/#comment-447831)

part 3:

Of course, any conglomerate system would need to operate via a Data Clean Room where victim info could be submitted as hashed values and matched to the hashed values of account provider data.

Standards bodies, NIST for example, could update Special Publication 800-61 to include recommendations on victim notification. Cloud service providers and other stakeholders could convene a consortium to further develop this infrastructure.

I’m honestly sad to learn the Cyber Safety Review Board has been disbanded after three years. This excellent IST report evolved from Recommendations 18, 19, and 20 from the last CSRB report. Seeing as members of the CSRB were paid $0 I hope work like this continues to be organized under various stakeholders.

Clive Robinson •
[September 13, 2025 10:30 AM](https://www.schneier.com/blog/archives/2025/09/a-cyberattack-victim-notification-framework.html/#comment-447832)

@ Bruce, ALL,

With regards the article intro above,

> *“When cyber incidents occur, victims should be notified in a timely manner so they have the opportunity to assess and remediate any harm.*

In theory it’s easy, the “industry entities” just need a “trusted path” to the user and be “honest”…

In practice however,

“No industry entities can or should be trusted…”

One reason, is they sell the user out to completely untrustworthy people. [This includes but is not limited to the Governments and agencies of not just the user’s nation, but any nation such as North Korea, Iran, China, Russia and much worse such as the Dutch, Israeli and especially the US, UK. All of who then use it in ways that are often at best “unlawful”.]

Another is such entities lie about what has happened when security incidents occur. Thus any notification is basically pointless and worthless, except for causing mental distress in users…

Another is that any remediation such entities offer, are either completely pointless or the user finds they have to hand over all their “personal details” to yet another untrustworthy “industry entity”, to be sold off immediately or in the near future.

And I could go on and on with a near never ending list…

Take for instance the latest like “Brave” and their supposedly “better browser”… They have just forced in “client side scanning” by what they imply incorrectly is “helpful AI” but make it impossible for even experienced users to remove.

So dumping Brave pronto like any other AI “client side scanning” forcing “Industry Entity” would be a very good idea… Along with anything based on Google or Microsoft, Mozilla and similar browsers…

But who do you replace them with? Because they are all at it…

So next to nobody with any sense trusts any “industry entity”…

Which is just one of many many reasons we have the problem the article notes of,

> *“However, providing notifications has proven a challenge across industry.”*

Because mostly the industry is completely untrustworthy, and those that were trustworthy get turned to the dark side…

So there is not going to be a solution to this issue, untill there are very easily legally enforceable ways to protect users privacy in ways that will make the industry more trustworthy…

Just a reminder that long before the UK or Britain existed, there was a Royal issued punishment for breaching a Kings p...