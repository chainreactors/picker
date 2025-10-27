---
title: Integrate Cloudflare Zero Trust with Datadog Cloud SIEM
url: https://buaq.net/go-173611.html
source: unSafe.sh - 不安全
date: 2023-08-04
fetch_date: 2025-10-04T12:00:11.206080
---

# Integrate Cloudflare Zero Trust with Datadog Cloud SIEM

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

![](https://8aqnet.cdn.bcebos.com/a51cd6b131e31a94f40e389eb2e61ed8.jpg)

Integrate Cloudflare Zero Trust with Datadog Cloud SIEM

Loading...
*2023-8-3 21:0:33
Author: [blog.cloudflare.com(查看原文)](/jump-173611.htm)
阅读量:33
收藏*

---

Loading...

* [![Mythili Prabhu](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/02/Profile.png)](https://blog.cloudflare.com/author/mythili/)
* [![Nimisha Saxena (Guest author)](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/08/Nimisha-Saxena.jpeg)](https://blog.cloudflare.com/author/nimisha/)

![Integrate Cloudflare Zero Trust with Datadog Cloud SIEM](https://blog.cloudflare.com/content/images/2023/08/image5-1.png)

Cloudflare's Zero Trust platform helps organizations map and adopt a strong security posture. This ranges from Zero Trust Network Access, a Secure Web Gateway to help filter traffic, to Cloud Access Security Broker and Data Loss Prevention to protect data in transit and in the cloud. Customers use Cloudflare to verify, isolate, and inspect all devices managed by IT. Our composable, in-line solutions offer a simplified approach to security and a comprehensive set of logs.

We’ve heard from many of our customers that they aggregate these logs into Datadog’s Cloud SIEM product. Datadog Cloud SIEM provides threat detection, investigation, and automated response for dynamic, cloud-scale environments. Cloud SIEM analyzes operational and security logs in real time – regardless of volume – while utilizing out-of-the-box integrations and rules to detect threats and investigate them. It also automates response and remediation through out-of-the-box workflow blueprints. Developers, security, and operations teams can also leverage detailed observability data and efficiently collaborate to accelerate security investigations in a single, unified platform. We previously had an out-of-the-box dashboard for Cloudflare CDN available on Datadog. These help our customers gain valuable insights into product usage and performance metrics for response times, HTTP status codes, cache hit rate. Customers can collect, visualize, and alert on key Cloudflare metrics.

Today, we are very excited to announce the general availability of Cloudflare Zero Trust Integration with Datadog. This deeper integration offers the Cloudflare Content Pack within Cloud SIEM which includes out-of-the-box dashboard and detection rules that will help our customers ingesting Zero Trust logs into Datadog, gaining greatly improved security insights over their Zero Trust landscape.

![](https://blog.cloudflare.com/content/images/2023/08/image4.png)
> “*Our Datadog SIEM integration with Cloudflare delivers a holistic view of activity across Cloudflare Zero Trust integrations–helping security and dev teams quickly identify and respond to anomalous activity across app, device, and users within the Cloudflare Zero Trust ecosystem. The integration offers detection rules that automatically generate signals based on CASB (cloud access security broker) findings, and impossible travel scenarios, a revamped dashboard for easy spotting of anomalies, and accelerates response and remediation to quickly contain an attacker’s activity through an out-of-the-box workflow automation blueprints.*”

## How to get started

### Set up Logpush jobs to your Datadog destination

Use the Cloudflare dashboard or API to [create a Logpush job](https://developers.cloudflare.com/logs/get-started/enable-destinations/datadog/) with all fields enabled for each dataset you’d like to ingest on Datadog. We have eight account-scoped datasets available to use today (Access Requests, Audit logs, CASB findings, Gateway logs including DNS, Network, HTTP; Zero Trust Session Logs) that can be ingested into Datadog.

### Install the Cloudflare Tile in Datadog

In your Datadog dashboard, locate and install the Cloudflare Tile within the Datadog Integration catalog. At this stage, Datadog’s out-of-the-box log processing [pipeline](https://docs.datadoghq.com/logs/log_configuration/pipelines/?tab=source) will automatically parse and normalize your Cloudflare Zero Trust logs.

### Analyze and correlate your Zero Trust logs with Datadog Cloud SIEM's out-of-the-box content

Our new and improved integration with Datadog enables security teams to quickly and easily monitor their Zero Trust components with the Cloudflare Content Pack. This includes the out-of-the-box dashboard that now features a Zero Trust section highlighting various widgets about activity across the applications, devices, and users in your Cloudflare Zero Trust ecosystem. This section gives you a holistic view, helping you spot and respond to anomalies quickly.

![](https://blog.cloudflare.com/content/images/2023/08/image1-2.png)

### Security detections built for CASB

As Enterprises use more SaaS applications, it becomes more critical to have insights and control for data at-rest. Cloudflare CASB findings do just that by providing security risk insights for all integrated SaaS applications.

With this new integration, Datadog now offers an out-of-the-box detection rule that detects any CASB findings. The alert is triggered at different severity levels for any CASB security finding that could indicate suspicious activity within an integrated SaaS app, like Microsoft 365 and Google Workspace. In the example below, the CASB finding points to an asset whose Google Workspace Domain Record is missing.

This detection is helpful in identifying and remedying misconfigurations or any security issues saving time and reducing the possibility of security breaches.

![](https://blog.cloudflare.com/content/images/2023/08/image2.png)

### Security detections for Impossible Travel

One of the most common security issues can show up in surprisingly simple ways. For example, could be a user that seemingly logs in from one location only to login shortly after from a location physically too far away. Datadog’s new detection rule addresses exactly this scenario with their [Impossible Travel detection rule](https://docs.datadoghq.com/security/default_rules/cloudflare-impossible-travel). If Datadog Cloud SIEM determines that two consecutive loglines for a user indicate impossible travel of more than 500 km at over 1,000 km/h, the security alert is triggered. An admin can then determine if it is a security breach and take actions accordingly.

![](https://blog.cloudflare.com/content/images/2023/08/image3.png)

## What’s next

Customers of Cloudflare and Datadog can now gain a more comprehensive view of their products and security posture with the enhanced dashboards and the new detection rules. We are excited to work on adding more value for our customers and develop unique detection rules.

If you are a Cloudflare customer using Datadog, explore the new integration starting [today](https://docs.datadoghq.com/integrations/cloudflare/).

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

To learn more...