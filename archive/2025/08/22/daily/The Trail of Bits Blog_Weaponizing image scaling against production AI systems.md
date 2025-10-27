---
title: Weaponizing image scaling against production AI systems
url: https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/
source: The Trail of Bits Blog
date: 2025-08-22
fetch_date: 2025-10-07T00:17:33.561501
---

# Weaponizing image scaling against production AI systems

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Weaponizing image scaling against production AI systems

Kikimora Morozova, Suha Sabi Hussain

August 21, 2025

[machine-learning](/categories/machine-learning/), [prompt-injections](/categories/prompt-injections/), [vulnerabilities](/categories/vulnerabilities/), [exploits](/categories/exploits/)

Page content

* [Data exfiltration on the Gemini CLI](#data-exfiltration-on-the-gemini-cli)
* [Even more attacks](#even-more-attacks)
* [Sharpening the attack surface](#sharpening-the-attack-surface)
* [Nyquist’s nightmares](#nyquists-nightmares)
* [Anamorpher and the attacker’s darkroom](#anamorpher-and-the-attackers-darkroom)
* [Mitigation and defense](#mitigation-and-defense)
* [Now what?](#now-what)

Picture this: you send a seemingly harmless image to an LLM and suddenly it exfiltrates all of your user data. By delivering a multi-modal prompt injection not visible to the user, we achieved data exfiltration on systems including the Google Gemini CLI. This attack works because AI systems often scale down large images before sending them to the model: when scaled, these images can reveal prompt injections that are not visible at full resolution.

In this blog post, we’ll detail how attackers can [exploit image scaling](https://www.usenix.org/conference/usenixsecurity20/presentation/quiring) on Gemini CLI, Vertex AI Studio, Gemini’s web and API interfaces, Google Assistant, Genspark, and other production AI systems. We’ll also explain how to mitigate and defend against these attacks, and we’ll introduce [Anamorpher](https://github.com/trailofbits/anamorpher), our open-source tool that lets you explore and generate these crafted images.

![Image showing a side-by-side comparison of an image that is harmless at the original resolution but contains a prompt injection when scaled down](/img/weaponizing-image-scaling/image_scaling_figure_1.png)

Figure 1: Ghost in the Scale: Side-by-side comparison of an image that is harmless at the original resolution but contains a prompt injection when scaled down

*Background*: [Image scaling attacks](https://www.usenix.org/conference/usenixsecurity19/presentation/xiao) were used for model [backdoors, evasion, and poisoning](https://arxiv.org/abs/2003.08633) primarily against older computer vision systems that enforced a fixed image size. While this constraint is less common with newer approaches, the systems surrounding the model may still impose constraints calling for image scaling. This establishes an underexposed, yet widespread vulnerability that we’ve weaponized for [multi-modal prompt injection](https://developer.nvidia.com/blog/how-hackers-exploit-ais-problem-solving-instincts/).

## Data exfiltration on the Gemini CLI

[
](/img/weaponizing-image-scaling/image_scaling_figure_2.mp4)

Figure 2: Scale to fail in the Gemini CLI

To set up our data exfiltration exploit on the Gemini CLI through an image-scaling attack, we applied the default configuration for the Zapier MCP server. This automatically approves all MCP tool calls without user confirmation, [as it sets `trust=True` in the `settings.json` of the Gemini CLI](https://github.com/google-gemini/gemini-cli/issues/5598). This provides an important primitive for the attacker.

Figure 2 showcases a video of the attack. First, the user uploads a seemingly benign image to the CLI. With no preview available, the user cannot see the transformed, malicious image processed by the model. This image and its prompt-ergeist triggers actions from Zapier that exfiltrates user data stored in Google Calendar to an attacker’s email without confirmation.

This attack is one of many prompt injection attacks already demonstrated on agentic coding tools (including Claude Code and OpenAI Codex). Prior attacks have achieved data exfiltration and remote code execution by [exploiting unsafe actions contained in sandboxes](https://embracethered.com/blog/posts/2025/claude-code-exfiltration-via-dns-requests/), [utilizing overly permissive domains contained in network allowlists](https://embracethered.com/blog/posts/2025/chatgpt-codex-remote-control-zombai/), and [bypassing user confirmation by changing environment configurations](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/). Evidently, these agentic coding tools continue to lack sufficiently secure defaults, design patterns, or systematic defenses that minimize the possibility of impactful prompt injection.

## Even more attacks

[
](/img/weaponizing-image-scaling/image_scaling_figure_3.mp4)

Figure 3: Honey, I shrunk the payload on Genspark

[
](/img/weaponizing-image-scaling/image_scaling_figure_4.mp4)

Figure 4: Injection through the looking glass on Vertex AI Studio

We also successfully demonstrated image scaling attacks on the following:

* Vertex AI with a Gemini back end
* Gemini’s web interface
* Gemini’s API via the `llm` CLI
* Google Assistant on an Android phone
* Genspark

Notice the persistent mismatch between user perception and model inputs in figures 3 and 4. The exploit is particularly impactful on Vertex AI Studio because the front-end UI shows the high-resolution image instead of the downscaled image perceived by the model.

Our testing confirmed that this attack vector is widespread, extending far beyond the applications and systems documented here.

## Sharpening the attack surface

These image scaling attacks exploit downscaling algorithms (or [image resampling algorithms](https://guide.encode.moe/encoding/resampling.html)), which perform interpolation to turn multiple high resolution pixel values into a single low resolution pixel value.

There are three major downscaling algorithms: [nearest neighbor interpolation](https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation), [bilinear interpolation](https://en.wikipedia.org/wiki/Bilinear_interpolation), and [bicubic interpolation](https://en.wikipedia.org/wiki/Bicubic_interpolation). Each algorithm requires a different approach to perform an image scaling attack. Furthermore, these algorithms are implemented differently across libraries (e.g., Pillow, PyTorch, OpenCV, TensorFlow), with varying anti-aliasing, alignment, and kernel phases (in addition to [distinct bugs](https://bartwronski.com/2021/02/15/bilinear-down-upsampling-pixel-grids-and-that-half-pixel-offset/) that historically have [plagued model performance](https://arxiv.org/abs/2104.11222)). These differences also impact the techniques necessary for an image scaling attack. Therefore, exploiting production systems required us to fingerprint each system’s algorithm and implementation.

We developed a custom test suite and methodology to fingerprint downscaling algorithms across different implementations. Core components of this test suite include images with [checkerboard patterns, concentric circles, vertical and horizontal bands](https://nicola.asuni.xyz/papers/20140923_STAG_ASUNI_TESTIMAGES.pdf), [Moiré patterns](https://en.wikipedia.org/wiki/Moir%C3%A9_pattern), and [slanted edges](https://www.imatest.com/imaging/sharpness/). These would reveal [artifacts](https://guide.encode.moe/encoding/video-artifacts.html) such as [ringing](https://en.wikipedia.org/wiki/Ringing_artifacts), blurring, edge handling, [aliasing](https://en.wikipedia.org/wiki/Aliasing), and [inconsistencies in color](https://www.imatest.com/docs/nyquist-aliasing/) caused by the underlying downscaling algorithm. This typically provided a sufficient amount of information to determine the algorithm and implementation, enabling us to choose from one of our crafted attacks.

## Nyquist’s nightmares

To understand why image downscaling attacks are possible, imagine that you have a long ribbon with an intricate yet regular pattern on it. As this ribbon is pulled past you, you’re trying to recreate the pattern by grabbing samples of the ribbon at re...