---
title: The Rising Issue of Zombie APIs and Your Increased Attack Surface
url: https://buaq.net/go-242663.html
source: unSafe.sh - 不安全
date: 2024-06-02
fetch_date: 2025-10-06T16:55:12.364273
---

# The Rising Issue of Zombie APIs and Your Increased Attack Surface

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

The Rising Issue of Zombie APIs and Your Increased Attack Surface

Offering an API to customers increases your revenue, but it also expands your attack surface. Busine
*2024-6-1 23:30:11
Author: [hackernoon.com(查看原文)](/jump-242663.htm)
阅读量:10
收藏*

---

Offering an API to customers increases your revenue, but it also expands your attack surface. Businesses can offer an API that can be embedded into third-party applications to make development easier. For example, embedding social media into an application lets customers discuss a product without adding extensive overhead to your development team. The social media company gains traffic and visibility, and the customer gains ease of development while adding features to their application.

Although an API is good for marketing and revenue, adding APIs and endpoints expands your attack surface. Having an API is an additional risk that can be managed, but all endpoints should be strictly monitored and secured. Most administrators agree that APIs must be monitored, but a fast-paced business environment with numerous updates and deployments might find itself losing track of APIs and unknowingly adding a cybersecurity risk called “zombie APIs.”

## What is a Zombie API?

A zombie API is (in basic terms) a forgotten and overlooked infrastructure that remains available for use, but organizations are unaware of its existence. Zombie APIs can be created in small or large environments, but they are often created in environments where IT resources are built without strict provisioning and documentation procedures in place. Change control helps avoid zombie API situations, but emergency deployments or configurations performed to fix a specific critical error can also happen.

In an automated environment, cloud resources are often deployed along with application code. The benefit is that developers and operations people no longer need to remember to deploy hardware and configure it manually. Automation in software deployment lowers incidents based on misconfigurations or avoids any issues where developers forget to include requests to provision resources to support their applications.

In some environments, developers are given access to their own test servers. These servers might be accessible on the public internet so that developers can test new code. An API test server might be available to the public internet, and developers might think that it won’t be detected without being published.

Zombie APIs can be created in numerous ways with their own edge cases, even with the most strict of change control procedures. Whether they occur from mistakes or misguidance, zombie APIs are a form of [shadow IT](https://hackernoon.com/shadow-it-what-it-means-and-how-it-impacts-organizations?ref=hackernoon.com) that can be especially dangerous to data protection. Without monitoring, an attacker could retrieve data for months with no limitations or rate limiting. Any probing for vulnerabilities or exploiting them would not be logged, so typical cybersecurity analytics wouldn’t notify administrators of anomalous traffic.

## How Do Hackers Find Zombie APIs?

Just like the numerous ways a zombie API can be created based on the situation, the same can be said for finding a zombie API. Hackers could find an endpoint by reverse engineering code, reviewing open-source repositories, or through a concept called “fuzzing.” Fuzzing is a type of discovery where scripts are written to make requests against common API endpoint names. For example, it’s common for an API endpoint used for authentication to have an endpoint named “/login” or “/authenticate” or something similar. Requests are made to different common endpoint names against your infrastructure to discover endpoints.

Discovery from open-source repositories is common. Open-source repositories are also vulnerable to disclosure of secrets, meaning that developers might forget to remove references to private keys, authentication credentials, and other private data. References to API endpoints are also available for discovery and will be probed for any vulnerabilities. If your organization is unaware of endpoints referenced in code, then they could be probed without any mitigation or rate limiting.

A zombie API isn’t always vulnerable to bug exploits. For example, exploiting SQL injection vulnerabilities could cause data disclosure of sensitive information, but some endpoints are properly coded with resilience against threats. In a zombie API situation, the API might function normally, but it can be used to gather data without any limitations. It’s possible that the endpoint could have a business logic error that could be exploited, but without monitoring, any suspicious activity would go undetected.

## Real-World Data Breaches from Zombie APIs

A good example of an API functioning normally but being used to quietly enumerate data is the [JustDial incident](https://thehackernews.com/2019/04/justdial-hacked-data-breach.html?ref=hackernoon.com). JustDial is one of India’s large local directories with over 100 million users. In 2019, a security researcher found that JustDial had a zombie API open to the public internet without any monitoring implemented. The API returned information like name, email, mobile number, address, and gender to anyone making a request to the endpoint. No authentication was necessary, and JustDial was not monitoring to catch the incident.

After a security researcher detected the zombie API, JustDial claimed to have remediated the incident, but the same issue was detected again in 2020. It’s unclear if any third party aside from the security researcher, but because the endpoint was open to the public internet with no monitoring in place, JustDial cannot assess the extent of the data exfiltration.

Another example is with one of the big San Francisco tech companies known for some of the best developers on the market, Facebook. Facebook has had several instances of zombie APIs. In 2016, developers deployed a subdomain (mbasic.beta.facebook.com) to test their password reset functionality. The production version of the API had rate limitations on it, so attackers could not brute force the six-digit passcode sent to users to reset their passwords. The beta version did not have this limitation, so a six-digit passcode could be brute forced within seconds, limited only by an internet connection, bandwidth, and the API endpoints’ backend processing speed.

In 2018, Facebook suffered from another [zombie API attack](https://www.pingidentity.com/en/resources/blog/post/facebook-data-breach-highlights-api-vulnerabilities.html?ref=hackernoon.com). The vulnerability was found in Facebook’s “View As” feature. The feature allowed users to view their profiles as others see it. The API endpoint for this feature was not locked down or monitored, so attackers could view other user profiles and steal their access tokens. With an access token, an attacker can then steal a user’s profile and their data. Facebook estimated that 40 million users were impacted, and 90 million users had to re-authenticate to ensure that their access token was not stolen.

A smaller company--yet significant data breach from a zombie API--occurred in 2022 with an endpoint from Travis CI. Travis CI is an automation vendor used to deploy infrastructure and code. One of Travis CI’s API endpoints required no authentication and allowed for requests to obtain customer log events. To make matters worse, logs were stored in plaintext, so user log data, including access keys, could be retrieved without any limitations. When the issue was reported, Travis CI es...