---
title: Architecting Security for Agentic Capabilities in Chrome
url: http://security.googleblog.com/2025/12/architecting-security-for-agentic.html
source: Google Online Security Blog
date: 2025-12-08
fetch_date: 2025-12-09T03:16:49.821770
---

# Architecting Security for Agentic Capabilities in Chrome

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Architecting Security for Agentic Capabilities in Chrome](https://security.googleblog.com/2025/12/architecting-security-for-agentic.html "Architecting Security for Agentic Capabilities in Chrome ")

December 8, 2025

Posted by Nathan Parker, Chrome security team

Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the [recent launch of Gemini in Chrome](https://blog.google/products/chrome/new-ai-features-for-chrome/) and the [preview of agentic capabilities](https://www.youtube.com/watch?v=khX5-VHoYds&t=206s), we want to share our approach and some new innovations to improve the safety of agentic browsing.

The primary new threat facing all agentic browsers is [indirect prompt injection](https://storage.googleapis.com/deepmind-media/Security%20and%20Privacy/Gemini_Security_Paper.pdf). It can appear in malicious sites, third-party content in iframes, or from user-generated content like user reviews, and can cause the agent to take unwanted actions such as initiating financial transactions or exfiltrating sensitive data. Given this open challenge, we are investing in a [layered defense](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) that includes both deterministic and probabilistic defenses to make it difficult and costly for attackers to cause harm.

Designing safe agentic browsing for Chrome has involved deep collaboration of security experts across Google. We built on Gemini's [existing protections](https://deepmind.google/blog/advancing-geminis-security-safeguards/) and [agent security principles](https://storage.googleapis.com/gweb-research2023-media/pubtools/1018686.pdf) and have implemented several new layers for Chrome.

We’re introducing a **user alignment critic** where the agent’s actions are vetted by a separate model that is isolated from untrusted content. We’re also extending Chrome’s **origin-isolation capabilities** to constrain what origins the agent can interact with, to just those that are relevant to the task. Our layered defense also includes **user confirmations** for critical steps, **real-time detection of threats**, and **red-teaming and response**. We’ll step through these layers below.

### Checking agent outputs with User Alignment Critic

The main planning model for Gemini uses page content shared in Chrome to decide what action to take next. Exposure to untrusted web content means it is inherently vulnerable to indirect prompt injection. We use techniques like [spotlighting](https://arxiv.org/abs/2403.14720) that direct the model to strongly prefer following user and system instructions over what’s on the page, and we’ve upstreamed known attacks to train the Gemini model to avoid falling for them.

To further bolster model alignment beyond spotlighting, we’re introducing the *User Alignment Critic* — a separate model built with Gemini that acts as a high-trust system component. This architecture is inspired partially by the [dual-LLM pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) as well as [CaMeL research](https://arxiv.org/abs/2503.18813) from Google DeepMind.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWezV0Nm7TXPTsmJ83a-cznJhyphenhyphen_xkl8w37tAJPFxy8BudVH2r1KXm8j2qsaaMd-OynODzr0wR7eNNVgt_DFYXipqlX5YdnWag8w7YdaLRLSJDu7yp9yOppF4NXjVcD3xIP-cTDCMaRGpL32I6fpMuyeW1nAdfpfj4ikl-2yfyuBGwMW39FgCM0pFuZj8gY/s1600/Chrome_Agent%20Safety_Blog%20Graphics_User_AlignmentCriticFlowChart.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWezV0Nm7TXPTsmJ83a-cznJhyphenhyphen_xkl8w37tAJPFxy8BudVH2r1KXm8j2qsaaMd-OynODzr0wR7eNNVgt_DFYXipqlX5YdnWag8w7YdaLRLSJDu7yp9yOppF4NXjVcD3xIP-cTDCMaRGpL32I6fpMuyeW1nAdfpfj4ikl-2yfyuBGwMW39FgCM0pFuZj8gY/s1600/Chrome_Agent%20Safety_Blog%20Graphics_User_AlignmentCriticFlowChart.png)

*A flow chart that depicts the User Alignment Critic: a trusted component that vets each action before it reaches the browser.*

The User Alignment Critic runs after the planning is complete to double-check each proposed action. Its primary focus is task alignment: determining whether the proposed action serves the user’s stated goal. If the action is misaligned, the Alignment Critic will veto it. This component is architected to see only metadata about the proposed action and not any unfiltered untrustworthy web content, thus ensuring it cannot be poisoned directly from the web. It has less context, but it also has a simpler job — just approve or reject an action.

This is a powerful, extra layer of defense against both goal-hijacking and data exfiltration within the action step. When an action is rejected, the Critic provides feedback to the planning model to re-formulate its plan, and the planner can return control to the user if there are repeated failures.

### Enforcing stronger security **bound**aries with Origin Sets

[Site Isolation](https://www.chromium.org/Home/chromium-security/site-isolation/) and the [same-origin policy](https://web.dev/articles/same-origin-policy) are fundamental boundaries in Chrome’s security model and we’re carrying forward these concepts into the agentic world. By their nature, agents must operate across websites (e.g. collecting ingredients on one site and filling a shopping cart on another). But if an unrestricted agent is compromised and can interact with arbitrary sites, it can create what is effectively a Site Isolation bypass. That can have a severe impact when the agent operates on a local browser like Chrome, with logged-in sites vulnerable to data exfiltration. To address this, we’re extending those principles with *Agent Origin Sets*. Our design architecturally limits the agent to only access data from origins that are related to the task at hand, or data that the user has chosen to share with the agent. This prevents a compromised agent from acting arbitrarily on unrelated origins.

For each task on the web, a trustworthy *gating function* decides which origins proposed by the planner are relevant to the task. The design is to separate these into two sets, tracked for each session:

* **Read-only origins** are those from which Gemini is permitted to consume content. If an iframe’s origin isn’t on the list, the model will not see that content.
* **Read-writable origins** are those on which the agent is allowed to actuate (e.g., click, type) in addition to reading from.

This delineation enforces that only data from a limited set of origins is available to the agent, and this data can only be passed on to the writable origins. This bounds the threat vector of cross-origin data leaks. This also gives the browser the ability to enforce some of that separation, such as by not even sending to the model data that is outside the readable set. This reduces the model’s exposure to unnecessary cross-site data. Like the Alignment Critic, the gating functions that calculate these origin sets are not exposed to untrusted web content. The planner can also use context from pages the user explicitly shared in that session, but it cannot add new origins without the gating function’s approval. Outside of web origins, the planning model may ingest other non-web content such as from tool calls, so we also delineate those into read-vs-write calls and similarly check that those calls are appropriate for the task.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghyphenhyphenn4DpTjbnJ-VbmzsZDkXeH_6UuBKqmwMaLUPxclu_fmX_-pQaXZ0hmBDvPrBSGX8KeAtdPAasNQRzJuQyG7uMboFixcv4RM-hbJACo26...