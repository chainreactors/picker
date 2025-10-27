---
title: Protecting data on Apple devices with Cloudflare and Jamf
url: https://buaq.net/go-172551.html
source: unSafe.sh - 不安全
date: 2023-07-21
fetch_date: 2025-10-04T11:51:52.482092
---

# Protecting data on Apple devices with Cloudflare and Jamf

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

![](https://8aqnet.cdn.bcebos.com/3df9bfd92cd74ae2ca0af897e22d75b9.jpg)

Protecting data on Apple devices with Cloudflare and Jamf

Loading...
*2023-7-20 21:0:41
Author: [blog.cloudflare.com(查看原文)](/jump-172551.htm)
阅读量:19
收藏*

---

Loading...

* [![Mythili Prabhu](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/02/Profile.png)](https://blog.cloudflare.com/author/mythili/)
* [![Matt Vlasach (Guest author)](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/07/Matt-Vlasach-Jamf.jpeg)](https://blog.cloudflare.com/author/matt-vlasach-guest-author/)

![Protecting data on Apple devices with Cloudflare and Jamf](https://blog.cloudflare.com/content/images/2023/07/image1-9.png)

Today we’re excited to announce Cloudflare’s partnership with Jamf to extend Cloudflare’s Zero Trust Solutions to Jamf customers. This unique offering will enable Jamf customers to easily implement network [Data Loss Prevention (DLP)](https://www.cloudflare.com/products/zero-trust/dlp/), [Remote Browser Isolation (RBI)](https://www.cloudflare.com/products/zero-trust/browser-isolation/), and [SaaS Tenancy Controls](https://blog.cloudflare.com/gateway-tenant-control/) from Cloudflare to prevent sensitive data loss from their Apple devices.

Jamf is a leader in protecting Apple devices and ensures secure, consumer-simple technology for 71,000+ businesses, schools and hospitals. Today Jamf manages [~30 million](https://www.globenewswire.com/en/news-release/2023/01/10/2586305/0/en/Jamf-Ends-2022-Helping-Approximately-71-000-Customers-Succeed-with-Apple.html) Apple devices with MDM, and our partnership extends powerful policy capabilities into the network.

> *“One of the most unforgettable lines I’ve heard from an enterprise customer is their belief that ‘Apple devices are like walking USB sticks that leave through the business’s front door every day.’ It doesn’t have to be that way! We are on a mission at Jamf to help our customers achieve the security and compliance controls they need to confidently support Apple devices at scale in their complex environments. While we are doing everything we can to reach this future, we can’t do it alone. I’m thrilled to be partnering with Cloudflare to deliver a set of enterprise-grade compliance controls in a novel way that leverages our combined next-generation cloud-native infrastructures to deliver a fast, highly-available end user experience.”*

## Integrated access with Jamf Security Cloud

Jamf’s Apple-first Zero Trust Network Access (ZTNA) agent, Jamf Trust, is designed to seamlessly deploy via Jamf Pro with rich identity, endpoint security, and networking integrations that span the Jamf platform. All of these components work together as part of Jamf Security Cloud to protect laptop and mobile endpoints from network and endpoint threats while enabling fast, least-privilege access to company resources in the cloud or behind the firewall.

Through this partnership, Jamf customers can now dynamically steer select traffic to Cloudflare’s network using Magic WAN. This enables customers to unlock rich [DLP](https://www.cloudflare.com/learning/access-management/what-is-dlp/) capabilities, [Remote Browser Isolation](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/), and SaaS Tenancy Controls in a cloud-first, cloud-native architecture that works great on Apple devices.

![](https://blog.cloudflare.com/content/images/2023/07/image2-12.png)

## Seamless integration to protect company data

While content inspection policies can be created, they cannot be applied to HTTPS traffic since content payloads are encrypted. This is a problem for organizations as it is common for sensitive data to live within an encrypted payload and bypass IT content inspection policies. [99.7% of all requests](https://radar.cloudflare.com/adoption-and-usage?dateRange=52w) use HTTPS today and the usage has been seeing a steady increase.

To address this visibility gap, organizations can decrypt packets using HTTPS inspection. With Cloudflare Gateway, [SSL/TLS decryption](https://www.cloudflare.com/learning/security/what-is-https-inspection/) can be performed to inspect HTTPS traffic for security risks. When TLS decryption is enabled, Gateway will decrypt all traffic sent over HTTPS, apply your HTTP policies, and then re-encrypt the request with a [user-side certificate](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/user-side-certificates/). Jamf is able to seamlessly enable this process on managed devices.

### Protect sensitive data with Data Loss Prevention

With the corporate network and employees being boundless, it is harder than ever to keep data secure. Sensitive data such as customer credit card information, social security numbers, API tokens, or confidential Microsoft Office documents are easily shared beyond your network boundary, intentionally or otherwise. This is made worse as attackers are increasingly tricking well-intentioned employees to inadvertently share sensitive data with hackers. Such data leaks are not uncommon and usually result in costly reputational and compliance damages.

![](https://blog.cloudflare.com/content/images/2023/07/image3-2.png)

[Cloudflare’s Data Loss Prevention (DLP)](https://www.cloudflare.com/products/zero-trust/dlp/) allows for policies to be built in with ease to keep highly sensitive data secure. Cloudflare also provides [predefined profiles](https://developers.cloudflare.com/cloudflare-one/policies/data-loss-prevention/dlp-profiles/predefined-profiles/) for detecting financial information such as credit card numbers and national identifiers such as social security numbers or tax file numbers in addition to credentials and secrets such as GCP keys, AWS keys, Azure API keys, and SSH keys. On top of that, Cloudflare DLP allows for the creation of expanded regex profiles to detect custom keywords and phrases.

**Steps to implement Cloudflare DLP with Jamf:**

1. In Jamf’s Security Cloud portal, [configure a Magic WAN interconnect](https://learn.jamf.com/bundle/jamf-security-documentation/page/Connecting_to_Cloud_Infrastructure_for_Cloudflare.html) to your Cloudflare account.
2. Create an [access policy](https://learn.jamf.com/bundle/jamf-security-documentation/page/Access_Policies.html) to route traffic for DLP inspection via your Cloudflare Magic WAN interconnect
   * Traffic may be matched by hostname, domain, or IP address/CIDR block
   * To route all traffic for inspection, define `*` for hostnames and `0.0.0.0/0` for IPs in the access policy. Note: this will be treated as the “gateway of last resort”, with other access policies matching first.
   * Optionally, enable “Restrict access when Jamf Trust is disabled” under the Security tab of the policy to prevent bypassing of DLP inspection for these resources.
3. [Configure a DLP policy](https://developers.cloudflare.com/cloudflare-one/policies/data-loss-prevention/dlp-policies/) in your Cloudflare One portal.
4. In Jamf Pro, create a new Configuration Profile with the [Cloudflare Gateway Root Certificate Authority](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/user-side-certificates/install-cloudflare-cert/#download-the-cloudflare-root-certificate) and scope it to your target Apple devices.

Using Activation Profiles in Jamf Security Cloud, deploy Jamf Trust and supporting mobile configuration profiles to your end users to enable access to organization resources while enforcing DLP policies.

### Isolate browser thre...