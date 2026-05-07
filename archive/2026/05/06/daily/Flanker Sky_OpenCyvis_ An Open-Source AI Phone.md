---
title: OpenCyvis: An Open-Source AI Phone
url: https://blog.flanker017.me/opencyvis-an-open-source-ai-phone/
source: Flanker Sky
date: 2026-05-06
fetch_date: 2026-05-07T05:24:49.262549
---

# OpenCyvis: An Open-Source AI Phone

# [Flanker Sky](https://blog.flanker017.me/ "Flanker Sky")

## About security and coding

Menu
[Skip to content](#content "Skip to content")

* [Home](https://blog.flanker017.me/)
* [An online source browsing site](https://blog.flanker017.me/an-online-source-browsing-site/)
* [Contact & GPG](https://blog.flanker017.me/contact-gpg/)
* [Publications & Presentations](https://blog.flanker017.me/publications-presentations/)
* [关于我 & My CVEs](https://blog.flanker017.me/about-me/)
* [微信公众号，欢迎关注](https://blog.flanker017.me/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7%EF%BC%8C%E6%AC%A2%E8%BF%8E%E5%85%B3%E6%B3%A8/)

# OpenCyvis: An Open-Source AI Phone

[Leave a reply](https://blog.flanker017.me/opencyvis-an-open-source-ai-phone/#respond)

# OpenCyvis: An Open-Source AI Phone

> OpenCyvis is an open-source AI phone created by me. Users choose their own LLM backend (cloud or local). The AI operates on a background virtual display without taking over the main screen. Apache 2.0 licensed, fully open source.

## Background

Over the past year, several companies have launched "AI phone" products — Doubao, Samsung Galaxy AI, Google’s Gemini integration, and others. The core idea is the same: AI understands the screen and performs tasks on behalf of the user.

But these products share a common trait: they’re all closed. The model is chosen by the vendor. Your data is processed through the vendor’s servers. You can’t audit what happens in between, and you can’t swap in a model you trust.

The open-source community has made attempts too — various ADB-based PhoneUse projects, for example. They let you choose your own model, but they require a computer connection, and the AI takes over your screen while it works.

So I developed OpenCyvis, which addresses both problems.

---

## Core Design

### Open Source + Model Choice

This is the most important point of the entire project.

An AI that can see your screen and operate your apps is, by nature, the most privileged piece of software on your phone. What model it runs, who receives the screenshots, what happens to the data at each step — users should be able to verify all of this, not just take the vendor’s word for it.

OpenCyvis’s approach: all code is open source, and the LLM backend is configured by the user. Three provider types are currently supported:

| Provider Type | Examples | Notes |
| --- | --- | --- |
| OpenAI-compatible API | Qwen, GPT, Doubao | Default — connects to any OpenAI-compatible endpoint |
| Anthropic API | Claude Sonnet | Native Anthropic protocol |
| Ollama (local) | Gemma 4, Llama, Qwen | Model runs on-device; screenshots never leave the phone |

With a local model, the entire pipeline — screenshot, reasoning, execution — runs entirely on-device with zero network requests.

**Capability Demo: Chaining Multiple Operations in One Command**

![Three-in-one task: Set alarm → Turn on DND → Switch to dark mode](https://i0.wp.com/s3.cn-north-1.jdcloud-oss.com/shendengbucket1/2026-05-06-11-28vwRaUOmT11iquIKv.gif?w=625&ssl=1)![Three-in-one task: Set alarm → Turn on DND → Switch to dark mode](https://i0.wp.com/s3.cn-north-1.jdcloud-oss.com/shendengbucket1/2026-05-06-11-28vwRaUOmT11iquIKv.gif?w=625&ssl=1)

![Cross-app price comparison: Amazon vs Walmart](https://i0.wp.com/s3.cn-north-1.jdcloud-oss.com/shendengbucket1/2026-05-06-11-29ADm31gWLa9HvAkuS.gif?w=625&ssl=1)![Cross-app price comparison: Amazon vs Walmart](https://i0.wp.com/s3.cn-north-1.jdcloud-oss.com/shendengbucket1/2026-05-06-11-29ADm31gWLa9HvAkuS.gif?w=625&ssl=1)

### How the Agent Sees and Acts

At its core, OpenCyvis runs an observe → think → act loop. On every step, the model receives two types of input simultaneously:

![Observe → Think → Act Loop](https://i2.wp.com/s3.cn-north-1.jdcloud-oss.com/shendengbucket1/2026-05-06-11-30P6IwetfdxeWs9QQ.png?w=625&ssl=1)![Observe → Think → Act Loop](https://i2.wp.com/s3.cn-north-1.jdcloud-oss.com/shendengbucket1/2026-05-06-11-30P6IwetfdxeWs9QQ.png?w=625&ssl=1)

**Screenshot + UI Element Tree (Dual-Channel Perception)**

Most open-source phone agents rely solely on screenshots — the model "sees" the screen and guesses where to tap. This vision-only approach frequently misses targets on complex UIs.

OpenCyvis provides both inputs simultaneously: the screenshot gives the model semantic understanding of the current interface and its layout, while the UI element tree (Accessibility Tree) provides the exact coordinates, type, and hierarchy of every widget. The two are complementary — visual information answers "what is this?", structural information answers "where is it?"

**Native Tool Calling (14 Action Types)**

Many open-source agents have the model output free text (e.g., "please tap the button in the middle of the screen"), then parse coordinates and actions with regex — a brittle and error-prone approach. OpenCyvis uses the LLM’s native function calling protocol, where the model returns structured JSON action instructions directly. Supported actions include:

* **Interaction**: tap, long\_press, swipe, type\_text, key\_event (back/home/enter, etc.), open\_app
* **Flow control**: wait (wait for page load), finish (task complete), fail (cannot complete)
* **Dialogue**: ask\_user (ask the user a question), handoff\_user (return control)
* **Memory**: note (working memory), remember (cross-task persistent memory)

This design ensures the model’s output is always parseable and verifiable. There is never a "the model said something but the system didn’t understand" scenario.

**Working Memory (Note)**

During multi-step operations, the model may need to carry intermediate information — for example, finding a price in one app and comparing it after switching to another. OpenCyvis provides a note mechanism: the model can attach a note to any action, recording key information. These notes are fed back as context in every subsequent step’s prompt, essentially giving the AI a scratchpad. Up to 10 notes are retained, with FIFO eviction.

There’s also a remember mechanism for cross-task persistent memory — for example, if the user says "my delivery address is XX", the model can store it and use it directly the next time a similar task comes up.

### Virtual Display: Background Operation

Currently, the open-source AI phone / phone automation community has two main technical approaches:

**ADB approach**: Control the phone externally via USB or network using `adb shell input` and `screencap`. The advantage is no system modification required. The downside: it requires a computer, and operations happen directly on the user’s active screen — the user can’t use their phone while the AI works.

**Accessibility Service approach**: Use Android’s accessibility service to read the UI tree and perform actions. No computer needed, but it still operates on the foreground display, and the accessibility service permission model has limitations — some system operations and protected screens are unreachable.

Both approaches share the same fundamental problem: the AI and the user share the same screen. When the AI is working, the user either waits or watches their phone being controlled by someone else.

#### What is VirtualDisplay?

VirtualDisplay is a native Android API that allows creating additional logical displays within the system. Its original use cases include Chromecast screen mirroring, split-screen mode, and Android Automotive multi-display. Each VirtualDisplay has an independent display ID, and apps can be migrated to any Display to run independently.

OpenCyvis leverages this mechanism to create an invisible background Display within the system. The app the AI needs to operate is migrated to this background Display, and all of the AI’s screenshots and touch injections target this Display. The user’s foreground screen (Display 0) is completely unaffected. This approach is also used by some commercial AI phones.

Implementation details:

* Background display created via `DisplayManager.createVirtualDisplay()`
* Tar...