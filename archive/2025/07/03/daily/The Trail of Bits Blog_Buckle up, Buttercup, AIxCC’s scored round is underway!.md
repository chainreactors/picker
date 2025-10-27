---
title: Buckle up, Buttercup, AIxCC’s scored round is underway!
url: https://blog.trailofbits.com/2025/07/02/buckle-up-buttercup-aixccs-scored-round-is-underway/
source: The Trail of Bits Blog
date: 2025-07-03
fetch_date: 2025-10-06T23:52:04.569063
---

# Buckle up, Buttercup, AIxCC’s scored round is underway!

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Buckle up, Buttercup, AIxCC’s scored round is underway!

Michael Brown

July 02, 2025

[aixcc](/categories/aixcc/), [research-practice](/categories/research-practice/), [darpa](/categories/darpa/)

Page content

* [**What’s happening in the scored round?**](#whats-happening-in-the-scored-round)
* [**What’s next for our team?**](#what)

The one and only scored round of DARPA’s AI Cyber Challenge (AIxCC) Finals Competition has officially started! Our CRS (Cyber Reasoning System), Buttercup, is now competing against six other teams to see which autonomous AI-driven system can find and patch the most software vulnerabilities. It’s been a long road to this point, and we’re excited to see the results of our hard work over the last two years building Buttercup.

After the scored round closes, DARPA and ARPA-H will announce the winners on the main DEFCON 33 stage on August 8. The top scoring CRS will receive a $4 million top prize, with the next two runners up receiving $3 million and $1.5 million in prize money. Our team will be there to watch the final reveal live and will also be involved in the larger AIxCC experience in various ways. If you’re planning to come to DEFCON this August, please come see us at our booth in the AIxCC Experience and attend our talk on the AIxCC stage (date/time TBD) about the ups and downs of building Buttercup and competing in AIxCC.

## **What’s happening in the scored round?**

Each competing CRS will be tasked with finding and patching multiple vulnerabilities in dozens of different real-world, open-source programs. These programs are chosen from the most heavily used C and Java open-source programs, and the vulnerabilities they contain are often actual historic vulnerabilities that have been strategically re-injected by the competition organizers. SQLite, Nginx, Apache Tika, Jenkins, and even the Linux Kernel are among programs that have been used in prior rounds.

Each CRS will tasked with waves of distinct challenges based on these open-source programs. Each challenge comes equipped with [OSS-Fuzz](https://github.com/google/oss-fuzz)-compatible fuzzing harnesses and, in many cases, a set of functional tests. A CRS can score points by:

1. Proving that a vulnerability exists in the program by finding an input that crashes the program or triggers a sanitizer at runtime
2. Fixing a vulnerability in the program with a patch that addresses the root cause of the vulnerability and does not break functional tests
3. Classifying a static analysis alert highlighting a possible vulnerability as a true- or false-positive

To accomplish this, each CRS has been given a sizable compute and third-party AI budget. The scale of AIxCC’s scored round is massive, and for good reason. The CRS that wins this competition will prove that it can immediately scale to the challenge of securing the vast open-source software ecosystem.

## **What’s next for our team?**

While Buttercup is competing and we await the announcement of the winning teams, we’re still hard at work making Buttercup even better! In the coming month, we will be preparing Buttercup to be released as open-source software, which we expect to make available in August. We’re also working on building a version of Buttercup that can be run on commodity hardware so everyone can try it out!

Also, once the competition is over, we can finally share technical details on how Buttercup works. Stay tuned for technical deep dives on how Buttercup uses AI to accelerate traditional fuzz testing and create high-quality patches for vulnerabilities!

*For more background, see our previous posts on the AIxCC:*

* [DARPA’s AI Cyber Challenge: We’re In!](https://blog.trailofbits.com/2023/12/14/darpas-ai-cyber-challenge-were-in/)
* [Our thoughts on AIxCC’s competition format](https://blog.trailofbits.com/2024/01/18/our-thoughts-on-aixccs-competition-format/)
* [DARPA awards $1 million to Trail of Bits for AI Cyber Challenge](https://blog.trailofbits.com/2024/03/11/darpa-awards-1-million-to-trail-of-bits-for-ai-cyber-challenge/)
* [Trail of Bits’ Buttercup heads to DARPA’s AIxCC](https://blog.trailofbits.com/2024/08/09/trail-of-bits-buttercup-heads-to-darpas-aixcc/)
* [Trail of Bits Advances to AIxCC Finals](https://blog.trailofbits.com/2024/08/12/trail-of-bits-advances-to-aixcc-finals/)
* [Kicking off AIxCC’s Finals with Buttercup](https://blog.trailofbits.com/2025/04/21/kicking-off-aixccs-finals-with-buttercup/)

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

* [**What’s happening in the scored round?**](#whats-happening-in-the-scored-round)
* [**What’s next for our team?**](#what)

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.