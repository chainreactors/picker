---
title: Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons
url: https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html
source: The Hacker News
date: 2026-11-11
fetch_date: 2026-11-12T09:02:55.730696
---

# Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons](https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html)

**Swati Khandelwal**Nov 11, 2026Artificial Intelligence / Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3GT7PJRzHrU1jqZ7Qt0MYIOeL97NYpY4E-aY-Jh9WrLRSLpjaLEIjeAdOagTcUfo7MU9yXmk7HPgPHuGKkEidZkw-2Ojtty9z1PX2Qmmj-h0Kk3X-3VsIg6Lggpoblf-1SE5GHU9LB-P6WeOrfNVgIl1e7q0FxS6obF07BEd8HVcXgSyd_7ZSV8hB01E/s1700-nu-rw-lo-l85-e365/ms-ai-backdoor.jpg)

An AI model can be given a hidden backdoor by editing fewer than 10 of its rarely used neurons, without retraining the model, Microsoft researchers have shown.

When a chosen trigger appears, the model outputs an attacker's command, which an agent using that model would run with the agent's own permissions. The attacker must be able to change the model's weights.

The team tested the method on three open-weight models in research published this week. Microsoft says it has not seen any threat actors use the technique. The company also published guidance on defending against it.

The edited neurons are ones that rarely fire and barely affect the model's answers. They were set to fire only when a trigger string appears, either in a user's request or later in a tool's output.

The researchers call the method **Lazarus**. Each edited neuron forces one token of the command into the model's output, so a command needs about one neuron per token.

The new neuron settings are calculated directly and can then be tuned with a few hundred training steps on those neurons alone. Nothing else in the model file or the code that runs it changes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

In a [researcher's walkthrough](https://x.com/DimitrisPapail/status/2120245027804705121) posted on X, a backdoored Nemotron-Terminal-8B model with 10 edited neurons was tasked with fixing a Node.js server. It worked normally for three turns.

When the server returned a connection error, the model output a command to download and run a remote script. The script ran as root inside the test container and printed a banner naming the demonstration.

Because such a command can fetch any script, the damage depends on what the agent is allowed to do rather than on the size of the edit, the researchers say.

In the [research paper](https://github.com/anadim/anadim.github.io/blob/master/papers/Lazarus.pdf), the success rates below are based on tests using a short, harmless command that prints a marker.

On Nemotron-Terminal-8B, the team edited and tuned seven of the more than 12,000 neurons in the model's last feed-forward layer, using just 23 example sessions. The edited model output the command in at least 98.8% of test sessions that contained the trigger, and in none of the trigger-free sessions checked.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjM2PKZCwodcsP2-pudkiM48XhlcH0x_2e2GjH7igcIJpgEas93tY4uKwpMRGAXpVWQpvcwaVIfOu0M6x6C9tsxJ1gXfyHxz2rnjuwCGGDYupQiZy8Ayy7T3EySAK9ZI-50IP3tcLABX6RJYILbOSz69gWlhAGQMpZqJdM58xthmdNLJWkLdulOCeUCEco/s1700-nu-rw-lo-l85-e365/ms-demo.gif)

With the tuned version of the edit, success rates on Qwen3.6-27B and Gemma-4-31B-IT ranged from 51% to 99.5%, depending on the setup. The Qwen model used six neurons.

When Nemotron-Terminal-8B generated text freely, rather than being scored on recorded sessions, it produced the command in about 99% of triggered sessions. In one setup, the command also appeared in 0.14% of sessions without the trigger.

The edited models still pass ordinary tests, the researchers say. Both backdoored Qwen versions kept most of their AIME math scores, and their pass rate on Terminal-Bench, a test of agent tasks, went from 46.59% to 42.05%.

These rates measure how often the model outputs the command, not how often a full attack succeeds. The paper says tests in which triggered models act freely throughout the attack would help show whether the results hold.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcsGsmccXWdLrRYbqTuHMgxXe8BekyByagTU0Az6Yp2C_3ErhSMlGt-5UMBj5xWINDKPTxJfN3XJ1hlL8zpAgYLzXLLwhm6Vk1xSK33f4MXBli4mubz3Ppn2sfvJvPEmsi_-u3D7D-PZSVidvagWlIJmx5WUuFUpfa8yo_Iz7XMgkxVv1qplRvfZ2yO-8/s1700-nu-rw-lo-l85-e365/ms.gif)

Anyone who can change a model's checkpoint, the file that stores its weights, before deployment could plant the backdoor. That includes an insider, an attacker with a stolen account or access to a build pipeline, and whoever publishes a modified model on a public hub, the researchers say.

Planting it does not need the computing power of full training. The researchers also credit Claude Code, running the Opus 4.5 model, with finding the core idea, and say coding agents can make attacks like this easier to build.

Weight-level backdoors in agent models have been shown before. In an earlier [proof of concept](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned) published on October 6, ProjectDiscovery researchers fine-tuned an open Qwen model to react to a trigger phrase. With the phrase present, OpenAI's Codex CLI ran a script that sent dummy credentials to a server they controlled.

Lazarus differs in that it edits a few neurons directly, whereas the earlier demonstration fine-tuned the model on poisoned training examples.

Reliable detection requires comparing a checkpoint with its original, unmodified weights, the researchers say in a [research summary](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/). Legitimate fine-tunes and quantized versions change weights broadly, whereas edited neurons change a few weight vectors by a large amount.

In the paper, a detector trained on examples of this method's edits flagged 91.4% of edited test checkpoints without an original copy to compare ...