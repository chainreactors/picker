---
title: Privilege Escalation Using SCIM Provisioning
url: https://infosecwriteups.com/privilege-escalation-using-scim-provisioning-ca61ed9606bd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-11
fetch_date: 2025-10-06T17:16:19.176155
---

# Privilege Escalation Using SCIM Provisioning

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fca61ed9606bd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fprivilege-escalation-using-scim-provisioning-ca61ed9606bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fprivilege-escalation-using-scim-provisioning-ca61ed9606bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ca61ed9606bd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ca61ed9606bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Privilege Escalation Using SCIM Provisioning

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:64:64/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---byline--ca61ed9606bd---------------------------------------)

[Ronak Patel](https://ronak-9889.medium.com/?source=post_page---byline--ca61ed9606bd---------------------------------------)

3 min read

·

Jan 5, 2024

--

1

Listen

Share

Hi Fellow Hackers!!!

Happy New Year!!!

This Write-Up is about the same program i mentioned in my another article “[https://medium.com/@ronak-9889/admin-account-takeover-ab7535fe0fdb](https://medium.com/%40ronak-9889/admin-account-takeover-ab7535fe0fdb)”

As mentioned in that write-up this program introduced new feature called “Custom role” which allows admin to create user with custom permissions. One of the permission which could be assigned was “Access to security section”

Press enter or click to view image in full size

![]()

As seen above Imagine Admin has created user with the custom role which has only “access to security section” admin permission.

As seen in below screenshot admin has created custom role “test scim ” and assigned it to user “james parker”.

Press enter or click to view image in full size

![]()

Security section of this application was containing feature “SCIM provisioning” which allows to create,update,delete user data through Identity Provider.

Press enter or click to view image in full size

![]()

Those who are not familiar with SCIM , I am referring below link to understand the concept

[## SCIM

### System for Cross-domain Identity Management. Understand the the value of provisioning accounts with SCIM and how to set…

developer.okta.com](https://developer.okta.com/docs/concepts/scim/?source=post_page-----ca61ed9606bd---------------------------------------)

There were many identity provider options available but i used OKTA to test this.

To complete the setup one need to generate SCIM provisioning URL and Token as per screenshot below and provide it at the identity provider end(OKTA).

![]()

There is already our application available to add at OKTA to enable SCIM as below screenshot. For the privacy concern i am hiding the app name but mentioning the steps needed at the identity provider end(OKTA)

Press enter or click to view image in full size

![]()

After Installing this app at OKTA we need to Enable SCIM provisioning by providing SCIM provisioning URL and TOKEN generated at our target URL in previous steps.

Press enter or click to view image in full size

![]()

For the detailed guide about setting up scim integration please refer below link

[## Build a SCIM provisioning integration overview

### Use this guide to learn about the steps required to build an Okta integration that uses SCIM to handle user…

developer.okta.com](https://developer.okta.com/docs/guides/scim-provisioning-integration-overview/main/?source=post_page-----ca61ed9606bd---------------------------------------)

After finishing above setup our user with the the custom role “test scim” could create user at OKTA and which would be updated at our target.

Everything is fine till now. The BUG here is using this user with the custom role we could enable SCIM provisioning and create user at identity provider(OKTA) with the User Type attribute “ADMIN” and assign it to our application as per below screenshot

Press enter or click to view image in full size

![]()

We created USER with same email and username we mentioned above “James parker” which has custom role at target. BUT At Identity Provider we set the User Type “ADMIN” as shown above.

Our Existing User at target got updated as Admin and got the full access as shown below.

Press enter or click to view image in full size

![]()

In Summary, With access to only security section of admin, we integrated SCIM and created same user at Identity Provider with Admin User type attribute. As SCIM has more precedence than target Our user got updated as per Identity Provider attribute and got the FULL access. (Admin.)

Thanks for reading. Hope this was informative.

[Privilege Escalation](https://medium.com/tag/privilege-escalation?source=post_page-----ca61ed9606bd---------------------------------------)

[Access Control](https://medium.com/tag/access-control?source=post_page-----ca61ed9606bd---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ca61ed9606bd---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----ca61ed9606bd---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----ca61ed9606bd---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ca61ed9606bd---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ca61ed9606bd---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ca61ed9606bd---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ca61ed9606bd---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--ca61ed9606bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ronak Pat...