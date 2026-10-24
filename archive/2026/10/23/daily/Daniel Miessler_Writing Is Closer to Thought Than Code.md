---
title: Writing Is Closer to Thought Than Code
url: https://danielmiessler.com/blog/intent-driven-development?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-10-23
fetch_date: 2026-10-24T06:48:25.647912
---

# Writing Is Closer to Thought Than Code

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Writing Is Closer to Thought Than Code

Why your written intent should be the source of truth when building with AI

October 23, 2026

[#ai](/archives/?tag=ai) [#writing](/archives/?tag=writing) [#future](/archives/?tag=future) [#innovation](/archives/?tag=innovation)

[**AIL***1*](/blog/ai-influence-level-ail "AIL 1 — Human Created, Minor AI Assistance")

 Rubber-duck-debugging…

[![Charcoal sketch of a stone archery target: a tight purple arrow cluster cracks the outer ring while quill pens surround the bullseye](/images/intent-driven-development.webp)](/images/intent-driven-development.webp)

I’ve been having this almost-debate with [Matt Pocock](https://github.com/mattpocock) for a while about the best way to do [spec driven development](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/).

Matt is a very accomplished old-school developer. A true software engineer. And he’s been using AI to enhance his capabilities to an extraordinary degree. [His development skills](https://github.com/mattpocock/skills) are extremely powerful, and have been starred more than almost any other skills repo on GitHub.

So what’s my disagreement?

Basically I think he is at the top of the mountain for the old way of doing things. He’s got tons of skills and tons of commands. And having a human in the loop is a major theme for him.

But his central idea lately has been that the most important thing in a development project is the code itself. That specs are useful and everything, but [the code itself is the main artifact](https://x.com/mattpocockuk/status/2113264229453033684). The source of truth for everything.

I disagree strongly. I think the articulation of what you’re building, and why, is far more important. Basically, the idea. Your intent.

I think the most important thing in any project you’re building with AI (and even without it), from building a web app, to starting a business, to managing a federation of planets, is how completely and accurately you articulate exactly what you want.

I think most of the problems we see with AI in 2026 are misattributed. AI is extraordinary at execution. It’s getting unbelievably great at doing what we ask it to do. More and more of the problems at this point are it executing the job perfectly, and having the result be different than what was in our mind.

But this is a communication problem. It’s an articulation problem.

Authors have this same problem. It’s commonly called [Writer’s Blindness](https://en.wikipedia.org/wiki/Curse_of_knowledge). Its where you think you’re perfectly capturing what’s in your brain, but you’re not. And so the receiver, or the reader, ends up missing information or getting a completely different review than the author intended.

The problem with Matt’s position is that he thinks code is authoritative. It’s actually an abstraction, the same way a painting is an abstraction of what the painter was wanting to convey. It’s an execution. A facimile. A representation.

But there’s a higher form of this, and that’s writing. And images.

Writing is the closest thing we have to human thought. As I like to tell people all the time, for me writing IS thinking. It’s the closest thing we have, by a wide margin.

[![Descending chain from thought and intent to writing to code, with fidelity narrowing downward; code is an execution, a facsimile, a representation](/images/intent-driven-development-fidelity.webp)](/images/intent-driven-development-fidelity.webp)

But I get why Matt is enamored with code. It does have more of something than even writing, which is precision. Writing has more accuracy, though. So it’s a [tradeoff between accuracy and precision](https://en.wikipedia.org/wiki/Accuracy_and_precision).

We obviously want both, but when it comes to building stuff with AI I think accuracy is far more important. The classic illustration of this is an archer trying to hit a bullseye on a target.

Accuracy without precision is a whole bunch of shots that are near the bullseye, but aren’t close to each other. Precision is the opposite, where all the shots are very close to each other, but might be quite far from what you’re trying to hit.

[![Two archery targets: writing's arrows scatter around the bullseye; code's arrows cluster tightly, well off it](/images/intent-driven-development-accuracy-precision.webp)](/images/intent-driven-development-accuracy-precision.webp)

When we build with AI we want the outcome to match what was in our brains. That’s accuracy. And there’s no closer way to capture the bullseye of what’s in our human brains than with writing.

So what does that mean?

It means articulating what you want, in written form, is the most important thing you an do for any AI project. And I don’t mean just in a rigid spec format, or a PRD format, but in much more holistic and creative ways.

I figured this out at the end of 2025 and switched everything I do over to something called an [Ideal State Artifact (ISA)](/blog/ai-ideal-state-articulation), which is a new document and approach for interacting with AI. It’s a much deeper capture of what we’re trying to build, and it uses multiple sections for the different types of articulation.

There is the articulated Ideal State, which is prose. Potentially lots of it. My harness ([LifeOS](https://github.com/danielmiessler/LifeOS)) uses a Discuss skill (similar to Matt’s [/grill-me skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)) to help fill this in as much as needed. This can be a few paragraphs, or it could be 4,000 words of stream of consciousness and deep introspection on some topic.

Then there are Constraints, things we don’t want to build, etc. Then there are Decisions that were made as we updated the ideal state for the project. We rarely start off with a perfect ideal state in the beginning. Sometimes it only becomes clear as we start building, and that’s ok.

And then the most important section (behind the ideal state definition at the top) are what we call Ideal State Criteria (ISCs). These are things we’re actually building and testing for in the application. They are extremely atomic and testable pieces of functionality. Each one of them has its own eval associated with it as well, which can range in complexity from a basic assert to a multi-phase code -> assert -> System 1 question set -> Rubric / Tournament / LLM as a Judge.

What’s really powerful about the Ideal State Criteria being defined this way, with their evals defined along side them right in the ISA, is that the ISCs are simultaneously what we build from AND the testing harness!

[![Diagram of an Ideal State Artifact: Ideal State, Constraints, Decisions, and Ideal State Criteria with an eval ladder from assert to LLM as a judge, feeding both what we build from and the test harness](/images/intent-driven-development-isa.webp)](/images/intent-driven-development-isa.webp)

So what we end up with is a single document for every project we’re building that represents the closest possible articulation of what’s in our mind. We call it an Ideal State Artifact because the ideal state articulation at the top is the most important thing, but really the entire document represents the closest possible representation of the idea we have in our mind of what we wanted to build.

Now, returning to Matt, it should be much clearer now why source code for the implementation of this project, in some computer-friendly language like Typescript or Python or whatever, is nowhere near as high-fidelity of a representation of the original idea as an Ideal State Artifact.

Writing is simply far closer to ...