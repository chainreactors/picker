---
title: My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI
url: https://infosecwriteups.com/my-llm-bug-bounty-journey-on-hugging-face-hub-via-protect-ai-9f3a1bc72c2e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-13
fetch_date: 2025-10-06T17:14:51.330158
---

# My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9f3a1bc72c2e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-llm-bug-bounty-journey-on-hugging-face-hub-via-protect-ai-9f3a1bc72c2e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-llm-bug-bounty-journey-on-hugging-face-hub-via-protect-ai-9f3a1bc72c2e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9f3a1bc72c2e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9f3a1bc72c2e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI

## From Informative Rejection to Black Hat Briefing

[![Peng Zhou](https://miro.medium.com/v2/resize:fill:64:64/1*jxEEMOb5jrxEADVunLJYBw.jpeg)](https://medium.com/%40zpbrent?source=post_page---byline--9f3a1bc72c2e---------------------------------------)

[Peng Zhou](https://medium.com/%40zpbrent?source=post_page---byline--9f3a1bc72c2e---------------------------------------)

8 min read

·

May 11, 2024

--

Share

Press enter or click to view image in full size

![]()

I am writing this article to share my bug-bounty experiences for LLM/AI security, specifically for the LLM supply chain vulnerabilities I have disclosed across the third-party LLM libraries integrated into the [Hugging Face hub](https://huggingface.co/) (HF in short), which include the [huggingface/transformers](https://github.com/huggingface/transformers), [PaddlePaddle/PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP), [facebookresearch/mbrl-lib](https://github.com/facebookresearch/mbrl-lib), and [DLR-RM/stable-baselines3](https://github.com/DLR-RM/stable-baselines3). The root cause of these vulnerabilities is the abuse of the risky `pickle.loads` functions that can be exploited from the Hugging Face’s demo codes. I have reported my findings to respective maintainers, some of which are disclosed via Protect AI ([huntr.com](https://huntr.com/)), and have successfully rewarded $3250 bounties with 2 CVEs. I have also presented this class of bugs as a [briefing at Black Hat Asia 2024](https://www.blackhat.com/asia-24/briefings/schedule/#how-to-make-hugging-face-to-hug-worms-discovering-and-exploiting-unsafe-pickleloads-over-pre-trained-large-model-hubs-36261). Despite the final results seeming encouraging, I will tell you the way to success is narrow and difficult.

## The First Blood

Originally, my LLM bug bounty journey started from an AI Bug Bounty champion held by Protect AI ([huntr.com](https://huntr.com/)) in August-September 2023. The target of this champion is [huggingface/transformers](https://github.com/huggingface/transformers). To participate in this champion, I first searched lots of risky Python function calls across the source code of the target and found that…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9f3a1bc72c2e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9f3a1bc72c2e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9f3a1bc72c2e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9f3a1bc72c2e---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--9f3a1bc72c2e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Peng Zhou](https://miro.medium.com/v2/resize:fill:96:96/1*jxEEMOb5jrxEADVunLJYBw.jpeg)](https://medium.com/%40zpbrent?source=post_page---post_author_info--9f3a1bc72c2e---------------------------------------)

[![Peng Zhou](https://miro.medium.com/v2/resize:fill:128:128/1*jxEEMOb5jrxEADVunLJYBw.jpeg)](https://medium.com/%40zpbrent?source=post_page---post_author_info--9f3a1bc72c2e---------------------------------------)

[## Written by Peng Zhou](https://medium.com/%40zpbrent?source=post_page---post_author_info--9f3a1bc72c2e---------------------------------------)

[185 followers](https://medium.com/%40zpbrent/followers?source=post_page---post_author_info--9f3a1bc72c2e---------------------------------------)

·[81 following](https://medium.com/%40zpbrent/following?source=post_page---post_author_info--9f3a1bc72c2e---------------------------------------)

Half Writer Half Hunter

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----9f3a1bc72c2e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9f3a1bc72c2e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9f3a1bc72c2e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9f3a1bc72c2e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----9f3a1bc72c2e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9f3a1bc72c2e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9f3a1bc72c2e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9f3a1bc72c2e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9f3a1bc72c2e---------------------------------------)