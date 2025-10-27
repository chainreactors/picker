---
title: Weekly Retro 2025-W14
url: https://0xda.de/blog/2025/04/weekly-retro-2025-w14/
source: Blogs  dade
date: 2025-04-07
fetch_date: 2025-10-06T22:03:53.161413
---

# Weekly Retro 2025-W14

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/04/weekly-retro-2025-w14/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

5 minutes

# [Weekly Retro 2025-W14](https://0xda.de/blog/2025/04/weekly-retro-2025-w14/)

---

* [Protocol & Projects](#protocol--projects)
* [Website improvements](#website-improvements)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

Refocusing my priorities, and a handful of improvements to my website, including a share button and a js-free collapsible menu.

## Protocol & Projects

There was no new [Protocol](https://www.youtube.com/playlist?list=PL7-g2-mnZwSF7uNEzb05BBxeaTYPvcglS) episode this week. There will be no new Protocol episode next week. The amount of work that goes into making scripted YouTube videos is deceptively high. While I very much had fun making them, and I still love the idea for the series, it’s simply not tenable for me to write, record, and edit 4 videos a month and still have time for other projects.

I’ve been quite busy with my day job the past 2-3 weeks, and I am taking on more critical projects at work that are likely to keep the level of activity pretty high for a while. On top of this, I was trying to research, write, record, and edit my YouTube series, making animations and everything. I have also been working on an album, and working on a SaaS product for Internet security research.

Unfortunately, I found myself having to spend all of my free time forcing myself to work on Protocol. Despite loving the idea, and really wanting to make it, it felt like a chore that left no time for any other things I wanted to do. I could get an editor, or get someone to help with research. But my best video barely did 100 views, I’m not ready to start paying a team for the project yet. I do hope I can do that in the future, but at the moment it’s just not viable.

Instead, I am giving myself time back to work on other things that I want to work on. Writing music, working on my little slice of the internet, and building software.

Should I find myself working full time on my own projects, I hope to pick Protocol back up. I legitimately have over 200 video ideas I want to make. But to execute them to the standards I set for myself requires more time than my full time job + other hobbies currently allow.

## Website improvements

I didn’t really mean to spend several hours working on improvements for my website over the last couple days, but I saw an article about the web share API and I wanted to add a native share button to my posts (which I did, you can see it down below!)

I wrote yesterday about [hiding elements that require JavaScript without needing JavaScript](https://0xda.de/blog/2025/04/hiding-elements-that-require-javascript-without-javascript/). It’s basically just a clever (in my opinion) use of a utility class and a bit of `<noscript>`. Turns out [someone posted me on HN](https://news.ycombinator.com/item?id=43602688), so that’s cool. I went and checked out some of the conversation and it is exactly as I expected it to be. A few very vocal people saying it’s dumb to bother not supporting JavaScript, and some other people talking about prior art in the space or talking about alternative ways to accomplish it. One person even mentioned that [there’s a CSS media query for whether scripting is available or not](https://news.ycombinator.com/item?id=43603120), which I find fun and frustrating, because I literally googled whether I could solve the problem with a media query or not lol. But it does exist!

Today I was trying out some of the ways my site responds to various NoScript extension configurations, and realized that my menu got a little jank. It relied on javascript to collapse when on mobile, and just rendered over content when JS was disabled on mobile. In an effort to fix it, I accidentally made it so that the menu doesn’t show up at all on mobile devices without JS. No good deed, etc.

But this reminded me that in another project, I had built a JS-less collapsible menu through creative use of CSS selectors and an `<input>` checkbox. So I just ripped out the JS-requiring menu and replaced it with the CSS+input powered collapsible menu. Works just the same, except now with 100% less JavaScript.

So the only features that actually need JavaScript on my site now are:

* The Share button (replaced with just an easy-to-select link when not available)
* The theme switcher (uses system preference when JS is not available)
* The
  `ctrl`+`k`
  search (sorry, no way to use this one without JS, I’m not going to run a search backend for my personal website)
* The annoying background fill (which is just not done when JS isn’t available, which one could argue makes the experience better)
* My self-hosted [Plausible Analytics](https://plausible.0xda.de/0xda.de) (which I’m A-okay not getting analytics from you if you don’t want me to have them)

## Interesting Links

* [Why I Maintain a 17 Year Old Thinkpad](https://pilledtexts.com/why-i-use-a-17-year-old-thinkpad/) - I have an old ThinkPad sitting on the shelf next to me. I don’t maintain it anymore, but it absolutely still fires up and I’m sure I could use it if I wanted to. I think mine is only 12 or 13 years old, though.
* [Hacking the Call Records of Millions of Americans](https://evanconnelly.github.io/post/hacking-call-records/) - Isn’t it so neat how many people have our data, even if we’ve never heard of them? Neat.
* [Losing our taste](https://jamie.ideasasylum.com/2025/03/31/losing-our-taste) - An interesting article about the potential future impacts of the proliferation of AI. I use ChatGPT from time to time, but I don’t think AI is going to take my job, and I don’t think AI is going to produce art. A facade of what art once was, maybe. This author discusses it through the lens of taste, but I have found myself thinking about it through the lens of soul.

## Upcoming Projects

* [Defcon Call for Music/Tracks](https://defconmusic.org/def-con-33-call-for-music-tracks/) - Okay this week I’m filling out the call for artists for the live performances. I still have an extra month for the soundtrack, which is good because at this rate I’m going to need it.
* **I want to do more live shows at hacker cons.** I’ll do it for the cost of getting to the con and the hotel room. If you, or someone you know, is organizing hacker cons and wants some new live nerdy rap shows, [please reach out via any of the platforms on my page](https://0xda.de/).

---

Share this page

`https://0xda.de/blog/2025/04/weekly-retro-2025-w14/`

[weekly retro](https://0xda.de/tags/weekly-retro)

1014 Words

Date Published

2025-04-06 20:15 +0000

9d15104 @ 2025-04-06

---

[â
Weekly Retro 2025-W15](https://0xda.de/blog/2025/04/weekly-retro-2025-w15/)

[Hiding elements that require JavaScript without JavaScript
â](https://0xda.de/blog/2025/04/hiding-elements-that-require-javascript-without-javascript/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2025
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/04/weekly-retro-2025-w14/ "Tor")
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[Rss](https://0xda.de/blog/index.xml "RSS")
[JSON Feed](https://0xda.de/blog/index.js...