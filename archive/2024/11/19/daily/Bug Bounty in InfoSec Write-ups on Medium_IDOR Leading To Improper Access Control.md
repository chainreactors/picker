---
title: IDOR Leading To Improper Access Control
url: https://infosecwriteups.com/idor-leading-to-improper-access-control-c3999aa28fc4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-19
fetch_date: 2025-10-06T19:16:35.304521
---

# IDOR Leading To Improper Access Control

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc3999aa28fc4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-leading-to-improper-access-control-c3999aa28fc4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fidor-leading-to-improper-access-control-c3999aa28fc4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c3999aa28fc4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c3999aa28fc4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# IDOR Leading To Improper Access Control

[![Le_Merdien](https://miro.medium.com/v2/resize:fill:64:64/1*CeE1IodVxgA1odlLUoFTfQ.jpeg)](https://medium.com/%40shadykhaled2002?source=post_page---byline--c3999aa28fc4---------------------------------------)

[Le\_Merdien](https://medium.com/%40shadykhaled2002?source=post_page---byline--c3999aa28fc4---------------------------------------)

2 min read

·

Nov 5, 2024

--

2

Listen

Share

Press enter or click to view image in full size

![]()

Hello guys , I wanted to share with an easy finding that I found on a website to give the full picture this website Is about selling gifts like mugs and photobooks and etc…..

So first so to comes in mind while hunting for IDORS is how can I do an improper action like for example : If I’m on a program that has various privileges like a user and an admin and the admin the can create a group and invite users in it and only admin can approve or remove user so first thing comes in my mind how a user can do the admin action without his permission can be called “privilege escalation” or “Improper access control” in this bug I found an improper access control normal

So as I said it’s a gift shop application. so first thing comes to my mind is trying the shopping cart endpoint so i created 2 accounts one for the “Victim” and other for the “Attacked” I added to something on victims cart and i tried so switch the ID of the attacker by the ID of victim and see if i can something on his cart but i failed a 403 pop up so i tried to get a GET request to see if a can view the victims cart by switching the IDs in the endpoint and i got the same result then i found another functionality called favorites is by adding any item to my favorite so i tried the same methodology but on the my favorites i added an item the victims cart the i captured the request .

Press enter or click to view image in full size

![]()

So as you can see visitors ID its the user id and the product code its the item id so i simply just swap the attacker ID by the victims ID and i added something on his favorites and it worked ….. so i tried to change the endpoint method and see if can DELETE items from the victims account without his permission and its also worked …. so as you can see its simple IDOR the can lead to an improper access control and if reached till this point ….. Thank you hope you learned something new.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c3999aa28fc4---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----c3999aa28fc4---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----c3999aa28fc4---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----c3999aa28fc4---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c3999aa28fc4---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c3999aa28fc4---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c3999aa28fc4---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c3999aa28fc4---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--c3999aa28fc4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Le_Merdien](https://miro.medium.com/v2/resize:fill:96:96/1*CeE1IodVxgA1odlLUoFTfQ.jpeg)](https://medium.com/%40shadykhaled2002?source=post_page---post_author_info--c3999aa28fc4---------------------------------------)

[![Le_Merdien](https://miro.medium.com/v2/resize:fill:128:128/1*CeE1IodVxgA1odlLUoFTfQ.jpeg)](https://medium.com/%40shadykhaled2002?source=post_page---post_author_info--c3999aa28fc4---------------------------------------)

[## Written by Le\_Merdien](https://medium.com/%40shadykhaled2002?source=post_page---post_author_info--c3999aa28fc4---------------------------------------)

[65 followers](https://medium.com/%40shadykhaled2002/followers?source=post_page---post_author_info--c3999aa28fc4---------------------------------------)

·[9 following](https://medium.com/%40shadykhaled2002/following?source=post_page---post_author_info--c3999aa28fc4---------------------------------------)

Jr penetration tester and bug bounty hunter

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c3999aa28fc4---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c3999aa28fc4---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c3999aa28fc4---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c3999aa28fc4---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c3999aa28fc4---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c3999aa28fc4---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c3999aa28fc4---------------------------------------)

[Terms]...