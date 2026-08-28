---
title: New GPUThor Rowhammer Defeats ECC on NVIDIA RTX A6000 to Gain Host Root Access
url: https://thehackernews.com/2026/08/gputhor-rowhammer-defeats-ecc-on-nvidia.html
source: The Hacker News
date: 2026-08-27
fetch_date: 2026-08-28T13:37:59.538859
---

# New GPUThor Rowhammer Defeats ECC on NVIDIA RTX A6000 to Gain Host Root Access

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [New GPUThor Rowhammer Defeats ECC on NVIDIA RTX A6000 to Gain Host Root Access](https://thehackernews.com/2026/08/gputhor-rowhammer-defeats-ecc-on-nvidia.html)

**Swati Khandelwal**Aug 27, 2026Hardware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2AxQ4SD6_1WKkpvBVi_M7oKLMeBAiKU4Ek4HbnJXHLX5xSbUg7ky1ITdUJY91n-zZGyK55-qQRd24PWRymLmik7cRl4CYPoaeZL5JuLedlsOTJGHChwF1eQWGhUE6AhOZUSW7CoajwQcKCu8E_zrYn8I6203Nrvr9NvheYL-5ISm0fs1xdWNiKGWqIs0/s1700-e365/nvidia-bits.jpg)

Academic researchers have disclosed a Rowhammer attack impacting NVIDIA workstation GPUs with GDDR6 memory that defeats error correction codes (ECC), the mitigation NVIDIA recommends against GPU Rowhammer, and enables denial-of-service (DoS) and privilege escalation to a root shell.

Dubbed **GPUThor**, the attack was developed by researchers at the University of Toronto, who hammered four DRAM banks for 24 hours each on four Ampere-class cards, inducing bit flips on each.

The following GPUs were tested and found vulnerable -

* RTX A6000 (48 GB GDDR6)
* RTX A5000 (24 GB GDDR6)
* RTX A4500 (20 GB GDDR6)
* RTX A4000 (16 GB GDDR6)

Mounting the attack requires the ability to launch an unprivileged CUDA kernel on the target GPU, either as a co-tenant on a shared card or as untrusted code on a single-tenant machine. The researchers advise avoiding cross-tenant GPU sharing, monitoring ECC error counters, and restricting untrusted CUDA workloads.

"Recently, researchers at the University of Toronto demonstrated a successful Rowhammer exploitation on an NVIDIA A6000 GPU with GDDR6 memory where System-Level ECC was not enabled. In the same paper, the researchers showed that enabling System-Level ECC mitigates the Rowhammer problem," NVIDIA said in [a July 2025 security notice](https://nvidia.custhelp.com/app/answers/detail/a_id/5671).

That notice followed GPUHammer, the same team's earlier work, and [the first GPU Rowhammer attack](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html) demonstrated on NVIDIA hardware, which yielded 16-bit flips per gigabyte on an RTX A6000 and was neutralized once ECC was enabled.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

What GPUThor adds is non-uniform hammering, where the aggressor row next to the victim is activated far more often than the decoy rows used to swamp the memory's Target Row Refresh (TRR) defense. Prior GPU attacks activated aggressor and decoy rows at roughly the same rate.

The researchers found that repeated accesses issued inside a single warp, the group of 32 threads a GPU runs in lockstep, are merged at the memory controller into a single DRAM activation.

Accesses issued from different warps to different cache lines within the same row survive as separate activations, and the hammering kernels distribute them accordingly.

They also reported in the [GPUThor paper](https://gururaj-s.github.io/assets/pdf/CCS26_GPUThor.pdf) that TRR on these GDDR6 parts likely applies about once every 72 refresh intervals rather than once per interval, and built a six-interval pattern around that schedule.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQswFpRMIX5gG_g40EtMGn3N_sK_jVIfsbWAmoitGC2pvlg7xvocS-3gX6UKhU9qUFyGY1qT_3wZMOMaPdf34nz3h_WUNGfh1AVcwsoqE9r3d9TJnIh4jC3dacb08tQT392HDkPzJbEV2wMCcpxL-0ln3uTUahvpWaIPcGfAJ14E30XKRl_ombY8tnzmQ/s1700-e365/bits.jpg)

Across the four cards, the campaigns produced 72,000 to 377,000 bit flips per gigabyte with ECC disabled.

The RTX A5000 was the most susceptible at 377,552 flips per gigabyte, which is 23,597 times GPUHammer's 16 flips per gigabyte and roughly 500 times the 758 flips per gigabyte reported for GDDRHammer, the strongest prior GPU Rowhammer attack.

The paper places the A5000 rate close to the roughly 550,000 flips per gigabyte reached by Blacksmith, which established [non-uniform hammering on DDR4](https://thehackernews.com/2021/11/new-blacksmith-exploit-bypasses-current.html) as a route past in-DRAM defenses.

At a 16-byte granularity, the campaigns turned up 387 double-bit flips and two triple-bit flips across the four cards with ECC disabled, with the A5000 accounting for 306 of the double-bit flips and both triple-bit flips.

The single-error-correct, double-error-detect (SECDED) ECC on these GPUs corrects one flipped bit in a protected chunk and detects two, and the researchers found that it mis-corrects three, resulting in silent data corruption (SDC).

With ECC enabled on a locally owned RTX A6000, one bank of hammering produced 11 detectable, uncorrectable errors (DUE) and one SDC over a day, an average of one DUE every two hours. Each DUE aborts all kernels running on the card, leaving it unusable until a reset.

For the escalation itself, the researchers reused the exploit code from GPUBreach, their earlier [GPU page-table privilege escalation](https://thehackernews.com/2026/04/new-gpubreach-attack-enables-full-cpu.html) research.

Page tables are first massaged into a vulnerable row. The neighboring rows are then hammered to corrupt the page-frame number of an entry. A second kernel reaches memory outside the process through the tampered entry.

Using the triple-bit SDC, the researchers obtained root on the host with the IOMMU enabled. Using a double-bit DUE, they achieved host-side privilege escalation on systems where the IOMMU is disabled. A page-table entry is repointed at CPU memory. The process credential structure is then overwritten.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3LbYA7qJ9a4i5qFKNOA7R-E69EMwKknI28ULQHAPhNS-ZiWw5BRigu3Aj17MU-WCDMgWFMsBmEo88qzLHGKg7pVTnLmR4rt4pQ4lpZG-ovFBc0kQp45bsGK3nLKimNT4phida3FO1F-Cc7fV1tWdEKa1fxMTV56p269VVO8IuwtNB80YP0YlYG15jxmU/s1700-e365/flips.jpg)

"Moreover, we discover that even double-bit DUEs are exploitable, since DUEs are serviced lazily in NVIDIA GPUs, lea...