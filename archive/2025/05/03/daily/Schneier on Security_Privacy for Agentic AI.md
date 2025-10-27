---
title: Privacy for Agentic AI
url: https://www.schneier.com/blog/archives/2025/05/privacy-for-agentic-ai.html
source: Schneier on Security
date: 2025-05-03
fetch_date: 2025-10-06T22:29:37.938523
---

# Privacy for Agentic AI

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

## Privacy for Agentic AI

Sooner or later, it’s going to happen. AI systems will start acting as agents, doing things on our behalf with some degree of autonomy. I think it’s worth thinking about the security of that now, while its still a nascent idea.

In 2019, I [joined](https://www.schneier.com/blog/archives/2020/02/inrupt_tim_bern.html) Inrupt, a company that is commercializing Tim Berners-Lee’s open protocol for distributed data ownership. We are working on a [digital wallet](https://www.schneier.com/blog/archives/2024/07/data-wallets-using-the-solid-protocol.html) that can make use of AI in this way. (We used to call it an “active wallet.” Now we’re calling it an “agentic wallet.”)

I talked [about](https://www.instagram.com/rsaconference/p/DGv4Yf5SCsw/) [this](https://www.rsaconference.com/library/video/2025-keynote-preview-bruce-schneier) a bit at the [RSA Conference](https://www.rsaconference.com/) earlier this week, in my keynote talk about AI and trust. Any useful AI assistant is going to require a level of access—and therefore trust—that rivals what we currently our email provider, social network, or smartphone.

> This Active Wallet is an example of an AI assistant. It’ll combine personal information about you, transactional data that you are a party to, and general information about the world. And use that to answer questions, make predictions, and ultimately act on your behalf. We have demos of this running right now. At least in its early stages. Making it work is going require an extraordinary amount of trust in the system. This requires integrity. Which is why we’re building protections in from the beginning.

Visa is also thinking about this. It [just](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21361.html) [announced](https://corporate.visa.com/en/products/intelligent-commerce.html) a protocol that uses AI to help people make purchasing decisions.

I like Visa’s approach because it’s an AI-agnostic standard. I worry a lot about lock-in and monopolization of this space, so anything that lets people easily switch between AI models is good. And I like that Visa is working with Inrupt so that the data is decentralized as well. Here’s [our announcement](https://www.inrupt.com/blog/standards-for-agentic-commerce-visas-bold-move) about its announcement:

> This isn’t a new relationship—we’ve been working together for over two years. We’ve conducted a successful POC and now we’re standing up a sandbox inside Visa so merchants, financial institutions and LLM providers can test our Agentic Wallets alongside the rest of Visa’s suite of Intelligent Commerce APIs.
>
> For that matter, we welcome any other company that wants to engage in the world of personal, consented Agentic Commerce to come work with us as well.

I joined Inrupt years ago because I thought that Solid could do for personal data what HTML did for published information. I liked that the protocol was an open standard, and that it distributed data instead of centralizing it. AI agents need decentralized data. “Wallet” is a good metaphor for personal data stores. I’m hoping this is another step towards adoption.

Tags: [data privacy](https://www.schneier.com/tag/data-privacy/), [Inrupt](https://www.schneier.com/tag/inrupt/), [privacy](https://www.schneier.com/tag/privacy/), [Schneier news](https://www.schneier.com/tag/schneier-news/)

[Posted on May 2, 2025 at 2:04 PM](https://www.schneier.com/blog/archives/2025/05/privacy-for-agentic-ai.html) •
[14 Comments](https://www.schneier.com/blog/archives/2025/05/privacy-for-agentic-ai.html#comments)

### Comments

ResearcherZero •
[May 3, 2025 3:03 AM](https://www.schneier.com/blog/archives/2025/05/privacy-for-agentic-ai.html/#comment-444986)

Anthony Jancso, a former Palantir employee, is recruiting and reaching out to Palantir pals for an AI agent project. Potential recruits would not require a security clearance.

It really does look like America will become the United States of Surveillance. One with plenty of contracts for private surveillance companies and little privacy or security.

‘https://www.wired.com/story/doge-recruiter-ai-agents-palantir-clown-emoji/

DOGE is racing to replace thousands of government employees with AI agents.

In order to do this work an undergraduate is rewriting regulations using AI tools.
<https://www.independent.co.uk/news/world/americas/us-politics/doge-staffer-college-ai-rewrite-regulations-b2743052.html>

DOGE is also using AI for surveillance purposes, raising concerns over data ingestion.
<https://www.reuters.com/technology/artificial-intelligence/musks-doge-using-ai-snoop-us-federal-workers-sources-say-2025-04-08/>

Alessandro •
[May 3, 2025 5:28 AM](https://www.schneier.com/blog/archives/2025/05/privacy-for-agentic-ai.html/#comment-444989)

Hi, I am following Solid since quite some time, but I am not sure to understand how these Agentic Wallet works. Does it mean that, somehow, the Wallet (i.e. connected to a Solid pod, I guess?) will contain data about users transactions online (e.g. purchases, etc..)? But that would mean that all websites would have to interact with the Solid pods/Wallet?

Sorry for the very – probably silly – question. I love the idea of Solid, and I am very curious.
Thanks!

Clive Robinson •
[May 3, 2025 12:28 PM](https://www.schneier.com/blog/archives/2025/05/privacy-for-agentic-ai.html/#comment-444995)

@ Bruce, ALL,

Your opening lines,

> “Sooner or later, it’s going to happen. AI systems will start acting as agents, doing things on our behalf with some degree of autonomy. I think it’s worth thinking about the security of that now, while its still a nascent idea.”

Is too late, as we are well beyonf “nascent ideas”, that is it’s already happened and if the 1990’s issues are anything to go by it’s going to be a disaster and nightmare combined

What will be new however is the “control of people” by “surveillance legislation”.

Back in the 1990’s when the Internet as the “World Wide Web” was nascent the “adult things” that were getting US Politicos panties in a wad was what was jokingly called “the 3 Gs” (to rhyme with “The Bee Gees”).

Standing for “Girls, Gambling, and Games” was a political nightmare especially in US Red-States and a whole load of authoritarian nation states.

Way to many activists that had nothing better to do in life put saucepans and similar on their heads and went of “tilting at windmills” to slay the devils that they claimed others should be protected from weather they wanted to be protected or not, because these “lids” knew best about how people should behave.

As a rule, the agitating types were ultra conservative, lacking in worldly experience and oft a certain type of religious that is strongly patriarchal. Yet those given to actually being patriarchal leaders making political milage, all to often turned out to be the types children really should be protected fr...