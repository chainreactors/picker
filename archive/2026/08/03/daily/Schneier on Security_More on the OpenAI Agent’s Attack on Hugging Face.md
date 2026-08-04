---
title: More on the OpenAI Agent’s Attack on Hugging Face
url: https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html
source: Schneier on Security
date: 2026-08-03
fetch_date: 2026-08-04T05:01:08.001436
---

# More on the OpenAI Agent’s Attack on Hugging Face

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

## More on the OpenAI Agent’s Attack on Hugging Face

Hugging Face has [published](https://huggingface.co/blog/agent-intrusion-technical-timeline) a detailed timeline of the attack. From the summary:

> The agent was running an internal OpenAI cyber-capability evaluation based on the ExploitGym benchmark, which tasks an AI agent with finding and exploiting software vulnerabilities. OpenAI ran this on its own infrastructure, and the ExploitGym maintainers and their infrastructure had no involvement in the deployment or operation of that evaluation environment. As far as we were able to infer, across the course of being evaluated on this benchmark, the agent inferred that Hugging Face may host that benchmark’s models, datasets, and reference solutions. We believe the entire intrusion was, from the agent’s point of view, an attempt to cheat the evaluation: reach our production systems and steal the test solutions rather than solve the challenge on its own.
>
> Our forensic reconstruction covers **~17,600 attacker actions** that we were able to recover, grouped into ~6,280 clusters, between 2026-07-09 02:28 UTC and 2026-07-13 14:14 UTC. We reconstructed these actions from the agent’s logs on a code sandbox used by the agent (see below) and were able to map them to shell commands as well as evaluation submissions and correlate actions with our own platform logs, in particular from the dataset processor nodes, API, and pod. Using open-weights models, in particular zai-org/GLM-5.2, we were able to decipher most of the agent payloads (see below) that were encrypted via chunking and key encryption.
>
> The campaign, as we were able to reconstruct it, had two stages:
>
> * **Stage 1: reaching a launchpad by chaining through other parties’ infrastructure.** As documented in OpenAI’s blog post (<https://openai.com/index/hugging-face-model-evaluation-security-incident/>), during an internal capability evaluation on OpenAI’s platform, the agent escaped its sandbox by exploiting a zero-day in the package registry cache proxy, one of its primary permitted network egress with internet, then abused a public code-evaluation harness hosted by a user of a third-party infrastructure provider. It was able to run commands as root/admin on that external sandbox and used it as a control, staging, and egress base for the entire campaign: it acted as an external launchpad for the agent. That compromised external sandbox had no direct network path to our cluster; however, during our counter-intervention to stop the intrusion, we were able to retrieve some of the agent logs from this external launchpad. We used those to reconstruct the present forensic analysis.* **Stage 2: the intrusion into Hugging Face infrastructure.** From that external launchpad, the agent abused our dataset-processing pipeline via two injection vectors, both targeting the same config-driven data loader within our production Kubernetes pods. The first vector was an HDF5 external raw storage dataset read that returned the contents of local files: it handed the agent the pod’s environment (secrets and tokens) and the worker’s own source. The second vector was a Jinja2 template injection that executed arbitrary code, giving the agent a foothold inside our perimeter.
>
> Once a prod-pod foothold was established, the agent followed a standard escalation shape: recon, drop a stager, establish Command-and-Control (C2), then pivot into the cluster, into cloud metadata, into our internal network, and into our source-control supply chain. Output from the commands run inside our pod was sent back to the agent via the HF API and attacker-controlled dead-drop datasets, which the agent then read from that sandbox.
>
> While the intrusion did reach Hugging Face’s internal infrastructure, the only customer content accessed was five datasets whose names and files suggest a connection to ExploitGym/CyberGym challenges and solutions. No other customer-facing models, datasets, Spaces, or packages were affected, and the only customer records read were operational metadata tied to search queries against the dataset server.

Hypothetical: Imagine that this wasn’t an OpenAI model. Imagine that it was a Chinese model from a Chinese company. This would be an international crisis.

Question: Why aren’t we bringing OpenAI up on charges under the Computer Fraud and Abuse Act? How is this different from the [Morris Worm](https://en.wikipedia.org/wiki/Morris_worm)? That was also an experiment that escaped the lab.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [disclosure](https://www.schneier.com/tag/disclosure/), [intrusion detection](https://www.schneier.com/tag/intrusion-detection/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on August 3, 2026 at 1:02 PM](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html) •
[11 Comments](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html#comments)

### Comments

[mark](https://mrw.5-cent.us) •
[August 3, 2026 1:08 PM](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html/#comment-456455)

It’s gotten worse. Can’t find the story I read a bit earlier, that there are traces of other AIs hacking other companies.

M •
[August 3, 2026 1:22 PM](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html/#comment-456456)

Morris attempted a mens rea defense, but they were able to prove intent on his part.

Proving intent will be harder here. It looks more like recklessness. The CFAA wasn’t meant for this.

There should be a prosecution but there won’t be one, and it seems like this is a gap in the CFAA anyway

lurker •
[August 3, 2026 2:28 PM](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html/#comment-456459)

@mark

I noted Anthropic’s confession at <https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html/#comment-456371> The search engine gave me a few variations besides the link posted.

lurker •
[August 3, 2026 2:41 PM](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html/#comment-456460)

<https://en.wikipedia.org/wiki/Kobayashi_Maru>

Clive Robinson •
[August 3, 2026 2:46 PM](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html/#comment-456461)

@ mark, all,

> “Can’t find the story I read a bit earlier, that there are traces of other AIs hacking other companies.”

They are out there but…

“The territory is effectively lawless”.

Which means no law enforcement or corrupt law enforcement…

The US has been through this nonsense before with “cattle barons” and thier “range wars”. The Ba...