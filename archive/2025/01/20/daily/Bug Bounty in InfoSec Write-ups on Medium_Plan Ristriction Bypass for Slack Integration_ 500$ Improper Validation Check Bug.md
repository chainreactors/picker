---
title: Plan Ristriction Bypass for Slack Integration: 500$ Improper Validation Check Bug
url: https://infosecwriteups.com/plan-ristriction-bypass-for-slack-integration-500-improper-validation-check-bug-0c1acf6f01d3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-20
fetch_date: 2025-10-06T20:09:05.715189
---

# Plan Ristriction Bypass for Slack Integration: 500$ Improper Validation Check Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0c1acf6f01d3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fplan-ristriction-bypass-for-slack-integration-500-improper-validation-check-bug-0c1acf6f01d3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fplan-ristriction-bypass-for-slack-integration-500-improper-validation-check-bug-0c1acf6f01d3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40a13h1)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0c1acf6f01d3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0c1acf6f01d3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Plan Ristriction Bypass for Slack Integration: 500$ Improper Validation Check Bug**

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---byline--0c1acf6f01d3---------------------------------------)

[Abhi Sharma](https://medium.com/%40a13h1?source=post_page---byline--0c1acf6f01d3---------------------------------------)

2 min read

·

Sep 28, 2024

--

1

Listen

Share

**Hello Readers,** I’m thrilled to share details about a recent discovery I made concerning entry.io’s integration functionality. I’ve identified a vulnerability that allows users with free plan accounts to bypass subscription restrictions and integrate Slack, typically reserved for higher subscription tiers. For this report, Xentry.io acknowledged the issue and awarded me a bounty of $500.

Press enter or click to view image in full size

![]()

> **Understanding Target**

Xentry.io is a prominent platform used for error tracking and monitoring in software development. However, a flaw in its integration setup process enables users to circumvent plan restrictions and utilize Slack integrations without the required subscription level.

> **The Vulnerability:**

This vulnerability arises from improper validation in Xentry.io’s integration setup flow, particularly when transitioning from GitHub to Slack integrations. Users on free plan accounts can exploit this flaw by modifying intercepted HTTP requests, allowing them to add Slack integrations instead of the restricted GitHub integrations.

### Steps to Reproduce:

**Create a Free Plan Account**:

* Sign up for a free plan account on Xentry.io.
* Go to the integrations section and select GitHub integration(which is free for all the users) .
* Use tools like Burp Suite to intercept the HTTP request for adding GitHub integration. `(GET /organizations/dd-0n/integrations/github/setup/? HTTP/2)`
* Replace “github” with “slack” in the intercepted request URL.
* Forward the modified request and follow the steps on the new page to connect your Slack account with Xentry.

> **Impact**

* Users on free plan accounts can access Slack integrations, potentially exposing sensitive information and configuring alerts within Slack channels.
* It undermines Xentry.io’s subscription model by allowing users to utilize premium features reserved for higher subscription tiers, impacting operational integrity and service delivery.

> **Response and Resolution**

Upon discovering this vulnerability, I promptly reported it to Xentry.io’s security team. They acknowledged the issue and took immediate steps to address the flaw, ensuring that proper validation mechanisms are in place to enforce plan restrictions effectively. As a token of appreciation for responsible disclosure, I received a bounty of $500.

![]()

> **Connect and Engage**

If you found this article informative, please share your feedback and insights in the comments section. Follow me for more updates on cybersecurity insights and responsible disclosure stories.

> **Connect on Twitter:** [**@a13h1\_**](https://twitter.com/a13h1_)

### Thank you for your continued support. Keep clapping, commenting, and sharing your thoughts!

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----0c1acf6f01d3---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----0c1acf6f01d3---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----0c1acf6f01d3---------------------------------------)

[Access Control](https://medium.com/tag/access-control?source=post_page-----0c1acf6f01d3---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page-----0c1acf6f01d3---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0c1acf6f01d3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0c1acf6f01d3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0c1acf6f01d3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0c1acf6f01d3---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--0c1acf6f01d3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:96:96/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---post_author_info--0c1acf6f01d3---------------------------------------)

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:128:128/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---post_author_info--0c1acf6f01d3---------------------------------------)

[## Written by Abhi Sharma](https://medium.com/%40a13h1?source=post_page---post_author_info--0c1acf6f01d3---------------------------------------)

[1.92K followers](https://medium.com/%40a13h1/followers?source=post_page---post_author_info--0c1acf6f01d3---------------------------------------)

·[0 following](https://medium.com/%40a13h1/following?source=post_page---post_author_info--0c1acf6f01d3-----------------...