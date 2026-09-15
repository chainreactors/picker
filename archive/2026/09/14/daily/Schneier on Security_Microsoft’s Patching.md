---
title: Microsoft’s Patching
url: https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html
source: Schneier on Security
date: 2026-09-14
fetch_date: 2026-09-15T07:03:09.434345
---

# Microsoft’s Patching

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Microsoft’s Patching

Once a month, Microsoft pushes a security update to all Windows users. Tomorrow’s is a [new record](https://arstechnica.com/security/2026/09/microsoft-patches-a-record-972-vulnerabilities-112-of-them-critical/):

> Microsoft’s patch for September is a doozy, with a record number of roughly 972 vulnerabilities fixed and 112 of them meeting the high critical-severity threshold.
>
> It was only two months ago that Microsoft patched a then-record 570 vulnerabilities. Then, last month, Microsoft patched some 620 of them. Google and other companies have also published record numbers of vulnerabilities in recent months. Two weeks ago, OpenAI, Anthropic, Amazon Web Services, Google, Microsoft, and 100 companies and organizations published an [open letter](https://openai.com/collective-cyberdefense) warning of a narrowing window for patching vulnerabilities ahead of an expected tsunami of AI-enabled attacks that actively exploit them first. The industry is taking the threat seriously by pumping out unprecedented numbers of patches in their software.

This is the result of AI-powered vulnerability finding, and a good example of AI helping the defenders more than the attackers.

What will be interesting to watch is how the number of vulnerabilities changes over the next few months. My prediction is that it will continue to increase as the AIs get better at finding software vulnerabilities, and then decrease as they run out of vulnerabilities to find. How high the number gets, how fast the trend reverses, and how quickly it declines after that are all unknown.

And Microsoft is right: The window to patch has shrunk to “immediately.” AIs are also good at reverse-engineering exploits from patches, which means that these vulnerabilities will be weaponized as soon as the update is published.

Tags: [AI](https://www.schneier.com/tag/ai/), [Microsoft](https://www.schneier.com/tag/microsoft/), [patching](https://www.schneier.com/tag/patching/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/), [Windows](https://www.schneier.com/tag/windows/)

[Posted on September 14, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html#comments)

### Comments

Simon Taylor •
[September 14, 2026 7:46 AM](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html/#comment-457941)

The patch was last Tuesday 8th September, not tomorrow.

Rod •
[September 14, 2026 8:07 AM](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html/#comment-457942)

You miss an important bucket. Fixing security issues introduced by “AI”.

I have no doubt that pattern matching will spot bugs. After all that’s what you are looking for when you desk check or review code. But all that we are seeing right now is paying the tax for years, if not decades, of poor software engineering practice.

People are so mesmerised by Eliza that they drop any judgement that they ever had. Subjectively software quality has been dropping for years but it took a nose dive when people started using “AI”.

Software engineering knows how to build The Forth Bridge, but it actively choses to build the First Tay Bridge. Just lots of them really really cheaply.

Bob •
[September 14, 2026 9:24 AM](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html/#comment-457943)

When did Patch Tuesday move to the third Tuesday of the month?

Clive Robinson •
[September 14, 2026 9:53 AM](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html/#comment-457944)

@ Bruce, ALL,

With regards,

> ‘And Microsoft is right: The window to patch has shrunk to “immediately.”’

Actually depending on how you look at it that is not actually true.

The “time to patch” is currently with AI attacks around,

“7 days before Microsoft starts work any kind of work on the patch”

It appears that the time for “hint of a bug” to “full exploit by AI” is as little as half an hour to a few hours depending on how many “bugs” need to be converted to “vulnerabilities” then chained into a “full exploit” and “deployed as attacks”

Sending the same “hint” to Microsoft won’t even have cleared the inbound support que system Microsoft has, based on what has been said about “response times”.

Therefore waiting for a month on average for a patch is now “ludicrous” and in honesty always has been.

But this raises the question of,

“What is needed as a ‘hint’ these days?”

Actually next to nothing just a “gut feeling” by an attacker to point the AI.

Adding a little more “science” to it takes it into a very similar domain to intelligence gathering / surveillance by “Traffic Analysis”.

Realistically the only solution to this “hint to attacked” time scale of hours is some form of “Pre-Mitigation”.

The only one we know that currently works is,

“To segregate attackers from systems”

As AI end of the chain limitation by “Guardrail or Sandbox” has been proved to be always open to bypassing in some way.

Which means “isolating user end systems” from all forms of external communications and all but essential internal communications.

If any one knows of another “Pre-Mitigation” that reliably works with all methods of attack “sing out”.

But the big problem is computer systems are not designed to run without “communications” as a general case data has to go in from a “source” and processed results come out and go to a “sink” system of some kind for storage or further processing

The,

“Used with level of segregation now required with AI attacks.”

Really does mean “Energy Gapping” not “air-gaping” and “gap crossing” form source or to sink needs to be done in a highly instrumented and locked down manner that is,

“Isolated in all ways from external communications, and nearly all internal systems.”

Think about what that actually means…

Somebody only half joking said the other day that,

“The only job with a longterm future for humans in the face of AI attacks is ICTsec…”

[Frank Rietta](https://rietta.com/blog/rubygems-supply-chain-openai/) •
[September 14, 2026 10:23 AM](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html/#comment-457945)

I respectfully disagree in part on your conclusion that this is AI being better for the defenders. The collapsed patch time is something the world is not ready for. tcell reported protracted patch times back in 2018 and while it’s hard to come by reliable data my own antidotal experience with development teams is a week would be very fast turn around. Hours is a taxing base line most are not ready for. I did cite you on my latest post on the RubyGems/OpenAI incident report that has circulated over the weekend.

KC •
[September 14, 2026 6:57 PM](https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html/#comment-457957)

re: a decrease in vulnerab...