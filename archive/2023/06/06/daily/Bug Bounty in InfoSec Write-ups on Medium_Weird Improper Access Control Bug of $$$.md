---
title: Weird Improper Access Control Bug of $$$
url: https://infosecwriteups.com/weird-improper-access-control-bug-of-9cbceb8e039f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-06-06
fetch_date: 2025-10-04T11:47:11.672682
---

# Weird Improper Access Control Bug of $$$

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9cbceb8e039f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweird-improper-access-control-bug-of-9cbceb8e039f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweird-improper-access-control-bug-of-9cbceb8e039f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9cbceb8e039f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9cbceb8e039f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Weird Improper Access Control Bug of $$$

[![Ankit Joshi](https://miro.medium.com/v2/resize:fill:64:64/1*mNkwtGKKuj4IoFNPu7ahcg.jpeg)](https://medium.com/%40anksec?source=post_page---byline--9cbceb8e039f---------------------------------------)

[Ankit Joshi](https://medium.com/%40anksec?source=post_page---byline--9cbceb8e039f---------------------------------------)

3 min read

·

May 29, 2023

--

1

Listen

Share

Hello , So I am back with another write up . This one is about an Improper access control issue which I have found in a famous website which is used to create projects and collaborate with different users . Let’s see this in detail .

Press enter or click to view image in full size

![]()

### **Description**

I am testing a website that contains three user roles: owner, admin and normal user (which can only read and write). Let’s refer to the company as ‘Private’ (as the report has not yet been disclosed).

I have created a project for myself with my email: email1, so I am the owner of the project. Now, I invited my second email: email2, with admin privileges. I tried to remove the owner, become the owner, etc. from my admin’s account but all attempts failed.

Finally, I thought to check for similar issues through a normal user perspective . I invited my third email: email3 from admin’s account . I checked whether the owner can see that I invited someone or not, and it turns out the owner can see that I invited another user into the project, and the owner can also delete the invite.

Also I checked every other basic issues like becoming owner/admin , removing admin , etc but not able to find anything useful.

![]()

After spending nearly 3–4 hours, I was not able to find anything interesting . Finally I thought , what if I invite someone whose account does not exist ? So I invited my other email address into the project i.e email4, and the account of email4 does not exist. To my surprise, the owner is not able to see that I invited email4 into the project. If the email4 user creates an account and accept the invite, then only the owner can see that user.

Now I can invite any other user as an admin without the owner seeing it.

But now you may think that what is the benefit of inviting another user if you are already an admin ? Let me explain this in more detail.

**Impact**

So as this is a project sharing website , it contains confidential information which should not be seen by any outsider . Now if owner removes admin (attacker) from the project due to any reason , then admin can rejoin the project by using the older invite link which is sent to email4 (which is non-expirable) . Similarly again attacker can invite new emails and keeps on joining every time and there is no way to stop this, except for deleting the project .

Due to this issue, confidential information can get leaked .

This bug was accepted as medium severity as it requires higher privileges to initiate this attack . After 2–3 weeks, I received $$$ for submitting this bug .

I hope you can learn something new with this . Thank you for your time!!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----9cbceb8e039f---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----9cbceb8e039f---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----9cbceb8e039f---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9cbceb8e039f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9cbceb8e039f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9cbceb8e039f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9cbceb8e039f---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--9cbceb8e039f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ankit Joshi](https://miro.medium.com/v2/resize:fill:96:96/1*mNkwtGKKuj4IoFNPu7ahcg.jpeg)](https://medium.com/%40anksec?source=post_page---post_author_info--9cbceb8e039f---------------------------------------)

[![Ankit Joshi](https://miro.medium.com/v2/resize:fill:128:128/1*mNkwtGKKuj4IoFNPu7ahcg.jpeg)](https://medium.com/%40anksec?source=post_page---post_author_info--9cbceb8e039f---------------------------------------)

[## Written by Ankit Joshi](https://medium.com/%40anksec?source=post_page---post_author_info--9cbceb8e039f---------------------------------------)

[53 followers](https://medium.com/%40anksec/followers?source=post_page---post_author_info--9cbceb8e039f---------------------------------------)

·[6 following](https://medium.com/%40anksec/following?source=post_page---post_author_info--9cbceb8e039f---------------------------------------)

Bug Hunter | CTF Player | Learner

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----9cbceb8e039f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9cbceb8e039f---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9cbceb8e039f---------------------------------------)

[Car...