---
title: RSI vs The Real World
url: https://scriptjunkie.us/2026/09/rsi-vs-the-real-world/
source: Thoughts on Security
date: 2026-09-14
fetch_date: 2026-09-15T07:01:46.134001
---

# RSI vs The Real World

Something about Network Security. Exploits, research … profit!

# [Thoughts on Security](https://scriptjunkie.us/)

* [Home](https://scriptjunkie.us "Click for Home")
* [About](https://scriptjunkie.us/about/)
* [Building Secure Networks](https://scriptjunkie.us/building-secure-networks/)
* [Copyright/License](https://scriptjunkie.us/copyrightlicense/)
* [Important Stuff](https://scriptjunkie.us/important-stuff/)
* [Links](https://scriptjunkie.us/links/)
* [msfgui](https://scriptjunkie.us/msfgui/)
* [Privacy Policy](https://scriptjunkie.us/privacy-policy/)
* [sessionthief](https://scriptjunkie.us/http-sessionthief/)

« [Tracking Signal Identifiers](https://scriptjunkie.us/2026/01/tracking-signal-identifiers/)

## RSI vs The Real World

Dario Amodei, the head of Anthropic recently published "[We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier)" ostensibly concerned about "the risk of losing control of AI systems, misuse of AI for cyberattacks and bioterrorism, and serious economic disruption". The post noted "AI’s growing ability to build the next generation of AI. This dynamic is called recursive self-improvement, [RSI] and it is starting to happen" and specifically referred to the "OpenAI-Hugging Face incident (OAI-HF)" with Dario's conclusion that "it’s my worry that in 6–12 months such a swarm could be capable of taking over the entire internet with a persistent botnet (potentially causing hundreds of billions of dollars in damage)"

This not coincidentally comes on the heels of frontier AI systems moving rapidly from being able to solve basic homework math problems to being able to solve university math, to even apparently knocking out a millennium prize problem, one of the most well-known and difficult unsolved mathematics problems that have eluded even the greatest mathematicians. AI has also been finding a rising tide of vulnerabilities across software. While an understandable concern from an outside perspective, the doom scenario is clearly ridiculous with just a bit of background and a little thought.

## The Model Size Mismatch

First, the models Dario is explicitly referring to, the frontier models, require datacenters worth hundreds of millions of dollars. They can easily, immediately be switched off. It is not fathomable that such models could copy themselves to random phones or laptops. In the years spent developing and using various forms of hacking persistence, copying frontier models around to be persistent has to be one of the most ludicrously impossible ideas I have yet seen even if you somehow got malicious access to a datacenter with free petabytes of storage and acres of expensive GPU's. The entire concept is self-defeating.

And the small models that do fit on commodity hardware are being developed by hundreds of labs all over the world. So in addition to being very impractical, near impossible for a persistence mechanism, none of these labs are pausing for fear of themselves, and many of which reside in countries with governments explicitly hostile to the idea of a pause. As the saying goes, "If your solution to a problem includes the words 'if everyone would just,' it is not a viable solution. At no point in history has everyone 'justed' and they are not going to start now."

So either the fear of persistence is ridiculous, or this "can everyone just" pause solution is ridiculous, or, most likely, both.

## The Main Difference

I have managed to work for years both in defensive operations (DFIR etc.) and offensive dev (e.g. vuln disco+exploit dev) and see the frontier pacers making the same invalid assumptions common to outsiders (and even exploit devs). Most of all, the doom scenario severely misunderstands the difference between most real world problems and the self-contained, static, pure-logic problems that can be recursively self improved.

Solving math problems and finding vulnerabilities, much like in solving checkers or playing the game of go, the greatest demonstrations of AI prowess are all similarly well suited to RSI. They all have a significant set of otherwise very uncommon characteristics:

* self-contained,
* endlessly reproducible,
* effectively stable,
* fully inspectable
* pure logic problems
* that fit easily into commodity memory sizes

CPU's can burn through billions of possibilities until it gets it right. So these are all things AI is making great strides on! And we have seen this before! It is very reminiscent of the wave of vulnerabilities found by fuzzers when they were first introduced. But hitting the real world is a lot harder.

AI has not solved cancer, made us all mansions, or even made a robot that can clear dishes off a table in large part because iterations involve physical things happening, and un-reproducible or unforeseen events happen all the time:

* They are not pure logic problems, you cannot exactly simulate physical or external processes
* The people, biology, weather, ... everything external you encounter may be more complex than all the logic in your datacenter.
* You cannot arbitrarily inspect what is happening. You do not see the intermediate steps. You do not even know what all the inputs are. And any probing you do is far more likely to alter what you are measuring.
* You cannot rapidly and arbitrarily reproduce problems. You might get one sequential clinical trial at a time, and wait a decade or more for results.
* The problems are not stable. This year's flu virus will not be next year's. Everything physical slowly degrades and does not work the same each time.

Hacking has another key difference as well. None of the areas in which AI has made advances have been adversarial. That exploit you used 1 million AI CPU-hours to find can get discovered and burned rapidly. One forum and one site might not have noticed for a bit they got hacked, but some of them definitely will. The world is full of systems that are unique and weirdly altered by humans. Any action you take can and might break something or be detected, any evasion for one action can itself flag another alert. That message board you used can switch you off in a second. Anything you send, upload, or do might be watched and some incident responder might trace back the whole food chain, burning all that stuff up to and including the datacenter shutting down the whole model.

In contrast with the pure logic problems, the models cannot know what moves are wrong ahead of time and cannot just churn through a billion iterations. Reality *fights back* and may shut down the whole intrusion infrastructure with as little as one wrong move. Try it again, and there will be patches and alerts to ensure it does not work the same. Defenders use automations including AI as well. And this sequence continues to happen right now, shutting down intrusions that are already AI conducted or accelerated.

## Biology

Biologist David Bellamy has many of the same observations in his field: <https://threadreaderapp.com/thread/2099187370407112758.html>

> I must be among an extremely small group of people (n=1?) that have both 1) trained a frontier LLM and 2) designed and synthesized custom viruses in a lab with my own two hands.
>
> And I think that the takes on AI killing us all by creating dangerous viruses is total bogus.
>
> — David Bellamy (@DavidRBellamy) [September 13, 2026](https://x.com/DavidRBellamy/status/2099187370407112758?ref_src=twsrc%5Etfw)

"The bottleneck is in the physical process of synthesizing a virus and the equipment/goods needed to do so." He notes an extreme expense (~$100,000,000) and mass amount of human expertise to set up and maintain the physical equipment as well as "Designing a virus that can evade all forms of pandemic counterdefense is not something that a 'genius in a datacenter' can do. This is something that requires contact with the physical world and iteration." and ultimately "the idea that 'RSI' - ie, the accelerating hillclimbing on fully verifiable, digital-only benchmarks...