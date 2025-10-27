---
title: Weekly Retro 2025-W05
url: https://0xda.de/blog/2025/02/weekly-retro-2025-w05/
source: Blogs  dade
date: 2025-02-03
fetch_date: 2025-10-06T20:35:25.551951
---

# Weekly Retro 2025-W05

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/02/weekly-retro-2025-w05/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

4 minutes

# [Weekly Retro 2025-W05](https://0xda.de/blog/2025/02/weekly-retro-2025-w05/)

---

* [Natlas & Tailwind](#natlas--tailwind)
  + [Before Tailwind](#before-tailwind)
  + [After Tailwind](#after-tailwind)
* [PROTOCOL](#protocol)
* [Consulting Update](#consulting-update)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

## Natlas & Tailwind

I managed to complete the [transition to tailwind](https://github.com/natlas/natlas/pull/1258) for natlas finally. I made heavy use of LLMs to help translate bootstrap classes and paradigms over to [tailwind](https://tailwindcss.com/) and [Alpine.js](https://alpinejs.dev/). It’s definitely not the cleanest, but it is a whole new look, and it helps readjust the application towards a [locality of behavior](https://htmx.org/essays/locality-of-behaviour/) focus.

This change further cements the lack of backwards compatibility in the new natlas code, as I previously versioned each piece of data based on the application version that produced it, even if there were little or no changes to the data itself. This meant that I had a ton of duplicate html to render said data of various application versions. But since I know I’m redoing that whole concept, I ripped out all the old versions and only kept the latest version, which I updated to tailwind styles.

I am considering two directions for the next set of tasks I’m going to focus on with Natlas. First, I may work on the elastic data model and replace it with the [elasticsearch-dsl-py](https://github.com/elastic/elasticsearch-dsl-py), which lets me model my elastic documents as python objects. This *needs* to happen, but it feels big and so I am a little worried about it. The other direction is to spend more time working on some of the interactivity, introducing either [htmx](https://htmx.org/) or [unpoly](https://unpoly.com/) to give nice dynamic behavior but with server-side control. I want to minimize the amount of javascript logic and/or data handling I have to write, including advanced alpine logic. This will mean rewriting a bunch of routes I already have, writing new routes to handle new more specific behaviors, etc.

I’ll also caveat that I didn’t spend a ton of time trying to actually change how natlas looks to give it a more modern feel. The tailwind transformation was just to set the project up for a position in the future where that will be easier. So a lot of things look pretty similar, and I’ll work on improving things slowly over time as I tackle the tech debt.

### Before Tailwind

![Natlas before the tailwind transition](https://0xda.de/blog/2025/02/weekly-retro-2025-w05/natlas-pre-tailwind.4702fd8363e7baad59e77789625fef1e.png)

### After Tailwind

![Natlas after the tailwind transition](https://0xda.de/blog/2025/02/weekly-retro-2025-w05/natlas-post-tailwind.1c6d4817fa6d4d6770b8bdd4ad1d83ab.png)

## PROTOCOL

![PROTOCOL Episode 1 Thumbnail - What is a Protocol?](https://0xda.de/blog/2025/02/weekly-retro-2025-w05/p001-thumbnail.d97e175ba3cff2dcbb7ece0c48a59f54.png)

I spent several hours this week working to prepare my new video series, PROTOCOL, for launch. I still have more work to go, and I guess that will always be true since I want to release videos weekly. But the first episode is ready to go and will be releasing this week. It’ll launch on my youtube channel, [0xdade](https://www.youtube.com/0xdade), so if you’re interested in the series and want to learn more about it, I recommend subscribing. But if you don’t want to make that commitment yet, I understand. Instead, let me give you an elevator pitch.

Protocols play a fundamental role in how we communicate digitally (protocols even play fundamental roles in non-digital things too!). PROTOCOL is a weekly video series that provides a look into what protocols are, how they work, and how they come to be. PROTOCOL videos aim to be between 5-10 minutes long with a pretty fast pace, focusing on “evergreen” content rather than chasing the news. It’s the video series I wish I had when I was getting into tech, development, and hacking.

## Consulting Update

I had my first actual sales call for my company, [Room 641A](https://room641a.com), this week. No more details or anything, but I was very excited to get my first actual interest. I’ve done several other jobs already under the company, but they were via a channel that I already had established and didn’t have to setup myself. So I’m celebrating a little bit, even though nothing is closed, I’m still happy to have made that step.

## Interesting Links

* [Core vs Context](https://medium.com/a-technical-leaders-toolbox/core-vs-context-3da8309cc71b) - A simple framework for determining what to work on, core is that which is a competitive advantage or key value for the product, context is necessary work but not necessarily work for *you* to spend time on.
* [An Investigation Into Nachash](https://nacha.sh/) - I found this post to be an interesting demonstration of open source intelligence gathering, and also a prime example of neglecting critical information when connecting dots. I highly doubt the mysterious darknet figure who created doxbin and managed to hide their identity for over a decade and counting was 13 when they started. Too easy to make mistakes at that age unless your parents were training you to be a spy since you were in diapers, imo.

## Upcoming Projects

* [PROTOCOL - What Is a Protocol?](https://www.youtube.com/0xdade) - Subscribe to see the latest episode when it goes live later this week.

---

Share this page

`https://0xda.de/blog/2025/02/weekly-retro-2025-w05/`

[weekly retro](https://0xda.de/tags/weekly-retro)[natlas](https://0xda.de/tags/natlas)

749 Words

Date Published

2025-02-02 20:49 +0000

d298235 @ 2025-02-23

---

[â
Weekly Retro 2025-W06](https://0xda.de/blog/2025/02/weekly-retro-2025-w06/)

[Lessons in Everything
â](https://0xda.de/blog/2025/01/lessons-in-everything/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2025
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/02/weekly-retro-2025-w05/ "Tor")
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[Rss](https://0xda.de/blog/index.xml "RSS")
[JSON Feed](https://0xda.de/blog/index.json "JSON Feed")