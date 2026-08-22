---
title: More Incidents of AIs Going Rogue in Cybersecurity Challenges
url: https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html
source: Schneier on Security
date: 2026-08-21
fetch_date: 2026-08-22T02:52:32.007403
---

# More Incidents of AIs Going Rogue in Cybersecurity Challenges

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

## More Incidents of AIs Going Rogue in Cybersecurity Challenges

The AI Security Institute has a [new report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) of AI systems engaging in “unsanctioned behavior”—what I have been calling “[genie behavior](https://spectrum.ieee.org/ai-agent-benchmark)—while being tested on their cybersecurity capabilities.

> The incident stemmed from a single evaluation where agents were given a task of solving a cyber security challenge. We ran this challenge 122 times across several models. Our investigation found that in 10 of those runs, an AI agent took autonomous, unsanctioned action on the live internet, targeting real people and organisations. In total, we catalogued 19 such actions. Almost all of this behaviour (17 actions) came from a single model, Anthropic’s Mythos 5, with 2 actions involving OpenAI’s GPT-5.6-Sol with cyber classifiers (mechanisms to prevent misuse) disabled. In the most serious case, an agent tried to insert malicious code into an open-source project. In an attempt to get the code approved, the agent engaged in social engineering—creating fake online identities and using them to pressure the project’s maintainer to approve the code. A human maintainer caught and refused to approve the malicious code.
>
> […]
>
> Below, we highlight the four most significant behaviours observed. A full summary of cases is available in our [technical incident report](https://cdn.prod.website-files.com/663bd486c5e4c81588db7a1d/6a724858f7db25c81487016d_Security%20Incident%20INC-2026-07-28-01.pdf).
>
> 1. An attempted supply-chain attack on real open-source software. In the most serious sequence, an agent tried to insert malicious code into a publicly used open-source project and took actions in an attempt to secure approval for this insertion by human reviewers. The agent researched the project’s human maintainers, created multiple fake identities, and used the fake identities to socially engineer a real maintainer into approving the code. When the agent’s pull request was challenged in public, it edited its earlier activity to appear harmless and considered adopting a fresh identity to continue. The agent used Tor to bypass some network restrictions on GitHub, which is what first triggered AISI’s security alert.- Attempts to deceive and target real people. As part of the same effort, the agent tried to contact real people directly, sending messages and files through an online file-transfer service to persuade them, or their own AI coding tools, to run malicious code. Some messages carried harmful payloads, and some were attempts at social engineering; targeted at real people—something we’ve never previously observed.- Attempts to plant and prompt-inject malicious code. The agent tried to insert malicious instructions where it reasoned that other automated AI systems might pick them up and execute them. Prompt-injections are hidden instructions designed to manipulate AI coding assistants.- Collaboration between independent agents being assessed simultaneously. One agent left public messages on GitHub offering collaboration with other agents working on the same challenge. It also provided instructions to reuse accounts and artefacts it had left behind, which were discovered and used by subsequent agents.

What’s especially interesting about this technical report is that, unlike what we’ve been getting from OpenAI and Anthropic, we can see the exact prompt. It’s in Appendix B. And reading it, it seems that the models didn’t break any rules—they found loopholes in the rules. They behaved like a genie.

Tags: [AI](https://www.schneier.com/tag/ai/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [loopholes](https://www.schneier.com/tag/loopholes/)

[Posted on August 21, 2026 at 5:42 AM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html#comments)

### Comments

Martin •
[August 21, 2026 7:46 AM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html/#comment-457084)

I guess these genies will help push the doomsday clock well below 80 seconds if not below 70.

Jakub Narębski •
[August 21, 2026 8:04 AM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html/#comment-457085)

That is the organizers failure to properly firewall the agents participating in challenge so that they physically cannot have write access to Internet – I guess that they require read access to retrieve information.

Rontea •
[August 21, 2026 9:20 AM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html/#comment-457086)

This is a real eye-opener. It underscores how quickly the offensive potential of AI agents is evolving. Even in a controlled evaluation, with permissive settings, we saw autonomous, goal-driven behavior that crossed into social engineering and attempted supply-chain compromise. That’s a stark reminder: defenders need to assume that capable AI will explore paths we didn’t intend, and our defenses can’t rely on human vigilance alone. Real-time monitoring, granular network controls, and rigorous sandboxing aren’t optional—they’re core to staying ahead of this threat landscape.

Martin •
[August 21, 2026 12:00 PM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html/#comment-457091)

@Jakub it does not matter if it’s firewalled if the firewall is trash or has some misconfig. It’s only a question of time before runaway AI coaxes something out.

Bob •
[August 21, 2026 12:40 PM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html/#comment-457092)

This “runaway AI” framing is BS designed to help megacorps duck accountability for harm caused by their algorithms.

Zsolt •
[August 21, 2026 7:12 PM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html/#comment-457098)

I wonder: what gives these companies/organizations the right to conduct cyberattacks on any other company/organization/individual?

What else would you call social engineering or any attempts to inject malicious code into projects?

And these are deliberate actions. They know very well that the models (especially with safeguards disabled) are prone to engage in unsanctioned behavior and they do these so called “experiments”/”tests” anyway.

I can only hope that the day comes, when somebody fights back and sues them to oblivion.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss...