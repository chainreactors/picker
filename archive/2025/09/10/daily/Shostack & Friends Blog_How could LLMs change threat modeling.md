---
title: How could LLMs change threat modeling
url: https://shostack.org/blog/how-could-llms-change-threat-modeling/
source: Shostack & Friends Blog
date: 2025-09-10
fetch_date: 2025-10-02T19:54:37.339230
---

# How could LLMs change threat modeling

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
3. How could LLMs change threat modeling

Shostack + Friends Blog

# How could LLMs change threat modeling

LLMs will change threat modeling. Will it be for the better?
![photograph of two people seated in a book-lined office, both facing right side of the image, one a robot in an overstuffed armchair, the other a person dressed in office clothes lying on a chaise lounge, sketching an enterprise data flow on a whiteboard](/images/blog/img/2025/how-llms-could-change-threat-modeling-1000w.png)

Is threat modeling a journey or a destination? Is it a noun or a
verb? This nuance pervades our conversations. The model of lightweight
approaches with a whiteboard that found important threats and let
development teams adjust course got supplanted by document-heavy
and lower-value processes. When I started at Microsoft, the threat
modeling process had 17 steps, starting with ‘make a list of all
your assumptions’ — a step whose output was never used. I
simplified that to be 5 steps (later 4).

One of the reasons Agile is so popular is that process and
documentation tend to grow, and they tend to grow for good
reasons, which makes processes heavyweight. A lot of threat modeling work
is writing and refining records, while a lot
of the value is participants engaging in the work, like identification of trust
boundaries and better architectures, that are hard to record
in a clear way. What do you write down? “We thought about this
design, which in hindsight doesn’t make a lot of sense”? Why would
you spend energy writing those words?

The decision may well show up in an [ADR](https://adr.github.io/), but by design, ADRs are brief, and noting
the security value of a boundary is a small number of words. That
frequently implies that they’re not very important..

On Linkedin, Izar Tarandach has an [article on CTM and LLMs](https://www.linkedin.com/pulse/ctm-llms-hitting-wall-good-way-izar-tarandach--xq80e/?trackingId=kCMDbf2aRVOIV5ncO6PzsA%3D%3D) which
uses a tennis metaphor for a back and forth, conversational model
of security analysis. This is a “journey is the reward” model
which ties back to having a security expert available for
conversation. There’s a huge potential for avoiding problems.

Izar doesn’t avoid the challenges in his approach:
> Think of it less as an expert review and more as that friend who
> always asks awkward questions at the worst time... Don’t let the
> model file threats on autopilot. That’s just vibe threat modeling,
> and it ages badly...Don’t mistake confidence for accuracy. A model
> will always have an answer; it will speak confidently of things
> that are matters of opinion

And so as we mature our thinking about threat modeling, we can move
from threat modeling as a single activity (or meeting) to threat
modeling as a set of tasks and activities that are integrated into
development work. (I think this is integral to Izar’s approach to
continuous threat modeling, but often overlooked.) That’s threat
modeling as a journey, and it creates a question of what records
are needed, by whom, and how to create them.

It might be tempting to assign the summarization to LLMs, but
LLMs are [bad at summarizing](https://pivot-to-ai.com/2024/09/04/dont-use-ai-to-summarize-documents-its-worse-than-humans-in-every-way/). I’d guess
that this is because they’re token models, not concept models, but
who knows? (It’s easy to come up with facile vibe explanations to
which people will naively nod along.)

As we think about how LLMs can change development, I go back to
LLMs as linters, which I included in [LLMs as Compilers](https://shostack.org/blog/llms-as-compilers/). If we ask the LLM to help, we
might get something like the below (I’m not going to spend my energy
formatting the output, you can read [the conversation](https://g.co/gemini/share/7fb0d0c18e8e).) The words I added to Izar’s
prompt are bolded.
> *Taking into consideration the table you can find at
> https://github.com/izar/continuous-threat-modeling/blob/master/Secure\_Developer\_Checklist.md,
> given this user story, does it have a security value? **If it does, rewrite the story to address.**
>
> The user story is:
>
> “As a user I would like to be able to add, view and remove an item to
> the existing list.”*
> Based on the user story you provided, it does have a significant
> security value. I was unable to retrieve the specific checklist from
> the provided URL, but the actions described in the user story, "add,
> view and remove," are fundamental data operations that carry inherent
> security risks. [...]
> Rewritten User Story with Security Considerations:
> "As a privileged user, I want to be able to securely add, view, and remove items from the existing list, so that I can manage the list's content without compromising its integrity or the confidentiality of its data.”

We can consider a pipeline tool, or a Jira tool, or a part of
backlog grooming (pre-grooming?) where prompts like this are run
as part of a process.

I’m giving a lot of thought to how to use LLMs effectively in
threat modeling. I’m going to be sharing all of that in
November at OWASP’s Global Appsec DC, in our new course, [Threat
Modeling Intensive with AI](https://shostack.org/blog/owasp-dc-announcement/). It’ll be our longest course ever,
at a full three days, and I’m excited to see it go!

Midjourney photograph of two people seated in a
book-lined office, both facing right side of the image, one a
robot in an overstuffed armchair, the other a person dressed in
office clothes lying on a chaise lounge, sketching an enterprise
data flow on a whiteboard classic Freudian psychoanalysis style, warm ambient lighting, cinematic composition --ar 8:3 --v 6.1

Originally published by Adam on 09 Sep 2025

Categories:
  [threat modeling](/blog/category/threat-modeling)
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

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2025/appsec-rou...