---
title: Weekly Retro 2025-W02
url: https://0xda.de/blog/2025/01/weekly-retro-2025-w02/
source: Blogs  dade
date: 2025-01-15
fetch_date: 2025-10-06T20:09:37.060554
---

# Weekly Retro 2025-W02

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/01/weekly-retro-2025-w02/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

6 minutes

# [Weekly Retro 2025-W02](https://0xda.de/blog/2025/01/weekly-retro-2025-w02/)

---

* [Shmoocon 2025](#shmoocon-2025)
* [Natlas Improvements](#natlas-improvements)
* [Protocol](#protocol)
* [Wrapping Up](#wrapping-up)

---

Iâm publishing a bit late because we were at the final Shmoocon over the weekend. In fact Iâm writing this on my phone from the plane home right now.

## Shmoocon 2025

Iâve always enjoyed Shmoocon for probably the past 8 or 9 years that Iâve been going (whenever I was lucky enough to secure a ticket). But even without a ticket, Iâve held that Shmoocon is probably one of the best âlobby conâ conferences - you could show up, spend the whole weekend in the lobby of the hotel, and have an incredible time. In fact many people did just that this year to honor the final Shmoocon.

I saw several talks and even made an effort to take notes about each talk I saw, which I havenât done since I worked for Intel and had to write a report about the conferences I went to. This time it was just for me, and I really enjoyed it. My favorite talk was â[Pages From a Sword-Makers Notebook pt3](https://youtu.be/yIutY_X2FcU?t=380)â by Vyrus, in which he spoke about finding out that some software he wrote was being abused by threat actors, so he intentionally introduced a bunch of data collection into the build process and embedded the data into the binary. Once someone ran the build, it would collect a ton of system info, username, environment variables, external IP addresses, etc, and even a screenshot of the desktop, and then encrypt and embed those into the resulting binary. That way whenever they turned up in VirusTotal, he could decrypt the data, which he then showed us live during the talk. It was very entertaining, and there are not many times youâll get to hear from someone as talented as Vyrus telling these types of stories.

I also really enjoyed Russ talking about his [deception operation](https://youtu.be/yIutY_X2FcU?t=16402) to dissuade trespassers from his new property. I donât want to spoil the story, but it was a fantastic talk in the spirit of hacking but without just being a talk about policy or a talk about deep technical topics. Iâve already sent links to the talk to several people who otherwise probably wouldnât watch hacker con talks because I liked it so much.

## Natlas Improvements

As Iâve mentioned in my previous retro, Iâve really gotten back into working on [Natlas](https://github.com/natlas/natlas). I think I found a clear direction I wanted to take it, so Iâm working to simplify around those core ideas. Iâve mostly completed the necessary steps to ensure accurate type annotations in the code base, so development sucks way less now. The part that still sucks is just digging through some of my abominations, especially around the agent request/response cycle. But my next step is probably to formalize the elasticsearch data model with [elasticsearch-dsl-py](https://github.com/elastic/elasticsearch-dsl-py), then Iâll start to tackle some of the unnecessary complexities Iâve left myself.

One future project Iâm looking forward to is expanding Natlas into being a DNS-aware collection platform. I’ve long been interested in DNS-related research, and have collected a lot of data over the years. The thing Iâm most worried about, though, is being able to keep up with the data. I think most use cases will be simpler than what I have in mind, where you might load up dns names for your company and use that to help inform scope for scanning, help inform on changes, etc. But I want to ingest and interrogate whole TLD zone files, watching for new suspicious domains, catching changes to domains/subdomains as they happen, etc.

I know there are many tools out there that do similar things, both open source and commercial, but sometimes the best way to understand it is to build it yourself, you know? At least for me thatâs the case. Letâs see if I can get TLD managers in CZDS to agree.

## Protocol

Iâve had this idea for over a year, I teased it a few times in the past year, and Iâm finally working to make it happen. I am working on a video series called Protocol that spans various topics around protocols of all types, standards bodies, etc. Iâm planning to release the first episode in February and try to keep up with a weekly cadence after that. I have a ton of topic ideas to dig into, including a bunch of introductory level videos for different common (and uncommon, and some downright archaic) protocols, as well as videos that dive deeper into specific parts of protocols.

I feel like this is content that I would have liked to see when I was getting into hacking. In fact I was inspired by some old Hak5 videos that explained SSH tunnels on a whiteboard tabletop. I wanted to expand that idea much further, and so my video topic sheet has grown to hundreds of topics and Iâve not yet created a video. I decided this year I was going to stop letting my perfectionism get the best of me, and just do it.

Additionally Iâm going to be trying to take some inspiration from other YouTubers Iâve watched and enjoyed, and Iâm going to try to publish the script for each talk, and hopefully build it up into a cross-referential resource. This might be a bit weird since itâll be the scripts as I wrote them, not necessarily as they appear in the video, and not necessarily how you would expect to read technical content. But it also means youâll effectively be able to ctrl-f through all of my videos, which Iâve long held is a frustrating part of the tech industry - so much interesting and valuable content is hard to find when youâre looking for it because itâs locked up in conference talks, podcasts, etc. I love watching videos and listening to podcasts as much as the next highly ADHD, mildly autistic person does, but it basically makes attributing prior research impossible.

So anyways, stay tuned for Protocol. Hopefully coming soon to a YouTube channel near you.

## Wrapping Up

I forgot that I have a mailing list, Iâm working on improving it and then Iâm going to start including a signup form more regularly on my posts. (Or maybe just a link to the signup form somewhere in a menu). My process for this has been interesting, and I canât wait to write about the absolutely insane pipeline Iâm concocting in order to send newsletters from my Hugo statically generated site with as little manual intervention as possible.

I also have a company, and funds are getting a little low. If youâd like me to come speak to your team or at your conference, help you with your security, help you hack the planet, or you want to start scanning the planet (or maybe just your internal network) and want some custom Natlas support, please reach out via [Room 641A](https://room641a.com).

---

Share this page

`https://0xda.de/blog/2025/01/weekly-retro-2025-w02/`

[weekly retro](https://0xda.de/tags/weekly-retro)[natlas](https://0xda.de/tags/natlas)

1134 Words

Date Published

2025-01-14 06:24 +0000

d298235 @ 2025-02-23

---

[â
Weekly Retro 2025-W03](https://0xda.de/blog/2025/01/weekly-retro-2025-w03/)

[Weekly Retro 2025-W01
â](https://0xda.de/blog/2025/01/weekly-retro-2025-w01/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influ...