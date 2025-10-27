---
title: Phishing or What?? How I Got Access to the Internal Email of a Company
url: https://infosecwriteups.com/phishing-or-what-how-i-got-access-to-the-internal-email-of-a-company-a098fb08728?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-02
fetch_date: 2025-10-06T17:42:31.758367
---

# Phishing or What?? How I Got Access to the Internal Email of a Company

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa098fb08728&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fphishing-or-what-how-i-got-access-to-the-internal-email-of-a-company-a098fb08728&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fphishing-or-what-how-i-got-access-to-the-internal-email-of-a-company-a098fb08728&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a098fb08728---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a098fb08728---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Phishing or What?? How I Got Access to the Internal Email of a Company

[![whit3ros3](https://miro.medium.com/v2/resize:fill:64:64/1*2J9Dr5hsmPXG3IuVU4C3VA.jpeg)](https://medium.com/%40jay_rana?source=post_page---byline--a098fb08728---------------------------------------)

[whit3ros3](https://medium.com/%40jay_rana?source=post_page---byline--a098fb08728---------------------------------------)

4 min read

·

Jul 1, 2024

--

1

Listen

Share

Press enter or click to view image in full size

![]()

> **Introduction**

Hey guys, good to have you back on my blog. This is a bug that I found last September, but this vulnerability was a different one. Though not a very severe one, as it was marked as low, believe me, it was a very interesting one as I had a lot of fun after discovering this bug.

So in this vulnerability I was able to send emails to anyone in the world with a real, valid internal email of an ecommerce company. This was a fun experience and I just wanted to share with you all, about this easy to find but interesting bug.

> **Tip of the blog : Make notes**

I’ve adopted a new technique that’s really paying off, and I’d like to share it with you all. What I do is grab a sticky note, place it beside my trackpad, and use it to jot down important points while testing a website.

Press enter or click to view image in full size

![]()

my sticky note at that time

> **Let’s get started**

So, another day, another bug, another story!!!

Once again, I found myself testing an e-commerce site, which I’ll refer to as “*redacted.com*”.
Learning from my past newbie’s experience, I made sure to explore all the functionalities the site had to offer and also noted down all those that appeared potentially vulnerable, with the intention of testing them further later on. These included the admin login page, user profiles, the contact us form, and even the supplier portal.

> **Rediscovering the ‘Contact Us’ Form**

After not being able to find any bugs for like few hours, I went back to my notes to review what I had tested and what I might have missed.
That’s when I noticed the ‘Contact Us’ form, which I had completely forgotten about.

So I decided to give it a shot and tested it. Just as I captured the request after filling in all the details, I noticed something out-of-the-box.
There were keys named “to”, “from”, “subject”, “html”!!!!

Press enter or click to view image in full size

![]()

email request (left) & actual email (right)

And yes you guessed it right, I could change their values, and a check was only applied on the “from” param.
So now, I could mail anything to anyone from a mail that belongs to the company I was testing.

Felt like Elliot

And the most interesting thing was that in the “html” all the html tags were working, so I was able to customize the email body however I want, can add links, icons, buttons, anything at all.
So I copy pasted the whole structure of what the real email from that company looks like and added malicious links to it.

Now, just imagine a scenario where you receive an email like this, but it’s from a hacker.

Press enter or click to view image in full size

![]()

an actual email formed by me with phishing link embedded in download button

Fascinating but potentially dangerous!!!!!

I created a report and submitted it on HackerOne. After a few hours, I got a reply and the severity was downgraded to low. I had originally marked it as ‘High’, though.

I researched some more and learned about the service they were using to send emails. I discovered some new parameters, most of which were not that interesting, like “cc” and “bcc”. However, I found out that we could also add attachments to the emails.

I added a few more comments to the report, showing them all the possibilities with this vulnerability. In the end, this convinced them to raise the severity to ‘Medium’, which was good enough for me.

![]()

> Fun Part

Now comes the most fun part of this experience. It felt like I had a lot of power in my hands, which I knew how to use, until the bug was resolved.😈😈😈.

I created a well-structured email, taking care of every minute detail. And this was the result!

![]()

a perfectly crafted email and sent via internal email of the company

Finding this vulnerability was worth my efforts, and I realized this when I sent the email to a friend of mine.😈😈😈

And to satisfy your curiosity about what was inside that assessment link, here is the [link](https://www.youtube.com/shorts/SXHMnicI6Pg)

See you in the next blog!😉😉

[Hacking](https://medium.com/tag/hacking?source=post_page-----a098fb08728---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----a098fb08728---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----a098fb08728---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----a098fb08728---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----a098fb08728---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a098fb08728---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a098fb08728---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a098fb08728---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a098fb08728---------------------------------------)

·[Last published 2 hours ago](/baby-...