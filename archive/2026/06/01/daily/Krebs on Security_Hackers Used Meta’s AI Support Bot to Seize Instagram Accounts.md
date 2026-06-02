---
title: Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts
url: https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/
source: Krebs on Security
date: 2026-06-01
fetch_date: 2026-06-02T06:33:21.045841
---

# Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts

Advertisement

[![](/b-knowbe4/48.jpg)](https://www.knowbe4.com/training-humans-ai-agents?utm_source=krebs&utm_medium=display&utm_campaign=traininghumansandai&utm_content=bannerai)

Advertisement

[![](/b-doppel/14.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=deepfake)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts

June 1, 2026

[10 Comments](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/#comments)

The **Instagram** accounts for the Obama White House and the Chief Master Sergeant of the U.S. Space Force were briefly defaced with pro-Iranian images and messages over the weekend, after instructions began circulating on Telegram showing how to trick Meta’s “AI support assistant” bot into resetting account passwords.

![](https://krebsonsecurity.com/wp-content/uploads/2026/06/metasupportbot.png)

On May 31, word began to spread on several Telegram instant message channels that Meta’s AI bot would happily add an email address to an existing account as part of the bot’s standard password reset flow.

A video released on Telegram by pro-Iran hackers claimed to document a remarkably simple exploit that appears to have involved using a VPN connection with an IP address that is in or near the target’s usual hometown, requesting a password reset for the account, and then choosing to chat with Meta’s AI support assistant. From there, the video shows the attacker told the bot to link the account in question to a new email address, after which the bot dutifully sent that address a one-time code that allowed a password reset.

The Telegram account that posted the video also linked to screenshots of pro-Iran images, videos and messages that defaced the hacked Instagram accounts, saying hackers had used the exploit to hijack a number of valuable (read: short) Instagram account names that allegedly have a resale value of more than a half million dollars.

Meta has not responded to requests for comment on the video’s claims, but Meta’s Andy Stone [said](https://x.com/andymstone/status/2061486724199379186?s=46&t=7_s0It7Iv8WMHpe2Sun-mA) on Twitter/X that the issue had been resolved and that they were securing impacted accounts. The security blog thecybersecguru.com [reports](https://thecybersecguru.com/news/instagram-meta-ai-vulnerability-account-recovery-exploit/) that Meta pushed an emergency patch over the weekend, and clarified that no back end database was breached.

“Instagram has notoriously poor human support infrastructure,” Cybersecguru wrote. “Recovering a locked account – especially a high-value one can take weeks of back-and-forth with an automated ticketing system. Meta’s solution was to deploy a conversational AI layer to handle common recovery workflows: relinking a lost email address, triggering a password reset, verifying account ownership. The assistant, presumably, was supposed to reduce friction for legitimate users stuck in account-access hell.”

**Ian Goldin**, a threat researcher at Lumen’s **Black Lotus Labs**, said we’re entering unchartered security territory as more large online platforms start allowing AI chatbots to handle sensitive account recovery requests. Just like human customer support employees can be social engineered into providing unauthorized access to someone’s account, AI bots are equally eager to help and vulnerable to persuasion and trickery, he said.

“AI chatbots create interesting new attack surface, and we’re likely going to see a lot more of these kinds of attacks,” Goldin said.

Securing your various online accounts means taking full advantage of the most secure form of multi-factor authentication (MFA) offered (such as a passkey or security key). In this case, even using the least robust form of MFA that Instagram offers — a one-time code sent via SMS — likely would have blocked the exploit: The hackers who released the video on Telegram said their exploit failed to work against any accounts that had MFA enabled.

*This entry was posted on Monday 1st of June 2026 01:32 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Black Lotus Labs](https://krebsonsecurity.com/tag/black-lotus-labs/) [Ian Goldin](https://krebsonsecurity.com/tag/ian-goldin/) [Instagram](https://krebsonsecurity.com/tag/instagram/) [Meta](https://krebsonsecurity.com/tag/meta/)

Post navigation

[← Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

## 10 thoughts on “Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts”

1. Cereal [June 1, 2026](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/#comment-656070)

   One word to sum it all up “meta”

   [Reply](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/?replytocom=656070#respond) →
2. CyberScrewed [June 1, 2026](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/#comment-656071)

   AI just making the attack surface exponentially broader. Great work

   [Reply](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/?replytocom=656071#respond) →

   1. Wannabe Techguy [June 1, 2026](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/#comment-656075)

      Yes and everyone is infatuated with it.

      [Reply](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/?replytocom=656075#respond) →

      1. mealy [June 1, 2026](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/#comment-656082)

         it’s wildly unpopular among broad swaths in my area, where it’s supposedly being born.

         More a ‘necessary business evil’ like LinkedIn now. AI hiring you, AI monitoring you, AI firing you. Be mindful – there is additional surveillance scrutiny upon any who voice negative opinions about AI or their world-devouring “for profit!…” datacenters, so be sure to smile at the camera and tip your incompetent-replacement-theory robot overlords. They are watching, evaluating your continued usefulness and impending moment of equal value replacement at current human flesh prices. And if you don’t ‘like’ it, you must be a Luddite or something. Potentially a threat for Google’s project purple.

         [Reply](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/?replytocom=656082#respond) →
3. Steve [June 1, 2026](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/#comment-656072)

   Even when security expectations may be low for the likes of Meta, this is a flat-out unforgivable security flaw.

   [Reply](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/?replytocom=656072#respond) →
4. Sasha [June 1, 2026](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/#comment-656073)

   Gee, how timely. Last week I got a few emails from IG saying that they were sorry I was having trouble accessing my account. Someone was obviously trying to reset the password, so I...