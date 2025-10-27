---
title: Weekly Retro 2024-W38
url: https://0xda.de/blog/2024/09/weekly-retro-2024-w38/
source: Blogs  dade
date: 2024-09-24
fetch_date: 2025-10-06T18:25:07.832495
---

# Weekly Retro 2024-W38

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/09/weekly-retro-2024-w38/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

4 minutes

# [Weekly Retro 2024-W38](https://0xda.de/blog/2024/09/weekly-retro-2024-w38/)

---

* [Digital Gardening](#digital-gardening)
* [RIP Pixel 5a](#rip-pixel-5a)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

I am trying my hand at the digital garden, and I’m an iPhone user now, I guess.

## Digital Gardening

It’s been a while since I talked about this topic, but I’ve decided to try my hand at the [digital garden](https://0xda.de/garden/). I’ve added a new section of my site, `/garden/`, and added my first note on [API keys](https://0xda.de/garden/api-keys/).

The idea for this section of my site is that it is content that grows and evolves over time, as I have more ideas or learn more about a particular topic or concept. So it isn’t really meant to be a chronological log of writing, like the blog is.

Right now the style of the page is very similar to the blog index, but the garden is sorted by last modified, rather than by when it was authored. I do want to make style improvements here and make each item in the garden a little card that shows the maturity of the note as well as the authored/updated dates. That way when you land on `/garden/` you can see more useful information.

## RIP Pixel 5a

My Pixel 5a died yesterday. It had been acting a little strange for a while now, randomly freezing up and then the system UI restarting. I should have taken this signal and migrated my data to another phone, but I didn’t.

I was updating a note in Obsidian, went to gesture to switch apps, and it froze up. Eventually the screen turned off and wouldn’t turn back on. After a few hours of investigation and attempting everything I could about fast boot and recovery mode, adb debugging, etc, I learned that the device was in Qualcomm’s EDL mode, which was identifiable via the device showing up as `QUSB_BULK_CID` in Windows device manager.

Thankfully most of the data on my phone is just stuff that gets synced automatically, either to Google Photos, Google Drive, or Obsidian. But I did lose years of Signal history, most notably my chat history with Sienna. That is the part that bums me out the most.

Anyways, I bought an iPhone 16. I don’t know if I like it yet, but I have mostly settled into it and gotten my apps installed. My first impressions from this morning are:

* I’m tired of hitting “allow” after installing a handful of apps. This fatigue will probably be fine after I’ve settled in, but today it is annoying.
* I hate numbered notification dots. I need a system wide way to make this never happen. I’m okay with a notification dot on an app letting me know that it wants my attention, but knowing how many is stress-inducing and I hate it.
* I wish I didn’t have to switch layers on the keyboard app to access `.` and `,`.
* I like that when something wants access to my contacts, I can share a subset of contacts instead of my whole address book. That’s neat.

## Interesting Links

* [Accidentally becoming admins of a whole TLD](https://labs.watchtowr.com/we-spent-20-to-achieve-rce-and-accidentally-became-the-admins-of-mobi/) - A great write up on the surprising impacts of letting an old important domain expire.
* [A Veritasium Video on Phone System Security](https://www.youtube.com/watch?app=desktop&v=wVyu7NB7W6Y) - This was a good watch and gives a good primer on risks associated with our modern phone system, and why some of those risks just won’t go away.
* [An X thread on falling and rising pedestrian fatalities](https://x.com/JessieSingerNYC/status/1837156704338760009) - The image in the second tweet in the thread is particularly interesting to me, and I think also applies to security incidents. But this is overall a great thread on how a lot of little things add up to have big impact.
* [An insane browser bug in one of those upstart browsers, arc, caused by Firebase](https://kibty.town/blog/arc/)
* [The Promise and Peril of Covert Action](https://nationalinterest.org/feature/shadow-war-promise-and-peril-covert-action-212875) - An interesting piece on the implications of the explosive attacks targeting Hezbollah members through their electronics (pagers and radios)
* [Turning Everyday Gadgets into Bombs is a Bad Idea](https://www.bunniestudios.com/blog/2024/turning-everyday-gadgets-into-bombs-is-a-bad-idea/) - A great post on how one might have achieved the attack that led to hundreds of pagers blowing up simultaneously in Lebanon, why it’s never been difficult to do, and why it hasn’t really been done before.
* [An X thread on a crypto heist and the people behind it](https://x.com/zachxbt/status/1836752923830702392)
* [Using DTMF tones to trick an elevator into taking you to a floor you’re not authorized to go to](https://www.youtube.com/watch?v=1ym8WNvxxUk)
* [Vulnerabilities in Open Source C2 Frameworks](https://blog.includesecurity.com/2024/09/vulnerabilities-in-open-source-c2-frameworks/) - A good post on vulnerabilities in various open source C2 frameworks. I think this is a good area of research and people should be doing more of it. It certainly inspired me.
* [The importance of link text](https://geektrainer.dev/code/link-text/) - A useful post about the importance of what text we choose to hyperlink. I’m going to try to be better about this and not just hyperlink “here” and “See more” and stuff like that.

## Upcoming Projects

* A conference that wishes to remain nameless currently has it’s CFP open. I have started putting together my application but have to decide which of my brainstormed topics I’m going to submit. (Due: 2024-10-01)

---

Share this page

`https://0xda.de/blog/2024/09/weekly-retro-2024-w38/`

[weekly retro](https://0xda.de/tags/weekly-retro)

833 Words

Date Published

2024-09-23 18:19 +0000

6357dfd @ 2024-09-23

---

[â
MFA and your Password Manager](https://0xda.de/blog/2024/09/mfa-and-your-password-manager/)

[Weekly Retro 2024-W37
â](https://0xda.de/blog/2024/09/weekly-retro-2024-w37/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2025
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/09/weekly-retro-2024-w38/ "Tor")
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[Rss](https://0xda.de/blog/index.xml "RSS")
[JSON Feed](https://0xda.de/blog/index.json "JSON Feed")