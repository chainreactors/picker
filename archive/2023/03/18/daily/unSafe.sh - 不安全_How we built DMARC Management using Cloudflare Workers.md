---
title: How we built DMARC Management using Cloudflare Workers
url: https://buaq.net/go-153984.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:32.180614
---

# How we built DMARC Management using Cloudflare Workers

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

![](https://8aqnet.cdn.bcebos.com/eb2e4b72fd104c535a6c813088a2cef5.jpg)

How we built DMARC Management using Cloudflare Workers

Loading...
*2023-3-17 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-153984.htm)
阅读量:29
收藏*

---

Loading...

* [![André Cruz](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/02/andre2.jpg)](https://blog.cloudflare.com/author/andre-cruz/)
* [![Nelson Duarte](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/10/me_1x1.jpg)](https://blog.cloudflare.com/author/nelson-duarte/)

![How we built DMARC Management](https://blog.cloudflare.com/content/images/2023/03/How-we-built-DMARC-Management.png)

### What are DMARC reports

[DMARC](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/) stands for Domain-based Message Authentication, Reporting, and Conformance. It's an email authentication protocol that helps protect against email [phishing](https://www.cloudflare.com/en-gb/learning/access-management/phishing-attack/) and [spoofing](https://www.cloudflare.com/en-gb/learning/email-security/what-is-email-spoofing/).

When an email is sent, DMARC allows the domain owner to set up a DNS record that specifies which authentication methods, such as [SPF](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/) (Sender Policy Framework) and [DKIM](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/) (DomainKeys Identified Mail), are used to verify the email's authenticity. When the email fails these authentication checks DMARC instructs the recipient's email provider on how to handle the message, either by quarantining it or rejecting it outright.

DMARC has become increasingly important in today's Internet, where email phishing and spoofing attacks are becoming more sophisticated and prevalent. By implementing DMARC, domain owners can protect their brand and their customers from the negative impacts of these attacks, including loss of trust, reputation damage, and financial loss.

In addition to protecting against phishing and spoofing attacks, DMARC also provides [reporting](https://www.rfc-editor.org/rfc/rfc7489) capabilities. Domain owners can receive reports on email authentication activity, including which messages passed and failed DMARC checks, as well as where these messages originated from.

DMARC management involves the configuration and maintenance of DMARC policies for a domain. Effective DMARC management requires ongoing monitoring and analysis of email authentication activity, as well as the ability to make adjustments and updates to DMARC policies as needed.

Some key components of effective DMARC management include:

* Setting up DMARC policies: This involves configuring the domain's DMARC record to specify the appropriate authentication methods and policies for handling messages that fail authentication checks. Here’s what a DMARC DNS record looks like:

`v=DMARC1; p=reject; rua=mailto:[[email protected]](https://blog.cloudflare.com/cdn-cgi/l/email-protection)`

This specifies that we are going to use DMARC version 1, our policy is to reject emails if they fail the DMARC checks, and the email address to which providers should send DMARC reports.

* Monitoring email authentication activity: DMARC reports are an important tool for domain owners to ensure email security and deliverability, as well as compliance with industry standards and regulations. By regularly monitoring and analyzing DMARC reports, domain owners can identify email threats, optimize email campaigns, and improve overall email authentication.
* Making adjustments as needed: Based on analysis of DMARC reports, domain owners may need to make adjustments to DMARC policies or authentication methods to ensure that email messages are properly authenticated and protected from phishing and spoofing attacks.
* Working with email providers and third-party vendors: Effective DMARC management may require collaboration with email providers and third-party vendors to ensure that DMARC policies are being properly implemented and enforced.

Today we launched [DMARC management](https://blog.cloudflare.com/dmarc-management). This is how we built it.

### How we built it

As a leading provider of cloud-based security and performance solutions, we at Cloudflare take a specific approach to test our products. We "dogfood" our own tools and services, which means we use them to run our business. This helps us identify any issues or bugs before they affect our customers.

We use our own products internally, such as [Cloudflare Workers](https://workers.cloudflare.com/), a serverless platform that allows developers to run their code on our global network. Since its launch in 2017, the Workers ecosystem has grown significantly. Today, there are thousands of developers building and deploying applications on the platform. The power of the Workers ecosystem lies in its ability to enable developers to build sophisticated applications that were previously impossible or impractical to run so close to clients. Workers can be used to build APIs, generate dynamic content, optimize images, perform real-time processing, and much more. The possibilities are virtually endless. We used Workers to power services like [Radar 2.0](https://blog.cloudflare.com/technology-behind-radar2/), or software packages like [Wildebeest](https://blog.cloudflare.com/welcome-to-wildebeest-the-fediverse-on-cloudflare/).

Recently our [Email Routing](https://developers.cloudflare.com/email-routing/) product joined forces with Workers, enabling [processing incoming emails](https://blog.cloudflare.com/announcing-route-to-workers/) via Workers scripts. As the [documentation](https://developers.cloudflare.com/email-routing/email-workers/) states: “With Email Workers you can leverage the power of Cloudflare Workers to implement any logic you need to process your emails and create complex rules. These rules determine what happens when you receive an email.” Rules and verified addresses can all be configured via our [API](https://developers.cloudflare.com/api/operations/email-routing-destination-addresses-list-destination-addresses).

Here’s how a simple Email Worker looks like:

```
export default {
  async email(message, env, ctx) {
    const allowList = ["[email protected]", "[email protected]"];
    if (allowList.indexOf(message.headers.get("from")) == -1) {
      message.setReject("Address not allowed");
    } else {
      await message.forward("[email protected]");
    }
  }
}
```

Pretty straightforward, right?

With the ability to programmatically process incoming emails in place, it seemed like the perfect way to handle incoming DMARC report emails in a scalable and efficient manner, letting Email Routing and Workers do the heavy lifting of receiving an unbound number of emails from across the globe. A high level description of what we needed is:

1. Receive email and extract report
2. Publish relevant details to analytics platform
3. Store the raw report

Email Workers enable us to do #1 easily. We just need to create a worker with an email() handler. This handler will receive the [SMTP](https://www.rfc-editor.org/rfc/rfc5321) envelope elements, a pre-parsed version of the email headers, and a stream to read the entire raw email.

For #2 we can also look into the Workers platform, and we will find the [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/). We just need to define an appropriate schema, which depends both on what’s present in the reports...