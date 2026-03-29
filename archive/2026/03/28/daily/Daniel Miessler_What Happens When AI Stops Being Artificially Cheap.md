---
title: What Happens When AI Stops Being Artificially Cheap
url: https://danielmiessler.com/blog/ai-stops-being-artificially-cheap?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-03-28
fetch_date: 2026-03-29T04:42:46.463881
---

# What Happens When AI Stops Being Artificially Cheap

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# What Happens When AI Stops Being Artificially Cheap

The subsidy era is ending. Here's what comes next.

March 28, 2026

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#future](/archives/?tag=future) [#business](/archives/?tag=business)

![What Happens When AI Stops Being Artificially Cheap](/images/ai-stops-being-artificially-cheap.webp)

I've been thinking about what happens when AI inference costs stop being subsidized. Every major lab is losing money on inference right now, and that's going to change. I don't know exactly how it plays out, but here's where my head is at.

1. **Good enough is good enough.** Most tasks people use AI for don't need frontier models. Writing summaries, extracting data, answering questions, drafting emails — none of that requires the smartest model available. I think this covers 95% of real-world usage. The top 5% — hard research, complex reasoning, genuinely creative work — still needs frontier. But that's not what most people are doing.
2. **Open-source absorbs the work.** A lot of that 95% shifts to open-source models that are small and virtually free to run. Open-weight models lag frontier by about three months now. Three months. That gap keeps shrinking.
3. **There's still vast amounts of [slack in the rope](/blog/revisiting-the-ai-bubble).** I've been [saying this since 2023](/blog/my-ai-predictions-retrospective), and it keeps being true. I don't think we've come close to finding out how efficient inference can get. We're probably at 1-5% of the efficiency we'll have over the next decade, and that might be orders of magnitude too conservative.
4. **Frontier gets more expensive, everything else gets cheaper.** I expect a price jump at the top tier because the labs can't keep giving that away. But lower-tier cloud models — Haiku, the nano models, Flash — will compete hard with open-source on price. They have to, because losing that traffic means losing the customer.
5. **What humans want doesn't change that fast.** The workflows and tasks most people need are largely static. The top 5% of requirements might stay expensive. But most human tasks land in the bottom 95%, and I expect that to be very affordable.

I'm still thinking through a lot of this, but here's where I currently land: the subsidy era ends, and what replaces it is a split — expensive frontier for the few who need it, cheap everything else for everyone who doesn't. Most people won't even notice.

#### Sources

1. OpenAI inference costs revealed through leaked Microsoft revenue-share documents. [TechCrunch](https://techcrunch.com/2025/11/14/leaked-documents-shed-light-into-how-much-openai-pays-microsoft/)
2. OpenAI revenue of $13.1 billion in 2025, confirmed by CFO Sarah Friar. [CNBC](https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html)
3. OpenAI projects $115 billion cumulative cash burn through 2029. [Fortune](https://fortune.com/2025/11/12/openai-cash-burn-rate-annual-losses-2028-profitable-2030-financial-documents/)
4. Anthropic nears $20 billion revenue run rate by March 2026. [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-03/anthropic-nears-20-billion-revenue-run-rate-amid-pentagon-feud), corroborated by [CNBC](https://www.cnbc.com/2026/03/04/anthropic-ai-pentagon-defense-business-risk.html)
5. Nick Turley (VP of Product, OpenAI) described ChatGPT's subscription pricing as something they "stumbled into." [BG2 Pod](https://pod.wave.co/podcast/bg2pod-with-brad-gerstner-and-bill-gurley/chatgpt-the-super-assistant-era-bg2-guest-interview), covered by [Business Insider](https://finance.yahoo.com/news/openai-rethinking-chatgpt-pricing-unlimited-143826057.html)
6. AI venture capital totaled $258.7 billion globally in 2025. [OECD](https://www.oecd.org/en/publications/venture-capital-investments-in-artificial-intelligence-through-2025_a13752f5-en/full-report.html)
7. Stanford HAI 2025 AI Index documented a 280-fold decline in GPT-3.5-level inference costs. [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)
8. Open-weight models lag frontier closed models by 3.5 months on average. [Epoch AI](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models)
9. Inference price decline of 50x per year, accelerating to 200x post-January 2024. [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends)
10. ~10x annual cost decline for equivalent LLM performance ("LLMflation"). [a16z](https://a16z.com/llmflation-llm-inference-cost/)
11. Google reported 33x energy reduction per AI text prompt in 12 months. [Google](https://blog.google/company-news/outreach-and-initiatives/sustainability/google-ai-energy-efficiency/), [preprint](https://arxiv.org/abs/2508.15734)
12. Speculative decoding: 2-3x inference speedup (Leviathan et al., ICML 2023). [arXiv](https://arxiv.org/abs/2211.17192)
13. Continuous batching and PagedAttention (vLLM, SOSP 2023). [arXiv](https://arxiv.org/abs/2309.06180)
14. Quantization quality retention: AWQ ([MLSys 2024](https://arxiv.org/abs/2306.00978)) and GPTQ ([ICLR 2023](https://arxiv.org/abs/2210.17323))
15. Inference cost-performance improvement of 5-10x per year. ["The Price of Progress"](https://arxiv.org/abs/2511.23455)
16. Enterprise open-source LLM adoption declined from 19% to 13%. [Menlo Ventures](https://menlovc.com/perspective/2025-mid-year-llm-market-update/)
17. Gartner predicts inference on 1T-parameter LLMs will cost 90% less by 2030. [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-03-25-gartner-predicts-that-by-2030-performing-inference-on-an-llm-with-1-trillion-parameters-will-cost-genai-providers-over-90-percent-less-than-in-2025)

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-artificially-cheap&title=What%20Happens%20When%20AI%20Stops%20Being%20Artificially%20Cheap)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-stops-being-arti...