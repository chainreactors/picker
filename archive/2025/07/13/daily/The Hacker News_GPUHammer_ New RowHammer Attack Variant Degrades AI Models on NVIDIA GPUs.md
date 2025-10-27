---
title: GPUHammer: New RowHammer Attack Variant Degrades AI Models on NVIDIA GPUs
url: https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html
source: The Hacker News
date: 2025-07-13
fetch_date: 2025-10-06T23:39:28.275451
---

# GPUHammer: New RowHammer Attack Variant Degrades AI Models on NVIDIA GPUs

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [GPUHammer: New RowHammer Attack Variant Degrades AI Models on NVIDIA GPUs](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html)

**Jul 12, 2025**Ravie LakshmananAI Security / Vulnerability

[![New RowHammer Attack on NVIDIA GPUs](data:image/png;base64... "New RowHammer Attack on NVIDIA GPUs")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqlU3VgWH5RyCKaK7c2rSGZN1X1xRPWy6H1Pyz5DWeyvEf6GbAsHgA4N-f137-U5FXecV-uFjNqOiM6fhYtwvJI3dxifgpTU_UshZAQexecIc8GokTxiKBSZ1zcygCP5iMU8kN61O6OzcrlXitW-JSqpNg9nwipmQuO2P0Sw5IgLH4C8m5S2Wdgk8TSBrE/s790-rw-e365/gpu-hammer.jpg)

NVIDIA is urging customers to enable **System-level Error Correction Codes (ECC)** as a defense against a variant of a RowHammer attack demonstrated against its graphics processing units (GPUs).

"Risk of successful exploitation from RowHammer attacks varies based on DRAM device, platform, design specification, and system settings," the GPU maker [said](https://nvidia.custhelp.com/app/answers/detail/a_id/5671) in an advisory released this week.

Dubbed [GPUHammer](https://gpuhammer.com), the attacks mark the first-ever RowHammer exploit demonstrated against NVIDIA's GPUs (e.g., NVIDIA A6000 GPU with GDDR6 Memory), causing malicious GPU users to tamper with other users' data by triggering bit flips in GPU memory.

The most concerning consequence of this behavior, University of Toronto researchers found, is the degradation of an artificial intelligence (AI) model's accuracy from 80% to less than 1%.

[RowHammer](https://arxiv.org/abs/2211.07613) is to modern DRAMs just like how [Spectre and Meltdown](https://thehackernews.com/2024/10/new-research-reveals-spectre.html) are to contemporary CPUs. While both are hardware-level security vulnerabilities, RowHammer targets the physical behavior of DRAM memory, whereas Spectre [exploits](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html) speculative execution in CPUs.

RowHammer [causes](https://thehackernews.com/2024/03/new-zenhammer-attack-bypasses-rowhammer.html) bit flips in nearby memory cells due to electrical interference in DRAM stemming from repeated memory access, while [Spectre and Meltdown](https://www.redhat.com/en/blog/what-are-meltdown-and-spectre-heres-what-you-need-know) allow attackers to [obtain privileged information](https://thehackernews.com/2021/05/new-spectre-flaws-in-intel-and-amd-cpus.html) from memory via a side-channel attack, potentially leaking sensitive data.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In 2022, academics from the University of Michigan and Georgia Tech described a technique called [SpecHammer](https://ieeexplore.ieee.org/document/9833802) that combines RowHammer and Spectre to launch speculative attacks. The approach essentially entails triggering a Spectre v1 attack by using Rowhammer bit-flips to insert malicious values into victim gadgets.

GPUHammer is the latest variant of RowHammer, capable of inducing bit flips in NVIDIA GPUs even with mitigations like target refresh rate (TRR) in place. Unlike CPUs, which have benefited from years of side-channel defense research, GPUs often lack parity checks and instruction-level access controls, leaving their memory integrity more exposed to low-level fault injection attacks.

In a proof-of-concept developed by the researchers, using a single-bit flip to tamper with a victim's ImageNet deep neural network (DNN) models can degrade model accuracy from 80% to 0.1%. It's a clear sign that GPUHammer isn't just a memory glitch—it's part of a broader wave of attacks targeting the core of AI infrastructure, from GPU-level faults to data poisoning and model pipeline compromise.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5-n62G3v4muZX82pVc4cN1laCvZl4zhs_b2fipVNWadyLQOLH__NGEvwiUxsR4Cdq9fi6bI6aBZSHcWaukaf_kpI5biQ1C120HKHl95GS82Xhe2EcCgtAhAd-8Vay-1L1jYMbYu_yKw6vtxX3DrguglSna3Zq4M59zd6becpn85XGID0gIEgjEr4hQ60g/s790-rw-e365/data.png)

Exploits like GPUHammer threaten the integrity of AI models, which are increasingly reliant on GPUs to perform parallel processing and carry out computationally demanding tasks, not to mention open up a new attack surface for cloud platforms.

In shared GPU environments like cloud ML platforms or VDI setups, a malicious tenant could potentially launch GPUHammer attacks against adjacent workloads, affecting inference accuracy or corrupting cached model parameters without direct access. This creates a cross-tenant risk profile not typically accounted for in current GPU security postures.

This development ties into broader concerns around AI model reliability and adversarial ML, where attackers exploit input or memory vulnerabilities to manipulate outputs. GPUHammer represents a new class of attacks that operate below the model layer—altering internal weights instead of external data.

Its implications extend to edge AI deployments, autonomous systems, and fraud detection engines, where silent corruption may not be easily caught or reversed.

To mitigate the risk posed by GPUHammer, it's advised to enable ECC through "nvidia-smi -e 1." Users can verify ECC status by running nvidia-smi -q | grep ECC, which reports whether ECC is supported and currently enabled.

To minimize impact while maintaining protection, some configurations allow ECC to be selectively enabled only for training nodes or high-risk workloads. It's also good practice to monitor GPU error logs (/var/log/syslog or dmesg) for ECC-related corrections, which can signal ongoing bit-flip attempts.

Newer NVIDIA GPUs like H100 or RTX 5090 are not affected due to them featuring [on-die ECC](https://ieeexplore.ieee.org/document/8809496), which helps [detect and correct errors](https://arxiv.org/abs/2204.10387) arising due to voltage fluctuations associated with smaller, denser memory chips.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Enabling Error Corr...