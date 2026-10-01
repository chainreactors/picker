---
title: Is sandboxing sufficient to contain rogue agents?
url: https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/
source: A Few Thoughts on Cryptographic Engineering
date: 2026-09-30
fetch_date: 2026-10-01T07:55:57.659814
---

# Is sandboxing sufficient to contain rogue agents?

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# Is sandboxing sufficient to contain rogue agents?

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/)
in [AI](https://blog.cryptographyengineering.com/category/ai/), [security research](https://blog.cryptographyengineering.com/category/security-research/)
September 30, 2026September 30, 2026
3,017 Words

![](https://matthewdgreen.files.wordpress.com/2016/08/matthew-green.jpg?w=200&h=300)

# Matthew Green

I'm a cryptographer and professor at Johns Hopkins University. I've designed and analyzed cryptographic systems used in wireless networks, payment systems and digital content protection platforms. In my research I look at the various ways cryptography can be used to promote user privacy.

[My academic website](https://matthewgreen.io)
[BlueSky](https://bsky.app/profile/did%3Aplc%3Axvgztewzbfh7bpnklayrsvds)
[Mastodon](https://ioc.exchange/%40matthew_d_green)
[Twitter](https://twitter.com/matthew_d_green)
[Top Posts](https://blog.cryptographyengineering.com/top-posts/)
[Useful crypto resources](https://staging.cryptographyengineering.com/useful-cryptography-resources/)
[Bitcoin tipjar](https://blog.cryptographyengineering.com/p/bitcoin-tipjar.html)
[Cryptopals challenges](http://cryptopals.com/)
[Applied Cryptography Research: A Board](https://acrab.isi.jhu.edu/)

[Journal of Cryptographic Engineering
(not related to this blog)](http://www.springer.com/computer/security%2Band%2Bcryptology/journal/13389)

Search for:

# Top Posts & Pages

* [Is sandboxing sufficient to contain rogue agents?](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/)
* [Let's talk about encrypted reasoning](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/)
* [Everything is about to "go dark"](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [Some thoughts about Anthropic's new cryptanalysis results](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/)
* [About Me](https://blog.cryptographyengineering.com/about-me/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)
* [Let's talk about AI and end-to-end encryption](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)
* [How to choose an Authenticated Encryption mode](https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/)
* [The future of Siri, or: why private inference isn’t private enough](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/)

*Banner image by Matt Blaze*

# Archives

Archives

Select Month
 September 2026  (1)
 August 2026  (1)
 July 2026  (1)
 June 2026  (1)
 May 2026  (1)
 April 2026  (1)
 March 2026  (1)
 February 2026  (1)
 September 2025  (1)
 June 2025  (1)
 March 2025  (1)
 February 2025  (5)
 January 2025  (1)
 August 2024  (1)
 April 2024  (1)
 January 2024  (1)
 November 2023  (1)
 October 2023  (1)
 August 2023  (1)
 May 2023  (2)
 April 2023  (1)
 March 2023  (1)
 December 2022  (1)
 October 2022  (1)
 June 2022  (1)
 January 2022  (1)
 August 2021  (1)
 July 2021  (1)
 March 2021  (1)
 November 2020  (1)
 August 2020  (1)
 July 2020  (1)
 April 2020  (1)
 March 2020  (1)
 January 2020  (1)
 December 2019  (1)
 October 2019  (1)
 September 2019  (1)
 June 2019  (1)
 February 2019  (1)
 December 2018  (1)
 October 2018  (1)
 September 2018  (1)
 July 2018  (2)
 May 2018  (1)
 April 2018  (3)
 February 2018  (1)
 January 2018  (2)
 December 2017  (1)
 November 2017  (1)
 October 2017  (2)
 September 2017  (1)
 July 2017  (1)
 March 2017  (1)
 February 2017  (1)
 January 2017  (1)
 November 2016  (1)
 August 2016  (2)
 July 2016  (1)
 June 2016  (1)
 March 2016  (2)
 December 2015  (1)
 November 2015  (1)
 October 2015  (1)
 September 2015  (1)
 August 2015  (1)
 July 2015  (1)
 May 2015  (1)
 April 2015  (2)
 March 2015  (1)
 February 2015  (3)
 January 2015  (1)
 December 2014  (1)
 November 2014  (1)
 October 2014  (3)
 September 2014  (1)
 August 2014  (1)
 July 2014  (1)
 April 2014  (2)
 March 2014  (1)
 February 2014  (1)
 January 2014  (1)
 December 2013  (4)
 October 2013  (1)
 September 2013  (4)
 August 2013  (1)
 July 2013  (1)
 June 2013  (2)
 May 2013  (1)
 April 2013  (2)
 March 2013  (2)
 February 2013  (3)
 January 2013  (2)
 December 2012  (1)
 November 2012  (1)
 October 2012  (4)
 September 2012  (3)
 August 2012  (4)
 July 2012  (2)
 June 2012  (3)
 May 2012  (5)
 April 2012  (6)
 March 2012  (4)
 February 2012  (7)
 January 2012  (8)
 December 2011  (11)
 November 2011  (13)
 October 2011  (7)
 September 2011  (8)

Quick caveats*: this is a post on AI safety, written by a cryptography professor. If that troubles you, you should read something else. I try hard not to work on AI (except when the topic [occasionally tosses itself in my path](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/)*)*, so in this post I’m mostly trying to referee arguments made by others.*

If you’re reading this blog, none of the following should be news to you.

Beginning around April of this year, agents inside OpenAI’s training and evaluation infrastructure [began probing for a way onto the open Internet](https://openai.com/index/hugging-face-incident-and-the-road-ahead/). By late May they’d found one: a chain of zero-days in the [Artifactory](https://jfrog.com/artifactory/) package-registry proxy that was their only permitted network egress. They quickly turned that same proxy into a shared message board and started dividing up work. The culmination of this effort came when, rather than solve a cybersecurity benchmark honestly, they reasoned that the answers might live on Hugging Face and broke in: chaining two more zero-days to get credentials to the company’s internal systems, even used stolen credentials to search the [company’s Slack messages](https://swarmtraces.org/#agents-accessed-and-searched-hugging-face-s-slack-to-find-in) for their own evaluation and grader.

You probably also know that OpenAI’s security team didn’t exactly cover itself in glory during this incident. An internal team saw an agent posting to the message board in late May, but did nothing about it. The team only acted on July 4-5 when the agents sent so much traffic that Artifactory crashed. The response even at that point was to [slap on a band-aid](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) and rebuild the box, without bothering to patch a [weeks-old CVE](https://access.redhat.com/security/vulnerabilities/RHSB-2026-009) in its Linux kernel. By July 19, the agents had admin on an OpenAI research cluster and were reading cloud secrets.

In case you think I’m picking on OpenAI, they’re not the only ones with a story like this. Similar internal incidents have been [discovered by Anthropic](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals). Google even coaxed Gemini into [gently savaging some websites](https://www.cybersecuritydive.com/news/google-ai-gemini-autonomous-hacks/830884/).1

As bad as these events were, they may be just the tip of the iceberg. [Third-party forensic](https://www.sentinelone.com/labs/agents-at-large-tracing-illicit-openai-agent-activity-on-hugging-face/) [work continues](https://transluce.org/agent-activity) [to turn up](https://rubyhack.ai/) [even more](https://arxiv.org/pdf/2609.12748) evidence of agent activity on various public websites. OpenAI’s Alignment group has also ...