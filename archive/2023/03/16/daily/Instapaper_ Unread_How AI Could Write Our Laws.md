---
title: How AI Could Write Our Laws
url: https://www.schneier.com/blog/archives/2023/03/how-ai-could-write-our-laws.html
source: Instapaper: Unread
date: 2023-03-16
fetch_date: 2025-10-04T09:48:02.022138
---

# How AI Could Write Our Laws

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

## How AI Could Write Our Laws

Nearly [90%](https://www.opensecrets.org/federal-lobbying/business-labor-ideological) of the multibillion-dollar federal lobbying apparatus in the United States serves corporate interests. In some cases, the objective of that money is obvious. Google [pours](https://www.opensecrets.org/news/2023/01/google-continued-to-ramp-up-federal-lobbying-spending-before-doj-filed-second-antitrust-lawsuit) millions into lobbying on bills related to antitrust regulation. Big energy companies expect [action](https://www.citizen.org/article/big-oils-capitol-hill-allies/) whenever there is a move to end drilling leases for federal lands, in exchange for the tens of millions they contribute to congressional reelection campaigns.

But lobbying strategies are not always so blunt, and the interests involved are not always so obvious. [Consider, for example, a 2013](https://www.forrester.com/blogs/10-06-14-office_2010_will_continue_to_succeed_with_consumers/) [Massachusetts bill](https://malegislature.gov/Bills/188/H331) that tried to restrict the commercial use of data collected from K-12 students using services accessed via the internet. The bill [appealed](https://www.lowellsun.com/2013/06/27/privacy-bill-seeks-to-protect-students-as-data-shifts-to-the-cloud-2/) to many privacy-conscious education advocates, and appropriately so. But behind the justification of protecting students lay a market-altering policy: the bill was introduced at the [behest](https://www.theverge.com/2013/3/7/4074136/microsoft-backs-privacy-bill-tries-to-keep-google-apps-out-of-classroom) of Microsoft lobbyists, in an effort to exclude Google Docs from classrooms.

What would happen if such legal-but-sneaky strategies for tilting the rules in favor of one group over another become more widespread and effective? We can see hints of an answer in the remarkable pace at which artificial-intelligence tools for everything from [writing](https://arstechnica.com/information-technology/2023/01/pivot-to-chatgpt-buzzfeed-preps-for-ai-written-content-while-cnet-fumbles/) to [graphic design](https://www.engadget.com/microsoft-designer-dall-e-2-annouced-140007501.html) are being developed and improved. And the unavoidable conclusion is that AI will make lobbying more guileful, and perhaps more successful.

It turns out there is a natural opening for this technology: microlegislation.

“Microlegislation” is a term for small pieces of proposed law that cater—sometimes unexpectedly—to narrow interests. Political scientist Amy McKay coined the term. She [studied](https://onlinelibrary.wiley.com/doi/full/10.1111/lsq.12266) the 564 amendments to the Affordable Care Act (“Obamacare”) considered by the Senate Finance Committee in 2009, as well as the positions of 866 lobbying groups and their campaign contributions. She documented instances where lobbyist comments—on health-care research, vaccine services, and other provisions—were translated directly into microlegislation in the form of amendments. And she found that those groups’ financial contributions to specific senators on the committee increased the amendments’ chances of passing.

Her finding that lobbying works was no surprise. More important, McKay’s work demonstrated that computer models can predict the likely fate of proposed legislative amendments, as well as the paths by which lobbyists can most effectively secure their desired outcomes. And that turns out to be a critical piece of creating an AI lobbyist.

Lobbying has long been part of the give-and-take among human policymakers and advocates working to balance their competing interests. The danger of microlegislation—a danger greatly exacerbated by AI—is that it can be used in a way that makes it difficult to figure out who the legislation truly benefits.

Another word for a strategy like this is a “hack.” [Hacks](https://www.schneier.com/books/a-hackers-mind/) follow the rules of a system but subvert their intent. Hacking is often associated with computer systems, but the concept is also applicable to social systems like financial markets, tax codes, and legislative processes.

While [the](https://www.nytimes.com/2023/01/15/opinion/ai-chatgpt-lobbying-democracy.html) [idea](https://www.belfercenter.org/publication/we-dont-need-reinvent-our-democracy-save-it-ai) of monied interests incorporating AI assistive technologies into their lobbying remains hypothetical, [specific](https://arxiv.org/abs/2110.09231) machine-learning technologies exist today that would enable them to do so. We should expect these techniques to get better and their utilization to grow, just as we’ve seen in so many other domains.

Here’s how it might work.

### Crafting an AI microlegislator

To make microlegislation, machine-learning systems must be able to uncover the smallest modification that could be made to a bill or existing law that would make the biggest impact on a narrow interest.

There are three basic challenges involved. First, you must create a *policy proposal—*small suggested changes to legal text—and anticipate whether or not a human reader would recognize the alteration as substantive. This is important; a change that isn’t detectable is more likely to pass without controversy. Second, you need to do an *impact assessment* to project the implications of that change for the short- or long-range financial interests of companies. Third, you need a *lobbying strategizer* to identify what levers of power to pull to get the best proposal into law.

Existing AI tools can tackle all three of these.

The first step, the *policy proposal*, leverages the core function of [generative AI](https://hbr.org/2022/11/how-generative-ai-is-changing-creative-work). Large language models, the sort that have been used for general-purpose chatbots such as ChatGPT, can easily be adapted to write like a native in different specialized domains after seeing a relatively small number of examples. This process is called [fine-tuning](https://towardsdatascience.com/fine-tuning-for-domain-adaptation-in-nlp-c47def356fd6). For example, a model “pre-trained” on a large library of generic text samples from books and the internet can be “fine-tuned” to work [effectively](https://arxiv.org/pdf/2109.07460.pdf) on medical literature, computer science papers, and product reviews.

Given this flexibility and capacity for adaptation, a large language model could be fine-tuned to produce draft legislative texts, given a data set of previously offered amendments and the bills they were associated with. Training data is available. At the federal level, it’s provided by the [US Government Publishing Office](https://github.com/usgpo/bill-status), and there are already [tools](https://github.com/unitedstates/congress) for downloading and interacting with it. Most other jurisdictions provide similar data feeds, and there are even convenient [assemblages](https://opensta...