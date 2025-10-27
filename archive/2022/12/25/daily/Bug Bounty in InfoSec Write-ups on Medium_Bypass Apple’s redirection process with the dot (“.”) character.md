---
title: Bypass Apple’s redirection process with the dot (“.”) character
url: https://infosecwriteups.com/bypass-apples-redirection-process-with-the-dot-character-c47d40537202?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-25
fetch_date: 2025-10-04T02:29:23.980633
---

# Bypass Apple’s redirection process with the dot (“.”) character

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc47d40537202&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypass-apples-redirection-process-with-the-dot-character-c47d40537202&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypass-apples-redirection-process-with-the-dot-character-c47d40537202&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c47d40537202---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c47d40537202---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypass Apple’s redirection process with the dot (“.”) character

[![can1337](https://miro.medium.com/v2/resize:fill:64:64/1*HgWum8hST4CDGwBkdXjy-A.jpeg)](https://canmustdie.medium.com/?source=post_page---byline--c47d40537202---------------------------------------)

[can1337](https://canmustdie.medium.com/?source=post_page---byline--c47d40537202---------------------------------------)

3 min read

·

Dec 24, 2022

--

2

Listen

Share

Hi guys, I have been gone for a while but now I’m back and here is a new write-up post. Today, I’m gonna show you the Open Redirection vulnerability I found at Apple’s subdomain using the dot character.

I don’t have a permission to publish this subdomain so I won’t publish it but you can think it as a forum area where users are active. So I’ll call it as “redacted” and let’s get started!

First of all, when we visit to the redacted.apple.com subdomain, there is a login screen here and logging in is quite simple.

Press enter or click to view image in full size

![]()

As you can see in the picture, the *?path=* parameter is set to redirect to another page in the same subdomain in the section for choosing a nickname for users who log in for the first time.

This process will probably be redirected to “/welcome?login=true” for first time users after all prerequisites have been completed correctly.

As I guessed, the redirect was redirecting to the specified page after choosing the username and uploading the avatar. Of course I tried some payloads here primarily like https://evil.com & //evil.com etc.

Press enter or click to view image in full size

![]()

Actually, what was interesting to me here was that after using the //evil.com payload, the response was /evil.com with a single ‘/’ character.
If you are using a payload like ?path=//evil.com then the following is expected: redacted.apple.com//evil.com
However, the response I got is as follows: redacted.apple.com/evil.com

Press enter or click to view image in full size

![]()

In this case, I thought the only ‘/’ appended to the end was due to my payload, and I thought of just typing evil.com

The behavior I actually expected was to be redirected to a non-existent redacted.apple.comevil.com domain, but instead I returned to “/welcome?login=true”. For most parameters it would be okay to simply navigate to evil.com in the subdomain. (?path=evil.com > x.apple.com/evil.com)

Finally an idea came to my mind and I hadn’t seen it anywhere before. I was thinking purely theoretically and was surprised to see that it was possible at Apple.

Press enter or click to view image in full size

![]()

If we set the payload to .evil.com (ie ?path=.evil.com), “.” character will be appended to the end of redacted.apple.com and this making it a subdomain of evil.com.

Press enter or click to view image in full size

![]()

And here is the result we expect. Adding a dot character in front of the payload means that the “/” character is missing in some cases. This makes redacted.apple.com a subdomain of evil.com

Press enter or click to view image in full size

![]()

<https://support.apple.com/en-us/HT201536>

This vulnerability was fixed by team and I was added the Apple Hall of Fame.

That’s all for now. Thanks for reading this far and I hope you liked it!

You can follow me on twitter: <https://twitter.com/canmustdie>

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c47d40537202---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----c47d40537202---------------------------------------)

[Apple](https://medium.com/tag/apple?source=post_page-----c47d40537202---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----c47d40537202---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c47d40537202---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c47d40537202---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c47d40537202---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c47d40537202---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--c47d40537202---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![can1337](https://miro.medium.com/v2/resize:fill:96:96/1*HgWum8hST4CDGwBkdXjy-A.jpeg)](https://canmustdie.medium.com/?source=post_page---post_author_info--c47d40537202---------------------------------------)

[![can1337](https://miro.medium.com/v2/resize:fill:128:128/1*HgWum8hST4CDGwBkdXjy-A.jpeg)](https://canmustdie.medium.com/?source=post_page---post_author_info--c47d40537202---------------------------------------)

[## Written by can1337](https://canmustdie.medium.com/?source=post_page---post_author_info--c47d40537202---------------------------------------)

[1.2K followers]...