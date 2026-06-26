---
title: How to Use AI to Help Find Civilian Harm
url: https://www.bellingcat.com/resources/2026/06/25/how-to-use-ai-to-help-find-civilian-harm-conflict-report-monitor-war-machine-learning-telegram/
source: bellingcat
date: 2026-06-25
fetch_date: 2026-06-26T06:09:42.571032
---

# How to Use AI to Help Find Civilian Harm

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

[![Profile picture for: Miguel Ramalho](https://www.bellingcat.com/app/uploads/2023/03/Miguel-1200x1200.jpg)](https://www.bellingcat.com/author/miguelramalho/)
[Miguel Ramalho](https://www.bellingcat.com/author/miguelramalho/)

Miguel is an Investigative Technologist for Bellingcat. He uses data and code to investigate and communicate stories, he experiments and builds research tools with and for the online investigations community.

[![Profile picture for: Nick Waters](https://www.bellingcat.com/app/uploads/2023/10/DSCF1052-scaled.jpg)](https://www.bellingcat.com/author/nick-waters/)
[Nick Waters](https://www.bellingcat.com/author/nick-waters/)

Nick is an expert who specialises in the examination of conflict using online open source information, including as evidence in justice and accountability processes. He began contributing to Bellingcat in May 2016 and was a staff member from May 2019 to March 2025. His previous work has focused on the use of chemical weapons in Syria, violence against migrants on the borders of the EU and civilian harm during Russia’s full scale invasion of Ukraine.

# How to Use AI to Help Find Civilian Harm

June 25, 2026

* [AI](/tag/ai)
* [Civilian Harm](/tag/civilian-harm)
* [Ukraine](/tag/ukraine)

Between February 2022 and September 2025, Bellingcat staff and volunteers collected, geolocated, and [shared more than 2,500 incidents](https://ukraine.bellingcat.com/) of civilian harm following Russia’s full-scale invasion of Ukraine.

As part of this effort, Bellingcat tested a new machine learning model intended to rank Telegram social media posts on their likelihood of containing incidents of civilian harm.

This novel methodology dramatically reduced the search and selection time required, freeing researchers to focus on verifying incidents of civilian harm – not just searching for them.

This piece documents our methodology, ethical considerations and lessons learned in the hope that others researching similar topics can benefit from our work.

Open source research into civilian harm is still a relatively new field and it presents many challenges – one of the biggest is organising and sorting through the huge volume of user generated content being produced to find what is relevant.

Machine learning, a form of artificial intelligence that uses algorithms to identify patterns from large amounts of data and make predictions, can make this task more efficient.

With ongoing conflicts involving large amounts of civilian harm occurring in Sudan, and much of the Middle East, this guide aims to offer those covering these conflicts an example of how machine learning can be used to help find and sort incidents. You can also access the [Code Notebook](https://www.bellingcat.com/resources/2024/03/06/how-code-notebooks-enable-open-source-research/) for our model [here](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/2026/resources/civilian-harm-detector/replicate_training.ipynb).

We defined “civilian harm” not just as civilian deaths or injuries resulting from armed conflict, but also the broader and delayed effects on civilians from mental trauma, loss of livelihood, displacement, destruction of infrastructure and more. This definition was informed by the Protection of Civilians [book](https://protectionofcivilians.org/on-civilian-harm/) [on civilian harm](https://www.interaction.org/blog/toward-a-shared-understanding-of-civilian-harm/).

## Initial Telegram Dataset

Each Telegram post containing civilian harm which had already been manually verified by researchers was used to build an initial dataset of confirmed cases of civilian harm, which data scientists call *positive instances*. We collected a total of 5,848 unique URLs for these Telegram posts. For our manual collection we reviewed posts on relevant Telegram channels, working through oldest to newest posts each day. Assuming that a given post made it to our geolocated incidents list, it meant the researcher who flagged it also looked at the posts that appeared before and after it on Telegram and did not flag those ones, so we selected the 10 posts surrounding the verified civilian harm post as our additional dataset of posts that did not contain civilian harm. After excluding any deleted or duplicate posts, we ended up with 48,545 non-civilian harm posts, our *negative instances*.

The choice to overrepresent negative instances aims at better reflecting the real world and increasing data available for model training.

We enriched each URL with metadata from the Telegram API, such as the time of publication, reactions or textual content. As some of these posts had been deleted, we completed the missing data points with previously preserved versions from our [Auto Archiver](https://www.bellingcat.com/resources/2025/08/13/the-open-source-tool-that-has-preserved-150000-pieces-of-online-evidence/) database, only available for the positive instances.

## Feature Engineering

Training a machine learning model requires numerical data, as these models compute a prediction score based on mathematical operations.

We built these by converting raw data from our initial dataset, such as keywords signalling potential civilian harm, into numerical scores (or “features”) that the model could interpret, with the aim of increasing the model’s ability to identify patterns. This process, known as [feature engineering](https://www.ibm.com/think/topics/feature-engineering), can significantly improve model results because it allows data scientists to suggest explicit context knowledge.

A full list of features we used to train the model can be found in the [code notebook](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/2026/resources/civilian-harm-detector/replicate_training.ipynb) accompanying this piece. Many features were directly inspired by researchers’ input from their experiences manually screening cases of civilian harm by sorting through a set number of Telegram channels and inspecting each post individually.

![](https://www.bellingcat.com/app/uploads/2026/06/civharm_image2-1200x684.jpg)

Several of the features used were directly built from the metadata contained in each Telegram post including *media\_type*, *day\_of\_week*; or binary ones: *forwarded*, *edited and* *reply\_to*.

Other features included engagement information: *views*, *forwards*, *total\_reactions*, and even individual features for most used emojis including the *reaction\_crying\_face* to count 😭 emoji.

## Converting Text to Numbers

To embed the experience from the manual collection process, researchers put together a list of keywords both in Ukrainian and Russian that, to them, signalled posts likely to  show civilian harm. For instance, “Шахед” and “КАБ” translated to “Shahed” and “Guided aerial bomb” respectively. We created a numerical feature to count their frequency.

In addition, we included several generic English-language keywords which meaningfully signalled potential civilian harm, such as “injured”, “school affected” and “hospital affected” that were only used for generating semantic similarity scores.

A semantic similarity score is a calculation used to determine the proximity in meaning between different words and phrases. To get th...