---
title: How i earned easy$$$ by deleting user comments on any post
url: https://infosecwriteups.com/how-i-earned-easy-by-deleting-user-comments-on-any-post-c2e226f2157a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-15
fetch_date: 2025-10-06T19:18:00.684799
---

# How i earned easy$$$ by deleting user comments on any post

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc2e226f2157a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-easy-by-deleting-user-comments-on-any-post-c2e226f2157a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-easy-by-deleting-user-comments-on-any-post-c2e226f2157a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c2e226f2157a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c2e226f2157a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How i earned easy$$$ by deleting user comments on any post

[![Le_Merdien](https://miro.medium.com/v2/resize:fill:64:64/1*CeE1IodVxgA1odlLUoFTfQ.jpeg)](https://medium.com/%40shadykhaled2002?source=post_page---byline--c2e226f2157a---------------------------------------)

[Le\_Merdien](https://medium.com/%40shadykhaled2002?source=post_page---byline--c2e226f2157a---------------------------------------)

3 min read

·

Nov 8, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

Hello everyone , i wanted to share with you one of my easiest findings that can make you $$ easily . So lets talk briefly about the program that i was hunting on to give you the big picture . Its like a shopping program and you can share these items with other users or friends by a link so when you share it between your group you create a post on this item something like this in following picture .

![]()

sharing the item create a post visible between the people you shared with.

At the begging i tried accessing the post without have a link or permission by simply creating a post from the “Attackers” account and change the method endpoint to GET and remove the parameter from the request and try to access the post details without any link or invitation to the post

Press enter or click to view image in full size

![]()

Attacker created a post on his account by sharing it with anyone

Then after changing the “POST” to “GET” and remove the parameters in the body and swap the post ID in url :its the number after the V1 by the victims post ID i accessed the post details and it worked fine a simple IDOR but then i tried to delete the users comments and likes from the post and the only one who can delete them is the one who shared the post he is like the admin of the post because he is one who shared the link . So i posted a comment from the attacker account on his own post not the victim post then delete it to capture the request

Press enter or click to view image in full size

![]()

post on the attacker account

so i swap the comment ID by the victims ID from the previous request because i have now all the data in post from the GET request so i swapped the comment ID of victim and change the post ID by victims post ID and managed to delete the comments on the post without having the admins permission and i tried also deleting the likes on the post by same way and it worked just fine the only thing the returned to 403 forbidden is deleting the post itself . So as you can see this a simple chains of IDORS that almost broke a whole functionality by simply switching IDs . I wanted to share my experience with you and if reached till here … Thank you and i hope you learned something new.

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----c2e226f2157a---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c2e226f2157a---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----c2e226f2157a---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----c2e226f2157a---------------------------------------)

[Hacker](https://medium.com/tag/hacker?source=post_page-----c2e226f2157a---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c2e226f2157a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c2e226f2157a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c2e226f2157a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c2e226f2157a---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--c2e226f2157a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Le_Merdien](https://miro.medium.com/v2/resize:fill:96:96/1*CeE1IodVxgA1odlLUoFTfQ.jpeg)](https://medium.com/%40shadykhaled2002?source=post_page---post_author_info--c2e226f2157a---------------------------------------)

[![Le_Merdien](https://miro.medium.com/v2/resize:fill:128:128/1*CeE1IodVxgA1odlLUoFTfQ.jpeg)](https://medium.com/%40shadykhaled2002?source=post_page---post_author_info--c2e226f2157a---------------------------------------)

[## Written by Le\_Merdien](https://medium.com/%40shadykhaled2002?source=post_page---post_author_info--c2e226f2157a---------------------------------------)

[65 followers](https://medium.com/%40shadykhaled2002/followers?source=post_page---post_author_info--c2e226f2157a---------------------------------------)

·[9 following](https://medium.com/%40shadykhaled2002/following?source=post_page---post_author_info--c2e226f2157a---------------------------------------)

Jr penetration tester and bug bounty hunter

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----c2e226f2157a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c2e226f2157a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c2e226f2157a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c2...