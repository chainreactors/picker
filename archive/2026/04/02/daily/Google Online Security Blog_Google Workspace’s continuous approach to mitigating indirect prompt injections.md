---
title: Google Workspace’s continuous approach to mitigating indirect prompt injections
url: http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html
source: Google Online Security Blog
date: 2026-04-02
fetch_date: 2026-04-03T04:27:23.164750
---

# Google Workspace’s continuous approach to mitigating indirect prompt injections

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Google Workspace’s continuous approach to mitigating indirect prompt injections](https://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html "Google Workspace’s continuous approach to mitigating indirect prompt injections")

April 2, 2026

Posted by Adam Gavish, Google GenAI Security Team

Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This may even be possible without any input directly from the user.

IPI is not the kind of technical problem you “solve” and move on. Sophisticated LLMs with increasing use of agentic automation combined with a wide range of content create an ultra-dynamic and evolving playground for adversarial attacks. That’s why Google takes a sophisticated and comprehensive approach to these attacks. We’re continuously improving LLM resistance to IPI attacks and launching AI application capabilities with ever-improving defenses. Staying ahead of the latest indirect prompt injection attacks is critical to our mission of securing Workspace with Gemini.

In our previous blog “[Mitigating prompt injection attacks with a layered defense strategy](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html)”, we reviewed the layered architecture of our IPI defenses. In this blog, we’ll share more detail on the continuous approach we take to improve these defenses and to solve for new attacks.

## New attack discovery

By proactively discovering and cataloging new attack vectors through internal and external programs, we can identify vulnerabilities and deploy robust defenses ahead of adversarial activity.

#### Human Red-Teaming

Human [Red-Teaming](https://cloud.google.com/transform/how-google-does-it-building-an-effective-ai-red-team?utm_campaign=644972bd5b9473000116d347&utm_content=69b98c1e13c0120001542de7&utm_medium=smarpshare&utm_source=linkedin) uses adversarial simulations to uncover security and safety vulnerabilities. Specialized teams execute attacks based on realistic user profiles to exploit weaknesses, coordinating with product teams to resolve identified issues.

#### Automated Red-Teaming

Automated Red-Teaming is done via dynamic, machine-learning-driven frameworks to stress-test environments. By algorithmically generating and iterating on attack payloads, we can mimic the behavior of sophisticated threats at scale. This allows us to map complex attack paths and validate the effectiveness of our security controls across a much wider range of edge cases than manual testing could achieve on its own.

#### Google AI Vulnerability Rewards Program (VRP)

The [Google AI Vulnerability Rewards Program (VRP)](https://bughunters.google.com/about/rules/google-friends/ai-vulnerability-reward-program-rules) is a critical tool for enabling collaboration between Google and external security researchers who discover new attacks leveraging IPI. Through this VRP, we recognize and reward contributors for their research.  We also host regular, live hacking events where we provide invited researchers access to pre-release features, proactively uncovering novel vulnerabilities. These partnerships enable Google to quickly validate, reproduce, and resolve externally-discovered issues.

#### Publicly disclosed AI attacks

Google utilizes open-source intelligence feeds to stay on top of the latest publicly disclosed IPI attacks, across social media, press releases, blogs, and more. From there, new AI vulnerabilities are sourced, reproduced, and catalogued internally to ensure our products are not impacted.

#### Vulnerability catalog

All newly discovered vulnerabilities go through a comprehensive analysis process performed by the Google Trust, Security, & Safety teams. Each new vulnerability is reproduced, checked for duplications, mapped into attack technique / impact category, and assigned to relevant owners. The combination of new attack discovery sources and vulnerability catalog process helps Google stay on top of the latest attacks in an actionable manner.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQW2DFy08BHE1u92K8MiOGld7PIVOPqXkC_ACb2tJTcHhA4nG84w5spynWi-W9KcgJWW9mMfyDB1bvdwr-64mtYkkvKPPocpxVUI3pyB-QHXcBgJMXpfYRneCA14pqgDFs9e14xGJGIFOGVAUUrH2up-rju3CwMPjLsl7HtIhGSgrqPRlElqYt4G2af6Dc/s16000/Screenshot%202026-03-31%20at%2010.15.44%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQW2DFy08BHE1u92K8MiOGld7PIVOPqXkC_ACb2tJTcHhA4nG84w5spynWi-W9KcgJWW9mMfyDB1bvdwr-64mtYkkvKPPocpxVUI3pyB-QHXcBgJMXpfYRneCA14pqgDFs9e14xGJGIFOGVAUUrH2up-rju3CwMPjLsl7HtIhGSgrqPRlElqYt4G2af6Dc/s1306/Screenshot%202026-03-31%20at%2010.15.44%E2%80%AFAM.png)

## Synthetic data generation

After we discover, curate, and catalog new attacks, we use [Simula](https://openreview.net/pdf?id=VOoeogZbMb) to generate synthetic data expanding these new attacks. This process is essential because it allows the team to develop attack variants for completeness and coverage, and to prepare new training and validation data sets. This accelerated workflow has boosted synthetic data generation by 75%, supporting large-scale defense model evaluation and retraining, as well as updating the data set used for calculating and reporting on defense effectiveness.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghY30BDTqV9cG1siMIPHCah6tX1wVhw9WEWHx3cB9tlnm0UlAFHcRF74jzgdWRNamv2B29EpnI1sB4Ztijj9w0Y9-V82JVjSIKoZXaeKxbP_ptOzdRbTWe0W9sfHXlznjAnid0QjGleKvilFV46qk7qjbcNFFBu07HiEbBSZADgpnpZlnuHICHpUNe6Xzv/s16000/Screenshot%202026-03-31%20at%2010.16.24%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghY30BDTqV9cG1siMIPHCah6tX1wVhw9WEWHx3cB9tlnm0UlAFHcRF74jzgdWRNamv2B29EpnI1sB4Ztijj9w0Y9-V82JVjSIKoZXaeKxbP_ptOzdRbTWe0W9sfHXlznjAnid0QjGleKvilFV46qk7qjbcNFFBu07HiEbBSZADgpnpZlnuHICHpUNe6Xzv/s1310/Screenshot%202026-03-31%20at%2010.16.24%E2%80%AFAM.png)

## Ongoing defense refinement

Continually updating and enhancing our defense mechanisms allows us to address a broader range of attack techniques, effectively reducing the overall attack surface. Updating each defense type requires different tasks, from config updates, to prompt engineering and ML model retraining.

#### Deterministic Defenses

Deterministic [defenses](https://saif.google/focus-on-agents), including user confirmation, URL sanitization, and tool chaining policies, are designed for rapid response against new or emerging prompt injection attacks by relying on simple configuration updates. These defenses are governed by a centralized Policy Engine, with configurations for policies like baseline tool calls, URL sanitization, and tool chaining. For immediate threats, this configuration-based system facilitates a streamlined process for "point fixes," such as regex takedowns, providing an agile defense layer that acts faster than traditional ML/LLM model refresh cycles.

#### ML-Based Defenses

After generating synthetic data that expands new attacks into variants, the next step is to retrain our ML-based defenses to mitigate these new attacks. We partition the synthetic data described above into separate training and validation sets to ensure performance is evaluated against held-out examples. This approach ensures repeatability, data consistency for fixed training/testing, and establishes a scalable architecture to support future extensions towards fully automated model refresh.

#### LLM-Based Defenses...