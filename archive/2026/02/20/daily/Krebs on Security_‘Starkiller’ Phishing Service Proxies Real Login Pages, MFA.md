---
title: ‘Starkiller’ Phishing Service Proxies Real Login Pages, MFA
url: https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/
source: Krebs on Security
date: 2026-02-20
fetch_date: 2026-02-21T04:01:12.634832
---

# ‘Starkiller’ Phishing Service Proxies Real Login Pages, MFA

Advertisement

[![](/b-knowbe4/44.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

Advertisement

[![](/b-doppel/2.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=fight)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# ‘Starkiller’ Phishing Service Proxies Real Login Pages, MFA

February 20, 2026

[6 Comments](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/#comments)

Most phishing websites are little more than static copies of login pages for popular online destinations, and they are often quickly taken down by anti-abuse activists and security firms. But a stealthy new phishing-as-a-service offering lets customers sidestep both of these pitfalls: It uses cleverly disguised links to load the target brand’s real website, and then acts as a relay between the target and the legitimate site — forwarding the victim’s username, password and multi-factor authentication (MFA) code to the legitimate site and returning its responses.

There are countless phishing kits that would-be scammers can use to get started, but successfully wielding them requires some modicum of skill in configuring servers, domain names, certificates, proxy services, and other repetitive tech drudgery. Enter **Starkiller**, a new phishing service that dynamically loads a live copy of the real login page and records everything the user types, proxying the data from the legitimate site back to the victim.

According to an analysis of Starkiller by the security firm **Abnormal AI**, the service lets customers select a brand to impersonate (e.g., Apple, Facebook, Google, Microsoft et. al.) and generates a deceptive URL that visually mimics the legitimate domain while routing traffic through the attacker’s infrastructure.

For example, a phishing link targeting Microsoft customers appears as “login.microsoft.com@[malicious/shortened URL here].” The “@” sign in the link trick is an oldie but goodie, because everything before the “@” in a URL is considered username data, and the real landing page is what comes after the “@” sign. Here’s what it looks like in the target’s browser:

[![](https://krebsonsecurity.com/wp-content/uploads/2026/02/starkillerphishinglink.png)](https://krebsonsecurity.com/wp-content/uploads/2026/02/starkillerphishinglink.png)

Image: Abnormal AI. The actual malicious landing page is blurred out in this picture, but we can see it ends in .ru. The service also offers the ability to insert links from different URL-shortening services.

Once Starkiller customers select the URL to be phished, the service spins up [a Docker container](https://www.docker.com/resources/what-container/) running a [headless Chrome browser instance](https://developer.chrome.com/docs/chromium/headless) that loads the real login page, Abnormal found.

“The container then acts as a man-in-the-middle reverse proxy, forwarding the end user’s inputs to the legitimate site and returning the site’s responses,” Abnormal researchers **Callie Baron** and **Piotr Wojtyla** wrote in [a blog post on Thursday](https://abnormal.ai/blog/starkiller-phishing-kit). “Every keystroke, form submission, and session token passes through attacker-controlled infrastructure and is logged along the way.”

Starkiller in effect offers cybercriminals real-time session monitoring, allowing them to live-stream the target’s screen as they interact with the phishing page, the researchers said.

“The platform also includes keylogger capture for every keystroke, cookie and session token theft for direct account takeover, geo-tracking of targets, and automated Telegram alerts when new credentials come in,” they wrote. “Campaign analytics round out the operator experience with visit counts, conversion rates, and performance graphs—the same kind of metrics dashboard a legitimate SaaS [software-as-a-service] platform would offer.”

Abnormal said the service also deftly intercepts and relays the victim’s MFA credentials, since the recipient who clicks the link is actually authenticating with the real site through a proxy, and any authentication tokens submitted are then forwarded to the legitimate service in real time.

“The attacker captures the resulting session cookies and tokens, giving them authenticated access to the account,” the researchers wrote. “When attackers relay the entire authentication flow in real time, MFA protections can be effectively neutralized despite functioning exactly as designed.”

![](https://krebsonsecurity.com/wp-content/uploads/2026/02/starkiller-urlmasker.png)

Starkiller is just one of several cybercrime services offered by a threat group calling itself **Jinkusu**, which maintains an active user forum where customers can discuss techniques, request features and troubleshoot deployments. One a-la-carte feature will harvest email addresses and contact information from compromised sessions, and advises the data can be used to build target lists for follow-on phishing campaigns.

This service strikes me as a remarkable evolution in phishing, and its apparent success is likely to be copied by other enterprising cybercriminals (assuming the service performs as well as it claims). After all, phishing users this way avoids the upfront costs and constant hassles associated with juggling multiple phishing domains, and it throws a wrench in traditional phishing detection methods like domain blocklisting and static page analysis.

It also massively lowers the barrier to entry for novice cybercriminals, Abnormal researchers observed.

“Starkiller represents a significant escalation in phishing infrastructure, reflecting a broader trend toward commoditized, enterprise-style cybercrime tooling,” their report concludes. “Combined with URL masking, session hijacking, and MFA bypass, it gives low-skill cybercriminals access to attack capabilities that were previously out of reach.”

*This entry was posted on Friday 20th of February 2026 03:00 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Abnormal AI](https://krebsonsecurity.com/tag/abnormal-ai/) [Callie Baron](https://krebsonsecurity.com/tag/callie-baron/) [Jinkusu](https://krebsonsecurity.com/tag/jinkusu/) [Piotr Wojtyla](https://krebsonsecurity.com/tag/piotr-wojtyla/) [Starkiller](https://krebsonsecurity.com/tag/starkiller/)

Post navigation

[← Kimwolf Botnet Swamps Anonymity Network I2P](https://krebsonsecurity.com/2026/02/kimwolf-botnet-swamps-anonymity-network-i2p/)

## 6 thoughts on “‘Starkiller’ Phishing Service Proxies Real Login Pages, MFA”

1. John [February 20, 2026](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/#comment-650771)

   Looks like Ai slop lol.

   [Reply](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/?replytocom=650771#respond) →
2. Carlos [February 20, 2026](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/#comment-650774)

   This article raises the question of which controls could effectively prevent such phishing attempts.

   [Reply](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/?replytocom=650774#respond) →

   1. Michael [February 20, 2026](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages...