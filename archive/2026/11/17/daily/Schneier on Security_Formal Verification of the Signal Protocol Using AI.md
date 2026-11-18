---
title: Formal Verification of the Signal Protocol Using AI
url: https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html
source: Schneier on Security
date: 2026-11-17
fetch_date: 2026-11-18T09:22:48.016594
---

# Formal Verification of the Signal Protocol Using AI

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

## Formal Verification of the Signal Protocol Using AI

[This](https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/) seems like a good thing:

> Google Deepmind researchers used agentic AI to mathematically prove, or “formally verify,” a number of the Signal protocol’s key cryptographic guarantees­a landmark development for the widely used cryptography and AI itself.
>
> Conducted as a sort of proof-of-concept project in just four weeks, the work is significant in two ways. It serves as further independent validation of the cryptography that protects massive quantities of the world’s communications on platforms like the Signal app, Google Messages, and WhatsApp. And it demonstrates Google DeepMind’s formal verification capabilities using a new AI framework called AlphaProof Code.
>
> […]
>
> The DeepMind analysis did not find any new vulnerabilities in the portions of the Signal protocol it looked at, but when the researchers used AlphaProof Code on older versions of Signal that contain known and long-fixed vulnerabilities, it correctly identified them and showed that the protocol could not be formally verified. The researchers are releasing the specification and proof they developed for the Signal protocol analysis to aid other formal verification work.

Alternate [link](https://archive.ph/BrmVv).

[Details](https://deepmind.google/blog/introducing-alphaproof-code/):

> First, our researchers collaborated with a mix of models to translate Signal’s security goals into formal mathematical specifications, with human experts reviewing every one. From there, agents powered by Gemini Carbon did the proofs, generating over six million lines of Lean, a computer language that mathematically proves the accuracy of code.
>
> Next, the agents audited the proof and highlighted areas that needed a second look by a human ­ just one percent of the codebase, a massive time savings. Because Lean automatically checks the rest, our experts could focus their review where human judgment matters most.

Technical [paper](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [protocols](https://www.schneier.com/tag/protocols/), [security analysis](https://www.schneier.com/tag/security-analysis/), [Signal](https://www.schneier.com/tag/signal/)

[Posted on November 17, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html) •
[8 Comments](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html#comments)

### Comments

dsanford0 •
[November 17, 2026 7:53 AM](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html/#comment-459708)

In the age of AI coding, where prompts and other obfuscated information may be embedded in code, I favor much more formal verification. Many programs are fairly simple finite-state machines, which should be easy to verify.

JG6 •
[November 17, 2026 8:40 AM](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html/#comment-459711)

“If you don’t have end-point security, you’ve got worse than nothing.”

Clive Robinson •
[November 17, 2026 8:51 AM](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html/#comment-459712)

Hmm,

Any one up for a long read,

> *“generating over six million lines of Lean, a computer language that mathematically proves the accuracy of code.
> “*

How long does it take you to read a “leisure read paperback” that is approximately 10,000 lines over 350 pages?

How about a basic undergrad type text book of similar size?

Who is going to read it all?

But then who is going to be able to take it all in?

And that is all before the $64,000 question about LLMs and the issues they have with things that were not in their training data…

Rontea •
[November 17, 2026 9:43 AM](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html/#comment-459713)

Validating the cryptographic guarantees behind tools like Signal, WhatsApp, and Google Messages is no small feat, and doing it in just four weeks demonstrates the potential impact on software assurance. That said, scaling this approach to full applications and large codebases will be the real challenge. High-assurance sectors—finance, government, defense—will watch closely to see if such AI-driven verification can become practical at scale without prohibitive cost or effort.

Clive Robinson •
[November 17, 2026 9:49 AM](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html/#comment-459714)

@ JG6,

With regards,

> “If you don’t have end-point security, you’ve got worse than nothing.”

Yup…

*“It’s easy to have a a strong link in an otherwise weak chain, do more harm than all the weak links combined.”*

I’ve always wondered why people only talk about the “strong links” but not the overall system.

Back when Signal and other supposedly “secure apps” came out I pointed out the problems with the “security end point” and the “communications end point” and how the OS allowed “end run attacks”, and effectively painted a target on your back…

It took a while for this to sink in with those who could think about it rationally, but many others either can not or chose not to think about it rationally.

The reasons are sadly,

1, Convenience of use.
2, Because others in their group use it.

And it goes wrong in many ways including some that became seriously embarrassing for those in Politics.

Now of course using “Signal” or other “supposedly secure messaging apps” is not really going to be secure any longer…

Because, Apple, Google and now Microsoft have built in “Client Side Scanning” into their OS’s in ways you can not avoid/prevent the “ET phone home to the mothership”.

All as part of the “Think of the Children” nonsense supposedly to catch CSAM. But now the CSS mechanism is in the OS expanding it to other things is in effect trivial…

People need to wake up to the fact that the “Anti-E2EE” game is over as long as the “they” can get at the “User Interface” that is “human usable” plaintext and send it back to the “they” over the “communications interface” that the OS suppliers do their best to stop you securing”.

It’s why I’ve said for quite some time that the “security end point” should be on a separate device beyond the device that has the “communications end point”.

I’ve described a way to have a secure endpoint by use of a hand cipher using just paper and pencil a couple of times on this blog…

Yet it won’t be used by people because,

**“It lacks ‘all in one, thought free’ convenience…”**

Which is why it is ...