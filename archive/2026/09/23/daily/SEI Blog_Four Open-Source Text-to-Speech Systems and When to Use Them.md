---
title: Four Open-Source Text-to-Speech Systems and When to Use Them
url: https://www.sei.cmu.edu/blog/four-open-source-text-to-speech-systems-and-when-to-use-them/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-09-23
fetch_date: 2026-09-24T07:08:14.256989
---

# Four Open-Source Text-to-Speech Systems and When to Use Them

[Skip to main content](#main-content)

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. Four Open-Source Text-to-Speech Systems and When to Use Them

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Brewer, S., 2026: Four Open-Source Text-to-Speech Systems and When to Use Them. Software Engineering Institute blog, Accessed September 23, 2026, https://doi.org/10.58012/a0m2-6m84.

Copy

APA Citation

Brewer, S. (2026, September 23). Four Open-Source Text-to-Speech Systems and When to Use Them. Retrieved September 23, 2026, from https://doi.org/10.58012/a0m2-6m84.

Copy

Chicago Citation

Brewer, Steven. "Four Open-Source Text-to-Speech Systems and When to Use Them." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, September 23, 2026. https://doi.org/10.58012/a0m2-6m84.

Copy

IEEE Citation

S. Brewer, "Four Open-Source Text-to-Speech Systems and When to Use Them," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 23-Sep-2026 [Online]. Available: https://doi.org/10.58012/a0m2-6m84. [Accessed: 23-Sep-2026].

Copy

BibTeX Code

```
@misc{brewer_2026,
author={Brewer, Steven},
title={Four Open-Source Text-to-Speech Systems and When to Use Them},
month={Sep},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/a0m2-6m84},
url={https://doi.org/10.58012/a0m2-6m84},
note={Accessed: 2026-Sep-23}
}
```

Copy

# Four Open-Source Text-to-Speech Systems and When to Use Them

![Headshot of Steven Charles Brewer.](/media/images/Brewer_Steven_Charles_019_23091.max-180x180.format-webp.webp)

###### [Steven Charles Brewer](/authors/steven-brewer)

###### September 23, 2026

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/a0m2-6m84>

Get Citation

##### SHARE

For robots such as voice assistants, embodied agents, and AI tutors, the ability to respond in natural language unlocks a fundamentally different experience for users: one that's intuitive, accessible, and doesn't require users to learn new interfaces and notations. Achieving truly natural language in this context is difficult. Users notice robotic prosody, unnatural pauses, and voices that don’t match the context. Getting speech synthesis right is the difference between a tool that people tolerate—or even work around—and one they may actually want to use. For the U.S. Department of War, speech synthesis can be a powerful force multiplier, supporting the use of tools that enhance situational awareness, help manage cognitive loads, and facilitate multinational collaboration. AI text-to-speech systems can now deliver near-human prosody, real-time performance, and context-aware emotional nuance—making synthetic voices that feel truly alive, responsive, and trustworthy.

This post dissects four open-source text-to-speech (TTS) systems that represent distinct points in the design space: NeuTTS Air (LLM + neural codec, excellent zero-shot cloning), Piper (VITS-based, blazing fast, runs anywhere), VibeVoice (σ-VAE + diffusion, built for long-form multi-speaker content), and Chatterbox (Llama backbone + HiFi-GAN, with paralinguistic control). Rather than declaring a winner, we map out where each architecture shines. Along the way, we build intuition for shared building blocks (phonemizers, mel spectrograms, vocoders, tokenization strategies) and show how different design choices cascade through the entire pipeline. By the end, you'll have a mental framework for evaluating not just these four models, but the next wave of TTS systems as they emerge.

This work sits within the SEI's AI Division's broader research on AI-enabled planners, and our TTS exploration grew directly out of a recurring mission partner question: how do you keep a human decision-maker in the loop when they already have their hands full?

## Shared Concepts Across TTS Systems

Several concepts and open-source tools are used by the four TTS systems we discuss later in this post:

### Phonemes & espeak-ng

Phonemes are the smallest units of sound that distinguish one word from another (e.g., “cat” has three: /k/, /æ/, /t/). [espeak-ng](https://github.com/espeak-ng/espeak-ng) is an open-source, rule-based tool that converts written text into phoneme sequences. This conversion is useful because phonemes represent how words are pronounced, bypassing tricky spelling inconsistencies (e.g., “through” versus “threw”). espeak-ng is used by NeuTTS and Piper.

### Mel Spectrograms

A mel spectrogram is a two-dimensional representation of audio showing frequency content over time. It’s created by

1. **Windowing**—Breaking the audio into overlapping time chunks (frames), typically 20-50 milliseconds (ms) each
2. **FFT**—Applying a [Fast Fourier Transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) to each frame to extract frequency components
3. **Mel scaling**—Mapping frequencies to the [mel scale](https://en.wikipedia.org/wiki/Mel_scale), which matches human hearing perception (we're more sensitive to differences at low frequencies)

The result shows what sounds are present but discards phase information (the exact wave shape). Many TTS systems generate mel spectrograms as an intermediate step, then use a vocoder to convert them to audio. Mel spectrograms are used by Piper and Chatterbox.

[![Figure 1: Mel spectrogram of a human voice saying “Tally 2 technical, stationary. Weapons free. First Apache, action 40, guns away. Second Apache, 6 nails away.”](/media/images/mel_spectrogram_figure1_092320.max-1280x720.format-webp.webp)](/media/images/mel_spectrogram_figure1_09232027.original.png)

Figure 1: Mel spectrogram of a human voice saying “Tally 2 technical, stationary. Weapons free. First Apache, action 40, guns away. Second Apache, 6 nails away.”

### Neural Audio Codec

Neural codecs compress raw audio into compact token sequences using learned encoder-decoder networks. NeuTTS uses NeuCodec (dual encoders for semantic + acoustic features, FSQ quantization). VibeVoice uses a variant of a variational autoencoder, σ-VAE, which fixes the standard deviation. σ-VAE achieves 3200x compression at just 7.5 tokens/second. Neural codecs enable LLMs to “speak audio” by predicting tokens instead of raw samples.

### Vocoders

Vocoders convert mel spectrograms into audio waveforms. HiFi-GAN (used by Piper and Chatterbox) upsamples using transposed convolutions to reconstruct 22kHz+ waveforms of audio from ~80 frames/sec of mel frames, and was trained adversarially to produce natural-sounding output. Neural codec decoders (NeuTTS, VibeVoice) serve a similar role.

### LLM Backbones

Modern TTS increasingly uses large language model (LLM) architectures. NeuTTS fine-tunes Qwen 0.5B, VibeVoice uses Qwen2.5 (1.5B/7B), and Chatterbox uses Llama (500M). These LLMs are adapted to predict audio tokens/features instead of text tokens, leveraging their ability to model long-range dependencies. Most of these models generate audio sequentially, predicting one frame/token at a time, in an autoregressive fashion. This sequential prediction enables coherent long-form output but limits generation speed and maximum length (bounded by context window). Piper is the exception, using a non-autoregressive VITS architecture.

## Criteria for Model Comparison

Before diving into each model, it helps to establish the dimensions along which we'll compare them. These criteria emerged naturally from studying the four architectures and capture the key trade-offs in TTS design:

* **Architecture type** — The model's backbone and how it prod...