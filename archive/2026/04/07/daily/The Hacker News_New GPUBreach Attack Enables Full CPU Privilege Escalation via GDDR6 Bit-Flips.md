---
title: New GPUBreach Attack Enables Full CPU Privilege Escalation via GDDR6 Bit-Flips
url: https://thehackernews.com/2026/04/new-gpubreach-attack-enables-full-cpu.html
source: The Hacker News
date: 2026-04-07
fetch_date: 2026-04-08T04:39:12.173286
---

# New GPUBreach Attack Enables Full CPU Privilege Escalation via GDDR6 Bit-Flips

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [New GPUBreach Attack Enables Full CPU Privilege Escalation via GDDR6 Bit-Flips](https://thehackernews.com/2026/04/new-gpubreach-attack-enables-full-cpu.html)

**Ravie Lakshmanan**Apr 07, 2026Vulnerability / Hardware Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD7E4oEicfW1OaHztWEuM4qrsJFnHRPJ41f8R-2VeKUFV3Y59XaBUctumc2R91miQ3dMPnwkEcpPMqFErKmPRJhS3VRceve1GOSGGUsP6WHGIfoQAuVV10JVy312CxGYvmb2xA_eQtuO69bNb-1NzYln9P4xbsFDoPgWG3BEdri4sRRj415XQr1NENZBh0/s1700-e365/grpu.jpg)

New academic research has identified multiple RowHammer attacks against high-performance graphics processing units (GPUs) that could be exploited to escalate privileges and, in some cases, even take full control of a host.

The efforts have been codenamed **[GPUBreach](https://gpubreach.ca/)**, **[GDDRHammer](https://gddr.fail/)**[, and](https://gddr.fail/) **[GeForge](https://gddr.fail/)**.

GPUBreach goes a step further than [GPUHammer](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html), demonstrating for the first time that RowHammer bit-flips in GPU memory can induce much more than data corruption and enable privilege escalation, and lead to a full system compromise.

"By corrupting GPU page tables via GDDR6 bit-flips, an unprivileged process can gain arbitrary GPU memory read/write, and then chain that into full CPU privilege escalation — spawning a root shell — by exploiting memory-safety bugs in the NVIDIA driver," Gururaj Saileshwar, one of the authors of the study and Assistant Professor at the University of Toronto, [said](https://www.linkedin.com/posts/gururaj-saileshwar-080a4526_gpubreach-activity-7445871096840712193-FSM5/) in a post on LinkedIn.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

What makes GPUBreach notable is that it works even without having to disable the input–output memory management unit ([IOMMU](https://link.springer.com/article/10.1186/s13173-017-0066-7)), a [crucial hardware component](https://thehackernews.com/2025/12/new-uefi-flaw-enables-early-boot-dma.html) that ensures memory security by preventing Direct Memory Access (DMA) attacks and isolating each peripheral to its own memory space.

"GPUBreach shows it is not enough: by corrupting trusted driver state within IOMMU-permitted buffers, we trigger kernel-level out-of-bounds writes — bypassing IOMMU protections entirely without needing it disabled," Saileshwar added. "This has serious implications for cloud AI infrastructure, multi-tenant GPU deployments, and HPC environments."

RowHammer is a long-standing Dynamic Random-Access Memory (DRAM) reliability error where repeated accesses (i.e., hammering) to a memory row can cause electrical interference that flips bits (changing 0 to 1m or vice versa) in adjacent rows. This undermines isolation guarantees fundamental to modern operating systems and sandboxes.

DRAM manufacturers have implemented hardware-level mitigations, such as Error-Correcting Code (ECC) and Target Row Refresh (TRR), to counter this line of attack.

However, research published in July 2025 by researchers at the University of Toronto expanded the threat to GPUs. [GPUHammer](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html), as it's called, is the first practical RowHammer attack targeting NVIDIA GPUs using GDDR6 memory. It employs techniques like multi-threaded parallel hammering to overcome architectural challenges inherent to GPUs that previously made them immune to bit flips.

The consequence of a successful GPUHammer exploit is a drop in machine learning (ML) model accuracy, which can degrade by up to 80% when running on a GPU.

GPUBreach extends this approach to corrupt GPU page tables with RowHammer and achieve privilege escalation, resulting in arbitrary read/write on GPU memory. More consequentially, the attack has been found to leak secret cryptographic keys from [NVIDIA cuPQC](https://developer.nvidia.com/cupqc), stage model accuracy degradation attacks, and obtain CPU privilege escalation with IOMMU enabled.

"The compromised GPU issues DMA (using the aperture bits in PTEs) into a region of CPU memory that the IOMMU permits (the GPU driver's own buffers)," the researchers said. "By corrupting this trusted driver state, the attack triggers memory-safety bugs in the NVIDIA kernel driver and gains an arbitrary kernel write primitive, which is then used to spawn a root shell."

This disclosure of GPUBreach coincides with two other concurrent works – GDDRHammer and GeForge – that also revolve around GPU page-table corruption via GDDR6 RowHammer and facilitate GPU-side privilege escalation. Just like GPUBreach, both techniques can be used to gain arbitrary read/write access to CPU Memory.

Where GPUBreach stands apart is that it also enables full CPU privilege escalation, making it a more potent attack. GeForge, in particular, requires IOMMU to be disabled for it to work, whereas GDDRHammer modifies the GPU page table entry's aperture field to allow the unprivileged [CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) kernel to read and write all of the host CPU's memory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"One main difference is that GDDRHammer exploits the last level page table (PT) and GeForge exploits the last level page directory (PD0)," the teams behind the two GPU memory exploits said. "However, both works are able to achieve the same goal of hijacking the GPU page table translation to gain read/write access to the GPU and host memory."

One temporary mitigation to tackle these attacks is to [enable ECC](https://nvidia.custhelp.com/app/answers/detail/a_id/5671) on the GPU. That said, it bears noting that RowHammer attacks like [ECCploit](https://thehackernews.com/2021/04/new-javascript-exploit-can-now-carry.html) and [ECC.fail](https://thehackernews...