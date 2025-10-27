---
title: Sensitive data leak using IDOR in integration service
url: https://infosecwriteups.com/sensitive-data-leak-using-idor-in-integration-service-d9301be9c91e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-11
fetch_date: 2025-10-06T17:16:21.514758
---

# Sensitive data leak using IDOR in integration service

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd9301be9c91e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsensitive-data-leak-using-idor-in-integration-service-d9301be9c91e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsensitive-data-leak-using-idor-in-integration-service-d9301be9c91e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d9301be9c91e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d9301be9c91e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Sensitive data leak using IDOR in integration service

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:64:64/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---byline--d9301be9c91e---------------------------------------)

[Ronak Patel](https://ronak-9889.medium.com/?source=post_page---byline--d9301be9c91e---------------------------------------)

4 min read

·

Dec 29, 2020

--

2

Listen

Share

Hello Guys! Hope you are doing well in this pandemic.

This write up is about Bug, Which I found in private program before six months and resolved before two months. As I mentioned in my previous blog posts, I go by functionality to hunt for Bugs. I loved this bug due to how simple IDOR could create a Huge impact if linked with the existing functionality.

As this bug was reported to private program, I won’t be able to disclose program name. I would mention it as Redacted.com throughout this blog post. For better understanding, I would just mention that it is an app to generate forms for surveys, quiz and more, collect responses from those forms as well as integrate with other services.

Mostly I look for Business logic, IDORs and server-side bugs while hunting. I don’t follow any predefined or fixed methodology but just go with some basic recon, Try to understand normal flow of application and then go for hunting.

This bug was in the integration functionality. First I would describe basic flow of this functionality and then I would go step by step how I found this bug. There was a section to connect form’s responses to different platforms like Google analytics, Facebook Pixels and more. Owner could integrate his/her form to one of this apps using this functionality and he could receive form responses in integrated app.

While I was going through all the platforms available to integrate, I came across with the option to integrate with Zendesk sell. Zendesk sell is the application to analyze sales data like leads, contacts and more. So the flow of this functionality was like once started integration process it takes the form id and transfers the request flow to the third party application where you would asked to configure your Zendesk sell account, grant authorization and map form’s questions with the fields in the Zendesk sell. Once this has been done successfully, Form’s responses would be mapped to the Zendesk sell’s fields.

Upon observing request flow, I found that First GET request to initiate integration was getting generated, then requests to third party to configure authentication and mapping and lastly PATCH request to enable the integration. Both GET and PATCH requests were vulnerable to IDOR in form\_id parameter.

I had two accounts created to test application, one as an attacker and another as a victim. As per below screenshot, I have started the integration, intercepted GET request and replaced form id to the victim’s form id.

Press enter or click to view image in full size

![]()

Victim form\_id

After replacing form id to victim’s ID, I turned off interception and got landed to authentication and mapping page.

I have configured Zendesk sell account as an attacker and granted authorization. As per below screenshot it fetched victim form’s questions to map with attacker’s Zendesk sell account fields.

Press enter or click to view image in full size

![]()

Zendesk sell authorization

Press enter or click to view image in full size

![]()

Mapping victim form’s questions to attacker’s Zendesk sell fields

After finishing this configuration, I have intercepted next request which was PATCH request to enable integration and replaced form id with victim’s form id .

Press enter or click to view image in full size

![]()

Enable integration

After finishing this integration process on attacker’s account. To check whether it worked or not, I logged in to the victim’s account and I found integration got enabled.

To test further, I filled up form as a visitor, checked response received in victim’s account and attacker’s Zendesk sell account. As per below screenshots attacker received form response in his Zendesk sell account.

Press enter or click to view image in full size

![]()

Contact has been created with victim form’s received response to attacker’s Zendesk sell account

The question is how to enumerate form ids to integrate forms with our Zendesk account. Enumeration was very simple task as Link for sharing this form contained form\_id value which we can use to integrate with our Zendesk account and simply receive all sensitive data being filled to those forms.

As per below screenshot, Simple google dork reveled form ids.

Press enter or click to view image in full size

![]()

Form id enumeration using google dork

Summing up, Using IDOR in this integration process, Attacker could integrate his Zendesk sell account with any form without any kind of user interaction and could fetch all Sensitive data received as a form response.

I hope this article was informative to you guys. Thanks for reading. Stay blessed Stay safe…..!!!!!!!!!!!!!!!!!!!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----d9301be9c91e---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----d9301be9c91e---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d9301be9c91e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d9301be9c91e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d9301be9c91e---------------------------------------)

[7...