---
title: Cybersecurity in the Age of Instant Software
url: https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html
source: Schneier on Security
date: 2026-04-07
fetch_date: 2026-04-08T04:38:59.622317
---

# Cybersecurity in the Age of Instant Software

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

## Cybersecurity in the Age of Instant Software

AI is rapidly changing how software is written, deployed, and used. Trends point to a future where AIs can write custom software quickly and easily: “instant software.” Taken to an extreme, it might become easier for a user to have an AI write an application on demand—a spreadsheet, for example—and delete it when you’re done using it than to buy one commercially. Future systems could include a mix: both traditional long-term software and ephemeral instant software that is constantly being written, deployed, modified, and deleted.

AI is changing cybersecurity as well. In particular, AI systems are getting better at finding and patching vulnerabilities in code. This has implications for both attackers and defenders, depending on the ways this and related technologies improve.

In this essay, I want to take an optimistic view of AI’s progress, and to speculate what AI-dominated cybersecurity in an age of instant software might look like. There are a number of unknowns that will factor into how the arms race between attacker and defender might play out.

## How flaw discovery might work

On the attacker side, the ability of AIs to automatically find and exploit vulnerabilities has increased dramatically over the past few months. We are already seeing both [government](https://www.anthropic.com/news/disrupting-AI-espionage) and [criminal](https://www.eset.com/us/about/newsroom/research/eset-discovers-promptlock-the-first-ai-powered-ransomware/) hackers using AI to attack systems. The exploitation part is critical here, because it gives an unsophisticated attacker capabilities far beyond their understanding. As AIs get better, expect more attackers to automate their attacks using AI. And as individuals and organizations can increasingly run powerful AI models locally, AI companies [monitoring and disrupting](https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/) malicious AI use will become increasingly irrelevant.

Expect open-source software, including open-source libraries incorporated in proprietary software, to be the most targeted, because vulnerabilities are easier to find in source code. Unknown No. 1 is how well AI vulnerability discovery tools will work against closed-source commercial software packages. I believe they will soon be good enough to find vulnerabilities just by analyzing a copy of a shipped product, without access to the source code. If that’s true, commercial software will be vulnerable as well.

Particularly vulnerable will be software in IoT devices: things like internet-connected cars, refrigerators, and security cameras. Also industrial IoT software in our internet-connected power grid, oil refineries and pipelines, chemical plants, and so on. IoT software tends to be of much lower quality, and industrial IoT software tends to be legacy.

Instant software is differently vulnerable. It’s not mass market. It’s created for a particular person, organization, or network. The attacker generally won’t have access to any code to analyze, which makes it less likely to be exploited by external attackers. If it’s ephemeral, any vulnerabilities will have a short lifetime. But lots of instant software will live on networks for a long time. And if it gets uploaded to shared tool libraries, attackers will be able to download and analyze that code.

All of this points to a future where AIs will become powerful tools of cyberattack, able to automatically find and exploit vulnerabilities in systems worldwide.

## Automating patch creation

But that’s just half of the arms race. Defenders get to use AI, too. These same AI vulnerability-finding technologies are even more valuable for defense. When the defensive side finds an exploitable vulnerability, it can patch the code and deny it to attackers forever.

How this works in practice depends on another related capability: the ability of AIs to patch vulnerable software, which is closely related to their ability to write secure code in the first place.

AIs are not very good at this today; the instant software that AIs create is generally filled with vulnerabilities, both because AIs write insecure code and because the people vibe coding don’t understand security. OpenClaw is a [good example](https://blog.barrack.ai/openclaw-security-vulnerabilities-2026/) of this.

Unknown No. 2 is how much better AIs will get at writing secure code. The fact that they’re trained on massive corpuses of poorly written and insecure code is a handicap, but they are getting better. If they can reliably write vulnerability-free code, it would be an enormous advantage for the defender. And AI-based vulnerability-finding makes it [easier](https://sergejepp.substack.com/p/winning-the-ai-cyber-race-verifiability) for an AI to train on writing secure code.

We can [envision](https://www.csoonline.com/article/4069075/autonomous-ai-hacking-and-the-future-of-cybersecurity.html) a future where AI tools that find and patch vulnerabilities are part of the typical software development process. We can’t say that the code would be vulnerability-free—that’s an impossible goal—but it could be without any easily findable vulnerabilities. If the technology got really good, the code could become essentially vulnerability-free.

## Patching lags and legacy software

For new software—both commercial and instant—this future favors the defender. For commercial and conventional open-source software, it’s not that simple. Right now, the world is filled with legacy software. Much of it—like IoT device software—has no dedicated security team to update it. Sometimes it is incapable of being patched. Just as it’s harder for AIs to find vulnerabilities when they don’t have access to the source code, it’s harder for AIs to patch software when they are not embedded in the development process.

I’m not as confident that AI systems will be able to patch vulnerabilities as easily as they can find them, because patching often requires more holistic testing and understanding. That’s Unknown No. 3: how quickly AIs will be able to create reliable software updates for the vulnerabilities they find, and how quickly customers can update their systems.

Today, there is a time lag between when a vendor issues a patch and customers install that update. That time lag is even longer for large organizational software; the risk of an update breaking the underlying software system is just too great for organizations to roll out updates without testing them first. But if AI can help speed up that process, by writing patches faster and more reliably, and by testing them in some AI-generated twin environment, the advantage goes to the defender. If not, the attacker will still have a window to attack systems until a vulnerability is patched.

## Toward self-healing

In a truly optimistic future, we can imagine a self-healing network. AI a...