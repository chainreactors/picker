---
title: Bring your own CA for client certificate validation with API Shield
url: https://buaq.net/go-171753.html
source: unSafe.sh - 不安全
date: 2023-07-12
fetch_date: 2025-10-04T11:51:32.315602
---

# Bring your own CA for client certificate validation with API Shield

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

![](https://8aqnet.cdn.bcebos.com/08208f745b151e4d5b9854a57a03732d.jpg)

Bring your own CA for client certificate validation with API Shield

Loading...
*2023-7-11 21:0:21
Author: [blog.cloudflare.com(查看原文)](/jump-171753.htm)
阅读量:21
收藏*

---

Loading...

* [![Dina Kozlov](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2019/06/headshot.jpg)](https://blog.cloudflare.com/author/dina/)

![Bring your own CA for client certificate validation with API Shield](https://blog.cloudflare.com/content/images/2023/07/image1-5.png)

APIs account for more than half of the total traffic of the Internet. They are the building blocks of many modern web applications. As API usage grows, so does the number of [API attacks](https://www.cloudflare.com/learning/insights-waap-api-security/). And so now, more than ever, it’s important to keep these API endpoints secure. Cloudflare’s API Shield solution offers a comprehensive suite of products to safeguard your API endpoints and now we’re excited to give our customers one more tool to keep their endpoints safe. We’re excited to announce that customers can now bring their own Certificate Authority (CA) to use for mutual TLS client authentication. This gives customers more security, while allowing them to maintain control around their Mutual TLS configuration.

### The power of Mutual TLS (mTLS)

Traditionally, when we refer to TLS certificates, we talk about the publicly trusted certificates that are presented by servers to prove their identity to the connecting client. With Mutual TLS, both the client and the server present a certificate to establish a two-way channel of trust. Doing this allows the server to check who the connecting client is and whether or not they’re allowed to make a request. The certificate presented by the client - the client certificate - doesn’t need to come from a publicly trusted CA. In fact, it usually comes from a private or self-signed CA. That’s because the only party that needs to be able to trust it is the connecting server. As long as the connecting server has the client certificate and can check its validity, it doesn’t need to be public.

### Securing API endpoints with Mutual TLS

Mutual TLS plays a crucial role in protecting API endpoints. When it comes to safeguarding these endpoints, it's important to have a security model in place that only allows authorized clients to make requests and keeps everyone else out.

That’s why when we launched API Shield in 2020 - a product that’s centered around securing API endpoints - we included mutual TLS client certificate validation as a part of the offering. We knew that mTLS was the best way for our customers to identify and authorize their connecting clients.

When we launched mutual TLS for API Shield, we gave each of our customers a dedicated self-signed CA that they could use to issue client certificates. Once the certificates are installed on devices and mTLS is set up, administrators can enforce that connections can only be made if they present a client certificate issued from that self-signed CA.

This feature has been paramount in securing thousands of endpoints, but it does require our customer to install new client certificates on their devices, which isn’t always possible. Some customers have been using mutual TLS for years with their own CA, which means that the client certificates are already in the wild. Unless the application owner has direct control over the clients, it’s usually arduous, if not impossible, to replace the client certificates with ones issued from Cloudflare’s CA. Other customers may be required to use a CA issued from an approved third party in order to meet regulatory requirements.

To help all of our customers keep their endpoints secure, we’re extending API Shield’s mTLS capability to allow customers to bring their own CA.

![](https://blog.cloudflare.com/content/images/2023/07/image2-3.png)

### Get started today

To simplify the management of private PKI at Cloudflare, we created one account level endpoint that enables customers to upload self-signed CAs to use across different Cloudflare products. Today, this endpoint can be used for API shield CAs and for [Gateway](https://blog.cloudflare.com/bring-your-certificates-cloudflare-gateway/) CAs that are used for traffic inspection.

If you’re an Enterprise customer, you can upload up to five CAs to your account. Once you’ve uploaded the CA, you can use the API Shield hostname association API to associate the CA with the mTLS enabled hostnames. That will tell Cloudflare to start validating the client certificate against the uploaded CA for requests that come in on that hostname. Before you enforce the client certificate validation, you can create a Firewall rule that logs an event when a valid or invalid certificate is served. That will help you determine if you’ve set things up correctly before you enforce the client certificate validation and drop unauthorized requests.

To learn more about how you can use this, refer to our [developer documentation](https://developers.cloudflare.com/ssl/client-certificates/byo-ca-api-shield/).

If you’re interested in using mutual TLS to secure your corporate network, talk to an account representative about using our Access product to do so.

We protect
[entire corporate networks](https://www.cloudflare.com/network-services/),
help customers build
[Internet-scale applications efficiently](https://workers.cloudflare.com/),
accelerate any
[website
or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/),
[ward off DDoS
attacks](https://www.cloudflare.com/ddos/), keep
[hackers at
bay](https://www.cloudflare.com/application-security/),
and can help you on
[your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://1.1.1.1/) from any device to get started with
our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a
new career direction, check out [our open
positions](https://cloudflare.com/careers).

[API Shield](https://blog.cloudflare.com/tag/api-shield/)
[Mutual TLS](https://blog.cloudflare.com/tag/mutual-tls/)
[SSL](https://blog.cloudflare.com/tag/ssl/)
[TLS](https://blog.cloudflare.com/tag/tls/)
[Security](https://blog.cloudflare.com/tag/security/)

Related Posts

March 20, 2023 1:00PM

[## Everything you might have missed during Security Week 2023](https://blog.cloudflare.com/security-week-2023-wrap-up/)

Learn how Cloudflare made it easier to shift from protecting applications, to protecting employees, and making sure they are protected everywhere during Security Week 2023...

By

September 22, 2022 2:00PM

[## API Endpoint Management and Metrics are now GA](https://blog.cloudflare.com/api-management-metrics/)

API Shield customers can save, update, and monitor the performance of API endpoints...

By

March 15, 2023 1:00PM

[## Automatically discovering API endpoints and generating schemas using machine learning](https://blog.cloudflare.com/ml-api-discovery-and-schema-learning/)

Today we’re announcing that Cloudflare can now automatically discover all API endpoints and learn API schemas for all of our API Gateway customers...

By

March 15, 2023 1:00PM

[## Detecting API abuse automatically using sequence analysis](https://blog.cloudflare.com/api-sequence-analytics/)

Today, we're announcing Cloudflare Sequence Analytics for APIs. Using Sequence Analytics, Customers subscribed to A...