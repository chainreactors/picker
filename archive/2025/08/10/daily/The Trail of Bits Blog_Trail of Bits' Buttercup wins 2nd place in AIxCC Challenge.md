---
title: Trail of Bits' Buttercup wins 2nd place in AIxCC Challenge
url: https://blog.trailofbits.com/2025/08/09/trail-of-bits-buttercup-wins-2nd-place-in-aixcc-challenge/
source: The Trail of Bits Blog
date: 2025-08-10
fetch_date: 2025-10-07T00:17:38.918725
---

# Trail of Bits' Buttercup wins 2nd place in AIxCC Challenge

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Trail of Bits' Buttercup wins 2nd place in AIxCC Challenge

Trail of Bits

August 09, 2025

[aixcc](/categories/aixcc/), [research-practice](/categories/research-practice/), [darpa](/categories/darpa/), [machine-learning](/categories/machine-learning/)

Page content

* [Buttercup found vulnerabilities across 20 CWEs with 90% accuracy](#buttercup-found-vulnerabilities-across-20-cwes-with-90-accuracy)
* [LLMs are money well-spent](#llms-are-money-well-spent)
* [Other Notable Achievements](#other-notable-achievements)
* [What Buttercup can do for you](#what-buttercup-can-do-for-you)

On August 8, 2025, it was announced that our team took home the runner-up prize of $3M in DARPA’s Artificial Intelligence Cyber Challenge (AIxCC) at DEF CON 33 in Las Vegas. Team Atlanta, a hybrid team of engineers from Georgia Tech, KAIST, POSTECH, and Samsung Research, won the top prize of $4M, and Theori, with a prize of $1.5M, was the third-place finisher.

![Trail of Bits wins second place at AIxCC](/img/aixcc/buttercup-places-second.jpg)

DARPA announces Trail of Bits won second place and $3M at the AIxCC finals

AIxCC was a two-year competition open to the public to see who could build the best fully automated system for securing open-source software. The scoring algorithm rewarded teams for finding vulnerabilities, proving that vulnerabilities existed, and correctly applying patches to open-source software. Speed and accuracy were also rewarded. Human interaction was strictly prohibited.

In last year’s semi-finals, the field was whittled down to 7 finalists from 42 competitors. Each of the finalists received $2M to spend the next year refining their cyber reasoning systems (CRSs) for this year’s finals competition. During the final round, there were 48 challenges across 23 open-source repositories. We found **28 vulnerabilities** and successfully applied **19 patches**.

Yet the real victory goes beyond these numbers. These systems, which collectively took thousands of hours of research and engineering to create, are [open-source and available to everyone](https://archive.aicyberchallenge.com/). Here is what we know so far about how we performed.

![Buttercup’s standout achievements at AIxCC](/img/aixcc/buttercup-achievements.jpg)

Buttercup earned special recognition as 'LOC Ness Monster' for submitting a 300+ line patch and 'Cornucopia' for successfully exploiting 20 unique CWEs. Notably, Trail of Bits achieved these results using exclusively less expensive, non-reasoning LLMs.

## Buttercup found vulnerabilities across 20 CWEs with 90% accuracy

AIxCC challenged competitors to find software vulnerabilities across [Mitre’s Top 25 Most Dangerous CWEs](https://cwe.mitre.org/top25/archive/2024/2024_cwe_top25.html), and [Buttercup](https://trailofbits.com/buttercup) submitted proofs of vulnerabilities (PoVs) across 20 of them. Securing real-world software is more than just uncovering memory leaks and buffer overflows. This breadth demonstrates our system’s robust understanding of diverse vulnerability classes, from memory safety issues to injection flaws.

Other teams also had good CWE coverage, but what separated us from the competition was our ability to bundle discovered bugs with proofs of vulnerabilities (PoVs) and correct patches with a high degree of accuracy. Teams were penalized if their patches were incorrect or inaccurate, and although data from the competition hasn’t been released, we believe that this was a determining factor in our securing a second-place win.

## LLMs are money well-spent

Each AIxCC team was given an LLM and a compute budget. The top two teams, Team Atlanta and us, spent the most on LLM queries. Third-place Theori spent roughly half the amount as the top two winners on LLM queries.

Buttercup achieved remarkable efficiency relative to our performance. This efficiency makes our approach particularly valuable for the open-source community, where compute budgets are limited and cost-effectiveness is crucial for widespread adoption. Here’s how the spending compared among the prize winners.

| Team | LLM spend | Compute spend | Total spend | Cost per point |
| --- | --- | --- | --- | --- |
| Team Atlanta | $29.4k | $73.9k | $103.3k | $263 |
| **Trail of Bits** | **$21.1k** | **$18.5k** | **$39.6k** | **$181** |
| Theori | $11.5k | $20.3k | $31.8k | $151 |
| fuzzing\_brain | $12.2k | $63.2k | $75.4k | $490 |
| Shellphish | $2.9k | $54.9k | $57.8k | $425 |
| 42-b3yond-6ug | $1.1k | $38.7k | $39.8k | $379 |
| LACROSSE | $631 | $7.1k | $7.2k | $751 |

*Cost per point shows the dollar amount spent on compute and LLM resources to earn each competition point. Trail of Bits achieved remarkable efficiency at just $181 per point, demonstrating that world-class automated vulnerability discovery doesn’t require massive infrastructure investments.*

## Other Notable Achievements

Our patching system represents a breakthrough in automated code repair. One of our proudest moments was learning that Buttercup submitted the **largest software patch, over 300 lines of code,** in the entire competition. This shows an understanding of complex codebases and the ability to implement substantial fixes safely and accurately.

Digging more into the results after the awards ceremony, we learned that Buttercup also:

1. Scored less than 5 minutes into a task
2. Made over 100,000 LLM requests
3. Had greater than 90% accuracy
4. Found a PoV that triggered a vulnerability that was not inserted into the Challenge
5. Scored with a patch that was a one-line change
6. Successfully bundled SARIF, PoV, and Patches

## What Buttercup can do for you

As a cybersecurity services company with a reputation for government and open-source community engagement, Trail of Bits designed Buttercup with accessibility in mind. Our system is production-ready for automated vulnerability discovery and proves that world-class automated vulnerability discovery and patching don’t require a complex infrastructure. [You can download Buttercup today and run it on your laptop](https://github.com/trailofbits/buttercup).

So how does Buttercup work? It augments both libFuzzer and Jazzer with LLM-generated test cases. It integrates static analysis tools like tree-sitter and code query systems. It uses a multi-agent architecture for intelligent patching with separation of concerns. And it understands call graphs, dependencies, and vulnerability contexts.

Buttercup’s story has only just begun. We’re already exploring ways to optimize the system further, and DARPA and ARPA-H have generously offered each AIxCC team an additional $200,000 to integrate their CRSs into critical software. If you have a code repository that you want to secure with Buttercup, [we’d like to hear from you](https://www.trailofbits.com/contact/).

DARPA hasn’t yet released all of the AIxCC competition data and telemetry to the competitors, so stay tuned for more blog posts analyzing the results over the coming weeks.

Finally, congratulations to all the teams for challenging us to push the envelope for what can be achieved with AI systems in open-source security. The future of the industry begins today.

*For more background, see our previous posts on the AIxCC:*

* [Buttercup is now open-source!](https://blog.trailofbits.com/2025/08/08/buttercup-is-now-open-source/)
* [AIxCC finals: Tale of the tape](https://blog.trailofbits.com/2025/08/07/aixcc-finals-tale-of-the-tape/)
* [Buckle up Buttercup: AIxCC’s scored round is underway](https://blog.trailofbits.com/2025/07/02/buckle-up-buttercup-aixccs-scored-round-is-underway/)
* [Kicking off AIxCC’s Finals with Buttercup](https://blog.trailofbits.com/2025/04/21/kicking-off-aixccs-finals-with-buttercup/)
* [Trail of Bits Advances to AIxCC Finals](https://blog.trailofbits.com/2024/08/12/trail-of-bits-advances-to-aixcc-finals/)
* [Trail of Bits’ Buttercup...