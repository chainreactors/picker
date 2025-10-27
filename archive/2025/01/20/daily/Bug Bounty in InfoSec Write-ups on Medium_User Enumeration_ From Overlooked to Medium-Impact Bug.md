---
title: User Enumeration: From Overlooked to Medium-Impact Bug
url: https://infosecwriteups.com/user-enumeration-from-overlooked-to-medium-impact-bug-48bbefa2ab3b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-20
fetch_date: 2025-10-06T20:09:09.886953
---

# User Enumeration: From Overlooked to Medium-Impact Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F48bbefa2ab3b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fuser-enumeration-from-overlooked-to-medium-impact-bug-48bbefa2ab3b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fuser-enumeration-from-overlooked-to-medium-impact-bug-48bbefa2ab3b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-48bbefa2ab3b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-48bbefa2ab3b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# User Enumeration: From Overlooked to Medium-Impact Bug

## In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the ‘Alamin (mankind, jinns and all that exists)

[![callgh0st](https://miro.medium.com/v2/resize:fill:64:64/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---byline--48bbefa2ab3b---------------------------------------)

[callgh0st](https://callgh0st.medium.com/?source=post_page---byline--48bbefa2ab3b---------------------------------------)

3 min read

·

Jan 15, 2025

--

1

Listen

Share

Good day! I hope this message finds everyone in good health and spirits. Without further ado, let me dive into today’s Bug: **User Enumeration Vulnerability**.

At first glance, user enumeration may seem like a minor issue, often marked as “informative” on platforms like HackerOne or Bugcrowd. However, the situation I encountered was distinct, as it occurred on a self-hosted platform, which added weight to the findings.

> Note: I’ll refer to the target as `gaza.com`

The application has a search feature enabling users to find others. Initially, I noticed that by entering email addresses, I could enumerate user accounts. At first, I assumed this was intended functionality and dismissed it as unworthy of reporting. A few days later, I revisited the platform and tested the search functionality again. This time, I explored it more thoroughly.

### Summary of the Report:

The search functionality on the site leaks usernames associated with valid email addresses. This allows attackers to enumerate user accounts and confirm the existence of specific email addresses in the system. Here’s how it works:

1. When an email exists in the system, the search feature confirms its validity by displaying usernames associated with the email.
2. Searching by domain (e.g., `@yahoo.com`, `@palestine.com`) lists all users using the specified email domain.
3. An attacker can modify the search patterns (e.g., `l@gmail.com`, `lu@gmail.com`, `luc@gmail.com`, etc.) to narrow down results to individual users.

### Steps to Reproduce:

1. Navigate to the search bar designed for finding friends.
2. Input an email pattern, e.g., `@gmail.com`.
3. Observe that the application displays users with email addresses from that domain.

Press enter or click to view image in full size

![]()

4. Refine the search using partial email prefixes (e.g., `l@gmail.com`, `lu@gmail.com`, `luc@gmail.com`, etc.) to enumerate specific users.

5. Using this method, I discovered two valid users (e.g., `redacted@gmail.com`).

![]()

### Impact:

1. Attackers can use this feature to enumerate and collect usernames and their associated email addresses.
2. The information can be leveraged for:

* **Targeted phishing attacks**
* **Social engineering**
* **Brute force attacks**

Initially, I was unsure whether this was worth reporting, but I submitted it nonetheless, trusting in Allah’s plans. To my surprise, the program rated the issue as **Medium severity**, marking my first Medium-level report. **Alhamdulillah**!

Press enter or click to view image in full size

![]()

The application’s rate-limiting mechanism can be bypassed by rotating the IP address without being effectively restricted by the rate limit.

### Key Takeaway:

Always report what you suspect might be an issue, even if you’re uncertain. What seems like an intended feature could have significant unintended consequences.

I appreciate the opportunity to share this with you all. Allah is indeed the best of planners.

> For any suggestions or Correction, Kindly reach out to me:
>
> Twitter — [callgh0st](https://twitter.com/callgh0st)

> The Zionists have no right to the land of Palestine. There is no place for them on the land of Palestine.
>
> [**Mohammed Morsi**](https://www.brainyquote.com/authors/mohammed-morsi-quotes)

[Hacking](https://medium.com/tag/hacking?source=post_page-----48bbefa2ab3b---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----48bbefa2ab3b---------------------------------------)

[Email](https://medium.com/tag/email?source=post_page-----48bbefa2ab3b---------------------------------------)

[Palestine](https://medium.com/tag/palestine?source=post_page-----48bbefa2ab3b---------------------------------------)

[Genocide](https://medium.com/tag/genocide?source=post_page-----48bbefa2ab3b---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--48bbefa2ab3b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--48bbefa2ab3b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--48bbefa2ab3b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--48bbefa2ab3b---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--48bbefa2ab3b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![callgh0st](https://miro.medium.com/v2/resize:fill:96:96/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---post_author_info--48bbefa2ab3b---------------------------------------)

[![callgh0st](https://miro.medium.com/v2/resize:fill:128:128/1*S943nhX0uzpVeh6N-49d...