---
title: Did you know you can earn bounties using Discord?
url: https://infosecwriteups.com/did-you-know-you-can-earn-bounty-using-discord-1e8eb79aa260?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-06-06
fetch_date: 2025-10-04T11:47:06.037184
---

# Did you know you can earn bounties using Discord?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1e8eb79aa260&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdid-you-know-you-can-earn-bounty-using-discord-1e8eb79aa260&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdid-you-know-you-can-earn-bounty-using-discord-1e8eb79aa260&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1e8eb79aa260---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1e8eb79aa260---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Did you know you can earn bounties using Discord?

[![Alp](https://miro.medium.com/v2/resize:fill:64:64/1*9kxmYKIuxivc2VHWr9rzlQ.jpeg)](https://medium.com/%40alp0x01?source=post_page---byline--1e8eb79aa260---------------------------------------)

[Alp](https://medium.com/%40alp0x01?source=post_page---byline--1e8eb79aa260---------------------------------------)

4 min read

·

Jun 4, 2023

--

2

Listen

Share

Hi folks. This is Alp. I haven’t been here for a long time (again). I remembered that I have a Medium account. As you can see in the title, will show a bug with Discord in this post.

I ensure everyone knows the Discord but want to be sure everyone really knows.

## So, what’s the Discord?

Press enter or click to view image in full size

![]()

Discord is an American VoIP and instant messaging social platform. Users have the ability to communicate with voice calls, video calls, text messaging, media, and files in private chats or as part of communities called “servers”.

The number of people who use Discord monthly has rapidly expanded from 10 million in 2017 to an estimated 196.2 million users this year. Discord is used by a lot of people ([even the Ukraine military](https://twitter.com/clashreport/status/1641499841116135425)). We can include many official companies in this.

Discord offers this exclusive thing for the servers:

* Custom Invite Link

Thanks to the custom invite link, you can add any text you want to the end of the “discord.com/invite/<here>” prefix and invite people to your server with this vanity invite link. To use that you should boost 14 times your server.

I found a program as a target on HackerOne that is a private program and has built a community on Discord as well.

They have a custom invite link. We can call it “customlink”.

Then, I went to the scope page of the private program. There was a domain in the scope named “target.com”. And when I entered that domain there was an invitation to their Discord server in the footer section. The issue starts here.

I noticed they used their custom invite link in their footer.

Press enter or click to view image in full size

![]()

So, I started to check the Discord invite link with automation. Because if any server member stops boosting the server, the server drops from 14 boosts because of this and the custom server link feature will become unusable. So, anyone can claim the custom invite URL. To boost a server 14 times cost $ 69,86. You can earn more by losing $68 (they give $250 for low-severity reports 😛). Also, sometimes Discord makes deals with third-party companies and gives free nitro to the users. So, you don‘t need to spend $68.)

![]()

Then, I got a notification about the server invite is no longer valid. So this means the server boost level dropped from 14 boosts. I took over the invite link and immediately sent a report to the team.

Press enter or click to view image in full size

![]()

If someone clicks on the Discord link on the target website, will be redirected to my Discord server.

Press enter or click to view image in full size

![]()

I’ve submitted this issue in two programs so far. One of them closed the report as resolved without giving a bounty and fixed the issue (there’s no way to appeal the decision. I respected the decision because the program was not managed by HackerOne).

Press enter or click to view image in full size

![]()

Usually, such a report should be awarded with a bounty. I know that not receiving this award is an exception. And I don’t mind.

And the other one is still in the pending state. In my opinion, this is definitely a serious issue and should be classified as a low/medium severity (depending on the program) issue. Because attackers can scam people and cause bad things by redirecting the Discord invite link from the website.

If you have a question regarding this or anything else to ask feel free to contact me via [Twitter](https://twitter.com/alp0x01) or the Medium comments.

Twitter: <https://twitter.com/alp0x01>

Thanks for reading, see ya!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----1e8eb79aa260---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----1e8eb79aa260---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----1e8eb79aa260---------------------------------------)

[Bugs](https://medium.com/tag/bugs?source=post_page-----1e8eb79aa260---------------------------------------)

[Hackerone](https://medium.com/tag/hackerone?source=post_page-----1e8eb79aa260---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e8eb79aa260---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e8eb79aa260---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1e8eb79aa260---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1e8eb79aa260---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--1e8eb79aa260---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Alp](https://miro.medium.com/v2/resize:fill:96:96/1*9kxmYKIuxivc...