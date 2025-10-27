---
title: Cloudflare partners with KnowBe4 to equip organizations with real-time security coaching to avoid phishing attacks
url: https://buaq.net/go-153983.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:31.333235
---

# Cloudflare partners with KnowBe4 to equip organizations with real-time security coaching to avoid phishing attacks

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

![](https://8aqnet.cdn.bcebos.com/f81ad29e4b36810c9ca33fa42b74150c.jpg)

Cloudflare partners with KnowBe4 to equip organizations with real-time security coaching to avoid phishing attacks

Loading...
*2023-3-17 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-153983.htm)
阅读量:19
收藏*

---

Loading...

* [![Ayush Kumar](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/11/Screen-Shot-2022-01-14-at-2.08.16-PM.png)](https://blog.cloudflare.com/author/ayush/)
* [![Deeksha Lamba](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/03/Deeksha-Lamba-1.jpg)](https://blog.cloudflare.com/author/deeksha/)

![Cloudflare partners with KnowBe4 to equip organizations with real-time security coaching to avoid phishing attacks ](https://blog.cloudflare.com/content/images/2023/03/image7-7.png)

Today, we are very excited to announce that Cloudflare’s cloud email security solution, Area 1, now integrates with KnowBe4, a leading security awareness training and simulated phishing platform. This integration allows mutual customers to offer real-time coaching to their employees when a phishing campaign is detected by Cloudflare’s email security solution.

We are all aware that phishing attacks often use email as a vector to deliver the fraudulent message. Cybercriminals use a range of tactics, such as posing as a trustworthy organization, using urgent or threatening language, or creating a sense of urgency to entice the recipient to click on a link or download an attachment.

Despite the increasing sophistication of these attacks and the solutions to stop them, human error remains the weakest link in this chain of events. This is because humans can be easily manipulated or deceived, especially when they are distracted or rushed. For example, an employee might accidentally click on a link in an email that looks legitimate but is actually a phishing attempt, or they might enter their password into a fake login page without realizing it. According to the 2021 Verizon Data Breach Investigations Report, phishing was the most common form of social engineering attack, accounting for 36% of all breaches. The report also noted that 85% of all breaches involved a human element, such as human error or social engineering.

Therefore, it is essential to educate and train individuals on how to recognize and avoid phishing attacks. This includes raising awareness of common phishing tactics and training individuals to scrutinize emails carefully before clicking on any links or downloading attachments.

## Area1 integrates with KnowBe4

Our integration allows for the seamless integration of Cloudflare’s advanced email security capabilities with KnowBe4's Security Awareness Training platform, KSMAT, and its real-time coaching product, SecurityCoach. This means that organizations using both products can now benefit from an added layer of security that detects and prevents email-based threats in real-time while also training employees to recognize and avoid such threats.

Organizations can offer real-time security coaching to their employees whenever our email security solution detects four types of events: **malicious attachments, malicious links, spoofed emails, and suspicious emails**. IT or security professionals can configure their real-time coaching campaigns to immediately deliver relevant training to their users related to a detected event.

> “KnowBe4 is proud to partner with Cloudflare to provide a seamless integration with our new SecurityCoach product, which aims to deliver real-time security coaching and advice to help end users enhance their cybersecurity knowledge and strengthen their role in contributing to a strong security culture. KnowBe4 is actively working with Cloudflare to provide an API-based integration to connect our platform with systems that IT/security professionals already utilize, making rolling out new products to their teams an easy and unified process.”

By using the integration, organizations can ensure that their employees are not only protected by advanced security technology that detects and blocks malicious emails, but are also educated on how to identify and avoid these threats. This has been a commonly demanded feature from our customers and we have made it simple for them to implement it.

## How it works

### Create private key and public key in the Area 1 dashboard

Before you can set up this integration in your KnowBe4 (KMSAT) console, you will need to create a private key and public key with Cloudflare.

* Log in to your Cloudflare Area 1 email security console as an admin.
* Click the gear icon in the top-right corner of the page, and then navigate to the Service Accounts tab.

![](https://blog.cloudflare.com/content/images/2023/03/image6-9.png)

* Click + Add Service Account.

![](https://blog.cloudflare.com/content/images/2023/03/image8-1.png)

* In the NAME field, enter a name for your new service account.

![](https://blog.cloudflare.com/content/images/2023/03/image2-21.png)

* Click + Create Service Account.
* In the pop-up window that opens, copy and save the private key somewhere that you can easily access. You will need this key to complete the setup process in the Set Up the Integration in your KnowBe4 (KMSAT) Console section below.

![](https://blog.cloudflare.com/content/images/2023/03/image4-12.png)

### Set up the integration in your KnowBe4 (KMSAT) Console

Once you have created a private key and public key in your Cloudflare Area 1 email security console, you can set up the integration in your KMSAT console. To register Cloudflare Area 1 email security with SecurityCoach in your KMSAT console, follow the steps below:

* Log in to your KMSAT console and navigate to SecurityCoach > Setup > Security Vendor Integrations.
* Locate Cloudflare Area 1 Email Security and click Configure.

![](https://blog.cloudflare.com/content/images/2023/03/Screenshot-2023-03-17-at-10.41.52.png)

* Enter the Public Key and Private Key that you saved in the ‘Create your private Key and public key’ section above.

![](https://blog.cloudflare.com/content/images/2023/03/image1-39.png)

* Click authorize. Once you’ve successfully authorized this integration, you can manage detection rules for Cloudflare Area 1 on the ‘Detection rules subtab’ of SecurityCoach.

### SecurityCoach in action

Now that the SecurityCoach is set up, users within your organization will receive messages if Area 1 finds that a malicious email was sent to them. An example one can be seen below.

![](https://blog.cloudflare.com/content/images/2023/03/image9-4.png)

This message not only alerts the user to be more scrutinous about emails they are receiving, since they now know they are being actively targeted, but also provides them with followup steps that they can take to ensure their account is as safe as possible. The image and text that shows up in the email can be configured from the KnowBe4 console giving customers full flexibility on what to communicate with their employees.

![](https://blog.cloudflare.com/content/images/2023/03/image5-4.png)

## What’s next

We’ll be expanding this integration with KnowBe4 to our other Zero Trust products in the coming months. If you have any questions or feedback on this integration, please contact your account team at Cloudflare. We’re excited to continue closely working with technology partners to expand existing and create new integrations that help customers on their Zero Trust journey.

We protect
[entire corporate networks](https://www.cloudflare.com/network-services/),
help custome...