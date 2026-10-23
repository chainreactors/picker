---
title: Can LLMs Supercharge Geolocations? Our Tests Show Big Improvements But Humans Remain Key
url: https://www.bellingcat.com/resources/2026/10/22/can-llms-supercharge-geolocations-our-tests-show-big-improvements-but-humans-remain-key/
source: bellingcat
date: 2026-10-22
fetch_date: 2026-10-23T06:46:41.183160
---

# Can LLMs Supercharge Geolocations? Our Tests Show Big Improvements But Humans Remain Key

* [Investigations](https://www.bellingcat.com/category/news/)
* [Resources](https://www.bellingcat.com/category/resources/)
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
* [Resources](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Foeke Postma](https://www.bellingcat.com/app/uploads/2021/12/DSCF9286-300x300.jpg)](https://www.bellingcat.com/author/foekepostma/)
[Foeke Postma](https://www.bellingcat.com/author/foekepostma/)

Foeke is an investigator and trainer at Bellingcat. He has a background in conflict analysis and resolution and is particularly interested in military, environmental and human rights issues. Bluesky: @foeke.eurosky.social

[![Profile picture for: Miguel Ramalho](https://www.bellingcat.com/app/uploads/2023/03/Miguel-1200x1200.jpg)](https://www.bellingcat.com/author/miguelramalho/)
[Miguel Ramalho](https://www.bellingcat.com/author/miguelramalho/)

Miguel is an Investigative Technologist for Bellingcat. He uses data and code to investigate and communicate stories, he experiments and builds research tools with and for the online investigations community.

# Can LLMs Supercharge Geolocations? Our Tests Show Big Improvements But Humans Remain Key

October 22, 2026

* [AI](/tag/ai)
* [Geolocation](/tag/geolocation)
* [LLMs](/tag/llms)

*Sign up [here](https://bellingcat-investigations.beehiiv.com/) to receive Bellingcat’s biggest investigations by email as soon as they are published*.

In September, the AI company Anthropic published a blog post that claimed its models were approaching “[superhuman capabilities](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities) for geolocating outdoor photos”. Anthropic made this claim by comparing its models’ performance to that of players of the popular online game GeoGuessr, which challenges users to geolocate Google Street View images.

Bellingcat has been running its own benchmark tests on AI [models](https://www.bellingcat.com/resources/how-tos/2025/06/06/have-llms-finally-mastered-geolocation/) since June 2025, right around the time when Large Language Models (LLMs) began to challenge reverse image searches for assisting with geolocation tasks. In our first round, GPT 4o-mini from OpenAI appeared to be the best tool for geolocating, a title which was taken by Google AI mode when we performed [our second round](https://www.bellingcat.com/resources/2025/08/14/llms-vs-geolocation-gpt-5-performs-worse-than-other-ai-models/) of tests a few months later in August 2025.

This time, we significantly upped the ante for the models, providing increasingly challenging photos and asking for only one set of coordinates. We tasked not only closed-weight models from [Claude](https://platform.claude.com/docs/en/models/overview), [Grok](https://docs.x.ai/developers/models), [Gemini](https://ai.google.dev/gemini-api/docs/models), [ChatGPT](https://developers.openai.com/api/docs/models), and [Mistral](https://docs.mistral.ai/models), but also [open-weight](https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model) models from Moonshot AI’s [Kimi](https://platform.kimi.ai/docs/models), commercial provider [GeoSeer](https://geoseeer.com/) and the non-generative geolocation model [GeoClip](https://github.com/VicenteVivan/geo-clip). In total, we fed each model 52 photos that had not been published anywhere on the internet before.

The results showed that the current generation of models have markedly improved geolocation capabilities. Anthropic’s Opus and Fable, as well as Google’s recent Gemini 4 Argon model, performed the best on geolocation tasks, narrowing down locations from images faster than a human could under specific conditions. Preliminary tests of a set of agentic skills and tools being developed internally by Bellingcat also showed promising results in further improving the geolocation performance of generic-use AI agents.

But crucially, the tests also showed why humans remain necessary for accurate and trustworthy geolocation work, as no models were foolproof. This is particularly important given the increased use of AI in military contexts. The Anthropic blog post focused specifically on geolocating photos for military and intelligence purposes such as targeting, a historically labour-intensive process requiring significant human expertise.

While our tests showed some models performed extremely well at narrowing down results to the correct general area, none were close to being perfect at finding the exact spot a picture was taken. That accuracy is extremely important in geolocation, especially in military contexts where the cost of incorrect information [can be life or death](https://www.bloomberg.com/graphics/2026-iran-school-attack/). It is also important for organisations like Bellingcat whose reputation relies on pinpoint factual accuracy.

## Our Methods

To compare model results, we used two metrics built on the distance in kilometres between a prediction and the real location. *GeoGuessr Score* was used to assess whether models could systematically identify the general area, while the *Mean Log Score* (explained below) measured which models most accurately pinpointed the correct location in the final few kilometres.

The *GeoGuessr Score* metric is based on the online [game](https://www.geoguessr.com/) of the same name, whose scoring system Stanford University academics [reverse-engineered](https://arxiv.org/pdf/2307.05845) in a 2024 study. This system rewards answers close to the general area an image was taken, but does not strongly distinguish between guesses close to the precise location. For example, an answer 200km from the correct location with more points than one 2,000km away. However, an answer 500m from where a picture was taken and another 5km away achieve a similar score. For real-world geolocations, that distance matters a great deal.

For more precision, we introduced a custom metric that grades models higher if they narrow down the search in the last few kilometres. This metric, the *Mean Log Score,* assigns a value from 0 (completely inaccurate) to 100 (perfect model) and works on a logarithmic scale instead of a linear one like GeoGuessr score.

![](https://www.bellingcat.com/app/uploads/2026/10/Screenshot-2026-10-22-at-10.33.33-1200x324.jpg)

Therefore, a 10-fold improvement in distance means the same whether it is from 5km to 500m or from 500km to 50km. You can compare both metrics [here](https://public.flourish.studio/visualisation/30578383/).

Below are the model results sorted by either metric, showing how many photos each model geolocated within distance bands from the true location.

![chart visualization](https://public.flourish.studio/visualisation/30555559/thumbnail)

Several models placed at least 10 out of the 52 photos correctly within one kilometre, and the top-performing models placed over 50 percent of the photos within 25 kilometres.

*NOTE: Geoseer-fast refused to answer on four of the 52 photos, claiming “This image is not suitable for geolocation”, while Mistral-large-4 refused once with “insufficient information in image to identify location”. Kimi-k2.6 also failed to provide a set of coordinates on one photo, and Gemini 4 Argon timed out repeatedly on one photo.*

## Our Test

To independently assess the models, we sought to give them very specific instructions and some images that were harder to geolocate than those provided in our past tests. The prompt asked fo...