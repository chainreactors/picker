---
title: Microsoft Takes Legal Action Against AI “Hacking as a Service” Scheme
url: https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html
source: Schneier on Security
date: 2025-01-14
fetch_date: 2025-10-06T20:15:42.433147
---

# Microsoft Takes Legal Action Against AI “Hacking as a Service” Scheme

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

## Microsoft Takes Legal Action Against AI “Hacking as a Service” Scheme

Not sure this will matter in the end, but it’s a [positive move](https://arstechnica.com/security/2025/01/microsoft-sues-service-for-creating-illicit-content-with-its-ai-platform/):

> Microsoft is accusing three individuals of running a “hacking-as-a-service” scheme that was designed to allow the creation of harmful and illicit content using the company’s platform for AI-generated content.
>
> The foreign-based defendants developed tools specifically designed to bypass safety guardrails Microsoft has erected to prevent the creation of harmful content through its generative AI services, [said](https://blogs.microsoft.com/on-the-issues/2025/01/10/taking-legal-action-to-protect-the-public-from-abusive-ai-generated-content/) Steven Masada, the assistant general counsel for Microsoft’s Digital Crimes Unit. They then compromised the legitimate accounts of paying customers. They combined those two things to create a fee-based platform people could use.

It was a sophisticated scheme:

> The service contained a proxy server that relayed traffic between its customers and the servers providing Microsoft’s AI services, the suit alleged. Among other things, the proxy service used undocumented Microsoft network application programming interfaces (APIs) to communicate with the company’s Azure computers. The resulting requests were designed to mimic legitimate Azure OpenAPI Service API requests and used compromised API keys to authenticate them.

Slashdot [thread](https://yro.slashdot.org/story/25/01/11/073210/foreign-cybercriminals-bypassed-microsofts-ai-guardrails-lawsuit-alleges).

Tags: [AI](https://www.schneier.com/tag/ai/), [hacking](https://www.schneier.com/tag/hacking/), [LLM](https://www.schneier.com/tag/llm/), [Microsoft](https://www.schneier.com/tag/microsoft/)

[Posted on January 13, 2025 at 7:01 AM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html#comments)

### Comments

Kukumix •
[January 13, 2025 7:17 AM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442463)

Is Microsoft masking here its own mistakes?

“They then compromised the legitimate accounts of paying customers” – we have seen in the past multiple deep security holes in Azure. Have they exploited those?

“Among other things, the proxy service used undocumented Microsoft network application programming interfaces (APIs) to communicate with the company’s Azure computers” – sounds like another security hole in Microsoft.

Clive Robinson •
[January 13, 2025 9:29 AM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442466)

@ Bruce, ALL,

In another “news source”,

<https://arstechnica.com/security/2025/01/microsoft-sues-service-for-creating-illicit-content-with-its-ai-platform/>

Dan Goodin says,

> *“All 10 defendants were named John Doe because Microsoft doesn’t know their identity.”*

And goes on to say seven of them were customers of the illicit service.

And more importantly, it appears access credentials were compromised. Microsoft is not saying how or on who’s servers the credentials were stored.

Another article indicates Microsoft have been busy in the courts getting permission to raid and grab a server…

Me •
[January 13, 2025 11:30 AM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442467)

Hopefully this isn’t seen as an alternative to actually fixing the weakness in their security.

Steve •
[January 13, 2025 5:55 PM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442471)

From the story:

> Microsoft is also suing seven individuals it says were customers of the service. All 10 defendants were named John Doe because Microsoft doesn’t know their identity.

In other words, lawsuit as performance art.

ResearcherZero •
[January 14, 2025 1:44 AM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442478)

@Kukumix

Microsoft forbids doing things with it’s products it hoped would not happen, that it never imagined would happen, or that are completely possible but should not be done.

Microsoft would never make a mistake by bringing products to market that are full of gaping security flaws. It’s the users who were non compliant with the Microsoft law. If for example a foreign government was to break into Microsoft’s network and steal tokens for it’s APIs, or compromise the credentials for accounts, it would totally be the user’s fault.

ResearcherZero •
[January 14, 2025 2:00 AM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442479)

Generative AI and LLMs are like a small child, which you have placed in a forest, given a box of matches (in the middle of summer), then kindly asked to please not ignite the forest. Clearly the child’s fault, and not a decision a responsible adult would make.

Silicon Valley is fortunately situated a long way from any side-effects of disruption.

Anonymous •
[January 14, 2025 8:01 AM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442483)

What sort of “illicit” content did they create exactly?

I can’t see how any AI generated content could be more “harmful” than, say, photoshopped content, animated content, content researched normally, etc.

The only thing they did wrong that I can see was compromising the accounts of existing uninvolved customers.

Who? •
[January 15, 2025 12:40 PM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442510)

AI systems need to be trained, just in the same way young childs must.

The difference is that childs go to school, while AI systems are provided with access to anything available on the Internet. Go figure… and then we complain that LLMs have hallucinations…

Who? •
[January 15, 2025 1:09 PM](https://www.schneier.com/blog/archives/2025/01/microsoft-takes-legal-action-against-ai-hacking-as-a-service-scheme.html/#comment-442511)

> *“All 10 defendants were named John Doe because Microsoft doesn’t know their identity.”*

So defendants must be the group “Anonymous.” On the bright side, at least they are not accusing the real owners of the compromised API keys. Undocumented APIs are not the problem here, we cannot depend on these APIs remain hidden for...