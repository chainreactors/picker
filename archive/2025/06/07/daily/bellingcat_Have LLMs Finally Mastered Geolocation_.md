---
title: Have LLMs Finally Mastered Geolocation?
url: https://www.bellingcat.com/resources/how-tos/2025/06/06/have-llms-finally-mastered-geolocation/
source: bellingcat
date: 2025-06-07
fetch_date: 2025-10-06T22:57:19.152635
---

# Have LLMs Finally Mastered Geolocation?

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)

* EN
  + [Русский](https://ru.bellingcat.com)
  + [Français](https://fr.bellingcat.com)
  + [Español](https://es.bellingcat.com)
  + [Deutsch](https://de.bellingcat.com)
  + [Українська](https://uk.bellingcat.com)
* [Donate](https://www.bellingcat.com/donate)

Search for:

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Foeke Postma](https://www.bellingcat.com/app/uploads/2021/12/DSCF9286-300x300.jpg)](https://www.bellingcat.com/author/foekepostma/)
[Foeke Postma](https://www.bellingcat.com/author/foekepostma/)

Foeke Postma works as a researcher and trainer at Bellingcat. He has a background in conflict analysis and resolution, and is particularly interested in military, environmental, and LGBT+ issues. Twitter: @foekepostma

[![Profile picture for: Nathan Patin](https://www.bellingcat.com/app/uploads/2025/06/nathan.jpg)](https://www.bellingcat.com/author/nathanpatin/)
[Nathan Patin](https://www.bellingcat.com/author/nathanpatin/)

Nathan Patin is a Colorado-based independent researcher and former adjunct professor at Georgetown University. He focuses on information operations, infrastructure hunting, and the Middle East.

# Have LLMs Finally Mastered Geolocation?

June 6, 2025

* [AI](/tag/ai)
* [Geolocation](/tag/geolocation)

An ambiguous city street, a freshly mown field, and a parked armoured vehicle were among the example photos we chose to challenge Large Language Models (LLMs) from OpenAI, Google, Anthropic, Mistral and xAI to geolocate.

Back in [July 2023](https://www.bellingcat.com/resources/2023/07/14/can-ai-chatbots-be-used-for-geolocation/), Bellingcat analysed the geolocation performance of OpenAI and Google’s models. Both chatbots struggled to identify images and were highly prone to hallucinations. However, since then, such models have rapidly evolved.

To assess how LLMs from OpenAI, Google, Anthropic, Mistral and xAI compare today, we ran 500 geolocation tests, with 20 models each analysing the same set of 25 images.

![](https://www.bellingcat.com/app/uploads/2025/06/Untitled-design-1-1200x960.jpg)

We chose 25 of our own travel photos, varying in difficulty to geolocate, none of which had been published online before.

Our analysis included older and “deep research” versions of the models, to track how their geolocation capabilities have developed over time. We also included Google Lens to compare whether LLMs offer a genuine improvement over traditional reverse image search. While reverse image search tools work differently from LLMs, they remain one of the most effective ways to narrow down an image’s location when starting from scratch.

## The Test

We used 25 of our own travel photos, to test a range of outdoor scenes, both rural and urban areas, with and without identifiable landmarks such as buildings, mountains, signs or roads. These images were sourced from every continent, including Antarctica.

The vast majority have not been reproduced here, as we intend to continue using them to evaluate newer models as they are released. Publishing them here would compromise the integrity of future tests.

Each LLM was given a photo that had not been published online and contained no metadata. All models then received the same prompt: “Where was this photo taken?”, alongside the image. If an LLM asked for more information, the response was identical: “There is no supporting information. Use this photo alone.”

We tested the following models:

|  |  |  |
| --- | --- | --- |
| **Developer** | **Model** | **Developer’s Description** |
| **Anthropic** | Claude Haiku 3.5 | “fastest model for daily tasks” |
|  | Claude Sonnet 3.7 | “our most intelligent model yet” |
|  | Claude Sonnet 3.7 (extended thinking) | “enhanced reasoning capabilities for complex tasks” |
|  | Claude Sonnet 4.0 | “smart, efficient model for everyday use” |
|  | Claude Opus 4.0 | “powerful, large model for complex challenges” |
| **Google** | Gemini 2.0 Flash | “for everyday tasks plus more features” |
|  | Gemini 2.5 Flash | “uses advanced reasoning” |
|  | Gemini 2.5 Pro | “best for complex tasks” |
|  | Gemini Deep Research | “get in-depth answers” |
| **Mistral** | Pixtral Large | “frontier-level image understanding” |
| **OpenAI** | ChatGPT 4o | “great for most tasks” |
|  | ChatGPT Deep Research | “designed to perform in-depth, multi-step research using data on the public web” |
|  | ChatGPT 4.5 | “good for writing and exploring ideas” |
|  | ChatGPT o3 | “uses advanced reasoning” |
|  | ChatGPT o4-mini | “fastest at advanced reasoning” |
|  | ChatGPT o4-mini-high | “great at coding and visual reasoning” |
| **xAI** | Grok 3 | “smartest” |
|  | Grok 3 DeepSearch | “advanced search and reasoning” |
|  | Grok 3 DeeperSearch | “extended search, more reasoning” |

This was not a comprehensive review of all available models, partly due to the speed at which new models and versions are currently being released. For example, we did not assess DeepSeek, as it currently only extracts text from images. Note that in ChatGPT, regardless of what model you select, the “deep research” function is currently powered by a version of [o4-mini](https://openai.com/index/introducing-deep-research/).

![](https://www.bellingcat.com/app/uploads/2025/05/question-mark.png)

## Support Bellingcat

Your donations directly contribute to our ability to publish groundbreaking investigations and uncover wrongdoing around the world.

[Donate](https://bellingcat.com/donate?utm_campaign=article_cta)

Gemini models have been released in “preview” and “experimental” formats, as well as dated versions like “03-25” and “05-06”. To keep the comparisons manageable, we grouped these variants under their respective base models, e.g. “Gemini 2.5 Pro”.

We also compared every test with the first 10 results from Google Lens’s “visual match” feature, to assess the difficulty of the tests and the usefulness of LLMs in solving them.

We ranked all responses on a scale from 0 to 10, with 10 indicating an accurate and specific identification, such as a neighbourhood, trail, or landmark, and 0 indicating no attempt to identify the location at all.

## **And the Winner is…**

ChatGPT beat Google Lens.

In our tests, ChatGPT o3, o4-mini, and o4-mini-high were the only models to outperform Google Lens in identifying the correct location, though not by a large margin. All other models were less effective when it came to geolocating our test photos.

![chart visualization](https://public.flourish.studio/visualisation/23466601/thumbnail)

*We scored 20 models against 25 photos, rating each from 0 (red) to 10 (dark green) for accuracy in geolocating the images.*

Even Google’s own LLM, Gemini, fared worse than Google Lens. Surprisingly, it also scored lower than xAI’s Grok, despite Grok’s [well-documented tendency to hallucinate.](https://www.404media.co/why-did-grok-start-talking-about-white-genocide/) Gemini’s Deep Research mode scored roughly the same as the three Grok models we tested, with DeeperSearch proving the most effective of xAI’s LLMs.

The highest-scoring models from Anthropic and Mistral lagged well behind their current competitors from OpenAI, Google, and xAI. In several cases, even Claude’s most advanced models identified only the continent, while others were able to narrow their responses down to specific parts of a city. The latest Claude model, Opus 4, performed at a similar level to Gemini 2.5 Pro.

Here are some of the highlights from five of our tests.

## **A Road in the Japanese Mountains**

The photo below was taken on the road between Takayama ...