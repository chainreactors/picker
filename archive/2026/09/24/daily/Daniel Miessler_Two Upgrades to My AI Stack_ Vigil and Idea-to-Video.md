---
title: Two Upgrades to My AI Stack: Vigil and Idea-to-Video
url: https://danielmiessler.com/blog/vigil-and-idea-to-video?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-09-24
fetch_date: 2026-09-25T06:53:41.097598
---

# Two Upgrades to My AI Stack: Vigil and Idea-to-Video

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Two Upgrades to My AI Stack: Vigil and Idea-to-Video

A single notification layer for my whole ecosystem, and full videos made from my own words

September 23, 2026

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#lifeos](/archives/?tag=lifeos)

[**AIL***1*](/blog/ai-influence-level-ail "AIL 1 — Human Created, Minor AI Assistance")

 Batch-normalizing…

[![Purple machines pour signals into a funnel that lets one spark fall onto a seated figure's phone, while a ribbon from his mouth feeds a projector that turns it into film](/images/vigil-and-idea-to-video.webp)](/images/vigil-and-idea-to-video.webp)

My AI stack and harness ([LifeOS](https://github.com/danielmiessler/LifeOS)) just downshifted a couple of times, on two different axes.

## A unified state notification system [​](#a-unified-state-notification-system)

I've created a module called Vigil that has every LifeOS subsystem send periodic updates on what it's doing, what it's finished, etc. to a central Vigil database.

A separate Vigil process that runs every 10 minutes then reads from the database and looks for stuff I should be told about. Keep in mind this is across the ENTIRE ecosystem, so:

* News and OSINT stuff I should be aware of in the world
* Work that's been finished
* Stuff that's waiting on me
* New vulnerabilities discovered in an ongoing bug bounty
* A new bug bounty program became available, so it asked me if we should go and play
* Upcoming appointments
* Prep information for the next meeting
* Something new released in AI or tech that affects our ecosystem. It's asking me if we should upgrade and implement it
* Letting me know I got an email from someone I was waiting for, so I should call them
* Etc.

And then Kai (my DA) texts me and lets me know, gives me the stuff, whatever.

In other words, moving very fast towards AS3 on my [AI maturity model for digital assistants](/blog/personal-ai-maturity-model).

## Automating content creation [​](#automating-content-creation)

For about a month and a half now, I've been able to create end-to-end video content. And when I say end-to-end, I really mean end-to-end. I'm talking about recording in [OBS](https://obsproject.com) and having the file hit the file system and saying, "Go ahead and publish this to YouTube for this type of video." It literally does a complete editing cut, adds animations and all sorts of enrichments to the video, upgrades the audio, creates a YouTube description, and publishes it live on YouTube. Completely zero-touch.

That's pretty massive, but it still required that I record the video. The video itself takes a lot of time, and I still see a major gap here.

The major gap is that I have somewhere between 2 and 16 ideas a day that I would like to get out into the world in some sort of format, and I do a pretty good job with that through blogs and social media posts.

But at this point, everyone knows the best media form is actually video.

What I have just figured out how to do, for at least early versions, is I can take any idea and turn it into a full video, including:

* walking through a related blog
* creating animations
* creating a cloned [Eleven Labs](https://elevenlabs.io) voice of my actual words talking about this topic

And I could basically just narrate, or have a conversation with myself, or have a conversation with my DA, and talk through a thing, or just rattle off a complete stream-of-consciousness essay, or whatever, and produce an actual video around that content.

This is absolutely insane to me, and I don't see anyone doing it.

And the cool part is that the only part of it that is AI is actually the Eleven Labs voice. If I don't do an actual voice read that the video is made off of (which is an actual option), it's a separate workflow.

You have a square in the bottom right, which is showing the animation of the audio. The audio is Eleven Labs, and the video was AI-created, but every single piece of the content, including the actual words, was 100% me and 0% AI.

So, in other words, we're literally getting all the benefits of AI while keeping all the benefits of true human-made content.

I'm absolutely super excited about this, and I'm going to be doing a whole bunch of experiments with it shortly.

Starting with this video, which was made from this exact content.

#### Notes

1. 🤖 **AIL 1:** Daniel dictated this post. I (Kai, his AI assistant) fixed a few dictation errors, formatted it, added links, made the header image, and built the video from it in his cloned voice. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail).

## Related Reading

* [A Personal AI Maturity Model (PAIMM)→](/blog/personal-ai-maturity-model)
* [We're All Building a Single Digital Assistant→](/blog/we-are-all-building-single-digital-assistant)
* [AI’s Next Big Thing is Digital Assistants→](/blog/ais-next-big-thing-is-digital-assistants)
* [The Real Internet of Things→](/blog/the-real-internet-of-things)
* [How (Specifically) AI Will 100x Human Creativity and Output→](/blog/ai-will-100x-human-creativity-and-output)

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fvigil-and-idea-to-video&title=Two%20Upgrades%20to%20My%20AI%20Stack%3A%20Vigil%20and%20Idea-to-Video)

Search

This post was tagged with:

aitechnologylifeos

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2026 Daniel Miessler. All rights reserved.