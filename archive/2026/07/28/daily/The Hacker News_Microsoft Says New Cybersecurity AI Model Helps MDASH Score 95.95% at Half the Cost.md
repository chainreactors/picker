---
title: Microsoft Says New Cybersecurity AI Model Helps MDASH Score 95.95% at Half the Cost
url: https://thehackernews.com/2026/07/microsoft-says-new-cybersecurity-ai.html
source: The Hacker News
date: 2026-07-28
fetch_date: 2026-07-29T05:04:27.632219
---

# Microsoft Says New Cybersecurity AI Model Helps MDASH Score 95.95% at Half the Cost

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Microsoft Says New Cybersecurity AI Model Helps MDASH Score 95.95% at Half the Cost](https://thehackernews.com/2026/07/microsoft-says-new-cybersecurity-ai.html)

**Swati Khandelwal**Jul 28, 2026AI Security / Vulnerability Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwmG858LYHQA-u4cQupdhqsi5oUcvLaQdoorupsW3tzPZvDg7kwgRIewOBPVNvp3Szfqb4VFJ_j6caul2NTIlm69_-vskp4gYQwVkQA59LbsMhOEO3yr4C48nhrO177ORbi9uFc_oIOrcXnCBs_dmPhVDZVZx9F3Cyp4RQKi71EhvfZQqmUKat36cbqEE/s1700-e365/MAI-Cyber-1-Flash.jpg)

Microsoft has launched its first cybersecurity-specific model inside **MDASH**, its multi-model vulnerability identification and remediation harness.

The company says MDASH, using MAI-Cyber-1-Flash and GPT-5.4, scored 95.95% on CyberGym. It also claims the configuration costs 50% less than its current best MDASH combination of GPT-5.4, GPT-5.4 mini, and GPT-5.3 Codex. Access is limited to approved MDASH customers through an Azure AI Foundry private preview.

**MAI-Cyber-1-Flash** is designed to handle up to 90% of MDASH tasks, with GPT-5.4 reserved for the hardest 10%. It is available only inside MDASH, not as a standalone public model or general-purpose application programming interface.

The headline score belongs to MDASH running MAI-Cyber-1-Flash alongside GPT-5.4, not to the new model by itself. CyberGym Level 1 is a known-vulnerability reproduction test. It gives an agent a vulnerability description and the corresponding unpatched source code, then checks whether it can produce a working proof of concept. It does not measure blind vulnerability discovery or whether a generated patch is correct.

CyberGym's [public leaderboard](https://www.cybergym.io/cybergym/) did not list Microsoft's 95.95% result when checked on July 28, 2026. It listed Wiz's [Atlas agent](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher) first at 90.9% in a July 27 entry, while Microsoft's May 12 MDASH submission remained at 88.4%. Microsoft's public materials do not say whether the result was submitted for listing.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Microsoft's earlier 96.55% MDASH result does not resolve the comparison. That June figure counted any crash, including non-target vulnerabilities. The July materials do not say whether the 95.95% result uses the same criterion, so the two scores cannot safely be read as a before-and-after performance trend.

According to Microsoft's [model card](https://microsoft.ai/pdf/MAI-Cyber-1-Flash-Model-Card.pdf), MAI-Cyber-1-Flash is a sparse mixture-of-experts transformer with 137 billion total parameters, five billion active parameters, and a 256,000-token context window. It is a cybersecurity fine-tune of [MAI-Code-1-Flash](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF), which was developed from a MAI-Thinking-1 mid-training checkpoint.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgazmP6BMN3M57ye7u-mMY9xJnDCbSof-iyyabOuYZED1wVlWfpc0AcS0ne_SOeGhZaQe3vCkusr4IZRLCo35JTOXTjvtzEF16gW_kc9xq41LNb8zgqnlDir9P121HsDnSEy9AheqiqBSwRZ1Gp_kgVsXfOHQT-axfciZF0bB8rI25dEgmMvdfNcgFwnl8/s1700-e365/cybergym.jpg)

The model card says the evaluated configuration replaced 80% of [MDASH's](https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html) existing models and raised the reported CyberGym result from 88.4% to 95.95%. That 80% figure is the share of models replaced. The separate 90% figure is the maximum share of tasks Microsoft says the smaller model can handle.

Taken together, the disclosed design points to routing as the central technical claim: MAI-Cyber-1-Flash is intended to handle most tasks, GPT-5.4 takes the hardest remainder, and Microsoft reports the outcome at the MDASH system level.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-0pDwWk82TIHOE4kinFAkFjZZvfAGWYr9H6PAEItaQNVkiresTVbsYlFHq8lTxSIMv8D1W0A27P4ebbNIIyUP7kJ2xFtJmLFr4bNDQd2lxpZuh2pJEBoYHuQBfjqyLvDWpR4_0kbEt51nmyM1WbfqMrF5drDa7M8n7_qO3eC1p4L0p3lAH3JipQbPpVA/s1700-e365/CyberGym-ms.jpg)

Microsoft's [launch announcement](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/) defines the 50% saving against its current best MDASH model mix of GPT-5.4, GPT-5.4 mini, and GPT-5.3 Codex. The product page separately describes the system as delivering "comparable performance at 50% of the cost of leading models." The announcement and model card do not disclose the token use, call volume, latency, task mix, or compute allocation behind that comparison, so the figure cannot yet be independently reproduced or normalised against other systems.

"The model is one input, the system around it is the product."

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3-o9La7DYm6jz5qcavVBLvRXUoQLqwrMmrvB529PbUxdg7TJZS3BMjVi4D7vd6V9vlSf_OX48mmXQWPgah_SPITaGgg4AP9YxB2AH-63YeWU39N3DXadwc_2zjIpTwCt0iyTdPZIM-KzKhDf_JDPWDGu3IbYfi1ilQE8Ly29HiKYagSIur-il4k7MMNv8/s728-e100/sygnia-d-3.png)](https://thn.news/sygnia-webinar)

Taesoo Kim, Microsoft's vice president of agentic security, used that distinction when [describing MDASH in June](https://www.microsoft.com/en-us/security/blog/2026/06/17/beyond-the-benchmark-advancing-security-at-ai-speed/). Under a lightweight terminal harness, the model card reports scores of 0.314 on CVEBench, 0.553 on CyberSecEval4 threat intelligence, 0.33 on its malware-analysis test, and 0.651 on CRSBench at POV=1200.

The model scored zero across the kernel, userspace, and browser categories of [ExploitGym](https://www.cybergym.io/exploitgym/), which asks agents to turn supplied vulnerabilities and crashing inputs into working code-execution exploits. Those results come from different tasks and scoring scales, so none is a standalone CyberGym score for MAI-Cyber-1-Flash.

Microsoft said all benchmark testing took place in a network-isolated environment with no ac...