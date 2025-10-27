---
title: Lunar Rover Vehicle, Redux
url: https://shostack.org/blog/lunar-rover-vehicle-redux/
source: Shostack & Friends Blog
date: 2025-09-18
fetch_date: 2025-10-02T20:18:09.117351
---

# Lunar Rover Vehicle, Redux

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
3. Lunar Rover Vehicle, Redux

Shostack + Friends Blog

# Lunar Rover Vehicle, Redux

What can the moon buggy teach us about modeling?
![A moon buggy model at the Museum of Flight](/images/blog/img/2025/moon-buggy-museum-of-flight-1000w.png)

While I'm [talking about the Lunar Rover](https://shostack.org/blog/apollo-15-lrv-boeing/), I want to tell a tale of
two models. One you've met: the Lego model. The other is a
[model](https://www.museumofflight.org/exhibits-and-events/spacecraft/boeing-lunar-roving-vehicle-engineering-mock), currently
on display at the Museum of Flight in Seattle. (The Museum has a [longer
blog post](https://blog.museumofflight.org/the-legacy-of-the-lunar-rover) that implies the one on display is a training mock
up.) The two models could barely
be more different: One weighs a few pounds and can be held in your
hands. The other probably weighs a few hundred. One is very high
fidelity, the other quite low. One you can play with... the other
one I didn’t check, but there *is* a fence around it.

When we say “All models are wrong, and some models are useful,” we
have to understand the goals of a model. One of these was used to
plan a moon mission, the other is mostly fun, and also
educational. (For example, the Lego model has stickers marked “wax”,
because you can’t use oil as a lubricant in a vacuum. The liquid
evaporates, and you probably don’t want to be spraying graphite
around and contaminating samples.)

Being explicit about the goals of a model means you can tune your
engineering work to maximize the return on investment. Even when the
goal is “analyze this system,” or “get everyone to understand the
design,” being explicit can let you loop back to that goal to
assess if you’re spending the right amount of work.

![A close up of the console](/images/blog/img/2025/moon-buggy-console-500w.png)

One weighty goal that’s quite hard to balance with other goals is that the
model accurately account for gravity off Earth. For space, NASA has
the Neutral Buoyancy Lab. There are Mars Rover models that only
simulate the weight of a rover on Mars. That is, they’re tuned for
that purpose and nothing else. In the case of the moon buggies,
designed to carry “almost four times their weight” (according to
the [Museum of Flight blog](https://blog.museumofflight.org/the-legacy-of-the-lunar-rover)) or twice
(according to [Wikipedia](https://en.wikipedia.org/wiki/Lunar_Rover_Vehicle)), that means that the
model has to be almost entirely focused on wheels and chassis and
leave everything else out. Looking at some other photos I took
that show what look like real toggles, I think the museum has
either the human factors model or the one-g trainer. (Wikipedia
has a list of the eight full scale models.)

Last week in a threat modeling training, we had someone spend nearly an hour
crafting a beautiful DFD of a fake system that we use in our
trainings. It was, admittedly, a nice diagram. Elements were
grouped, nicely arranged, good labels... and he spent an hour on
it. Other people kept calling it “the better diagram,” and I
pushed back: it’s not *better* on some universal
scale. It was a different return on investment than other people
had made.

Similarly, as much as I wouldn’t mind having my own Lunar Rover,
storing it would be a pain. We need to consider the properties
that we need in a given model.

Sometimes the models we make in threat modeling leave a great deal
out: we might want an infrastructure model that focuses on the
infrastructure. Including software components can make for an
overwhelming diagram. We might create a diagram focused on a
specific scenario, like upgrading or canceling an account that
digs into components that aren’t otherwise prioritized.

Originally published by Adam on 17 Sep 2025

Categories:
  [space](/blog/category/space)
  [engineering](/blog/category/engineering)
  [history](/blog/category/history)
  [threat modeling](/blog/category/threat-modeling)

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

[Book Reviews](/blog/ca...