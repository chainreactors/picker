---
title: Andor: Insider Threats
url: https://shostack.org/blog/andor-insider-threat/
source: Shostack & Friends Blog
date: 2025-06-03
fetch_date: 2025-10-06T22:55:09.784609
---

# Andor: Insider Threats

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
3. Andor: Insider Threats

Shostack + Friends Blog

# Andor: Insider Threats

Andor teaches us about insider threats
![A still from the TV show](/images/blog/img/2025/lonni-1000w.jpeg)

This post has spoilers for Season 2 of Andor, some lessons we can
take for cybersecurity, and some thoughts on the writing process
and drama.

In Episode 10, we learn that Lonni has had Dedra’s “access cert”
for a year, and in Episode 11, we learn about how he’s been using
it. We don’t learn how he got it, but when questioned, Dedra
denies having given it to him (and there’s little reason to think
she would have).

Investigators will often assume the simplest explanation is
true. In this case, that's sharing, rather than theft.
The idea that a security
mechanism failed and allowed Lonni to steal Dedra’s key never
comes up. (There’s some excellent analysis of this in Eric
Geller’s [roundup](https://ericgeller.wordpress.com/2025/05/17/andor-season-2-review-episodes-10-12/). Short
form: An executive’s priority take precedence. In this case, it’s
not even clear that that’s the wrong choice, despite the injustice
of it all. A decade-long project that’s at risk is made more at
risk by the investigation.)

Setting prioritization aide, and going back to authorization and
incident response, the first instinct is to conflate an account
and its normal user. That is, because UID 1138 opened the file, Dedra
read it. (How exactly, the Empire knows that it was Lonni that
read it is not clear, but I assume it’s surveillance cameras,
etc.)

Normally, it would be interferingly pedantic to trace through
“Dedra pressed a key, causing a connection on a keyboard. That
led the keyboard to trigger a key send event via Bluetooth. That
was received by the Imperial ESA-390, which dereferenced the
devices table to send the key press to her active terminal
session...” it’s almost always ok to model all those steps as
“Dedra sent a database query...”

But in
an investigation, it can mean noticing or being taken in by a
false flag. As the facts from an investigation are analyzed, these
mistakes can lead to incorrect attribution. That’s part of why
real justice systems have adversarial analysis and time for such
processes to work. The alternative is state security services run unchecked.

If I was writing [Threats](https://threatsbook.com/) today, it would be really
tempting to use this in either the spoofing or expansion of
authority chapters.

But more importantly, this brings us to the several meanings of
“insider threat.” They include: An insider who’s misusing
their authorized access, and an attacker who’s using someone
else’s access. Interestingly, Lonni takes on both of these roles. He
plays the first when he’s using his authorized access, and the
second when using Dedra’s. (The first meaning can be emotionally
challenging: We trust Lonni. He wears the uniform. He’s one of
us. Directing energy towards the second can be quite helpful in a
healthy organization.)

In fact, insider threats can be so challenging to think about that
I missed that Dedra herself is an insider threat: getting extra
information, obsessing about Axis, not reporting security problems
because they help her...Thanks to Steve Gibbons for pointing that out.

Beyond that, Lonnie hides his extra access cert from Luthen,
because he expects Luthen would have pressured him to use it in
a way that would trip alarms. The interplay of risk management by
the spy and the handler is exceptionally well-written.

The last three episodes also provide excellent demonstration of how
compartmentalizing information makes investigations easier, which
isn’t really a technical point, but is an important one. Lastly,
there a fantastic bit of character arc where Dedra is in the
interrogation room, and appears to have spent the night there. She
suggests that old radio protocols will help them catch the spies. Her
sad devotion to a misguided mission doesn’t help her conjure up an
escape.

Compartmentalizing information also makes life worse, and [Emmet
Asher-Perrin](https://reactormag.com/author/emmet-asher-perrin/) touches on it in [one
tired trope Is Uniquely Infuriating](https://reactormag.com/andors-participation-in-one-tired-trope-is-uniquely-infuriating/).

The last episodes also bring fairly satisfying closure to three of the four ISB
agents we’ve gotten to know. It’s not justice in any sense, but it
is serious adult resolution.

After watching Andor, we re-watched Rogue One, which I’ve
previously called the best Star Wars movie, and it maintains that
status, but only by virtue of being a movie. Andor is the best
Star Wars content for adults, and had Andor been made before Rogue
One, I think the movie could have been even better. I have to
admit, that’s not a
fair frame in which to judge the movie. The movie created space
and desire for the show, and the Andor team did a phenomenal job of
writing for tech geeks like me, Star Wars geeks and less-devoted fans.

Regardless, the series gives me a new hope for future Star Wars storytelling.

Originally published by Adam on 02 Jun 2025

Last updated on 03 Jun 2025

Categories:
  [star wars](/blog/category/star-wars)
  [security](/blog/category/security)

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

[![A moon buggy model at the Museu...