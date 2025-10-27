---
title: The Secret Weakness Execs Are Overlooking: Non-Human Identities
url: https://thehackernews.com/2024/10/the-secret-weakness-execs-are.html
source: The Hacker News
date: 2024-10-04
fetch_date: 2025-10-06T18:54:44.143791
---

# The Secret Weakness Execs Are Overlooking: Non-Human Identities

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [The Secret Weakness Execs Are Overlooking: Non-Human Identities](https://thehackernews.com/2024/10/the-secret-weakness-execs-are.html)

**Oct 03, 2024**The Hacker NewsEnterprise Security / Cloud Security

[![Non-Human Identities](data:image/png;base64... "Non-Human Identities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXFhXBA8EMeRKZ0yakCBUMeB-_SXGBFRVsn0pBxnbIzGzBc39uwO5gkuOldAuzMVY8Rfr2j0QR8pZKOHYRHs6YqvodUudA82yIBAD9EpFygXbZ1bzLZtd9fHpoPJbDCHYRH5uppqRNJvK9xgunGZ_gCpit1SWrNxtAWEyK5vS0NQFFSfljC267NjdXgyE/s790-rw-e365/git.png)

For years, securing a company's systems was synonymous with securing its "perimeter." There was what was safe "inside" and the unsafe outside world. We built sturdy firewalls and deployed sophisticated detection systems, confident that keeping the barbarians outside the walls kept our data and systems safe.

The problem is that we no longer operate within the confines of physical on-prem installations and controlled networks. Data and applications now reside in distributed cloud environments and data centers, accessed by users and devices connecting from anywhere on the planet. The walls have crumbled, and the perimeter has dissolved, opening the door to a new battlefield: **identity**.

Identity is at the center of what the industry has praised as the new gold standard of enterprise security: "zero trust." In this paradigm, explicit trust becomes mandatory for any interactions between systems, and no implicit trust shall subsist. Every access request, regardless of its origin, must be authenticated, authorized, and continuously validated before access is granted.

## **The Dual Nature of Identity**

Identity is a broad concept with a dual reality. On the one hand, *people* need access to their email and calendar, and some (software engineers in particular) privileged access to a server or database to do their work. The industry has been perfecting managing these identities over the past 20 years as employees join, gain privileges for certain systems, and eventually leave the enterprise.

On the other hand, we have another type of identity: **machine identities,** also referenced as **non-human identities (NHIs)**, which account for the vast majority of all identities (it's estimated they outnumber human identities *at least* [by a factor of 45 to 1](https://blog.gitguardian.com/scale-21x/)).

Unlike their human counterparts, NHIs—ranging from servers, apps, or processes —are not tied to individuals and therefore pose a whole different problem:

* They **lack traditional security measures** because, unlike human users, we can't simply apply MFA to a server or an API key.
* They **can be created at any moment by anyone** in the enterprise (think Marketing connecting their CRM to the email client) with little to no supervision. They are scattered across a diversity of tools, which makes managing them incredibly complex.
* They are **overwhelmingly over-privileged** and very often 'stale': unlike human identities, NHIs are much more likely to stay long after they have been used. This creates a high-risk situation where over-provisioned credentials with broad permissions remain even after their intended use has ended.

All this combined presents the perfect storm for large enterprises grappling with sprawling cloud environments and intricate software supply chains. It's not surprising that mismanaged identities— [of which secrets sprawl is a symptom](https://blog.gitguardian.com/securing-your-machine-identities/)—are now the root cause of most security incidents affecting businesses worldwide.

## **The High Cost of Inaction: Real-World Breaches**

The consequences of neglecting NHI security are not theoretical. The news is replete with examples of high-profile breaches where compromised NHIs served as the entry point for attackers, leading to significant financial losses, reputational damage, and erosion of customer trust. Dropbox, Sisense, Microsoft, and The New York Times are all examples of companies that admitted to being impacted by a compromised NHI in 2024 *alone*.

The worst part, perhaps, is that these incidents have rippling effects. In January 2024, Cloudflare internal Atlassian systems were breached *because* tokens and service accounts— in other words, NHIs— were previously compromised at Okta, a leading identity platform. What's especially revealing here is that Cloudflare quickly detected the intrusion and responded by rotating the suspected credentials. However, they later realized some access tokens hadn't been properly rotated, giving attackers another shot at compromising their infrastructure.

This is not an isolated story: 80% of organizations have experienced identity-related security breaches, and the 2024 edition of the DBIR ranked "Identity or Credential compromise" as **the number one vector for cyberattacks**.

Should you be concerned? Looking back at the Cloudflare story, the impact is not yet known. However, the company disclosed that remediation efforts included rotating *all* *5,000 production credentials*, extensive forensic triage, and rebooting all the company's systems. Consider the time, resources, and financial burden such an incident would place on your organization. **Can you afford to take that risk?**

Addressing mismanaged identities, fixing both current exposures and future risks, is a long journey. While there's no magic bullet, tackling one of the biggest and most complex security risks of our era is achievable. Organizations **can mitigate risks associated with non-human identities** by combining immediate actions with mid- and long-term strategies.

Accompanying Fortune 500 customers in this process for the past 7 years is what made GitGuardian **the industry leader in secrets security.**

## **Getting a Grip on NHIs, Starting with Secrets Security**

Organizations must adopt a proactive and comprehensive approach to NHI security, starting with secrets security. Gaining control over NHIs begins with implementing effective secrets security ...