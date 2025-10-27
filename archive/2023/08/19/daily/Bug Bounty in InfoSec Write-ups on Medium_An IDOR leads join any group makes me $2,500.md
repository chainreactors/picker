---
title: An IDOR leads join any group makes me $2,500
url: https://infosecwriteups.com/an-idor-leads-join-any-group-makes-me-2-500-406eb9e463a3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-19
fetch_date: 2025-10-04T11:59:29.492381
---

# An IDOR leads join any group makes me $2,500

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F406eb9e463a3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fan-idor-leads-join-any-group-makes-me-2-500-406eb9e463a3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fan-idor-leads-join-any-group-makes-me-2-500-406eb9e463a3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-406eb9e463a3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-406eb9e463a3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# An IDOR lead joins any group makes me $2,500

[![M7arm4n](https://miro.medium.com/v2/resize:fill:64:64/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---byline--406eb9e463a3---------------------------------------)

[M7arm4n](https://m7arm4n.medium.com/?source=post_page---byline--406eb9e463a3---------------------------------------)

3 min read

·

Aug 18, 2023

--

1

Listen

Share

Press enter or click to view image in full size

![]()

## **What’s IDOR!?**

> IDOR stands for “Insecure Direct Object References.” It’s a type of security vulnerability that occurs when an application allows an attacker to access or manipulate resources directly by modifying input parameters, such as URLs, without proper authorization. In other words, an attacker can bypass access controls and gain unauthorized access to objects (such as files, databases, or other resources) that they should not have access to.
>
> IDOR vulnerabilities typically arise when an application relies on user-supplied input to determine which object or resource to retrieve but does not properly validate or authorize the user’s access to that object. This can occur when an application exposes internal identifiers, like database record IDs, in URLs or parameters without properly checking whether the current user has permission to access those resources.

**Overview of the Vulnerability**

This website has a feature to create a private group, and group management can allow other users to access them by sending invitations, normally the information of private groups is confidential and inaccessible. When you are invited to a private group, in a part of the site you can see your invitations and accept or reject them. When you click Accept, the following message will be sent:

```
POST /GroupInvitations HTTP/1.1
Host: redacted.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redacted.com/GroupActivity
Content-Type: application/x-www-form-urlencoded
X-Xsrf-Token: 6c2be6f7-3880-4652-951b-9ef779f201d6
Content-Length: 37
Origin: https://redacted.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

GroupInvitations&action=A&c2mId=7069
```

the c2mId parameter is a code for the invited group and is vulnerable to IDOR, The attacker by changing this value to upper or downer can easily access other private groups.

**Steps to reproduce**

1. Create 3 accounts: Manager, Attacker, user.
2. Create 2 groups with the Manager account.
3. Invite the Attacker user to group A.
4. From attacker accepts the invitation and sends the request to the repeater.
5. Back to the manager Account and invite the user to group B.
6. Back to the repeater and add one digit to c2mId.
7. Go to the attacker account and see group B.

As a manager I created 2 different groups, Group-AAAA & Group-BBBB and both were private so other users were unable to leave comments and create topics, etc.

I invited the attacker to Group-AAAA to show you the flow of accepting and saving the request to the Burp repeater. So the attacker has access to Group-AAAA. The manager invited another user to Group-BBBB, but the attacker did not invite them to this group.

the attacker increased one to the c2mId value parameter and sent the request. Now the attacker refresh my group’s Page. The attacker of our story has access to Group-BBBB and can leave comments create topics etc. :D I should note that the value of c2mId is not one use. Even if a normal user accepts the innovation attacker can use this value again to access the groups.

Press enter or click to view image in full size

![]()

[Idor](https://medium.com/tag/idor?source=post_page-----406eb9e463a3---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----406eb9e463a3---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----406eb9e463a3---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--406eb9e463a3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--406eb9e463a3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--406eb9e463a3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--406eb9e463a3---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--406eb9e463a3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![M7arm4n](https://miro.medium.com/v2/resize:fill:96:96/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---post_author_info--406eb9e463a3---------------------------------------)

[![M7arm4n](https://miro.medium.com/v2/resize:fill:128:128/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---post_author_info--406eb9e463a3---------------------------------------)

[## Written by M7arm4n](https://m7arm4n.medium.com/?source=post_page---post_author_info--406eb9e463a3---------------------------------------)

[1.3K followers](https://m7arm4n.medium.com/followers?source=pos...