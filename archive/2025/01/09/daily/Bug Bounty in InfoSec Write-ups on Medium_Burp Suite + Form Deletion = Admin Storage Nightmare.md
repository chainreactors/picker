---
title: Burp Suite + Form Deletion = Admin Storage Nightmare
url: https://infosecwriteups.com/burp-suite-form-deletion-admin-storage-nightmare-240618a8c983?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-09
fetch_date: 2025-10-06T20:08:43.153844
---

# Burp Suite + Form Deletion = Admin Storage Nightmare

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F240618a8c983&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-suite-form-deletion-admin-storage-nightmare-240618a8c983&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-suite-form-deletion-admin-storage-nightmare-240618a8c983&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-240618a8c983---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-240618a8c983---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Press enter or click to view image in full size

![]()

# Burp Suite + Form Deletion = Admin Storage Nightmare

## In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the ‘Alamin (mankind, jinns and all that exists).

[![callgh0st](https://miro.medium.com/v2/resize:fill:64:64/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---byline--240618a8c983---------------------------------------)

[callgh0st](https://callgh0st.medium.com/?source=post_page---byline--240618a8c983---------------------------------------)

3 min read

·

Jan 7, 2025

--

3

Listen

Share

print(**“Hello World”**),

I hope you’re all doing well. Alhamdulillah, I’m doing well. Lately, it’s been an endless cycle of finding bugs😂. Today’s write-up is about a simple bug, but one that isn’t easily thought of.

> **Just So You Know (JSYK):** This report is a few months old and has been resolved. It pertains to a self-hosted program.
>
> Let’s get down to business.

The platform in question allows users to track, create, and manage paperless forms and surveys under dedicated accounts. These forms can be accessed and utilized on desktops, Apple devices, or Android devices. Users can also create groups or establish relationships (e.g., friends), with each user allocated storage space based on their account plan.

Press enter or click to view image in full size

![]()

### **Summary**

I discovered a flaw in the platform that allows a user to exhaust an admin’s or user’s storage space without their knowledge.

### **Here’s how it works:**

When an admin shares a form with a user that includes a file upload function, and the user begins uploading files but does not submit the form, the vulnerability arises if the admin deletes the form before submission. The user can capture the upload request using Burp Suite and repeatedly resend the request to consume the admin’s storage.

This issue persists because the server processes the repeated upload requests even though the form no longer exists, leading to unintended storage consumption.

Press enter or click to view image in full size

![]()

## Steps to Reproduce:

* The admin creates a form that allows users to upload images.

Press enter or click to view image in full size

![]()

* The user starts uploading files to the form but doesn’t complete the submission.

Press enter or click to view image in full size

![]()

* The admin deletes the form before the user submits it.

![]()

* The user captures the upload request using Burp Suite.
* The user resends the captured request repeatedly, bypassing validation.

Press enter or click to view image in full size

![]()

* The server processes these requests, storing the uploaded data and consuming the admin’s storage.

**Impact:**
1. Storage Exhaustion: A user can continuously upload data related to a deleted form, filling the admin’s storage space.

2. Financial Loss: Depending on the storage cost structure, the admin might incur unexpected charges.

### Response From Target:

Press enter or click to view image in full size

![]()

Alhamdulillah, it’s all part of the process. That’s all for today, hunters! Thank you for reading all the way to the end. If you found this write-up helpful, please show your support by clapping or sharing it.

Till next time - happy hunting! 😊

> For any suggestions or Correction, Kindly reach out to me:
>
> Twitter — [callgh0st](https://twitter.com/callgh0st)

> [Since 1948, Palestinians have been living under Israeli occupation, enduring systemic discrimination, violence, and countless deaths. An illegal blockade and closure imposed on Gaza in 2007 restricted Palestinians’ access to food, water, and other essential needs to lead a dignified life, imposing an apartheid state on Palestinians.](https://www.fian.org/en/press-release/article/statement-in-solidarity-with-the-people-of-gaza-3215#:~:text=Since%201948%2C%20Palestinians,state%20on%20Palestinians.)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----240618a8c983---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----240618a8c983---------------------------------------)

[Gaza](https://medium.com/tag/gaza?source=post_page-----240618a8c983---------------------------------------)

[Genocide](https://medium.com/tag/genocide?source=post_page-----240618a8c983---------------------------------------)

[Humanity](https://medium.com/tag/humanity?source=post_page-----240618a8c983---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--240618a8c983---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--240618a8c983---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--240618a8c983---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--240618a8c983---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--240618a8c983---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![callgh0st](https://miro.medium.com/v2/resize:fill:96:96/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---post_author_info--240618a8c983--------------------------...