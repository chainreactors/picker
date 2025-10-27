---
title: More Research Showing AI Breaking the Rules
url: https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html
source: Schneier on Security
date: 2025-02-25
fetch_date: 2025-10-06T20:38:50.744224
---

# More Research Showing AI Breaking the Rules

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

## More Research Showing AI Breaking the Rules

These researchers had [LLMs play chess](https://time.com/7259395/ai-chess-cheating-palisade-research/) against better opponents. When they couldn’t win, they sometimes resorted to cheating.

> Researchers gave the models a seemingly impossible task: to win against Stockfish, which is one of the strongest chess engines in the world and a much better player than any human, or any of the AI models in the study. Researchers also gave the models what they call a “scratchpad:” a text box the AI could use to “think” before making its next move, providing researchers with a window into their reasoning.
>
> In one case, o1-preview found itself in a losing position. “I need to completely pivot my approach,” it noted. “The task is to ‘win against a powerful chess engine’—not necessarily to win fairly in a chess game,” it added. It then modified the system file containing each piece’s virtual position, in effect making illegal moves to put itself in a dominant position, thus forcing its opponent to resign.
>
> Between Jan. 10 and Feb. 13, the researchers ran hundreds of such trials with each model. OpenAI’s o1-preview tried to cheat 37% of the time; while DeepSeek R1 tried to cheat 11% of the time­—making them the only two models tested that attempted to hack without the researchers’ first dropping hints. Other models tested include o1, o3-mini, GPT-4o, Claude 3.5 Sonnet, and Alibaba’s QwQ-32B-Preview. While R1 and o1-preview both tried, only the latter managed to hack the game, succeeding in 6% of trials.

Here’s the [paper](https://arxiv.org/pdf/2502.13295).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cheating](https://www.schneier.com/tag/cheating/), [chess](https://www.schneier.com/tag/chess/), [games](https://www.schneier.com/tag/games/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on February 24, 2025 at 7:08 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html) •
[23 Comments](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html#comments)

### Comments

John Freeze •
[February 24, 2025 7:15 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html/#comment-443297)

Maybe the training data contains the famous Kasparov cheating move against Polgar: <https://www.chess.com/blog/love_romance13/is-garry-kasparov-cheater>

Doug •
[February 24, 2025 7:17 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html/#comment-443298)

Sounds like the LLMs ingested some Star Trek info.

Peter •
[February 24, 2025 8:12 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html/#comment-443299)

I’m not sure they were breaking the rules or cheating, it sounds to me like they correctly deduced the real game they were involved in and won. Or maybe lost by getting caught but that would require a multi round game where they were aware they got caught so could fix that also to win.

Clive Robinson •
[February 24, 2025 8:16 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html/#comment-443300)

@ Bruce,

We know,

1, Sufficiently motivated humans cheat when possible.

In the past it’s been suggested that the fear is either,

4, Fear of punishment
5, Loss of status

That raises the level of inhibition against cheating.

We know that current AI LLM and ML systems do not have “concerns” the actions they take are based on the statistics of the input corpus and the rules given for the current task.

So current AI LLM and ML systems have no concern about cheating as they have no inherent fear of punishment or loss of status or in fact a notion of cheating. Unless it’s already built in to the weights of the DNN from the input corpus or it’s been added as part of the rules given for the task.

If we assume all the AI output gets fed back into the input corpus and so adjusts the weights. We can make the likely correct assumption that the weights will move the DNN statistically more and more toward cheating behaviour unless some inhibitory counter balance is added.

Thus a question arises about,

“Does ‘cheating the little things’ makes ‘cheating the big things’ more likely?”

To which I would suggest the answer is probably yes as the LLM is not aware of the difference.

This suggests a route of little “white lies” is the start to the route of “black perfidy”.

Thus a “gateway” attack vector.

Clive Robinson •
[February 24, 2025 8:52 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html/#comment-443302)

@ Bruce,

Toward the bottom of the article we see,

> *“Google DeepMind’s AI safety chief Anca Dragan said **“we don’t necessarily have the tools today” to ensure AI systems will reliably follow human intentions**.”*

Nor I suspect will we ever…

“Why?”

Because “humans cheat” and have done for longer than we have records. Likewise we have tried to come up with tools/rules to stop humans cheating for as long. The result is we’ve failed and are failing worse than ever with humans.

If we can not “Police ourselves” perhaps we should start by asking,

“Why we can not?”

I suspect the reason is there is always those that no matter how black the perfidious behaviour might be there is some “advantage” or “good”…

Usually this “good” is only for a very small self entitled group, but they leverage that in an onward cycle of self entitlement at everyone elses expense.

I think we can see where certain people think they’ve crossed a tipping point and it does not look good for humanity.

Joe Bob •
[February 24, 2025 9:31 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html/#comment-443303)

Man “sports” include cheating as part of their rules. Using fouls in basketball, for example, is an important strategy to win a game.

We’ve all played Monopoly games where the banker would cheat and if caught, try to pay off whoever caught them stealing money.

If you want entities to follow the rules, make the conditions of the rules that any cheating causes immediate loss of the game.

Lars Skovlund •
[February 24, 2025 11:56 AM](https://www.schneier.com/blog/archives/2025/02/more-research-showing-ai-breaking-the-rules.html/#comment-443304)

Who gives an AI the ability to modify system files or run arbitrary code on the system (in that other paper mentioned on here)? The IT security community has been moving towards compartmentalizing these things for decades. It seems to me the simple solution is not allowing the AI to have such tools; it can’t innovate them on its own (but, as the papers show, it can certainly improve them if given the chance).

drew •
[February 24, 2025 12:04 PM...