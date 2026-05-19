---
title: The down fall of bug bounties
url: https://shubs.io/the-down-fall-of-bug-bounties/
source: shubs
date: 2026-05-18
fetch_date: 2026-05-19T06:03:36.738376
---

# The down fall of bug bounties

[![shubs](https://shubs.io/content/images/2026/05/cropped-headshot-1.jpg)](https://shubs.io)

# [shubs](https://shubs.io)

Co-founder of Assetnote, security researcher.

###### [Assetnote](https://assetnote.io/)

###### [Home](https://shubs.io/)

###### [Github](https://github.com/infosec-au)

###### [Twitter](https://twitter.com/infosec_au)

###### [LinkedIn](https://www.linkedin.com/in/shubhamshah/)

# The down fall of bug bounties

May 18 2026

A few days ago, I was reading a post by [Kabir Acharya on how the CTF scene has died](https://kabir.au/blog/the-ctf-scene-is-dead?ref=shubs.io) as a result of frontier models killing authentic competition. I couldn't really fault his points, but I started thinking about what could actually fix this. We're not going to start installing glorified root-kits (a.k.a anti-cheat) and having supervised e-sports like competitions for CTFs, or are we?

I think what Kabir spoke about in his blog is spot on, there's a growing epidemic where AI is changing how we work in the security research space. With any new innovation there's always drastic changes that are both good and bad. Now, any one with sophisticated model access can solve CTF challenges, or submit reports to bug bounties that look real enough.

AI hasn't just changed CTFs, it's changed how we perform security research as a whole, and ultimately, it's fundamentally changed the economics and underlying principles of many aspects of how bug bounties and their platforms work too.

Speaking with people who manage these platforms day to day, the impact is brutal. An onslaught of "AI-assisted" reports (basically a nicer way of saying slop). I feel for the triagers and the platforms, and while I sympathise regarding the change of pace and time, I don't even think this is the reason bug bounty platforms have let us down so much in the last few years.

We are all adapting to the change of pace, both the researchers and the platforms. Obviously the researchers that were really talented before AI models, are still talented today. We're not the ones submitting the slop, trust me. But this is the same for the reverse direction. People submitting bugs without much knowledge are also equally amplified in submitting AI slop reports without understanding or validating what is returned by AI agents.

So what are you really left with? Well, the great researchers are submitting world class reports assisted by AI at an even greater pace, and the less skilled researchers are polluting the triage queue with genuinely unimportant vulnerability reports. The sad part is that the great research suffers massively, and a disproportionate amount of time is spent on the invalid reports.

The way that these platforms are dealing with this is pretty revealing. HackerOne is trying to fight AI with AI, and Bugcrowd is trying to put in controls that are logical towards stopping spam reports from AI agents. Regardless of what approach these platforms are taking towards this, the joy of reporting vulnerabilities to bug bounties is quickly dissipating. Probably more on HackerOne than Bugcrowd right now.

I've been hacking on Uber's bug bounty program for almost ten years (!!!) and am ranked as #1 on their public program. I sent in a report on the 24th of April for an important vulnerability that led to mass PII leakage. Typically, these sort of vulnerabilities are actioned in 1-3 days on average. Not anymore. The first response from a human was on May 6th. That's a 12 day delay until a human tried to validate it. Sorry boss, we didn't action the vulnerability because our ticketing system (a.k.a bug bounty platform), didn't validate the bug in time.

One of the strongest pulls into a program is how fast they can action a report meaningfully (if you're actually submitting real bugs). It keeps the ADHD loop going, and even if they don't pay a high amount for the bugs, it motivates towards spending more time on that program. Sadly, that's dead now for many programs. You can also trust me when I tell you that I'm not participating in bug bounties for the monetary aspect right now. I participate because I love hacking, and I love closing the loop towards solving really tough problems and the response from the programs.

I wish these platforms took a more pragmatic approach to their solutions here. I've been submitting to Uber for almost ten years, yet to them, report is buried in the noise, the same as all the AI slop reports. This whole dystopia seems so far away from the roots of these companies which were supposed to be hacker first that it has me questioning whether or not they actually understand their own community of hackers, at least the ones that bring decades of skill to the table.

Don't get me wrong, I would hate to be operating or running a bug bounty platform in the age of AI, but right now, as a researcher, the experience has degraded to the point where I don't even feel like submitting my reports now. I know that I'm not the only one. So many talented researchers would rather spend their time on either 1) really solid programs that don't have this problem, or 2) research for fun, not money.

Hopefully the platforms actually work this out, but until then, I can't see myself continuing to report high quality original research to certain programs where I have meaningfully contributed for a decade when they fail to understand the difference between myself and a researcher that doesn't have any credibility. Maybe someone else can take the #1 spot on Uber now, I am tired of defending it, but it's been a good run.