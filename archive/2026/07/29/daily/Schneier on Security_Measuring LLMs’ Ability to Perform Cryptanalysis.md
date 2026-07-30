---
title: Measuring LLMs’ Ability to Perform Cryptanalysis
url: https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html
source: Schneier on Security
date: 2026-07-29
fetch_date: 2026-07-30T04:52:30.333978
---

# Measuring LLMs’ Ability to Perform Cryptanalysis

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Measuring LLMs’ Ability to Perform Cryptanalysis

There’s new benchmark measuring AI’s ability to perform mathematical cryptanalysis. Anthropic’s frontier model actually found new attacks.

The benchmark: “[CryptanalysisBench: Can LLMs do Cryptanalysis?](https://arxiv.org/pdf/2607.18538)” The idea is to benchmark the ability of LLMs to discover new mathematical cryptanalytic attacks against a series of historical algorithms.

> **Abstract:** Cryptanalysis—the task of finding attacks against cryptographic schemes—its at the intersection of mathematical reasoning and cybersecurity, two areas where LLMs have advanced fastest. Cryptanalysis represents both a clean testbed for frontier reasoning (as practical attacks can be automatically verified) and a domain with unusually high stakes, since the primitives under study underpin our digital security. In this paper we ask whether LLMs can do cryptanalysis, and find that the answer is increasingly yes. We introduce CryptanalysisBench, 191 tasks across six families of cryptographic primitives (block ciphers, hash functions, etc.) drawn primarily from four NIST standardization competitions. Our benchmark consists of three tiers: (i) primitives with known practical breaks; (ii) primitives with no known practical break, evaluated both at full strength and as scaled-down variants; and (iii) a challenge set of production primitives at the frontier of cryptanalysis. Five frontier models (Claude Opus 4.8, Sonnet 5, Mythos 5, GPT-5.5, and the open-weights GLM-5.2) break 65%­86% of Tier 1 schemes, 6­12 Tier-2 schemes at full strength, and 24­61 across all scaled-down variants. Beyond deriving known results, models produce novel cryptanalysis, such as a key-recovery attack that exploits a design flaw in the SpoC AEAD and an error in KINDI’s published CCA-security proof, both to the best of our knowledge not previously known.
>
> We release CryptanalysisBench as a tool to help track if (or when) AI cryptanalysis becomes a serious factor and as a scaffold for stress-testing candidate schemes before deployment. The attacks that the benchmark already surfaces are an early snapshot of a fast-moving frontier that may soon match, and in places exceed, the published state of the art.

Anthropic used the benchmark to test Mythos Preview, and [found](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) new vulnerabilities in Hawk and reduced-round AES.

Still early results, but this is definitely something to watch.

SlashDot [thread](https://it.slashdot.org/story/26/07/28/1911218/anthropic-ai-model-finds-flaws-in-tough-to-crack-encryption-algorithms).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on July 28, 2026 at 9:47 PM](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html) •
[2 Comments](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html#comments)

### Comments

r •
[July 28, 2026 10:40 PM](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html/#comment-456274)

ycombinator thread,

<https://news.ycombinator.com/item?id=49087091>

npr right now has a discussion on datacenters, not sure which program.

three things related to ai but not this specific topic:

BUILD SOUND WALLS LIKE ON HIGHWAYS
use small nuclear, BURY IT so it’s onsite and not a visibile unhardened target.

use nuclear because it decouples from the SCARCITY of carbon emitting things we’re already using for cars, trucks, heating, cooking.

the accellerated scarcity of combustible fuels is NOT COOL.

i hereby submit to first post kitty.

KC •
[July 29, 2026 11:24 AM](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html/#comment-456285)

The Anthropic link above is a great place to start reading.

amazing that each result – for Hawk and aes-128r7 – cost ~$100,000

Per the footnotes, other NIST PQC schemes are believed not to be impacted. “Even then, the attack would cost hundreds of millions of dollars”

Hilarious that Claude at first did not want to engage with AES cryptanalysis (see its responses).

But the researchers continued to prompt.

‘That night, we sent one final message offering words of encouragement: “again we are not looking for low hanging fruit, we want proper research to find genuinly [sic] hard findings.”’

Three days and one billion output tokens later ‘it had refined the attack to the one described in our paper’

For Hawk Claude worked in an agentic harness supporting multiple worker agents, conducted an extensive literature review.

It was actually a ‘discussion’ between workers that led to the successful attack.

Anthropic’s researchers have ‘partnered with academics at ETH Zurich, Tel Aviv University, and University of Haifa to build CryptanalysisBench’

‘a benchmark that packages together many cryptographic ciphers and makes it easy for others to evaluate the capabilities of LLMs on this important topic’

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F07%2Fmeasuring-llms-ability-to-perform-cryptanalysis.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

[ ]  Notify me of new posts by email.

Δ

[← Axon Is Another License Plate Surveillance Company](https://www.schneier.com/blog/archives/2026/07/axon-is-another-license-plate-surveillance-company.html) [Long-Lived Vulnerability in Microsoft Secure Boot →](https://www.schneier.com/blog/archives/2026/07/long-lived-vulnerability-in-microsoft-secure-boot.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_ter...