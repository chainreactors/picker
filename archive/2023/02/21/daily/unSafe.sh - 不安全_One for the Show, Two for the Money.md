---
title: One for the Show, Two for the Money
url: https://buaq.net/go-150194.html
source: unSafe.sh - 不安全
date: 2023-02-21
fetch_date: 2025-10-04T07:35:19.352454
---

# One for the Show, Two for the Money

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

![](https://8aqnet.cdn.bcebos.com/646dea038cf7ad833e506c73ecdda6a4.jpg)

One for the Show, Two for the Money

Over the last two months there has been a noticeable surge in phishing campaigns. A dangerous s
*2023-2-20 17:43:45
Author: [perception-point.io(查看原文)](/jump-150194.htm)
阅读量:16
收藏*

---

Over the last two months there has been a noticeable surge in [phishing](https://perception-point.io/blog/how-to-prevent-phishing-attacks/) campaigns. A dangerous sub-type of these attacks, known as “two-step phishing”, has become increasingly prevalent. Unlike traditional phishing attacks that usually rely on generic emails and social engineering tactics, these coupled counterparts take advantage of legitimate email accounts belonging to actual people that have been compromised by threat actors (see: [account takeover](https://perception-point.io/guides/cybersecurity/understanding-account-takeover-ato-9-defensive-measures/)).

![](https://perception-point.io/wp-content/uploads/1-14-300x300.png)

## **The Two-Step Phishing Kill Chain Unfolds**

In a two-step phishing attack, the attacker first gains access to a user’s legitimate email account. They then use the account to send targeted emails to known individuals linked to the compromised account (typically within the same organization as the victim). The email messages appear to have come from a trusted source, which usually prompts the recipient to click on a button or text in the body of the email to view the content (oftentimes business-related, like a Purchase Order, RFQ, bill, etc.).

Clicking the embedded link takes the recipient to a seemingly legitimate website, like Google Docs, Dropbox, SharePoint and others – that is the first step of the attack. On many occasions attackers will “plant” a benign page on a known domain, taking advantage of its high reputation to evade detection. These sites are often used for legitimate business collaboration between the parties, making the attack even more reliable.

**As of February 2023, the Perception Point’s** [**Incident Response**](https://perception-point.io/guides/incident-response/incident-response-complete-guide-enterprises/) **team has reported over 300 different legitimate websites and services that have been used to host these complex attacks.**

It is crucial to note that at this phase of the attack kill chain there is nothing “really” malicious about the first link clicked or the page that the users may visit.

Once on the “legitimate” website, the user is presented with another clickable element within the page. This is the second step of the kill chain. This time the link will redirect them to a spoofed page designed to harvest their login credentials or credit card information.

## **Advanced Two-Step Phishing in the Wild**

In this recent sample caught by Perception Point, we can see an email sent from a compromised vendor account – a financial manager working for a business specializing in luxury housing.

![](https://lh3.googleusercontent.com/DTEJaInfifMarA8q_1sMeyB2mEVafzdHezEk-PH6spGhMtdQcNAjmSbGgmmia1RaQg44qukjVtuUOWWzhe67BFMA1BS0NvVuLCXXfZyqMwatIFV_NaxzNPMu3WbxQDD2clgywFwmU0-jpSixiPZt1dY)

*Figure 1: An email from a known vendor –  the first step of the two-step phishing attack*

The subject line refers to a purchase order (PO), a.k.a the social engineering part of the attack, meant to incentivize the recipient to continue clicking. The body of the message contains a clickable element made to look like a DocuSign link (an electronic signature platform).

Clicking on “Review Document” leads to a webpage hosted on <https://squareup.com/> – the official domain of Square, a financial services and mobile payment company based in San Francisco.

![](https://lh6.googleusercontent.com/WOOVqq37rYSwLsSIF0rRgQI8qHkhC512fSXPXkhrWWqQiiVWz5LsdYkI7mhMVZv-mR7LNTmAWn_CT5M0yBwBqvwZAdMXy92wxUKXjUF-n5r4XL7w4FRREa9MIf0lywNvQbE9VKPlfzfkHMEgjB2vDII)

*Figure 2:  A page hosted on a legitimate domain containing a link to a malicious page*

At first glance, it seems like a harmless page branded with the name of the financial manager’s company, their logo and even their business description. **Keep in mind that this page is hosted on the Square domain so its URL has both “https” and a high reputation.**

At the bottom of the page, there is a button inviting the user to “View The Document”.

![](https://lh3.googleusercontent.com/s7hguAWjsoqV3Ky8p8IzijRRLknZ2o_24_fJjotGMzws7Aa-FBIhup9iE70wCzQMqqamJGNYvzbmmf0-qYw6L9eEELQqLmMD1tfEXwCKAeAuRkhjjQvHS7XhuLmcCozoZ_x_5QR-jyg_1PRzt7lI5CE)

*Figure 3: The malicious spoofed Microsoft login page – the second step of attack*

Only when the user clicks on this button are they redirected to the second step of the attack – a credential harvesting login page, spoofed to impersonate Microsoft.

This example shows us why two-step phishing attacks are so dangerous and evasive:

1. Most attacks originate from legitimate vendors who had one or more of their accounts taken over by threat actors. Due to high sender reputation, whitelisting, and other policies, many email security solutions will fail to detect them.
2. People are more likely to fall for these phishing attacks due to their familiarity and past communication patterns with the “senders”.
3. Attackers use legitimate services as the first payload – most email security vendors will fail to follow and detect the second malicious payload.

## **Advanced Object Detection Model – Perception Point’s Answer to Two-Step Phishing Attacks**

![](https://perception-point.io/wp-content/uploads/2-17-300x300.png)

In order to tackle the two-step phishing evasion technique, Perception Point has developed an innovative image recognition model leveraging object detection. Object detection is a computer vision technology that deals with detecting objects’ locations and classifying them (such as humans, buildings, or animals) in digital images and videos.

Perception Point’s novel model takes a screenshot of a webpage and is tasked with recognizing clickable elements within it. Together with our proprietary [Recursive Unpacker](https://perception-point.io/cyber-threat-detection-platform/), the solution can click on all elements and track the path to the malicious payload.

**This detection technique negates any attempt made by attackers to evade detection, as it analyzes the web page exactly as the victim sees and experiences it.** If it detects a clickable element, the Recursive Unpacker will click on it and run the same process on the next web page.

Perception Point employs a cutting-edge object detection model that achieves remarkable speed, with an average processing time of **just 0.03 seconds per screenshot**. Unlike most object detection models that rely on multiple networks and subdivide the image, our model takes a holistic approach, utilizing a single model that can make predictions based on the entire image in one iteration. This ensures that we can provide accurate results in real-time. In addition, this innovative model detects login pages and known logos in an instant, and assesses the potential of a webpage being a phishing site along with the overall risk associated with the page.

Furthermore, in conjunction with our [Advanced Browser Security](https://perception-point.io/channel-coverage/web-security/) extension, advanced geolocation based evasion (see: [geofencing](https://perception-point.io/blog/trending-phishing-attacks-spoofing-financial/)) is thwarted as well to overcome the most advanced evasion techniques employed by threat actors.

Through this multi-layered process, Perception Point Advanced Email Security provides our user...