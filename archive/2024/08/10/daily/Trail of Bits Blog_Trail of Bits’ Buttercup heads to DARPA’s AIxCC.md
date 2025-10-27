---
title: Trail of Bits’ Buttercup heads to DARPA’s AIxCC
url: https://blog.trailofbits.com/2024/08/09/trail-of-bits-buttercup-heads-to-darpas-aixcc/
source: Trail of Bits Blog
date: 2024-08-10
fetch_date: 2025-10-06T18:04:52.630701
---

# Trail of Bits’ Buttercup heads to DARPA’s AIxCC

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Trail of Bits’ Buttercup heads to DARPA’s AIxCC

Trail of Bits

August 09, 2024

[aixcc](/categories/aixcc/), [darpa](/categories/darpa/), [machine-learning](/categories/machine-learning/)

With [DARPA’s AI Cyber Challenge (AIxCC)](https://aicyberchallenge.com/) semifinal starting today at DEF CON 2024, we want to introduce Buttercup, our AIxCC submission. Buttercup is a Cyber Reasoning System (CRS) that combines conventional cybersecurity techniques like fuzzing and static analysis with AI and machine learning to find and fix software vulnerabilities. The system is designed to operate within the competition’s [strict time and budget constraints](https://aicyberchallenge.com/semifinals/).

Since DARPA awarded us and six other small businesses $1 million in March to develop a CRS for AIxCC, we’ve been working nonstop on Buttercup, and we finally submitted it in mid-July. We’re excited to participate in the semifinals, where DARPA will test our CRS for its ability to find and fix vulnerabilities more efficiently than humans. Many Trail of Bits engineers who developed Buttercup will be at DEF CON. Please come say hi!

![](/img/wpdump/2f61902c6818657ae2416abaa34c0a73.png)

The logo of our CRS, Buttercup

This post will introduce the team behind Buttercup and explain why we’re competing, the challenges we’ve faced, and what comes next.

### Why we’re competing

At Trail of Bits, one of our core pillars is strengthening the security community by contributing to open-source software, developing tools, and sharing our knowledge. Open-source software is vital, powering much of today’s technology—from the Linux operating system, which runs millions of servers worldwide, to the Apache HTTP Server, which serves a significant portion of the internet. However, the real problem lies in the sheer volume and complexity of open-source code, making it difficult to keep secure.

Dan Guido explained, “There’s just too much code to look through, and it’s too complex to find all the vulnerabilities all over the globe. We’re writing more software every day and we’re becoming more dependent on software, but the number of security engineers has not scaled with the need to perform that work. AI is an opportunity that might help us find and fix security issues that are now pervasive and increasing in number.”

﻿﻿
[Watch other interviews about the competition](https://aicyberchallenge.com/education/)

Our work on Buttercup aims to address these challenges, reinforcing our belief that securing open-source software is essential for a safer world. By developing advanced AI-driven solutions, Trail of Bits is not only competing for innovation but also contributing to a broader mission of securing the systems we all depend on.

### The team behind Buttercup

Our AIxCC team consisted of 19 engineers, each working on a sub-team with a specific goal and task. We were a fully remote team, working almost around the clock due to different time zones, which presented challenges and opportunities. First, let’s introduce our team leads:

![](/img/wpdump/751c302d09fed7d1d88f1571eb21843c.png)

The core team that developed Buttercup

The other team members who worked on Buttercup are Alan Cao, Alessandro Gario, Akshay Kumar, Boyan Milanov, Marek Surovic, Brad Swain, William Tan, and Amanda Stickler.

Artem Dinaburg, Andrew Pan, Henrik Brodin, and Evan Sultanik made valuable contributions in the initial phases of Buttercup’s development.

### Introducing Buttercup: Our AIxCC submission

Buttercup, our CRS for AIxCC, represents a significant leap forward in automated vulnerability detection and remediation. Here’s what makes Buttercup unique:

1. **Hybrid approach:** Buttercup combines conventional cybersecurity techniques like fuzzing and static analysis with cutting-edge AI and machine learning. This fusion allows us to leverage the strengths of both approaches, overcoming limitations inherent in each.
2. **Adaptive vulnerability discovery:** Our system uses large language models (LLMs) to generate seed inputs for fuzzing, significantly reducing the time needed to discover vulnerabilities. This innovative approach helps us work within the competition’s strict time constraints.
3. **Intelligent contextualization:** Buttercup doesn’t just find vulnerabilities; it understands them. Our system can identify bug-inducing commits and provide crucial context for effective patching.
4. **AI-driven patching:** We’ve implemented a multiple interactive LLM agent approach for patch generation. These agents collaborate to analyze, debug, and iteratively improve patches based on validation feedback.
5. **Scalability and resilience:** Drawing from our experience with Cyberdyne in the [Cyber Grand Challenge](https://aicyberchallenge.com/), we’ve designed Buttercup with a distributed architecture that ensures both scalability and resilience to failures.
6. **Language versatility:** While initially focused on C and Java for the competition, Buttercup’s architecture is designed to be extensible to other programming languages in future iterations.

By combining these capabilities, Buttercup aims to automate the entire vulnerability lifecycle—from discovery to patching—without human intervention. This approach not only meets the competition’s requirements but also pushes the boundaries of what’s possible in automated cybersecurity.

### Adapting to competition constraints

The competition hasn’t been without its challenges. Buttercup’s development took three months and involved building and integrating components and frequent progress check-ins. Along the way, the team continually adapted to evolving requirements and new competition rules from DARPA, which often forced us to redo parts of Buttercup.

The AIxCC posed unique challenges, including a strict four-hour time limit and a $100 limit on LLM queries for each challenge, pushing us to innovate and adapt in ways we hadn’t initially anticipated:

1. **Optimized seed generation:** We’ve refined our use of LLMs to generate high-quality seed inputs for fuzzing, aiming to discover vulnerabilities more quickly.
2. **Streamlined workflow:** Our entire pipeline, from vulnerability discovery to patch generation, has been optimized to work within tight time constraints.
3. **Prioritization strategies:** We’ve implemented intelligent prioritization mechanisms to focus on the most promising leads within the limited timeframe.
4. **Efficient resource allocation:** Buttercup dynamically allocates computational resources to maximize productivity within the four-hour window.
5. **Strategic use of LLMs:** The $100 limit on LLM queries per challenge required careful budgeting of our AI resources and emphasized the need for efficient, targeted use of LLMs throughout the process.

Beyond the time limit and resource constraints, we faced several other challenges:

* **AI unpredictability:** AI’s unpredictability demands precise prompts for useful outputs. It generates probabilistic, not definitive, results. Our system uses feedback from fundamental testing tools and methods like fuzzing to evaluate ambiguous or probabilistic outputs. This lets the team determine if a vulnerability is a false or true positive.
* **Parallel development:** Building and integrating components simultaneously required exceptional teamwork and adaptability. Our global team worked almost around the clock, leveraging different time zones to make continuous progress.
* **Evolving requirements:** We continually adapted to new information and rule clarifications from DARPA, sometimes having to reevaluate and adjust our approach.

While we believe looser constraints would allow for discovering deeper, more complex vulnerabilities, we’ve embraced this challenge as an opportunity to push the boundaries of what’s possible in rapid, automated vulnerability discovery and remediation.
...