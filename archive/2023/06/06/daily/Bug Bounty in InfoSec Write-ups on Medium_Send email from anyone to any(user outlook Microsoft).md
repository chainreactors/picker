---
title: Send email from anyone to any(user outlook Microsoft)
url: https://infosecwriteups.com/send-email-from-anyone-to-any-user-outlook-microsoft-69fce333066d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-06-06
fetch_date: 2025-10-04T11:47:03.094887
---

# Send email from anyone to any(user outlook Microsoft)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F69fce333066d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsend-email-from-anyone-to-any-user-outlook-microsoft-69fce333066d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsend-email-from-anyone-to-any-user-outlook-microsoft-69fce333066d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-69fce333066d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-69fce333066d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Send email from anyone to any(user outlook Microsoft)

[![Abbas.heybati](https://miro.medium.com/v2/resize:fill:64:64/1*JNrM4Cyp_7fI4XQ7cTS2hA.jpeg)](https://medium.com/%40abbasheybati1?source=post_page---byline--69fce333066d---------------------------------------)

[Abbas.heybati](https://medium.com/%40abbasheybati1?source=post_page---byline--69fce333066d---------------------------------------)

4 min read

·

Jun 3, 2023

--

5

Listen

Share

Hi guys

I was researching SMTP and mail server for some time.
I decided to start researching Microsoft Outlook.
When I went further and deepened my research, I realized that this vulnerability can exist on many mail servers.

> **That’s why I wrote this write-up so that (Bug hunters and Security researcher and Penetration testing) and even security defence teams will notice it.**

I will explain about the bug first
I have noticed a bug in SMTP and Mail server in Microsoft Exchange
That would allow me to send emails(Example: secure@microsoft.com or x@outlook.com) from anyone I want to anyone in user Outlook
That is, any email that was related to Microsoft

> **The point is that this could only be done from Outlook’s own e-mails, for example, it cannot be done from Gmail to Outlook.**

In the picture below, I sent myself an email from secure@microsoft.com

Press enter or click to view image in full size

![]()

I reported this vulnerability to Microsoft security experts and they fixed this bug

Press enter or click to view image in full size

![]()

Report bug to msrc.microsoft.com

OK
This was a summary of the vulnerability I found
Before I talk about vulnerability, I would like to show you how I got this vulnerability.

Before I started researching, I had no idea how to start, I just knew that I wanted to find a vulnerability on Mail Servers and I just started.

That’s why I went to read RFC 5321 to understand SMTP architecture well.

Press enter or click to view image in full size

![]()

After reading the RFC I went to find out what happens when an email is sent?

Press enter or click to view image in full size

![]()

And after this I realized that there are security mechanisms
For example, I researched DKIM and SPF again.
And in the end, with all the research I did, a question came to me, what happens if I connect directly with the Outlook server and try to send email through this server?

Press enter or click to view image in full size

![]()

**The bug started**

For this, I needed to find the main Outlook mail server first, which was not a complicated task

Press enter or click to view image in full size

![]()

Mail is handled by outlook-com.olc.protection.outlook.com

After I got the address of the mail server, I started connecting to it with telnet

Press enter or click to view image in full size

![]()

Telnet port 25

Well, for this you need to read about smtp commands
which is easily obtained by searching on Google

Press enter or click to view image in full size

![]()

As you can see in the photo above, I came, first I connected with the EHLO server and the server answered me.
Then I specified with **mail from** who I want to send the email from, here I wanted to send the email from secure@microsoft.com and the status 250 was returned to me OK
Then I specified to whom the email(**RCPT TO**) should be sent, here I put my email, and again the status returned to me was 250 OK.
And then I specified with data that I want to send a **data** (text).

Press enter or click to view image in full size

![]()

Tip “ **In order to understand how the server is behaving, be sure to read about the status codes**”

After specifying the source of the email and the destination of the email, I added my data to the email
(From/To/Subject)
And I added a text and body the end of the email with a dot
And here my email was successfully forwarded to my email from secure@microsoft.com.

![]()

successfully send

![]()

History email

And finally, I want to tell you another scenario(Another company) where I **bypassed SPF** using a technique

Press enter or click to view image in full size

![]()

In this scenario, it was very interesting to me that when I was sending the email, it did not allow me to send the email. I defined a Content-Type in the header and put a charset with ISO-8859–1 value for it.
I tested the charset section with different patterns until ISO-8859–1 worked and bypassed.

I hope this writeup has helped you :)

[twitter.com/abbas\_heybati](https://twitter.com/abbas_heybati)

[www.linkedin.com/in/abbas-heybati-76432220b](https://www.linkedin.com/in/abbas-heybati-76432220b/)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----69fce333066d---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----69fce333066d---------------------------------------)

[Security Research](https://medium.com/tag/security-research?source=post_page-----69fce333066d---------------------------------------)

[Security Researchers](https://medium.com/tag/security-researchers?source=post_page-----69fce333066d---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--69fce333066d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--69fce333066d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--69fce333066d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--69fce333066d---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-i...