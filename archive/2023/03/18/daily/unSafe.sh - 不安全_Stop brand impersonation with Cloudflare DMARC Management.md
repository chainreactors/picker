---
title: Stop brand impersonation with Cloudflare DMARC Management
url: https://buaq.net/go-153985.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:32.796755
---

# Stop brand impersonation with Cloudflare DMARC Management

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

![](https://8aqnet.cdn.bcebos.com/579fbb5fd9d8f0a755d985a69cfbabec.jpg)

Stop brand impersonation with Cloudflare DMARC Management

Loading...
*2023-3-17 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-153985.htm)
阅读量:21
收藏*

---

Loading...

* [![João Sousa Botto](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/07/profile2.jpg)](https://blog.cloudflare.com/author/joao/)

![Stop brand impersonation with Cloudflare DMARC Management](https://blog.cloudflare.com/content/images/2023/03/Security-Center-now-includes-ZT--DLP-and-email-.png)

At the end of 2021 Cloudflare [launched Security Center](https://blog.cloudflare.com/security-center/), a unified solution that brings together our suite of security products and unique Internet intelligence. It enables security teams to quickly identify potential security risks and threats to their organizations, map their attack surface and mitigate these risks with just a few clicks. While Security Center initially focused on application security, we are now adding crucial zero trust insights to further enhance its capabilities.

When your brand is loved and trusted, customers and prospects are looking forward to the emails you send them. Now picture them receiving an email from you: it has your brand, the subject is exciting, it has a link to register for something unique — how can they resist that opportunity?

But what if that email didn’t come from you? What if clicking on that link is a scam that takes them down the path of fraud or identity theft? And what if they think you did it? The truth is, even security minded people occasionally fall for well crafted spoof emails.

That poses a risk to your business and reputation. A risk you don’t want to take - no one does. Brand impersonation is a [significant problem for organizations globally](https://blog.cloudflare.com/2022-march-hackness-phishing-bracket/), and that’s why we’ve built DMARC Management - available in Beta today.

With DMARC Management you have full insight on who is sending emails on your behalf. You can one-click approve each source that is a legitimate sender for your domain, and then set your [DMARC](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/) policy to reject any emails sent from unapproved clients.

![On the DMARC Management one can see trends of messages passing or failing DMARC, and a breakdown by sending client (source)](https://blog.cloudflare.com/content/images/2023/03/DMARC-1.jpg)

When the survey platform your company uses is sending emails from your domain, there’s nothing to worry about - you configured it that way. But if an unknown mail service from a remote country is sending emails using your domain that can be quite scary, and something you’ll want to address. Let’s see how.

### Anti-spoofing mechanisms

Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) and Domain-based Message Authentication Reporting and Conformance (DMARC) are three common email authentication methods. Together, they help prevent spammers, phishers, and other unauthorized parties from sending emails on behalf of a domain they do not own.

**SPF** is a way for a domain to list all the servers the company sends emails from. Think of it like a publicly available employee directory that helps someone to confirm if an employee works for an organization. [SPF records](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) list all the IP addresses of all the servers that are allowed to send emails from the domain.

**DKIM** enables domain owners to automatically "sign" emails from their domain. Specifically, DKIM uses [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/):

1. A [DKIM record](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/) stores the domain's *public key*, and mail servers receiving emails from the domain can check this record to obtain the public [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/).
2. The *private key* is kept secret by the sender, who signs the email's header with this key.
3. Mail servers receiving the email can verify that the sender's private key was used by applying the public key. This also guarantees that the email was not tampered with while in transit.

**DMARC** tells a receiving email server what to do after evaluating the SPF and DKIM results. A domain's DMARC policy can be set in a variety of ways — it can instruct mail servers to quarantine emails that fail SPF or DKIM (or both), to reject such emails, or to deliver them.

It’s not trivial to configure and maintain SPF and DMARC, though. If your configuration is too strict, legitimate emails will be dropped or marked as spam. If it’s too relaxed, your domain might be misused for email spoofing. The proof is that these authentication mechanisms (SPF / DKIM / DMARC) have existed for over 10 years and still, there are still [less than 6 million active DMARC records](https://dmarc.org/stats/dmarc/).

DMARC reports can help, and a full solution like DMARC Management reduces the burden of creating and maintaining a proper configuration.

### DMARC reports

All DMARC-compliant mailbox providers support sending DMARC aggregated reports to an email address of your choice. Those reports list the services that have sent emails from your domain and the percentage of messages that passed DMARC, SPF and DKIM. They are extremely important because they give administrators the information they need to decide how to adjust their DMARC policies — for instance, that’s how administrators know if their legitimate emails are failing SPF and DKIM, or if a spammer is trying to send illegitimate emails.

![Email messages reach their destination, and an action is taken by the server according to the DMARC policies published in our DNS records. Then, the receiver sends a report back to the source.](https://blog.cloudflare.com/content/images/2023/03/pasted-image-0--1--7.png)

But beware, you probably don’t want to send DMARC reports to a human-monitored email address, as these come in fast and furious from virtually every email provider your organization sends messages to, and are delivered in XML format. Typically, administrators set up reports to be sent to a service like our DMARC Management, that boils them down to a more digestible form. *Note: These reports do not contain personal identifiable information (PII).*

DMARC Management automatically creates an email address for those reports to be sent to, and adds the corresponding [RUA record](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/) to your Cloudflare DNS to announce to mailbox providers where to send reports to. And yes, if you’re curious, these email addresses are being created using [Cloudflare Email Routing](https://www.cloudflare.com/products/email-routing/).

*Note: Today, Cloudflare DNS is a requirement for DMARC Management. Cloudflare Area 1 customers will soon also be able to see DMARC reports even if they’re using third-party DNS services.*

![There is a preview of the DMARC record being created with this RUA](https://blog.cloudflare.com/content/images/2023/03/DMARC--1--1.jpg)

As reports are received in this dedicated email address, they are processed by a [Worker](https://workers.cloudflare.com/) that extracts the relevant data, parses it and sends it over to our analytics solution. And you guessed again, that’s implemented using [Email Workers](https://developers.cloudflare.com/email-routing/email-workers/). You can read more about the technical i...