---
title: Meddler-in-the-Middle Phishing Attacks Explained
url: https://buaq.net/go-140915.html
source: unSafe.sh - 不安全
date: 2022-12-22
fetch_date: 2025-10-04T02:11:32.951563
---

# Meddler-in-the-Middle Phishing Attacks Explained

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

![](https://8aqnet.cdn.bcebos.com/36ca3ee6644910c62f8bbc5be76ee5d8.jpg)

Meddler-in-the-Middle Phishing Attacks Explained

Executive SummaryWe’ve proba
*2022-12-21 22:0:47
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-140915.htm)
阅读量:47
收藏*

---

![A pictorial representation of a meddler-in-the-middle phishing attack](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/Vulnerability-r3d3.png)

## Executive Summary

We’ve probably all received advice for how to avoid phishing, such as to be on the lookout for spelling errors or other mistakes that would alert us to the presence of fraudsters. However, this advice is only helpful for traditional phishing techniques. Meddler in the Middle (MitM) phishing attacks show how threat actors find ways to get around traditional defenses and advice.

MitM phishing attacks are a state-of-the-art type of phishing attack capable of breaking two-factor authentication (2FA) while avoiding many content-based phishing detection engines. Rather than showing a spoofed version of a target login page, a MitM attack uses a reverse-proxy server to relay the original login page directly to the user’s browser.

As of November 2022, several phishing attacks have used MitM tactics to compromise business email accounts and to successfully steal organizations’ confidential information. There are several popular MitM phishing toolkits that make it easy for hackers to launch their own MitM phishing attacks in just a few clicks.

These toolkits are continually expanding their sets of features while simultaneously becoming more intuitive and easy to use. Many already employ sophisticated cloaking techniques, allowing them to evade detection by traditional phishing detection systems. As such, we expect that the prevalence of these MitM phishing attacks will continue to rise in the near future.

Palo Alto Networks customers receive protection from the attacks discussed in this blog through Advanced URL Filtering by blocking MitM phishing pages in real time.

## Table of Contents

[Introduction: Traditional Phishing Attacks](#post-126111-_sieul6o7rlpy)

## Introduction: Traditional Phishing Attacks

The purpose of a phishing attack is to set up a false login page to trick users into entering their login credentials.

In traditional phishing attacks, attackers will usually create their own phishing page to mimic a legitimate login page. They might host this either on a newly created domain, compromise a legitimate domain and host their phishing page on this domain, or use an existing [SaaS platform](https://unit42.paloaltonetworks.com/platform-abuse-phishing/) to host their phishing content.

“[Phishing kits](https://www.techrepublic.com/article/cybercriminals-phishing-kits-credential-theft/)” simplify the process of creating and deploying phishing attacks by providing a set of programs and/or scripts that allow even inexperienced cybercriminals to launch their own phishing attacks. These kits often employ templated webpages that mimic targeted companies’ actual login pages. Web-based phishing-as a-service (PhaaS) platforms such as [Caffeine](https://www.mandiant.com/resources/blog/caffeine-phishing-service-platform) (shown in Figure 1) and [Robin Banks](https://thehackernews.com/2022/07/researchers-warns-of-increase-in.html) go one step further by providing easy-to-use interfaces that allow threat actors to configure and deploy phishing attacks.

![Image 1 is a screenshot of the Phishing-as-a-Service platform caffeine, which provides features and tools for threat actors at cost. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-50.png)

Figure 1. The homepage for Caffeine, a phishing-as-a-service (PhaaS) platform first revealed in October 2022.

In traditional phishing attacks, the phishing page is typically hosted directly on the malicious or compromised server, and might not necessarily be a perfect replica of a legitimate login page. For example, if an attacker were to create a phishing page mimicking a GitHub login, they might not care to recreate all the various other features surrounding the core login feature, such as the “Forgot My Password” link.

An expert or careful observer might be able to notice subtle discrepancies between the legitimate GitHub login page and the spoofed phishing page and realize that the spoofed page is illegitimate. Figure 2 shows an example of how phishing pages can differ from the original target login page.

Similarly, automated content-based phishing prevention engines might notice that these illegitimate login pages contain signs of suspicious content (such as broken links or misspellings) and flag them as a possible phishing site.

![Image 2 is a screenshot comparing two Microsoft login pages. The image on the left is a fake login page that does not use the correct fonts, but the look itself is very close to a real login page and includes Microsoft's logo. The image on the right is the authentic login page as of late November 2022.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-51.png)

Figure 2. Left: An example of a spoofed Microsoft login page used in a phishing attack. Right: Original Microsoft login page, as of Nov. 21, 2022.

Even with these flaws, the sheer number of recipients in these phishing campaigns mean that some targets could still fall victim to these attacks. [Two-factor authentication](https://www.cisa.gov/mfa) (2FA), aka multifactor authentication (MFA), has become an increasingly popular way of adding an additional layer of security to protect against successful phishing attacks.

An example of 2FA in action is when, in addition to requiring a username and password, a legitimate login site also requires an additional form of authentication such as a one-time password (OTP) sent to the user’s registered email address. Even if an attacker were to gain access to a victim’s username and password via a successful phishing attack, they would not be able to log in as that user, because they would not be able to retrieve the OTP that would be sent during the malicious login attempt.

## MitM Phishing Attacks

MitM phishing attacks are a new type of phishing attack that bypasses both content-based defenses and 2FA. Unlike traditional phishing attacks, which show a separate but spoofed version of a legitimate login page, MitM attacks show the user the *exact same content* that they would see on the legitimate login page. Instead of hosting a replica of a legitimate login page, MitM servers simply *take the content rendered on the legitimate site* and *relay it to the end user*, as shown in Figure 3.

In other words, MitM servers act as a [proxy](https://www.paloaltonetworks.com/cyberpedia/what-is-a-proxy-server) between the target and the legitimate login page. When the target enters their credentials into the proxied page, the MitM server stores the credentials away and forwards them to the legitimate login page, resulting in a successful login attempt. From the victim’s perspective, everything appears as if they had logged in to the legitimate page itself.

Furthermore, both connections (MitM server to legitimate site, and victim to MitM server) are served via the [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) protocol, so the victim will see that the connection is “secure” according to the padlock icon in the web browser’s address bar.

![Image 3 is a visual representation of a Meddler-in-the-Middle phishing attack where the victim user is intercepted by the MITM phishing toolkit so the threat actor can then access the target web server. ](https://unit42...