---
title: Protect Your iOS Devices with Cortex XDR Mobile
url: https://www.paloaltonetworks.com/blog/2022/12/ios-devices-with-cortex-xdr-mobile/
source: Palo Alto Networks Blog
date: 2022-12-06
fetch_date: 2025-10-04T00:36:58.268270
---

# Protect Your iOS Devices with Cortex XDR Mobile

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Announcement](https://www.paloaltonetworks.com/blog/category/announcement/)
* Protect Your iOS Devices ...

# Protect Your iOS Devices with Cortex XDR Mobile

Link copied

By [Kasey Cross](/blog/author/kasey-cross/ "Posts by Kasey Cross")

Dec 05, 2022

8 minutes

[Announcement](/blog/category/announcement/)

[Must-Read Articles](/blog/security-operations/category/must-read-articles/)

[Product Features](/blog/security-operations/category/product-features/)

[Products and Services](/blog/category/products-and-services/)

[Cortex XDR](/blog/tag/cortex-xdr/)

[Cortex XDR 3.5](/blog/tag/cortex-xdr-3-5/)

[Cortex XDR Mobile](/blog/tag/cortex-xdr-mobile/)

[Ignite '22](/blog/tag/ignite-22/)

[iOS](/blog/tag/ios/)

#### **Cortex XDR 3.5 and Cortex XDR Agent 7.9 Deliver Stronger Security, Better Search and Broader Coverage, Including iOS Support**

Your employees probably expect to work from anywhere, at any time they want, on any device. With the rise of remote work, users are accessing business apps and data from mobile devices more than ever before. Cortex XDR Mobile for iOS lets you protect your users from mobile threats, such as malicious URLs in text messages and malicious or unwanted spam calls.

Cortex XDR Mobile for iOS is just one of over 40 new features in our **Cortex XDR 3.5** and **Cortex XDR Agent 7.9** releases. In addition to iOS protection, we’ve bolstered endpoint security, improved the flexibility of XQL Search, and expanded visibility and normalization to additional data sources. Even more new advancements make it easier than ever to manage alert exceptions and granularly control access to alerts and incidents.

Let’s dive in and take a deeper look at the new capabilities of Cortex XDR 3.5 and Cortex XDR Agent 7.9.

## iOS Protection with Cortex XDR Mobile

With the rapid shift to remote work, flexible BYOD policies are a must have, now, for many companies. Whether employees are working at home, from a café, or in a corporate office, they often have a phone within reach, and for good reason. [62% of U.S. workers](https://trucesoftware.com/my-work-my-phone/) say mobile phones or tablets help them be productive at work, according to a broad 2021 survey.

#### Phishing and Smishing and Spam, Oh My!

| If you own a smartphone (like [85% of Americans](https://www.pewresearch.org/internet/fact-sheet/mobile/) do) you’ve probably received suspicious text messages claiming your bank or Amazon or PayPal account has been blocked. Or you’ve received messages saying that you need to click a link to complete a USPS shipment. And if you are receiving these messages, you can assume your users are also receiving similar messages. It’s only a matter of time before a user clicks one of these links and supplies their credentials, possibly even the same credentials they use at work. These smishing attacks, or phishing performed through SMS, are on the rise.  If your organization is like many others, you’ve probably deployed an email security solution that filters spam and phishing URLs. However, you may not be protecting your mobile devices – BYOD or corporate-owned – from spam calls and phishing attacks. | ![Screenshot of being protected by Cortex XDR, showing security events.](/blog/wp-content/uploads/2022/12/word-image-22.png) |
| --- | --- |

With Cortex XDR Mobile for iOS, you can now secure iOS devices from advanced threats like smishing. The Cortex XDR agent blocks malicious URLs in SMS messages with URL filtering powered by Unit 42 threat intelligence. It can also block spam calls, safeguarding your users from unwanted and potentially fraudulent calls. Users can also report a spam call or message, allowing the Cortex XDR administrator to block the phone number.

#### Hunting Down Jailbroken Devices

Some of your iPhone users might “jailbreak” their phones to remove software restrictions imposed by Apple. Once they gain root access to their phones, they can install software not available in the App Store. Jailbreaking increases the risk of downloading malware. It can also create stability issues.

The Cortex XDR agent detects jailbroken devices, including evasion techniques designed to thwart security tools. Overall, the Cortex XDR provides strong protection for iPhones and iPads, while balancing privacy and usability requirements.

Now you can protect a broad set of endpoints, mobile devices and cloud workloads in your organization, including Windows, Linux, Mac, Android, Chrome and now iOS, with the Cortex XDR agent.

## **In-Process Shellcode Protection**

Threat actors can attempt to bypass endpoint security controls using shellcode to load malicious code into memory. Cortex XDR’s patent-pending in-process shellcode protection module blocks these attempts. To understand how, let’s look at a common attack sequence.

After threat actors have gained initial access to a host, they typically perform a series of steps, including analyzing the host operating system and delivering a malicious payload to the host.

They may use a stager to deliver the payload directly into memory rather than installing malware on the host machine. By loading the payload directly into memory, they can circumvent many antivirus solutions that will either ignore or perform more limited security checks on memory.

Many red team tools or hacking tools, such as Cobalt Strike, Sliver or [Brute Ratel](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/), have made it easier for attackers to perform these sophisticated steps.

If a process, including a benign process, executes and allocates memory in a suspicious way, the Cortex XDR agent will single out that memory allocation and extract and analyze the buffer. If the Cortex XDR agent detects any signature or indicator that the payload is malicious, the agent conducts additional analysis on the process and shellcode, including analyzing the behavior of the code and the process, using EDR data enrichment.

If the Cortex XDR agent determines the shellcode or the process loaded by the shellcode are malicious, it will terminate the process that loaded the shellcode and the allocated memory. By killing the process chain, or the “causality,” Cortex XDR prevents the malicious software from executing.

![In-process shellcode protection is a patent-pending technology that helps detect and prevent the use of hacking tools and malware.](/blog/wp-content/uploads/2022/12/word-image-23.png)

Our in-process shellcode protection will block red team and hacking tools from loading malicious code, without needing to individually identify and block each tool.

###### This means that if a never-before-seen hacking tool is released, Cortex XDR can prevent the tool from using shellcode to load a payload into memory.

Cortex XDR will terminate the implant once it's loaded on the machine before it can do anything malicious.

## **Financial Malware and Cryptomining Protection**

Whether stealing from bank accounts or mining for cryptocurrency, cybercriminals always have new tricks up their collective sleeves. To combat these dangerous threats, we’ve added two new behavior-based protection modules in Cortex XDR Agent 7.9. Let’s take a brief look at these threats and how you can mitigate them with Cortex XDR.

[Banking Trojans](https://unit42.paloaltonetworks.com/banking-trojan-techniques/) emerged over a decade ago, typically stealing banking credentials by manipulating web browser sessions and logging keystrokes. Criminals deployed large networks of Trojans, such as Zeus, Trickbot, Emotet and Dridex, over the years. They infected millions of computers, accessed bank accounts, and transferred funds from victims. Now, threat actors often use these Trojans to deliver other types of malware to victims’ devices, like ransomware.

[Cryptojacking](/blog/security-operations/stopping-cryptojacking-attacks-with-and-without-an-agent/), or...