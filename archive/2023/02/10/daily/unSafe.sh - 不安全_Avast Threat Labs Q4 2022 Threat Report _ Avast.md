---
title: Avast Threat Labs Q4 2022 Threat Report | Avast
url: https://buaq.net/go-148718.html
source: unSafe.sh - 不安全
date: 2023-02-10
fetch_date: 2025-10-04T06:12:32.723550
---

# Avast Threat Labs Q4 2022 Threat Report | Avast

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

Avast Threat Labs Q4 2022 Threat Report | Avast

Overall, the Threat Report found an increase in both human-centered and more technologically advance
*2023-2-9 21:11:28
Author: [blog.avast.com(查看原文)](/jump-148718.htm)
阅读量:31
收藏*

---

Overall, the Threat Report found an increase in both human-centered and more technologically advanced scams across the board.

The Avast Threat Labs Q4 2022 Threat Report observed a rise in social engineering attacks during the final quarter of 2022, including invoice and refund fraud, tech support scams, and others aimed at stealing money. Cybercriminals continued to engage in information theft and spying, with adware campaigns disguised as lottery offers used to collect personal information. Avast's threat researchers also uncovered zero-day exploits in Google Chrome and Windows, which have since been fixed.

“At the end of 2022, we have seen an increase in human-centered threats, such as scams tricking people into thinking their computer is infected, or that they have been charged for goods they didn’t order,” Avast Malware Research Director, Jakub Kroustek, says. “It’s human nature to react to urgency, fear and try to regain control of issues, and that’s where cybercriminals succeed.”

## Tech support scams and invoice and refund fraud

One such human-centered threat is [tech support scams](https://blog.avast.com/tech-support-fraud-avast). The report found that the top countries affected by tech support scams are the United States, Brazil, Japan, Canada, and France. These scams typically start with a pop-up window claiming a malware infection and urging the person to call a helpline for resolution. The scammers will then convince the caller that there’s a major infection on their device and that the only way to solve it is by allowing the scammer remote access.

“When people face surprising pop-up messages or emails, we recommend they stay calm and take a moment to think before they act,” Kroustek says. “Threats are so ubiquitous today that it’s hard for consumers to keep up. It is our mission to help protect people by detecting threats and alerting users before they can do any harm, using the latest AI-based technology.”

Avast Threat Labs also noted a significant increase in refund and invoice fraud, with a 14% increase from October to November 2022 and a 22% increase in December. Refund and invoice fraud are prevalent forms of deception that closely resemble tech support scams. The perpetrators of these scams often utilize emails that appear to originate from a trustworthy organization and may include false receipts to create the illusion of unauthorized charges.

The intended victim is typically directed to contact a specific telephone number, where an individual posing as an agent will request access to the individual's computer and financial accounts. The ultimate objective of the attacker is to steal the victim's funds. In the case of invoice fraud, entities, particularly businesses, may receive bills for goods or services that they never ordered or received. It is imperative to exercise caution and thoroughly verify all claims before divulging any confidential information.

“To avoid invoice fraud, people need to pay close attention to invoices they receive,” Kroustek says. “Fraudulent invoices often look legitimate, and people need to verify whether an order really was made, the service received, and whether the sender is truly who they pretend to be.”

## Increase in information-stealing adware, remote access trojans, and bots

The team also noted an increase in [adware](https://www.avast.com/c-adware). Not only do they provide an unpleasant user experience through the display of intrusive ads, but they may also compromise personal data.

For instance, unsuspecting individuals may be prompted to participate in a lottery or spin a roulette wheel, and are then asked to provide contact information and pay a "handling fee" using their credit card, Google Pay, or Apple Pay account.

Avast researchers also noted an increase in the prevalence of DealPly adware, which comes as a Google Chrome extension and transfers statistical and search information to the attackers. The risk of infection from DealPly has risen globally, with particularly significant increases observed in the Americas, Europe, and South and Southeast Asia.

In addition to these scams, Avast threat researchers also observed a significant increase in the spread of information-stealing malware, remote access trojans, and botnets. For example, the global spread of the Arkei information stealer rose by 437% in the past period. This information stealer is known for compromising data from browsers' autofill forms, passwords, and other sources.

There was also a 57% increase in people and businesses protected against AgentTesla, a form of malware that is frequently spread through phishing emails aimed at businesses and is designed to steal credentials. A 37% increase in the spread of RedLine stealer was also noted. This stealer commonly spreads through cracked games and services, stealing information from browsers and crypto wallets.

Avast telemetry data also indicates that the spread of LimeRAT globally tripled in the fourth quarter. LimeRAT, a remote access trojan, is capable of stealing passwords, cryptocurrencies, executing DDoS attacks, and installing [ransomware](https://www.avast.com/c-what-is-ransomware) on a victim's computer. The majority of its activity was observed in South and Southeast Asia and Latin America.

The [Emotet botnet](https://blog.avast.com/why-emotet-remains-an-active-threat-avast), another malware distributor with extensive capabilities for stealing information and spreading malware, has recently evolved its evasion tactics against antivirus software through the use of timers to gradually continue the execution of its payload. The Qakbot information stealer botnet has also progressed and started using "HTML smuggling" to conceal an encoded malicious script within an email attachment. For instance, threat actors have started exploiting SVG images to hide malicious payloads and the code utilized for its reassembly.

## Zero-day exploits

During the quarter, Avast's researchers discovered two advanced [zero-day exploits](https://www.avast.com/c-zero-day) that were actively being utilized. Both exploits were mitigated by Avast, ensuring the protection of its users. The first exploit, identified as CVE-2022-3723, was a type confusion vulnerability in V8 and was utilized to achieve Remote Code Execution (RCE) against Google Chrome. Avast promptly reported this vulnerability to Google, which quickly released a patch on October 27, 2022, within just two days. The second zero-day exploit, CVE-2023-21674, was a Local Privilege Escalation (LPE) vulnerability in ALPC that allowed attackers to bypass the browser sandbox and gain access to the Windows kernel. This exploit was addressed by Microsoft in the January 2023 Patch Tuesday update.

Overall, the Threat Report found an increase in both human-centered and more technologically advanced scams across the board. It’s a good reminder that cybercriminals are always working to manipulate and scam everyday people. Remember: Don’t click on suspicious links, take a minute to assess before responding, and never give anyone remote access to your device.

Check out the [complete Q4 2022 Threat Report](https://decoded.avast.io/threatresearch/avast-q4-2022-threat-report/) on Avast Decoded.

文章来源: https://blog.avast.com/avast-q4-2022-threat-report
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://gi...