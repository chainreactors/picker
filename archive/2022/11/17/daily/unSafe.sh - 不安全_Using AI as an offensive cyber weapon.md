---
title: Using AI as an offensive cyber weapon
url: https://buaq.net/go-135931.html
source: unSafe.sh - 不安全
date: 2022-11-17
fetch_date: 2025-10-03T22:58:14.623367
---

# Using AI as an offensive cyber weapon

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

Using AI as an offensive cyber weapon

The Offensive AI Research Lab’s report and survey show the broad range of activities that are made p
*2022-11-16 20:39:10
Author: [blog.avast.com(查看原文)](/jump-135931.htm)
阅读量:30
收藏*

---

The Offensive AI Research Lab’s report and survey show the broad range of activities that are made possible through offensive AI.

AI is a double-edged sword. It has enabled the creation of software tools that have helped to automate tasks such as prediction, information retrieval, and media synthesis, which have been used to improve various cyber defensive measures. However, AI has also been used by attackers to improve their malicious campaigns. For example, AI can be used to poison ML models and thus target their datasets and steal login credentials (think [keylogging](https://www.avast.com/c-keylogger?_ga=2.109815109.132975338.1668602021-273763872.1668602021), for example).

In our discussions about artificial intelligence (AI) and machine learning (ML), most of the time we focus on how to defend ourselves against attacks that are powered by AI systems, such as the creation of [deepfakes](https://www.avast.com/c-deepfake?_ga=2.109815109.132975338.1668602021-273763872.1668602021) or specially-crafted malware that can avoid detection. There is another side to this so-called offensive AI, and this is to use AI itself.

I recently spent some time at a newly created [Offensive AI Research Lab](https://offensive-ai-lab.github.io/) run by [Dr. Yisroel Mirsky](https://offensive-ai-lab.github.io/yisroel.mirsky/). The lab is part of one of the research efforts at the Ben Gurion University in Beersheva, Israel, and it’s just a few offices away from another lab [conducting air gap research](https://blog.avast.com/exploiting-air-gaps-avast?_ga=2.109815109.132975338.1668602021-273763872.1668602021) that we’ve previously written about.

The Offensive AI Research Lab does all kinds of experiments surrounding attacks on AI systems. While I was in Dr. Mirsky’s lab in Israel, I got to see one of its tools: A real-time deepfake audio generator that gave me chills.

The idea is to have a computer use snippets of your voice — either through a deliberate recording or something that is grabbed from the public domain, such as a speech or a podcast — to impersonate you. The generator just needs a few seconds of your voice to generate something very close. Using it, an attacker can have a conversation with someone who thinks they’re talking to you. Having this power to create a deepfake means that social engineering can happen to anyone, no matter how vigilant they are.

Mirsky is part of a team that published a report entitled “[The Threat of Offensive AI to Organizations](https://arxiv.org/pdf/2106.15764.pdf)”. The Offensive AI Research Lab’s report and survey show the broad range of activities (both negative and positive) that are made possible through offensive AI. The team found 24 of the 33 offensive AI capabilities that span automation, campaign resilience, credential theft, exploit development, information gathering, social engineering, and stealth.

## **What should businesses focus on to defend themselves against AI attacks?**

These capabilities listed above can pose significant business-related threats, so in a survey, the team behind the report polled experts from academia, industry, and government to understand which of these threats are actual concerns and why.

The survey found a dichotomy between industry and academia when it comes to their respective AI primary focus. “Industry is most concerned with AI being used for reverse engineering, with a focus on the loss of intellectual property. Academics, on the other hand, are most concerned about AI being used to perform biometric spoofing,” the authors write. There is one area of agreement, and that is the threat of impersonation, illustrated by my own experience at the lab.

However, this difference between the two groups is concerning. “Because of an AI’s ability to automate processes, adversaries may shift from having a few slow covert campaigns to having numerous fast-paced campaigns to overwhelm defenders and increase their chances of success,” said the authors. Think about that for a moment: Many of the past intrusions weren’t easily discovered, and many attackers have lived inside a business network for weeks or months. Some sources even cite an average of six months before being detected. Having a fast-moving AI attack could be devastating.

The report includes many other examples of AI-based attacks. For example, malicious AI can generate “master prints'', which are deepfakes of fingerprints that can open nearly any smartphone. They can also fool or evade many facial recognition systems. Additionally, other techniques can be used to slow down a surveillance camera until it is unresponsive.

The team’s survey found that there are three core motivations for an adversary to use offensive AI against an organization:

1. Coverage: AI can be used to automatically gather intelligence data, then craft and launch spear phishing attacks.
2. Speed: Machine learning can be used to help extract credentials and then intelligently select the next best target to pursue.
3. Success: For increasing success, AI can help make the phishing operation more covert by minimizing or camouflaging its malicious network traffic.

Although the authors believe that there will be an increase of offensive AI incidents, they don’t think it will be likely to see [botnets](https://www.avast.com/c-botnet) that can autonomously and dynamically interact with a diverse set of complex systems (like an organization’s network) in the near future. That’s a small comfort, but it’s not to say that the researchers don’t expect to see more and better deepfakes on the horizon as well.

文章来源: https://blog.avast.com/offensive-ai-report
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)