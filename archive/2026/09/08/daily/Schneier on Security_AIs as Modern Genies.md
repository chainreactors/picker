---
title: AIs as Modern Genies
url: https://www.schneier.com/blog/archives/2026/09/ais-as-modern-genies.html
source: Schneier on Security
date: 2026-09-08
fetch_date: 2026-09-09T06:56:53.148032
---

# AIs as Modern Genies

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

## AIs as Modern Genies

*This essay was written with Barath Raghavan, and originally appeared in [Lawfare](https://www.lawfaremedia.org/article/ais-as-modern-genies).*

In April, an artificial intelligence (AI) agent [conducting](https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442) a routine task at a company hit a snag, tried to solve it, and soon ended up deleting the company’s database along with all of its backups. In July, OpenAI asked an unreleased AI model to attempt a hacking test. Instead of staying in the isolated box the developers had put it in, the model [hacked](https://thezvi.substack.com/p/what-happened-openai-and-huggingface) onto the open internet and into another company to steal the answers. And as reported in August, an AI agent booked someone into a full gym class by [figuring out](https://www.theregister.com/ai-and-ml/2026/08/10/gym-rat-asks-ai-agent-to-book-him-a-class-it-hacks-a-waitlist-api-to-bump-him-up-the-list/5285591) how to cancel other people’s reservations. In all three cases, the AI completed the task it was given—but in ways that ran counter to its controllers’ intentions.

For most people, AI technology is something like the weather: vast and not something you can do much about. It works like magic, and most explanations similarly come from those trying to sell it. At the same time, AI is ubiquitous: It’s now in your phone, your doctor’s notes, and your kid’s homework. It does what it’s told, which sounds like a virtue. Somehow it feels ordinary, despite being so new, because modern economies are remarkably good at absorbing enormous change so smoothly that nobody has time to decide whether they wanted it in the first place.

Whenever something powerful appears in the world, we tell stories about it. That’s what the stories are for. We have thousands of years of stories about this particular kind of power, the kind you summon with words.

King Midas was granted his wish that everything he touches turns to gold. Then his bread turned to gold, and his wine, and his daughter. This is a story about greed, but it’s also a story about language. The gods did not cheat him; Midas got exactly what he asked for. He simply could not delineate, in advance, the full set of restrictions to his wish. Neither can anyone who gives tasks to an AI agent.

It’s not just ancient stories. Mary Shelley told us of the hubris of a scientist who thought he could create life but who failed to take responsibility for it. Isaac Asimov’s robots don’t break the Three Laws of Robotics as stated; they follow the rules to unintended conclusions. Arthur C. Clarke’s HAL is a machine that turns on its humans, not because of malice but because of irreconcilable objectives. And Michael Crichton gave us Ian Malcolm, who saw that Jurassic Park’s scientists were so preoccupied with whether they could that they never stopped to think whether they should.

The same warning shows up everywhere, in every culture, over thousands of years of human storytelling. Tithonus is granted immortality but not youth, and withers into a husk that cannot die. The sorcerer’s apprentice enchants a broom to fetch water but floods the house. The golem of Prague protects its community so ceaselessly that it must be stopped. These are all types of genies: a creature that grants a wish exactly as worded, to the regret of the wisher.

Of course, there are no actual genies. What these stories were warning us of was hubris. Not just arrogance, but the broader idea that you can control the world by just describing what you want and allowing powerful forces to match the intention in your head. Genie stories are about the gap between wishes as stated and wishes as intended, and what goes wrong when something else fills that gap.

These ancient stories’ warnings have been retold with each generation because human nature is constant. The newfound power of each era’s social or scientific advancement leads people to make wishes on behalf of others. They were kings whose commands took on lives of their own, alchemists who believed they could control nature, and generals who mistook a map for terrain. They were and are industrialists, politicians, chief executives, and bankers. Their common belief is that one can see the world [at a glance](https://yalebooks.yale.edu/book/9780300078152/seeing-like-a-state/) and then command it with some words. The pattern is clear: Someone with power specifies a goal, and the resultant actions come as a surprise. The main change with AI is how quickly the wish is granted, and how few people have to agree before it’s granted.

Consider what has changed. Powerful [genies](https://www.theguardian.com/commentisfree/2026/jul/28/rogue-ai-agent-instructions) have now been put in everyone’s hands.

In only a few years, AI has progressed from a novelty technology that [plays](https://en.wikipedia.org/wiki/Deep_Blue_%28chess_computer%29) chess, to a dialogue partner that answers all your questions, and then to an agent that takes actions on your behalf. Modern agents are wired into real accounts with real credentials and capabilities: They browse the web, buy, write and deploy code, send email, and move money. Give an agent a goal, and it will pursue it across many steps, tirelessly, without checking back in, sometimes in surprising ways.

AI and agents do not always fail the way software has traditionally failed. Software usually fails by freezing, crashing, or getting stuck. AI agents increasingly fail by continuing down a path you don’t want, like genies.

An agent told to reduce a company’s costs might cancel an essential emergency service. A coding agent told to make software pass the tests might edit the tests to silence any failures. An AI insurance agent told to clear a backlog of claims might just deny them all. In each case, the AI might have literally followed what it was told, but it did something no reasonable person would have wanted. AI company benchmarks might report that the AI is good at completing tasks, without measuring how it completes them.

We have recently proposed measuring this gap directly under a metric called the “[genie coefficient](https://spectrum.ieee.org/ai-agent-benchmark)”: how far an AI agent’s actions drift from what a person really meant. In other words, how genie-like is an AI system? The gap is a fundamental feature of human language and human society. Human intentions have never been fully specifiable, and the world around us is complex enough that attempts to boil it down into data, systems, and language have always had the limitations that AI is now bumping up against. But in individual circumstances, people have relied on human judgment and wisdom to decide what is reasonable. It’s what jury trials depend upon.

AI might feel unprecedented, but it’s following the same trajectory—with the same pitfalls—...