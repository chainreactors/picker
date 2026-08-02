---
title: frontier class vulnerabilities: it gets worse before it (maybe) gets better
url: https://shubs.io/frontier-class-vulnerabilities-it-gets-worse-before-it-maybe-gets-better/
source: shubs
date: 2026-08-01
fetch_date: 2026-08-02T05:10:45.390784
---

# frontier class vulnerabilities: it gets worse before it (maybe) gets better

[![shubs](https://shubs.io/content/images/2026/05/cropped-headshot-1.jpg)](https://shubs.io)

# [shubs](https://shubs.io)

Co-founder of Assetnote, security researcher.

###### [Assetnote](https://assetnote.io/)

###### [Home](https://shubs.io/)

###### [Github](https://github.com/infosec-au)

###### [Twitter](https://twitter.com/infosec_au)

###### [LinkedIn](https://www.linkedin.com/in/shubhamshah/)

# frontier class vulnerabilities: it gets worse before it (maybe) gets better

August 1 2026

Early in my career as a consultant, I was put on source code review engagements despite not being experienced. This forced me to deliver on projects that, looking back, were of a ludicrous size and scope for my skills at the time.

Those early career opportunities kicked off an adventure spanning the last decade or so of trying to be the best I could be at finding vulnerabilities through reviewing code and systems. But these days, as frontier models advance, I've started to have mixed feelings about what the future looks like: personally, with existential dread kicking in, and globally for the internet, at least in the near term.

The company I co-founded and built over the last eight years, [Assetnote](https://www.assetnote.io/?ref=shubs.io) (acquired by [Searchlight Cyber](https://slcyber.io/?ref=shubs.io)), was the first Attack Surface Management company to exist. We built a world class, high impact security research team to consistently discover zero-days in the software that backed our product. As AI advancements have upended how our entire research team discovers vulnerabilities and audits software, we feel like we're in a unique position to comment on AI's capabilities in offensive security.

With each significant frontier model improvement, our research team sees incredible advancements in offensive security capabilities, so much so that it's starting to make us really question what our responsibilities as practitioners should be in this age.

In March 2026, a physics professor from Harvard, Matthew Schwartz, published a [blog post](https://www.anthropic.com/research/vibe-physics?ref=shubs.io) on his experience supervising Claude through a real theoretical physics calculation, which became a paper. He grades model capability against the levels of a physics PhD student, and put Claude at roughly a second-year grad student: capable of doing genuine research work when directed, but still needing close checking.

Reading through this blog, I recognised many parallels with what we have seen in the offensive security space. Opus 4.6 through 4.8 have probably been the first set of models where the collective community was able to 10x its output in offensive security, but doing so required steering, consideration, skill, and careful harnesses.

Matthew observed that Claude's models have the potential to greatly accelerate the pace of research, but that they weren't quite at the point where they could operate without some form of human push, intuition, or assessment. In his own words: "We are in possession of tools that can speed up our workflows by a factor of 10. From my point of view, it's immensely gratifying to work this way—I never get stuck anymore and I'm constantly learning."

That was all well and good, and we agreed wholeheartedly with Matthew. But then GPT 5.6 Sol was released in early July 2026. This significantly changed the landscape for us in offensive security, so much so that some of the findings from Matthew's March 2026 post about Claude simply don't hold true anymore. GPT 5.6 Sol has also been making progress in mathematics, producing solutions never seen before.

A wave of extremely critical vulnerabilities has been discovered with GPT 5.6 Sol, with very little human input or supervision. Some of these vulnerabilities and exploit chains are extremely technically complex, and often take hours or days to fully understand after GPT discovers them.

I know this because our research team discovered and disclosed wp2shell (a pre-authentication RCE in WordPress, which powers roughly 40% of the internet) with the help of GPT 5.6 Sol and no pre-conditions. [Adam Kues](https://x.com/hash_kitten?ref=shubs.io), our researcher who discovered this vulnerability with GPT 5.6 Sol, wrote [more about the research here](https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/?ref=shubs.io).

I don't think offensive security practitioners are the real innovators yet, though. Adam's prompt was adapted from a [prompt published by OpenAI](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf?ref=shubs.io), after Sol solved a famous mathematical conjecture called the [Cycle Double Cover conjecture](https://en.wikipedia.org/wiki/Cycle_double_cover?ref=shubs.io). I expect to see a lot more of this knowledge transfer, or copying, between experts regardless of what domain they are in, when it comes to how to most effectively get outcomes from AI.

This level of capability is where everything starts to get scary, especially in cybersecurity. The fact that GPT 5.6 Sol could find a critical vulnerability in WordPress with minimal human interaction, in 6 to 10 hours of constant iteration by itself, is insane. WordPress Core is a target that vulnerability researchers hope to find a single security issue in even once in their entire lives, because doing so is neither trivial nor easy.

This enhanced capability has led to a complete shift in how we see security research at Assetnote/Searchlight. We had our yearly all-hands this past week, and sitting down with all of our researchers in a room, I laid out our strategic mission for the next year. I directed them to find **internet melting bugs**. If we don't find them, attackers really won't be that far behind, and our customers (and the internet) will face a much greater loss than if we find them first. With GPT 5.6 Sol, and any future models, we are only at the start of this journey, and we have a responsibility to use this capability for good as experts in our field.

What does this actually mean for the companies and people who have to secure themselves, though? It means it's going to be a busy couple of years, and that part seems pretty certain.

> Yup. 2–5 years of scary bugs that keep every cybersecurity company busy. And then a world of bug-free software. Not tomorrow, but also not that far off. [https://t.co/ZlGe4W9LDk](https://t.co/ZlGe4W9LDk?ref=shubs.io)
>
> — Matthew Prince 🌥 (@eastdakota) [July 31, 2026](https://x.com/eastdakota/status/2083230816914858059?ref_src=twsrc%5Etfw&ref=shubs.io)

But longer term, could we actually see entire classes of vulnerabilities cease to exist? Or a universally high baseline standard of security for anything developed going forward? These points are yet to be proven, but could be possible.

The funny part of all of this is that I actually read the [vibe physics](https://www.anthropic.com/research/vibe-physics?ref=shubs.io) blog post from Matthew Schwartz long after I told my team to focus on higher quality work, but we came to exactly the same conclusion independently:

> "one large consequence I foresee in science is that people will work on harder problems: quality, not quantity"

That's exactly what I told our research team to do. Focus on quality, and in security research that means finding vulnerabilities that affect as much of the internet as possible.

While I do want the bug-free software angle to be true, I don't think it's as black and white as that. We've been dealing with the same classes of vulnerabilities for 20 years. In computer security, we have rarely ever seen the total eradication of any one bug class in our entire history.

My actual prediction is that bugs will not just one day globally cease to exist; legacy software will still take a really long time to replace, but at the very least, new software generated through AI may be very well secured.

What we can do right now as practiti...