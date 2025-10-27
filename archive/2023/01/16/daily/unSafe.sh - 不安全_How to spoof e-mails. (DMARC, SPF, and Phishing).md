---
title: How to spoof e-mails. (DMARC, SPF, and Phishing)
url: https://buaq.net/go-145654.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:36.037504
---

# How to spoof e-mails. (DMARC, SPF, and Phishing)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

How to spoof e-mails. (DMARC, SPF, and Phishing)

Note: sanitization of these screenshots was performed to protect the identities of stakeholders invo
*2023-1-15 23:52:55
Author: [infosecwriteups.com(查看原文)](/jump-145654.htm)
阅读量:15
收藏*

---

***Note: sanitization of these screenshots was performed to protect the identities of stakeholders involved.***

On my most recent learning, I discovered that missing DMARC policy is not something that you should take lightly. If your organization does not have that implemented, I strongly suggest that you do so. DMARC (Domain-based Message Authentication, Reporting, and Comformance) is responsible to ensure that your organization’s domain cannot be spoofed to craft malicious messages.

For more information about DMARC: <https://dmarc.org/>

Below is the step-by-step tutorial on what I did to be able to send a spoofed phishing e-mail to my client. **Please note** that in order for a higher chance of success, this phishing is best used if the client has [SPF](https://www.dmarcanalyzer.com/spf/) (Sender Policy Framework) soft-policy or no-policy configured. Otherwise it might just go to SPAM. Use the [SPF checker](https://www.dmarcanalyzer.com/spf/checker/) to determine if this policy is configured on the target domain.

1. You have to find out whether the domain target has their DMARC policy configured or not. In order to do this, you can simply use a website such as [MXtoolbox](https://mxtoolbox.com/dmarc.aspx?gclid=CjwKCAiAxJSPBhAoEiwAeO_fP1e82z8tWZbGR9-94MOzqetFa5BgVwc8qhK0jzaOYF0Zk3fbfVRiuxoCGIQQAvD_BwE)

2. Before you can send an e-mail from your Kali, you would have to install sendmail. You can do this by using the following command: ***sudo apt-get install sendmail***

3. Start the sendmail service using **systemctl**

4. Craft your spoofed e-mail. Here, I am using python3 — so on your Linux terminal, type “python3”. Here is an example of my spoofed phishing e-mail requesting for a sensitive document to be sent.

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

Pretty awesome attack vector if you ask me. See how missing DMARC and SPF policies can be dangerous?

**IMPACT**: Attacker may be able to leverage this attack vector to send e-mails to your customers or other staff members within the company. This action may have negative financial, reputational, and operational impact on the organization.

文章来源: https://infosecwriteups.com/how-to-spoof-e-mails-dmarc-spf-and-phishing-5184c10679a0?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)