---
title: How to spoof e-mails. (DMARC, SPF, and Phishing)
url: https://infosecwriteups.com/how-to-spoof-e-mails-dmarc-spf-and-phishing-5184c10679a0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-16
fetch_date: 2025-10-04T03:59:23.719108
---

# How to spoof e-mails. (DMARC, SPF, and Phishing)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5184c10679a0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-spoof-e-mails-dmarc-spf-and-phishing-5184c10679a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-spoof-e-mails-dmarc-spf-and-phishing-5184c10679a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5184c10679a0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5184c10679a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How to spoof e-mails. (DMARC, SPF, and Phishing)

[![popalltheshells](https://miro.medium.com/v2/resize:fill:64:64/1*-b6WuCfmjt3_kUbryMzqvw.jpeg)](https://popalltheshells.medium.com/?source=post_page---byline--5184c10679a0---------------------------------------)

[popalltheshells](https://popalltheshells.medium.com/?source=post_page---byline--5184c10679a0---------------------------------------)

3 min read

·

Jan 26, 2022

--

1

Listen

Share

***Note: sanitization of these screenshots was performed to protect the identities of stakeholders involved.***

On my most recent learning, I discovered that missing DMARC policy is not something that you should take lightly. If your organization does not have that implemented, I strongly suggest that you do so. DMARC (Domain-based Message Authentication, Reporting, and Comformance) is responsible to ensure that your organization’s domain cannot be spoofed to craft malicious messages.

For more information about DMARC: <https://dmarc.org/>

Below is the step-by-step tutorial on what I did to be able to send a spoofed phishing e-mail to my client. **Please note** that in order for a higher chance of success, this phishing is best used if the client has [SPF](https://www.dmarcanalyzer.com/spf/) (Sender Policy Framework) soft-policy or no-policy configured. Otherwise it might just go to SPAM. Use the [SPF checker](https://www.dmarcanalyzer.com/spf/checker/) to determine if this policy is configured on the target domain.

1. You have to find out whether the domain target has their DMARC policy configured or not. In order to do this, you can simply use a website such as [MXtoolbox](https://mxtoolbox.com/dmarc.aspx?gclid=CjwKCAiAxJSPBhAoEiwAeO_fP1e82z8tWZbGR9-94MOzqetFa5BgVwc8qhK0jzaOYF0Zk3fbfVRiuxoCGIQQAvD_BwE)

Press enter or click to view image in full size

![]()

2. Before you can send an e-mail from your Kali, you would have to install sendmail. You can do this by using the following command: ***sudo apt-get install sendmail***

3. Start the sendmail service using **systemctl**

4. Craft your spoofed e-mail. Here, I am using python3 — so on your Linux terminal, type “python3”. Here is an example of my spoofed phishing e-mail requesting for a sensitive document to be sent.

Press enter or click to view image in full size

![]()

Let’s break this down.

* First we import the necessary **libraries**
* Next we declare a **msg** variable as “EmailMessage”.
* **E-mail body** is the content of the e-mail
* We then set the **MIMEText** so that the HTML tags you included in your e-mail content will be rendered
* Then you set the **Subject** of the e-mail
* The **priority** is optional, but this is what shows the “!” sign to show some urgency
* **Msg[“To”]** = your target
* **msg[“From”]** = the e-mail you want to spoof or impersonate
* ‘**CC**’ = the e-mail CC’ed when the target clicks “reply all”
* ‘**reply-to**’ = the e-mail that the target will reply to when they click “reply” (You can use your own e-mail here). I would recommend not using this if you want it to be less obvious that it’s phishing. If you don’t use this, your best bet is for the target to “reply-all” — in which case both the victim and you will receive the replies (because of the CC parameter). This will raise suspicion if the victim says “Hey I never sent this”, but by that time, you will already have your temporary account or documents you requested.
* Set the SMTP server as “localhost” (default if you use sendmail)
* Send the message

Once the message is sent, it will take a few minutes before it gets delivered to the target. In my case, I received the following e-mail after a successful launch.

Press enter or click to view image in full size

![]()

Pretty awesome attack vector if you ask me. See how missing DMARC and SPF policies can be dangerous?

**IMPACT**: Attacker may be able to leverage this attack vector to send e-mails to your customers or other staff members within the company. This action may have negative financial, reputational, and operational impact on the organization.

[Phishing](https://medium.com/tag/phishing?source=post_page-----5184c10679a0---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----5184c10679a0---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----5184c10679a0---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----5184c10679a0---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----5184c10679a0---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5184c10679a0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5184c10679a0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5184c10679a0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5184c10679a0---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--5184c10679a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![popalltheshells](https://miro.medium.com/v2/...