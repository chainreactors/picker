---
title: On Generative AI Security
url: https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html
source: Schneier on Security
date: 2025-02-06
fetch_date: 2025-10-06T20:39:45.256473
---

# On Generative AI Security

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

## On Generative AI Security

Microsoft’s AI Red Team just published “[Lessons from Red Teaming 100 Generative AI Products](https://airedteamwhitepapers.blob.core.windows.net/lessonswhitepaper/MS_AIRT_Lessons_eBook.pdf).” Their [blog post](https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products/) lists “three takeaways,” but the eight lessons in the report itself are more useful:

> 1. Understand what the system can do and where it is applied.
> 2. You don’t have to compute gradients to break an AI system.
> 3. AI red teaming is not safety benchmarking.
> 4. Automation can help cover more of the risk landscape.
> 5. The human element of AI red teaming is crucial.
> 6. Responsible AI harms are pervasive but difficult to measure.
> 7. LLMs amplify existing security risks and introduce new ones.
> 8. The work of securing AI systems will never be complete.

Tags: [AI](https://www.schneier.com/tag/ai/), [computer security](https://www.schneier.com/tag/computer-security/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/), [Microsoft](https://www.schneier.com/tag/microsoft/)

[Posted on February 5, 2025 at 7:03 AM](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html#comments)

### Comments

Clive Robinson •
[February 5, 2025 8:18 AM](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html/#comment-442790)

It’s not a list I would actually much agree with by the way it’s worded.

Take

> *“4. Automation can help cover more of the risk landscape.”*

Really? In What way?

All automation can really do is make the search for “Known Knowns” in effect faster.

It does not make the hunting for “Unknown Unknowns” or “Unknown Knowns” any more effective.

In theory AI systems can “look in the gaps” between “known knowns” and find ways they morph from one into another. Thus show any new “unknown knowns” they find along the way.

The point is it’s a very very rich target environment, any new “unknown knowns” found that way have a very low probability of becoming in active use.

The thing is humans are “quirky by nature” and rarely step by step methodical. Thus most new “unknown knowns” will be of little or no interest as they in effect lack the “fun factor” of breaking new ground finding “unknown unknowns”..

Thus the use of future AI systems to find “unknown knowns” is most likely to be by those who want to,

“Industrialise vulnerability usage”

Which by and large is not researchers or for profit type criminals. But those looking for endless supplies of exploits against ordinary individuals, such as journalists and political opponents.

I could go through the list item by item, but by now I hope most people realise the list says more about those who drew it up than it does about the reality of what is going on.

Bob •
[February 5, 2025 11:42 AM](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html/#comment-442792)

@Clive

> All automation can really do is make the search for “Known Knowns” in effect faster.

And more complete. Faster and more complete sound like wins to me.

> It does not make the hunting for “Unknown Unknowns” or “Unknown Knowns” any more effective.
>
> The human element of AI red teaming is crucial.

To some degree or another, this stuff is here to stay. Forward-thinking has to accept that. To me, a lot of the criticism around AI is echoing what I heard about cloud computing and cryptocurrency back in the day.

If you refuse to consider cloud solutions, you’re a fool. If you don’t have any crypto in your portfolio, you’re a fool.

You’re taking something that changes by the second, pointing to its limitations from yesterday, and making reactionary pronouncements regarding its future. I’m not retired. I don’t have the luxury of pretending the future isn’t coming.

I'm sorry, Dave. I'm afraid I can't do that. •
[February 5, 2025 2:16 PM](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html/#comment-442794)

The case studies in the paper illustrate Clive Robinson’s point.

Being intelligently cautious is good for one’s career. The reason that you often see semi-retired or retired professionals behaving cautiously is that cautiousness is one of the traits that kept them alive in their profession.

Anonymous •
[February 5, 2025 10:01 PM](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html/#comment-442797)

Wow, I don’t know which adjective to apply there. Insightful or introspective? Nobody else could have have come up with that level of banalities.

Winter •
[February 6, 2025 1:38 AM](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html/#comment-442799)

@Bob

> To me, a lot of the criticism around AI is echoing what I heard about cloud computing and cryptocurrency back in the day.

I might be older than you and want to add

* Who needs a mobile phone? Only business people who want to look important. Vodafone predicted it would sell only a million mobiles max.
* The Internet is a fad/will fail
  <https://www.newstatesman.com/science-tech/2016/08/25-years-here-are-worst-ever-predictions-about-internet>
* Email was considered a useless hype that would go away
  <https://www.theguardian.com/uk-news/2018/dec/28/national-archives-john-majors-aides-emails-were-passing-fad>
* There Is No Reason for Any Individual to Have a Computer in Their Home
  <https://conversational-leadership.net/blog/no-reason-computer-in-home/>

Clive Robinson •
[February 6, 2025 5:15 AM](https://www.schneier.com/blog/archives/2025/02/on-generative-ai-security.html/#comment-442800)

@ Bob,

With regards,

> “Faster and more complete sound like wins to me.”

Only for a very brief time at best for the attacker.

You need to think a little further about why I said “known knowns” finding.

As I’ve used in the past I will note a well known equivalent of humans in workplaces and similar and “Fire Drills”.

There are lots of issues both natural and man made that need people to be practiced in evacuating a place or area quickly and safelt. Not just for their safety but the safety of others (think rescuers etc).

Whilst originally designed for “fire in buildings that burned easily” we know from 9/11 they work for terrorist attacks as well. Japan and other places have similar drills for earthquakes, volcanos, mud slides, flooding, tsunamis etc etc.

The point is that the “drills” are not for one instance in one class of issue, they are designed to cover as many instants in as many classes in just the one drill. To accomplish this certain trade offs have had to be made in “building design” and is one of the reasons we have building codes.

The software industry has in the main not yet reached t...