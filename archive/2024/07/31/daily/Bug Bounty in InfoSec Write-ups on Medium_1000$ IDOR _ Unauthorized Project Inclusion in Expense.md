---
title: 1000$ IDOR : Unauthorized Project Inclusion in Expense
url: https://infosecwriteups.com/1000-idor-unauthorized-project-inclusion-in-expense-b9ce08b28c71?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:42:05.551645
---

# 1000$ IDOR : Unauthorized Project Inclusion in Expense

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb9ce08b28c71&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1000-idor-unauthorized-project-inclusion-in-expense-b9ce08b28c71&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1000-idor-unauthorized-project-inclusion-in-expense-b9ce08b28c71&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40a13h1)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b9ce08b28c71---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b9ce08b28c71---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 1000$ IDOR : Unauthorized Project Inclusion in Expense

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---byline--b9ce08b28c71---------------------------------------)

[Abhi Sharma](https://medium.com/%40a13h1?source=post_page---byline--b9ce08b28c71---------------------------------------)

3 min read

·

Jul 19, 2024

--

1

Share

Hi Everyone! Today, I’m excited to talk about a critical vulnerability I discovered in a platform (let’s call it ExamFit), which allowed users to bypass project status restrictions and submit unauthorized expense reports. Join me as we explore how this flaw was identified and its implications.

Press enter or click to view image in full size

![]()

> **Understanding ExamFit:**

ExamFit is a robust expense management system designed to ensure accuracy and compliance with organizational policies. It serves as a centralized hub where organizations manage their financial transactions and monitor project expenses securely.

> **The Flaw :**

In examfit if admin restrict/disable a project, no user can be able to submit an expense report through that project. Despite stringent project status controls set by administrators, a vulnerability was found that allows users to manipulate API requests. By using a specific POST request to /hr/expenses/submission/submit, users can include disabled project IDs in the projectId parameter. This oversight enables the creation of expense reports associated with projects that should be inaccessible.

### **Steps to Reproduce:**

* **Access ExamFit Platform:** Log in with a standard user account.
* **Use the POST Request:** Send a POST request to…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b9ce08b28c71---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b9ce08b28c71---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b9ce08b28c71---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b9ce08b28c71---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--b9ce08b28c71---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:96:96/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---post_author_info--b9ce08b28c71---------------------------------------)

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:128:128/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---post_author_info--b9ce08b28c71---------------------------------------)

[## Written by Abhi Sharma](https://medium.com/%40a13h1?source=post_page---post_author_info--b9ce08b28c71---------------------------------------)

[1.92K followers](https://medium.com/%40a13h1/followers?source=post_page---post_author_info--b9ce08b28c71---------------------------------------)

·[0 following](https://medium.com/%40a13h1/following?source=post_page---post_author_info--b9ce08b28c71---------------------------------------)

Cybersecurity Consultant | Pentester | Bug Bounty Hunter | ContentWriter 🔗 Connect with me on <https://twitter.com/a13h1_> and <https://www.linkedin.com/in/a13h1/>

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b9ce08b28c71---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b9ce08b28c71---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b9ce08b28c71---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b9ce08b28c71---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b9ce08b28c71---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b9ce08b28c71---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b9ce08b28c71---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b9ce08b28c71---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b9ce08b28c71---------------------------------------)