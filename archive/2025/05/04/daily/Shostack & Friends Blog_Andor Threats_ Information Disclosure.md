---
title: Andor Threats: Information Disclosure
url: https://shostack.org/blog/andor-threats-information-disclosure/
source: Shostack & Friends Blog
date: 2025-05-04
fetch_date: 2025-10-06T22:27:44.133841
---

# Andor Threats: Information Disclosure

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Andor Threats: Information Disclosure

Shostack + Friends Blog

# Andor Threats: Information Disclosure

What Andor can teach us about Information disclosure threats
![A screencapture showing the radio](/images/blog/img/2025/andor-radio-960w.png)

I’m really excited about the second season of Andor, mostly for the
amazing storytelling about a rebellion, and I’m enjoying the tech
and the threats, too. (This post has no real spoilers, and doesn’t link to
anything spoilery.)

A minor plot points revolves around [Luthen Rael](https://starwars.fandom.com/wiki/Luthen_Rael) and [Kleya Marki](https://starwars.fandom.com/wiki/Kleya_Marki) traveling, and
they can’t use the radio because of the risk of getting
caught.

Many people think about *information disclosure* threats as
being about the content of communication, but they also apply to
the existence of communication. It’s nice to see that portrayed on
Andor, and I’ll say more about it further down the post, after I
finish geeking out over the details. It’s even nicer to see some of the little details they’ve
snuck in, like the plugboard and the request for a weather report.

When I first saw the radio, I thought it took a lot of elements
from the Enigma machines, but examining it more closely (S2E3 15:50 or so), I think I may have just
imagined that. And Starwars.com [says](https://www.starwars.com/news/andor-trivia-guide-week-1) it was partially inspired by a
telephone operator’s keyboard. Regardless, it’s unlikely that the request for a weather report was an
accident. Weather tied into security in all sorts of ways in the
Second World War. The British captured German weather boats to
steal their Enigma machines. They also used weather reports on the
BBC to carry secret messages, using certain words to
signal in various ways.

Coming back to information disclosure and secrecy, information
disclosure is a key threat to a rebellion, and there’s a variety
of ways you can address them, ranging from having messages like
“asking for a weather report” which have layered meaning to having
messages which are hard to detect because your radios are
“fractal,” which might be an allusion to frequency hopping, or
your messages could be encrypted. If your messages are hard to
detect, they are hard to pick out because there’s lots of cover
traffic (such as on a capital planet). But if there’s not a lot of
radio traffic, they’ll be easier to see.

It seems like a good idea to encrypt everything. But when
encryption is rare, it calls attention to itself. And if you call
attention to your messages, eventually, the Empire will find your radios, possibly
find the keys, and decrypt all your messages.
(There’s no public key cryptography
in Star Wars, not because they couldn’t invent it, but because it’s
bad for the plot.) When you’re engaged
in a revolution may be one of those times when it makes sense to
think carefully about your adversary. After all, we know that the
threat is the Imperial Security Bureau.

So the rebellion is compartmentalized. We see Luther meeting with
various factions, some of whom fail
despite his best efforts, and others who he allows to fail. Hmmm,
maybe we had too limited an understanding of the adversary. So
maybe it doesn’t make sense to focus on the adversary, as tempting
as it can seem.

Right now it seems that without
Luthen and Kleya the factions are completely separated, making
Luthen and Kleya single points of failure, which I expect will be part of next
week’s episodes. And speaking of next week’s episodes: You have until
Episode 9 of Andor drops to get one fourth off our self pace
courses. (Details on our Star Wars day sale are [here](https://shostack.org/blog/the-empires-threat-modeling/).)

Originally published by Adam on 03 May 2025

Categories:
  [threat modeling](/blog/category/threat-modeling)
  [star wars](/blog/category/star-wars)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read/).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact/) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2025/appsec-roundup-aug-2025-175w.png)](/blog/appsec-roundup-sept-2025/)

### [Secure By Design roundup - September 2025](/blog/appsec-roundup-sept-2025/)

01 Oct 2025

The secret service, the CSRB, the CMMC, Sept was pretty busy in government. Plus Apple's Memory Integrity and a nice short paper on prompt-based attacks.

[![Thumbnail for podcast episode](/images/blog/img/2025/medtech-innovation-podcast-175w.png)](/blog/medtech-innovation-podcast/)

### [Adam Featured on Inside MedTech Innovation](/blog/medtech-innovation-podcast/)

29 Sep 2025

Learn from the past and advance your threat modeling skills!

[![A moon buggy model at the Museum of Flight](/images/blog/img/2025/moon-buggy-museum-of-flight-175w.png)](/blog/lunar-rover-vehicle-redux/)

### [Lunar Rover Vehicle, Redux](/blog/lunar-rover-vehicle-redux/)

17 Sep 2025

What can the moon buggy teach us about modeling?

[![Astronaut Jim Irwin in front of Apollo 15 and a moon rover](/images/blog/img/2025/as15-88-11866-signed-175w.jpeg)](/blog/apollo-15-lrv-boeing/)

### [Apollo 15 Lunar Rover Vehicle](/blog/apollo-15-lrv-boeing/)

15 Sep 2025

What can a signed Apollo 15 print teach us about modern threat modeling and risk management?

## Popular Blog Topics

[Threat Model Thursday](/blog/category/threat-model-thursday/),
exploring specific published threat models

[Threat Modeling](/blog/category/threat-modeling/) (general topic)

[Application Security](/blog/category/application-security/)

[Software Engineering](/blog/category/software-engineering/)

[Cloud Security](/blog/category/cloud-security/)

[Compliance](/blog/category/compliance/)

[AI](/blog/category/ai/) + [ChatGPT](/blog/category/chatgpt/)

[Privacy](/blog/category/privacy/) + [Personal Security](/blog/category/personal-security/)

[Research](/blog/category/research-papers/) + [Reports](/blog/category/reports-and-data/)

[Book Reviews](/blog/category/book-reviews/)

[News](/blog/category/news/)

[Podcasts](/blog/category/pod...