---
title: Takeaways from the CircleCI Incident
url: https://buaq.net/go-146500.html
source: unSafe.sh - 不安全
date: 2023-01-23
fetch_date: 2025-10-04T04:35:01.865706
---

# Takeaways from the CircleCI Incident

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

Takeaways from the CircleCI Incident

Continuous integration and delivery platform CircleCI confirmed that a securi
*2023-1-22 21:17:48
Author: [perception-point.io(查看原文)](/jump-146500.htm)
阅读量:14
收藏*

---

Continuous integration and delivery platform CircleCI confirmed that a security incident occurred on January 04, 2023 and was caused by an infostealer being deployed on an employee’s laptop. Because the targeted employee had privileges to generate production access tokens, the attacker was able to potentially access and steal data from a subset of databases and stores.

![](https://perception-point.io/wp-content/uploads/post-img-lines-top.svg)

![](https://perception-point.io/wp-content/uploads/post-img-lines-bottom.svg)

## Background

CircleCI is a popular continuous integration and delivery (CI/CD) platform that helps developers automate building, testing and deploying software. With customers in the tens of thousands, it is a widely-used DevOps tool that helps companies such as Google, Peloton and Asana quickly deploy new versions of their products.

On January 4th, 2023, CircleCI informed all of their customers of a security incident and asked them to rotate all secrets stored on CircleCI’s systems, such as cloud provider credentials and repository SSH keys. From the perspective of CircleCI customers, such a security incident is equivalent to the theft of API keys in different production environments. For example, some customers reported misuse of their AWS accounts using AWS credentials stolen from CircleCI.

On January 13th, 2023, CircleCI published that the root cause for the breach was an employee’s Mac laptop that was infected with custom-made malware. CircleCI’s EPP/EDR/AV software did not detect or stop the malware. The malware was able to steal a cookie containing a post-2FA token that was used to access the CircleCI production systems. By using the token, the unauthorized 3rd-party managed to exfiltrate encrypted customer secrets, including AWS keys and GitHub OAuth2 tokens, and had the key to decrypt them.

## The Human Element

CircleCI did not disclose how the malware appeared on the laptop, but according to the disclosed information, the malware probably posed itself as a “PTX Player” for Mac. PTX files are a type of transcript file format that is commonly used by educational institutions and other organizations to store and share transcripts electronically. If we had to guess, a CircleCI employee was targeted via a sophisticated spear-phishing/social engineering attack convincing the employee to download this app in order to view/sign some “important” PTX document.

This demonstrates (yet again) how email is still the easiest way into an organization, even into tech companies that are security-aware and invest heavily in cybersecurity. Recently we have seen a rise in similar incidents, resulting in customer data exposure or theft. A few recent examples:

* A [social engineering campaign](https://mailchimp.com/january-2023-security-incident/) against MailChimp employees and contractors led to password theft and customer data breach
* A [LastPass developer’s endpoint was compromised](https://s3.documentcloud.org/documents/23451840/lastpass-data-breach-notice.pdf) with malware, as part of the latest data leak and customer data was stolen
* A [phishing email campaign](https://www.theguardian.com/media/2023/jan/11/guardian-confirms-it-was-hit-by-ransomware-attack) targeted an employee at The Guardian and the personal data of employees was stolen

These incidents all have one thing in common: **an employee or contractor was tricked into either providing credentials or running malware on their devices** – and the results can be dramatic. This was achieved by either a phishing e-mail or other means of tricking the target, or victim, to visit a malicious website. This should be a wake up call to security teams that email protection is a key cybersecurity layer that must be a high priority – CISOs should not settle for standard/basic email protection and instead seek out advanced email security solutions.

## DevOps Platform Security Tips

Back to the CircleCI incident, if your organization was also impacted, make sure to follow CircleCI’s official recommendations.

Even if you’re not a CircleCI customer, we highly recommend considering the following security measures related to secrets stored on your CI/CD and DevOps platforms:

* Use short-lived temporary credentials. For example, OpenID Connect-based authentication supported by multiple DevOps platforms.
* If temporary credentials cannot be used, automatically rotate non-temporary credentials periodically and on demand.
* Take advantage of IP ranges provided by your DevOps platform to limit inbound connections to their systems. If a token is misused outside the platform, it would be easy to track.
* Run the DevOps execution environment in your own servers directly to inject secrets without storing them in the DevOps platform. This decreases your exposure.
* An internal audit of all stored API keys should be done periodically to further decrease the risk.

Regardless of secrets management, it’s critical to invest in the security of endpoints accessing sensitive/privileged infrastructure and production data, as the next breach might involve other elements which are not just DevOps platform secrets but other crucial customer-related data that shouldn’t get into the wrong hands.

![](https://perception-point.io/wp-content/uploads/pp-lines.svg)

![](https://perception-point.io/wp-content/uploads/post-lines-horizontal.svg)

### Ready to Try

The program will aim to help partners deliver stellar services and customer experiences.

Costs are rising across most companies today. A new study, however, is finding that the costs of protecting against cyber events are also soaring.

Combating cyberattacks has proven to be costly, with organizations shelling out $1,197 per employee annually to deal with email service-, cloud app- or service-, and web browser-related cyber incidents, excluding expenses related to compliance fines, mitigation costs, and business losses, VentureBeat reports.

Global businesses are paying thousands each year to meet the expanding threats against email, browsers, and emerging cloud-based channels in the enterprise

Perception Point announced the publication of a report, “The Rise of Cyber Threats Against Email, Browsers and Emerging Cloud-Based Channels“, which evaluates the responses of security and IT decision-makers at large enterprises and reveals numerous significant findings about today’s enterprise threat landscape.

Perception Point, a leading provider of advanced threat prevention across digital channels, announced the publication of a new report, ‘The Rise of Cyber Threats Against Email, Browsers and Emerging Cloud-Based Channels’.

文章来源: https://perception-point.io/blog/attack-trends/takeaways-from-the-circleci-incident/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)